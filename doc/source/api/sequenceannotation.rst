.. _sequence_annotation

****************************
GA4GH Sequence Annotation
****************************
For the Sequence Annotation schema definitions, see `Sequence Annotation schema <schemas/sequenceAnnotations.html>`_


------------------------
Feature Based Hierarchy
------------------------
The central object of the GA4GH Sequence Annotation API is a Feature.  The Feature describes an interval of interest on some reference(s).  It has a span from a start position to a stop position as well as descriptive data.  A Feature has one or more parent Features which enables the construction of more complex representations in a hierarchical way.

For example, a top level Feature may be a single Gene.  The different transcripts would have the gene Feature as parent.  Similarly, the specific exons for each transcript would have both gene and transcript as parent.  This structure can also exend to annotating CDS, binding sites or any other sub-gene level features.

This model is very similar to that used by `GFF3`_.

.. _GFF3: http://sequenceontology.org/resources/gff3.html

---------------------------
The Sequence Annotation Schema
---------------------------
TODO: insert an example annotation translation from GFF3 to GA4GH

---------------------------------------
Annotation Design - RNA Considerations
---------------------------------------

Read data derived from RNA samples can differ from genomic read data due to the presence of non-genomic sequences.  An example would be a read that spans a splice junction.  It describes a contiguous sequence of reads, but a dis-continuous genomic region due to the missing intron.  Feature level read assignment is further complicated by the existence of multiple splice isoforms.  A read that can be definitely assigned to a particular feature (an exon in this case) may still not be definitely assigned to a particular transcript if multiple transcript share that exon.  The annotation API needs to be able to report assignment at the feature level as well as aggregate assignment at the transcript or even the whole gene level if assignment is not more specific than that.

Splicing (other post-transcriptional modifications?) can occur with degrees of complexity.  A ‘typical’ splice will result in a mature transcript with exon in positional (numerical) order in a head-to-tail orientation.  Back splicing (tail-to-head) can result in transcripts with the exon order reversed (1-3-2-4 instead of 1-2-3-4) and even circular RNA.  The exon order in a transcript as well as the orientation of the splice should be discoverable via the API.  In a more general case, the API should allow child features to have an ordered relationship.

The annotation API needs to also be flexible enough to handle multiple references in the same gene or transcript.  This is needed to cover the cases of fusion genes or inter-chromosomal translocations.
