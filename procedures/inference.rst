Inference
=========

P_astro
-------

**P_astro** gives the categorical (BBH, BNS, NSBH) posterior probabilities
that a candidate event is of astrophysical origin. The underlying principle
involves:

* The assumption that terrestrial and astrophysical events occur as
  independent Poisson processes.
 
* Mass-based weighting of templates, which are used to compute the
  mean of the expected counts associated with the categories. These
  weights are dynamic and are determined on a weekly basis.

* The mean values are then used to predict the category for a
  new trigger uploaded by :doc:`search pipelines </procedures/searches>`.


EM_Bright
---------
**EM-Bright** gives two probablities: that of the secondary object being
a neutron star, `HasNS` and that of having remnant matter after
merger, `HasRemnant`.

* For the computation of `HasNS`, we simply report the probability of
  the secondary mass component satifying, :math:`m_2 \leq 3 M_{\odot}`.

* For `HasRemnant`, we use a fitting formula for the remnant disk mass
  proposed by `Foucart et al. 2018`_ (see Eq. 4 therein).

* We use supervised learning to compute the probabilities.

* The training is done assuming rate of events reported by the **P_astro**.

.. _`Foucart et al. 2018`: https://arxiv.org/abs/1807.00011
