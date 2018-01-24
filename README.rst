.. figure:: http://genomicsandhealth.org/files/logo_ga.png
	    :alt: Image


Schemas for the Data Working Group
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

|Build Status| |Docs| |PyPi Release|

The `Global Alliance for Genomics and Health
<http://genomicsandhealth.org/>`__ is an international coalition,
formed to enable the sharing of genomic and clinical data.

REPOSITORY RETIREMENT NOTICE
@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The Genomics API was intended to act as a suite of integrated APIs each targeting a different aspect of exchanging genomic information between data providers and consumers. The Genomics API, together with the Reference Server and Compatibility test suite, was retired on January 24, 2018 and several of the sub-APIs are now being pursued under the auspices of new GA4GH Work Streams. We would like to thank those of you who have worked on this and look forward to ongoing contributions in the GA4GH Work Streams. You may still fork this repository if you wish to pursue developments. You may read the meeting minutes of the GA4GH Engineering Committee to learn more about the decision to retire the API. For additional questions or to get involved with ongoing technical work at GA4GH, please see the website at `Global Alliance for Genomics and Health
<http://ga4gh.org/>`__

Previous Readme Information continues below

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
   the data that is manipulated by the API. See the `Proto
   directory <src/main/proto>`__ for our in-progress work on
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

Variant Annotation Task Team
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The Variant Annotation Task Team is focused on developing standards for reporting
variant annotation including results formats, ontologies and vocabularies for
different classes of annotation so reporting is consistent and in a manner that
facilitates benchmarking and evaluation.

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

The relevant place for finding out about accepted metadata formats is the `*metadata-integration branch* <https://github.com/ga4gh/ga4gh-schemas/tree/metadata-integration>`__


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


.. |Build Status| image:: https://travis-ci.org/ga4gh/ga4gh-schemas.svg?branch=master
			  :target: https://travis-ci.org/ga4gh/ga4gh-schemas
.. |Docs| image:: https://readthedocs.org/projects/ga4gh-schemas/badge/
		  :target: http://ga4gh-schemas.readthedocs.org
.. |PyPi Release| image:: https://img.shields.io/pypi/v/ga4gh-schemas.svg
			  :target: https://pypi.python.org/pypi/ga4gh-schemas/
