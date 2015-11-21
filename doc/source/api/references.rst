.. _references:


References API
!!!!!!!!!!!!!!

See `References schema <../schemas/refernces.html>`_ for a detailed reference.


References Data Model
@@@@@@@@@@@@@@@@@@@@@

A genome assembly is a digital representation of a genome. It is
typically composed of *contigs*, each an uninterrupted string
representing a DNA sequence, arranged into *scaffolds*, each of which
orders and orients a set of contigs. Scaffolds are typically
represented as a string, with runs of wildcard characters (N or n)
used to represent interstitial regions of uncertain DNA between
contigs.

A reference genome is a genome assembly that other genomes are
compared to and described with respect to.  For example, sequencing
reads are mapped to and described with respect to a reference genome
in the API, and genetic variations are described as edits to reference
scaffolds/contigs.  In the API a reference genome is described by a
*ReferenceSet*. In turn a *ReferenceSet* is composed of a set of
*Reference* objects, each which represents a scaffold or contig in the
assembly.  A fairly minimal amount of metadata is associated with the
*ReferenceSet* and *Reference* objects.

