.. _introduction:

************
Introduction
************

The `Data Working Group <http://ga4gh.org/#/>`_ of the
`Global Alliance for Genomics and Health <http://genomicsandhealth.org/>`_
developed this
`web API <http://ga4gh.org/documentation/api/v0.5.1/ga4gh_api.html#/>`_
to facilitate access to and exchange of genomics data across remote sites. 

--------------------------
Why use this web API?
--------------------------

You can use this API to share genomics data without needing to copy files around or worry about details of file formats:

* Exchange genome annotations, DNA sequence reads, reference-based alignments, metadata, and variant calls
* Request alignments and variant calls for one genome, or a million
* Explore data by slicing alignments and variants by genomic range across one or multiple samples
* Interactively process entire cohorts

--------------------------
The GA4GH web API
--------------------------

This API was created to enable researchers to better access and exchange genomic data across remote sites. Instead of having to
download large BAM files or whole genome annotations, the API allows you to retrieve data about, for instance, single genes or genomic
regions.  The API is designed for a variety of uses, from interactive visualization to large-scale analysis.

For a full list of the GA4GH API goals, see :ref:`apigoals`

The API consists of a series of :ref:`apidefinition`, or schemas, that define datasets, metadata, read group sets, reads, variants, etc. 

The GA4GH web API schemas show developers how to connect data consumers ('clients') to data providers ('servers').
They define how the data is organized, and thereby give information on what can be requested.
The schemas are defined in Avro Interactive Data Language (extension .avdl), and 
can be used to create code in any programming language.

--------------------------
API design patterns
--------------------------
Web APIs use the protocols and conventions of the Web to connect consumers and providers of data, known as clients and servers.  This API uses these patterns:

* HTTP protocol
* ReST (Representational State Transfer) conventions
* Paging
* AVRO definition language
* JSON representation

For more details on web APIs, see `this wikipedia page <https://en.wikipedia.org/wiki/Web_API>`_  

HTTP protocol
.............
API clients use HTTP (`Hypertext Transfer Protocol <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_) for sending API queries and getting responses.
HTTP is the same protocol that web browsers use for requesting pages from web servers.

In a typical conversation, a client sends a GET request to a server to ask for a specific resource, such as a set of reads.
If the request contains appropriate identification and authorization information, the server responds with a copy of the requested information.

Many GA4GH API servers will also support HTTPS, a variant of HTTP that uses encryption to protect messages from eavesdropping and modification while in transit.

ReST (Representational State Transfer) conventions
..................................................
The GA4GH APIs follow `ReST conventions <https://en.wikipedia.org/wiki/Representational_state_transfer>`_ for web services on HTTP.  In particular:

* The API defines many different kinds of resources, some of which are collections of other kinds of resources.
* Each resource is identified by a unique URI.
* Clients can create resources and retrieve information about them by applying standard HTTP verbs like GET, PUT, POST, DELETE to appropriate URIs.
* GET is used to list collections and retrieve individual items. GET requests never have side effects.
* PUT is used to replace collections and items.  PUT requests are idempotent - repeating the same PUT request is equivalent to doing it just once.
* POST is used to modify collections.
* DELETE is used to remove collections and items.  DELETE requests are idempotent - repeating the same DELETE request is equivalent to doing it just once.

TODO examples of GA4GH resources and their use.

Paging
......

All GA4GH APIs implement a paging convention, so that the amount of information returned in a single response can be bounded. All
GA4GH APIs have paging support, even those that are very unlikely to return large amounts of information. This convention helps avoid breaking changes later:
paging often becomes necessary eventually, and adding paging in later would break clients that don't expect it.

TODO more details of paging convention and use.


Avro definition language
........................

:ref:`avro` is a data format definition language which can also be used to generate tools and libraries for working with the data format.
Here, data means both the request ('send me reads for gene X in sample Y') and the response (the set of reads).
Apache Avro only sends data in :ref:`json` or Binary Avro format, so requests and responses must be converted into one of those formats.

JSON representation
...................

`JSON <https://en.wikipedia.org/wiki/JSON>`_ is a commonly used language-independent notation for representing hierarchical data
structures. For more details on JSON, see :ref:`json`.

-----------------------
How to use Avro schemas
-----------------------

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

