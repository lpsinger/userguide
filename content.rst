Alert Contents
==============

Public LIGO/Virgo alerts are distributing using NASA's Gamma-ray Coordinates
Network (:term:`GCN`). There are two types of alerts:

**GCN Notices** are machine-readable packets. They are available as
:term:`VOEvent` XML and `several other formats`_. See the
:doc:`/tutorial/index` section for instructions on receiving GCNs in VOEvent
format.

.. warning::
   We recommend receiving LIGO/Virgo alerts in the VOEvent XML format using one
   of `GCN's anonymous VOEvent brokers`_. VOEvent over anonymous :term:`VTP` is
   the **only GCN format and distribution method that is fully supported by
   LIGO/Virgo.**

   The VOEvent XML alerts are official data products of LIGO/Virgo. GCN
   produces `several other legacy formats`_ from them, in particular a
   text-based "full format" and binary format. LIGO/Virgo performs only limited
   quality control of the legacy formats.

**GCN Circulars** are short human-readable astronomical bulletins. They are
written in a certain well-established `format and style`_. You can `subscribe
to GCN Circulars`_ to receive and post them by email, or you can view them in
the public `GCN Circulars archive`_.

Notice Types
------------

For each event, there are up to four kinds of GCN Notices:

A **Preliminary GCN Notice** is issued automatically within minutes after a
gravitational-wave candidate is detected. The candidate must have passed some
automated data quality checks, but it may later be :ref:`retracted
<retraction>` after human vetting. There is no accompanying GCN Circular at
this stage.

An **Initial GCN Notice** is issued after human vetting (see
:doc:`/analysis/vetting`). If the signal does not pass human vetting (e.g., it
is a glitch), then instead of an initial alert there will be a retraction_. The
initial alert is also accompanied by a GCN Circular, which should be considered
as the first formal publication of the candidate and can be cited as such.

An **Update GCN Notice** is issued whenever further analysis leads to improved
estimates of the sky localization, significance, or classification. There
may be multiple updates for a given event, and updates may be issued hours,
days, or even weeks after the event.

.. _retraction:

Lastly, a **Retraction GCN Notice** is issued if the candidate is rejected as a
result of vetting by human instrument scientists and data analysts. A
retraction indicates that the candidate has been withdrawn because it is
probably not astrophysical.

All types of GCN Notices *except for Retraction notices* contain the following
information, which are described in further detail below:

* Name_: a unique identifier for the candidate
* Significance_: estimated false alarm rate (:term:`FAR`)
* `Sky localization`_: inferred sky position and (:term:`CBC` candidates only)
  distance
* Inference_: (:term:`CBC` candidates only) inferred source classification and
  properties

Of the above fields, Retraction notices provide only the name.

Initial and Update notices are accompanied by human-readable GCN Circulars,
which restate all of the above information and also may include a `data quality
assessment`_.

Notice Contents
---------------

The table below is a representation of the contents of a LIGO/Virgo GCN Notice.

+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| **Root**                                                                                                                                          |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| IVORN             | :samp:`ivo://gwnet/LVC#[{{T,M}}]S{YYMMDDabc}-{{1,2,3}}-{{Preliminary,Initial,Update,Retraction}}`                             |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Role              | :samp:`{{observation,test}}`                                                                                                  |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| **Who**                                                                                                                                           |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Date              | Time sent (UTC, ISO-8601), e.g. :samp:`2018-11-01T22:34:49`                                                                   |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Author            | :samp:`LIGO Scientific Collaboration and Virgo Collaboration`                                                                 |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| **WhereWhen**     | Time of signal (UTC, ISO-8601), e.g. :samp:`2018-11-01T22:22:46.654437`                                                       |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| **What**                                                                                                                                          |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| GraceID           | GraceDB ID: :samp:`[{{T,M}}]S{YYMMDDabc}`. Example: :samp:`MS181101abc`                                                       |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Packet Type       | GCN Notice type: :samp:`{{Preliminary,Initial,Update,Retraction}}`                                                            |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Notice Type       | Numerical equivalent of GCN Notice type: :samp:`{{150,151,152,164}}`                                                          |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| FAR               | Estimated :term:`FAR` in Hz                                                                                                   |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Sky Map           | Versioned URL of HEALPix FITS sky localization file in the format                                                             |
|                   | :samp:`https://gracedb.ligo.org/api/superevents/[{{T,M}}]S{YYMMDDabc}/files/{{bayestar,LALInference,cWB}}.fits.gz,{[0-8]}`.   |
|                   | Example: :samp:`https://gracedb.ligo.org/api/superevents/S190901ap/files/bayestar.fits.gz,0`                                  |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Group             | :samp:`CBC`                                               | :samp:`Burst`                                                     |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Pipeline          | :samp:`{{gstlal,MBTAOnline,pycbc,spiir}}`                 | :samp:`{{CWB,oLIB}}`                                              |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| CentralFreq       | N/A                                                       | Central frequency in Hz                                           |
+-------------------+                                                           +-------------------------------------------------------------------+
| Duration          |                                                           | Duration of burst in s                                            |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| BNS, NSBH, BBH,   | Probability that the source is a :term:`BNS`,             | N/A                                                               |
| MassGap, Noise    | :term:`NSBH`, :term:`BBH`, or :term:`MassGap` merger, or  |                                                                   |
|                   | :term:`terrestrial` (i.e, noise) respectively             |                                                                   |
+-------------------+-----------------------------------------------------------+                                                                   +
| HasNS, HasRemnant | Probability, under the assumption that the source is not  |                                                                   |
|                   | noise, that at least one of the compact objects was a     |                                                                   |
|                   | neutron star, and that the system ejected a non-zero      |                                                                   |
|                   | amount of neutron star matter, respectively               |                                                                   |
+-------------------+-----------------------------------------------------------+-------------------------------------------------------------------+

In the event of a coincidence between a gravitational-wave candidate and an
alert from a third party (e.g. a gamma-ray burst or neutrino trigger), the
following fields will also be present:

+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| External GCN Notice ID                | :samp:`{{583417860, 583327924}}`                                                                                      |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| External IVORN                        | External IVORN identification field                                                                                   |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| External Observatory                  | :samp:`{{Fermi,Swift}}`                                                                                               |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| External Search                       | :samp:`{{GRB,SubGRB}}`                                                                                                |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Time Coincidence FAR                  | Estimated coincidence false alarm rate in Hz using timing                                                             |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Time and Sky Position Coincidence FAR | Estimated coincidence false alarm rate in Hz using timing and sky position                                            |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Combined Sky Map                      | URL of combined GW-External HEALPix FITS sky localization file                                                        |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Time Difference                       | Time between source and external event in seconds                                                                     |
+---------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

Name
~~~~

The name of an event is its :term:`GraceDB` ID, a uniquely assigned identifier
such as :samp:`MS181101abc`. A GraceDB ID has three parts:

* Prefix: ``S`` for normal candidates and ``MS`` or ``TS`` for mock or test
  events respectively. The S stands for
  :doc:`superevent </analysis/superevents>`.

* Date: The six-digit UTC date of the event consisting of a two-digit year,
  month, and day of month.

* Suffix: A lowercase alphabetic string that is incremented automatically
  (``a``, ``b``, ..., ``z``, ``aa``, ``ab``, ... ``az``, ``aaa``, etc.)
  whenever a candidate on a given date is added to GraceDB.

Significance
~~~~~~~~~~~~

The significance of the event is quantified by its false alarm rate (FAR): the
expected rate of events from the pipeline that produced the preferred event
with equal or greater significance in the absence of any astrophysical signals.

Sky Localization
~~~~~~~~~~~~~~~~

The sky localization consists of the posterior probability distribution of the
source's sky position and (for :term:`CBC` events only) luminosity distance.
The GCN Notice and Circular will provide a URL for the sky localization file
stored in GraceDB. The sky localization is saved in a :term:`FITS` file as a
:term:`HEALPix` [#HEALPixFramework]_ all-sky image. See our :doc:`sample code
</tutorial/skymaps>` for instructions on working with sky localization files.

The sky map URL will generally be of the form
:samp:`https://gracedb.ligo.org/api/superevents/{sid}/files/{method}.fits.gz,{v}`,
where :samp:`{sid}` is the :doc:`superevent </analysis/superevents>` ID,
:samp:`{method}` is the sky localization algorithm (usually :samp:`bayestar`,
:samp:`LALInference`, or :samp:`cWB`), and :samp:`{v}` is an integer that
uniquely identifies different versions of the localization. The version number
is automatically assigned by GraceDB, starting from 0, and increments for each
file of the same name. For example, the first FITS file with the name
``bayestar.fits.gz`` becomes ``bayestar.fits.gz,0``, then the next one is
``bayestar.fits.gz,1``, and so on. The filename without the version suffix,
such as ``bayestar.fits.gz``, always points to the most recent version.

..  important::
    We generally provide localizations in two HEALPix formats, distinguished by
    file extension:

    ..  rubric:: ``*.fits.gz``

    A subset of the standard HEALPix-in-FITS format (see semi-official
    specifications `from the HEALPix team`_ and :ref:`from the gamma-ray
    community <gamma-astro-data-formats:healpix_skymap>`) that is recognized by
    a wide variety of astronomical imaging programs including DS9_ and Aladin_.
    It uses HEALPix :ref:`implicit indexing
    <gamma-astro-data-formats:hpx_implicit>` and the `NESTED numbering scheme`_.
    **This is the primary and preferred format, and the only format that is
    explicitly listed in the GCN Notices and Circulars.** See the section
    :doc:`/tutorial/skymaps` for details.

    ..  rubric:: ``*.multiorder.fits``

    A new variant of the HEALPix format that is designed to overcome
    limitations of the ``*.fits.gz`` format for well-localized events from
    three-detector operations and future gravitational-wave facilities (see
    rationale in :dcc:`G1800186`). It uses HEALPix :ref:`explicit indexing
    <gamma-astro-data-formats:hpx_explicit>` and the `NUNIQ numbering scheme`_,
    which is closely related to `multi-order coverage (MOC) maps`_ in Aladin.
    This is the internal format that is used by the LIGO/Virgo low-latency
    alert pipeline. **This is an experimental format, and it is currently
    recommended only for advanced users.** See the section
    :doc:`/tutorial/multiorder_skymaps` for details.

    Both formats always use celestial (equatorial, J2000) coordinates.

Inference
~~~~~~~~~

The inference section is present for :term:`CBC` events *only*. It has two
parts:

**Classification**: Five numbers, summing to unity, giving probability that the
source belongs to the following five mutually exclusive categories:

* :term:`BNS` merger
* :term:`NSBH` merger
* :term:`BBH` merger
* :term:`MassGap` merger
* :term:`Terrestrial` (i.e., a chance background fluctuation or a glitch)

The figure below shows the extent of the three astrophysical categories (BNS,
NSBH, BBH, and MassGap) in terms of the component masses :math:`m_1` and
:math:`m_2`.

.. note::
   By convention, the component masses are defined such that :math:`m_1 \geq
   m_2`, so that the :term:`primary` compact object in the binary (i.e.,
   component 1), is always more massive than the :term:`secondary` compact
   object (i.e., component 2).

   In the mass diagram below, the upper diagonal region :math:`m_1 < m_2` is
   lightly shaded in order to indicate that the definitions of four mass
   classes (BNS, NSBH, BBH, MassGap) are *symmetric* in :math:`m_1` and
   :math:`m_2`.

.. _classification-diagram:

.. plot::
   :alt: Mass parameter space

    from matplotlib import pyplot as plt
    from matplotlib import patheffects
    from matplotlib.patches import Rectangle
    from matplotlib.ticker import FormatStrFormatter
    import seaborn

    def get_center(bbox):
        return 0.5 * (bbox.x0 + bbox.x1), 0.5 * (bbox.y0 + bbox.y1)

    min_mass = 1
    ns_max_mass = 3
    bh_min_mass = 5
    max_mass = 11
    ax = plt.axes(aspect=1)
    ax.set_xlim(min_mass, max_mass)
    ax.set_ylim(min_mass, max_mass)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ticks = [min_mass, ns_max_mass, bh_min_mass]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    ticklabels = [r'{} $M_\odot$'.format(tick) for tick in ticks]
    ax.set_xticklabels(ticklabels)
    ticklabels[0] = ''
    ax.set_yticklabels(ticklabels)

    ax.set_xlabel(r'$m_1$')
    ax.set_ylabel(r'$m_2$', rotation=0, ha='right')
    ax.xaxis.set_label_coords(1.0, -0.025)
    ax.yaxis.set_label_coords(-0.025, 1.0)

    bns_color, nsbh_color, gap_color, bbh_color = seaborn.color_palette(
        'pastel', 4)

    p = ax.add_patch(Rectangle((min_mass, min_mass),
                               ns_max_mass - min_mass, ns_max_mass - min_mass,
                               color=bns_color, linewidth=0))
    ax.text(0.25 * min_mass + 0.75 * ns_max_mass, 0.5 * min_mass + 0.5 * ns_max_mass,
            'BNS', ha='center', va='center',
            path_effects=[patheffects.Stroke(linewidth=2, foreground=bns_color),
                          patheffects.Normal()])

    p = ax.add_patch(Rectangle((bh_min_mass, bh_min_mass),
                               max_mass - bh_min_mass, max_mass - bh_min_mass,
                               color=bbh_color, linewidth=0))
    ax.text(0.5 * (bh_min_mass + max_mass), 0.75 * bh_min_mass + 0.25 * max_mass,
            'BBH', ha='center', va='center')

    p = ax.add_patch(Rectangle((min_mass, bh_min_mass),
                               ns_max_mass - min_mass, max_mass - bh_min_mass,
                               color=nsbh_color, linewidth=0))

    p = ax.add_patch(Rectangle((bh_min_mass, min_mass),
                               max_mass - bh_min_mass, ns_max_mass - min_mass,
                               color=nsbh_color, linewidth=0))
    ax.text(*get_center(p.get_bbox()), 'NSBH', ha='center', va='center')

    ax.add_patch(Rectangle((min_mass, ns_max_mass),
                           max_mass - min_mass, bh_min_mass - ns_max_mass,
                           color=gap_color, linewidth=0))
    ax.add_patch(Rectangle((ns_max_mass, min_mass),
                           bh_min_mass - ns_max_mass, max_mass - min_mass,
                           color=gap_color, linewidth=0))
    p = ax.add_patch(Rectangle((ns_max_mass, ns_max_mass),
                               bh_min_mass - ns_max_mass, bh_min_mass - ns_max_mass,
                               color=gap_color, linewidth=0))
    ax.text(0.5 * (bh_min_mass + max_mass), 0.5 * (ns_max_mass + bh_min_mass),
            'MassGap', ha='center', va='center')

    ax.fill_between([min_mass, max_mass],
                    [min_mass, max_mass],
                    [max_mass, max_mass],
                    color='white', linewidth=0, alpha=0.75, zorder=1.5)
    ax.plot([min_mass, max_mass], [min_mass, max_mass], '--k')

    ax.annotate('',
                xy=(0.975, 1.025), xycoords='axes fraction',
                xytext=(1.025, 0.975), textcoords='axes fraction',
                ha='center', va='center',
                arrowprops=dict(
                    arrowstyle='->', shrinkA=0, shrinkB=0,
                    connectionstyle='angle,angleA=90,angleB=180,rad=7'))
    ax.text(0.975, 1.025, '$m_1 \geq m_2$ by definition  ',
            ha='right', va='center', transform=ax.transAxes, fontsize='small')

    for args in [[1, 0, 0.025, 0], [0, 1, 0, 0.025]]:
        ax.arrow(*args,
                 transform=ax.transAxes, clip_on=False,
                 head_width=0.025, head_length=0.025, width=0,
                 linewidth=ax.spines['bottom'].get_linewidth(),
                 edgecolor=ax.spines['bottom'].get_edgecolor(),
                 facecolor=ax.spines['bottom'].get_edgecolor())

**Properties**: Probabilities that the source has each of the following
properties, *assuming that it is not noise* (e.g., assuming that it is a BNS,
NSBH, BBH, or MassGap merger):

* **HasNS**: The mass of one or more of the binary's two companion compact
  objects is consistent with a neutron star. Equivalently, the mass of the
  *secondary* or less massive compact object is consistent with a neutron star,
  :math:`m_2 \leq 3 M_\odot`.
* **HasRemnant**: A non-zero amount of neutron star material remained outside
  the final remnant compact object (a necessary but not sufficient condition to
  produce certain kinds of electromagnetic emission such as a short :term:`GRB`
  or a kilonova).

All of the quantities in the Classification and Properties sections are model
dependent to some extent: the Classification section takes into consideration
prior knowledge of astrophysical compact binary merger rates from previous
LIGO/Virgo observations, and both the Classification and Properties sections
depend on details of neutron star physics (e.g. maximum NS mass, equation of
state). See the earlier subsection of the :doc:`Data Analysis
</analysis/inference>` section for implementation details.

Circular Contents
-----------------

The following information will be present in the human-readable GCN Circulars.

Data Quality Assessment
~~~~~~~~~~~~~~~~~~~~~~~

Circulars may contain concise descriptions of any instrument or data quality
issues that may affect the significance estimates or the GW parameter
inferences. Unresolved data quality issues could mean that sky localization
estimates may shift after they have been mitigated, but does not mean that they
will. This is to be considered as advisory information.

Sky Localization Ellipse
~~~~~~~~~~~~~~~~~~~~~~~~

Generally, GW sky localizations are irregularly shaped. However, for
particularly accurately localized events, the sky localization region can be
well described by an ellipse. When the area of the 90% ellipse is less than
1.35 times the area of the *smallest possible 90% credible region*, the GCN
Circular will provide a 90% containment ellipse. For details of the ellipse
fitting algorithm, see :mod:`ligo.skymap.postprocess.ellipse`.

The ellipse is described in the format of a `DS9 region string`_. Many tools
can read DS9 region strings, including `DS9`_, `Aladin`_, :doc:`astropy-regions
<astropy-regions:index>`, and :doc:`pyregion <pyregion:index>`. The region
string contains the right ascension, declination, semi-major axis, semi-minor
axis, position angle of the semi-minor axis). Here is an example::

    icrs; ellipse(03h08m25s, -45d08m14s, 9d, 3d, 112d)

*Not* Included in Alerts
------------------------

The alerts will not contain quantitative estimates of intrinsic properties such
as masses and spins, nor contain information on the GW strain or reconstructed
waveforms. After final analysis, those data products are released through the
`Gravitational Wave Open Science Center
<https://www.gw-openscience.org/about/>`_.

Examples
--------

Below are some sample VOEvents to illustrate the formatting of the GCN Notices.

.. tabs::

   .. tab:: Preliminary

      .. literalinclude:: _static/MS181101ab-1-Preliminary.xml
         :language: xml

   .. tab:: Initial

      .. literalinclude:: _static/MS181101ab-2-Initial.xml
         :language: xml

   .. tab:: Update

      .. literalinclude:: _static/MS181101ab-3-Update.xml
         :language: xml

   .. tab:: Retraction

      .. literalinclude:: _static/MS181101ab-4-Retraction.xml
         :language: xml

   .. tab:: External Coincidence

      .. literalinclude:: _static/MS181101ab-5-Update.xml
         :language: xml

.. _`from the HEALPix team`: https://healpix.sourceforge.io/data/examples/healpix_fits_specs.pdf
.. _`NESTED numbering scheme`: https://healpix.sourceforge.io/html/intro_Geometric_Algebraic_Propert.htm#SECTION410
.. _`NUNIQ numbering scheme`: https://healpix.sourceforge.io/html/intro_Geometric_Algebraic_Propert.htm#SECTION420
.. _`multi-order coverage (MOC) maps`: http://ivoa.net/documents/MOC/
.. _`format and style`: https://gcn.gsfc.nasa.gov/gcn3_circulars.html
.. _`subscribe to GCN Circulars`: https://gcn.gsfc.nasa.gov/gcn_circ_signup.html
.. _`GCN Circulars archive`: https://gcn.gsfc.nasa.gov/gcn3_archive.html
.. _`examples from GW170817`: https://gcn.gsfc.nasa.gov/other/G298048.gcn3
.. _`several other formats`: https://gcn.gsfc.nasa.gov/gcn_describe.html#tc7
.. _`several other distribution methods`: https://gcn.gsfc.nasa.gov/tech_describe.html
.. _`GCN's anonymous VOEvent brokers`: https://gcn.gsfc.nasa.gov/voevent.html#tc2
.. _`DS9 region string`: http://ds9.si.edu/doc/ref/region.html
.. _`DS9`: http://ds9.si.edu/
.. _`Aladin`: https://aladin.u-strasbg.fr/

.. |apj| replace:: *Astrophys. J.*

.. [#HEALPixFramework]
   Górski, K.M., Hivon, E., Banday, A.J., et al. 2005, |apj|, 622, 759.
   :doi:`10.1086/427976`
