
Variant Annotation API
!!!!!!!!!!!!!!!!!!!!!!

See `Allele Annotation schema <../schemas/alleleAnnotations.html>`_ for a detailed reference.

Introduction
@@@@@@@@@@@@

Variant alleles can be annotated by comparing them to other reference data sets
using a variety of algorithms. A standard form of annotation is to compare 
alleles to a transcript set and calculate the expected functional consequence 
of the change (e.g. an amino acid change a protein coding transcripts affected 
by the variant).

This API supports the mining of variant annotations by region or genomic 
feature and the filtering of the results by predicted functional effect.

Variants Schema Entities
@@@@@@@@@@@@@@@@@@@@@@@@

The ``VariantAnnotation`` data model, is based on the results provided by variant 
annotation programs such as VEP, SnpEff and Annovar and others, as well as the 
VCF's `ANN format <http://snpeff.sourceforge.net/VCFannotationformat_v1.0.pdf>`_ . 

Instead of sending whole set of annotations, the server can send information 
on specific variants, genomic regions or annotations instead.

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
| TranscriptEffect    | A transcript effect record describes the effect of an allele on a transcript.                                       |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| AlleleLocation      | An allele location record holds the location of an allele relative to a non-genomic coordinate system such as a CDS |
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

Impact Classification
@@@@@@@@@@@@@@@@@@@@@

The predicted impact is a simple prioritization or classification based on the 
putative deleteriousness of the variant allele on the transcript. This is usually 
calculated based on naive algorithms and may not accurately predict true impact 
at protein level. 

Impact classification is summarized using the terms:

+----------+----------------------------------------------+
| Impact   | Meaning                                      |
+==========+==============================================+
| HIGH     | the variant highly disrupts protein function |
+----------+----------------------------------------------+
| MODERATE | Moderately disrupts protein function         |
+----------+----------------------------------------------+
| LOW      | Low disruption of protein impact             |
+----------+----------------------------------------------+
| MODIFIER | No known effect                              |
+----------+----------------------------------------------+

