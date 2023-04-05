VOEvent Notices via GCN Classic
===============================

In this section, we'll write a GCN handler function, write a script to receive
and parse VOEvent notices using PyGCN, and finally download and parse an
example notice. You do not need to create an account or set up credentials to
receive GCN classic notices.

Receiving and Parsing Notices
-----------------------------

The following basic handler function will parse out the URL of the FITS file,
download it, and extract the probability sky map. We :term:`decorate
<decorator>` the handler with ``@gcn.handlers.include_notice_types`` to specify
that we only want to process certain GCN notice types (``LVC_EARLY_WARNING``,
``LVC_PRELIMINARY``, ``LVC_INITIAL``, ``LVC_UDPATE`` and ``LVC_RETRACTION``).


.. important::
   Note that mock or 'test' observations are denoted by the ``role="test"``
   VOEvent attribute. Alerts resulting from real LIGO/Virgo/KAGRA science data
   will always have ``role="observation"``. The sample code below will respond
   **only** to 'test' events. When preparing for actual observations, you
   **must remember to switch to 'observation' events**.

.. note::
   Observe in the example below that we do not have to explicitly download the
   FITS file because the :func:`hp.read_map() <healpy.fitsfunc.read_map>`
   function works with either URLs or filenames. However, you could download
   and save the FITS file in order to save it locally using
   :func:`astropy.utils.data.download_file`, :func:`requests.get`,
   :func:`urllib.request.urlopen`, or even curl_.

.. testcode::

    import gcn
    import healpy as hp
    import ligo.skymap
    import ligo.skymap.io

    # Function to call every time a GCN is received.
    # Run only for notices of type LVC_EARLY_WARNING, LVC_PRELIMINARY,
    # LVC_INITIAL, LVC_UPDATE, or LVC_RETRACTION.
    @gcn.handlers.include_notice_types(
        gcn.notice_types.LVC_EARLY_WARNING,
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
            skymap, header = ligo.skymap.io.read_sky_map(params['skymap_fits'])
            header = dict(header)

            # Print some values from the FITS header.
            print('Distance =', header['distmean'], '+/-', header['diststd'])

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

When you run this script you should receive a sample LIGO/Virgo/KAGRA GCN
Notice every hour. For each event received it will print output that looks like
what is shown in the :ref:`offline-testing-voevent` example below.

.. note::
   ``gcn.listen`` will try to automatically reconnect if the network connection
   is ever broken.

.. _offline-testing-voevent:

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
    Significant = 1
    Group = CBC
    Pipeline = gstlal
    Search = MDC
    skymap_fits = https://emfollow.docs.ligo.org/userguide/_static/bayestar.multiorder.fits,0
    BNS = 0.95
    NSBH = 0.01
    BBH = 0.03
    Terrestrial = 0.01
    HasNS = 0.95
    HasRemnant = 0.91
    HasMassGap = 0.01
    Distance = 39.76999609489013 +/- 8.308435058808886

.. testcleanup::

    os.chdir(old_dir)
    patcher.stop()

.. _curl: https://curl.se
