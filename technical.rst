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

  * pygcn_ for connecting to GCN (alternatives: comet_)
  * requests_ for easy HTTP downloads in Python (many alternatives in the
    :mod:`urllib` module from the Python standard library)
  * astropy-healpix_ for decoding HEALPix coordinates (alternatives: DS9_,
    Aladin_, `official C/C++/Fortran/Java/IDL HEALPix bindings`_)
  * astropy_ version 1.0.1 or newer (optional, for computing observability
    windows, etc.)
  * numpy_ and matplotlib_, popular math and plotting packages for Python

If you are on a Mac and use the MacPorts_ package manager, you can install all
of the above with the following command::

    $ sudo port install py37-gcn py37-requests py37-astropy-healpix

Otherwise, the fastest way to install the dependencies is with pip_, a package
manager that comes with most Python distributions. To install these packages
with ``pip``, run the following command::

    $ pip install pygcn requests astropy-healpix

Alert Schema
------------

+-------------------+-------------------------------------------+-------------------------------------------------------+
|                   | CBC                                       | Burst                                                 |
+===================+===========================================+=======================================================+
| **IVORN**         | :samp:`ivo://nasa.gsfc.gcn/LVC#S{YYMMDDabc}-{{1,2,3}}-{{Preliminary,Initial,Update,Retraction}}`  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| **Who**           | :samp:`LIGO Scientific Collaboration and Virgo Collaboration`                                     |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| **WhereWhen**     | Arrival time (UTC, ISO-8601), e.g. :samp:`2010-08-27T19:21:13.982800`                             |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| **What**          | GraceDB ID: :samp:`S{YYMMDDabc}`                                                                  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Search          | :samp:`CBC`                               | :samp:`Burst`                                         |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Pipeline        | :samp:`{{Gstlal,MBTA,PyCBC,SPIIR}}`       | :samp:`{{cWB,oLIB}}`                                  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - FAR             | Estimated false alarm rate in Hz                                                                  |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Network         | Flag for each detector (:samp:`LHO_participated`, etc.)                                           |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Sky map         | URL of HEALPix FITS localization file                                                             |
+-------------------+-------------------------------------------+-------------------------------------------------------+
| - Distance,       | *a posteriori* mean and standard          | N/A                                                   |
|   DistanceError   | deviation of luminosity distance          |                                                       |
+-------------------+-------------------------------------------+                                                       |
| - ProbHasNS,      | Probability (0–1) that the less massive   |                                                       |
|   ProbHasRemnant  | companion has mass :math:`<3 M_\odot`,    |                                                       |
|                   | and that the system ejected a significant |                                                       |
|                   | amount of NS material, respectively       |                                                       |
+-------------------+-------------------------------------------+-------------------------------------------------------+

Python Sample Code
------------------
* How to subcribe to GCN, receive and send alerts https://dcc.ligo.org/public/0118/G1500442/010/ligo-virgo-emfollowup-tutorial.html
* Interaction with GraceDB 


.. _GCN: http://gcn.gsfc.nasa.gov/
.. _VTP: http://www.ivoa.net/documents/Notes/VOEventTransport/
.. _VOEvent: http://www.ivoa.net/documents/VOEvent/
.. _pygcn: https://pypi.org/project/pygcn/
.. _comet: https://pypi.org/project/Comet/
.. _requests: https://pypi.org/project/requests/
.. _astropy-healpix: https://pypi.org/project/astropy-healpix/
.. _DS9: http://ds9.si.edu
.. _Aladin: https://aladin.u-strasbg.fr
.. _`official C/C++/Fortran/Java/IDL HEALPix bindings`: https://healpix.sourceforge.io
.. _astropy: https://pypi.org/project/astropy/
.. _numpy: https://pypi.org/project/numpy/
.. _matplotlib: https://pypi.org/project/matplotlib/
.. _MacPorts: https://www.macports.org
.. _pip: https://pip.pypa.io
