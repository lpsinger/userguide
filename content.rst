Alert Contents
==============

Public LIGO/Virgo alerts are distributing using NASA's Gamma-ray Coordinates
Network (:term:`GCN`). There are two types of alerts:

**GCN Notices** are machine-readable packets. They are available as
:term:`VOEvent` XML and `several other formats`_. We strongly recommend
receiving LIGO/Virgo alerts in the VOEvent XML format.

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
:doc:`/procedures/vetting`). If the signal does not pass human vetting (i.e.,
it is a glitch), then instead of an initial alert there will be a retraction_.
The initial alert is also accompanied by a GCN Circular which should be
considered as the first formal publication of the candidate and can be cited as
such.

An **Update GCN Notice** is issued whenever further analysis leads to improved
estimates of the source localization, significance, or classification. There
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
* Significance_: estimated false alarm rate
* Localization_: inferred sky position and (:term:`CBC` candidates only) distance
* Inference_: inferred source classification and properties (:term:`CBC`
  candidates only)

All types of GCN Notices *except for Preliminary notices* are accompanied by
human-readable GCN Circulars, which restates all of the above information as
well as a `data quality assessment`_.

Notice Contents
---------------

The table below is a diagrammatic representation of the contents of a
LIGO/Virgo GCN Notice.

+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **Root**                                                                                                                                  |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| IVORN             | :samp:`ivo://nasa.gsfc.gcn/LVC#[{{T,M}}]S{YYMMDDabc}-{{1,2,3}}-{{Preliminary,Initial,Update,Retraction}}`             |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Role              | :samp:`{{observation,test}}`                                                                                          |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **Who**                                                                                                                                   |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Date              | Time sent (UTC, ISO-8601), e.g. :samp:`2018-11-01T22:34:49`                                                           |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Author            | :samp:`LIGO Scientific Collaboration and Virgo Collaboration`                                                         |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **WhereWhen**     | Time of signal (UTC, ISO-8601), e.g. :samp:`2018-11-01T22:22:46.654437`                                               |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **What**                                                                                                                                  |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| GraceID           | GraceDb ID: :samp:`[{{T,M}}]S{YYMMDDabc}`. Example: :samp:`MS181101abc`                                               |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Packet Type       | GCN Notice type: :samp:`{{Preliminary,Initial,Update,Retraction}}`                                                    |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Notice Type       | Numerical equivalent of GCN Notice type: :samp:`{{150,151,152,164}}`                                                  |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| FAR               | Estimated false alarm rate in Hz                                                                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Sky Map           | URL of HEALPix FITS localization file                                                                                 |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Group             | :samp:`CBC`                                               | :samp:`Burst`                                             |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Pipeline          | :samp:`{{Gstlal,MBTAOnline,PyCBC,SPIIR}}`                 | :samp:`{{cWB,oLIB}}`                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| CentralFreq       | N/A                                                       | Central frequency in Hz                                   |
+-------------------+                                                           +-----------------------------------------------------------+
| Duration          |                                                           | Duration of burst in s                                    |
+-------------------+                                                           +-----------------------------------------------------------+
| Fluence           |                                                           | Gravitational-wave fluence in erg cm\ :math:`^{-2}`       |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| BNS, NSBH, BBH,   | Probability that the source is a :term:`BNS`,             | N/A                                                       |
| MassGap, Noise    | :term:`NSBH`, :term:`BBH` merger, :term:`MassGap` or      |                                                           |
|                   | terrestrial (i.e, noise) respectively                     |                                                           |
+-------------------+-----------------------------------------------------------+                                                           +
| HasNS, HasRemnant | Probability, under the assumption that the source is not  |                                                           |
|                   | noise, that at least one of the compact objects was a     |                                                           |
|                   | neutron star, and that the system ejected a nonzero amount|                                                           |
|                   | of neutron star matter, respectively.                     |                                                           |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+

Name
~~~~

The name of an event is its :term:`GraceDb` ID, a uniquely assigned identifier
such as :samp:`MS181101abc`. A GraceDb ID has three parts:

* Prefix: ``S`` for normal candidates and ``MS`` or ``TS`` for mock or test
  events respectively. The S stands for 
  :doc:`superevent </procedures/superevents>`.

* Date: The six-digit UTC date of the event consisting of a two-digit year,
  month, and day of month.

* Suffix: A lowercase alphabetic string that is incremented automatically
  (``a``, ``b``, ..., ``z``, ``aa``, ``ab``, ... ``az``, ``aaa``, etc.)
  whenever a candidate on a given date is added to GraceDb.

Significance
~~~~~~~~~~~~

The significance of the event is quantified by its false alarm rate (FAR): the
expected rate of events from the pipeline that produced the preferred event
with equal or greater significance in the absence of any astrophysical signals.

Localization
~~~~~~~~~~~~

The localization consists of the posterior probability distribution of the
source's sky position and (for :term:`CBC` events only) luminosity distance.
The GCN Notice and Circular will provide a URL for the localization file stored
in GraceDb. The localization is saved in a :term:`FITS` file as a
:term:`HEALPix` all-sky image. See our :doc:`sample code </tutorial/skymaps>`
for instructions on working with localization files.

Inference
~~~~~~~~~

The inference section is present for :term:`CBC` events *only*. It has two
parts:

**Classification**: Five numbers, summing to unity, giving probability that the
source belongs to the following five categories:

* :term:`BNS` merger
* :term:`NSBH` merger
* :term:`BBH` merger
* :term:`MassGap` merger
* Terrestrial (i.e., a chance background fluctuation or a glitch)

The figure below shows the extent of the three astrophysical categories (BNS,
NSBH, BBH and MassGap) in terms of the component masses :math:`m_1` and :math:`m_2`.

.. plot::
   :alt: Mass parameter space

    from matplotlib import pyplot as plt
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
    ax.text(*get_center(p.get_bbox()), 'BNS', ha='center', va='center')

    p = ax.add_patch(Rectangle((bh_min_mass, bh_min_mass),
                               max_mass - bh_min_mass, max_mass - bh_min_mass,
                               color=bbh_color, linewidth=0))
    ax.text(*get_center(p.get_bbox()), 'BBH', ha='center', va='center')

    p = ax.add_patch(Rectangle((min_mass, bh_min_mass),
                               ns_max_mass - min_mass, max_mass - bh_min_mass,
                               color=nsbh_color, linewidth=0))
    ax.text(*get_center(p.get_bbox()), 'NSBH', ha='center', va='center')

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
    ax.text(*get_center(p.get_bbox()), 'MassGap', ha='center', va='center')

    for args in [[1, 0, 0.025, 0], [0, 1, 0, 0.025]]:
        ax.arrow(*args,
                 transform=ax.transAxes, clip_on=False,
                 head_width=0.025, head_length=0.025, width=0,
                 linewidth=ax.spines['bottom'].get_linewidth(),
                 edgecolor=ax.spines['bottom'].get_edgecolor(),
                 facecolor=ax.spines['bottom'].get_edgecolor())

**Properties**: Probabilities that the source has each of the following
properties, *assuming that it is not noise* (e.g., assuming that it is a BNS,
NSBH, BBH or MassGap merger):

* **HasNS**: The mass of one or more of the binary's two companion compact
  objects is consistent with a neutron star.
* **HasRemnant**: A nonzero amount of neutron star material remained outside
  the final remnant compact object (a necessary but not sufficient condition to
  produce certain kinds of electromagnetic emission such as a short GRB or a
  kilonova).

All of the quantities in the Classification and Properties sections are model
dependent to some extent: the Classification section takes into consideration
prior knowledge of astrophysical compact binary merger rates from previous
LIGO/Virgo observations, and both the Classification and Properties sections
depend on details of neutron star physics (e.g. maximum NS mass, equation of
state). See the earlier :doc:`procedures </procedures/inference>` for
implementation details.

Circular Contents
-----------------

The following information will be present in the human-readable GCN Circulars.

Data Quality Assessment
~~~~~~~~~~~~~~~~~~~~~~~

Circulars may contain concise descriptions of any instrument or data quality
issues that may affect the significance estimates or the GW parameter
inferences. Unresolved data quality issues could mean that localization
estimates may shift after they have been mitigated, but does not mean that they
will. This is to be considered as advisory information.

Localization Ellipse
~~~~~~~~~~~~~~~~~~~~

Generally, GW localizations are irregularly shaped. However, for particularly
accurately localized events, the localization region can be well described by
an ellipse. For well-localized events, the GCN Circulars will include a 90%
containment ellipse in the format of a `DS9 region string`_ (right ascension,
declination, semi-major axis, semi-minor axis, position angle of the semi-minor
axis), for instance::

    icrs; ellipse(03h08m25s, -45d08m14s, 9d, 3d, 112d)

*Not* Included in Alerts
------------------------

The alerts will not contain quantitative estimates of intrinsic properties such
as masses and spins, nor contain information on the GW strain or reconstructed
waveforms. After final analysis, those data products are released through the
`Gravitational Wave Open Science Center <https://www.gw-openscience.org/>`_.

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

.. _`format and style`: https://gcn.gsfc.nasa.gov/gcn3_circulars.html
.. _`subscribe to GCN Circulars`: https://gcn.gsfc.nasa.gov/gcn_circ_signup.html
.. _`GCN Circulars archive`: https://gcn.gsfc.nasa.gov/gcn3_archive.html
.. _`examples from GW170817`: https://gcn.gsfc.nasa.gov/other/G298048.gcn3
.. _`several other formats`: https://gcn.gsfc.nasa.gov/gcn_describe.html#tc7
.. _`DS9 region string`: http://ds9.si.edu/doc/ref/region.html
