.. _json:

**********************
The JSON Format
**********************

JSON, or JavaScript Object Notation, is officially defined `here <http://json.org/example>`_. It is the standard data interchange format for web APIs.

The GA4GH Web API uses a JSON wire protocol, exchanging JSON representations of the objects defined in its Protocol Buffers schemas. More information on the schemas is available in :ref:`proto`; basically, the Protocol Buffers type definitions say what attributes any given JSON object ought to have, and what ought to be stored in each of them.

------------------------
GA4GH JSON Serialization
------------------------

The GA4GH web APIs use Protocol Buffers IDL to define their schemas, and use the associated Google Protocol Buffers JSON serialization libraries. Notice that the Protocol Buffers IDL uses snake case, while the on-the-wire protocol is in camel case.

---------------------
Serialization example
---------------------

For example, here is the schema definition for Variants (with comments removed)::

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
 * "repeated" types are serialized as JSON arrays.
 * Maps are serialized as JSON objects.
 * Messages are also serialized as JSON objects.
 * Enums (not shown here) are serialized as JSON strings.

