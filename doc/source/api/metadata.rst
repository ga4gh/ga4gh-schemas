.. _metadata:


Metadata API
!!!!!!!!!!!!


Goals and Scope
@@@@@@@@@@@@@@@

The metadata API provides information on the primary data objects
available via the GA4GH API, and facilities to organize primary data
objects.

The current metadata API is immature and will evolve in future.


Datasets
@@@@@@@@


All GA4GH data objects are part of a *dataset*. A dataset is a
data-provider-specified collection of related data of multiple types.
Logically, it's akin to a folder, where it's up to the provider what
goes into the folder. Individual data objects are linked by
`datasetId` fields to `Dataset objects
<../schemas/metadata.html#avro.Dataset>`_.

Since the grouping of content in a dataset is determined by the data
provider, users should not make semantic assumptions about that data.
Subsets of the data in a dataset can be selected for analysis using
other metadata or attributes.

.. _metadata_date_time:

Date and Time Format Specifications
-----------------------------------

Date and time formats are specified as ISO8601 compatible strings, both for
time points as well as for intervals and durations.
An optional required granularity may be specified as part of the respective
attributes' documentations.

Time points
===========

The specification of a time point is given through the concatenation of

* a date in YYYY-MM-DD
* the designator "T" indicating a following time description
* the time of day in HH:MM:SS.SSS form, where "SSS" represents a decimal
  fraction of a second
* a time zone offset in relation to UTC

**Examples**

* year (YYYY)
    2015

* date (e.g. date of birth) in YYYY-MM-DD
    2015-02-10

* time stamp in milliseconds in YYYY-MM-DDTHH:MM:SS.SSS
    2015-02-10T00:03:42.123Z

**Implementations**

* created
* updated
* many proposed in metadata branch

Durations
=========

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
- `sampleId` is referenced in metadata, reads, and variants records of
  the schema, however there is no `Sample` object defined in metadata.
- There has been DWG discussion about proposing a new role for the
  `Dataset` object.
- Lifecycle and version management of metadata objects is not clearly
  defined.  This includes the use of timestamps.
- `Experiment` object is currently copied into the `ReadGroup` object.
  Given metadata becomes a chain of objects associated with the data,
  copying records seems less that ideal.
