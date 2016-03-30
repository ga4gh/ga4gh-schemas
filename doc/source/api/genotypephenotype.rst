.. _genotypephenotype:

Summary
-------

This API endpoint allows users to search for genotype-phenotype
associations in a GA4GH datastore. The user can search for associations
by building queries composed of features, phenotypes, and/or evidence
terms. The API is designed to accommodate search terms specified as
either a string, external identifier, ontology identifier, or as an
'entity' (See Data Model section). These terms are combined as an
``AND`` of ``(feature && phenotype && evidence)``. This flexibility in
the schema allows a variety of data to be stored in the database and
allows users to express a wide range of queries.

Users will receive an array of associations as a response. Associations
contain description and environment fields in addition to the relevant
feature, phenotype, and evidence fields for that instance of
association.

API
---

Request
~~~~~~~

The G2P schemas define a single endpoint ``/genotypephenotype/search``
which accepts a POST of a `request body <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotypemethods.avdl#L102>`__
in `JSON <http://json.org/example.html>`__ format. The request may
contain a feature, phenotype, and/or evidence, which are combined as a
logical AND to query the underlying datastore. Missing types are treated
as a wildcard, returning all data.

|image| http://yuml.me/edit/bf06b90a

Response
~~~~~~~~

`Responses <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotypemethods.avdl#L130>`__
of matching data are returned as a list of
`FeaturePhenotypeAssociation <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotype.avdl#L132>`__\ s.

.. figure:: /_static/g2p_response.png
   :alt: image

   image

http://yuml.me/edit/25343da1 ## Data Model

Intent: The GA4GH Ontology schema provides structures for unambiguous
references to ontological concepts and/or controlled vocabularies within
AVRO. The structures provided are not intended for de novo modeling of
ontologies, or representing complete ontologies within AVRO. References
to e.g. classes from external ontologies or controlled vocabularies
should be interpreted only in their original context i.e. the source
ontology.

Due to the flexibility of the data model, users have a number of options
for specifying each query term
(`feature <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotypemethods.avdl#L105>`__,
`phenotype <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotypemethods.avdl#L108>`__,
and
`evidence <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotypemethods.avdl#L111>`__).
For instance, a feature can potentially be represented in increasing
specificity as either [a string, an ontology identifier, an external
identifier, or as a feature 'entity'].

The POST data sent as part of ``/genotypephenotype/search`` must be in
JSON format and must obey the
`SearchFeaturesRequest <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotypemethods.avdl#L102>`__
schema.
`SearchFeaturesResponse <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/genotypephenotypemethods.avdl#L130>`__
is the response from ``POST /genotypephenotype/search``, also expressed
as JSON.

The ``SearchFeaturesRequest`` and ``SearchFeaturesResponse`` records
each have their own data structures, but they use many of the same types
(see the 3rd table for shared data-types). Many types rely heavily on
the concept of an
`OntologyTerm <https://github.com/ga4gh/schemas/blob/be171b00a5f164836dfd40ea5ae75ea56924d316/src/main/resources/avro/ontologies.avdl#L10>`__
(see end of document for discussion on usage of OntologyTerms).

Use cases
---------

1) As a clinician or a genomics researcher, I may have a patient with
   Gastrointestinal stromal tumor, GIST, and a proposed drug for
   treatment, imatinib. In order to identify whether the patient would
   respond well to treatment with the drug, I need a list of features
   (e.g. genes) which are associated with the sensitivity of GIST to
   imatinib. Suppose I am specifically interested in a gene, *KIT*,
   which is implicated in the pathogenesis of several cancer types. I
   could submit a query to ``/genotypephenotype/search`` with GIST as
   the phenotype, *KIT* as the feature, and
   `clinical study evidence <http://purl.obolibrary.org/obo/ECO_0000180>`__
   as the evidence.

In response, I will receive back a list of associations involving GIST
and *KIT*, which I can filter for instances where imatinib is mentioned.
URI's in the ``associations`` field could - hypothetically - be followed
to discover that `GIST patients with wild-type *KIT* have decreased
sensitivity to therapy with
imatinib <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2651076/>`__.

If I left both the ``genotype`` and ``evidence`` fields as ``null``, I
would receive back all associations which involve GIST as a phenotype.

2) As a non-Hodgkin's lymphoma researcher, I may know that the gene
   *CD20* has abnormal expression in
   `Hodgkin's lymphoma <http://purl.obolibrary.org/obo/DOID_8567>`__.
   I might be interested in knowing whether *CD20* also has abnormal
   expression in
   `non-Hodgkin lymphoma <http://purl.obolibrary.org/obo/DOID_0060060>`__.
   Therefore I could perform a query with *CD20* as a feature,
   non-Hodgkin's lymphoma as a phenotype, and
   `RNA sequencing <http://purl.obolibrary.org/obo/OBI_0001177>`__
   as the evidence type.

3) As a genetic counselor, I may be wondering if a mutation in one of my
   clients' genes has ever been associated with a disease. I could then
   do a query based on the gene name as the feature and
   `disease <http://purl.obolibrary.org/obo/DOID_4>`__ as the
   phenotype.

For specifics of the json representations, please see the
`server <https://github.com/ga4gh/server>`__ and
`compliance <https://github.com/ga4gh/compliance>`__ repositories.

Ontologies
----------

**Usage:** Multiple ontology terms can be supplied e.g. to describe a series
of phenotypes for a specific sample. The ontology.avdl is not intended
to model relationships between terms, or to provide mappings between
ontologies for the same concept. Should an OntologyTerm be unavailable,
or terms unmapped then an 'annotation' can be provided which can later
be mapped to an ontology term using a service designed for this. Using
OntologyTerm is preferred to using Annotation. Though annotations can be
supplied with related ontology terms if desired. A use case could be
when a free text annotation is very specific and a more general
OntologyTerm is supplied.


**Definitions:**

*Annotation* - A free text annotation which is not an
ontology term describing some attribute. Annotations have associations
with OntologyTerms to allow these to be added after annotations are
captured. OntologyTerms are preferred over Annotations in all cases.
Annotations can be used in conjucntion with OntologyTerms

*OntologyTerm* - the preferred term for the class in question. For example
http://purl.obolibrary.org/obo/HP\_0011927 preferred term is 'short
digit' and synonym is 'VERY SHORT DIGIT'. 'short digit' is the term that
should be used.


*OntologyTerm identifier* - An identifier for a single ontology term from
a single ontology source specified as a CURIE (preferred) or PURL

*OntologySource* - the name of ontology from which the term is obtained.
e.g. 'Human Phenotype Ontology'

*OntologySource identifier* - the identifier -a CURIE (preferred) or PURL
for an ontology source e.g. http://purl.obolibrary.org/obo/hp.obo

*OntologySource version* - the version of the ontology from which the
OntologyTerm is obtained. E.g. 2.6.1. There is no standard for ontology
versioning and some frequently released ontologies may use a datestamp,
or build number.

**Implementation Guidance: Queries**

*Id Searches: Feature Lookup*

| Q: I have a SNPid ("rs6920220"). Create an External Identifier Query.
| ``{… "feature": {"ids": [{"identifier": "rs6920220", "version": "*", "database": "dbSNP"}]},  … }``
| The system should respond with features that match on external identifier

| Q: I have a featureId  ("f12345").
| Create a GenomicFeatureQuery
| ``{… "feature" : {"features", [{id:"f12345"}]  … }``
| The system should respond with features that match on that identifier
| Clarification needed - why not use the <string> Feature type?


*Id Searches: Phenotype Lookup*

| Q: I have a Disease ontology id ("http://www.ebi.ac.uk/efo/EFO_0003767").
| Use an OntologyTermQuery.
| The system should respond with phenotypes that match on OntologyTerm.id

| Q: I have a phenotype id (“p12345”)
| Create an PhenotypeQuery using id field.
| ``{"id": "p12345",...}``
| The system should respond with phenotypes that match on PhenotypeInstance.id

**Implementation Guidance: Results**

| Q: I need a place to store publication identifiers or model machine learning and statistical data
| A: The "info" key value pair addition to Evidence

>>>
    {
      "evidenceType": {
        "sourceName": "IAO",
        "id": "http://purl.obolibrary.org/obo/IAO_0000311",
        "sourceVersion": null,
        "term": "publication"
      },
      "info": {"source": ["PMID:21470995"]},
      "description": "Associated publication"
    }
    {
      "evidenceType": {
        "sourceName": "OBI",
        "id": "http://purl.obolibrary.org/obo/OBI_0000175",
        "sourceVersion": null,
        "term": "p-value"
      },
      "info": {"p-value": ["1.00e-21"]}
      "description": "Associated p-value"
    },
    {
      "evidenceType": {
        "sourceName": "OBCS",
        "id": "http://purl.obolibrary.org/obo/OBCS_0000054",
        "sourceVersion": null,
        "term": "odds ratio"
      },
      "description": "1.102"
    }
>>>

**Current work**
~~~~~~~~~~~~~~~~

*Background*

G2P servers are implemented in three different contexts:

* As a wrapper around standalone local G2P "knowledge bases" (eg Monarch, CiVIC,etc).  Important considerations are the API needs to function independently of other parts of the API and separately from any specific omics dataset.  Often, these databases are not curated with complete Feature fields (referenceName,start,end,strand)

|image-g2p-standalone|

* Coupled with sequence annotation and GA4GH datasets.  Clients will want implementation specific featureId/genotypeId to match and integrate with the rest of the APIs.

|image-g2p-integrated|


* Operating in concert with other instances of g2p servers where the client's loosely federated query is supported by heterogeneous server.  Challenges:  Normalizing API behavior across implementations (featureId for given region different per implementation)

|image-g2p-federated|

**Problems**

*Flexible representation of Feature*

Not all G2P databases have complete genomic location information or are associated with GA4GH omics dataset.


*Free form strings in queries*

>>>
If I understand this correctly, I think we should be concerned about clashing of unscoped identifiers. For example, I read this as supporting something like { 'phenotype': ['FH'] }, in which I think it's unclear whether that's FH the gene (via "ExternalIdentifierQuery") or Familial Hypercholesterolemia (via "PhenotypeQuery"). Is that (or something like it) a valid concern here?
https://github.com/ga4gh/schemas/pull/432#issuecomment-189512499
The semantics of SearchGenotypePhenotypeRequest are very unclear. I would really have no idea how to construct a query.
https://github.com/ga4gh/schemas/pull/432#discussion_r54935254
>>>

Search for Feature - alternatives

| #1 Q: I have a gene name / variant name / protein name  ("KIT").
| Create a GenomicFeatureQuery, use Key values suggested by http://www.sequenceontology.org/gff3.shtml
| ``{... "feature": {"attributes": {"vals": {"Name": ["KIT"]}},...} }``
| The system should respond with features that match on that name. The system should match on wildcards

| #2 Q: I have a feature description  ("KIT N822K").
| Create a GenomicFeatureQuery, use Key values suggested by http://www.sequenceontology.org/gff3.shtml
| ``{... "feature": {"attributes": {"vals": {"Description": ["KIT N822K"]}},...} }``
| The system should respond with features that match on that description. The system should match on wildcards

| Clarification needed - If these examples are valid, why support  <string> Feature type?
| e.g: I have an arbitrary string("KIT N822K").
| Create a simple string query, submit to /geneotypephenotype/search
| ``{… "feature" :"KIT N822K",  … }``

| Alternative: Create a new endpoint  /feature/search that takes a `term` or `wildcard`
| POST /search/feature
| { "term" : { "name" : "KIT" }  }
| { "term" : { "description" : "KIT N822K" }  }
| { "wildcard" : { "name" : "K??" }  }
| { "wildcard" : { "description" : "KIT N82*" }  }
| The system should respond with features that match on the field described.
| The client would then use the featureIds returned to re-query  /genotypephenotype/search

| Alternative: Re-use endpoint /geneotypephenotype/search, create replace new type TermQuery

>>>
record TermQuery {
  /**
  The query type, currently `term` (exact match) or `wildcard` (regexp).
  */
 union { null, map<string> } term = {};
 union { null, map<string> } wildcard = {};
}
record SearchGenotypePhenotypeRequest {
...
union {null, TermQuery, ExternalIdentifierQuery, OntologyTermQuery,GenomicFeatureQuery} feature = null;
...
}
>>>

| The system should respond with features that match on the field described.



Search for Phenotype alternatives

| #1 Q: I have a disease name "inflammatory bowel disease"
| Create an PhenotypeQuery using description field.
| ``{"description": "inflammatory bowel disease",...}``
| The system responds with Phenotypes that match on OntologyTerm.term

| #2 Q: I have a disease name "inflammatory bowel disease"
| Use a simple string query.
| ``{… "phenotype" :"inflammatory bowel disease",  … }``
| The system responds with Phenotypes that match on OntologyTerm.term

| #3 Q: I have a disease name "inflammatory bowel disease"
| Alternative, use TermQuery for phenotype
| ``{ "term" : { "name" : "inflammatory bowel disease" }  }``
| The system responds with Phenotypes that match on OntologyTerm.term


Multiple server collation

| #1 Q: I have results from multiple G2P Servers.  How do I collate them?
| Use HGVS annotation to identify identical features?






.. |image| image:: /_static/g2p_request.png
.. |image-g2p-standalone| image:: /_static/g2p-standalone.png
.. |image-g2p-integrated| image:: /_static/g2p-integrated.png
.. |image-g2p-federated| image:: /_static/g2p-federated.png
