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

.. _far-significance:

False alarm rate and significance
---------------------------------

Each search produces a set of candidate events time-stamped at or close to
the estimated peak of GW strain amplitude. For binary merger candidates,
this would be the time of merger.

Each candidate event is assigned a ranking statistic value by the search
pipeline that produced it: higher statistic values correspond to a higher
probability of astrophysical (signal), as opposed to terrestrial (noise)
origin. The statistical significance of a candidate produced by a given
pipeline is quantified by its :term:`false alarm rate <FAR>`. This is the
expected number of events of noise origin produced by the pipeline with a
higher ranking statistic than the candidate, per unit of time searched.
Since each search pipeline has an independent method of generating and ranking
events, and of estimating the noise background, the false alarm rates assigned
for events in the same superevent will in general be different. For an alert
to be sent automatically, we require at least one event to have a false alarm
rate below the :ref:`alert threshold <alert-threshold>`.

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
to compute a :term:`FAR` and a p-value. The template bank being used by GstLAL
in O4 is described in [#GstLAL3]_.

**MBTA** [#MBTA1]_ [#MBTA2]_ constructs its background by making every possible
coincidence from single detector triggers over a few hours of recent data. It
then folds in the probability of a pair of triggers passing the time
coincidence test.

**PyCBC Live** [#PyCBC1]_ [#PyCBC2]_ estimates the noise background by
performing time-shifted analyses using triggers from a few hours of recent
data. Single-detector triggers from one detector are time shifted by every
possible multiple of 100 ms, thus any resulting coincidence must be unphysical
given the :math:`\sim 10` ms light travel time between detectors. All such
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

**cWB** [#cWB1]_ [#cWB2]_ searches for and reconstructs gravitational-wave
transient signals without relying on a specific waveform model. cWB searches
for signals with durations of up to a few seconds that are coincident in
multiple detectors. The analysis is performed on the time-frequency data
obtained with a wavelet transform. cWB selects wavelet amplitudes above the
fluctuations of the detector noise and groups them into clusters. Tuned
versions for binary black holes (search name BBH and IMBH) choose
time-frequency patterns with frequency increasing in time. For clusters
correlated in multiple detectors, cWB reconstructs the direction to the source
and the signal waveforms with the constrained maximum likelihood method. To
assign detection significance to the found events, cWB ranks them by the
coherent signal-to-noise ratio obtained from cross-correlation of the signal
waveforms reconstructed in different detectors.

**oLIB** [#oLIB]_ uses the Q transform to decompose GW strain data into several
time-frequency planes of constant quality factors :math:`Q`, where :math:`Q
\sim \tau f_0`. The pipeline flags data segments containing excess power and
searches for clusters of these segments with identical :math:`f_0` and
:math:`Q` spaced within 100 ms of each other. Coincidences among the detector
network of clusters within a 10 ms light travel time window are then analyzed
with a coherent (i.e., correlated across the detector network) signal model to
identify possible GW candidate events.

.. 
	**MLy** ("Emily") [#MLy]_ is a machine-learning-based search for generic
	sub-second-duration transient gravitational wave signals in the 20 Hz to 500 Hz
	frequency band. MLy works by passing data from the Hanford-Livingston-Virgo or
	Hanford-Livingston networks through a pair of convolutional neural networks (CNNs)
	trained to recognize signals that are simultaneous (up to the light travel time
	across the network) and coherent between detectors. The training uses randomly
	generated test signals rather than specific signal models, giving MLy sensitivity
	to a wide range of signal morphologies. Events are ranked by their combined CNN
	scores. MLy constructs a sky map of the direction to the source using
	a maximum-likelihood approach.

Coincident with External Trigger Search
---------------------------------------

**RAVEN** [#RAVEN]_ In addition, we will operate the Rapid On-Source VOEvent
Coincidence Monitor (RAVEN), a fast search for coincidences between GW and
non-GW events. RAVEN will process alerts for gamma-ray bursts (GRBs) from the
Gamma-ray Burst Monitor (GBM) onboard Fermi, the Burst Alert Telescope (BAT)
onboard the Neil Gehrels Swift Observatory, and the Mini-Calorimeter (MCAL)
onboard AGILE, as well as galactic supernova alerts from the
SNEWS collaboration. Two astronomical events
are considered coincident if they are within a particular time window of each
other, which varies depending on which two types of events are being considered
(see the table below). Note that these time windows are centered on the GW,
e.g., [-1,5] s means we consider GRBs up to one second before or up to 5
seconds after the GW.

+-----------------------+-----------+-----------+---------------------------+
| Event Type            | Time window (s)       |  Notice Type Considered   |
|                       |                       |  (`see full list`_)       |
|                       +-----------+-----------+                           |
|                       | CBC       | Burst     |                           |
+=======================+===========+===========+===========================+
| | GRB                 | [-1,5]    | [-60,600] |    | FERMI_GBM_ALERT      |
| | (*Fermi*, *Swift*,  |           |           |    | FERMI_GBM_FIN_POS    |
|    *INTEGRAL*,        |           |           |    | FERMI_GBM_FLT_POS    |
|    *AGILE*)           |           |           |    | FERMI_GBM_GND_POS    |
|                       |           |           |    | FERMI_GBM_SUBTHRESH  |
|                       |           |           |    | SWIFT_BAT_GRB_ALERT  |
|                       |           |           |    | SWIFT_BAT_GRB_LC     |
|                       |           |           |    | INTEGRAL_WAKEUP      |
|                       |           |           |    | INTEGRAL_REFINED     |
|                       |           |           |    | INTEGRAL_OFFLINE     |
|                       |           |           |    | AGILE_MCAL_ALERT     |
+-----------------------+-----------+-----------+---------------------------+
| | Low-energy Neutrinos| [-10,10]  | [-10,10]  |     SNEWS                 |
| | (SNEWS)             |           |           |                           |
+-----------------------+-----------+-----------+---------------------------+

In addition, RAVEN will calculate coincident :term:`FARs <FAR>`, one including
only timing information (temporal) and one including GRB/GW sky map information
(space-time) as well. RAVEN is currently under review and is planned to be able
to trigger preliminary alerts once this is finished.

**LLAMA** [#LLAMA1]_ [#LLAMA2]_ The `Low-Latency Algorithm for Multi-messenger
Astrophysics`_ is a an online search pipeline combining LIGO/Virgo/KAGRA GW
triggers with High Energy Neutrino (HEN) triggers from IceCube. It finds
temporally-coincident sub-threshold IceCube neutrinos and performs a detailed
Bayesian significance calculation to find joint GW+HEN triggers.

.. _`Low-Latency Algorithm for Multi-messenger Astrophysics`: https://multimessenger.science
.. _see full list: https://gcn.gsfc.nasa.gov/filtering.html

.. include:: /journals.rst

.. [#GstLAL1]
   Messick, C., Blackburn, K., Brady, P., et al. 2017, |PRD|, 95, 042001.
   :doi:`10.1103/PhysRevD.95.042001`

.. [#GstLAL2]
   Sachdev, S., Caudill, S., Fong, H., et al. 2019.
   :arxiv:`1901.08580`

.. [#GstLAL3]
   Sakon, S., Tsukada, L., Fong, H., et al. 2023.
   :arxiv:`2211.16674`

.. [#SPIIR]
   Hooper, S., Chung, S. K., Luan, J., et al. 2012, |PRD|, 86, 024012.
   :doi:`10.1103/PhysRevD.86.024012`

.. [#SPIIRThesis]
   Chu, Q. 2017, Ph.D. Thesis, The University of Western Australia.
   https://api.research-repository.uwa.edu.au/portalfiles/portal/18509751

.. [#MBTA1]
   Aubin, F., Brighenti, F., Chierici, R. et al. 2021, |CQG|, 38, 095004.
   :doi:`10.1088/1361-6382/abe913`

.. [#MBTA2]
   Andres, N., Assiduo, M., Aubin, F. et al. 2022, |CQG|, 39, 055002.
   :doi:`10.1088/1361-6382/ac482a`

.. [#PyCBC1]
   Nitz, A. H., Dal Canton, T., Davis, D. & Reyes, S. 2018, |PRD|, 98, 024050.
   :doi:`10.1103/PhysRevD.98.024050`

.. [#PyCBC2]
   Dal Canton, T., Nitz, A. H., Gadre, B., et al. 2021, |ApJ|, 923, 254.
   :doi:`10.3847/1538-4357/ac2f9a`

.. [#cWB1]
   Klimenko, S., Mohanty, S., Rakhmanov, M., Mitselmakher, |PRD|,  72, 122002.
   :doi:`10.1103/PhysRevD.72.122002`

.. [#cWB2]
   Klimenko, S., Vedovato, G., Drago, M., et al. 2016, |PRD|, 93, 042004.
   :doi:`10.1103/PhysRevD.93.042004`

.. [#oLIB]
   Lynch, R., Vitale, S., Essick, R., Katsavounidis, E., & Robinet, F. 2017, |PRD|, 95, 104046.
   :doi:`10.1103/PhysRevD.95.104046`

.. [#MLy]
   Skliris, V., Norman, M., Sutton, P. 2022,
   :arXiv:`2009.14611`

.. [#RAVEN]
   Urban, A. L. 2016, Ph.D. Thesis.
   https://dc.uwm.edu/etd/1218/

.. [#LLAMA1]
   Bartos, I., Veske, D., Keivani, A., et al. 2019, |PRD|, 100, 083017.
   :doi:`10.1103/PhysRevD.100.083017`

.. [#LLAMA2]
   Countryman, S., Keivani, A., Bartos, I., et al. 2019.
   :arxiv:`1901.05486`
