.. _network:


*************************
Connecting GA4GH Services
*************************


The GA4GH aims to create an easy to implement network of Genomics data
services. To achieve this end, the protocol presents some message, endpoints,
and methods that are dedicated to communicating about a service's status
when establishing peers.

Genomic data is not passed over the Network methods. Network participation
is not mandatory, although it is encouraged.


Peer Service
------------

Two servers, if they are able to communicate over a network connection, can
form a simple ad-hoc peer to peer relationship by notifying each other of
their existence. A network can be formed by allowing services to share their
list of peers with each other.

Use Cases
=========

-  Alice would like to join an existing P2P network by announcing to a
   good known peer. By sending an announce request with the URL of her
   service to the URL of a known good peer, she has advertised her
   services.
-  Alice would like to create an ad-hoc peer to peer network with Bob.
   She first announces her service to Bob and then adds Bob’s service to
   her list of peers.
-  Alice would like to get a list of all the available datasets on a
   GA4GH network. She first requests the dataset from a known member of
   the network. She then requests that service’s list of peers. She then
   requests the list of datasets from each peer in the peer list. By
   recursively following peer lists she can list all the datasets on the
   network.
-  Alice would like to advertise the protocol version her service
   presents. This is done by exposing an endpoint where a client can
   request the protocol version and other information about her service.

Network Topology Design
=======================

Ad-hoc private networks can be established between peers, as well as hub and
spoke models.

Institutions may choose to take advantage of the Peer Service to tier
services. This is done by presenting a service to the public on the GA4GH
network that performs aggregations of data on underlying peers. These peers
only expose their services to the aggregation service.

We are seeking client demonstrations of crawlers, authentication mechanisms,
and aggregators that take advantage of these methods.

Network Diagram
***************

This diagram conceives of a network architecture where public nodes create
a fully connected network, while aggregators over private data make some of
these results available to the wider scientific community.

.. image:: /_static/network.svg
   :align: center


This architecture is not enforced by the protocol and network participants
will determine what topology the network takes.

Network Membership
******************

Service operators choose whether to respond to announcements, or whether to
add a peer to their peer list. Since services are free to manage their peer
list as they please, various network configurations can be achieved. Using a
known good list of peers a single decentralized, fully connected network
can be made.

Public Initial Peers
********************

The GA4GH attempts to bootstrap this network by maintaining the latest
released network protocol at http://1kgenomes.ga4gh.org . However, the
process of evaluating announcements requires human curation, so do not expect
your peer to be listed immediately.

Private Networks
****************

White listing allows one to create a service that only responds to requests
from known hosts. By configuring a node to only respond to requests from a
certain domain, it is placed in a private network.

By white listing only the peers on a service's peer list, it is possible for
server maintainers to create private network topologies to suit their needs.

Methods
=======

The Peer Service presents three endpoints: ``/announce``, ``peers/list``, and
``/info``. Small messages about services or potential peers are communicated
over them.

Announcements
*************

Any client can notify a server about a possible peer using an `AnnouncePeerRequest
<../schemas/peer_service.proto.html#protobuf.AnnouncePeerRequest>`_,
which is a simple message including the URL of the intended peer.
That service can then respond to the announcement by adding that peer to its
list of peers.

By reviewing announcements a server operator can control which announcements
are promoted into peers.

Listing Peers
*************

Each service, in addition to receiving announcements about the presence of
other peers, shares its list of peers at the ``peers/list`` endpoint. This
list can be paged through if the list of peers gets very long. Each entry
in the `ListPeersResponse
<../schemas/peer_service.proto.html#protobuf.ListPeersResponse>`_ includes a URL to a possible peer. It is up to
individual services to maintain their list of peers.

The endpoint is named off of the ``peers`` path because, in practice, we expect
implementations to provide ``peers/add`` and ``peers/remove`` methods, however,
these are internal configuration paths and not needed to comply with the
protocol.

Get Info
********

To assist in the process of evaluating a peer, an info endpoint allows a client
to request information about the service. The `GetInfoResponse
<../schemas/peer_service.proto.html#protobuf.GetInfoResponse>`_
includes the protocol version.


For implementation details, please visit `the protobuf description
<../schemas/peer_service.proto.html>`_.
