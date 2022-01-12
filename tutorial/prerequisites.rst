Prerequisites
=============

In order to run this sample code, you will need Python >= 3.5 on a Unix-like
operating system (Linux or macOS) and a few third-party Python packages:

* PyGCN_ for connecting to GCN (alternatives: comet_)
* lxml_ for parsing :term:`VOEvent` XML packets (see also the voevent-parse_
  and VOEventLib_ helper libraries, both of which are based on lxml)
* :doc:`Healpy <healpy:index>` for decoding :term:`HEALPix` coordinates
  (alternatives: astropy-healpix_, the official C/C++/Fortran/Java/IDL
  HEALPix bindings for HEALPix_, DS9_, Aladin_)
* astropy_ for astronomical coordinate transformations, observability, etc.
* numpy_ and matplotlib_, popular math and plotting packages for Python
* confluent-kafka_ a data streaming platform
* fastavro_ a faster implementation of the avro data serialization system

* You will also need the OS virtualization software Docker_ in order to run the examples using Kafka with Avro.


If you are on a Mac and use the MacPorts_ package manager, you can install all
of the above with the following command:

.. code-block:: shell-session

    $ sudo port install py37-gcn py37-healpy

Otherwise, the fastest way to install the dependencies is with pip_, a package
manager that comes with most Python distributions. To install these packages
with ``pip``, run the following command:

.. code-block:: shell-session

    $ pip install pygcn healpy

Another option is the `Anaconda`_ Python distribution. To install these
packages using Anaconda, first :doc:`install conda
<conda:user-guide/install/index>` and then run the following commands:

.. code-block:: shell-session

    $ conda config --add channels conda-forge
    $ conda install pygcn healpy

.. _Aladin: https://aladin.u-strasbg.fr
.. _`Anaconda`: https://www.anaconda.com/
.. _astropy-healpix: https://pypi.org/project/astropy-healpix/
.. _astropy: https://pypi.org/project/astropy/
.. _comet: https://pypi.org/project/Comet/
.. _confluent-kafka: https://pypi.org/project/confluent-kafka/
.. _Docker: https://docs.docker.com/get-docker/
.. _DS9: http://ds9.si.edu
.. _fastavro: https://pypi.org/project/fastavro/
.. _HEALPix: https://healpix.sourceforge.io
.. _lxml: https://pypi.org/project/lxml/
.. _MacPorts: https://www.macports.org
.. _matplotlib: https://pypi.org/project/matplotlib/
.. _numpy: https://pypi.org/project/numpy/
.. _pip: https://pip.pypa.io/en/stable/
.. _PyGCN: https://pypi.org/project/pygcn/
.. _voevent-parse: https://pypi.org/project/voevent-parse/
.. _VOEventLib: https://pypi.org/project/VOEventLib/
