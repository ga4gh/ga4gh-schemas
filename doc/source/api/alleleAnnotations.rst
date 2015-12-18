
Variant Annotation API
!!!!!!!!!!!!!!!!!!!!!!

See `Allele Annotation schema <../schemas/alleleAnnotations.html>`_ for a detailed reference.

Introduction
@@@@@@@@@@@@

Variant alleles can be annotated by comparing them to other reference data sets
using a variety of algorithms. A standard form of annotation is to compare 
alleles to a transcript set and calculate the expected functional consequence 
of the change ( e.g. a variant within a protein coding transcript may change the
amino acid sequence of the resulting protein).

This API supports the mining of variant annotations by region or genomic 
feature and the filtering of the results by predicted functional effect.

Variants Schema Entities
@@@@@@@@@@@@@@@@@@@@@@@@

The ``VariantAnnotation`` data model, is based on the results provided by variant 
annotation programs such as VEP, SnpEff and Annovar and others, as well as the 
VCF's `ANN format <http://snpeff.sourceforge.net/VCFannotationformat_v1.0.pdf>`_ . 


+---------------------+---------------------------------------------------------------------------------------------------------------------+
| Record              | Description                                                                                                         |
+=====================+=====================================================================================================================+
| VariantAnnotationSet| A VariantAnnotationSet record groups VariantAnnotation records. It represents the comparison of a VariantSet to a   |
|                     | specified reference data set using specified algorithms. It holds information describing the software and reference |
|                     | data versions use.                                                                                                  |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| VariantAnnotation   | A VariantAnnotation record represents the result of comparing a single variant to the set of reference data. It     |
|                     | contains structured sub-records and a flexible key-value pair ‘info’ field.                                         |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| TranscriptEffect    | A TranscriptEffect record describes the effect of an allele on a transcript.                                        |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| AlleleLocation      | An AlleleLocation record holds the location of an allele relative to a non-genomic coordinate system such as a CDS  |
|                     | or protein. It holds the reference and alternate sequence where appropriate                                         |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| AnalysisResult      | An AnalysisResult record holds the output of a prediction package such as SIFT on a specific allele.                |
+---------------------+---------------------------------------------------------------------------------------------------------------------+


TranscriptEffect attributes
@@@@@@@@@@@@@@@@@@@@@@@@@@@

A ``VariantAnnotation`` record may have many ``TranscriptEffect`` records as one is 
reported for each possible combination of alternate alleles and overlapping 
transcripts. The record includes:

* The identifier of the transcript feature the variant was analysed against.
* The alternate allele of the variant analysed. This is necessary as the current variant model supports multiple alternate alleles.
* The predicted effects of the allele on the transcript, which should be described using `Sequence Ontology <http://www.sequenceontology.org>`_ terms.
* Human Genome Variation Society (`HGVS <http://www.hgvs.org/mutnomen>`_ variant description nomenclature at genomic, transcript and protein level. 
* ``AlleleLocation`` records describing the changes at cDNA, CDS and protein level.
* A set of results from prediction packages analyzing the allele impact.
* A summary impact classification reflecting the highest impact consequence.

Predicted Molecular Impact Classification
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The predicted molecular impact is a simple prioritization based on the putative
deleteriousness of the variant allele on the transcript, which is popular with
users of annotation tools. This is usually calculated based on naive algorithms
and may not accurately predict true impact at protein level.

Predicted Molecular Impact classification is summarized using the terms:

+----------+-----------------------------------------------+-------------------------------------------+
| Impact   | Meaning                                       | Example SO terms                          |                   
+==========+===============================================+===========================================+
| HIGH     | Highly likely to disrupt protein function     | splice_donor_variant, stop_gained         |
+----------+-----------------------------------------------+-------------------------------------------+
| MODERATE | Moderately likely to disrupt protein function | missense_variant, inframe_insertion       |
+----------+-----------------------------------------------+-------------------------------------------+
| LOW      | Not likely to disrupt protein function        | synonymous_variant, stop_retained_variant |
+----------+-----------------------------------------------+-------------------------------------------+
| MODIFIER | No predicted effect                           | 3_prime_UTR_variant, intron_variant       |
+----------+-----------------------------------------------+-------------------------------------------+

Search Options
@@@@@@@@@@@@@@

VariantAnnotationSets can be extracted by Dataset or VariantSet, or retrieved by id.

A VariantAnnotationSet can be searched for VariantAnnotations by region and filters
can be applied.

* A region to search must be specified. This can be done by providing the id of one or more genomic features or a reference sequence (identified by name or id) with start and end coordinates.
* Results can be filtered by the predicted effect of the variant, using a Sequence Ontology OntologyTerm, or by variant name.

