# Schema Release `v0.6.0a9`

Changes to `ga4gh/schemas` `master` branch since version `0.6.0a8` (Oct 26, 2016)

* Fixed bugs:
   * Fixed typo in get: `/v0.6.0a8/variantannotationset/{variant_annotation_set_id}`
   * Fix to be able to handle VCFs with genotype == `./.`
* Upgrade to use protobuf release 3.1
* Introduced a pip installable schemas package called `ga4gh-schemas`. We have also 
   created pip installable packages for a support library called `ga4gh-common`
   and a client library module called `ga4gh-client`.
* Introduced a schemas package release to Maven Central. We will be posting regular
   ga4gh packages for each official schema release to Maven going forward.
* Changed the name of the biosample terms to track be consistent with the use
   of camel-case and the underscore character.
* Added a new schema visualization tool to create UML diagrams from the schemas.
   The new diagrams can be viewed on the Schemas page in the Read The Docs 
   documents.

# Schema Release `v0.6.0.a8` 

Changes to `ga4gh/schemas` `master` branch since version `0.6.0a7` (Aug 19, 2016)

* Introduced G2P API endpoints including the following:
  * POST `/phenotypeassociationsets/search`
  * POST `/phenotypes/search`
  * POST `/featurephenotypeassociations/search`
* Add biometadata to RNA quantifications
* Add protobuf based HTTP annotations

# Schema Release `v0.6.0.a7` 

Changes to `ga4gh/schemas` `master` branch since version `0.6.0a6` (Jul 25, 2016)

Introduced RNA API endpoints including the following:

* POST `/rnaquantificationsets/search`
* GET `/rnaquantificationsets/{id}`
* POST `/rnaquantifications/search`
* GET `/rnaquantifications/{id}`
* POST `/expressionlevels/search`
* GET `/expressionlevels/{id}`

# Schema Release `v0.6.0.a6` 

Changes to `ga4gh/schemas` `master` branch since version `0.6.0a5` (Jun 20, 2016)
NOTE: release notes have not been updated for several versions. 

## changes made in the most recent release

* Metadata section added
* Now support searching features by 'name' and 'gene_symbol' 


# Schema Release `v0.6.0.a5`

Changes to `ga4gh/schemas` `master` branch since version `v0.6.0a4` (Apr 7, 2016)

First Protocol Buffers (protobuf v3.0.0) version of the GA4GH API. 
Same set of features (messages, endpoints) as previous alpha release.

IMPORTANT: The switch from AVRO to protobuf in this pre-release will 
break compatibility with all client applications written against the 
previous AVRO schema version.


# Schema Release `v0.6.0.a4`

Changes to `ga4gh/schemas` `master` branch since version `v0.6.0a3` (Mar 1, 2016)

Introduced Sequence Annotations API record types (FeatureSet and Feature) 
and associated endpoints 
`POST featuresets/search`
`GET featuresets/<id>`
`POST features/search`
`GET features/<id>`


# Schema Release `v0.6.0.a3`

Changes to `ga4gh/schemas` `master` branch since version `v0.6.0a2` (Feb 24, 2016)

Changed properPlacement in Reads API to improperPlacement (defaults to 
False), corrected documentation on variation annotation and dateTime format.


# Schema Release `v0.6.0.a62

Changes to `ga4gh/schemas` `master` branch since version `v0.6.0a1` (Dec 15, 2015)

Added Variant Annotations draft API


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
