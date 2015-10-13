===========================================================
Formats for object identifiers (OID)
===========================================================

Object identifiers have properties based on varying requirements, 
depending on their usage. Main features to be considered are:

- uniqueness (global/local/none)
- content dependency (partial/full content hashing)
- generation (machine vs. readable/legacy)

//FIXME: the GUID question

Following attributes are used as record identifiers and descriptors:

id
--
- required
- (at least) locally unique
- systematic and/or machine generated
- possibly, but not necessarily "human readable" (GSM2492834, BRCA-2015-DCIS0012 ...)
- main type for (local) references

name
----
- not necessarily "clean"; possibly descriptive ("patient_25, PB")
- important for legacy data & "human parsing"
- not recommended for object references
  
versionId
---------
- (partial/complete) object hash
- version management (e.g. combined with time stamps)
- global references with absolut uniqueness

accessions
----------
- list of one or more IDs or URIs for public exposure of the object

description
-----------
- free text description of the object's scope

