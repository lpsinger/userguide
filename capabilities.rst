Observing Capabilities
======================

This section summarizes the observing capabilities of the global
gravitational-wave detector network as of early 2019. This as a quick reference
to the anticipated commissioning and observing schedule, sensitivity to
gravitational-wave transients, and sky localization accuracy, as described in
the following external documents:

* White Paper [#WhitePaper]_ on gravitational-wave data analysis and
  astrophysics
* Living Review [#LivingReview]_ (see preprint of revised version
  [#O3ObservingScenarios]_) on prospects for observing and localizing
  gravitational-wave transients with Advanced LIGO, Advanced Virgo, and
  :term:`KAGRA`
* Current O3 Schedule [#CurrentO3Schedule]_

Timeline
--------

The gravitational-wave observing schedule is divided into Observing Runs or
epochs of months to years of operation at fixed sensitivity, down time for
construction and commissioning, and transitional Engineering Runs between
commissioning and observing runs. The long-term observing schedule is shown
below. Since :term:`BNS` mergers are a well-studied class of gravitational-wave
signals, this figure gives the BNS :term:`range` for each observing run.

.. figure:: _static/observing-scenarios-timeline.*
   :alt: Long-term observing schedule

Engineering Run 14 (ER14) started on 2019-03-04. The transition into Observing
Run 3 (O3) occurred on 2019-04-01. O3 is planned to end on 2020-04-30.

During O3, we expect that three facilities (:term:`LHO`, :term:`LLO`, and
Virgo) will observe for one year. It is possible that the Japanese KAGRA
detector may come online and become part of the international
gravitational-wave network at some point during O3. The near-term observing
schedule is shown below, reproduced from [#CurrentO3Schedule]_.

.. figure:: _static/O3Schedule.*
   :alt: Current observing schedule

Live Status
-----------

There are a handful of public web pages that report live status of the
LIGO/Virgo detectors and alert infrastructure.

*  | **Detector Status Portal**: Daily summary of detector performance.
   | https://www.gw-openscience.org/detector_status/

*  | **GWIStat**: Real-time detector up/down status.
   | https://ldas-jobs.ligo.caltech.edu/~gwistat/gwistat/gwistat.html

*  | **LIGO Data Grid Status**: Live dashboard showing up/down status of the
     detectors and online analyses. Status of the LIGO/Virgo alert pipeline is
     indicated by the "EMFollow" box.
   | https://monitor.ligo.org/gwstatus

Sensitivity
-----------

The following O3 projections are adapted from the preprint version of the
Living Review [#O3ObservingScenarios]_ on prospects for observing and
localizing gravitational-wave transients with Advanced LIGO, Advanced Virgo,
and KAGRA. The table below gives the :term:`range` of each individual detector
for :term:`BNS`, :term:`NSBH`, and :term:`BBH` mergers, and unmodeled
:term:`bursts <burst>`.

+-----------+-----------+-----------+-----------+-----------+
| Detector  | :term:`Range` (Mpc)                           |
|           +-----------+-----------+-----------+-----------+
|           | BNS       | NSBH      | BBH       | Burst     |
+===========+===========+===========+===========+===========+
| **LIGO**  | 110–130   | 190-240   | 990-1200  | 80–90     |
+-----------+-----------+-----------+-----------+-----------+
| **Virgo** | 50        | 90        | 500       | 35        |
+-----------+-----------+-----------+-----------+-----------+
| **KAGRA** | 8–25      | 15-45     | 80-260    | 5-25      |
+-----------+-----------+-----------+-----------+-----------+

These ranges are given for the following fiducial signals:

BNS
    A merger of two :math:`1.4 M_\odot` :term:`NSs <NS>`.
NSBH
    A merger of a :math:`10 M_\odot` :term:`BH` and a
    :math:`1.4 M_\odot` :term:`NS`.
BBH
    A merger of two :math:`30 M_\odot` :term:`BHs <BH>`.
Burst
    A monochromatic signal at a frequency of 140 Hz carrying an energy of
    :math:`E_\mathrm{GW}=10^{-2} M_\odot c^2`.

.. note::
   The :term:`range` is defined in relation to the :term:`sensitive volume`, or
   the surveyed space-time volume per unit detector time. The range is neither
   a luminosity distance nor a comoving distance.

Detection Rate and Localization Accuracy
----------------------------------------

Here we provide predicted detection rates, distances, and localization
uncertainties for :term:`BNS`, :term:`NSBH`, and :term:`BBH` mergers in O3 and
O4, based on a Monte Carlo simulation of detection and localization of events
in O3 and O4. Details of the simulation are described in
[#O3ObservingScenarios]_.

**Sky localization FITS files** from these simulations are provided at
https://git.ligo.org/emfollow/obs-scenarios-2019-fits-files.

Summary Statistics
~~~~~~~~~~~~~~~~~~

The table below summarizes the predicted detection rate and sky localization
accuracy in O3 and O4. All values are given as a 5% to 95% confidence
intervals.

+-----------+-----------+---------------+---------------+---------------+
|           |           | Source class                                  |
| Observing |           +---------------+---------------+---------------+
| run       | Network   | :term:`BNS`   | :term:`NSBH`  | :term:`BBH`   |
+===========+===========+===============+===============+===============+
|                                                                       |
| | **Merger rate per unit comoving volume per unit proper time**       |
| | (Gpc\ :superscript:`-3` year\ :superscript:`-1`,                    |
|   log-normal uncertainty)                                             |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
|                       | 110-3840      | 0.60-1000     | 25-109        |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Sensitive volume: detection rate / merger rate**                  |
| | (Gpc\ :superscript:`3`, Monte Carlo uncertainty)                    |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLV       | :math:`0.0033 | :math:`0.02   | :math:`0.34   |
|           |           | ^{+0.00028}   | ^{+0.0016}    | ^{+0.026}     |
|           |           | _{-0.00026}`  | _{-0.0015}`   | _{-0.025}`    |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLVK      | :math:`0.0034 | :math:`0.020  | :math:`0.35   |
|           |           | ^{+0.00028}   | ^{+0.0016}    | ^{+0.026}     |
|           |           | _{-0.00027}`  | _{-0.0015}`   | _{-0.025}`    |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HLVK      | :math:`0.016  | :math:`0.092  | :math:`1.5    |
|           |           | ^{+0.0014}    | ^{+0.0077}    | ^{+0.10}      |
|           |           | _{-0.0013}`   | _{-0.0072}`   | _{-0.096}`    |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Annual number of detections**                                     |
| | (log-normal merger rate uncertainty :math:`\times` Poisson          |
|   counting uncertainty)                                               |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLV       | :math:`1      | :math:`0      | :math:`17     |
|           |           | ^{+12}        | ^{+19}        | ^{+22}        |
|           |           | _{-1}`        | _{-0}`        | _{-11}`       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLVK      | :math:`1      | :math:`0      | :math:`18     |
|           |           | ^{+12}        | ^{+19}        | ^{+22}        |
|           |           | _{-1}`        | _{-0}`        | _{-12}`       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HLVK      | :math:`10     | :math:`1      | :math:`79     |
|           |           | ^{+52}        | ^{+91}        | ^{+89}        |
|           |           | _{-10}`       | _{-1}`        | _{-44}`       |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Median luminosity distance**                                      |
| | (Mpc, Monte Carlo uncertainty)                                      |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLV       | :math:`110    | :math:`210    | :math:`640    |
|           |           | ^{+3.7}       | ^{+6.6}       | ^{+29}        |
|           |           | _{-4.6}`      | _{-8.2}`      | _{-19}`       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLVK      | :math:`110    | :math:`210    | :math:`630    |
|           |           | ^{+3.8}       | ^{+7.7}       | ^{+25}        |
|           |           | _{-4.2}`      | _{-6.9}`      | _{-23}`       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HLVK      | :math:`170    | :math:`330    | :math:`990    |
|           |           | ^{+6.3}       | ^{+7.0}       | ^{+35}        |
|           |           | _{-4.8}`      | _{-13}`       | _{-29}`       |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Median 90% credible area**                                        |
| | (deg\ :superscript:`2`, Monte Carlo uncertainty)                    |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLV       | :math:`270    | :math:`330    | :math:`280    |
|           |           | ^{+34}        | ^{+24}        | ^{+30}        |
|           |           | _{-20}`       | _{-31}`       | _{-23}`       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLVK      | :math:`190    | :math:`240    | :math:`220    |
|           |           | ^{+36}        | ^{+37}        | ^{+33}        |
|           |           | _{-30}`       | _{-44}`       | _{-24}`       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HLVK      | :math:`33     | :math:`50     | :math:`41     |
|           |           | ^{+4.9}       | ^{+8.0}       | ^{+7.2}       |
|           |           | _{-5.3}`      | _{-8.4}`      | _{-5.7}`      |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Median 90% credible comoving volume**                             |
| | (10\ :superscript:`3` Mpc\ :superscript:`3`,                        |
|   Monte Carlo uncertainty)                                            |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLV       | :math:`120    | :math:`860    | :math:`16000  |
|           |           | ^{+19}        | ^{+150}       | ^{+2200}      |
|           |           | _{-24}`       | _{-150}`      | _{-2500}`     |
+-----------+-----------+---------------+---------------+---------------+
| O3        | HLVK      | :math:`79     | :math:`560    | :math:`11000  |
|           |           | ^{+27}        | ^{+190}       | ^{+2300}      |
|           |           | _{-19}`       | _{-160}`      | _{-2300}`     |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HLVK      | :math:`52     | :math:`430    | :math:`7700   |
|           |           | ^{+9.9}       | ^{+100}       | ^{+1500}      |
|           |           | _{-9.1}`      | _{-78}`       | _{-920}`      |
+-----------+-----------+---------------+---------------+---------------+

**Merger rate per unit comoving volume per unit proper time** is the
astrophysical rate of mergers in the reference frame that is comoving with the
Hubble flow. It is averaged over a distribution of masses and spins that is
assumed to be non-evolving.

.. caution::

   The merger rate per comoving volume should not be confused with the binary
   formation rate, due to the time delay between formation and merger.

   It should also not be confused with the merger rate per unit comoving volume
   per unit *observer* time. If the number density per unit comoving volume is
   :math:`n = dN / dV_C`, and the merger rate per unit proper time :math:`\tau`
   is :math:`R = dn/d\tau`, then the merger rate per unit *observer* time is
   :math:`R / (1 + z)`, with the factor of :math:`1 + z` accounting for time
   dilation.

For :term:`BNS` and :term:`BBH`, the merger rate is inferred from fitting the
observed population of LIGO/Virgo events in O1 and O2 [#O1O2Rates]_\ [#GWTC1]_.
For :term:`NSBH`, the merger rate is taken from [#RatePredictions]_. The quoted
confidence interval assumes that the uncertainty in the rate has a log-normal
distribution.

**Sensitive volume** is the quotient of the rate of detected events per unit
observer time and the merger rate per unit comoving volume per unit proper
time. The definition is given in the glossary entry for :term:`sensitive
volume`. To calculate the detection rate, multiply the merger rate by the
sensitive volume.

The quoted confidence interval represents the uncertainty from the Monte Carlo
simulation.

**Annual number of detections** is the number of detections in one calendar
year of observation. The quoted confidence interval incorporates both the
log-normal distribution of the merger rate *and* Poisson counting statistics,
but does not include the Monte Carlo error (which is negligible compared to the
first two sources of uncertainty).

The remaining sections all give median values over the population of detectable
events.

**Luminosity distance** is the luminosity distance in Mpc of detectable events.
The quoted confidence interval represents the uncertainty from the Monte Carlo
simulation.

**90% credible area** is the area in deg\ :math:`^2` of the smallest (not
necessarily simply connected) region on the sky that has a 90% chance of
containing the true location of the source.

**90% credible volume** is the comoving volume enclosed in the smallest region
of space that has a 90% chance of containing the true location of the source.

Cumulative Histograms
~~~~~~~~~~~~~~~~~~~~~

Below are cumulative histograms of the 90% credible area, distance, and 90%
credible comoving volume of detectable events in O3 and O4.

.. figure:: _static/area(90).*

   Distribution of 90% credible areas for simulated compact binary merger
   events from O3 and O4. The best-localized BNS merger (GW170817) and BBH
   merger (GW170818) as of this writing are shown at top as black tick marks.

.. figure:: _static/distance.*

   Distribution of luminosity distances for simulated compact binary merger
   events from O3 and O4. The best-localized BNS merger (GW170817) and BBH
   merger (GW170818) as of this writing are shown at top as black tick marks.

.. figure:: _static/vol(90).*

   Distribution of 90% credible comoving volumes for simulated compact binary
   merger events from O3 and O4. The best-localized BNS merger (GW170817) and
   BBH merger (GW170818) as of this writing are shown at top as black tick
   marks.

.. include:: /journals.rst

.. [#WhitePaper]
   LIGO Scientific Collaboration & Virgo Collaboration 2019, *The LSC-Virgo
   White Paper on Gravitational Wave Data Analysis and Astrophysics*.
   :dcc:`T1900541-v2`

.. [#LivingReview]
   Abbott, B. P., Abbott, R., Abbott, T. D., et al. 2018, |LRR|, 21, 3.
   :doi:`10.1007/s41114-018-0012-9`

.. [#O3ObservingScenarios]
   LIGO Scientific Collaboration & Virgo Collaboration 2019, *Prospects for
   Observing and Localizing Gravitational-Wave Transients with Advanced LIGO,
   Advanced Virgo and KAGRA*. :arxiv:`1304.0670`

.. [#CurrentO3Schedule]
   LIGO Scientific Collaboration & Virgo Collaboration 2019, *Current O3
   Schedule*. :dcc:`G1901531-v1`

.. [#O1O2Rates]
   LIGO Scientific Collaboration & Virgo Collaboration 2019, *Binary Black Hole
   Population Properties Inferred from the First and Second Observing Runs of
   Advanced LIGO and Advanced Virgo*. |ApJL|, 882, 24.
   :doi:`10.3847/2041-8213/ab3800`

.. [#GWTC1]
   LIGO Scientific Collaboration & Virgo Collaboration 2019, *GWTC-1: A
   Gravitational-Wave Transient Catalog of Compact Binary Mergers Observed by
   LIGO and Virgo during the First and Second Observing Runs*. |PRX|, 9,
   031040.
   :doi:`10.1103/PhysRevX.9.031040`

.. [#RatePredictions]
   LIGO Scientific Collaboration & Virgo Collaboration 2010, *Predictions for
   the rates of compact binary coalescences observable by ground-based
   gravitational-wave detectors*. |CQG|, 27, 173001.
   :doi:`10.1088/0264-9381/27/17/173001`

.. [#DistanceMeasuresInGWCosmology]
   Chen, H.-Y., Holz, D. E., et al. 2017, *Distance measures in
   gravitational-wave astrophysics and cosmology*. :arxiv:`1709.08079`
