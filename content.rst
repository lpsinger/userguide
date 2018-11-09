Alert Contents
==============

Public LIGO/Virgo alerts are distributing using NASA's Gamma-ray Coordinates
Network (:term:`GCN`). There are two types of alerts:

**GCN Circulars** are short human-readable astronomical bulletins. They are written
in a certain well-established `format and style`_. You can `subscribe to GCN
Circulars`_ to receive and post them by email, or you can view them in the
public `GCN Circulars archive`_.

**GCN Notices** are machine-readable packets. They are available as :term:`VOEvent`
XML and `several other formats`_. We strongly recommend receiving LIGO/Virgo
alerts in the VOEvent XML format.

.. _`format and style`: https://gcn.gsfc.nasa.gov/gcn3_circulars.html
.. _`subscribe to GCN Circulars`: https://gcn.gsfc.nasa.gov/gcn_circ_signup.html
.. _`GCN Circulars archive`: https://gcn.gsfc.nasa.gov/gcn3_archive.html
.. _`examples from GW170817`: https://gcn.gsfc.nasa.gov/other/G298048.gcn3
.. _`several other formats`: https://gcn.gsfc.nasa.gov/gcn_describe.html#tc7

Notice Types
------------

For each event, there are up to four kinds of GCN Notices:

A **Preliminary GCN Notice** is issued automatically within minutes after a
gravitational-wave candidate is detected. The candidate must have passed some
automated data quality checks, but it may later be :ref:`retracted
<retraction>` after human vetting. There is no accompanying GCN Circular at
this stage.

An **Initial GCN Notice** is issued within 4 hours of the preliminary alert,
after vetting by human instrument scientists and data analysts. If the signal
does not pass human vetting (i.e., it is a glitch), then instead of an initial
alert there will be a retraction_. The initial alert is also accompanied by a
GCN Circular which should be considered as the first formal publication of the
candidate and can be cited as such.

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
* Inference_: inferred source classification and properties (:term:`CBC` candidates only)

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
| IVORN             | :samp:`ivo://nasa.gsfc.gcn/LVC#[{{T,M}}]S{YYMMDDabc}-{{1,2,3}}-{{Preliminary,Initial,Update,Preliminary-Retraction}}` |
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
| Packet Type       | GCN Notice type: :samp:`{{Preliminary,Initial,Update}}`                                                               |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Notice Type       | Numerical equivalent of GCN Notice type: :samp:`{{150,151,152}}`                                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| FAR               | Estimated false alarm rate in Hz                                                                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Sky Map           | URL of HEALPix FITS localization file                                                                                 |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Group             | :samp:`CBC`                                               | :samp:`Burst`                                             |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Pipeline          | :samp:`{{Gstlal,MBTA,PyCBC,SPIIR}}`                       | :samp:`{{cWB,oLIB}}`                                      |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| CentralFreq       | N/A                                                       | Central frequency in Hz                                   |
+-------------------+                                                           +-----------------------------------------------------------+
| Duration          |                                                           | Duration of burst in Hz                                   |
+-------------------+                                                           +-----------------------------------------------------------+
| Fluence           |                                                           | Gravitational-wave fluence in erg cm\ :math:`^{-2}`       |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| **Why**           | Inference about the source                                                                                            |
+-------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| BNS, NSBH, BBH,   | Probability that the source is a :term:`BNS`,             | N/A                                                       |
| Noise             | :term:`NSBH`, :term:`NSBH` merger, or just noise,         |                                                           |
|                   | respectively (mutually exclusive)                         |                                                           |
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
  events respectively. The S stands for `superevent <superevents>`_.

* Date: The six-digit UTC date of the event consisting of a two-digit year,
  month, and day of month.

* Suffix: A lowercase alphabetic string that is incremented automatically
  (``a``, ``b``, ..., ``z``, ``aa``, ``ab``, ... ``az``, ``aaa``, etc.)
  whenever a candidate on a given date is added to GraceDb.

Significance
~~~~~~~~~~~~

The significance of the event is quantified by its false alarm rate (FAR): the
expected rate of events with equal or greater significance in the absence of
any astrophysical signals. If the estimated FAR is less than
:math:`(100\,\mathrm{yr})^{-1}`, then the Circular will simply describe the
event as "highly significant." Otherwise, the value of the FAR will be stated
in the Circular.

Localization
~~~~~~~~~~~~

The localization is consists of the posterior probability distribution of the
source's sky position ("2D localization") or of the source's sky position and
luminosity distance ("3D localization," available only for :term:`CBC` events).
The GCN Notice and Circular will provide a URL for the localization file stored
in GraceDb. The localization is saved a :term:`FITS` file as a :term:`HEALPix`
all-sky image. See our :doc:`sample code </tutorial/skymaps>` for instructions
on working with localization files.

Inference
~~~~~~~~~

The inference section is present for :term:`CBC` events *only*. It has two
parts:

**Classification**: Four numbers, summing to unity, giving probability that the
source belongs to the following four categories:

* :term:`BNS` merger
* :term:`NSBH` merger
* :term:`BBH` merger
* noise (i.e., a chance background fluctuation or a glitch)

**Properties**: Probabilities that the source has each of the following
properties, *assuming that it is not noise* (e.g., assuming that it is a BNS,
NSBH, or BBH merger):

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

Data quality assessment
~~~~~~~~~~~~~~~~~~~~~~~

Circulars may contain concise descriptions of any instrument or data quality
issues that may affect the significance estimates or the GW parameter
inferences. Unresolved data quality issues could mean that localization
estimates may shift after they have been mitigated, but does not mean that they
will. This is to be considered as advisory information.

What is *not* included in alerts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The alerts will not contain quantitative estimates of intrinsic properties such
as masses and spins, nor contain information on the GW strain or reconstructed
waveforms. After final analysis, those data products are released through the
`Gravitational Wave Open Science Center <https://www.gw-openscience.org/>`_.

Examples
--------

Below are some sample VOEvents to illustrate the formatting of the GCN Notices.

.. tabs::

   .. tab:: Preliminary

      .. literalinclude:: _static/MS181101abc-1-Preliminary.xml
         :language: xml

   .. tab:: Initial

      .. literalinclude:: _static/MS181101abc-2-Initial.xml
         :language: xml

   .. tab:: Update

      .. literalinclude:: _static/MS181101abc-3-Update.xml
         :language: xml

   .. tab:: Retraction

      .. literalinclude:: _static/MS181101abc-4-Retraction.xml
         :language: xml
