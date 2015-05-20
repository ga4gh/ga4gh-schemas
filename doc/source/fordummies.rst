.. _fordummies:

*****************
GA4GH for dummies
*****************

-------------
The cool part
-------------
This API allows researchers to query genomics data such as short reads or genome annotations by (for example) genomic region, 
without having to download complete BAM or GFF3 files.

------------
Useful links
------------
The `Data Working Group <http://ga4gh.org/#/>`_ of the
`Global Alliance for Genomics and Health <http://genomicsandhealth.org/>`_

---
API
---
An Application Programming Interface (API) is a set of routines, protocols, and tools for building software applications.
An API expresses a software component in terms of its operations, inputs, outputs, and underlying types.

Email is dependent on an API: it doesn't matter what programming language is used to read or write the email client, as long as
it understands the protocols for talking to an email server.

Like email protocols, the GA4GH API defines ways to share data across the internet. The data model is conceptual, meaning that no data is actually
shared or presented by the project. Instead the working group defines schemas for requests and responses, allowing other
developers to create code in their language of choice.

ReST HTTP protocol: stateless, client-server communications protocol, which does NOT keep info on the server (which for instance NCBI does
when queries are built).

The underlying system is Apache Avro, which does the actual data exchange. It can transfer anything, such as JSON (text) or
a binary data format. It takes care of serialization so that large chunks of memory can be transferred.

.. NOTE::
    Not quite clear on what's Avro and what's GA4GH API in the example below.

-----------
Apache Avro
-----------
`Info on Apache Avro <http://avro.apache.org/>`_ 

So the way it works is the client creates a request using the Avro encoder in JSON, Binary Avro, or ProtoBuf (a Google format) - currently only JSON
is supported - and sends that in a HTTP to the server. HTTP is basically a header that describes what kind of data is in the request, and also what it
will accept as response, and then the main body contains the data (JSON, Binary Avro, etc).
The server receives this request and decodes it using the Avro decoder. It retrieves the necessary data, Avro encodes it in the requested format,
and sends it back using HTTP. The client then decodes it.

A schema definition looks like::

  record VariantSetMetadata {
	string key;
  	string value;
  	string id;
  	string type;
  	metadata.
  	map<array<string>> info = {};
  }

So this defines the variable names and types. These can then be used in e.g. a Python library to create a dict or an object.

The idea is that these libraries are really all the user needs to deal with, though the documentation needs to describe it
in more generic terms, because libraries can be made for any programming language.

.. ATTENTION::
    this is also a documentation challenge, because there will be two types of users: developers, who need the nitty gritty,
    and bioinfo people who just want to get the data out.

Currently only the Variants and Reads are fleshed out properly and available on the reference server, but that's a good start.
The Reads are BAM based and so the tags reflect BAM info.

The variants are VCF-like. The 
`Variant Call Format <http://www.1000genomes.org/wiki/analysis/variant-call-format/bcf-binary-vcf-version-2>`_
was devised for the 1000 genomes project

It is quite BAM-like in that it has a header with general info, some of which is mandatory, and a tab separated body with tags

