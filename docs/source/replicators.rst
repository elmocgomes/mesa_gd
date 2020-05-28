Replicators
========================

Replicators are material structures hosted by the entity that is involved in the replication process and carries information.
Replication is a process whereby replicators are copied under the following conditions:

#. Causal implications: The source must be causally involved in the production of the copy, at least in the sense that, without the source, the particular copy would not be created.
#. Similarity: The copy must be like its source in relevant respects. In particular, the replicated entity must also be or contain replicator.
#. Information transfer: During its creation, the copy must obtain the information that makes the copy similar to its source from the same source.

Replicators are programmed as functions in the mesa_gd package, which can be energized under the interactor instance.
The Class built on Interactor has the list of keys to replicators as an attribute, referencing such functions and energizing it when required.
