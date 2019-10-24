Online Pipelines
================

A number of search pipelines run in a low latency, online mode. These can be
divided into two groups, modeled and unmodeled. The modeled (:term:`CBC`)
searches specifically look for signals from compact binary mergers of neutron
stars and black holes (:term:`BNS`, :term:`NSBH`, and :term:`BBH` systems). The
unmodeled (Burst) searches on the other hand, are capable of detecting signals
from a wide variety of astrophysical sources in addition to compact binary
mergers: core-collapse of massive stars, magnetar star-quakes, and more
speculative sources such as intersecting cosmic strings or as-yet unknown GW
sources.

Modeled Search
--------------

**GstLAL**, **MBTA**, **PyCBC Live** and **SPIIR** are matched-filtering based
analysis pipelines that rapidly identify compact binary merger events, with
:math:`\lesssim 1` minute latencies. They use discrete banks of waveform
templates to cover the target parameter space of compact binaries, with all
pipelines covering the mass ranges corresponding to :term:`BNS`, :term:`NSBH`,
and :term:`BBH` systems.

A coincident analysis is performed by all pipelines, where candidate events are
extracted separately from each detector via matched-filtering and later
combined across detectors. SPIIR extracts candidates from each detector via
matched-filtering and looks for coherent responses from the other detectors to
provide source localization. Of the four pipelines, GstLAL and MBTA use several
banks of matched filters to cover the detectors bandwidth, i.e., the templates
are split across multiple frequency bands. All pipelines also implement
different kinds of signal-based vetoes to reject instrumental transients that
cause large :term:`SNR` values but can otherwise be easily distinguished from
compact binary coalescence signals.

**GstLAL** [#GstLAL1]_ [#GstLAL2]_ is a matched-filter pipeline designed to
find gravitational waves from compact binaries in low-latency. It uses a
likelihood ratio, which increases monotonically with signal probability, to
rank candidates, and then uses Monte Carlo sampling methods to estimate the
distribution of likelihood-ratios in noise. This distribution can then be used
to compute a :term:`FAR` and p-value.

**MBTA** [#MBTA]_ constructs its background by making every possible
coincidence from single detector triggers over a few hours of recent data. It
then folds in the probability of a pair of triggers passing the time
coincidence test.

**PyCBC Live** [#PyCBC1]_ [#PyCBC2]_ estimates the noise background by
performing time-shifted analyses using triggers from a few hours of recent
data. Single-detector triggers from one detector are time shifted by every
possible multiple of 100 ms, thus any resulting coincidence must be unphysical
given the :math:`\sim 10` ms light travel time between detectors.  All such
coincidences are recorded and assigned a ranking statistic. The false alarm
rate is then estimated by counting accidental coincidences ranked higher than a
given candidate, i.e. with a higher statistic value. When three detectors are
observing at the time of a particular candidate, the most significant double
coincidence is selected, and its false alarm rate is modified to take into
account the data from the remaining detector.

**SPIIR** [#SPIIR]_ [#SPIIRThesis]_ applies summed parallel infinite impulse
response (IIR) filters to approximate matched-filtering results. It selects
high-:term:`SNR` events from each detector and finds coherent responses from
other detectors. It constructs a background statistical distribution by
time-shifting detector data one hundred times over a week to evaluate
foreground candidate significance.

Unmodeled Search
----------------

**cWB** [#cWB]_ is an excess power algorithm to identify short-duration
gravitational wave signals. It uses a wavelet transformation to identify
time-frequency pixels that can be grouped in a single cluster if they satisfy
neighboring conditions. A tuned version for compact-binary coalescences chooses
the time-frequency pixels if they mainly follow a pattern that increases in
frequency. A maximum-likelihood-statistics calculated over the cluster is used
to identify the proper parameter of the event, in particular the probability of
the source direction and the coherent network signal-to-noise ratio. The
largest likelihood value is used to assign detection significance to the found
events.

**oLIB** [#oLIB]_ uses the Q transform to decompose GW strain data into several
time-frequency planes of constant quality factors :math:`Q`, where :math:`Q
\sim \tau f_0`. The pipeline flags data segments containing excess power and
searches for clusters of these segments with identical :math:`f_0` and
:math:`Q` spaced within 100 ms of each other. Coincidences among the detector
network of clusters within a 10 ms light travel time window are then analyzed
with a coherent (i.e., correlated across the detector network) signal model to
identify possible GW candidate events.

Coincident with External Trigger Search
---------------------------------------

**RAVEN** [#RAVEN]_ In addition, we will operate the Rapid On-Source VOEvent
Coincidence Monitor (RAVEN), a fast search for coincidences between GW and
non-GW events. RAVEN will process alerts for gamma-ray bursts (GRBs) from both
the *Fermi*-GBM instrument and the Neil Gehrels Swift Observatory, as well as
galactic supernova alerts from the SNEWS collaboration. Two astronomical events
are considered coincident if they are within a particular time window of each
other, which varies depending on which two types of events are being considered
(see the table below). Note that these time windows are centered on the GW,
e.g., [-1,5] s means we consider GRBs up to one second before or up to 5
seconds after the GW.

+-----------------------+-----------+-----------+-----------------------------------------------------------------+
| Event Type            | Time window (s)       |     | Notice Type Considered                                    |
|                       |                       |     | (`see full list`_)                                        |
|                       +-----------+-----------+                                                                 |
|                       | CBC       | Burst     |     .. _see full list: http://gcn.gsfc.nasa.gov/filtering.html  |
+=======================+===========+===========+=================================================================+
| | GRB                 | [-1,5]    | [-60,600] |    | FERMI_GBM_ALERT                                            |
| | (*Fermi*, *Swift*)  |           |           |    | FERMI_GBM_FIN_POS                                          |
|                       |           |           |    | FERMI_GBM_FLT_POS                                          |
|                       |           |           |    | FERMI_GBM_GND_POS                                          |
|                       |           |           |    | FERMI_GBM_SUBTHRESH                                        |
|                       |           |           |    | SWIFT_BAT_GRB_ALERT                                        |
|                       |           |           |    | SWIFT_BAT_GRB_LC                                           |
+-----------------------+-----------+-----------+-----------------------------------------------------------------+
| | Low-energy Neutrinos| [-10,10]  | [-10,10]  |     SNEWS                                                       |
| | (SNEWS)             |           |           |                                                                 |
+-----------------------+-----------+-----------+-----------------------------------------------------------------+

In addition, RAVEN will calculate coincident :term:`FARs <FAR>`, one including
only timing information (temporal) and one including GRB/GW sky map information
(space-time) as well. RAVEN is currently under review and is planned to be able
to trigger preliminary alerts once this is finished.

**LLAMA** [#LLAMA1]_ [#LLAMA2]_ The `Low-Latency Algorithm for Multi-messenger
Astrophysics <http://gwhen.com>`__
is a an online search pipeline combining LIGO/Virgo GW triggers with High
Energy Neutrino (HEN) triggers from IceCube. It finds temporally-coincident
sub-threshold IceCube neutrinos and performs a detailed Bayesian significance
calculation to find joint GW+HEN triggers.

.. |apj| replace:: *Astrophys. J.*
.. |cqg| replace:: *Class. Quantum Grav.*
.. |prd| replace:: *Phys. Rev. D*

.. [#GstLAL1]
   Messick, C., Blackburn, K., Brady, P., et al. 2017, |prd|, 95, 042001.
   :doi:`10.1103/PhysRevD.95.042001`

.. [#GstLAL2]
   Sachdev, S., Caudill, S., Fong, H., et al. 2019.
   :arxiv:`1901.08580`

.. [#SPIIR]
   Hooper, S., Chung, S. K., Luan, J., et al. 2012, |prd|, 86, 024012.
   :doi:`10.1103/PhysRevD.86.024012`

.. [#SPIIRThesis]
   Chu, Q. 2017, Ph.D. Thesis, The University of Western Australia.
   https://api.research-repository.uwa.edu.au/portalfiles/portal/18509751

.. [#MBTA]
   Adams, T., Buskulic, D., Germain, V., et al. 2016, |cqg|, 33, 175012.
   :doi:`10.1088/0264-9381/33/17/175012`

.. [#PyCBC1]
   Nitz, A. H., Dal Canton, T., Davis, D. & Reyes, S. 2018, |prd|, 98, 024050.
   :doi:`10.1103/PhysRevD.98.024050`

.. [#PyCBC2]
   Dal Canton, T., & Harry, I. W. 2017.
   :arxiv:`1705.01845`

.. [#cWB]
   Klimenko, S., Vedovato, G., Drago, M., et al. 2016, |prd|, 93, 042004.
   :doi:`10.1103/PhysRevD.93.042004`

.. [#oLIB]
   Lynch, R., Vitale, S., Essick, R., Katsavounidis, E., & Robinet, F. 2017, |prd|, 95, 104046.
   :doi:`10.1103/PhysRevD.95.104046`

.. [#RAVEN]
   Urban, A. L. 2016, Ph.D. Thesis.
   https://dc.uwm.edu/etd/1218/

.. [#LLAMA1]
   Bartos, I., Veske, D., Keivani, A., et al. 2018.
   :arxiv:`1810.11467`

.. [#LLAMA2]
   Countryman, S., Keivani, A., Bartos, I., et al. 2019.
   :arxiv:`1901.05486`
