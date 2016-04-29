.. _apidesign:


API Design
!!!!!!!!!!

.. _apidesign_object_ids:
Object Ids and Names
@@@@@@@@@@@@@@@@@@@@

* Many objects need to be referenced by the API (e.g. a search method
  may return a list of objects) and by applications built outside the
  API (e.g. a visualization app may refer back to the objects being
  shown). The API has a standard mechanism for referring to such
  objects.

* The standard way to programmatically reference an object is via an
  **id** field. The id is server-assigned, and must provide “id-like”
  semantics, including:

  * ids are unique within the scope of the server instance

  * ids are durable for the lifetime of the server, and persistent
    across server restarts -- once a user is given an ID for data
    stored on a server, the id remains valid for as long as the server
    is still storing that data

* Many objects, including most ‘container’ objects, also have a
  **name** field. The name is user-defined with the uniqueness requirements
  vary between the various objects types.  Some containers require name
  uniqueness within their scope, other don't enforce a uniqueness requirement.
  Unless explicitly stated, there is no uniqueness requirement should be
  assumed. It is intended to be human readable, although usually symbolic, not
  a natural language description.

Cross-repository data federation will need a standard way to refer to
a data object, regardless of which repository it’s in. There is no
such standard currently, and the current API, including the id and
name fields, isn’t sufficient.  A future API may introduce standard
cross-repository identifiers using some combination of **content
hashes**, **GUIDs**, and central **accession** facilities.


Object Relationships
@@@@@@@@@@@@@@@@@@@@

* Some objects are contained by other objects. These relationships can
  be

  * many:1 (e.g. ReadGroupSets in a Dataset); aka single-include

  * many:many (e.g. ReadGroups in a ReadGroupSet); aka multi-include

* Some objects are derived from other objects. These relationships can
  be

  * many:1 (e.g different aligned ReadGroupSet’s derived from an
    unaligned ReadGroupSet using different alignment algorithms and/or
    reference sequences)

  * many:many (e.g. different VariantSets derived from a collection of
    ReadGroupSets using different joint variant calling algorithms)

Dataset
@@@@@@@

A dataset is a highest level grouping that contains sequence and
variant data. It provides the concept of a container which allows high
level separation between data.

For the Dataset schema definition see the `Metadata schema
<schemas/metadata.html>`_

    
