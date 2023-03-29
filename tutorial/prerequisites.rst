Prerequisites
=============

In order to run this sample code, you will need Python >= 3.8 on a Unix-like
operating system (Linux or macOS) and a few third-party Python packages.

Python Packages
---------------

If you want to consume notices over Kafka (recommended), you will need one of either:

* gcn-kafka_ for connecting to `GCN Kafka`_ to receive JSON-serialized notices
  over Kafka
* hop-client_ for connecting to `HOPSKOTCH`_ to receive Avro-serialized notices
  over Kafka

.. note::
   The Kafka servers hosted by `GCN Kafka`_ and `HOPSKOTCH`_ should be
   accessible using any Kafka client, however we will only provide directions
   in this guide that use gcn-kafka_ for the former and hop-client_ for the
   latter.

If you want to consume notices from `GCN Classic`_, you will need:

* PyGCN_ for connecting to legacy GCN (alternatives: comet_)
* lxml_ for parsing :term:`VOEvent` XML packets (see also the voevent-parse_
  and VOEventLib_ helper libraries, both of which are based on lxml)

The following libraries are needed for working with the sky maps associated with
notices:

* :doc:`Healpy <healpy:index>` for decoding :term:`HEALPix` coordinates
  (alternatives: astropy-healpix_, the official C/C++/Fortran/Java/IDL
  HEALPix bindings for HEALPix_, DS9_, Aladin_)
* astropy_ for astronomical coordinate transformations, observability, etc.
* numpy_ and matplotlib_, popular math and plotting packages for Python

Installation
------------

The fastest way to install the dependencies is with pip_, a package manager
that comes with most Python distributions.  Another option is the `Anaconda`_
Python distribution.

Pip
~~~

Run the following command to install gcn-kafka_ and the packages needed to
work with sky maps:

.. code-block:: shell-session

    $ pip install gcn-kafka healpy

Run the following command to install hop-client_ and the packages needed to
work with sky maps:

.. code-block:: shell-session

    $ pip install hop-client healpy

Run the following command to install PyGCN_, lxml_, and the packages needed to
work with sky maps:

.. code-block:: shell-session

   $ pip install pygcn healpy

Anaconda
~~~~~~~~

To install these packages using Anaconda, first :doc:`install conda
<conda:user-guide/install/index>`.

Run the following command to install gcn-kafka_ and the packages needed to
work with sky maps:

.. code-block:: shell-session

    $ conda install -c conda-forge gcn-kafka healpy

Run the following command to install hop-client_ and the packages needed to
work with sky maps:

.. code-block:: shell-session

    $ conda install -c conda-forge hop-client healpy

Run the following command to install PyGCN_, lxml_, and the packages needed to
work with sky maps:

.. code-block:: shell-session

    $ conda install -c conda-forge pygcn healpy

.. _Aladin: https://aladin.u-strasbg.fr
.. _`Anaconda`: https://www.anaconda.com/
.. _astropy-healpix: https://pypi.org/project/astropy-healpix/
.. _astropy: https://pypi.org/project/astropy/
.. _comet: https://pypi.org/project/Comet/
.. _confluent-kafka: https://pypi.org/project/confluent-kafka/
.. _DS9: http://ds9.si.edu
.. _gcn-kafka: https://pypi.org/project/gcn-kafka/
.. _GCN Classic: https://gcn.nasa.gov/
.. _GCN Kafka: https://gcn.nasa.gov/
.. _HEALPix: https://healpix.sourceforge.io
.. _hop-client: https://pypi.org/project/hop-client/
.. _HOPSKOTCH: https://scimma.org/hopskotch.html
.. _lxml: https://pypi.org/project/lxml/
.. _matplotlib: https://pypi.org/project/matplotlib/
.. _numpy: https://pypi.org/project/numpy/
.. _pip: https://pip.pypa.io/en/stable/
.. _PyGCN: https://pypi.org/project/pygcn/
.. _voevent-parse: https://pypi.org/project/voevent-parse/
.. _VOEventLib: https://pypi.org/project/VOEventLib/
