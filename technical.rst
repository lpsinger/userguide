Technical Reference
===================

Public LIGO/Virgo alerts are distributed using the Gamma-ray Coordinates
Network/Transient Astronomy Network (`GCN/TAN`_). The machine-readable alerts
are called GCN Notices.

GCN Notices are available over several different protocols and in several
different formats. LIGO/Virgo strongly recommends using the VOEvent Transport
Protocol (`vTCP`_) to receive notices in `VOEvent`_ XML format because it is
anonymous, configuration-free, and easy to parse.

.. _`GCN/TAN`: http://gcn.gsfc.nasa.gov/
.. _`vTCP`: http://www.ivoa.net/documents/Notes/VOEventTransport/
.. _`VOEvent`: http://www.ivoa.net/documents/VOEvent/

Alert Schema
------------

+-------------------+-------------------------------------------+-------------------------------------------+
|                   | CBC                                       | Burst                                     |
+===================+===========================================+===========================================+
| **IVORN**         | :samp:`ivo://nasa.gsfc.gcn/LVC#S{YYMMDDabc}-{{1,2,3}}-{{Preliminary,Initial,Update}}` |
+-------------------+-------------------------------------------+-------------------------------------------+
| **Who**           | :samp:`LIGO Scientific Collaboration and Virgo Collaboration`                         |
+-------------------+-------------------------------------------+-------------------------------------------+
| **What**          | GraceDB ID: :samp:`S{YYMMDDabc}`                                                      |
+-------------------+-------------------------------------------+-------------------------------------------+
| - **Search**      | :samp:`CBC`                               | :samp:`Burst`                             |
+-------------------+-------------------------------------------+-------------------------------------------+
| - **Pipeline**    | :samp:`{{Gstlal,MBTA,PyCBC,SPIR}}`        | :samp:`{{cWB,oLIB}}`                      |
+-------------------+-------------------------------------------+-------------------------------------------+

Python Sample Code
------------------
* How to subcribe to GCN, receive and send alerts https://dcc.ligo.org/public/0118/G1500442/010/ligo-virgo-emfollowup-tutorial.html
* Interaction with GraceDB 
