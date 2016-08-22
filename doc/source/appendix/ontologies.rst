.. _metadata_ontologies:

Use of Ontologies in GA4GH API
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Examples for OntologyTerm use
-----------------------------

* Info: Ontogenesis blog
* Info: Working implementation of the GA4GH docsystem's Ontologies document

.. _ciliopathy:

Why should we use an ontology term?
===================================

* Info: http://ontogenesis.knowledgeblog.org/1296

A user may want to retrieve the rsIDs of all genomic variants to ciliopathies. Each rsID is annotated with a specific disease (e.g. Bardet Biedl syndrome, orofaciodigital syndrome). To query by a the functional grouping ‘ciliopathy’, classification of these diseases ciliopathies  is needed, and can be provided through an ontology.


Ontology Lookup Service
=======================

* http://www.ebi.ac.uk/efo/EFO_0003900
* multiple child classes are returned, including those without a lexical match to the disease name

The effective use of ontology lookups requires the annotation of rsIDs with
unique identifiers for the associated diseases, so that a programmatic lookup
can use these to identify their parents and/or relations. Text queries are
likely to return partial or erroneous result sets. Ontologies overlap in their
scope, design and content. In the case of results from different ontologies,
which may have a varying depth, the executioner of the query has to judge
about the optimal scope of the returned data.


What is the minimum attribute requirement for  OntologyTerm in GA4GH?
=====================================================================

Conceptually (and consistent with the metadata branch)

:termId:
  The unique identifier of the term in an ontology source. This should be a CURIE (e.g., SO:0001234), but may be an alphanumerical string (e.g., 8000/3) if no CURIE are available.
:term:
  preferred but not required (e.g. ‘exon’); corresponds to class label
:termUri:
  A fully qualified URI that can be used to access details regarding the term. e.g. http://purl.bioontology.org/ontology/SNOMEDCT/76345009.
:sourceName:
  not required since should be resolved from prefix etc., but supporting/fall-back in case of non-standard/deprecated/entropic annotations; possible use for CURIEs in compact sequence ontology implementations  (e.g. SO:0000147)
:sourceVersion:
  not required but good practice; if no explicit versioning, ISO8601 formatted data of retrieval should be used.


Ontology Selection and Overlap
==============================

Sometimes a single ontology provides excellent coverage of a domain. For
example, the Sequence Ontology is used successfully in GFF files to annotate
exons, introns, etc. There are multiple ontologies in some domains which overlap
in scope and content and also interoperation between ontologies.


For example, the Human Phenotype Ontology (HP) provides terms describing human phenotypes.
Disease phenotype associations are not provided directly by the HP, but rather as supporting
files with common cross references such as OMIM identifiers.


When selecting an ontology consider coverage - how much of your data is represented? Does the ontology provide structure that meets your use cases? For the case above
contains a class ciliopathy_, update frequency, ability to request
terms when needed, adherence to community standards  e.g. OBO foundry provides
recommendations on versioning strategy and term deprecation.
Note that OBO policy dictates that when the meaning of a class changes,
then the identifier/IRI is deprecated/obsoleted, and a new identifier/IRI is
minted. As a consequence, many databases that store associations to OBO classes
(genes, diseases to phenotype etc) do not record the version of the ontology,
as the semantics of the ID can be treated as immutable.

.. _`Why use the Human Phenotype Ontology`: http://monarch-initiative.blogspot.ch/2015/05/why-human-phenotype-ontology.html

* Info: `Why use the Human Phenotype Ontology`_ (blog post by Melissa Haendel)


*Age, date, time interval values => ISO8601* (see :ref:`Date and Time<metadata_date_time>`)


Examples
--------

Genotypic sex
=============

:termId:
  "PATO:0020001",
:term:
  "male genotypic sex" ,
:termUri:
  "http://purl.obolibrary.org/obo/PATO_0020001"
:sourceName:
  "PATO Phenotypic quality",


Sequence Ontology
=================

:termId:
  "SO:0001583",
:term:
  "missense_variant",
:termUri:
  "http://purl.obolibrary.org/obo/SO_0001583",
:sourceName:
  "Sequence Ontology",
:sourceVersion:
  "release_2.5.3"


Human Phenotype ontology
========================

:termId:
  "HP:0000819",
:term:
  "Diabetes mellitus",
:termUri:
  "http://purl.obolibrary.org/obo/HP_0000819",
:sourceName:
  "human_phenotype Ontology",
:sourceVersion:
  "release_Jan2016*"

----

:termId:
  "HP:0012059",
:term:
  "Lentigo maligna melanoma",
:termUri:
  "http://www.ebi.ac.uk/efo/HP_0012059",
:sourceName:
  "human_phenotype_ontology",
:sourceVersion:
  "2016-01-14”


Body part (Uberon)
==================

:termId:
  "UBERON:0003403",
:term:
  "skin of forearm",
:termUri:
  "http://www.ebi.ac.uk/efo/UBERON_0003403",
:sourceName:
  "uberon",
:sourceVersion:
  "2015-11-23”


Human disease ontology
======================

:termId:
  "DOID:9351",
:term:
  "diabetes mellitus",
:termUri:
  "DOID_9351",
:sourceName:
  "disease_ontology",
:sourceVersion:
  "2016-01-25"


Experimental factor ontology
============================

:termId:
  "EFO:0000400",
:term:
  "diabetes mellitus",
:termUri:
  "http://purl.obolibrary.org/obo/EFO_0000400",
:sourceName:
  "experimental_factor_ontology",
:sourceVersion:
  "V2.68”

----

:termId:
  "EFO:0004422",
:term:
  "exome",
:termUri:
  "http://www.ebi.ac.uk/efo/EFO_0004422",
:sourceName:
  "Experimental Factor Ontology",
:sourceVersion:
  "release_2.68"


SNOMEDCT representation of ICD-O 3 Cancer Histology
===================================================

:termId:
  "M-94703“,
:term:
  "Medulloblastoma, NOS”,
:termUri:
  "http://purl.bioontology.org/ontology/SNMI/M-94703",
:sourceName:
  "SNOMED CT model component”,
:sourceVersion:
  "2016-01-28"


Unit Ontology
=============

:termId:
  "UO:0000016",
:term:
  "millimetre",
:termUri:
  "http://purl.obolibrary.org/obo/UO_0000016",
:sourceName:
  "Unit Ontology",
:sourceVersion:
  "2015-12-17"
