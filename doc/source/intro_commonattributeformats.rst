===========================================================
Formats for object identifiers (OID)
===========================================================

Object identifiers have properties based on varying requirements, 
depending on their usage. Main features to be considered are:

* uniqueness (global/local/none)
* content dependency (partial/full content hashing)
* generation (machine vs. readable/legacy)

Following attributes are used as record identifiers and descriptors:

* id
  * required
  * locally unique
  * systematic and/or "readable" in local context (GSM2492834, BRCA-2015-DCIS0012; partial hash ...)
  * main type for (local) references
* guid
  * UUIDv4
  * assumed to be globally unique without central arbitration, due to its structure
  * computer generated at creation
  * global references (though no guarantee that not duplication of another object)
* name
  * not necessarily "clean"; possibly descriptive ("patient_25, PB")
  * important for legacy data & "human parsing"
  * not recommended for object references
* versionId
  * (partial/complete) object hash
  * version management (e.g. combined with time stamps)
  * global references with absolut uniqueness
* accessions
  * list of one or more IDs or URIs for public exposure of the object
* description
  * free text description of the object's scope

