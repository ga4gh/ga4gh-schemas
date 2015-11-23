# GA4GH top level Makefile (requires GNU make)

.DELETE_ON_ERROR:
.PHONY : FORCE
.PRECIOUS :
.SUFFIXES :

SHELL:=/bin/bash -o pipefail
SELF:=$(firstword $(MAKEFILE_LIST))
BUILD_DIR:=target/doc

############################################################################
#= BASIC USAGE
default: help

#=> help -- display this help message
.PHONY: help
help:
	@tools/makefile-extract-documentation "${SELF}"

#=> docs -- make docs (in build/html)
# N.B. this command mimics behavior on RTD
# doc/source is the root of the rst files; the ../.. components effectively
# counter the cd doc/source to place the docs at the schemas root
.PHONY: docs
docs: docs-schemas
	cd doc/source; sphinx-build -b html -d ../../${BUILD_DIR}/doctrees . ../../${BUILD_DIR}/html

#=> docs-schema -- generate rst files from avdl
docs-schemas:
	make -C doc/source/schemas default

.PHONY: package
package:
	mvn package


.PHONY: clean cleaner cleanest
clean:
	find . -regex '.*\(~\|\.bak\)' -print0 | xargs -0r /bin/rm -v
	make -C doc/source/schemas $@
cleaner: clean
	make -C doc/source/schemas $@
cleanest: cleaner
	find . -regex '.*\(\.orig\)' -print0 | xargs -0r /bin/rm -v
	rm -fr target
	make -C doc/source/schemas $@
