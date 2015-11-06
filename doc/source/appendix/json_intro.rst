.. _json:

**********************
The JSON Format
**********************

JSON, or JavaScript Object Notation, is officially defined `here <http://json.org/example>`_. It is the standard data interchange format for web APIs.

The GA4GH Web API uses a JSON wire protocol, exchanging JSON representations of the objects defined in its AVDL schemas. More information on the AVDL schemas is available in :ref:`avro`; basically, the AVDL type definitions say what attributes any given JSON object ought to have, and what ought to be stored in each of them.

-----------------------
GA4GH JSON Serialization
-----------------------

The GA4GH web APIs use Avro IDL to define their schemas, and use the associated Avro JSON serialization libraries. Since the schemas use a restricted subset of AVDL types (see `A note on unions`_ below), the serialized JSON format is fairly standard. This means that standard non-Avro JSON serialization and deserialization libraries (like, for example, the Python ``json`` module) can be used to serialize and deserialize GA4GH JSON messages in an idiomatic way.

---------------------
Serialization example
---------------------

For example, here is the schema definition for Variants (with comments removed)::

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

Here is a serialized variant in JSON. It's a bit of an edge case in some respects::

  {
      "id": "gv79384-3200-11",
      "variantSetId": "vs-44-1",
      "names": [
          "rs110",
          "Victoria"
      ],
      "created": 1446842841,
      "updated": null,
      "start": 1000,
      "end": 1001,
      "referenceBases": "A",
      "alternateBases": [
          "C",
          "CTATCTT"
      ],
      "info": {
          "variantfacts": ["is_interesting", "is_long"],
          "numberOfPapers": ["11"]
      },
  }

Things to notice:
 * A serialized record contains no explicit information about its type.
 * Arrays are serialized as JSON arrays.
 * Maps are serialized as JSON objects.
 * Records are also serialized as JSON objects.
 * Enums (not shown here) are serialized as JSON strings.
 * Nulls are serialized as JSON nulls.
 * Fields with default values may be omitted (see the lack of an ``updated`` or ``calls``) as a way of serializing their default values.
 * Unions of ``null`` and a non-``null`` type are serialized as either ``null`` or the serialized non-null value. No other kinds of unions are present or permitted.

-----------------------
A note on unions
-----------------------

As noted above, a field with union type serialized in GA4GH JSON looks no different from a field of any other type: you just put the field name and its recursively serialized value. In order for the Avro JSON libraries to support this, it is necessary that AVDL ``union`` types union together only ``null`` and a single non-``null`` type. If there were two or more non-``null`` types, the Avro libraries would need to include additional type information to say which to use when deserializing. Since we prohibit those unions, however, API clients and alternative server implementations never need to worry about this additional type information or its syntax. They can just handle "normal" JSON.

.. todo::
   * add example of Python decoder output
   * create a python class, if necessary
   
-----------------------
Wire protocol example
-----------------------

This is from the `ga4gh server example`_.

.. _ga4gh server example: http://ga4gh-reference-implementation.readthedocs.org/en/stable/demo.html#demo

To get information from the readgroupsets on a server, create a JSON format request::

    {
      "datasetIds":[], 
      "name":null
    }

.. note::
    What is this actually asking?

To send this to the server, we need to create a HTTP request which tells the server what type of
data to expect (JSON format, in this case)
In our test case, we have a server running at \http://localhost:8000

Since we want to query the readgroupsets, we'll have to make that part of the URL

.. note::
     * How do we know it's v0.5.1?
     * where is the readgroupsets/search part documented or defined?

To create a command line request, we can use `cURL <http://curl.haxx.se/>`_::

    curl --data '{"datasetIds":[], "name":null}' --header 'Content-Type: application/json' http://localhost:8000/v0.5.1/readgroupsets/search

The server returns::

    {
    "nextPageToken": null,
    "readGroupSets": [{
    "readGroups": [{
    "info": {}, 
    "updated": 1432287597662, 
    "predictedInsertSize": null, 
    "description": null, 
    "created": 1432287597662, 
    "programs": [], 
    "sampleId": null, 
    "experiment": null,
    "referenceSetId": null,
    "id":
    "low-coverage:HG00533.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522",
    "datasetId": null,
    "name":
    "low-coverage:HG00533.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522"
    }, 
    {   "info": {},
    "updated": 1432287793946,
    "predictedInsertSize": null,
    "description": null,
    "created": 1432287793946,
    "programs": [],
    "sampleId": null,
    "experiment": null,
    "referenceSetId": null,
    "id":
    "low-coverage:HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522",
    "datasetId": null,
    "name":
    "low-coverage:HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522"
    }, 
    {    "info": {},
    "updated": 1432287793946,
    "predictedInsertSize": null,
    "description": null,
    "created": 1432287793946,
    "programs": [],
    "sampleId": null,
    "experiment": null,
    "referenceSetId": null,
    "id":
    "low-coverage:HG00534.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522",
    "datasetId": null,
    "name":
    "low-coverage:HG00534.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522"
    }],
    "id":
    "low-coverage",
    "datasetId": null,
    "name": null
    }
    ]
    }



