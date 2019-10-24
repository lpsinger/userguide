Sky Map Visualizations and Credible Regions in Aladin
=====================================================

In this section, we demonstrate working with gravitational-wave sky
localizations in `Aladin Desktop`_. The following main topics are addressed.

.. contents:: :local:

MOC and GW Sky Localizations
----------------------------

The enclosed area within a given probability level contour of a GW sky map can
be effectively described with a Multi-Order Coverage (:term:`MOC`) map
[#Fernique15]_. MOC is a standard of the Virtual Observatory which provides a
representation of arbitrary regions on the unit sphere using the
:term:`HEALPix` sky tessellation.

The MOC data structure encodes irregular sky regions as a hierarchy of HEALPix
pixels. Each MOC cell is defined by two numbers: the hierarchy level (HEALPix
:math:`\mathit{order}`) and the pixel index (HEALPix :math:`\mathit{ipix}`).
MOCs are serialized as FITS or JSON files. The finest level of refinement
within the MOC hierarchy is determined by the HEALPix :math:`\mathit{order}`
parameter or the equivalent :math:`\mathit{nside}` parameter, related by
:math:`\mathit{nside} = 2^\mathit{order}`. For example, ``order=9`` corresponds
to ``nside=512``, and a resolution of :math:`6.9'` per pixel.

The MOC maps make database queries for retrieving objects and logical operation
(such as union, intersection, subtraction, difference) extremely fast even for
very complex sky regions.

MOC maps and :doc:`multi-order sky maps </tutorial/multiorder_skymaps>` are
closely related. They use similar multi-resolution HEALPix data structures. The
main distinction is that MOC maps encode *regions on the sphere*, whereas
multi-order sky maps encode *sampled images or functions on the sphere*. The
multi-order sky map FITS format is a superset of the MOC FITS format, the only
difference being that a multi-order sky map has values attached to each cell
(probability density, distance estimates) whereas a MOC map does not. Future
Aladin releases will support the LIGO/Virgo multi-resolution sky maps.

Running Aladin Desktop
----------------------

Aladin Desktop is a Java application. To run it, you must first have the `Java
Virtual Machine`_ (JVM) installed. More details are in Aladin's `download
page`_.

.. note::
   Aladin may fail to load some LIGO/Virgo sky maps and display a
   ``java.lang.OutOfMemoryError`` error message. This is because the highest
   resolution LIGO/Virgo sky maps do not fit inside Aladin's default memory
   size.

   You can increase the maximum memory size used by your Java runtime
   environment by following the instructions below.

   Download the Aladin.jar from the Aladin `download page`_. Execute it from a
   terminal by typing::

       $ java -Xmx2g -jar Aladin.jar

   The flag :samp:`-Xmx{<ammount of memory>}` specifies the maximum memory
   allocation pool for a JVM. Here 2GB of memory is allocated. For GW sky
   localizations with ``nside=2048``, increase the memory allocated up to 3GB,
   ``-Xmx3g``.

Loading a GW Sky Localization
-----------------------------

You can copy and paste the sky map URL from the `GraceDB`_ or drag and drop a
HEALPix FITS file from your operating system's file browser in the main Aladin
window. Aladin recognizes only the standard HEALPix format with the file
extension ``.fits.gz``. Here we will work with the `LALinference sky map of
GW170817`_.

Building a Credible Region
--------------------------

The sequence of the Aladin Desktop commands to create a credible region at a
defined confidence level is described below. From the menu bar, select
:menuselection:`Coverage --> Generate a MOC based on --> The current
probability skymap`.

.. figure:: /_static/aladin_fig1.png
   :alt: Create a MOC from a GW sky localization

The :guilabel:`MOC generation` window has two options: the probability sky map
and the threshold. Make sure that the GW sky map that we loaded in the previous
step is selected in the :guilabel:`Proba skymap` dropdown menu. Then enter a
number between 0 and 1 for the credible level in the :guilabel:`Probability
threshold` box. Finally, press the :guilabel:`CREATE` button. The MOC for the
credible region is created and loaded in the Aladin Stack. If you repeat this
process multiple times for different credible levels, then you can select each
MOC independently from the Aladin stack.

Area Within a Credible Region
-----------------------------

There are two ways to get the area within a MOC credible region. If you hover
over the cursor over the MOC name in the Aladin stack, then the area in square
degrees and the percentage of the sky are shown in the top-right corner of the
Aladin window. Alternatively, you can right-click the MOC in the Aladin stack
and select :guilabel:`Properties` from the contextual menu. The area and
percentage of the sky are shown in the :guilabel:`Properties` dialog box. From
this dialog box, you can also control the appearance and color of the MOC,
which is useful for distinguishing multiple MOCs for different credible levels.

.. figure:: /_static/aladin_fig2.png
   :alt: Properties window

Querying and Filtering a Galaxy Catalog
---------------------------------------

Each gravitational-wave sky map for a :term:`CBC` event provides a
three-dimensional probability distribution as a function of sky position and
distance [#Singer16b]_. Cross-matching that distribution with positions and
redshifts of a galaxy catalog provides a filtered list of of possible host
galaxies (see :doc:`/tutorial/3d`). Aladin does not yet implement a galaxy
catalog query by the three-dimensional posterior probability distribution.
However, it is currently possible in Aladin to search for galaxies within the
2D credible region on the sky and, afterwards, apply a distance cut that it
independent of sky position.

Here we query the galaxies collected in the `GLADE catalog`_ inside the 90%
credible region of GW170817. Then we filter those galaxies according to the
marginal distance posterior distribution integrated over the whole sky.

1. **Pick out the galaxy catalog from the data collections tree**.

   Any of the 20,000 catalogs published in the Virtual Observatory can be
   retrieved from the data collections tree in the left panel of the main
   Aladin window.

   To find the GLADE catalog, make sure that :menuselection:`-- all
   collections --` is selected in the :guilabel:`from` dropdown menu in the
   bottom of the left panel, then type :samp:`GLADE` in the :guilabel:`select`
   text field. In the data collections tree, click on :menuselection:`GLADE
   v2.3 catalog (Dalya+, 2018)`.

2. **Load the galaxy catalog filtered by the 2D credible region.**

   In the popup window, click the :guilabel:`by region & MOC` checkbox in order
   to filter it by the 2D credible region that we created earlier. Then press
   the :guilabel:`Load` button.

  .. figure:: /_static/aladin_fig3.png
     :alt:  Aladin data collection tree

3. **Filter the galaxy catalog by distance.**

   The posterior mean distance and the posterior standard deviation of
   luminosity distance in Mpc are reported in the FITS file header with the
   keywords ``DISTMEAN`` and ``DISTSTD``, respectively. In the case of
   GW170817, they have the values ``DISTMEAN = 38.0`` and ``DISTSTD = 7.5``.

   Select :menuselection:`Catalog --> Create a filter` from the menu bar. This
   opens the :guilabel:`Properties` dialog box contains two tabs. Select the
   :guilabel:`Advanced mode` tab and copy the following text into the filter
   definition box::

       ${Dist} > 30.5 && ${Dist} < 45.5 {draw}

   This is an expression for a 1-sigma cut on distance in the `Aladin filter
   syntax`_. ``Dist`` is the column in the GLADE catalog corresponding to the
   distance in Mpc.

   Click on :guilabel:`Apply` and then on :guilabel:`Export` to create a new
   level in the Aladin stack consisting only of sources selected by the filter.

   .. figure:: /_static/aladin_filter.png
      :alt: Aladin filter

.. Thumbnail View Generator
   ------------------------

   Finally, we make a mosaic of the filtered galaxies. Select :menuselection:`Tool
   --> Thumbnail view generator` from the menu bar, then click the :guilabel:`Ok`
   button in the dialog box.

   Here the thumbnails are color composition images of the Digitized Sky Surveys
   (`DSS`_).

   .. figure:: /_static/aladin_fig4.png
      :alt: Thumbnail view generator

   You can load additional surveys from the `HiPS list aggregator`_.
   As an example, for loading the Two Micron All Sky Survey (`2MASS`_), you just
   need to copy and paste in the Aladin :guilabel:`Command` box the **Base URL**
   (http://alasky.u-strasbg.fr/2MASS/Color) reported in the `2MASS preview page`_.

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
.. _`download page`: https://aladin.u-strasbg.fr/java/nph-aladin.pl?frame=downloading
.. _`script launcher`: https://aladin.u-strasbg.fr/java/Aladin
.. _`GraceDB`: https://gracedb.ligo.org/
.. _`LALinference sky map of GW170817`: https://dcc.ligo.org/public/0157/P1800381/006/GW170817_skymap.fits.gz
.. _`GLADE catalog`: http://aquarius.elte.hu/glade/index.html
.. _`Aladin filter syntax`: https://cdsweb.u-strasbg.fr/boch/doc/filters.htx
.. _`2MASS preview page`: https://alasky.u-strasbg.fr/2MASS/Color/
.. _`HiPS list aggregator`: https://aladin.unistra.fr/hips/list
.. _`DSS`: https://archive.stsci.edu/dss/index.html
.. _`2MASS`: https://www.ipac.caltech.edu/2mass/
.. _`preview page`: https://alasky.u-strasbg.fr/2MASS/Color/