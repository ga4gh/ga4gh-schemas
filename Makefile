# GA4GH top level Makefile to build document (requires GNU make)
#
# make is use to allow building on readthedocs.org, which does not
# support JAVA required for maven.

.DELETE_ON_ERROR:
.PRECIOUS :
.SUFFIXES :

# enable more robust bash
SHELL:=/bin/bash -beEu -o pipefail
BUILD_DIR:=target/doc

############################################################################
default: help

.PHONY: help
help:
	@echo "targets: " >&2
	@echo "   help - display this help messsage" >&2
	@echo "   docs - build HTML documentation in ${BUILD_DIR}" >&2
	@echo "   package - run mvn package" >&2
	@echo "   clean - delete generated documentation" >&2
	@exit 1

# N.B. this command mimics behavior on RTD
# doc/source is the root of the rst files; the ../.. components effectively
# counter the cd doc/source to place the docs at the schemas root
.PHONY: docs
docs:
	cd doc/source && sphinx-build -b html -d ../../${BUILD_DIR}/doctrees . ../../${BUILD_DIR}/html

.PHONY: package
package:
	mvn package

.PHONY: clean
clean:
	rm -rf ${BUILD_DIR}
