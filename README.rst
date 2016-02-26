.. figure:: http://genomicsandhealth.org/files/logo_ga.png
	    :alt: Image


Schemas for the Data Working Group
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

|Build Status| |Docs|

The `Global Alliance for Genomics and Health
<http://genomicsandhealth.org/>`__ is an international coalition,
formed to enable the sharing of genomic and clinical data.

The `Data Working
Group <http://genomicsandhealth.org/working-groups/data-working-group>`__
concentrates on data representation, storage, and analysis, including
working with platform development partners and industry leaders to
develop standards that will facilitate interoperability.

Each area of genomics and health has a dedicated team working to define
those standards.

Reads Task Team
@@@@@@@@@@@@@@@

The `Reads Task
Team <https://groups.google.com/forum/#!forum/dwgreadtaskteam>`__ is
focused on standards for accessing genomic read data -- collections of
primary data collected from sequencing machines.

The team will deliver:

#. Data model. An abstract, mathematically complete and precise model of
   the data that is manipulated by the API. See the `Avro
   directory <src/main/resources/avro>`__ for our in-progress work on
   defining v0.5 of the data model.

#. API Specification. A human-readable document introducing and
   defining the API, accompanied by a formal specification. See the
   `documentation page <http://ga4gh.org/#/apis/reads/v0.1>`__ for the
   published v0.1 API.

#. Reference Implementation. Open source working code demonstrating
   the API, ideally which can underpin real world working
   implementations.


Reference Variation Task Team
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The Reference Variation Task Team is focused on standards for storing
and accessing reference genome and variant data -- the results of
analysis of primary data collected from sequencing machines.

File Formats Task Team
@@@@@@@@@@@@@@@@@@@@@@

One small but essential part of this effort is the definition,
standardisation, and improvement of basic file formats for sequence and
variation data, and for associated infrastructure such as index formats.

These format specifications can be found in the `samtools/hts-specs
repository <https://github.com/samtools/hts-specs>`__.

Metadata Task Team
@@@@@@@@@@@@@@@@@@

The Metadata Task Team (MTT) concerns itself with data structures,
attributes and values used to describe *everything but the sequence*.
This includes metadata for individuals, samples, analyses,
instrumentation a well as ontology representations for metadata.
Naturally, the group interacts heavily with members of most other task
teams and working groups.

`MTT Wiki <https://github.com/ga4gh/metadata-team/wiki>`__

How to build
@@@@@@@@@@@@

See `INSTALL.rst <INSTALL.rst>`__ for instructions on how to build the
schemas and their documentation.

How to contribute changes
@@@@@@@@@@@@@@@@@@@@@@@@@

See the `CONTRIBUTING.rst <CONTRIBUTING.rst>`__ document.

License
@@@@@@@

See the `LICENSE <LICENSE>`__


.. |Build Status| image:: https://travis-ci.org/ga4gh/schemas.svg?branch=master
			  :target: https://travis-ci.org/ga4gh/schemas
.. |Docs| image:: https://readthedocs.org/projects/ga4gh-schemas/badge/
		  :target: http://ga4gh-schemas.readthedocs.org
