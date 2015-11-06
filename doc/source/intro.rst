.. _introduction:

************
Introduction
************

The `Data Working Group <http://ga4gh.org/#/>`_ of the
`Global Alliance for Genomics and Health <http://genomicsandhealth.org/>`_
developed this
`web API <http://ga4gh.org/#/api/v0.5.1>`_
to facilitate access to and exchange of genomics data across remote sites. 

--------------------------
Why use this web API?
--------------------------

This API is specifically designed to allow sharing of genomics data without having to exchange complete experiments.
With this API, you can

* Exchange genome annotations, DNA sequence reads, reference-based alignments, metadata, and variant calls
* Request alignments and variant calls for one genome or a million.
* Explore data by slicing alignments and variants by genomic range across one or multiple samples
* Interactively process entire cohorts

--------------------------
If you need background
--------------------------
For more details on web APIs, see `this wikipedia page <https://en.wikipedia.org/wiki/Web_API>`_  

ReST protocols for data transfer are described `here <https://en.wikipedia.org/wiki/Representational_state_transfer>`_

--------------------------
The GA4GH web API
--------------------------
This API was created to enable researchers to better access and exchange genomic data across remote sites. Instead of downloading complete BAM files or
whole genome annotations, the API allows retrieval of information on, for instance, single genes or genomic regions.

For a full list of the GA4GH API goals, see :ref:`apigoals`

The API consists of a series of :ref:`apidefinition`, or schemas, that define datasets, metadata, read group sets, reads, variants, etc. 

The schemas are written in Avro Interactive Data Language (extension .avdl). 

:ref:`avro` is a data serialization system, it defines how data gets transported across the internet.
Here, data means both the request ('send me RNASeq for gene X in sample Y') and the response (the BAM file). Apache Avro only sends data in
:ref:`json` or Binary Avro format, so requests and responses must be converted into one of those formats.

For more details on AVRO, see :ref:`avro`

For more details on JSON, see :ref:`json`


-----------------------
How to use Avro schemas
-----------------------
The GA4GH web API schemas show developers how to make servers and clients interact. 
They define how the data is organized, and thereby give information on what can be requested.
The schemas can be used to create code in any programming language.


Here's the schema definition for Variants (with comments removed)::

  record Variant {
    string id;
    string variantSetId;
    array<string> names = [];
    union { null, long } created = null;
    union { null, long } updated = null;
    string referenceName;
    long start;
    long end;
    string referenceBases;
    array<string> alternateBases = [];
    map<array<string>> info = {};
    array<Call> calls = [];
  }

This means that when you request a single variant by, for example, its ID, you get back a JSON file
with the information listed above. The JSON can be read using the JSON decoder from the
Python standard library, which creates (an object?) in which the JSON array becomes Python's list, 
and any NULL values become None.

.. todo::
   * add example of decoder output
   * create a python class, if necessary

Click for more :ref:`samplecode`.

