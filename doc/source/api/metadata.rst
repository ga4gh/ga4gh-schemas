.. _metadata:

************
Metadata API
************

---------------
Goals and Scope
---------------

The metadata API provides information on the primary data object available via
the GA4GH API.  It also provides facilities to organizing primary data
objects.

The current metadata API is immature and will evolve in future.

------
Design
------


**Data organization**

All data objects in GA4GH are part of a *data set*. A data set is a
data-provider-specified collection of related data of multiple types.
Logically, it's akin to a folder. It's up to the provider what goes into the
folder.  A data objects are linked by `dataSetId` to `Dataset objects
<../schemas/metadata.html#avro.Dataset>`_.

For server implementors, they're a useful level of granularity for
implementing administrative features such as access control (e.g. Data sett X
is public; data set Y is only available to lab Z's collaborators) and billing
(e.g. the costs of hosting Dataset Y should be charged to lab Z).

For data curators, they're 'the simplest thing that could possibly work' for
grouping data (e.g. Dataset X has all the reads, variants, and expression
levels for a particular research project; Dataset Y has all the work product
from a particular grant).

One should not make undue semantic assumptions on data in a data set.  A
subset of data in a data set is normally select for analysis using other
metadata or attributes.

---------
Use Cases
---------

TODO: use cases need to be specified

-------------
Issues (TODO)
-------------
- Metadata API is immature and under development.
- `sampleId` is referenced in metadata, reads, and variants records of the
  schema, however there is no `Sample` object defined in metadata.
- There is some disagreement of the role of the `Dataset` by members of the DWG.
- Life cycle and version management of metadata objects is not clearly defined.
  This includes use of times
- `Experiment` object is currently copied into the `ReadGroup` object.  Given
  metadata becomes a chain of objects associate with the data, coping records
  seems less that ideal.
