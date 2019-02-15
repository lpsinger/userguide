Receiving GCNs
==============

Next, we'll write a GCN handler function that we want PyGCN to call every time
it receives a GCN notice. We :term:`decorate <decorator>` the handler with
``@gcn.handlers.include_notice_types`` to specify that we only want to process
certain GCN notice types (``LVC_PRELIMINARY``, ``LVC_INITIAL``, and
``LVC_UDPATE``).

Events come in two very general flavors: 'CBC' or compact binary coalescence
candidates detected by matched filtering, and generic 'Burst' candidates
detected by model-independent methods. Your handler can take different actions
based on this. The example below will handle only 'CBC' events.

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
    # LVC_PRELIMINARY, LVC_INITIAL, or LVC_UPDATE.
    @gcn.handlers.include_notice_types(
        gcn.notice_types.LVC_PRELIMINARY,
        gcn.notice_types.LVC_INITIAL,
        gcn.notice_types.LVC_UPDATE)
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

        # Respond only to 'CBC' events. Change 'CBC' to "Burst'
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

When you run this script, you should receive a sample LIGO/Virgo GCN Notice
every hour. For each event received, it will print output that looks like what
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

    $ curl -O https://emfollow.docs.ligo.org/userguide/_static/MS181101ab-1-Preliminary.xml

Then you can manually invoke your GCN handler using this Python code:

.. testsetup::

    import os
    old_dir = os.getcwd()
    os.chdir('_static')

.. testcode::

    import lxml.etree
    payload = open('MS181101ab-1-Preliminary.xml', 'rb').read()
    root = lxml.etree.fromstring(payload)
    process_gcn(payload, root)

Upon running this, you should see:

.. testoutput::

    internal = 0
    Packet_Type = 150
    Pkt_Ser_Num = 1
    GraceID = MS181101ab
    AlertType = Preliminary
    HardwareInj = 0
    OpenAlert = 1
    EventPage = https://example.org/superevents/MS181101ab/view/
    Instruments = H1,L1
    FAR = 9.11069936486e-14
    Group = CBC
    Pipeline = gstlal
    Search = MDC
    skymap_fits = https://emfollow.docs.ligo.org/userguide/_static/bayestar.fits.gz
    BNS = 0.95
    NSBH = 0.01
    BBH = 0.03
    Terrestrial = 0.01
    HasNS = 0.95
    HasRemnant = 0.91
    Distance = 141.1453950128411 +/- 39.09548411497191

.. testcleanup::

    os.chdir(old_dir)

.. _curl: https://curl.haxx.se
