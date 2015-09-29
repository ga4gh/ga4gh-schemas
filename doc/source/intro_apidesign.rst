.. _apidesign:

****************************
GA4GH API Design
****************************
=============
Object Ids
=============

* Many objects need to be referenced by the API (e.g. a search method may return a list of objects) and by applications built outside the API (e.g. a visualization app may refer back to the objects being shown). The API has a standard mechanism for referring to such objects.

* The standard way to programmatically reference an object is via an **id** field. The id is server-assigned, and must provide “id-like” semantics, including:

  * ids are unique within the scope of the server instance
  * ids are durable for the lifetime of the server, and persistent across server restarts -- once a user is given an ID for data stored on a server, the id remains valid for as long as the server is still storing that data

* Many objects, including most ‘container’ objects, also have a **name** field. The name is user-defined, isn’t programmatically required to be unique in any given scope (although in practice data owners will often choose unique names), and is intended to be human readable.  This can be thought of as a display name.

Cross-repository data federation will need a standard way to refer to a data object, regardless of which repository it’s in. There is no such standard currently, and the current API, including the id and name fields, isn’t sufficient.
A future API may introduce standard cross-repository identifiers using some combination of **content hashes**, **GUIDs**, and central **accession** facilities.

=====================
Object Relationships
=====================

* Some objects are contained by other objects. These relationships can be

  * many:1 (e.g. ReadGroupSets in a Dataset); aka single-include
  * many:many (e.g. ReadGroups in a ReadGroupSet); aka multi-include

* Some objects are derived from other objects. These relationships can be

  * many:1 (e.g different aligned ReadGroupSet’s derived from an unaligned ReadGroupSet using different alignment algorithms and/or reference sequences)
  * many:many (e.g. different VariantSets derived from a collection of ReadGroupSets using different joint variant calling algorithms)
