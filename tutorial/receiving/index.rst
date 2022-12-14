Receiving Notices
=================

There are three supported methods of receiving notices. The two recommended
methods both involve receiving serialized messages over Kafka; receiving
VOEvents over Classic GCN is also supported. All three methods communicate the
same information, and involve writing code to both listen for and parse
the notices.

Events come in two very general flavors: 'CBC' for compact binary coalescence
candidates detected by matched filtering, and 'Burst' for candidates detected
by model-independent methods. Your code can take different actions based on
this. The examples in the following sections will handle only 'CBC' events.

.. toctree::
   :maxdepth: 1

   scimma
   classic
   gcn
