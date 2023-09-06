Glossary
========

.. glossary::

    Avro
        Apache Avro is an open, binary data serialization format. See
        https://avro.apache.org for more information.

    Base64
        A common binary encoding scheme supported by many open-source libraries, e.g. the `Python standard library <https://docs.python.org/3/library/base64.html>`_.

    BBH
        Binary black hole, a binary system composed of two black holes. See
        :term:`BH`.

    BH
        Black hole.

    BNS
        Binary neutron star, a binary system composed of two neutron stars.
        See :term:`NS`.

    burst
        In the context of gravitational waves, a signal candidate that is
        detected without a template and without prior knowledge of the
        waveform. Examples of potential sources of gravitational-wave bursts
        include high mass :term:`BBH` mergers, core-collapse supernovae, and
        cosmic string cusps.

    chirp mass
        In a binary system, the chirp mass is a symmetric combination of the
        :term:`primary` and :term:`secondary` component masses :math:`m_1` and
        :math:`m_2` that parameterizes the leading-order time or frequency
        evolution of the gravitational-wave signal. It is usually denoted by a
        script "M" symbol, :math:`\mathcal{M}`, and is defined as
        :math:`\mathcal{M} = (m_1 m_2)^{3/5} (m_1 + m_2)^{-1/5}`.

    CBC
        Compact binary coalescence.

    EOS
        Equation of state. The equation of state determines the relation between
        mass and radius, or mass and compactness, or pressure and (mass, energy,
        or number) density, of neutron stars.
    
    FAP
        False alarm probability, a measure of the fraction of noise events 
        incorrectly classified as astrophysical events by a binary classifier.
        
    FNP
        False negative probability, a measure of the fraction of astrophysical 
        events incorrectly classified as noise by a binary classifier.

    FAR
        False alarm rate, a statistic that is used to describe the significance
        of a gravitational-wave event. See section
        :ref:`false alarm rate (FAR) <far-significance>` for details.
        FAR has units of frequency (one over time).

    FITS
        Flexible Image Transport System, a format for astronomical tables,
        images, and multidimensional data sets. See NASA's FITS Support Office
        (https://fits.gsfc.nasa.gov) for specifications, software, and
        documentation.

    GCN
        The General Coordinates Network (https://gcn.nasa.gov), a NASA-hosted
        public portal for discoveries and observations of astronomical transients.
        GCN hosts one of the :term:`Kafka` brokers used to distribute
        LIGO/Virgo/KAGRA alerts.
        See https://gcn.nasa.gov.

    GCN Circular
        A human-readable astronomical bulletin distributed through :term:`GCN`.

    GraceDB
        Gravitational Wave Candidate Event Database (https://gracedb.ligo.org),
        the official public marshal portal for LIGO/Virgo/KAGRA candidates.

    GRB
        Gamma-ray burst.
        
    GWSkyNet
        A machine learning classifier for the identification of multi-detector 
        :term:`CBC` events and noise [#GWSkyNet]_. See section 
        :ref:`GWSkyNet classification <gwskynetclass>` for details.

    HEALPix
        Hierarchical Equal Area isoLatitude Pixelation, a scheme for indexing
        positions on the unit sphere. See https://healpix.sourceforge.io.

    HEN
        High Energy Neutrino, particularly in the context of multi-messenger
        GW+HEN follow-up.

    JSON
        JavaScript Object Notation is an open data serialization format.
        JSON-serialized data look like JavaScript literals. See
        https://json.org for more information.

    Kafka
        Apache Kafka is an open-source distributed event streaming platform.
        See https://kafka.apache.org for more information.

    KAGRA
        Kamioka Gravitational Wave Detector (see `KAGRA home page
        <https://gwcenter.icrr.u-tokyo.ac.jp/en/>`_), an underground
        gravitational-wave detector in the Kamioka mine in Japan.

    LHO
        LIGO Hanford Observatory (see `LHO observatory home page
        <https://www.ligo.caltech.edu/WA>`_), site of a 4 km gravitational-wave
        detector in Hanford, Washington, USA.

    LLO
        LIGO Livingston Observatory (see `LLO observatory home page
        <https://www.ligo.caltech.edu/LA>`_), site of a 4 km gravitational-wave
        detector in Livingston, Louisiana, USA.

    MassGap
        Compact binary systems with at least one compact object whose mass is
        in the hypothetical "mass gap" between neutron stars and black holes,
        defined here as 3-5 solar masses.

    MCMC
        Markov chain Monte Carlo. A numerical algorithm for sampling complex,
        multidimensional probability distributions, or for integrating
        functions of many variables. Used extensively in gravitational-wave
        parameter estimation.

    MOC
        Multi-Order Coverage map, a format to describe the coverage of an
        arbitrary region on the unit sphere. A MOC consists of a list of
        :term:`HEALPix` cells at different depths. For the specification, see
        the `HiPS IVOA Recommendation <http://www.ivoa.net/documents/HiPS/>`_.

    Notice
        A machine-readable alert distributed through :term:`GCN` or
        :term:`SCiMMA`.

    NS
        Neutron star.

    NSBH
        Neutron star black hole, a binary system composed of one neutron star
        and one black hole. See :term:`NS`, :term:`BH`.

    O1
        Advanced LIGO and Advanced Virgo's first observing run.

    O2
        Advanced LIGO and Advanced Virgo's second observing run.

    O3
        Advanced LIGO and Advanced Virgo's third observing run.

    primary
        When referring to the two component compact objects or the masses of
        the two component compact objects in a binary, the `primary` is the
        more massive one, i.e., :math:`m_1 \geq m_2`. See :term:`secondary`.

    range
        A figure of merit to describe the sensitivity of a gravitational-wave
        detector to a given source population that is uniformly distributed in
        volume. It is defined as the radius :math:`R` of a Euclidean sphere
        with the volume equal to the :term:`sensitive volume` :math:`V_z`. It
        may be written as:

        .. math::

           R = \left(\frac{3 V_z}{4 \pi}\right)^{1/3}.

    secondary
        When referring to the two component compact objects or the masses of
        the two component compact objects in a binary, the `secondary` is the
        less massive one, i.e., :math:`m_2 \leq m_1`. See :term:`primary`.

    sensitive volume
        A figure of merit for the sensitivity of a gravitational-wave detector
        or a network of detectors. It is defined as the space-time volume
        surveyed per unit detector time, and may be expressed as (cf.
        [#DistanceMeasuresInGWCosmology]_):

        .. math::

           V_\mathrm{z}
               = \frac{
                   \int_{z < z^*(\Theta)} p(\Theta) \frac{dV_C}{dz} \frac{dz}{1 + z}
               }{\int p(\Theta) d\Theta}.

        Here, :math:`\Theta` is the set of parameters that describe the
        gravitational-wave signal (merger time, sky location, orbital elements,
        masses, and spins) and :math:`p(\Theta)` is the redshift-independent
        population model for those parameters. The term :math:`\frac{dV_C}{dz}`
        is differential comoving volume per unit redshift. The function
        :math:`z^*(\Theta)` is the *threshold redshift*, or the redshift at
        which a binary with parameters :math:`\Theta` is just at the limit of
        detection. Detection may be defined, for instance, by a threshold on
        event SNR or FAR; see :ref:`capabilities:Detection Threshold` for
        thresholds used in this guide. The factor of :math:`{1 + z}` in the
        denominator accounts for time dilation from the source frame to the
        detector frame.

        If a population of sources occurs at a fixed rate per unit comoving
        volume per unit proper time :math:`\dot{n}`, then the rate of observed
        events in the detector frame is :math:`\dot{n} V_z`.

    SN
        Supernova.

    SNR
        Signal-to-noise ratio, here applied to gravitational-wave signals. It
        is defined as the square root of the integral over frequency of the
        power spectral density of the gravitational-wave signal divided by the
        integral over frequency of the average power spectral density of the
        noise.

    source-frame mass
        Since observed frequencies of distant sources are subject to redshift by
        :math:`f_\mathrm{obs} = (1 + z)^{-1} f_\mathrm{source}`, and gravitational-wave
        frequency scales inversely with mass, the observer- and source-frame masses
        are related by :math:`m_\mathrm{obs} = (1 + z) m_\mathrm{source}`.

    Terrestrial
        Classification for signals in gravitational-wave detectors that are of
        instrumental or environmental origin. Terrestrial signals are not
        astrophysical and not due to gravitational waves. Some examples of
        sources of terrestrial signals are statistical noise fluctuations,
        detector glitches, and ground motion.

    SCiMMA
        Scalable Cyberinfrastructure to support Multi-Messenger Astrophysics.
        SCiMMA hosts one of the :term:`Kafka` brokers used to distribute
        LIGO/Virgo/KAGRA alerts. See https://scimma.org.

    Virgo
        Virgo Observatory (see `Virgo observatory home page
        <https://www.virgo-gw.eu>`_), site of a 3 km gravitational-wave detector
        in Cascina, Italy.

    VOEvent
        An XML format for describing astronomical transients. For the
        specification, see the official `VOEvent IVOA Recommendation
        <http://www.ivoa.net/documents/VOEvent/index.html>`_.

    VTP
        VOEvent Transport Protocol, a simple TCP-based protocol for sending and
        receiving VOEvents, used by :term:`GCN`. For the specification, see the
        official `VTP IVOA recommendation
        <http://www.ivoa.net/documents/Notes/VOEventTransport/>`_.

.. include:: /journals.rst

.. [#GWSkyNet]
   Cabero, M., Mahabal, A. and McIver, J. 2020, |ApJL|, 904, L9.
   :doi:`10.3847/2041-8213/abc5b5`

.. [#DistanceMeasuresInGWCosmology]
   Chen, H.-Y., Holz, D. E., et al. 2017, *Distance measures in
   gravitational-wave astrophysics and cosmology*. :arxiv:`1709.08079`   
