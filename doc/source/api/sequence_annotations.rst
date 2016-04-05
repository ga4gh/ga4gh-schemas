.. _sequence_annotations:

************************
Sequence Annotations API
************************
For the Sequence Annotation schema definitions, see `Sequence Annotation schema <../schemas/sequenceAnnotations.html>`_


------------------------
Feature Based Hierarchy
------------------------
The central object of the GA4GH Sequence Annotation API is a Feature.  The Feature describes an interval of interest on some reference(s).  It has a span from a start position to a stop position as well as descriptive data.  A Feature can have a parent Feature, and can have an ordered array of child Features, which enables the construction of more complex representations in a hierarchical way.

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


--------------------------------------
Annotation Design - RNA Considerations
--------------------------------------

Read data derived from RNA samples can differ from genomic read data due to the presence of non-genomic sequences.  An example would be a read that spans a splice junction.  It describes a contiguous sequence of reads, but a dis-continuous genomic region due to the missing intron.  Feature level read assignment is further complicated by the existence of multiple splice isoforms.  A read that can be definitely assigned to a particular feature (an exon in this case) may still not be definitely assigned to a particular transcript if multiple transcript share that exon.  The annotation API needs to be able to report assignment at the feature level as well as aggregate assignment at the transcript or even the whole gene level if assignment is not more specific than that.

Splicing (other post-transcriptional modifications?) can occur with degrees of complexity.  A ‘typical’ splice will result in a mature transcript with exon in positional (numerical) order in a head-to-tail orientation.  Back splicing (tail-to-head) can result in transcripts with the exon order reversed (1-3-2-4 instead of 1-2-3-4) and even circular RNA.  The exon order in a transcript as well as the orientation of the splice should be discoverable via the API.  In a more general case, the API should allow child features to have an ordered relationship.
