.. _sequence_annotations:

************************
Sequence Annotations API
************************
For the Sequence Annotation schema definitions, see `Sequence Annotation schema <../schemas/sequenceAnnotations.html>`_


------------------------
Feature Based Hierarchy
------------------------
The central object of the GA4GH Sequence Annotation API is a Feature.  The Feature describes an interval of interest on some reference(s).  It has a span from a start position to a stop position as well as descriptive data.  A Feature has one parent Feature, and can have an ordered array of child Features, which enables the construction of more complex representations in a hierarchical way.

For example, a single gene Feature may be parent to several different transcript Features.  The specific exons for each transcript would have that transcript Feature as parent.  The same physical exon may occur as part of two different transcript Features, but in our notation, it would be
encoded as two separate exon Features, each with a different parent, both occupying the same genomic coordinates. This structure can also exend to annotating CDS, binding sites or any other sub-gene level features.


------------------------------
The Sequence Annotation Schema
------------------------------

This model is similar to that used by the standard `GFF3`_ file format.

.. _GFF3: http://sequenceontology.org/resources/gff3.html

The main differences concern the deprecation and replacement of discontinuous features, the replacing
of multi-parent features with multiple copies of that feature, and the ability to impose an explicit order on child features.

In the first case, a CDS composed of multiple regions is sometimes encoded as multiple rows of a GFF3 file, each with the same feature ID. This is translated in our hierarchy into a single CDS Feature with an ordered set of CDS_region Feature children, each corresponding to a single row of the original record.

In the second case, as explained above, features with multiple parents in a GFF3 record are simply replicated and assigned a new identifier as many times as needed to ensure a unique parent for every feature.

In the final case, an explicit mechanism is provided for ordering child Features. Most of the time this ordering is trivially derived from the genomic coordinate ordering of the children, but in some biologically important cases this order can differ, such as in non-canonical splicing of exomes into transcripts (also known as back splicing - see below).

A FeatureSet is simply a collection of features from the same source. An implementer may, for example, choose to gather all Features from the same GFF3 file into a common FeatureSet.

