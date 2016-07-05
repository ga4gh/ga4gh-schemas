.. _proto:

***********************
Google Protocol Buffers
***********************

Apache Avro is a data serialization ecosystem, comparable to Google's Protocol Buffers.

-------------------------------------------------------
What does the GA4GH web API take from Protocol Buffers?
-------------------------------------------------------

The GA4GH web API uses the Google Protocol Buffers language and JSON serialization libraries.

The GA4GH web API presents a simple HTTP(S) and JSON interface to clients. It does **not** use Protocol Buffers's binary serialization format.

-------------------------------------------------------
How does the GA4GH web API use Protocol Buffer schemas?
-------------------------------------------------------

GA4GH web API objects, including both the data objects actually exchanged and the control messages requesting and returning those objects, are defined in Protocol Buffers.

The full documentation for the Protocol buffers language can be found `here <https://developers.google.com/protocol-buffers/docs/proto3>`_.

------------------------------------------------
How does the GA4GH Web API use Protocol Buffers?
------------------------------------------------

The GA4GH web API schemas are broken up into multiple proto files, which reference each other. Each file defines a number of message types, grouped into a "protocol" that defines a facet of the API. Mostly, the files come in pairs: a normal proto file defining the types representing actual data, and a "methods" proto file defining the control messages to be sent back and forth to query and exchange the representational types, and the URLs associated with various operations.

Each type has a leading comment documenting its purpose, and each field in the type has a description. These are included in the automatically generated API documentation.

Here is an example of a proto definition from , in this case defining a genomic `Position` type which is used across the API::

  message Position {
    // The name of the `Reference` on which the `Position` is located.
    string reference_name = 1;

    // The 0-based offset from the start of the forward strand for that
    // `Reference`. Genomic positions are non-negative integers less than
    // `Reference` length.
    int64 position = 2;

    // Strand the position is associated with.
    Strand strand = 3;
  }
  
This is a "message", which contains three fields. All of the fields are required to be filled in, and all of the fields can only hold objects of a particular single type. The last field holds a `Strand` object, which is defined elsewhere in the file.

.. todo::
   * How much of the Protocol Buffers tutorial do we want in here?
   * Document/show an example for methods (request and response pairing pattern)
   * Talk about how we manually specify that some things land in URLs

