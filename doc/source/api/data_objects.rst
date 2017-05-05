************
data_objects API
************

Goals and Scope
---------------

* standardized use of common attributes/values for data_objects(files, images and resources)
* comply with data_set container semantics

The API provides information on the data_objects and how the link to data_sets and other entities in the metadata schema.


DataObject Records
----------------

A data object represents a resource associated with a project, individual, sample or other metadata entity.

Data objects can belong to one or more `Dataset objects
<metadata.rst#refdatasetmetadata_dataset>`_.


**Dataobject Use Cases**

For server implementors, data_objects are a useful way
to represent data stored in a file system, object store 'bucket', API or other data management system.

For data curators, data_objects provide a mechanism to represent and exchange the data describing the underlying resources for a project or experiment.

For data accessors, data_objects are a simple way provide provenance and reproducibility.
