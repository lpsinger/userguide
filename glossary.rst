Glossary
========

.. glossary::

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

    CBC
        Compact binary coalescence.

    FAR
        False alarm rate, a statistic that is used to describe the significance
        of a gravitational-wave event. It is defined as the rate of accidental
        events due to detector noise or glitches, in the absence of any
        astrophysical sources, that are as loud as or louder than the event in
        question.

    FITS
        Flexible Image Transport System, a format for astronomical tables,
        images, and multidimensional data sets. See NASA's FITS Support Office
        (https://fits.gsfc.nasa.gov) for specifications, software, and
        documentation.

    GCN
        The Gamma-ray Coordinates Network (https://gcn.gsfc.nasa.gov), a portal
        for discoveries and observations of astronomical transients.
        Historically, GCN has served high-energy satellites but now also other
        electromagnetic wavelengths and also gravitational-wave, cosmic ray,
        and neutrino facilities.

    GCN Circular
        A human-readable astronomical bulletin distributed through :term:`GCN`.

    GCN Notice
        A machine-readable alert distributed through :term:`GCN`.

    GraceDB
        Gravitational Wave Candidate Event Database (https://gracedb.ligo.org),
        the official public marshal portal for LIGO/Virgo candidates.

    GRB
        Gamma-ray burst.

    HEALPix
        Hierarchical Equal Area isoLatitude Pixelation, a scheme for indexing
        positions on the unit sphere. See https://healpix.sourceforge.io.

    HEN
        High Energy Neutrino, particularly in the context of multi-messenger
        GW+HEN follow-up.

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
        detector to a given source population at cosmologically significant
        distances. It is defined as the radius :math:`R` of a Euclidean sphere
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
        detection. The factor of :math:`{1 + z}` in the denominator accounts
        for time dilation from the source frame to the detector frame.

        If a population of sources occurs at a fixed rate per unit comoving
        volume per unit proper time :math:`\dot{n}`, then the rate of observed
        events in the detector frame is :math:`\dot{n} V_z`.

    SN
        Supernova.

    SNR
        Signal-to-noise ratio, here applied to gravitational-wave signals. It
        is defined the square root of the integral over frequency of the power
        spectral density of the gravitational-wave signal over the integral
        over frequency of the average power spectral density of the noise.

    Terrestrial
        Classification for signals in gravitational-wave detectors that are of
        instrumental or environmental origin. Terrestrial signals are not
        astrophysical and not due to gravitational waves. Some examples of
        sources of terrestrial signals are statistical noise fluctuations,
        detector glitches, and ground motion.

    Virgo
        Virgo Observatory (see `Virgo observatory home page
        <http://www.virgo-gw.eu>`_), site of a 3 km gravitational-wave detector
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

.. [#DistanceMeasuresInGWCosmology]
   Chen, H.-Y., Holz, D. E., et al. 2017, *Distance measures in
   gravitational-wave astrophysics and cosmology*. :arxiv:`1709.08079`
