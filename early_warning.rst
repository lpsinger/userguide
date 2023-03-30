.. |deg2| replace:: deg\ :superscript:`2`

✨Early-Warning Alerts
======================

:term:`BNS` mergers spend several minutes in band of the Advanced ground-based
gravitational-wave detectors.  For some loud and nearby :term:`BNS`
mergers, it is possible to accumulate enough :term:`SNR` and detect them
several tens of seconds before merger.  During O3, automated public alerts for
:term:`CBC` events have been sent within as little as 2 minutes after merger.
In O4, we will be deploying search pipelines that can in principle detect
BNS events before merger.

Since it is generally assumed that detectable electromagnetic (or neutrino)
emission starts shortly *after* merger, a pre-merger gravitational-wave
detection would provide *early warning* of an impending electromagnetic
transient and might make it possible for automated follow-up facilities to
capture any prompt emission from the merger environment, the jet, and other
unknown activity.

We had previously conducted a trial early warning public alert infrastructure
in June 2020 replaying an 8-day period of archival LIGO data from O3. Results
from this study were published in [#FirstDemonstration]_. This study
demonstrated that in principle it is possible to sent out GCN Notices in
advance of a BNS merger. Based on the current expect BNS merger rate,  we expect O(1) event per year to be detected before merger in O4.

**We have commissioned the capability to produce and distribute
early warning gravitational-wave alerts up to tens of seconds before merger. We
have also reduced the latency of ordinary post-merger alerts to within tens of
seconds after merger.**

Subscribe to Early-Warning Alerts
---------------------------------

Early warning alerts are publicly distributed as :term:`Notices <Notice>` just
like ordinary gravitational-wave alerts (see the :doc:`content` section).
**They have exactly the same format and content** as a :ref:`Preliminary Notice
<preliminary>`. In particular, early warning GCN Notices have significance
estimates, sky localizations, and source classifications. Also, like
Preliminary GCN Notices, **Early Warning Notices are sent prior to vetting
by humans, and are not accompanied by a GCN Circular.**

Early warning GCN Notices are differentiated from ordinary GCN Notices by the
new ``LVC_EARLY_WARNING`` GCN Notice type. If you are receiving GCN Notices via
an anonymous VOEvent connection and you are using the Python sample code from
the :doc:`tutorial/receiving/classic` section, then all you have to do is add
the notice type to your GCN handler::

    import gcn

    @gcn.handlers.include_notice_types(
        gcn.notice_types.LVC_EARLY_WARNING,  # <-- new notice type here
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

Detection Method
----------------

All of our :term:`CBC` search pipelines (GstLAL [#GstLALEarlyWarning]_, MBTA,
PyCBC, and SPIIR) are participating in early-warning alerts. See the
:doc:`analysis/searches` section for details
on these analyses. Localizations will be produced with BAYESTAR; see the
:doc:`analysis/parameter_estimation` section for details.

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
off at a selection of times before merger.


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

The animations below taken from the data release [#DataRelease]_ show the
evolution of early-warning sky maps for three representative events with
different :term:`SNR` values. Note that this study assumed the detectors to be
operating at their final design sensitivity.

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

+---------------+---------------+---------------+---------------+
| Final SNR     | 11            | 18            | 25            |
+---------------+---------------+---------------+---------------+
|Distance       | 250 Mpc       | 210 Mpc       | 160 Mpc       |
+===============+===============+===============+===============+
| **Sky map**   | |skymap1|     | |skymap2|     | |skymap3|     |
| (animated GIF)|               |               |               |
+---------------+---------------+---------------+---------------+
| **Frequency** | **Localization accuracy** (90% credible area) |
+---------------+---------------+---------------+---------------+
| 29 Hz         | Not           | Not           | 12000 |deg2|  |
+---------------+ detected      + detected      +---------------+
| 32 Hz         |               |               | 10000 |deg2|  |
+---------------+               +---------------+---------------+
| 38 Hz         |               | 9200 |deg2|   | 8200  |deg2|  |
+---------------+---------------+---------------+---------------+
| 49 Hz         | 2300 |deg2|   | 1000 |deg2|   | 730   |deg2|  |
+---------------+---------------+---------------+---------------+
| 56 Hz         | 1000 |deg2|   | 700  |deg2|   | 250   |deg2|  |
+---------------+---------------+---------------+---------------+
| 1024 Hz       | 10   |deg2|   | 31   |deg2|   | 5.4   |deg2|  |
+---------------+---------------+---------------+---------------+


.. [#FirstDemonstration]
   Magee, R., Chatterjee, D., Singer, L. P., Sachdev, S., et al. 2022.
   :doi:`10.3847/2041-8213/abed54`

.. [#GstLALEarlyWarning]
   Sachdev, S., Magee, R., Hanna, C., et al. 2020.
   :doi:`10.3847/2041-8213/abc753`

.. [#DataRelease]
    https://gstlal.docs.ligo.org/ewgw-data-release/

.. _`Advanced LIGO`: https://ligo.caltech.edu
.. _`Advanced Virgo`: http://www.virgo-gw.eu
.. _`GW170817`: https://en.wikipedia.org/wiki/GW170817
.. _`GW170817 LSC`: https://www.ligo.org/detections/GW170817.php
.. _`GW170817 Press Release`: https://www.ligo.caltech.edu/page/press-release-gw170817
.. _`submit a change to your GCN Notice subscription settings`: https://gcn.gsfc.nasa.gov/gcn/config_builder.html
