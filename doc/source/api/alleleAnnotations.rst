
Allele Annotation API
!!!!!!!!!!!!!!!!!!!!!!

See `Allele Annotation schema <../schemas/alleleAnnotations.html>`_ for a detailed reference.

Introduction
@@@@@@@@@@@@

Variant alleles can be annotated by comparing them to gene annotation data
using a variety of algorithms. A standard form of annotation is to compare 
alleles to a transcript set and calculate the expected functional consequence 
of the change ( e.g. a variant within a protein coding transcript may change the
amino acid sequence of the resulting protein).

This API supports the mining of variant annotations by region 
and the filtering of the results by predicted functional effect.

Allele Annotation Schema Entities
@@@@@@@@@@@@@@@@@@@@@@@@

The ``VariantAnnotation`` data model, is based on the results provided by variant 
annotation programs such as VEP, SnpEff and Annovar and others, as well as the 
VCF's `ANN format <http://snpeff.sourceforge.net/VCFannotationformat_v1.0.pdf>`_ . 


+---------------------+---------------------------------------------------------------------------------------------------------------------+
| Record              | Description                                                                                                         |
+=====================+=====================================================================================================================+
| VariantAnnotationSet| A VariantAnnotationSet record groups VariantAnnotation records. It represents the comparison of a VariantSet to     |
|                     | specified gene annotation data using specified algorithms. It holds information describing the software and         |
|                     | annotation data versions used.                                                                                      |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| VariantAnnotation   | A VariantAnnotation record represents the result of comparing a single variant to the set of annotation data. It    |
|                     | contains structured sub-records and a flexible key-value pair ‘info’ field.                                         |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| TranscriptEffect    | A TranscriptEffect record describes the effect of an allele on a transcript.                                        |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| AlleleLocation      | An AlleleLocation record holds the location of an allele relative to a non-genomic coordinate system such as a CDS  |
|                     | or protein. It holds the reference and alternate sequence where appropriate                                         |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| HGVSAnnotation      | A HGVSAnnotation record holds Human Genome Variation Society ( `HGVS <http://www.hgvs.org/mutnomen/recs.html>`_ )   |
|                     | descriptions of the sequence change at genomic, transcript and protein level where relevant.                        |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| AnalysisResult      | An AnalysisResult record holds the output of a prediction package such as SIFT on a specific allele.                |
+---------------------+---------------------------------------------------------------------------------------------------------------------+

The schema is shown in the diagram below.

.. image:: /_static/variant_annotation_schema.svg


TranscriptEffect attributes
@@@@@@@@@@@@@@@@@@@@@@@@@@@

A ``VariantAnnotation`` record may have many ``TranscriptEffect`` records as one is 
reported for each possible combination of alternate alleles and overlapping 
transcripts. The record includes:

* The identifier of the transcript feature the variant was analysed against.
* The alternate allele of the variant analysed. This is necessary as the current variant model supports multiple alternate alleles.
* The predicted effects of the allele on the transcript, which should be described using `Sequence Ontology <http://www.sequenceontology.org>`_ terms.
* A ``HGVSAnnotation`` record containing variant descriptions at all relevant levels. 
* ``AlleleLocation`` records describing the changes at cDNA, CDS and protein level.
* A set of results from prediction packages analyzing the allele impact.

Search Options
@@@@@@@@@@@@@@

VariantAnnotationSets can be extracted by Dataset or VariantSet, or retrieved by id.

A VariantAnnotationSet can be searched for VariantAnnotations by region and filters
can be applied.

* A region to search must be specified. This can be done by providing a reference sequence (identified by name or id) with start and end coordinates.
* Results can be filtered by the predicted effect of the variant using a Sequence Ontology OntologyTerm.

