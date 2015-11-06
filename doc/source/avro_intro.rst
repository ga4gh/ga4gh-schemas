.. _avro:

*******************
Apache Avro
*******************

Copied from the `Avro documentation <http://avro.apache.org/docs/1.7.7/>`_

Avro is a data serialization system. It deals with the how of sending large data files across the internet.

Avro relies on schemas. When Avro data is read, the schema used when writing it is always present.
This permits each datum to be written with no per-value overheads, making serialization both fast and small.
This also facilitates use with dynamic, scripting languages, since data, together with its schema, is fully self-describing.

When Avro data is stored in a file, its schema is stored with it, so that files may be processed later by any program.
If the program reading the data expects a different schema this can be easily resolved, since both schemas are present.

When Avro is used in RPC, the client and server exchange schemas in the connection handshake.
(This can be optimized so that, for most calls, no schemas are actually transmitted.)
Since both client and server both have the other's full schema, correspondence between same named fields, missing fields,
extra fields, etc. can all be easily resolved.

Avro schemas are defined with JSON. This facilitates implementation in languages that already have JSON libraries.

..note::
    This is verbatim from the documentation. However, GA4GH defines schemas in .avdl

To actually send the data, Apache Avro uses the ReST protocol, which uses HTTP.
<more about http>

