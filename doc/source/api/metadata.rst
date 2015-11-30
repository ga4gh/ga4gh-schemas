.. _metadata:


Metadata API
!!!!!!!!!!!!


Goals and Scope
@@@@@@@@@@@@@@@

The metadata API provides information on the primary data objects
available via the GA4GH API, and facilities to organize primary data
objects. Main goals of the metadata definitions are to provide

* standardized use of common attributes/values
* a schema of how objects relate to each other

The  metadata API is under continuous development.


Common Attribute Names and Formats
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Throughout the schema definitions, a consistent use of common attributes should
be enforced. The following list should serve as guidance for schema developers.


========================= ======================================================
Attribute                 Note
========================= ======================================================
id                        the objects ID, used for references; (at least) locally unique
name                      a more descriptive object label or legacy ID; should *not* be used as reference
accessions                an ``ARRAY`` containing other names, IDs, URIs of the object
description               a string describing aspects of the object; *not* a list or nested object itself
recordCreateTime          time at which this record was created in ISO 8601 (see **Date and Time...**)
recordUpdateTime          time at which this record was updated in ISO 8601 (see **Date and Time...**)
========================= ======================================================

Date and Time Format Specifications
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Date and time formats are specified as ISO8601 compatible strings, both for
time points as well as for intervals and durations.
The required granularity has to be specified as part of the respective
attributes' documentations.

===========
Time points
===========

The specification of a time point is given through the concatenation of

* a date in YYYY-MM-DD
* the designator "T" indicating a following time description
* the time of day in HH:MM:SS.SSS form, where "SSS" represents a decimal fraction of a second
* a time zone offset in relation to UTC

**Examples**

* year (YYYY)
    2015

* date (e.g. date of birth) in YYYY-MM-DD
    2015-02-10

* time stamp in milliseconds in YYYY-MM-DDTHH:MM:SS.SSS
    2015-02-10T00:03:42.123Z

**Implementations**

* recordCreateTime (G2P, metadata)
* recordUpdateTime (G2P, metadata)
* many proposed in the metadata branch

===========
Durations
===========

Durations are a specific form of intervals, without reference to time points.
They are indicated with a leading "P", followed by unit delimited
quantifiers. A leading "T" is required before the start of the time components.
Durations do not have to be normalized; "PT50H" is equally valid as "P2T2H".

**Examples**

* age in years in PnY
    P44Y

* age in years and months in PnYnM
    P44Y08M

* short time interval (e.g. 30min in experimental time series) in PTnM
    PT30M

==============
Time intervals
==============

Time intervals consist of a combination of two time designators. These can be
either two time points for start and end, or one time point and a leading
(time point indicates end) or trailing (time point indicates start) duration.
The time elements are separated by a forward slash "/".

**Examples**

* age with date of birth in YYYY-MM-DD/PnYnMnD
    1967-11-21/P40Y10M05D

* anchored 3 month interval, e.g. a therapy cycle in YYYY-MM-DD/YYYY-MM-DD
    2015-04-18/2015-07-17

* experimental intervention of 30min in YYYY-MM-DDTHH:MM/YYYY-MM-DDTHH:MM
    2014-12-31T23H45M/2015-01-01T00H15M


Object: Dataset
@@@@@@@@@@@@@@@

GA4GH data objects can be part of one or several *dataset*(s). A dataset is a
data-provider-specified collection of related data of multiple types.
Logically, it's akin to a folder, where it's up to the provider what
goes into the folder. Individual data objects are linked by optional
`datasetId` fields to `Dataset` objects
<../schemas/metadata.html#avro.Dataset>`_.

Since the grouping of content in a dataset is determined by the data
provider, users should not make semantic assumptions about that data.
Subsets of the data in a dataset can be selected for analysis using
other metadata or attributes.


**Use Cases**

For server implementors, datasets are a useful level of granularity
for implementing administrative features such as access control
(e.g. Data set X is public; data set Y is only available to lab Z's
collaborators) and billing (e.g. the costs of hosting Dataset Y should
be charged to lab Z).

For data curators, datasets are 'the simplest thing that could
possibly work' for grouping data (e.g. Dataset X has all the reads,
variants, and expression levels for a particular research project;
Dataset Y has all the work product from a particular grant).

For data accessors, datasets are a simple way to scope exploration and
analysis (e.g. are there any supporting examples in 1000genomes?
what's the distribution of that result in the data from our project?).


Issues (TODO)
@@@@@@@@@@@@@

- Metadata API is immature and under development.
- `sampleId` is referenced in reads and variants records of
  the schema, however this corresponds to a `BioSample` object defined in metadata.
- The role and usage of the `Dataset` object has to be evaluated critically.
- Lifecycle and version management of metadata objects is not clearly
  defined. Current objects make canonical use of timestamps for creation
  and update events; however, this could be left to non-API exposed,
  local implementations or addressed through a versioning schema.
- `Experiment` object is currently copied into the `ReadGroup` object.
  Given metadata becomes a chain of objects associated with the data,
  copying records seems less that ideal.
