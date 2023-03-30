Observing Capabilities
======================

This section summarizes the projected observing capabilities of the global
gravitational-wave detector network as of March 2023, superseding the Living
Review [#LivingReview]_ on prospects for observing and localizing
gravitational-wave transients with Advanced LIGO, Advanced Virgo, and KAGRA.

Timeline
--------

.. note::
   Check the :doc:`LIGO, Virgo, and KAGRA Observing Run Plans
   <observing-plan:index>` for the latest details on scheduling of the next
   observing run, which are summarized here.

The gravitational-wave observing schedule is divided into Observing Runs or
epochs of months to years of operation at fixed sensitivity, down time for
construction and commissioning, and transitional Engineering Runs between
commissioning and observing runs. The long-term observing schedule is shown
below. Since :term:`BNS` mergers are a well-studied class of gravitational-wave
signals, this figure gives the BNS :term:`range` *for highly confident
detections* in each observing run.

.. figure:: _static/ObsScen_timeline.*
   :alt: Long-term observing schedule

We plan that following a one-month engineering run, Observing Run 4 (O4) will
start on May 24. During O4, we expect that four facilities (:term:`LHO`,
:term:`LLO`, :term:`Virgo`, and :term:`KAGRA`) will observe for over 18 months
with one or two one-month breaks for maintenance. KAGRA will begin the run with
LIGO and Virgo and then return to extended commissioning to re-join with
greater sensitivity toward the end of O4.

Live Status
-----------

There are a handful of public web pages that report live status of the
LIGO/Virgo/KAGRA detectors and alert infrastructure.

*  | **Detector Status Portal**: Daily summary of detector performance.
   | https://www.gw-openscience.org/detector_status/

*  | **GWIStat**: Real-time detector up/down status.
   | https://ldas-jobs.ligo.caltech.edu/~gwistat/gwistat/gwistat.html

*  | **LIGO Data Grid Status**: Live dashboard showing up/down status of the
     detectors and online analyses. Status of the LIGO/Virgo/KAGRA alert
     pipeline is indicated by the "EMFollow" box.
   | https://monitor.ligo.org/gwstatus

Public Alert Rate and Localization Accuracy
-------------------------------------------

Here we provide predicted public alert rates, distances, and localization
uncertainties for :term:`BNS`, :term:`NSBH`, and :term:`BBH` mergers in O4 and
O5, based on a Monte Carlo simulation of detection and localization of events.

The methodology of the simulation is the same as described in [#LivingReview]_
and [#DataDrivenExpectations]_, although the GW detector network
configurations, sensitivity curves, astrophysical rates, and mass and spin
distributions have been updated.

**Source code to reproduce these simulations** is available at
https://github.com/lpsinger/observing-scenarios-simulations/tree/v2 or
https://doi.org/10.5281/zenodo.5206852.

**Sky localization FITS files** from these simulations are provided at
:doi:`10.5281/zenodo.7026209`.

Detection Threshold
~~~~~~~~~~~~~~~~~~~

The network :term:`SNR` threshold for detection was set to 8 in order to
approximately reproduce the rate of *public alerts that were sent in O3* (see
[#DataDrivenExpectations]_).

.. important::
   **This section predicts the rate of public alerts, not the rate of highly
   confident detections. Most public alerts do not survive as confident
   detections in the authoritative end-of-run LIGO/Virgo/KAGRA compact binary
   catalogs.**

   Previous versions of this User Guide used a network SNR threshold of
   12, which roughly corresponds to the single-detector SNR threshold that is
   assumed for the canonical BNS :term:`range` shown in the timeline figure
   above.

   The change in the detection threshold from 12 to 8 accounts for an increase
   in the predicted number of events by a factor of
   :math:`\sim (12/8)^3 = 3.375` over previous versions of this User Guide.

Detector Network
~~~~~~~~~~~~~~~~

The detector sensitivity curves used for the simulation are available in
:dcc:`T2200043-v3`. The filenames for each detector and observing run are given
in the table below.

+-----------------+--------------------------------+--------------------------------+
| Detector        | Observing run                                                   |
|                 +--------------------------------+--------------------------------+
|                 | O4                             | O5                             |
+=================+================================+================================+
| :term:`LHO`,    | :file:`aligo_O4high.txt`       | :file:`AplusDesign.txt`        |
| :term:`LLO`     |                                |                                |
+-----------------+--------------------------------+--------------------------------+
| :term:`Virgo`   | :file:`avirgo_O4high_NEW.txt`  | :file:`avirgo_O5low_NEW.txt`   |
+-----------------+--------------------------------+--------------------------------+
| :term:`KAGRA`   | :file:`kagra_10Mpc.txt`        | :file:`kagra_128Mpc.txt`       |
+-----------------+--------------------------------+--------------------------------+

These noise curves correspond to the high ends of the BNS ranges shown in the
timeline figure above, with the exception of Virgo in O5, for which it
represents the low end.

We assume that each detector has an independent observing duty cycle of 70%.

Source Distribution
~~~~~~~~~~~~~~~~~~~

We draw masses and spins of compact objects from a global maximum
*a posteriori* fit of all O3 compact binary observations [#O3b_pop]_. The
distribution and its parameters are described below.

.. rubric:: Masses

The 1D source-frame component mass distribution is the
"Power Law + Dip + Break" model based on [#Farah2021]_, and is given by:

.. math::
   \begin{aligned}
      p(m|\lambda) \propto &\,
      l(m|M_\mathrm{max},\eta_\mathrm{max})
      \times h(m|M_\mathrm{min},\eta_\mathrm{min})
      \times n(m| M^\mathrm{gap}_\mathrm{low}, M^\mathrm{gap}_\mathrm{high}, \eta_\mathrm{low}, \eta_\mathrm{high}, A) \\
         &\times\begin{cases}
            & \left(\frac{m}{M^\mathrm{gap}_\mathrm{high}}\right)^{\alpha_1}\text{ if }m < M^\mathrm{gap}_\mathrm{high} \\
            & \left(\frac{m}{M^\mathrm{gap}_\mathrm{high}}\right)^{\alpha_2}\text{ if }m \geq M^\mathrm{gap}_\mathrm{high} \\
         \end{cases},
   \end{aligned}

defined for :math:`1 \leq m / M_\odot \leq 100`. It consists of four terms:

*   a high-mass tapering function
    :math:`l(m|M_\mathrm{max},\eta_\mathrm{max}) = \left(1 + \left(m / M_\mathrm{max}\right)^{\eta_\mathrm{max}}\right)^{-1}`,
*   a low-mass tapering function
    :math:`h(m|M_\mathrm{min},\eta_\mathrm{min}) = 1 - l(m|M_\mathrm{min},\eta_\mathrm{min})`,
*   a function
    :math:`n(m| M^\mathrm{gap}_\mathrm{low}, M^\mathrm{gap}_\mathrm{high}, \eta_\mathrm{low}, \eta_\mathrm{high}, A) = 1 - A \, l(m|M^\mathrm{gap}_\mathrm{high}, \eta_\mathrm{high}) \, h(m|M^\mathrm{gap}_\mathrm{low}, \eta_\mathrm{low})`
    that suppresses masses in the hypothetical "mass gap" between NSs and BHs, and
*   a piecewise power law.

The joint 2D distribution of the primary mass :math:`m_1` and the secondary
mass :math:`m_2` builds on the 1D component mass distribution and adds a
pairing function that weights binaries by mass ratio:

.. math::
    p(m_1,m_2|\Lambda)\propto\, p(m=m_1|\lambda) p(m=m_2|\lambda) \left(\frac{m_2}{m_1}\right)^{\beta},

defined for
:math:`(m_1 \geq m_2) \cap ((m_1 \leq 60 M_\odot) \cup (m_2 \geq 2.5 M_\odot))`.
The two figures below show the 1D and joint 2D component mass distributions.

.. plot::
   :context: reset

   from matplotlib import pyplot as plt
   import numpy as np

   ALPHA_1 = -2.16
   ALPHA_2 = -1.46
   A = 0.97
   M_GAP_LO = 2.72
   M_GAP_HI = 6.13
   ETA_GAP_LO = 50
   ETA_GAP_HI = 50
   ETA_MIN = 50
   ETA_MAX = 4.91
   BETA = 1.89
   M_MIN = 1.16
   M_MAX = 54.38


   def lopass(m, m_0, eta):
      return 1 / (1 + (m / m_0)**eta)


   def hipass(m, m_0, eta):
      return 1 - lopass(m, m_0, eta)


   def bandpass(m, m_lo, m_hi, eta_lo, eta_hi, A):
      return 1 - A * hipass(m, m_lo, eta_lo) * lopass(m, m_hi, eta_hi)


   def pairing_function(m1, m2):
      m1, m2 = np.maximum(m1, m2), np.minimum(m1, m2)
      return np.where((m1 <= 60) | (m2 >= 2.5), (m2 / m1) ** BETA, 0)


   def mass_distribution_1d(m):
      return (
         bandpass(m, M_GAP_LO, M_GAP_HI, ETA_GAP_LO, ETA_GAP_HI, A) *
         hipass(m, M_MIN, ETA_MIN) *
         lopass(m, M_MAX, ETA_MAX) *
         (m / M_GAP_HI) ** np.where(m < M_GAP_HI, ALPHA_1, ALPHA_2)
      )


   def mass_distribution_2d(m1, m2):
      return (
         mass_distribution_1d(m1) *
         mass_distribution_1d(m2) *
         pairing_function(m1, m2)
      )


   # Plot 1D distribution of component mass.

   m = np.geomspace(1, 100, 200)
   fig, ax = plt.subplots()
   ax.set_xscale('log')
   ax.plot(m, m * mass_distribution_1d(m))
   ax.set_xlim(1, 100)
   ax.set_ylim(0, None)
   ax.set_xlabel(r'Component mass, $m$ ($M_\odot$)')
   ax.set_ylabel(r'$m \, p(m|\lambda)$')
   ax.set_yticks([])
   ax2 = ax.twiny()
   ax2.set_xlim(ax.get_xlim())
   ax2.set_xscale(ax.get_xscale())
   ax2.set_xticks([M_MIN, M_GAP_LO, M_GAP_HI, M_MAX])
   ax2.set_xticklabels([r'$M_\mathrm{min}$',
                        r'$M^\mathrm{gap}_\mathrm{low}$',
                        r'$M^\mathrm{gap}_\mathrm{high}$',
                        r'$M_\mathrm{max}$'])
   ax2.set_xticks([], minor=True)
   ax2.grid(axis='x')
   fig.show()

   # Plot joint 2D distribution of m1, m2.

   m1, m2 = np.meshgrid(m, m)
   fig, ax = plt.subplots(subplot_kw=dict(aspect=1))
   ax.set_xlim(1, 100)
   ax.set_ylim(1, 100)
   ax.set_xscale('log')
   ax.set_yscale('log')
   ax.set_xlabel(r'Primary mass, $m_1$ ($M_\odot$)')
   ax.set_ylabel(r'Secondary mass, $m_2$ ($M_\odot$)')
   img = ax.pcolormesh(m, m, m1 * m2 * mass_distribution_2d(m1, m2),
                       vmin=0, vmax=25, shading='gouraud', rasterized=True)
   cbar = plt.colorbar(img, ax=ax)
   cbar.set_label(r'$m_1 \, m_2 \, p(m_1, m_2 | \Lambda)$')
   cbar.set_ticks([])

   ax.fill_between([1, 100],
                   [1, 100],
                   [100, 100],
                   color='white', linewidth=0, alpha=0.75, zorder=1.5)
   ax.plot([1, 100], [1, 100], '--k')

   ax.annotate('',
               xy=(0.975, 1.025), xycoords='axes fraction',
               xytext=(1.025, 0.975), textcoords='axes fraction',
               ha='center', va='center',
               arrowprops=dict(
                   arrowstyle='->', shrinkA=0, shrinkB=0,
                   connectionstyle='angle,angleA=90,angleB=180,rad=7'))
   ax.text(0.975, 1.025, '$m_1 \geq m_2$ by definition  ',
           ha='right', va='center', transform=ax.transAxes, fontsize='small')

   fig.show()

.. rubric:: Spins

The spins of the binary component objects are isotropically oriented. Component
objects with masses less than 2.5 :math:`M_\odot` have spin magnitudes that are
uniformly distributed from 0 to 0.4, and components with greater masses have
spin magnitudes that are uniformly distributed from 0 to 1.

.. rubric:: Sky Location, orientation

Sources are isotropically distributed on the sky and have isotropically
oriented orbital planes.

.. rubric:: Redshift

Sources are uniformly distributed in differential comoving volume per unit
proper time.

.. rubric:: Rate

The total rate density of mergers, integrated across all masses and spins, is
set to :math:`240_{-140}^{+270}\,\mathrm{Gpc}^{-3}\mathrm{yr}^{-1}`
([#O3b_pop]_, Table II, first row, last column).

.. rubric:: Parameters

The parameters of the mass and spin distribution are given below.

+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| Parameter                            | Description                                                                       | Value                 |
+======================================+===================================================================================+=======================+
| :math:`\alpha_1`                     | Spectral index for the power law of the mass distribution at low mass             | -2.16                 |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`\alpha_2`                     | Spectral index for the power law of the mass distribution at high mass            | -1.46                 |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`\mathrm{A}`                   | Lower mass gap depth                                                              | 0.97                  |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`M^\mathrm{gap}_\mathrm{low}`  | Location of lower end of the mass gap                                             | 2.72 :math:`M_\odot`  |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`M^\mathrm{gap}_\mathrm{high}` | Location of upper end of the mass gap                                             | 6.13 :math:`M_\odot`  |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`\eta_\mathrm{low}`            | Parameter controlling how the rate tapers at the low end of the mass gap          | 50                    |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`\eta_\mathrm{high}`           | Parameter controlling how the rate tapers at the low end of the mass gap          | 50                    |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`\eta_\mathrm{min}`            | Parameter controlling tapering the power law at low mass                          | 50                    |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`\eta_\mathrm{max}`            | Parameter controlling tapering the power law at high mass                         | 4.91                  |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`\beta`                        | Spectral index for the power law-in-mass-ratio pairing function                   | 1.89                  |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`M_{\rm min}`                  | Onset location of low-mass tapering                                               | 1.16 :math:`M_\odot`  |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`M_{\rm max}`                  | Onset location of high-mass tapering                                              | 54.38 :math:`M_\odot` |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`a_{\mathrm{max, NS}}`         | Maximum allowed component spin for objects with mass :math:`< 2.5\, M_\odot`      | 0.4                   |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+
| :math:`a_{\mathrm{max, BH}}`         | Maximum allowed component spin for objects with mass :math:`\geq 2.5\, M_\odot`   | 1                     |
+--------------------------------------+-----------------------------------------------------------------------------------+-----------------------+

Summary Statistics
~~~~~~~~~~~~~~~~~~

The table below summarizes the estimated public alert rate and sky localization
accuracy in O4 and O5. All values are given as a 5% to 95% confidence
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
|                       | :math:`210    | :math:`8.6    | :math:`17.1   |
|                       | ^{+240}       | ^{+9.7}       | ^{+19.2}      |
|                       | _{-120}`      | _{-5.0}`      | _{-10.0}`     |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Sensitive volume: detection rate / merger rate**                  |
| | (Gpc\ :superscript:`3`, Monte Carlo uncertainty)                    |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HKLV      | :math:`0.172  | :math:`0.78   | :math:`15.15  |
|           |           | ^{+0.013}     | ^{+0.14}      | ^{+0.42}      |
|           |           | _{-0.012}`    | _{-0.13}`     | _{-0.41}`     |
+-----------+-----------+---------------+---------------+---------------+
| O5        | HKLV      | :math:`0.827  | :math:`3.65   | :math:`50.7   |
|           |           | ^{+0.044}     | ^{+0.47}      | ^{+1.2}       |
|           |           | _{-0.042}`    | _{-0.43}`     | _{-1.2}`      |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Annual number of public alerts**                                  |
| | (log-normal merger rate uncertainty :math:`\times` Poisson          |
|   counting uncertainty)                                               |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HKLV      | :math:`36     | :math:`6      | :math:`260    |
|           |           | ^{+49}        | ^{+11}        | ^{+330}       |
|           |           | _{-22}`       | _{-5}`        | _{-150}`      |
+-----------+-----------+---------------+---------------+---------------+
| O5        | HKLV      | :math:`180    | :math:`31     | :math:`870    |
|           |           | ^{+220}       | ^{+42}        | ^{+1100}      |
|           |           | _{-100}`      | _{-20}`       | _{-480}`      |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Median luminosity distance**                                      |
| | (Mpc, Monte Carlo uncertainty)                                      |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HKLV      | :math:`398    | :math:`770    | :math:`2685   |
|           |           | ^{+15}        | ^{+67}        | ^{+53}        |
|           |           | _{-14}`       | _{-70}`       | _{-40}`       |
+-----------+-----------+---------------+---------------+---------------+
| O5        | HKLV      | :math:`738    | :math:`1318   | :math:`4607   |
|           |           | ^{+30}        | ^{+71}        | ^{+77}        |
|           |           | _{-25}`       | _{-100}`      | _{-82}`       |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Median 90% credible area**                                        |
| | (deg\ :superscript:`2`, Monte Carlo uncertainty)                    |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HKLV      | :math:`1860   | :math:`2140   | :math:`1428   |
|           |           | ^{+250}       | ^{+480}       | ^{+60}        |
|           |           | _{-170}`      | _{-530}`      | _{-55}`       |
+-----------+-----------+---------------+---------------+---------------+
| O5        | HKLV      | :math:`2050   | :math:`2000   | :math:`1256   |
|           |           | ^{+120}       | ^{+350}       | ^{+48}        |
|           |           | _{-120}`      | _{-220}`      | _{-53}`       |
+-----------+-----------+---------------+---------------+---------------+
|                                                                       |
| | **Median 90% credible comoving volume**                             |
| | (10\ :superscript:`3` Mpc\ :superscript:`3`,                        |
|   Monte Carlo uncertainty)                                            |
|                                                                       |
+-----------+-----------+---------------+---------------+---------------+
| O4        | HKLV      | :math:`67.9   | :math:`232    | :math:`3400   |
|           |           | ^{+11.3}      | ^{+101}       | ^{+310}       |
|           |           | _{-9.9}`      | _{-50}`       | _{-240}`      |
+-----------+-----------+---------------+---------------+---------------+
| O5        | HKLV      | :math:`376    | :math:`1350   | :math:`8580   |
|           |           | ^{+36}        | ^{+290}       | ^{+600}       |
|           |           | _{-40}`       | _{-300}`      | _{-550}`      |
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

   See [#DistanceMeasuresInGWCosmology]_ for further discussion of cosmological
   distance measures as they relate to sensitivity figures of merit for
   gravitational-wave detectors.

**Sensitive volume** is the quotient of the rate of detected events per unit
observer time and the merger rate per unit comoving volume per unit proper
time. The definition is given in the glossary entry for :term:`sensitive
volume`. To calculate the detection rate, multiply the merger rate by the
sensitive volume.

The quoted confidence interval represents the uncertainty from the Monte Carlo
simulation.

**Annual number of public alerts** is the number of alerts in one calendar
year of observation. The quoted confidence interval incorporates both the
log-normal distribution of the merger rate *and* Poisson counting statistics,
but does not include the Monte Carlo error (which is negligible compared to the
first two sources of uncertainty).

The remaining sections all give median values over the population of detectable
events.

**Median luminosity distance** is the median luminosity distance in Mpc of
detectable events. The quoted confidence interval represents the uncertainty
from the Monte Carlo simulation.

.. note::
   Although the luminosity distances for BNSs in the table above are about
   twice as large as the BNS :term:`ranges <range>` in the figure in the
   :ref:`capabilities:Timeline` section, the median luminosity distances should
   be better predictors of the typical distances of events that will be
   detectable during the corresponding observing runs.

   The reason is that the BNS range is a characteristic distance for a single
   GW detector, not a network of detectors. LIGO, Virgo, and KAGRA as a network
   are sensitive to a greater fraction of the sky and a greater fraction of
   binary orientations than any single detector alone.

**Median 90% credible area** is the area in deg\ :math:`^2` of the smallest
(not necessarily simply connected) region on the sky that has a 90% chance of
containing the true location of the source.

**Median 90% credible volume** is the median comoving volume enclosed in the
smallest region of space that has a 90% chance of containing the true location
of the source.

Cumulative Histograms
~~~~~~~~~~~~~~~~~~~~~

Below are cumulative histograms of the 90% credible area, 90% credible comoving
volume, and luminosity distance of detectable events in O3, O4, and O5.

.. figure:: _static/annual-predictions.*

   Cumulative annual public alert rate of simulated mergers as a function of 90%
   credible area (left column), 90% credible comoving volume (middle column),
   or luminosity distance (right column). Rates are given for three
   sub-populations: BNS (top row), NSBH (middle row), and BBH (bottom row).
   The shaded bands give the inner 90% confidence interval including
   uncertainty in the estimated merger rate, Monte Carlo uncertainty from the
   finite sample size of the simulation, and Poisson fluctuations in the number
   of sources detected in one year.

   This plot is based on Figure 2 of [#DataDrivenExpectations]_ but uses the
   simulations described above employing the mass and spin distributions from
   [#O3b_pop]_.

.. include:: /journals.rst

.. [#LivingReview]
   Abbott, B. P., Abbott, R., Abbott, T. D., et al. 2020, |LRR|, 23, 3.
   :doi:`10.1007/s41114-020-00026-9`

.. [#DataDrivenExpectations]
   Petrov, P., Singer, L. P., Coughlin, M. W., et al. 2022, |ApJ| 924, 54.
   :doi:`https://doi.org/10.3847/1538-4357/ac366d`

.. [#O3b_pop]
   LIGO Scientific Collaboration & Virgo Collaboration 2021, *The population of
   merging compact binaries inferred using gravitational waves through GWTC-3*.
   :arxiv:`2111.03634`

.. [#Farah2021]
   Farah, A., Fishbach, M., et al. 2022, *Bridging the Gap: Categorizing
   Gravitational-wave Events at the Transition between Neutron Stars and Black
   Holes*. |ApJ|, 931, 108. :doi:`10.3847/1538-4357/ac5f03`

.. [#DistanceMeasuresInGWCosmology]
   Chen, H.-Y., Holz, D. E., et al. 2017, *Distance measures in
   gravitational-wave astrophysics and cosmology*. :arxiv:`1709.08079`
