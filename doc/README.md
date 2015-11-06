![Image](http://genomicsandhealth.org/files/logo_ga.png)

# Documentation system for the GA4GH APIs

This sub-tree contains the overview documentation and generation system for
the GA4GH API.  The generation is based on [Sphinx](http://sphinx-doc.org/),
with documentation being extracted from the schemas.

**[The documentation is available for your perusal on ReadTheDocs](http://ga4gh-schemas.readthedocs.org)**

A daily build of the documentation is temporarily available here:
 
http://hgwdev.cse.ucsc.edu/~markd/ga4gh/documentation-pr/

# Building the Documentation

The documentation is built using Sphinx, which is run through Maven in top-level
project directory. See [INSTALL.md](../INSTALL.md) for instructions on building
the documentation.

In particular, the Makefile seen here **cannot** be used to manually build the
documentation.
