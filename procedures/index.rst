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
  
.. image:: /_static/Flowchartprocv2.jpg
   :alt: Alert Flowchart

.. digraph:: flowchart

    compound = true
    nodesep = 0.1
    ranksep = 0.5

    node [
        fillcolor = white
        shape = box
        style = filled
        target = "_top"
    ]

    graph [
        labeljust = "left"
        style = filled
        target = "_top"
    ]

    subgraph cluster_minutes {
        style = "filled, rounded";
        color = lightgrey;
        node [style=filled,color=white];

        online_searches [
            label = "Online searches\n(few minutes)"
        ]

        preferred_event [
            label = "Get preferred event\n(seconds)"
        ]

        skymap_available [
            label = "Skymap available?"
            shape = diamond
        ]

        preliminary_notice_map [
            label = "Preliminary notice \nwith skymap"
            shape = egg
        ]

        preliminary_notice_nomap [
            label = "Preliminary notice \nwithout skymap"
            shape = egg
        ]

        preliminary_notice_2_map [
            label = "Second preliminary notice \nwith skymap"
            shape = egg
        ]

        online_searches -> preferred_event;
        preferred_event -> skymap_available;
        skymap_available -> preliminary_notice_map [label = Yes];
        skymap_available -> preliminary_notice_nomap [label = No];
        preliminary_notice_nomap -> preliminary_notice_2_map [label = "Skymap available"];
        label = "Within minutes: fully automatic"
    }

    subgraph cluster_hours {
        style = "filled, rounded";
        color = lightgrey;
        node [style=filled,color=white];

        updated_skymaps [
            label = "Updated skymaps and \nsource classification"
        ]

        human_vetting [
            label = "Human vetting"
        ]

        trigger_type [
            label = "Type of trigger"
            shape = diamond
        ]
        
        data_good [
            label = "Data good?"
            shape = diamond
        ]

        initial [
            label = "Initial notice and circular"
            shape = egg
        ]

        retraction [
            label = "Initial notice (retraction)"
            shape = egg
        ]

        confirm [
            label = "Initial notice (confirmation)"
            shape = egg
        ]

        updated_skymaps -> human_vetting;
        human_vetting -> trigger_type;
        trigger_type -> initial [label=BBH];
        trigger_type -> data_good [label="BNS, NSBH,\n or burst"]
        data_good -> confirm [label=Yes]
        data_good -> retraction [label=No]

        label = "Within four hours: human vetting"
    }

    subgraph cluster_day {
        style = "filled, rounded";
        color = lightgrey;
        node [style=filled,color=white];

        sub_thres [
            label = "Sub-thresholds triggers\nwith EM or extraordinary triggers"
        ]

        sky_local_improve [
            label = "Sky localization or \nsignificance area \n improves"
        ]

        update [
            label = "Update notice and circular"
            shape = egg
        ]

        sub_thres -> initial;
        sub_thres -> sky_local_improve [style=invis]
        sky_local_improve -> update
        label = "Any time"
    }

    preliminary_notice_2_map -> updated_skymaps [style=invis]
