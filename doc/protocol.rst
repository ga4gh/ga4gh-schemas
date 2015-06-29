GA4GH Wire Protocol Specification
=================================

* OFFSET and LIMIT

Version 0.2 [draft]

This document defines the GA4GH data exchange API Internet protocol.
It provides a restartable, streaming protocol with both ASCII and binary
encodings.  It is designed to efficiently send a stream of small
messages.

The streaming protocol replaces the current GA4GH paging protocol.

This document is intended to be normative. The protocol should
be completely implementable based on this document and
referenced standards. Any undefined behavior or ambiguities
discovered during any implementation must result in an update of
this specification.

Three-layer protocol
--------------------

This protocol is defined in three layers to separate concerns
and allow for evolution of the protocol to meet changing
requirements.

The three layers are:

- GA4GH object layer - Data objects defined by the GA4GH
  schemas, such as ``VariantSet``, ``Variant``, ``Call``,
  etc. They are agnostic to the transport mechanism.
- Messaging layer - Responsible for managing the flow of data
  between GA4GH compliant servers and clients. GA4GH objects
  are encoded in either ProtBuf V3 binary or ProtBuf V3 JSON
  format in a ``dataObject`` message. Other messages handle
  error recovery and other miscellaneous information required
  to establish efficient communication between the client and
  the server.
- HTTP 1.1 Internet protocol layer - HTTP 1.1 chunked encoding
  is used to robustly transfer a stream of objects without
  requiring the buffering of the entire request or response.
  Message objects are encoded in either ProtBuf V3 binary or
  ProtBuf V3 JSON format in the HTTP body chunks. This results
  in two levels of encoding for the GA4GH data objects.

Internet protocol
-----------------

GA4GH clients and servers communicate via streaming HTTP/HTTPS
using chunked transfer encoding ([rfc7230 - Hypertext Transfer
Protocol (HTTP/1.1): Message Syntax and Routing]
(http://tools.ietf.org/html/rfc7230)).  Data in the stream
consists of variable length message encode in one of the formats
defined in this document. The encoding is determined using HTTP
content-type negotiation ([rfc7231 -Hypertext Transfer Protocol
(HTTP/1.1): Semantics and Content]
(http://tools.ietf.org/html/rfc7231)).  A request maybe send
using either either a single HTTP 1.0 message with content
length or using HTTP 1.1 chunked transfer encoding.  Responses
must be sent using chunked transfer encoding.

The HTTP 1.1 chunked transfer encoding error report model is
used to indicate failed transfers. A connection that is closed
without receiving a trailer chunk must be treated as an
error. When a trailer chunk is received, it must be interrogated
to see if it contains a ``Status`` header that indicates an
error.

MIME type is in the form
``application/ga4gh.v${apiversion}+${encoding}``. Where
``${encoding}`` is the encoding format described below. The
``${apiversion}`` is the dot-separate hierarchal API version of
the GA4GH API. For requests, the ``Accepts`` header is used to
specify the desired encoding and API version. The API version
hierarchy requested can be as specific as required, with omitted
minor versions resulting in the newest version available on the
server matching. Thus, a version of ``1.5`` can be satisfied
with version such as ``1.5``, or ``1.5.3``, etc. The individual
dot versions are compared as integers.  The response
``Content-Type`` contains the exact version of the API that was
return.

Messaging
---------

Messages are used to implement the streaming protocol. A message
is not a GA4GH data object, it is a transfer facility with a
predefined set of messages.  One type of message is used to send
GA4GH query and response data. In response to a query, a stream
of messages is sent as a single HTTP chunk transfer encoded
response. The protocol allows for a stream of mixed GA4GH object
types.

Both request and response use the same set of messages.

Transfer resume
~~~~~~~~~~~~~~~

The GA4GH streaming protocol supports resume of a stream by
sending periodic checkpoint messages that can be used to restart
a transfer at that point. See the Rationale section for
discussion of this design decision. To resume from a failure, a
``resume`` message, along with a checkpoint object is sent to
the server.

The frequency of checkpoint messages can be requested by the
client using the ``X-GA4GH-CHECKPOINT-FREQUENCY`` request
header. This is an advisory request; the exact frequency of
checkpoints is up to the discretion of the server. The value is
the approximate number of bytes to stream before sending a
checkpoint message.

The client tunes the checkpoint frequency based on network speed
and reliability. Since it's expected that that checkpoint will
on be used for larger transfers over wide area networks, the
default value is disabled (0), There is no requirement that
clients implement checkpoint resume.

The same facility will be used for implementing checkpoints
originating at from the client once a write API has been defined
by GA4GH.

Message types
~~~~~~~~~~~~~

The following message types are defined:

- ``dataType typeKey typeName`` - Defines a key used to identify
   the types of data objects that follow in a stream. This
   supports mixed GA4GH data types in given stream. A message
   for a given type is only sent once, before any data objects
   of that type are sent. They may be sent at any point in the
   stream, the only requirement is that a ``dataType`` message
   must precede the first message of the type. If a stream is
   resumed from a checkpoint, ``dataType`` objects will be
   resent before objects of a given type are sent.  The\
   ``typeKey`` parameter is an integer that is included in the
   ``dataObject`` messages. The value is server-instance
   dependent and its scope is only the current data stream. If a
   request is resumed, it should not be assume that the
   ``typeKey`` values will be the same as the original stream.
   The ``typeName`` parameter is a full qualified record name
   ``package.message`` that identifies the type. All GA4GH
   objects will match ``org.ga4gh.*``.  Non-GA4GH data types may
   also use this protocol, however they must not be under the
   ``org.ga4gh`` package.

- ``dataObject typeKey data`` - Used to send a data object. The
  ``typeKey`` parameter is used to find the matching
  ``dataType`` message. The ``data`` parameter is the data
  object.

- ``checkpoint memento`` - Specify a checkpoint in the data
  stream.  The ``memento`` is an opaque, server-dependent
  object. It should be returned as-is when resuming a
  stream. The memento object should contain all state necessary
  to resume the query provided the data is still available on
  the server (ReSTful).

- ``resume memento`` - Resume a transfer at the specified
   checkpoint, as define by the ``memento`` object, in data
   stream. The next data object that was or would have been
   received after the corresponding ``checkpoint`` message will
   be the next data object received on the stream. It will be
   preceded by the required ``dataType`` message. The same
   checkpoint may resumed multiple times, as would be required
   if there was a failure before another ``checkpoint`` messages
   is received in the stream.

Message Encoding
----------------

Messages are encoded using `Protocol Buffers V3
<https://developers.google.com/protocol-buffers/docs/proto3>`__.
Use of protocol buffers to encode a message is independent of
the encoding of the GA4GH object. That is, there are two levels
of Protocol Buffers encoding, the object itself, which are send
in GA4GH messages, also encoded using Protocol Buffers.

Messages are encoded as ``oneof`` alternatives in a ``Message``
object. The Protocol
Buffers declarations for the GA4GA messages are:

::

        syntax = "proto3";

        package org.ga4gh.protocol;

        message DataType {
          int32 type_key = 1;
          string type_name = 2;
        }

        message DataObject {
          int32 type_key = 1;
          bytes data = 2;
        }

        message Checkpoint {
          bytes memento = 1;
        }

        message Restart {
          bytes memento = 1;
        }

        message Message {
          oneof message_type {
            DataType data_type = 1;
            DataObject data_object = 2;
            Checkpoint checkpoint = 3;
            Restart restart = 4;
          }
        }

JSON ASCII message encoding
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Messages are encoding as UTF-8 text following the standard
defined by Protocol Buffers V3 JSON encoding. While
implementation are not required to use the Protocol Buffers
software, the JSON encode must follow its
specification. Messages are written to the stream in
[line-delimited JSON format]
(https://en.wikipedia.org/wiki/JSON_Streaming#Line_delimited_JSON).

The MIME type for JSON encode is
``application/ga4gh.v${apiversion}+JSON``.

Binary message encoding
~~~~~~~~~~~~~~~~~~~~~~~

Message may be encoded in an efficient binary format using
Protocol Buffers V3 binary encoding format. Each message is
preceded by a 32-bit byte length written in network byte order,
followed by the message bytes.

The MIME type for binary encode is
``application/ga4gh.v${apiversion}+x-protobuf``.

Goals and Rationale
-------------------

The goals for introducing a streaming protocol are:

-  Improve performance by reducing latency of multiple page responses
-  Providing efficient binary encoding as well as simple JSON encoding
-  Simplify server implementation
-  Simplify client programming paradigm
-  Allow restarting larger result queries that fail
-  Allow results of mixed object types without creating new containers

Rationale for a streaming protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The original GA4GH paging protocol offers a simple client
interface that allows clients to read a complete JSON documents
'off-the-wire'. The returned response objects contained a
homogeneous vector of results along with a next page token. This
also allows for the easy resumption of failed transfers.

However, during the implementing of the protocol, drawbacks have
been recognized:

- Paging introduces latency, as the client must get a complete
  response and parse the document before it can issue the
  request for the next page. Large pages make for poor
  interactive responsiveness, and small pages lead to a high
  protocol overhead.
- Paging was performance limiting due to the need to buffer the
  returned JSON document. It requires a tradeoff between
  client/server memory and the number of requests. Even if a
  given client can dedicate a lot of memory for a transfer, the
  server must impose limits to prevent DoS attacks and manage an
  unpredictable request load.
- Paging makes the implementation of a server complex. This is
  due it must be able to efficiently resume every query at an
  arbitrary point determined by the client.
- Fixed return structures limit the flexibility of queries. New
  result structures must be defined for every new query.
- Result structures limited to a single returned object type
  influence the data model. We end up with more complex, larger
  objects to include more information in a single
  response. Variant is the degenerate example, where it can
  contain thousands of calls.

Rationale for mixed object type results streams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While ReST APIs tend to return one of more objects of the same
type, it may be desirable for a query language API to produce
more complex result streams. It was felt that the increased
expressiveness and efficiency of query languages will make them
important for GA4GH and a single flexible response protocol
should be use for all messages.

One type specification design that was considered was to send a
``dataType`` message when the data types changes in the
stream. It was felt that this could result in degenerate cases
of a larger number of ``dataType`` messages.  It was also
thought that it would be a similar level of client complexity to
build a ``typeKey`` map as to track the type of the
stream. There is also a robustness advantage in ``dataObject``
messages having an inexpensive type
identifier include in the message.

Checkpoint rationale
~~~~~~~~~~~~~~~~~~~~

On of the goals of paging is to allow for restarting large
transfers on failure.  With paging, the error recover is part of
every transaction rather than handled as the exceptional
case. Clients and servers on a highly reliable local network,
such as in a compute cloud, still pay the penalty of paging,
although such failures will be rare.

The implementation of paging required servers to be able to
restart a query from any point. The checkpoint approach allows
server implementations more discretion in the granularity of the
checkpoints, possibly simplifying the implementation.

Issues
~~~~~~

-  Need to define HTTP error codes and responses for messaging layer.
-  Need to define how GA4GH-level errors are passed through
-  Should parallel transfers be support for larger data queries. If so,
   how to prevent duplication of objects on different streams.

References
~~~~~~~~~~

- `rfc7230 - Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and
  Routing <http://tools.ietf.org/html/rfc7230>`__
- `rfc7231 -Hypertext Transfer Protocol (HTTP/1.1): Semantics and
  Content <http://tools.ietf.org/html/rfc7231>`__
- `Protocol Buffers
  V3 <https://developers.google.com/protocol-buffers/docs/proto3>`__
