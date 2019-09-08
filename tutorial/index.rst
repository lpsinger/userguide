Sample Code
===========

This section provides Python sample code for receiving and interacting with
:term:`GCN Notices <GCN Notice>`. GCN Notices are available over several
different protocols and in several different formats. LIGO/Virgo recommends
using the VOEvent Transport Protocol (:term:`VTP`) to receive notices in
:term:`VOEvent` XML format because it is anonymous, configuration-free, and
easy to parse.

.. warning::
   The VOEvent XML alerts are official data products of LIGO/Virgo. GCN
   produces `several other legacy formats`_ from them, in particular a
   text-based "full format" and binary format. LIGO/Virgo performs only limited
   quality control of the legacy formats.

This tutorial will walk you through writing a Python script to receive and
process the example LIGO/Virgo GCN notices that are sent every hour. The
tutorial is broken into the following subsections:

.. toctree::
   :maxdepth: 1

   prerequisites
   receiving
   skymaps
   multiorder_skymaps
   observability
   3d

.. _`several other formats`: https://gcn.gsfc.nasa.gov/gcn_describe.html#tc7
.. _`several other distribution methods`: https://gcn.gsfc.nasa.gov/tech_describe.html
.. _`GCN's anonymous VOEvent brokers`: https://gcn.gsfc.nasa.gov/voevent.html#tc2
