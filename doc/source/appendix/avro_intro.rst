.. _avro:

*******************
Apache Avro
*******************

Apache Avro is a data serialization ecosystem, comparable to Google's Protocol Buffers.

-------------------
What does the GA4GH web API take from Avro?
-------------------

The GA4GH web API uses the Avro IDL (aka AVDL) language and JSON serialization labraries.

The GA4GH web API presents a simple HTTP(S) and JSON interface to clients. It does **not** use Avro's binary serialization format, or Avro's built-in client/server networking and RPC features.

------------------
How does the GA4GH web API use Avro schemas?
------------------

GA4GH web API objects, including both the data objects actually exchanged and the control messages requesting and returning those objects, are defined in the Avro IDL language, AVDL.

The `full documentation for the AVDL language is abvailable here <https://avro.apache.org/docs/1.7.6/idl.html>`_. Bear in mind that the Avro IDL comes with an entire ecosystem; the GA4GH web APIs do not use most of it.

------------------
How does the GA4GH Web API use AVDL?
------------------

The GA4GH web API schemas are broken up into multiple AVDL files, which reference each other. Each file defines a number of types (mostly Avro Records, with a smattering of Avro Enums), grouped into a "protocol" (which is somewhat of a misnomer) of types defining a facet of the API. Mostly, the files come in pairs: a normal AVDL file defining the types representing actual data, and a "methods" AVDL file defining the control messages to be sent back and forth to query and exchange the representational types, and the URLs associated with various operations.

Each type has a leading comment documenting its purpose, and each field in the type has a description. These are included in the automatically generated API documentation.

Here is an example of an AVDL definition from, in this case defining a genomic `Position` type which is used across the API::

  /**
  A `Position` is an unoriented base in some `Reference`. A `Position` is
  represented by a `Reference` name, and a base number on that `Reference`
  (0-based).
  */
  record Position {
    /**
    The name of the `Reference` on which the `Position` is located.
    */
    string referenceName;

    /**
    The 0-based offset from the start of the forward strand for that `Reference`.
    Genomic positions are non-negative integers less than `Reference` length.
    */
    long position;

    /**
    Strand the position is associated with.
    */
    Strand strand;
  }
  
This is a "record", which contains three fields. All of the fields are required to be filled in, and all of the fields can only hold objects of a particular single type. (In cases where this is not desired, see the AVDL documentation on unions). The last field holds a `Strand` object, which is defined elsewhere in the file.

~~~~~~~~~~~~~~~~~~
A note on unions and optional fields
~~~~~~~~~~~~~~~~~~

Any field which is optional should be defined as a ``union<null, ActualType>``, and given a default value of ``null``. Note that ``null`` should always be first in the union, since it is the type of the default value.

The Avro JSON libraries serialize union types strangely, so the GA4GH API schemas have been specifically designed never to include union types that would trigger this behavior. The upshot of this is that the **only** legal union type is ``union<null, ActualType>``. Unions with multiple non-``null`` types are not allowed.

.. todo::
   * How much of the AVDL tutorial do we want in here?
   * Document/show an example for methods (request and response pairing pattern)
   * Talk about how we manually specify that some things land in URLs

