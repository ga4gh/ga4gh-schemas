Documention
!!!!!!!!!!!

This directory contains source and tools to build the GA4GH schemas
documentation.

The documentation is built automatically by Read the Docs upon commit
to the master branch.  The resulting docs should appear at
https://ga4gh-schemas.readthedocs.org/ within 2 minutes after commit.


Building
@@@@@@@@

To build documentation, type::

  make docs

in the schemas root directory.  The resulting documentation will be in
the ``target/doc/html`` directory.  (You will need certain
prerequisites and, for the moment, you'll have to ferret those out
yourself.)


Building Process
@@@@@@@@@@@@@@@@

The current doc flow is roughly as follows::

  avdl ----1----> avpr ----2----> rst -| 
                                       | ----3----> html
                                  rst -|

  |- doc/source/schema/Makefile  -| |--  sphinx  --|
  |------ top-level Makefile ('make docs') --------|
                    
* 1 = avro-tools, downloaded on demand; requires java
* 2 = avpr2rest.py, a custom script in tools/sphinx/
* 3 = sphinx-build, part of the sphinx package

.. warning:: Because we cannot currently run step 1 at Read the Docs,
             it is imperative that developers type `make docs-schema`
             at the top level if avdl files are updated, and then
             commit the changed rst files.


Documentation tips
@@@@@@@@@@@@@@@@@@

Documents are written in `ReStructured Text
<http://sphinx-doc.org/rest.html>`_ using `Sphinx
<http://sphinx-doc.org/>`_.  documentation being extracted from the
schemas.

Abbreviations are stored in ``epilog.rst``.

Reference avro elements with ``:avro:key``.

