Documention
!!!!!!!!!!!

This directory contains source and tools to build the GA4GH schemas
documentation.

The `GA4GH schemas documentation
<http://ga4gh-schemas.readthedocs.org/>`_ is built automatically by
Read the Docs, typically within two minutes of a commit to the master
branch.


Building
@@@@@@@@

Make sure you have graphviz installed (`brew install graphviz` or `sudo apt-get install graphviz`).
Then to build documentation, type::

  make docs

in the schemas root directory.  The resulting documentation will be in
the ``target/doc/html`` directory.  (You will need certain
prerequisites and, for the moment, you'll have to ferret those out
yourself.)


Documentation tips
@@@@@@@@@@@@@@@@@@

Documents are written in `ReStructured Text
<http://sphinx-doc.org/rest.html>`_ using `Sphinx
<http://sphinx-doc.org/>`_.  documentation being extracted from the
schemas.

- Abbreviations are stored in ``epilog.rst``.
