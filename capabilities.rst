Observing Capabilities
======================

This section summarizes the observing capabilities of the global
gravitational-wave detector network as of early 2019. This as a quick reference
to the anticipated commissioning and observing schedule, sensitivity to
gravitational-wave transients, and sky localization accuracy, as described in
the following external documents:

* White Paper [#WhitePaper]_ on gravitational-wave data analysis and
  astrophysics
* Living Review [#LivingReview]_ on prospects for observing and localizing
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
signals, this figure gives the :term:`BNS range` for each observing run.

.. figure:: _static/Scripts_Figure2_ObsScen_fig2_final.*
   :alt: Long-term observing schedule

Engineering Run 14 (ER14) started on 2019-03-04. The transition into Observing
Run 3 (O3) occurred on 2019-04-01.

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

Sensitivity and Sky Localization Accuracy
-----------------------------------------

The following O3 projections are adapted from the Living Review
[#LivingReview]_ on prospects for observing and localizing gravitational-wave
transients with Advanced LIGO, Advanced Virgo, and KAGRA. The :term:`BNS range`
and :term:`burst range` (luminosity distance of detectable sources, averaged
over sky position and source orientation) given the detectors' anticipated
sensitivities are listed in the table below.

+-----------+-----------+-----------+-----------+-----------+
| Detector  | Range (Mpc)                                   |
|           +-----------+-----------+-----------+-----------+
|           | BNS       | BBH       | NSBH      | Burst     |
+===========+===========+===========+===========+===========+
| **LIGO**  | 110–130   | 990-1200  | 190-240   | 80–90     |
+-----------+-----------+-----------+-----------+-----------+
| **Virgo** | 50        | 500       | 90        | 35        |
+-----------+-----------+-----------+-----------+-----------+
| **KAGRA** | 8–25      | 80-260    | 15-45     | 5-25      |
+-----------+-----------+-----------+-----------+-----------+

We expect of order 10 :term:`BNS` events over the course of O3. For BNS events, the
median sky localization accuracy of in terms of the 90% credible area will be
250–320 deg². 10–15% of BNS mergers will be localized to less than 20 deg².

Event Rates
-----------


See the O3 Observing Scenarios [#O3ObservingScenarios]_ paper for LIGO and
Virgo's most current estimates of astrophysical rates of compact binary mergers.
The detection rate estimates contained in [#LivingReview]_ and later updated in the
O3 Observing Scenarios [#O3ObservingScenarios]_ paper embody estimates derived from the knowledge of mass,
spin, and rate distributions available at the time. These estimates are regularly
revised as our understanding of those distributions is enhanced with additional
detections. Updates will also take into account the network evolution and actual
advancement of the sensitivity of the instruments compared to projections in
[#LivingReview]_.

.. |LRR| replace:: *Living Rev. Rel.*

.. [#WhitePaper]
   LIGO Scientific Collaboration & Virgo Collaboration 2018, *The LSC-Virgo
   White Paper on Gravitational Wave Data Analysis and Astrophysics*.
   :dcc:`T1800058-v1`

.. [#LivingReview]
   Abbott, B. P., Abbott, R., Abbott, T. D., et al. 2018, |LRR|, 21, 3.
   :doi:`10.1007/s41114-018-0012-9`

.. [#CurrentO3Schedule]
   LIGO Scientific Collaboration & Virgo Collaboration 2019, *Current O3
   Schedule*. :dcc:`G1901531-v1`

.. [#O3ObservingScenarios]
   LIGO Scientific Collaboration & Virgo Collaboration 2019, *Prospects for
   Observing and Localizing Gravitational-Wave Transients with Advanced LIGO,
   Advanced Virgo and KAGRA*.
   :arxiv:`1304.0670`

