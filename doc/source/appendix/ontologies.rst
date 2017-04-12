.. _metadata_ontologies:

Use of Ontologies in GA4GH API
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Examples for OntologyTerm use
-----------------------------

* Info: Ontogenesis blog
* Info: Working implementation of the GA4GH docsystem's Ontologies document


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

:term_id:
  required and implemented as CURIE
  we assume this resolves to a meaningful document, e.g. http://purl.obolibrary.org/obo/SO_0000147, using a prefix mapper, e.g. SO: <=> http://purl.obolibrary.org/obo/SO_
:term:
  preferred but not required (e.g. ‘exon’); corresponds to class label


Ontology Selection and Overlap
==============================

Sometimes a single ontology provides excellent coverage of a domain. For
example the Sequence Ontology is used successfully in GFF files to annotate
exons, introns etc. There are multiple ontologies in some domains which overlap
in scope and content and also interoperation between ontologies. For example
the Human Phenotype Ontology (HP) provides terms describing human phenotypes.
Disease phenotype associations are not provided in the HP, rather as supporting
files with common cross references such as OMIM identifiers. When selecting an
ontology consider coverage - how much of your data is represented; structure -
does the ontology provide structure that meets your use cases, e.g.
contains a class ciliopathy (see above), update frequency, ability to request
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

:term_id:
	"PATO:0020001",
:term:
  "male genotypic sex" ,

Sequence Ontology
=================

:term_id:
  "SO:0001583",
:term:
	"missense_variant",

Human Phenotype ontology
========================

:term_id:
  "HP:0000819",
:term:
  "Diabetes mellitus",

----

:term_id:
  "HP:0012059",
:term:
  "Lentigo maligna melanoma",

Body part (Uberon)
==================

:term_id:
	"UBERON:0003403",
:term:
	"skin of forearm",

Human disease ontology
======================

:term_id:
	"DOID:9351",
:term:
	"diabetes mellitus",

Experimental factor ontology
============================

:term_id:
	"EFO:0000400",
:term:
	"diabetes mellitus",

----

:term_id:
	"EFO:0004422",
:term:
	"exome",


Unit Ontology
=============

:term_id:
	"UO:0000016",
:term:
	"millimetre",
