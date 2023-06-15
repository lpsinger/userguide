Sky Localization and Parameter Estimation
=========================================

Immediately after one of the :doc:`search pipelines <searches>` reports an
event, sky localization and parameter estimation analyses begin. These analyses
all use Bayesian inference to calculate the posterior probability distribution
over the parameters (sky location, distance, and/or intrinsic properties of the
source) given the observed gravitational-wave signal.

There are different parameter estimation methods for modeled (CBC) and
unmodeled (:term:`burst`) events. However, in both cases there is a rapid
analysis that estimates only the sky localization, and is ready in seconds, and
a refined analysis that explores a larger parameter space and completes up to
hours or a day later.

Modeled Events
--------------

**BAYESTAR** [#BAYESTAR]_ is the rapid CBC sky localization algorithm. It reads
in the matched-filter time series from the :doc:`search pipeline <searches>`
and calculates the posterior probability distribution over the sky location and
distance of the source by coherently modeling the response of the
gravitational-wave detector network. It explores the parameter space using
Gaussian quadrature, lookup tables, and sampling on an adaptively refined
:term:`HEALPix` grid. The sky localization takes tens of seconds and is
included in the preliminary alert.

**Bilby** [#Bilby]_ is a full CBC parameter estimation pipeline in Python.
Bilby provides a user-friendly and accessible interface with the latest
stochastic sampling methods built-in. It explores a greatly expanded parameter
space including sky location, distance, masses, and spins, and performs full
forward modeling of the gravitational-wave signal and the strain calibration of
the gravitational-wave detectors. It explores the parameter space using
stochastic sampling methods such as :term:`MCMC` and nested sampling.
For all events, there is an automated Bilby analysis whose settings
depend on the initial estimate of :term:`chirp mass` from the search pipeline.
The table below summarizes the waveform model and spin prior employed for
parameter estimation. The analysis is accelerated with the reduced order
quadrature basis elements constructed for the employed waveform models [#ROQ]_,
and completes within tens of minutes for :term:`BNS` and hours for :term:`NSBH`
and :term:`BBH`.

+-------------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------------------+
| Chirp-mass from the search pipeline                   | Waveform model                             | Spin prior                                                                        |
+=======================================================+============================================+===================================================================================+
| :math:`\mathcal{M} < 1.465M_{\odot}`                  | IMRPhenomD [#IMRPhenomD1]_ [#IMRPhenomD2]_ | Aligned with the orbital angular momentum, dimensionless magnitude from 0 to 0.05 |
+-------------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------------------+
| :math:`1.465M_{\odot} \leq \mathcal{M} < 12M_{\odot}` | IMRPhenomPv2 [#IMRPhenomPv2]_              | Any orientation, dimensionless magnitude from 0 to 0.99                           |
+-------------------------------------------------------+--------------------------------------------+                                                                                   |
| :math:`\mathcal{M} \geq 12M_{\odot}`                  | IMRPhenomXPHM [#IMRPhenomXPHM]_            |                                                                                   |
+-------------------------------------------------------+--------------------------------------------+-----------------------------------------------------------------------------------+

Unmodeled Events
----------------

**cWB**, the burst :doc:`search pipeline <searches>`, also performs a rapid sky
localization based on its coherent reconstruction of the gravitational-wave
signal using a wavelet basis and the response of the gravitational-wave
detector network [#cWBLocalization]_. The cWB sky localization is included in
the preliminary alert.

Refined sky localizations for unmodeled bursts are provided by two algorithms
that, like Bilby, use :term:`MCMC` and nested sampling methodologies.
**LALInference Burst (LIB)** [#oLIB]_ models the signal as a single
sinusoidally modulated Gaussian. **BayesWave** [#BayesWave]_ models the signal
as a superposition of wavelets and jointly models the background with both a
stationary noise component and glitches composed of wavelets that are present
in individual detectors.

.. include:: /journals.rst

.. [#BAYESTAR]
   Singer, L. P., & Price, L. R. 2016, |PRD|, 93, 024013.
   :doi:`10.1103/PhysRevD.93.024013`

.. [#Bilby]
   Ashton, G., Hübner, M., Lasky, P. D., Talbot, C., et al. 2019, |ApJS|, 241, 27.
   :doi:`10.3847/1538-4365/ab06fc`

.. [#IMRPhenomD1]
   Husa, S., et al. 2016, |PRD|, 93, 044006.
   :doi:`10.1103/PhysRevD.93.044006`

.. [#IMRPhenomD2]
   Khan, S., et al. 2016, |PRD|, 93, 044007.
   :doi:`10.1103/PhysRevD.93.044007`

.. [#IMRPhenomPv2]
   Hannam, M., et al. 2014, |PRL|, 113, 151101.
   :doi:`10.1103/PhysRevLett.113.151101`

.. [#IMRPhenomXPHM]
   Pratten, G., et al. 2021, |PRD|, 103, 104056.
   :doi:`10.1103/PhysRevD.103.104056`

.. [#ROQ]
   Morisaki, S., Smith, R., et al. 2023, arXiv:`2307.13380`.
   :doi:`10.48550/arXiv.2307.13380`

.. [#cWBLocalization]
   Klimenko, S., Vedovato, G., Drago, M., et al. 2011, |PRD|, 83, 102001.
   :doi:`10.1103/PhysRevD.83.102001`

.. [#oLIB]
   Lynch, R., Vitale, S., Essick, R., Katsavounidis, E., & Robinet, F. 2017, |PRD|, 95, 104046.
   :doi:`10.1103/PhysRevD.95.104046`

.. [#BayesWave]
   Cornish, N. J., & Littenberg, T. B. 2015, |CQG|, 32, 135012.
   :doi:`10.1088/0264-9381/32/13/135012`
