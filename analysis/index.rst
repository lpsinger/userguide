Data Analysis
=============

In this section we describe the different online searches looking for GW
signals, the selection and vetting of candidates, and parameter estimation
analysis.

When multiple candidates from different pipelines are close enough together in
time, they will be considered as originating from the same physical event and
will be grouped into a single :doc:`superevent <superevents>`. See the
following pages for technical details.

.. toctree::
   :maxdepth: 1

   searches
   superevents
   vetting
   parameter_estimation
   inference

The timeline for distribution of alerts is described below.

Alert Timeline
--------------

Here, we describe the sequence of LIGO/Virgo/KAGRA alerts for a single event
that will be distributed through the Gamma-ray Coordinates
Network (:term:`GCN`) via notices and circulars (see the :doc:`/content` and
:doc:`/tutorial/index` sections for details).

.. plot::
    :alt: Timeline for sending gravitational-wave alerts

    from astropy.visualization import quantity_support
    from astropy import units as u
    from matplotlib import pyplot as plt
    from matplotlib.transforms import blended_transform_factory
    import numpy as np

    quantity_support()

    gradient = np.linspace(0, 1, 256)[np.newaxis, :]**0.5

    plot_data = [[['Sky Localization', -20 * u.second, 5 * u.second],
                  ['Classification', -20 * u.second, 5 * u.second],
                  ['Detection', -50  * u.second, 30 * u.second]],
                 [['Sky Localization', 30 * u.second, 5 * u.second],
                  ['Classification', 30 * u.second, 5 * u.second],
                  ['Automated Vetting', 30 * u.second, 5 * u.second],
                  ['Detection', 16 * u.second, 14 * u.second]],
                 [['Re-annotate', 3.6 * u.min, 1 * u.min],
                  ['Cluster additional events', 0.8 * u.min, 2.8 * u.min]],
                 [['Classification', 4 * u.hour, 10 * u.minute],
                  ['Human Vetting', 5 * u.minute, 4 * u.hour],
                  ['Parameter Estimation', 75 * u.second, 4 * u.hour]],
                 [['Classification', 6 * u.day, 6 * u.hour],
                  ['Parameter Estimation', 4 * u.hour, 6 * u.day]]]

    alert_labels = ['Early Warning\nAlert Sent',
                    '1st Preliminary\nAlert Sent',
                    '2nd Preliminary\nAlert Sent',
                    'Initial Alert or\nRetraction Sent',
                    'Update\nAlert Sent']
    bar_height = 0.8

    xlim = [-10 * u.minute, 100 * u.day]

    fig, axs = plt.subplots(
        len(plot_data),
        sharex=True,
        figsize=(8, 4),
        gridspec_kw=dict(
            height_ratios=[len(_) + 1 - bar_height for _ in plot_data],
            top=0.9, left=0, right=1, hspace=0.05, bottom=0.1
        ))

    for ax, data, alert_label, props in zip(axs, plot_data, alert_labels, axs[0]._get_lines.prop_cycler):
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_yticks([])
        ax.xaxis.label.set_visible(False)
        ax.set_facecolor('0.95')

        labels, starts, durations = zip(*data)
        starts = u.Quantity(starts).to(u.second)
        durations = u.Quantity(durations).to(u.second)

        t = max(starts + durations)
        if t.value > 0:
            tp = t * 1.1
            tp2 = t * 1.25
            tp10 = 10*t
        else:
            tp = t + 3 * u.second
            tp2 = t + 8 * u.second
            tp10 = t + 40 * u.second
        ax.axvline(tp, color='black')
        ax.text(tp2, 0.5, alert_label,
                transform=blended_transform_factory(ax.transData, ax.transAxes),
                fontweight='bold', va='center', ha='left')

        ax.barh(np.arange(len(labels)), width=durations,
                left=starts, height=bar_height,
                facecolor=props['color'], edgecolor='black')
        for i, (start, duration, label) in enumerate(zip(starts, durations, labels)):
            ax.text(start, i,
                    ' ' + label + ' ', ha='right', va='center')
        ax.set_ylim(0.5 * bar_height - 1, len(labels) - 0.5 * bar_height)
        ax.imshow(gradient, extent=[tp.value, tp10.value, -10, 10], cmap='Greys_r', vmin=-1, vmax=1, aspect='auto')
        ax.axvspan(tp10, xlim[1], color='white')

    fig.suptitle('Time relative to gravitational-wave merger')
    ax.set_xscale('symlog', linthresh=40)
    ax.set_xlim(-10 * u.minute, 100 * u.day)
    ticks = [-30 * u.second, 0 * u.second, 30 * u.second, 3 * u.minute, 1 * u.hour, 1 * u.day, 1 * u.week]
    ax.set_xticks(ticks)
    ax.set_xticklabels([
        '{0.value:g} {0.unit.short_names[0]}'.format(_) if abs(_) < 1 * u.minute else
        '{0.value:g} {0.unit.long_names[0]}'.format(_)
        for _ in ticks
    ])
    ax.minorticks_off()
    ax.set_xlabel('Time since GW signal')
    axs[-1].arrow(0, 0, 1, 0,
                  transform=ax.transAxes, clip_on=False,
                  head_width=0.1, head_length=0.01,
                  linewidth=axs[-1].spines['bottom'].get_linewidth(),
                  edgecolor=axs[-1].spines['bottom'].get_edgecolor(),
                  facecolor=axs[-1].spines['bottom'].get_edgecolor(),
                  length_includes_head=True)
    for ax in axs[:-1]:
        plt.setp(ax.xaxis.get_major_ticks(), visible=False)


**Beginning from 1 minute before the GW merger time**, an
:doc:`early warning search </early_warning>` may find a pre-merger
candidate. If it does, then an :doc:`Early Warning alert </content>` may be
sent before the GW merger time.

**Within 1–10 minutes after GW trigger time**, the first and second
:doc:`preliminary alerts</content>` will be sent fully autonomously. The
trigger will be immediately and publicly visible in the :term:`GraceDB`
database. Since the procedure is fully automatic, some preliminary alerts may
be retracted after human inspection for data quality, instrumental conditions,
and pipeline behavior.

**Within 24 hours after the trigger time** of any **significant**
gravitational-wave alerts (possibly within 4 hours for :term:`BNS`
or :term:`NSBH` sources), the :doc:`Initial or Retraction alert
and circular </content>` will be distributed. It will include an updated sky
localization and source classification. At this stage, the event will have been
vetted by human instrument scientists and data analysts. The candidate will either
be **confirmed** by an Initial alert and circular or withdrawn by a Retraction
alert and circular if the data quality is unsuitable.

:doc:`Update alerts and circulars </content>` are sent whenever the sky
localization area or significance accuracy improves (e.g. as a result of
improved calibration, glitch removal, or computationally deeper parameter
estimation). Updates will be sent up until the position is determined more
accurately by public announcement of an unambiguous counterpart. At that point,
there will be no further sky localization updates until the publication of the
event in a peer-reviewed journal.

**At any time**, we may promote a candidate to be a **significant**
gravitational-wave alert if it is compellingly associated with a
multimessenger signal (e.g. :term:`GRB`, core-collapse :term:`SN`). In this
case, :doc:`Initial alert and circulars </content>` will be distributed.

.. _alert-threshold:

Alert Threshold
---------------

Automated preliminary alerts are sent out with an expected false alarm rate
(:term:`FAR`) of :math:`2.3 \times  10^{-5}` Hz (two per day). We will divide
gravitational-wave alerts into two categories:
(1) **low-significance** gravitational-wave alerts and (2) **significant**
gravitational-wave alerts. **Significant** gravitational-wave alerts will be sent
out with an expected false alarm rate of :math:`3.9 \times 10^{-7}` Hz (one
per month) for :term:`CBC` sources, and of :math:`3.2 \times 10^{-8}` Hz (one per year)
for unmodeled burst signals that do not have a CBC signature.
This alert threshold aims to reach 90\% purity for  **significant**
gravitational-wave alerts.

We will not perform any further analysis following **low-significance**
gravitational-wave preliminary alerts or early warning alerts that are not followed
by a **significant** preliminary alert. That means that the initial, retraction, and
update alerts will be sent out only for those alerts that are associated with **significant**
preliminary alerts.


.. _alert-threshold-trial-factor:

Alert Threshold Trials Factor
-----------------------------

We run both :term:`CBC`-focused and burst-focused searches. For :term:`CBC`,
there are five independent searches, including a :term:`CBC`-focused burst search; for burst, there
are three independent searches. There is also an external coincidence search RAVEN that looks at
results from both the aforementioned :term:`CBC` and burst searches. To account for the trials
factor from the different searches with statistically independent false alarms, an alert will
be marked as **significant** for events that generate a preliminary alert with a :term:`FAR`
threshold of  :math:`6.4 \times 10^{-8}` Hz (one per 6 months) for :term:`CBC` target searches
and of :math:`7.9 \times 10^{-9}` (one per four years) for unmodeled
burst searches. That corresponds to the expected effective rate of **significant** false alarms
of :math:`3.9 \times 10^{-7}` Hz (one per month) for :term:`CBC` sources,
and :math:`3.2 \times 10^{-8}` Hz (one per year) for unmodeled burst sources.

The presence of a trial factor (eight searches) implies that public alerts will
be sent for all triggers that pass a false alarm rate (FAR) threshold of :math:`2.9 \times 10^{-6}` Hz
(one per four days).
