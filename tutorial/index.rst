Sample Code
===========

Public LIGO/Virgo alerts are distributed using :term:`GCN`. The
machine-readable alerts are called :term:`GCN Notices <GCN Notice>`.

GCN Notices are available over several different protocols and in several
different formats. LIGO/Virgo strongly recommends using the VOEvent Transport
Protocol (:term:`VTP`) to receive notices in VOEvent_ XML format because it is
anonymous, configuration-free, and easy to parse.

This section provides Python sample code for receiving and interacting with GCN
Notices.

Contents
--------

.. toctree::
   :maxdepth: 1

   prerequisites
   receiving
   skymaps
   observability
   3d
   tools

.. _VOEvent: http://www.ivoa.net/documents/VOEvent/
