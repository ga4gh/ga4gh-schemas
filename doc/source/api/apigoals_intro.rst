.. _apigoals:


API Goals
!!!!!!!!!


* From the `GA4GH DWG <http://ga4gh.org/#/documentation>`_ site:

    The Global Alliance for Genomics and Health (GA4GH) Genomics [API]
    will allow the interoperable exchange of genomic information
    across multiple organizations and on multiple platforms. This is a
    freely available open standard for interoperability, that uses
    common web protocols to support serving and sharing of data on DNA
    sequences and genomic variation. The API is implemented as a
    webservice to create a data source which may be integrated into
    visualization software, web-based genomics portals or processed as
    part of genomic analysis pipelines. It overcomes the barriers of
    incompatible infrastructure between organizations and institutions
    to enable DNA data providers and consumers to better share genomic
    data and work together on a global scale, advancing genome
    research and clinical application.

* The API must allow flexibility in server implementation, including:

  * choice of persistent backend (e.g. files, SQL, NoSQL)
  * choice of implementation language (e.g. Java, Python, Go)
  * choice of authorization model (e.g. all public, all private, fine-grain ACLs)
  * choice of import mechanism (e.g. self-service vs. centrally managed)
  * choice of commercial model (e.g. single payer vs. per-data-owner billing)
  * choice of scale (from a single researcher working with dozens of
    sequences and homogeneous tools, to government-funded studies with
    over a million sequences and multiple tool chains)

* The API must allow full-fidelity representation of data that was
  prepared using today’s common methods and stored using today’s
  common file formats.

  * Note that real-world data files sometimes use invalid or ambiguous
    syntax, making it hard to understand the semantics of the
    contained data. If a server can't figure out what those semantics
    are, it can throw an error on import. But whenever the semantics
    are clear, including when they're specified in valid data files,
    the API must allow preserving them.
  
* The API should allow adding more structure to data beyond today’s
  common practices (e.g. formal provenance, versioning).

* The API should allow data owners to organize their data in ways that
  make sense to them, which implies there often isn’t One True
  Taxonomy. For example, a ReadGroupSet is defined as “a set of
  ReadGroups that are intended to be analyzed together” -- different
  researchers might choose different sets for different purposes.

  * At the same time, the API should encourage reusable organization,
    anticipating a future that supports cross-researcher and
    cross-repository data federation.


Unresolved Issues
@@@@@@@@@@@@@@@@@

* What is the operational scope of the API?  Is the capacity goal for
  a transfer?  Should it handle small amounts of data randoman or
  larger transfers?
* How is sharing defined?  Download of data for use in another
  environment or online, random access to the data?
* What are the performance goals of the API in various configurations?
* What is the scope of interoperability?  Code-only interoperability
  or data interoperability?
* Is the DWG defining an API or a federated network of servers, tools
  to build a federated network of servers?  Need to define the scope.
* Need high-level uses cases for entire API.
