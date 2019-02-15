Sample Code
===========

This section provides Python sample code for receiving and interacting with
:term:`GCN Notices <GCN Notice>`. GCN Notices are available over several
different protocols and in several different formats. LIGO/Virgo strongly
recommends using the VOEvent Transport Protocol (:term:`VTP`) to receive
notices in :term:`VOEvent` XML format because it is anonymous,
configuration-free, and easy to parse.

This tutorial will walk you through writing a Python script to receive and
process example LIGO/Virgo GCN notice that are sent every hour. The tutorial is
broken into the following subsections:

.. toctree::
   :maxdepth: 1

   prerequisites
   receiving
   skymaps
   observability
   3d
   tools
