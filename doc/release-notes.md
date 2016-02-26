# Changes to `ga4gh/schemas` `master` branch since version `v0.5.1` (Oct 2, 2014)

## Pervasive changes

Renamed all protocols and records to remove the "`GA`" prefix from
their names.  (Hence `GASearchVariantSetsRequest` is now
`SearchVariantSetsRequest`, etc.)  
The exception is `GAException`, which is unchanged.

There is no longer one unitary namespace.  Objects now reside in
"`org.ga4gh.models`", methods in "`org.ga4gh.methods`".

Updated the version number to `0.6.0a1`.


## Changes visible to API clients

### Additions

`Dataset` is now utilized throughout the API.

#### New methods, HTTP endpoints:

* `getDataset` via GET `datasets/<id>`
* `searchDatasets` via POST `/datasets/search`
* `getReadGroupSet` via  GET `/readgroupsets/<id>`
* `getReadGroup` via GET `/readgroups/<id>`
* `getVariant` via GET `/variants/<id>`
* `getVariantSet` via GET `/variantsets/<id>`
* `getCallSet` via GET `/callsets/<id>`

#### New and modified entities:

* New record type `ExternalIdentifier` introduced.
* New record type `ReadStats` now optionally part of a returned `ReadGroup` or `ReadGroupSet` object.
* `Position` record type now specifies strand via new enum `Strand` (in place of `boolean reverseStrand`).

#### Field default values:

* `SearchReadsRequest.start` as passed into `/reads/search` is optional and no longer defaults to 0.
* Boolean fields in `ReadAlignment` as returned from `/reads/search` now default to `null` instead of `false`.

#### Field types:

* `SearchVariantSetsRequest` as passed into `/variantsets/search` now takes a single dataset ID, not an array.
* `SearchCallSetsRequest` as passed into `/callsets/search` now takes a single variant set ID, not an array.
* `SearchReferenceSetsRequest` as passed into `/referencesets/search` changed two parameters from arrays to
singletons:

    * `md5checksum`
    * `accession`

#### New fields:

* `SearchReferencesRequest` passed into `/references/search` now accepts a `referenceSetId` parameter.
* `SearchVariantsRequest` passed into `/variants/search` now takes a `variantSetId` parameter.
* `SearchReadsRequest` passed into `/reads/search` now includes `readGroupIds`.
* `SearchReadGroupSetsRequest` passed into `/readgroupsets/search` takes a `datasetId`.
* `ReferenceSet` returned from `/references/search` now includes a name.
* `VariantSet` returned from `/variants/search` adds name and reference set ID fields.
* `ReadGroup` returned from `/readgroups/<id>` adds `stats`.


## Changes internal to Schemas, documentation and organization

### Removed

* `src/main/resources/avro/beacon.avdl`
* Files designated "Work In Progress" ("`wip`"):
    * `src/main/resources/avro/wip/metadata.avdl`
    * `src/main/resources/avro/wip/metadatamethods.avdl`
    * `src/main/resources/avro/wip/variationReference.avdl`

### Changed

Moved `GAException` to `methods.avdl`.

## Documentation

Using Doxygen to generate HTML documentation from schema (`*.avdl`) files.

Clarifications:

* How the `SearchReadGroupSetsRequest.name` field is interpreted.
* The meaning of `SearchCallSetsRequest.name`.
* `Reference`, `ReferenceSet` docs.

Updated `CONTRIBUTING.md` to describe the latest contribution rules.

Moved `GeneratingDocumentation.md` to `doc/`.

`README.md` now includes information about the Metadata Task Team.

## Tests

Added tests to ensure Maven processes the schemas into a `jar` file
successfully, and that we can compile the schemas into Python.
