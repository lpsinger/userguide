.. LIGO/Virgo Public Alerts User Guide documentation master file, created by
   sphinx-quickstart on Wed Sep 19 09:39:42 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

LIGO/Virgo Public Alerts User Guide
===================================

Welcome to the LIGO/Virgo Public Alerts User Guide! This document is intended
for both professional astronomers and science enthusiasts who are interested in
receiving alerts and real-time data products related to gravitational-wave (GW)
events.

Three sites (:term:`LHO`, :term:`LLO`, :term:`Virgo`) together form a global
network of ground-based GW detectors. The `LIGO Scientific Collaboration
<https://ligo.org/>`_ and the `Virgo Collaboration
<http://public.virgo-gw.eu/the-virgo-collaboration/>`_ jointly analyze the data
in real time to detect and localize transients from compact binary mergers and
other sources GW bursts. When a signal candidate is found, an alert is sent to
astronomers in order to search for counterparts (electromagnetic waves or
neutrinos).

Advanced LIGO and Advanced Virgo are preparing for their third observing run
(O3) in early 2019. For the first time, **LIGO/Virgo alerts will be public**.
Alerts will be distributed through NASA's Gamma-ray Coordinates Network
(:term:`GCN`). There are two types of alerts: human-readable :term:`GCN
Circulars <GCN Circular>` and machine-readable :term:`GCN Notices <GCN
Notice>`. This document provides a brief overview of the procedures for vetting
and sending GW alerts, describes their contents and format, and includes
instructions and sample code for receiving GCN Notices and decoding GW sky maps.

.. warning::
   Some technical details of LIGO/Virgo public alerts may change before the
   start of Observing Run 3 (O3) in 2019. In particular, details of the alert
   format and the :term:`GraceDb` public portal may evolve. Please check this
   document regularly for announcements and updates.


Contents
--------

.. toctree::
   :maxdepth: 2

   quickstart
   capabilities
   procedures/index
   content
   tutorial/index

Appendix
--------

.. toctree::
   :hidden:

   glossary

* :doc:`glossary`
* :ref:`search`
* `Report issues <contact+emfollow/userguide@support.ligo.org>`_

.. _Virgo: http://www.virgo-gw.eu
