Documention
!!!!!!!!!!!

This directory contains source and tools to build the GA4GH schemas
documentation.

Building
@@@@@@@@

To build documentation, type::

  make docs

in the schemas root directory.  The resulting documentation will be in
the ``schemas/build/html`` directory.

.. note:: The ``tools/sphinx/generate_sphinx_docs.sh`` script is
          obsolete.  The functionality is entirely subsumed by ``make
          docs``, which also enables incremental updates.

A `daily build
<http://hgwdev.cse.ucsc.edu/~markd/ga4gh/documentation-pr/>`_ is also
available at UCSC. 

Changes are in progress to enable building the documentation at Read
the Docs.


Building Process
@@@@@@@@@@@@@@@@

Documentation is currently derived in part from avdl files by
processing files ``schemas/src/main/resources/avro/`` to generate rst
files in ``schemas/doc/sources/schemas``.  See
schemas/doc/sources/schemas/Makefile for details about this process.
``make docs`` invokes this conversion automatically.

Currently, rst files are generated everytime docs are built, and
requires tools that cannot be easily made available on Read The Docs.
Alternatively we are considering building the rst files upon commit,
which would then enable read the docs to build from rst sources.


Documentation tips
@@@@@@@@@@@@@@@@@@

Documents are written in `ReStructured Text
<http://sphinx-doc.org/rest.html>`_ using `Sphinx
<http://sphinx-doc.org/>`_.  documentation being extracted from the
schemas.

- Abbreviations are stored in ``epilog.rst``.
- Reference avro elements with ``:avro:key``.

