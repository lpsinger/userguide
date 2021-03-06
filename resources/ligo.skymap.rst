ligo.skymap: Advanced Python Tools for Probability Sky Maps
===========================================================

The :doc:`ligo.skymap <ligo.skymap:index>` Python package includes a number of
advanced tools for working with GW probability sky maps.

* Publication-quality astronomical mapmaking built on Astropy
  (:mod:`ligo.skymap.plot.allsky`)

  .. image:: https://lscsoft.docs.ligo.org/ligo.skymap/_images/allsky-1.png
     :alt: A figure made with ligo.skymap.plot.allsky

* Functions for manipulating distance posteriors (:mod:`ligo.skymap.distance`)

* Probabilistic airmass plots (:doc:`ligo-skymap-plot-airmass
  <ligo.skymap:tool/ligo_skymap_plot_airmass>`)

  .. image:: https://lscsoft.docs.ligo.org/ligo.skymap/_images/ligo_skymap_plot_airmass-1.png
     :alt: A probabilistic airmass plot.

* The rapid sky localization code :doc:`BAYESTAR <ligo.skymap:bayestar/index>`,
  which is used to produce the initial sky maps for CBC events but can also be
  used to create :doc:`simulated sky localizations
  <ligo.skymap:quickstart/bayestar-injections>`.

* The postprocessing tool that creates updated sky maps from :term:`MCMC`
  samples (:doc:`ligo-skymap-from-samples
  <ligo.skymap:tool/ligo_skymap_from_samples>`)
