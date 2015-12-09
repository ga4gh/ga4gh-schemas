# Changes to `ga4gh/schemas` `master` branch since version `v0.5.1` (Oct 2, 2014)

### Pervasive changes

Renamed all protocols and records to remove the "`GA`" prefix from
their names.  (Hence `GASearchVariantSetsRequest` is now
`SearchVariantSetsRequest`, etc.)  The exception is `GAException`,
which is unchanged.

There is no longer one unitary namespace.  Objects now reside in
"`org.ga4gh.models`", methods in "`org.ga4gh.methods`".

Updated the version number to `0.6.0-SNAPSHOT`.

### Added

Datasets are now used throughout the API.

#### Methods:

* `getDataset`
* `searchDatasets`
* `getReadGroupSet`
* `getReadGroup`
* `getVariant`
* `getVariantSet`
* `getCallSet`

#### Records:

* `ExternalIdentifier`
* `Experiment`
* `Dataset`
* `ReadStats`
* `Fragment` _(apparently unused)_

#### Enum:

* `Strand`

### Removed

* `src/main/resources/avro/beacon.avdl`
* Files designated "Work In Progress" ("`wip`"):
    * `src/main/resources/avro/wip/metadata.avdl`
    * `src/main/resources/avro/wip/metadatamethods.avdl`
    * `src/main/resources/avro/wip/variationReference.avdl`

### Changed

Moved `GAException` to `methods.avdl`.

#### Field default values:

* `SearchReadsRequest.start` is optional and no longer defaults to 0.
* Boolean fields in `ReadAlignment` now default to `null` instead of `false`.

#### Field types:

* `SearchVariantSetsRequest` now takes a single dataset ID, not an array.
* `SearchCallSetsRequest` now takes a single variant set ID, not an array.
* `SearchReferenceSetsRequest` changed two parameters from arrays to
singletons:

    * `md5checksum`
    * `accession`

#### New fields:

* `SearchReferencesRequest` now accepts a `referenceSetId` parameter.
* `SearchVariantsRequest` now takes a `variantSetId` parameter.
* `SearchReadsRequest` now includes `readGroupIds`.
* `SearchReadGroupSetsRequest` takes a `datasetId`.
* `ReferenceSet` now includes a name.
* `VariantSet` adds name and reference set ID fields.
* `ReadGroup` adds `stats`.

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
