# avdl-to-rst Makefile
#
# GA4GH schema docs are generated from avdl comments.  The process is
# coordinated by this Makefile in these steps:
#   * All .avdl files are converted to .avpr using the avro-tools
#   package, which is downloaded if needed.
#   * All .avpr files are converted to .rst using a python script in
#   schemas/tools.


.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

CACHE_DIR:=${HOME}/.cache/ga4gh
AVPR_DIR:=/tmp/ga4gh-${UID}/avpr
AVDL_DIR:=../../../src/main/resources/avro

AVPR2REST_PATH:=../../../tools/sphinx/avpr2rest.py
AVRO_JAR_PATH:=${CACHE_DIR}/avro-tools.jar
AVRO_JAR_URL:=http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar

AVDL_BASENAMES:=$(subst ${AVDL_DIR}/,,$(wildcard ${AVDL_DIR}/*.avdl))
AVPR_BASENAMES:=${AVDL_BASENAMES:.avdl=.avpr}
RST_BASENAMES:=${AVDL_BASENAMES:.avdl=.rst}


default: ${RST_BASENAMES}


${AVRO_JAR_PATH}:
	mkdir -p ${@D}
	curl -o $@ ${AVRO_JAR_URL}

%.avpr: ${AVDL_DIR}/%.avdl ${AVRO_JAR_PATH}
	java -jar ${AVRO_JAR_PATH} idl $< $@

%.rst: %.avpr
	python ${AVPR2REST_PATH} $< .

.PHONY: clean cleaner cleanest
clean:
	/bin/rm -f *~
cleaner: clean
	/bin/rm -f *.avpr
cleanest: cleaner
	/bin/rm -f ${RST_BASENAMES}
