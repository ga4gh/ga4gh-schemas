.. _apidesign:


API Design
!!!!!!!!!!


Object Ids
@@@@@@@@@@

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
  **name** field. The name is user-defined, isn’t programmatically
  required to be unique in any given scope (although in practice data
  owners will often choose unique names), and is intended to be human
  readable.  This can be thought of as a display name.

Cross-repository data federation will need a standard way to refer to
a data object, regardless of which repository it’s in. There is no
such standard currently, and the current API, including the id and
name fields, isn’t sufficient.  A future API may introduce standard
cross-repository identifiers using some combination of **content
hashes**, **GUIDs**, and central **accession** facilities.


ID and Name
@@@@@@@@@@@

Throughout the API objects have *IDs*. The purpose of IDs is to allow
unique identification of all objects within a single server, such that
no two objects in a given server have the same ID and no object has
more than one ID.  The scope of an ID is limited to a given server and
an ID may be an arbitrary string.

A name is a user defined identifier. Names need only be uniquely
identifying within a specific scope, for example, the names of
sequences within a ReferenceSet must be distinct, but there might be
two sequences named "chr1" stored in a server, each in a different
ReferenceSet. Names may be an arbitrary string.


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

    
Unresolved Issues
@@@@@@@@@@@@@@@@@

* Is the GA4GH object design a conceptual data model that must be
  followed or only containers for data exchange.  If they are
  containers, where is the conceptual data model defined?

* Are GA4GH objects idempotent?  In particular, can one obtain an
  object with a subset of it's fields?

* Is object life-cycle semantics in the scope of GA4GH API? Which
  objects are immutable and which are mutable?  If objects are
  mutable, how does one know they have changed?  How does one protect
  against changes while using the objects over a given time-frame?

* What is the definition of the wire protocol?  HTTP 1.0? Is HTTP 1.1
  chunked encoding allowed?  What is the specification for the
  generate JSON for a given an Avro schema?

* What is the role of Avro?  Is it for documentation-only or for use
  as an IDL?

* Need overall object relationship diagram.
