.. _introduction:

Introduction
!!!!!!!!!!!!

The `Data Working Group <http://ga4gh.org/#/>`_ of the `Global
Alliance for Genomics and Health <http://genomicsandhealth.org/>`_
developed this `web API <http://ga4gh.org/#/api/v0.5.1>`_ to
facilitate access to and exchange of genomics data across remote
sites.


Why use this web API?
@@@@@@@@@@@@@@@@@@@@@

This API is specifically designed to allow sharing of genomics data in a
standardized manner and without having to exchange complete experiments.
With this API, you can

* Exchange genome annotations, DNA sequence reads, reference-based
  alignments, metadata, and variant calls
* Request alignments and variant calls for one genome or a million.
* Explore data by slicing alignments and variants by genomic location
  or other feature across one or multiple genomes.
* Interactively process entire cohorts


If you need background
@@@@@@@@@@@@@@@@@@@@@@
For more details on web APIs, see `this wikipedia page <https://en.wikipedia.org/wiki/Web_API>`_.
ReST protocols for data transfer are described `here <https://en.wikipedia.org/wiki/Representational_state_transfer>`_.
Wikipedia also has good overviews of `bioinformatics <https://en.wikipedia.org/wiki/Bioinformatics>`_
and `DNA sequencing <https://en.wikipedia.org/wiki/DNA_sequencing>`_


The GA4GH web API
@@@@@@@@@@@@@@@@@

This API was created to enable researchers to better access and
exchange genomic data across remote sites. For example, instead of downloading
complete BAM files or whole genome annotations, the API allows
retrieval of information on, for instance, single genes or genomic
regions.

For a full list of the GA4GH API goals, see :ref:`apigoals`


Schemas and formats
@@@@@@@@@@@@@@@@@@@

The API consists of a series of :ref:`schemas` that
define the types of things that API clients and servers exchange:
requests for data, server responses, error messages, and objects
actually representing pieces of genomics data.

The schemas are written in Protocol Buffers Interface Description
Language (extension .proto). For more details on Protocol Buffers
and how it is used in the GA4GH APIs, see :ref:`proto`.

Here is an example schema definition for a Variant (with comments
removed)::

  message Variant {
    string id = 1;
    string variant_set_id = 2;
    repeated string names = 3;
    int64 created = 4;
    int64 updated = 5;
    string reference_name = 6;
    int64 start = 7;
    int64 end = 8;
    string reference_bases = 9;
    repeated string alternate_bases = 10;
    map<string, google.protobuf.ListValue> info = 11;
    repeated Call calls = 12;
  }

On the wire, the GA4GH web API takes the form of a client and a server
exchanging JSON-serialized objects over HTTP or HTTPS. For more
details on JSON, including how the GA4GH web API serializes and
deserializes Protocol Buffers objects in JSON, see :ref:`json`.
