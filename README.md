![Image](http://genomicsandhealth.org/files/logo_ga.png)


# Schemas for the Data Working Group


The [Global Alliance for Genomics and Health][ga4gh] is an international
coalition, formed to enable the sharing of genomic and clinical data.

The [Data Working
Group](http://genomicsandhealth.org/our-work/working-groups/data-working-group)
concentrates on data representation, storage, and analysis, including working
with platform development partners and industry leaders to develop standards
that will facilitate interoperability.

Each area of genomics and health has a dedicated team working to define those
standards.


## Reads Task Team

The [Reads Task Team](https://groups.google.com/forum/#!forum/dwgreadtaskteam)
is focused on standards for accessing genomic read data -- collections of
primary data collected from sequencing machines.

The team will deliver:

  1. Data model. An abstract, mathematically complete and precise model of the
     data that is manipulated by the API. See the [proto
     directory](src/main/resources/proto) for our in-progress work on defining
     the data model. 
  2. API Specification. A human-readable document introducing and defining the
     API, accompanied by a formal specification. See the [documentation
     page](http://ga4gh.org/#/apis/reads/v0.1) for the published v0.1
     API.
  3. Reference Implementation. Open source working code demonstrating the API,
     ideally which can underpin real world working implementations.

## Reference Variation Task Team

The Reference Variation Task Team is focused on standards for storing and
accessing reference genome and variant data -- the results of analysis of
primary data collected from sequencing machines.

## File Formats Task Team

One small but essential part of this effort is the definition,
standardisation, and improvement of basic file formats for sequence and
variation data, and for associated infrastructure such as index formats.

These format specifications can be found in the
[samtools/hts-specs repository][hts-specs].

[ga4gh]:      http://genomicsandhealth.org/
[hts-specs]:  https://github.com/samtools/hts-specs

## Metadata Task Team

The Metadata Task Team (MTT) concerns itself with data structures, attributes 
and values used to describe *everything but the sequence*.  This includes 
metadata for individuals, samples, analyses, instrumentation a well as 
ontology representations for metadata. Naturally, the group interacts 
heavily with members of most other task teams and working groups.

[MTT Wiki](https://github.com/ga4gh/metadata-team/wiki)


## Build Status

[![Build Status](https://travis-ci.org/ga4gh/schemas.svg?branch=master)](https://travis-ci.org/ga4gh/schemas)

## How to contribute changes

See the [CONTRIBUTING.md](CONTRIBUTING.md) documement.

## License

See the [LICENSE](LICENSE)
