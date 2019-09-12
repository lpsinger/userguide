Sky Map Visualizations and Credible Regions
===========================================

In this section, we demonstrate some basic strategies for working with
gravitational-wave sky localizations in `Aladin Desktop`_. The following main
topics are addressed.

.. contents:: :local:

MOC and GW Sky Localizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The enclosed area within a given probability level contour of a GW sky map can
be effectively described through the Multi-Order Coverage (MOC) method
[#Fernique15]_. It is a standard of the Virtual Observatory which provides a
multi-scale mapping based on HEALPix sky tessellation.

The data structure maps irregular and complex sky regions into hierarchically
grouped predefined cells. Each MOC cell is defined by two numbers: the
hierarchy level (HEALPIx order) and the pixel index (HEALPIx ipix). The
``NUNIQ`` scheme defines an algorithm for packing an (order, ipix) pair into a
single integer for compactness. MOCs are serialized as FITS or JSON files. The
MOC resolution is determined by the map resolution parameter ``nside``, which
is used for defining the resolution of the grid. For a typical ``nside=512``
(:math:`6.871'` per pixel), the MOC order resolution is ``order = 9``

.. math::
   \mathit{nside} = 2^\mathit{order}.

The MOC maps make database queries for retrieving objects and logical operation
(such as union, intersection, subtraction, difference) extremely simple and
fast even for very complex sky regions. If databases are adapted to support MOC
based queries, such as `VizieR`_, they offer a useful method allowing any
support of sky region query.

The resolution of a GW sky localization with three or more detectors can reach
a resolution considerably large. To mitigate the computational time, a new
variant of the HEALPix format is designed and annotated with the file extension
``.multiorder.fits``. See the section :doc:`/tutorial/multiorder_skymaps` for
details. Although the FITS format for LIGO/Virgo multi-resolution sky maps uses
the **UNIQ** indexing scheme and is a superset of the FITS serialization for
MOC map, operationally, they are defined as follows. With *MOC map*, we
indicate the method to map complex regions for fast queries and sky map
comparisons, while, with *multi-order sky map*, we refer to a new HEALPix
format to deal with computational challenges related to highly accurate
localizations. Future Aladin releases will support the LIGO/Virgo
multi-resolution sky maps.

1. Running Aladin Desktop
-------------------------

Aladin is developed in Java. As any Java tool, Aladin Desktop requires a `Java
Virtual Machine`_ (JVM) and a classical installation on the user machine
according with your operating system. More details in the `Download
instructions`_.

.. note::
   If Aladin fails during operation with a message that says something about a
   ``java.lang.OutOfMemoryError``, then your heap size is too small for what
   you are trying to do. You will have to run Java with a bigger heap size. You
   can increase the maximum memory size used by your Java runtime environment
   by following the instructions below.

   Download the ``Aladin.jar`` file from `here`_ and execute it from a terminal
   by typing::

       $ java -Xmx2g -jar Aladin.jar

   The flag ``-Xmx< ammount of memory >`` specifies the maximum memory
   allocation pool for a Java Virtual Machine (JVM). Here 2GB of memory is
   allocated. For GW sky localizations with ``NSIDE = 2048``, increase the
   memory allocated up to 3GB, ``-Xmx3g``.

2. Loading a GW Sky Localization
--------------------------------

You can copy and paste the sky map URL from the `GraceDB`_ or drag and drop a
HEALPix FITS file from your operating system's file browser in the main Aladin
window. Aladin recognizes only the standard HEALPix format with the file
extension ``.fits.gz``. Here we will work with the `LALinference sky map of
GW170817`_.

3. Building a Credible Region
-----------------------------

The sequence of the Aladin Desktop commands to create a credible region at a
defined confidence level is reported below. From the main menu press
:menuselection:`Coverage --> Generate a MOC based on --> The current
probability skymap --> MOC generation`

.. figure:: /_static/aladin_fig1.png
   :alt: Create a MOC from a GW sky localization

The :guilabel:`MOC generation` window requires two mandatory parameters 1) the
probability sky map and 2) the threshold. The probability sky map entry, that
means the GW sky localization in our context, can be selected from the
drop-down menu. The drop-down menu contains the GW sky localization previously
loaded and showed in the Aladin Stack. The threshold input represents the
percentage of the credible region in decimal (ranging from 0 to 1). Press the
:guilabel:`CREATE` button to generate the resulting credible region. The
credible region is created and loaded in the Aladin Stack. The credible region
obtained so far are decoded in the Multi Order Coverage map (MOC) and each new
level can be independently used.

4. :guilabel:`Properties` Window
--------------------------------

To open the :guilabel:`Properties` window, right click on the selected plan in
the Aladin stack. The associated :guilabel:`Properties` windows allows to
change the drawing methods in perimeter in order to simultaneously visualize
multiple confidence levels. This operation facilitates tiling operations by
telescopes monitoring the highest probability areas. The enclosed sky area in
square degrees and the percentage of the sky coverage are quoted for each
credible region either **i)** by leaving the cursor on the corresponding plan
loaded in the Aladin stack or **ii)** by opening the associated Properties
windows.

.. figure:: /_static/aladin_fig2.png
   :alt: Properties window

You can overlap a large data set of image backgrounds provided by the `HiPS
list aggregator`_ or you can generate your own HiPS from image/cube data. For
doing this, from the main menu press :menuselection:`Tool --> Generate a HiPS
based on --> An image collections (FITS, JPEG, PNG)`

5. Querying and Filtering a Galaxy Catalog
------------------------------------------

Singer et al. [#Singer16b]_ discuss a fast algorithm for obtaining a
three-dimensional probability estimates of sky location and luminosity distance
from observations of binary compact object mergers with Advanced LIGO and
Virgo. Combining the reconstructed gravitational wave volumes with positions
and redshifts of possible host galaxies provides a filtered list of sky
location targets to search for the electromagnetic counterpart of the
gravitational wave signal. At present it is not implemented in Aladin a catalog
query by the GW three-dimensional posterior probability distribution. What we
can currently achieve is to query the entire galaxy catalog and, afterwards, to
filter the selection. Here a cut-distance filter is applied taking into account
the marginal distance posterior distribution integrated over the whole sky.
These tasks are efficiently performed in the Aladin Desktop using the data
collections tree and the filter methods as follows.

:menuselection:`Aladin data collections tree --> Select --> click on the
catalog item --> in the popup window check --> by region & MOC`

  .. figure:: /_static/aladin_fig3.png
   :alt:  Aladin data collection tree

Now we can filter the galaxy catalog. From the main menu press

:menuselection:`Catalog --> Create a filter--> Properties --> Advanced mode -->
Or enter your filter definition`

An example about the Aladin filter using as galaxy selection the marginal
distance posterior distribution integrated over the whole sky is reported
below: ``${Dist} > DISTMEAN-DISTSTD && ${Dist} < DISTMEAN+DISTSTD {draw}``. The
posterior mean distance (Mpc) and the posterior standard deviation of distance
(Mpc) are reported in the fits file header with the keywords ``DISTMEAN`` and
``DISTSTD``. Click on ``Apply`` and then ``Export`` to create a new plane
consisting only of sources selected by the filter.

  .. figure:: /_static/aladin_filter.png
   :alt: Aladin filter

Finally, make thumbnails of the selected galaxies. From the main menu press
:menuselection:`Tool --> Thumbnail view generator` download and select in the
Aladin stack any image background to obtain the corresponding galaxy images.

  .. figure:: /_static/aladin_fig4.png
   :alt: Thumbnail view generator

.. |apjl| replace:: *Astrophys. J. Lett.*
.. |A&A|  replace:: *Astronomy & Astrophysics*
.. |prd|  replace:: *Phys. Rev. D*

.. [#Fernique15]
   Fernique, P., Allen, et al. 2015, |A&A|, 578, A114.
   :doi:`10.1051/0004-6361/201526075`

.. [#Singer16b]
   Singer, L. P., Chen, H.-Y., Holz, D. E., et al. 2016, |apjl|, 829, L15.
   :doi:`10.3847/2041-8205/829/1/L15`

.. _`Aladin Desktop`:  https://aladin.u-strasbg.fr/AladinDesktop/
.. _`VizieR`:  http://vizier.u-strasbg.fr/index.gml
.. _`Java Virtual Machine`: https://www.java.com/en/
.. _`Download instructions`: https://aladin.u-strasbg.fr/java/nph-aladin.pl?frame=downloading
.. _`here`: https://aladin.u-strasbg.fr/java/nph-aladin.pl?frame=downloading
.. _`script launcher`: https://aladin.u-strasbg.fr/java/Aladin
.. _`GraceDB`: https://gracedb.ligo.org/
.. _`LALinference sky map of GW170817`: https://dcc.ligo.org/public/0157/P1800381/006/GW170817_skymap.fits.gz
.. _`HiPS list aggregator`: https://aladin.unistra.fr/hips/list