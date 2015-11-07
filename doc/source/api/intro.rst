.. _introduction:

************
Introduction
************

The API is designed for sharing genomic data. It currently has support for sharing
sequencing reads and genetic variants, and is closely aligned to the data structures 
in `SAM`_, BAM (The binary incarnation of SAM) and `VCF`_ formats. 

.. _SAM: https://samtools.github.io/hts-specs/SAMv1.pdf
.. _VCF: https://samtools.github.io/hts-specs/VCFv4.2.pdf

In the following sections we outline the data model, covering the data structures to model 
a reference genome, sequencing reads, genetic variants and associated metadata. First
we outline key high level concepts and objects.

-----------
ID and Name
-----------

Throughout the API objects have *IDs*. The purpose of IDs is to allow unique
identification of all objects within a single server, such that no two objects in a 
given server have the same ID and no object has more than one ID. 
The scope of an ID is limited to a given server and an ID may be an arbitrary string. 

A name is a user defined identifier. Names need only be uniquely identifying 
within a specific scope, for example, the names of sequences within a ReferenceSet
must be distinct, but there might be two sequences named "chr1" stored in a server, each
in a different ReferenceSet. Names may be an arbitrary string. 

-------
DataSet
-------

A dataset is a highest level grouping that contains sequence and variant data. It provides
the concept of a container which allows high level separation between data. 

For the DataSet schema definition see the `Metadata schema <schemas/metadata.html>`_

------------
ReferenceSet
------------

A genome assembly is a digital representation of a genome. It is typically composed of *contigs*, 
each an uninterrupted string representing a DNA sequence, arranged into *scaffolds*, 
each of which orders and orients a set of contigs. Scaffolds are typically represented as a string, 
with runs of wildcard characters (N or n) used to represent interstitial regions of uncertain DNA between contigs. 

A reference genome is a genome assembly that other genomes are compared to and described with respect to.
For example, sequencing reads are mapped to and described with respect to a reference genome in the API,
and genetic variations are described as edits to reference scaffolds/contigs.
In the API a reference genome is described by a *ReferenceSet*. In turn a *ReferenceSet* 
is composed of a set of *Reference* objects, each which represents a scaffold or contig in the assembly.
A fairly minimal amount of metadata is associated with the *ReferenceSet* and *Reference* objects. 

For the Reference schema definitions see the `References schema <schemas/references.html>`_
