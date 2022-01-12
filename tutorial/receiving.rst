Receiving GCNs
==============

Next, we'll write a GCN handler function that we want PyGCN to call every time
it receives a GCN notice. We :term:`decorate <decorator>` the handler with
``@gcn.handlers.include_notice_types`` to specify that we only want to process
certain GCN notice types (``LVC_PRELIMINARY``, ``LVC_INITIAL``, and
``LVC_UDPATE``).

Events come in two very general flavors: 'CBC' for compact binary coalescence
candidates detected by matched filtering, and 'Burst' for candidates detected
by model-independent methods. Your handler can take different actions based on
this. The example below will handle only 'CBC' events.

Using Avro with Kafka
=====================

Avro alerts use serialized data based on schema to send and receive alerts. The different types of alerts are "EarlyWarning", "Preliminary", "Initial", "Update", and "Retraction". The JSON schema below is a representation of the GW alerts that will be serialized into an AVRO file.

..testcode::
    [
  {
    "name": "AlertType",
    "namespace": "igwn.alerts",
    "type": "enum",
    "symbols": ["EarlyWarning", "Preliminary", "Initial", "Update", "Retraction"]
  },
  {
    "name": "AlertChanged",
    "namespace": "igwn.alerts",
    "type": "enum",
    "symbols": [
      "NEW_EVENT",
      "EVENT_RETRACTED",
      "EVENT_CONFIRMED",
      "EVENT_UPDATED",
      "SKYMAP_UPDATED",
      "CLASSIFICATION_UPDATED",
      "PROPERTIES_UPDATED"
    ]
  },
      {
    "name": "EventInfo",
    "namespace": "igwn.alerts",
    "type": "record",
    "fields": [
      {"name": "time", "type": "string"},
      {"name": "far", "type": "double"},
      {"name": "instruments", "type": {"type": "array", "items": "string", "default": []}},
      {"name": "group", "type": "string"},
      {"name": "pipeline", "type": "string"},
      {"name": "search", "type": "string"},
      {"name": "classification", "type": {"type": "map", "values": "double", "default": {}}},
      {"name": "properties", "type": {"type": "map", "values": "double", "default": {}}},
      {"name": "skymap", "type": "bytes"}
    ]
  },
  {
    "name": "Alert",
    "namespace": "igwn.alerts",
    "type": "record",
    "fields": [
      {"name": "author", "type": "string"},
      {"name": "alert_type", "type": "AlertType"},
      {"name": "time_created", "type": "string"},
      {"name": "superevent_id", "type": "string"},
      {"name": "is_public", "type": "boolean"},
      {"name": "is_injection", "type": "boolean"},
      {"name": "changed", "type": "AlertChanged"},
      {"name": "event", "type": ["null", "EventInfo"]},
      {"name": "urls", "type": {"type": "map", "values": "string", "default": {}}},
      {"name": "event_revision", "type": "int"},
      {"name": "schema_version", "type": "int"}
    ]
  }
 ]


In order to send and receive alerts you will need Docker running on your machine. To start the Docker container run the following command:
docker run -it --rm --hostname localhost -p 9092:9092 scimma/server:latest --noSecurity
 
Then, download and execute the sample scripts below for sending and receiving alerts.
python send_alerts.py
.. literalinclude:: _static/send_alerts.py
         :language: python

python receive_alerts.py
.. literalinclude:: _static/receive_alerts.py
         :language: python
 
Which should yield the following  message:
 
{'author': 'LIGO Scientific Collaboration and Virgo Collaboration', 'alert_type': 'Update', 'time_created': '2018-11-01T22:36:25', 'superevent_id': 'MS181101ab', 'is_public': True, 'is_injection': False, 'changed': 'SKYMAP_UPDATED', 'event': {'time': '2018-11-01T22:22:46.654437', 'far': 9.11069936486e-14, 'instruments': ['H1', 'L1', 'V1'], 'group': 'CBC', 'pipeline': 'gstlal', 'search': 'MDC', 'classification': {'BNS': 0.95, 'NSBH': 0.01, 'BBH': 0.03, 'Terrestrial': 0.01}, 'properties': {'HasNS': 0.95, 'HasRemnant': 0.91}, 'skymap': None}, 'external_coinc': None, 'urls': {'gracedb': 'https://example.org/superevents/MS181101ab/view/'}, 'event_revision': 4, 'api_version': 1}
 
This demonstrates generating an alert with send_alerts.py, then receiving and reading the alert with receive_alerts.py.


.. important::
   Note that mock or 'test' observations are denoted by the ``role="test"``
   VOEvent attribute. Alerts resulting from real LIGO/Virgo science data will
   always have ``role="observation"``. The sample code below will respond
   **only** to 'test' events. When preparing for actual observations, you
   **must remember to switch to 'observation' events**.

.. note::
   Observe in the example below that we do not have to explicitly download the
   FITS file because the :func:`hp.read_map() <healpy.fitsfunc.read_map>`
   function works with either URLs or filenames. However, you could download
   and save the FITS file in order to save it locally using
   :func:`astropy.utils.data.download_file`, :func:`requests.get`,
   :func:`urllib.request.urlopen`, or even curl_.

The following basic handler function will parse out the URL of
the FITS file, download it, and extract the probability sky map:

.. testcode::

    import gcn
    import healpy as hp

    # Function to call every time a GCN is received.
    # Run only for notices of type
    # LVC_PRELIMINARY, LVC_INITIAL, LVC_UPDATE, or LVC_RETRACTION.
    @gcn.handlers.include_notice_types(
        gcn.notice_types.LVC_PRELIMINARY,
        gcn.notice_types.LVC_INITIAL,
        gcn.notice_types.LVC_UPDATE,
        gcn.notice_types.LVC_RETRACTION)
    def process_gcn(payload, root):
        # Respond only to 'test' events.
        # VERY IMPORTANT! Replace with the following code
        # to respond to only real 'observation' events.
        # if root.attrib['role'] != 'observation':
        #    return
        if root.attrib['role'] != 'test':
            return

        # Read all of the VOEvent parameters from the "What" section.
        params = {elem.attrib['name']:
                  elem.attrib['value']
                  for elem in root.iterfind('.//Param')}

        if params['AlertType'] == 'Retraction':
            print(params['GraceID'], 'was retracted')
            return

        # Respond only to 'CBC' events. Change 'CBC' to 'Burst'
        # to respond to only unmodeled burst events.
        if params['Group'] != 'CBC':
            return

        # Print all parameters.
        for key, value in params.items():
            print(key, '=', value)

        if 'skymap_fits' in params:
            # Read the HEALPix sky map and the FITS header.
            skymap, header = hp.read_map(params['skymap_fits'],
                                         h=True, verbose=False)
            header = dict(header)

            # Print some values from the FITS header.
            print('Distance =', header['DISTMEAN'], '+/-', header['DISTSTD'])

Listen for GCNs
---------------

Now, we will start the VOEvent client to listen for GCNs using the
``gcn.listen`` function. By default, this will connect to the anonymous, public
GCN server. You just need to tell ``gcn.listen`` what function to call whenever
it receives an GCN; in this example, that is the ``process_gcn`` handler that
we defined above.

::

    # Listen for GCNs until the program is interrupted
    # (killed or interrupted with control-C).
    gcn.listen(handler=process_gcn)

When you run this script you should receive a sample LIGO/Virgo GCN Notice
every hour. For each event received it will print output that looks like what
is shown in the :ref:`offline-testing` example below.

.. note::
   ``gcn.listen`` will try to automatically reconnect if the network connection
   is ever broken.

.. _offline-testing:

Offline Testing
---------------

Sometimes it is convenient to be able to explicitly call the GCN handler with a
sample input, rather than waiting for the next broadcast of a sample alert. You
can download the `example GCN notices <../content.html#examples>`_ from this
documentation and pass it into your GCN handler at any time. First, download
the sample GCN notice:

.. code-block:: shell-session

    $ curl -O https://emfollow.docs.ligo.org/userguide/_static/MS181101ab-2-Preliminary.xml

Then you can manually invoke your GCN handler using this Python code:

.. testsetup::

    import os
    import unittest.mock
    import urllib.parse
    from urllib.request import urlopen, Request

    old_dir = os.getcwd()
    os.chdir('_static')

    def patched_urlopen(url, *args, **kwargs):
        new_url = url
        if isinstance(new_url, Request):
            new_url = new_url.full_url
        parsed_url = urllib.parse.urlparse(new_url)
        dirname, basename = os.path.split(parsed_url.path)
        if parsed_url.netloc != 'emfollow.docs.ligo.org' \
                or dirname != '/userguide/_static':
            return urlopen(url, *args, **kwargs)
        return urlopen('file:{}'.format(basename), 'rb')

    patcher = unittest.mock.patch('urllib.request.urlopen', patched_urlopen)
    patcher.start()

.. testcode::

    import lxml.etree
    payload = open('MS181101ab-2-Preliminary.xml', 'rb').read()
    root = lxml.etree.fromstring(payload)
    process_gcn(payload, root)

Upon running this, you should see:

.. testoutput::

    Packet_Type = 150
    internal = 0
    Pkt_Ser_Num = 2
    GraceID = MS181101ab
    AlertType = Preliminary
    HardwareInj = 0
    OpenAlert = 1
    EventPage = https://example.org/superevents/MS181101ab/view/
    Instruments = H1,L1,V1
    FAR = 9.11069936486e-14
    Group = CBC
    Pipeline = gstlal
    Search = MDC
    skymap_fits = https://emfollow.docs.ligo.org/userguide/_static/bayestar.fits.gz,0
    BNS = 0.95
    NSBH = 0.01
    BBH = 0.03
    MassGap = 0.0
    Terrestrial = 0.01
    HasNS = 0.95
    HasRemnant = 0.91
    Distance = 39.76999609489013 +/- 8.308435058808886

.. testcleanup::

    os.chdir(old_dir)
    patcher.stop()

.. _curl: https://curl.haxx.se
