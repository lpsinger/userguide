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

The following basic handler function will parse out the URL of
the FITS file, download it, and extract the probability sky map::

    # Function to call every time a GCN is received.
    # Run only for notices of type
    # LVC_PRELIMINARY, LVC_INITIAL, or LVC_UPDATE.
    @gcn.handlers.include_notice_types(
        gcn.notice_types.LVC_PRELIMINARY,
        gcn.notice_types.LVC_INITIAL,
        gcn.notice_types.LVC_UPDATE)
    def process_gcn(payload, root):
        # Print the alert
        print('Got VOEvent:')
        print(payload)

        # Respond only to 'test' events.
        # VERY IMPORTANT! Replace with the following code
        # to respond to only real 'observation' events.
        # if root.attrib['role'] != 'observation':
        #    return
        if root.attrib['role'] != 'test':
            return

        # Respond only to 'CBC' events. Change 'CBC' to "Burst'
        # to respond to only unmodeled burst events.
        if root.find(".//Param[@name='Group']").attrib['value'] != 'CBC':
            return

        # Read out integer notice type (note: not doing anythin with this right now)
        notice_type = int(root.find(".//Param[@name='Packet_Type']").attrib['value'])

        # Read sky map
        skymap, header = get_skymap(root)

The ``get_skymap`` function will be defined in the next section.

Download the Sky Map
--------------------

Now we will define the function ``get_skymap`` get the sky map URL from the
VOEvent, download it, and read it with Healpy.

.. note::
   We do not have to explicitly download the FITS file because the
   :func:`hp.read_map() <healpy.fitsfunc.read_map>` function works with either
   URLs or filenames. However, you could download and save the FITS file in
   order to save it locally using :func:`astropy.utils.data.download_file`,
   :func:`requests.get`, :func:`urllib.request.urlopen`, or even curl_.

::

    def get_skymap(root):
        """
        Look up URL of sky map in VOEvent XML document,
        download sky map, and parse FITS file.
        """
        # Read out URL of sky map.
        # This will be something like
        # https://gracedb.ligo.org/api/events/M131141/files/bayestar.fits.gz
        skymap_url = root.find(
            ".//Param[@name='skymap_fits']").attrib['value']

        # Read the sky map.
        # Note: this works on filenames or URLs.
        # The `h=True` argument instructs Healpy to also return the metadata
        # from the FITS header, and the `verbose=False` argument suppresses
        # printing of some diagnostic information.
        skymap, header = hp.read_map(skymap_url, h=True, verbose=False)

        # Done!
        return skymap, header

Listen for GCNs
---------------

Finally, we will start the VOEvent client to listen for GCNs using the
``gcn.listen`` function. By default, this will connect to the anonymous, public
GCN server. You just need to tell ``gcn.listen`` what function to call whenever
it receives an GCN; in this example, that is the ``process_gcn`` handler that
we defined above.

.. note::
   ``gcn.listen`` will try to automatically reconnect if the network connection
   is ever broken.

::

    # Listen for GCNs until the program is interrupted
    # (killed or interrupted with control-C).
    gcn.listen(handler=process_gcn)

.. _curl: https://curl.haxx.se
