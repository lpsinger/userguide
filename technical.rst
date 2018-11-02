Technical Reference
===================

Public LIGO/Virgo alerts are distributed using the Gamma-ray Coordinates
Network (GCN_). The machine-readable alerts are called GCN Notices.

GCN Notices are available over several different protocols and in several
different formats. LIGO/Virgo strongly recommends using the VOEvent Transport
Protocol (VTP_) to receive notices in VOEvent_ XML format because it is
anonymous, configuration-free, and easy to parse.

Prerequisites
-------------

You will need to install a few third-party Python packages to run the example code below. These include:

  * A POSIX-like operating system (Linux or macOS)
  * Python >= 3.5
  * pygcn_ for connecting to GCN (alternatives: comet_)
  * requests_ for easy HTTP downloads in Python (many alternatives in the
    :mod:`urllib` module from the Python standard library)
  * healpy_ for decoding HEALPix coordinates (alternatives: astropy-healpix_,
    `official C/C++/Fortran/Java/IDL HEALPix bindings`_, DS9_, Aladin_)
  * astropy_ for astronomical coordinate transformations, observability, etc.
  * numpy_ and matplotlib_, popular math and plotting packages for Python

If you are on a Mac and use the MacPorts_ package manager, you can install all
of the above with the following command::

    $ sudo port install py37-gcn py37-requests py37-healpy

Otherwise, the fastest way to install the dependencies is with pip_, a package
manager that comes with most Python distributions. To install these packages
with ``pip``, run the following command::

    $ pip install pygcn requests healpy

Python Sample Code
------------------

Now we'll write a GCN handler script. First, some imports::

    # Python standard library imports
    import tempfile
    import shutil
    import sys
    import glob

    # Third-party imports
    import gcn
    import gcn.handlers
    import gcn.notice_types
    import requests
    import healpy as hp
    import numpy as np

Next, we'll write a function that we want to get called every time a GCN notice
is received. We will use the :term:`function decorator <decorator>`
``@gcn.handlers.include_notice_types`` to specify that we only want to process
certain notice types. There are three notice types:

 1. ``LVC_PRELIMINARY``: Provides the time, significance, and basic parameters
    about a GW detection candidate. The event has passed some automated checks
    but has not been vetted by humans. Sent with a latency of a minute or so.
 2. ``LVC_INITIAL``: The event has been vetted by humans. An updated sky
    localization may be included. Sent with a latency of a minutes to hours.
 3. ``LVC_UDPATE``: The event has been vetted by humans. An updated sky
    localization is included. Sent with a latency of hours or more.

In the following example, we will process all three alert types. The following
handler function will parse out the URL of the FITS file, download it, and
extract the probability sky map.

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
        # VERY IMPORTANT! Replce with the following line of code
        # to respond to only real 'observation' events.
        # if root.attrib['role'] != 'observation': return
        if root.attrib['role'] != 'test': return

        # Respond only to 'CBC' events. Change 'CBC' to "Burst' to respond to only
        # unmodeled burst events.
        if root.find(".//Param[@name='Group']").attrib['value'] != 'CBC': return

        # Read out integer notice type (note: not doing anythin with this right now)
        notice_type = int(root.find(".//Param[@name='Packet_Type']").attrib['value'])

        # Read sky map
        skymap, header = get_skymap(root)

.. important::
   Note that mock or 'test' observations are denoted by the ``role="test"``
   VOEvent attribute. Alerts resulting from real LIGO/Virgo science data will
   always have ``role="observation"``. The sample code below will respond
   **only** to 'test' events. When preparing for actual observations, you
   **must remember to switch to 'observation' events**.

Events come in two very general flavors: 'CBC' or compact binary coalescence
candidates detected by matched filtering, and generic 'Burst' candidates
detected by model-independent methods. Most users will want to receive only
'CBC' or only 'Burst' events. In this example code, we are going to keep only
'CBC' events.

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

        # Send HTTP request for sky map
        response = requests.get(skymap_url, stream=True)

        # Raise an exception unless the download succeeded (HTTP 200 OK)
        response.raise_for_status()

        # Create a temporary file to store the downloaded FITS file
        with tempfile.NamedTemporaryFile() as tmpfile:
            # Save the FITS file to the temporary file
            shutil.copyfileobj(response.raw, tmpfile)
            tmpfile.flush()

            # Uncomment to save FITS payload to file
            # shutil.copyfileobj(reponse.raw, open('example.fits.gz', 'wb'))

            # Read HEALPix data from the temporary file
            skymap, header = hp.read_map(tmpfile.name, h=True, verbose=False)
            header = dict(header)

        # Done!
        return skymap, header


.. _Aladin: https://aladin.u-strasbg.fr
.. _astropy-healpix: https://pypi.org/project/astropy-healpix/
.. _astropy: https://pypi.org/project/astropy/
.. _comet: https://pypi.org/project/Comet/
.. _DS9: http://ds9.si.edu
.. _GCN: http://gcn.gsfc.nasa.gov/
.. _healpy: https://pypi.org/project/healpy/
.. _MacPorts: https://www.macports.org
.. _matplotlib: https://pypi.org/project/matplotlib/
.. _numpy: https://pypi.org/project/numpy/
.. _pip: https://pip.pypa.io
.. _pygcn: https://pypi.org/project/pygcn/
.. _requests: https://pypi.org/project/requests/
.. _VOEvent: http://www.ivoa.net/documents/VOEvent/
.. _VTP: http://www.ivoa.net/documents/Notes/VOEventTransport/
.. _`official C/C++/Fortran/Java/IDL HEALPix bindings`: https://healpix.sourceforge.io
