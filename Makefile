# GA4GH top level Makefile (requires GNU make)

.DELETE_ON_ERROR:
.PHONY : FORCE
.PRECIOUS :
.SUFFIXES :

SHELL:=/bin/bash -o pipefail
SELF:=$(firstword $(MAKEFILE_LIST))


############################################################################
#= BASIC USAGE
default: help

#=> help -- display this help message
help:
	@tools/makefile-extract-documentation "${SELF}"

#=> docs -- make docs (in build/html)
docs: docs-schemas
	PYTHONPATH=tools/sphinx sphinx-build -b html -d build/doctrees doc/source build/html

#=> docs-schema -- generate rst files from avdl
docs-schemas:
	make -C doc/source/schemas default
