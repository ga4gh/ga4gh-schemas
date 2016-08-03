GA4GH Wire Protocol Specification
=================================

Version 0.3 [draft]

This document defines the GA4GH data exchange API Internet
protocol.  It provides a restartable, streaming protocol with
both ASCII and binary encoding formats.  It is designed to
efficiently send a potentially long stream of small messages.

This streaming protocol replaces the current GA4GH paging protocol.

This document is intended to be normative. The protocol should
be completely implementable based on this document and
referenced standards. Any undefined behavior or ambiguities
discovered during any implementation must result in an update of
this specification.

Goals
-----
The goals of this protocol are:

- Provide an efficient, straight-forward HTTP/1.1 based protocol for the GA4GH
  ReST requests and responses.  Initial, only responses are addressed, request
  protocol will be defined when write functionality is added to the API.
- Simple to define in an interoperable manner based.
- Allow for recovery of partial, failed transfers in an implementation independent
  manner.

  
Two-layer protocol
------------------

This protocol is defined in two layers:

- Data object layer - Data objects defined by the GA4GH
  schemas, such as ``VariantSet``, ``Variant``, ``Call``,
  etc.  Responses contain a series of GA4GH objects
  GA4GH objects that are encoded in either protocol buffers
  binary format or JSON.  
- HTTP 1.1 Internet protocol layer - HTTP 1.1 chunked encoding
  is used to robustly transfer a stream of objects without
  requiring the buffering of the entire request or response.
  

Internet protocol layer
-----------------------

GA4GH clients and servers communicate via streaming HTTP/HTTPS
using chunked transfer encoding ([rfc7230 - Hypertext Transfer
Protocol (HTTP/1.1): Message Syntax and Routing]
(http://tools.ietf.org/html/rfc7230)).  Data in the stream
consists of variable length message encode in one of the formats
defined in this document. The encoding is determined using HTTP
content-type negotiation ([rfc7231 -Hypertext Transfer Protocol
(HTTP/1.1): Semantics and Content]
(http://tools.ietf.org/html/rfc7231)).
Requests and responses may be sent using either a single HTTP
response body with content length or using HTTP 1.1 chunked
transfer encoding.
Servers are encouraged to implement chunked transfer encoding,
as it efficiently supports arbitrary length responses.  Clients
must accept chunked transfer encoding, as required by HTTP 1.1.

The HTTP 1.1 chunked transfer encoding error report model
indicates failed transfers. A connection that is closed without
receiving a trailer chunk must be treated as an error. When a
trailer chunk is received, it must be interrogated to see if it
contains a ``Status`` header that indicates an error.

MIME type is in the form
``application/ga4gh.v${apiversion}+${encoding}``. Where
``${encoding}`` is the encoding format described below. The
``${apiversion}`` is the dot-separate hierarchical API version of
the GA4GH API. For requests, the ``Accepts`` header is used to
specify the desired encoding and API version. The API version
hierarchy requested can be as specific as required, with omitted
minor versions resulting in the newest version available on the
server matching. Thus, a version of ``1.5`` can be satisfied
with version such as ``1.5``, or ``1.5.3``, etc. The individual
dot versions are compared as integers.  The response
``Content-Type`` contains the exact version of the API that was
return.

Data Object Layer
-----------------

The data object layer is implemented on top of the HTTP Internet
layer.  Except for restrictions place on object alignment for
checkpoint/resume (see below), the object layer views the
Internet layer as a stream of bytes.  Data objects are encoded
in this layer in either JSON or binary protocol buffer format.

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

Data objects may be encoded in an efficient binary format using
Protocol Buffers V3 binary encoding format. Each message is
preceded by a 32-bit byte length written in network byte order,
followed by the message bytes.

The MIME type for binary encode is
``application/ga4gh.v${apiversion}+x-protobuf``.

Transfer checkpoint/resume
~~~~~~~~~~~~~~~~~~~~~~~~~~

The GA4GH streaming protocol supports resuming an interrupted
response by sending periodic checkpoint object that can be used
to resume a transfer at that point. See the Rationale section for discussion
of this design decision.

As the checkpoint functional may induce a implementation burden
for clients and servers, and given it is not required in all
applications or environments, implementing this functional is
optional.

Checkpoint/resume is only useful and support on top of chunked
transfer encoding.

The server may send periodic checkpoint objects that are used to
resume failed transfers.  Checkpoint objects are sent as the
value of chunk extension named ``X-GA4GH-CHECKPOINT``.  The
value is the checkpoint object, which encodes the state required
for the server to resume at the beginning of the chuck.  This
mechanism should not rely on preserving client state on the server
and remain valid over restarts of the server.  If the underlying
data that would be included in the response changes, the
behavior is undefined.  Chunks containing a checkpoint object
must start on a GA4GH data object boundary.

To resume from a failure, the original request should be
resent, along with  ``X-GA4GH-CHECKPOINT-FREQUENCY``
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
mainly be used for larger transfers over wide area networks, the
default value is disabled (0).

The checkpoint object must be encoded in a manner that is valid
as an HTTP header value and as a chunk extension value. The HTTP
specification is not entirely clear on valid values.  Using only
printable ASCII characters, excluding semi-colon, will suffice.
URL encoding of checkpoint object is recommended.

It is expected that a similar checkpoint/resume facility will
be used in a write API when it is defined by GA4GH.

Rationale
---------

Rationale for a streaming protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The original GA4GH paging protocol offers a simple client
interface that allows clients to read a complete JSON documents
'off-the-wire'. The returned response objects contained a
homogeneous vector of results along with a next page object. This
also allows for the easy resumption of failed transfers.  This
resulted in paging being requirement of the interface, not at
option, as with many ReST APIs (e.g. AWS).

However, during the implementing of the protocol, drawbacks have
been recognized:

- Paging introduces latency, as the client must get a complete
  response and parse the document before it can issue the
  request for the next page. Large pages make for poor
  interactive responsiveness, and small pages lead to a high
  protocol overhead.
- Paging is performance limiting due to the need to buffer the
  returned JSON document. It requires a trade-off between
  client/server memory and the number of requests. Even if a
  given client can dedicate a lot of memory for a transfer, the
  server must impose limits to prevent DoS attacks and manage an
  unpredictable request load.
- Paging can make the implementation of a server complex. This is due the
  requirement to efficiently resume every query at an arbitrary point
  determined by the client.  Paging's easy of implementation varies with the type
  of data store and complexity of queries.  While many ReST APIs implement
  paging, it's not clear that specifying in an interoperable API independent
  of the implementation is desirable.

Alternative Technologies
~~~~~~~~~~~~~~~~~~~~~~~~

Multiple technologies are available to 


Checkpoint rationale
~~~~~~~~~~~~~~~~~~~~

One of the apparent goals of paging is to allow for resumes large
transfers on failure.  With paging, the error recover is part of
every transaction rather than handled as the exceptional
case. Clients and servers on a highly reliable local network,
such as in a compute cloud, still pay the penalty of paging,
although such failures will be rare.

The implementation of paging required servers to be able to
resume a query from any point. The checkpoint approach allows
server implementations more discretion in the granularity of the
checkpoints, possibly simplifying the implementation.


Possible additions to specification
-----------------------------------

Support for GUI-style paging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User interface applications often allow for paging through
results from a query.  Support for GUI is not a priority in the
GA4GH API design.  For instance, there is no support getting the
counting of results without reading the without reading the
entire response or and no support for sorting responses.
However, it's felt that basic support for GUIs can be added to
the GA4GH protocol with a small amount of additional complexity.

A key piece of API functionality required for GUIs is the
ability to incrementally display results.  This is normally done
with paging.  However, users don't normally go beyond the first
few pages of the results.  This assumption allows for supporting
this access pattern without the complexity of efficient paging
through the result set.  Paging through the initial part of a
result set can usually be implemented by executing a query and
discarding records up to a specified offset and then returning
the specified number of records.  While inefficient in the
general cases,  this may meet the needs of many GUI applications.

This approach to supporting GUIs is placed in this document for
discussion, and given the lack of support for sorting, may not
be implemented.


Issues
~~~~~~

- Need GA4GH info request to determine if checkpoints are supported.

References
~~~~~~~~~~

- `rfc7230 - Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and
  Routing <http://tools.ietf.org/html/rfc7230>`__
- `rfc7231 -Hypertext Transfer Protocol (HTTP/1.1): Semantics and
  Content <http://tools.ietf.org/html/rfc7231>`__
- `Protocol Buffers
  V3 <https://developers.google.com/protocol-buffers/docs/proto3>`__
