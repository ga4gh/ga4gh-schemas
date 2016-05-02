.. _rnaquantification:

***************************
RNA Quantification API
***************************

For the RNA Quantification schema definitions, see the `RNA Quantification schema <schemas/rnaquantification.html>`_


--------------------
RNA Quantification
--------------------
The RNA Quantification provides a means of obtaining feature level quantifications derived from a set of RNA reads.


--------------
API Use Cases
-------------
Case 1: Obtain quantification data for one or more features (genes) in an RNASeq experiment

User desires:
Feature quantification data (numeric) for one or more features identified in an RNASeq experiment result.  User will provide a list of one or more features for which results should be returned.  If a feature list is not provided, all quantification results for the selected RNASeq experiment should be returned.  Numeric quantification should be provided as raw read count to allow for user conversion to desired units.  If desired TPM, RPKM or other enumerated units of measure can also be reported.

Additional Considerations:
An RNASeq experiment result is the output of running an analysis pipeline on a set of read data.  The result should have metadata that describes the pipeline that was used in detail.  It should include the identity of the input reads in enough detail to retrieve the read data.  All software used should include version, parameters and command line.  Any genome or transcriptome annotations used should be described in enough detail to retrieve the exact version used.  Any changes in software, parameters, annotations or other analysis details should result in a new RNASeq experiment result associated with that input read data.

Case 2: Obtain quantification data for one or more features (genes) for comparison between  multiple RNASeq experiments

User desires:
Feature quantification data (numeric) for one or more features identified in one or more RNASeq experiment results.  User will provide a list of one or more features for which results should be returned.  If a feature list is not provided, all quantification results for the selected RNASeq experiment(s) should be returned.  User will provide a list of one or more RNASeq experiments to obtain quantification results from.

Additional Considerations:
In order to request quantifications for comparison with either repository datasets or a local dataset the user needs to determine if the repository RNASeq experiment is comparable to other datasets.  Pipeline metadata needs to be provided so that this can be determined:
Sample-level: bio sample data such as tissue type, collection methods, sample preparation protocol, library generation protocol, spikes used
Read-level: sequencer type and protocol, sequence data generation software version, parameters and command line
Quantification-level: genome annotation, transcriptome annotation if any, software pipeline including versions, parameters and command line
Batch-level: Adjustments or normalization done at the batch level

Case 3: Obtain input data to use in Assembly activities

User desires:
Sequence level read data for both mapped and unmapped reads in the associated RNA experiment.  For typical read data this is contained in the fastq file(s) produced by the sequencer pipeline.  The API should either provide the original fastq or the read data necessary and sufficient to generate it.  It is desirable to be able to easily retrieve all the related reads at the fragment level for downstream analysis.  At this time, these would be either single or paired reads but for future-proofing the API should be able to handle the delivery of an arbitrary number of reads for a specific fragment.

Case 4: Obtain input data for DESeq Differential Expression analysis

User desires:
Feature quantification array for two or more comparable RNASeq experimental results.  This is similar to the case where the user requests feature level data.  In this case, it is critical that the user be able to identify comparable datasets.

Case 5: Obtain input data for RNASeq analysis by Kallisto software

User desires:
Calculate feature quantification by a new method.  In the Kallisto example here, the software does not utilize read alignments.  Repository needs to be able to supply raw read sequence (fastq format or convertible to fastq) and optionally annotation for the user.

Case 6: Obtain quantification data for non-read-based RNA experiments (MicroArrays)

User desires:
Discover and retrieve feature level quantification data that is derived from non-read-based sources such as the large sources of microarray-based expression data.  The quantification API needs to be source agnostic and allow for a general linking of quantity to feature.  It must be flexible and not lock the results to a reads/sequencer data collection model.  There should be no required data source or metadata fields that are specific for a given data collection method.


---------------------------------------
Annotation Design - RNA Considerations
---------------------------------------

Read data derived from RNA samples can differ from genomic read data due to the presence of non-genomic sequences.  An example would be a read that spans a splice junction.  It describes a contiguous sequence of reads, but a dis-continuous genomic region due to the missing intron.  Feature level read assignment is further complicated by the existence of multiple splice isoforms.  A read that can be definitely assigned to a particular feature (an exon in this case) may still not be definitely assigned to a particular transcript if multiple transcript share that exon.  The annotation API needs to be able to report assignment at the feature level as well as aggregate assignment at the transcript or even the whole gene level if assignment is not more specific than that.

Splicing (other post-transcriptional modifications?) can occur with degrees of complexity.  A ‘typical’ splice will result in a mature transcript with exon in positional (numerical) order in a head-to-tail orientation.  Back splicing (tail-to-head) can result in transcripts with the exon order reversed (1-3-2-4 instead of 1-2-3-4) and even circular RNA.  The exon order in a transcript as well as the orientation of the splice should be discoverable via the API.  In a more general case, the API should allow child features to have an ordered relationship.

The annotation API needs to also be flexible enough to handle multiple references in the same gene or transcript.  This is needed to cover the cases of fusion genes or inter-chromosomal translocations.

--------------------------
RNA Quantification Schema
--------------------------

The RNA Quantification Schema is designed around a quantification analysis.  Each set of feature quantifications describes the results of running an analysis ona set of input data.

The RnaQuantification identifies the experiment and describes the analysis pipeline used as well as the input dataset and annotations, if any, used.  ReadCounts and Characterization are optional API elements that further describe RNASeq analyses.

ExpressionLevel contains the identity of the specific feature measured as well as the final resulting quantification from the pipeline.  The FeatureSet exists to group related features if it is desirable to do so.  For example, in the case where exon-level quantifications would be grouped by parent gene or transcript.


..todo::
   Add visual schema representation

