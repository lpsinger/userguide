Procedures
==========

In this section we describe the different online searches looking for GW
signals. The corresponding triggers from multiple pipelines close enough in
time will be considered at originating from the same physical event and will be
grouped in a unique :doc:`superevent <superevents>`. See the following pages
for technical details.

.. toctree::
   :maxdepth: 1

   searches
   parameter_estimation
   superevents
   inference
   vetting

The timeline for distribution of alerts is described below.

Alert Timeline
--------------

Here, we described the sequence of the GW alert distributed the Gamma-ray
Coordinates Network (:term:`GCN`) via notices and circulars (:doc:`Alert
content </content>` and :doc:`Technical </tutorial/index>`). Alerts should
contain all of the information that is useful for searching for a counterpart.

.. plot::
    :alt: Timeline for sending gravitational-wave alerts

    from astropy.visualization import quantity_support
    from astropy import units as u
    from matplotlib import pyplot as plt
    from matplotlib.transforms import blended_transform_factory
    import numpy as np

    quantity_support()

    plot_data = [[['Rapid Localization', 10 * u.second, 20 * u.second],
                  ['Classification', 26 * u.second, 1 * u.second],
                  ['Automated Vetting', 25 * u.second, 1 * u.second],
                  ['Set Preferred Event', 10 * u.second, 15 * u.second],
                  ['GraceDb Upload', 0.001 * u.second, 9.999 * u.second]],
                 [['Classification', 4 * u.hour, 10 * u.minute],
                  ['Human Vetting', 5 * u.minute, 4 * u.hour],
                  ['Automated Parameter Estimation', 25 * u.second, 4 * u.hour]],
                 [['Classification', 6 * u.day, 1 * u.hour],
                  ['Manual Parameter Estimation', 4 * u.hour, 6 * u.day]]]

    alert_labels = ['Preliminary\nAlert Sent',
                    'Initial Alert or\nRetraction Sent',
                    'Update Alert']
    bar_height = 0.8

    fig, axs = plt.subplots(
        len(plot_data),
        sharex=True,
        figsize=(8, 3),
        gridspec_kw=dict(
            height_ratios=[len(_) + 1 - bar_height for _ in plot_data],
            top=0.9, left=0, right=1, hspace=0.05, bottom=0.2
        ))

    for ax, data, alert_label in zip(axs, plot_data, alert_labels):
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_yticks([])
        ax.xaxis.label.set_visible(False)

        labels, starts, durations = zip(*data)
        starts = u.Quantity(starts).to(u.second)
        durations = u.Quantity(durations).to(u.second)

        t = max(starts + durations) * 1.1
        ax.axvline(t, color='black')
        ax.axvspan(1e-2 * u.second, t, color='lightgray')
        ax.text(t * 1.15, 0.5, alert_label,
                transform=blended_transform_factory(ax.transData, ax.transAxes),
                fontweight='bold', va='center')

        ax.barh(np.arange(len(labels)), width=durations, left=starts, height=bar_height)
        for i, (start, duration, label) in enumerate(zip(starts, durations, labels)):
            ax.text(max(start, 10 * u.second), i,
                    ' ' + label + ' ', ha='right', va='center')
        ax.set_ylim(0.5 * bar_height - 1, len(labels) - 0.5 * bar_height)

    fig.suptitle('Time since gravitational-wave signal')
    ax.set_xscale('log')
    ax.set_xlim(1e-1 * u.second, 100 * u.day)
    ticks = [1 * u.second, 1 * u.minute, 1 * u.hour, 1 * u.day, 1 * u.week]
    ax.set_xticks(ticks)
    ax.set_xticklabels(
        ['{0.value:g} {0.unit.long_names[0]}'.format(_) for _ in ticks])
    ax.minorticks_off()
    ax.set_xlabel('Time since GW signal')

**Within minutes after GW trigger time**, the first :doc:`preliminary notice
</content>` will be sent fully autonomously (not necessary attached to
localization). The trigger will be immediately visible under the LIGO/Virgo GW
database :term:`GraceDb`. As soon as the localization area is available, a
second preliminary notice is sent. The procedure is fully automatic and some
preliminary alerts may be retracted after human inspection for data quality,
instrumental conditions, and pipeline behavior.

**Within 4 hours after the GW trigger time**, the :doc:`Initial notices and
circulars </content>` will be distributed with an update for the sky
localization area and the source classification. They are vetted by human
instrument scientists and analysts. In case of a binary coalescence including a
neutron star or a burst trigger, the initial circular can labeled as
**retracted** (data are unsuitable) or **confirmed**. Note that the initial
circular is considered the first LIGO/Virgo publication of a GW candidate,
appropriate to cite in publications.

**Within a day**, black hole mergers will be fully vetted by experts and
retraction or confirmation status will be reported.

:doc:`Update notice and circulars </content>` are sent whenever the sky
localization area or significance accuracy improves (e.g. as a result of
improved calibration, de-glitching, or computationally deeper parameter
estimation). Updates will be sent up until the position is determined more
accurately by public announcement of an unambiguous counterpart. At which point
they will stop until publication of the event.

**Any time**, we can **promote** an extraordinary candidate that does not pass
our public alert thresholds if it is compellingly associated with a
multimessenger signal (e.g. GRB, core-collapse SN). In this case, :doc:`Initial
notices and circulars </content>` will be distributed.
