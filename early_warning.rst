.. |deg2| replace:: deg\ :superscript:`2`

✨Early-Warning Alerts
======================

During O3, automated public alerts for :term:`CBC` events have been sent within
as little as 2 minutes after merger. However, some :term:`BNS` mergers are
detectable for up to tens of seconds *before* merger during the event's
inspiral phase during which the signal sweeps in frequency from tens of hertz
to kilohertz across LIGO's sensitive band.

Since it is generally assumed that detectable electromagnetic (or neutrino)
emission starts shortly *after* merger, a pre-merger gravitational-wave
detection would provide *early warning* of an impending electromagnetic
transient and might make it possible for automated follow-up facilities to
capture any prompt emission from the merger environment, the jet, and other
unknown activity.

**We have commissioned an experimental capability to produce and distribute
early warning gravitational-wave alerts up to tens of seconds before merger. We
have also reduced the latency of ordinary post-merger alerts to within tens of
seconds after merger.**

We are conducting a trial early warning public alert infrastructure. Since
production analysis had to be suspended due to COVID-19 pandemic, we are
replaying an 8-day period of saved LIGO data from O3 with a random (and
undisclosed) time shift. **Early-warning alerts arising from the replayed data
will be publicly distributed as test alerts at a rate of approximately once per
day**.

Subscribe to Early-Warning Alerts
---------------------------------

Early warning alerts are publicly distributed as :term:`GCN Notices <GCN
Notice>` just like ordinary gravitational-wave alerts (see the :doc:`content`
section). **They have exactly the same format and content** as a
:ref:`Preliminary GCN Notice <preliminary>`. In particular, early warning GCN
Notices have significance estimates, sky localizations, and source
classifications. Also, like Preliminary GCN Notices, **Early Warning GCN
Notices are sent prior to vetting by humans, and are not accompanied by a GCN
Circular.**

Early warning alerts are differentiated from ordinary alerts by the new
``LVC_EARLY_WARNING`` GCN Notice type. If you are receiving GCN Notices via an
anonymous VOEvent connection and you are using the Python sample code from the
:doc:`tutorial/receiving` section, then all you have to do is add the notice
type to your GCN handler::

    import gcn

    @gcn.handlers.include_notice_types(
        gcn.notice_types.LVC_EARLY_WARNING  # <-- new notice type here
        gcn.notice_types.LVC_PRELIMINARY,
        gcn.notice_types.LVC_INITIAL,
        gcn.notice_types.LVC_UPDATE,
        gcn.notice_types.LVC_RETRACTION)
    def process_gcn(payload, root):
        ...  # <-- put your code here

    gcn.listen(handler=process_gcn)

(If you are using a non-anonymous GCN connection or one of the many other
notice formats provided by GCN, then you will also need to `submit a change to
your GCN Notice subscription settings`_.)

.. important::
    Since these early-warning events will arise from time-shifted and replayed
    data and not live observations, the GCN notices will be flagged as test
    events by setting the VOEvent ``role="test"`` attribute.

Detection Method
----------------

Three :term:`CBC` search pipelines are participating in early-warning alerts:
GstLAL, SPIIR, and MBTA. See the :doc:`analysis/searches` section for details
on these analyses. Localizations will be produced with BAYESTAR; see the
:doc:`analysis/parameter_estimation` section for details.

.. note::
    The following material describes the detection method and simulated
    observing capabilities with GstLAL, but is also broadly applicable to
    SPIIR and MBTA.

:term:`BNS` signals sweep up smoothly in frequency for a few minutes across the
Advanced LIGO band. In that time, they may accumulate enough SNR to be detected
before merger. A GW170817-like system with a total network SNR of 32 will
already accumulate an SNR of 11 by the time the signal sweeps up to 30 Hz,
about a minute before merger.

.. figure:: _static/frqsnrtime.*
   :alt: Time evolution of SNR for a GW170817-like system

   The time evolution of the gravitational-wave frequency and the cumulative
   :term:`SNR` for a GW170817-like :term:`BNS` system.

The early warning search is a matched-filter search that uses templates that
have been truncated at a selection of end frequencies---or equivalently, cut
off at a selection of times before merger. The early warning template bank
spans (source frame) component masses between 1 and 2 :math:`M_\odot` and
:term:`chirp masses <chirp mass>` between 0.9 and 1.7 :math:`M_\odot`. The end
frequencies are 29 Hz, 32 Hz, 38 Hz, 49 Hz, and 56 Hz, corresponding to about
60 s, 45 s, 30 s, 15 s, and 10 s before merger.

Early warning events passing a :term:`FAR` threshold of one per week are sent
as alerts.

Source Classification
---------------------

The automated :doc:`source classification and properties <analysis/inference>`
have not been trained or tested extensively for early warning alerts. However,
the early warning analysis is **only sensitive to BNS-mass mergers**. As a
result, the favored source class in early warning GCN Notices will always be
either BNS or Terrestrial, with a 0% chance of NSBH or BBH. The HasNS and
HasRemnant fields will always show 100%.

Localization
------------

Sky localizations for early warning alerts are typically very coarse because
the early warning analysis inherently does not make use of the full duration
and bandwidth of the gravitational-wave signal. The localization improves
slowly up until the last second before merger, and then converges rapidly in
the last second.

The animations below show the evolution of early-warning sky maps for four
representative events with different :term:`SNR` values.

.. only:: latex

    In this PDF version of the User Guide, the images below are hyperlinks to
    the animations. Clicking on one of them will open the animation in your Web
    browser.

.. Note that absolute URLs are needed below to resolve hyperlinks from within
   the latexpdf build.

.. |skymap1| image:: _static/31109.*
    :alt: Animation of sky map for an event with SNR=11.0
    :target: https://emfollow.docs.ligo.org/userguide/_images/31109.gif
.. |skymap2| image:: _static/29958.*
    :alt: Animation of sky map for an event with SNR=18.2
    :target: https://emfollow.docs.ligo.org/userguide/_images/29958.gif
.. |skymap3| image:: _static/10390.*
    :alt: Animation of sky map for an event with SNR=25.2
    :target: https://emfollow.docs.ligo.org/userguide/_images/10390.gif
.. |skymap4| image:: _static/24926.*
    :alt: Animation of sky map for an event with SNR=35.6
    :target: https://emfollow.docs.ligo.org/userguide/_images/24926.gif

+---------------+---------------+---------------+---------------+---------------+
| Final SNR     | 11            | 18            | 25            | 36            |
+---------------+---------------+---------------+---------------+---------------+
|Distance       | 250 Mpc       | 210 Mpc       | 160 Mpc       | 110 Mpc       |
+===============+===============+===============+===============+===============+
| **Sky map**   | |skymap1|     | |skymap2|     | |skymap3|     | |skymap4|     |
| (animated GIF)|               |               |               |               |
+---------------+---------------+---------------+---------------+---------------+
| **Frequency** | **Localization accuracy** (90% credible area)                 |
+---------------+---------------+---------------+---------------+---------------+
| 29 Hz         | Not           | Not           | 12000 |deg2|  | 9400 |deg2|   |
+---------------+ detected      + detected      +---------------+---------------+
| 32 Hz         |               |               | 10000 |deg2|  | 7300 |deg2|   |
+---------------+               +---------------+---------------+---------------+
| 38 Hz         |               | 9200 |deg2|   | 8200  |deg2|  | 5100 |deg2|   |
+---------------+---------------+---------------+---------------+---------------+
| 49 Hz         | 2300 |deg2|   | 1000 |deg2|   | 730   |deg2|  | 2700 |deg2|   |
+---------------+---------------+---------------+---------------+---------------+
| 56 Hz         | 1000 |deg2|   | 700  |deg2|   | 250   |deg2|  | 1600 |deg2|   |
+---------------+---------------+---------------+---------------+---------------+
| 1024 Hz       | 10   |deg2|   | 31   |deg2|   | 5.4   |deg2|  | 34   |deg2|   |
+---------------+---------------+---------------+---------------+---------------+

Detection Rate and Localization Accuracy
----------------------------------------

This section describes the results of a simulation demonstrating the
capabilities of the early warning pipeline. This simulation provides an
expectation of how many events are detectable before merger, and how accurately
they can be localized at different times leading up to the merger.

We synthesized stretches of Gaussian noise with the power spectral densities of
Advanced LIGO and Virgo at their final design sensitivities. We injected
337,033 simulated :term:`BNS` signals distributed up to a redshift of
:math:`z=0.2`. We ran the GstLAL early warning search on the simulated data to
recover the injections and then produced sky localizations with BAYESTAR.

In the figure below, we show predicted detection rates, distances, and
localization uncertainties for BNS events. Of all BNS events detected by LIGO
and Virgo, only 5-30% will be amenable for sending early warning alerts. About
5% of all BNS events will be localized to an area of ~400 |deg2| by ~30 seconds
before merger. At the time of merger, the sky localization will be reduced to
about ~1 |deg2| for these events. At 60 s before merger, one event per year is
expected to be localized to within 400 |deg2|. At 30 seconds before merger, at
least one event per year is expected to be localized to within 40 |deg2| and ~4
events per year are expected to be localized to within 400 |deg2|. By 10
seconds before merger, ~10 events per year are expected to be localized to
within 400 |deg2|.

.. figure:: _static/areatest_log.*
    :alt: Cumulative distribution of localization area for early warning events

    Cumulative distribution of localization accuracy for early warning events.
    Assuming the median BNS merger rate, the right vertical axis shows the
    number of expected events to be recovered per year as a function of the
    90% credible area.

The figure below shows the cumulative fraction of recovered injections as a
function of distance. This figure shows the distance distribution of the events
recovered at various early warning frequencies.

.. figure:: _static/dist_hist.*
    :alt: Cumulative distribution of distance for early warning events

    Cumulative distribution of distance for early warning events.

.. _`Advanced LIGO`: https://ligo.caltech.edu
.. _`Advanced Virgo`: http://www.virgo-gw.eu
.. _`GW170817`: https://en.wikipedia.org/wiki/GW170817
.. _`GW170817 LSC`: https://www.ligo.org/detections/GW170817.php
.. _`GW170817 Press Release`: https://www.ligo.caltech.edu/page/press-release-gw170817
.. _`submit a change to your GCN Notice subscription settings`: https://gcn.gsfc.nasa.gov/gcn/config_builder.html
