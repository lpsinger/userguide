Source Classification
=====================

For the computation of the EM-Bright probability we use a fitting formula
proposed by Foucart, Hinderer and Nissanke (arXiv:1807.00011). Both the
EM-Bright probability and the probability of the secondary object being a
neutron star are computed for the detection pipeline point estimates. We are in
the process of integrating a new functionality that will allow supervised
learning to compute the probabilities in a robust fashion. This improves the
previous method based on ellipsoids on multiple counts. First, it could be
several orders of magnitude faster. The ellipsoid method could take as much as
tens of minutes for low mass systems, while the supervised learning method
computes the probability practically instantaneously. Second, the supervised
learning method shows evidence of being more robust to pipeline systematics.
Third, supervised learning will enable us to incorporate rates of events from
the "P_astro" pipeline directly in the training process. This method requires
injection campaigns for training.

P_astro computes the posterior conditional probability that a candidate event
is of astrophysical origin, given a list of triggers, assuming that terrestrial
and astrophysical events occur as independent Poisson processes. In addition,
with the help of mass-based template-weights computed using either injection
campaigns or some other possibly analytical method, this astrophysical
probability is redistributed across CBC source-types, viz. BNS, NSBH and BBH.
There are two aspects to the computation of P_astro. The first involves the
computation of the mean values of the Poisson expected counts for each
source-category, using all available triggers above a predefined
ranking-statistic threshold. This is planned to take place once a week during
maintenance of detectors. The second involves using these mean values to
compute astrophysical probabilities for each new candidate event -- this step
is what determines the latency of P_astro, which is negligible ( << 1 second)

We plan to combine P_astro and EM-Bright under one umbrella of source
classification in the near future. The probability of the presence of neutron
star in the binary from the EM-Bright pipeline and the source type
classification (BNS/NSBH/BBH) from the P_astro pipeline will be used for
consistency checks.
