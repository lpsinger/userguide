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

Here, we describe the sequence of LIGO/Virgo alerts for a single event that
will be distributed through the Gamma-ray Coordinates Network (:term:`GCN`) via
notices and circulars (see the :doc:`/content` and :doc:`/tutorial/index`
sections for details).

.. plot::
    :alt: Timeline for sending gravitational-wave alerts

    from astropy.visualization import quantity_support
    from astropy import units as u
    from matplotlib import pyplot as plt
    from matplotlib.transforms import blended_transform_factory
    import numpy as np

    quantity_support()

    gradient = np.linspace(0, 1, 256)[np.newaxis, :]**0.5

    plot_data = [[['Rapid Sky Localization', 60 * u.second, 20 * u.second],
                  ['Classification', 75 * u.second, 5 * u.second],
                  ['Automated Vetting', 75 * u.second, 5 * u.second],
                  ['Original Detection', 0 * u.second, 59.999 * u.second]],
                 [['Re-annotate', 3.6 * u.min, 1 * u.min], 
                  ['Cluster additional events', 2.5 * u.min, 1 * u.min]], 
                 [['Classification', 4 * u.hour, 10 * u.minute],
                  ['Human Vetting', 5 * u.minute, 4 * u.hour],
                  ['Parameter Estimation', 75 * u.second, 4 * u.hour]],
                 [['Classification', 6 * u.day, 6 * u.hour],
                  ['Parameter Estimation', 4 * u.hour, 6 * u.day]]]

    alert_labels = ['1st Preliminary\nAlert Sent',
                    '2nd Preliminary\nAlert Sent',
                    'Initial Alert or\nRetraction Sent',
                    'Update\nAlert Sent']
    bar_height = 0.8

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

        labels, starts, durations = zip(*data)
        starts = u.Quantity(starts).to(u.second)
        durations = u.Quantity(durations).to(u.second)

        t = max(starts + durations) * 1.1
        ax.axvline(t, color='black')
        ax.axvspan(1e-2 * u.second, t, color='0.95')
        ax.text(t * 1.15, 0.5, alert_label,
                transform=blended_transform_factory(ax.transData, ax.transAxes),
                fontweight='bold', va='center')

        ax.barh(np.arange(len(labels)), width=durations,
                left=starts, height=bar_height,
                facecolor=props['color'], edgecolor='black')
        for i, (start, duration, label) in enumerate(zip(starts, durations, labels)):
            ax.text(max(start, 1 * u.minute), i,
                    ' ' + label + ' ', ha='right', va='center')
        ax.set_ylim(0.5 * bar_height - 1, len(labels) - 0.5 * bar_height)
        ax.imshow(gradient, extent=[t.value, (10 * t).value, -10, 10], cmap='Greys_r', vmin=-1, vmax=1)

    fig.suptitle('Time since gravitational-wave signal')
    ax.set_xscale('log')
    ax.set_xlim(1 * u.second, 100 * u.day)
    ticks = [10 * u.second, 1 * u.minute, 1 * u.hour, 1 * u.day, 1 * u.week]
    ax.set_xticks(ticks)
    ax.set_xticklabels(
        ['{0.value:g} {0.unit.long_names[0]}'.format(_) for _ in ticks])
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

**Within 1–10 minutes after GW trigger time**, the first and second :doc:`preliminary
notices </content>` will be sent fully autonomously. The trigger will be immediately
and publicly visible in the :term:`GraceDB` database. Since the procedure is fully
automatic, some preliminary alerts may be retracted after human inspection for
data quality, instrumental conditions, and pipeline behavior.

**Within 24 hours after the GW trigger time** (possibly within 4 hours for
:term:`BNS` or :term:`NSBH` sources), the :doc:`Initial or Retraction notice
and circular </content>` will be distributed. It will include an updated sky
localization and source classification. At this stage, the event will have been
vetted by human instrument scientists and analysts. The candidate will either
be **confirmed** by an Initial notice and circular or withdrawn by a Retraction
notice and circular if the data quality is unsuitable.

**Within a day**, black hole mergers will be fully vetted by experts and
retraction or confirmation status will be reported.

:doc:`Update notice and circulars </content>` are sent whenever the sky
localization area or significance accuracy improves (e.g. as a result of
improved calibration, glitch removal, or computationally deeper parameter
estimation). Updates will be sent up until the position is determined more
accurately by public announcement of an unambiguous counterpart. At that point,
there will be no further sky localization updates until the publication of the
event in a peer-reviewed journal.

**At any time**, we can **promote** an extraordinary candidate that does not
pass our public alert thresholds if it is compellingly associated with a
multimessenger signal (e.g. :term:`GRB`, core-collapse :term:`SN`). In this
case, :doc:`Initial notices and circulars </content>` will be distributed.

.. _alert-threshold:

Alert Threshold
---------------

Automated preliminary alerts are sent for all events that pass a false alarm
rate (:term:`FAR`) threshold. The :term:`FAR` threshold is :math:`3.8 \times
10^{-8}` Hz (one per 10 months) for :term:`CBC` searches and is :math:`7.9
\times 10^{-9}` (one per 4 years) for unmodeled burst searches. Since there are
4 independent :term:`CBC` searches and 3 independent :term:`burst` searches,
as well as a coincidence search :doc:`RAVEN <searches>` that looks at the
results from both the aforementioned :term:`CBC` and :term:`burst` searches,
the effective rate of false alarms for :term:`CBC` sources is :math:`1.9 \times
10^{-7}` Hz (one per 2 months), and for unmodeled bursts is :math:`3.2 \times
10^{-8}` Hz (one per year).
