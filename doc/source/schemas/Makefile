# proto-to-rst Makefile
#
# GA4GH schema docs are generated from proto comments.  The process is
# coordinated by this Makefile in these steps:
#   * All .proto files are converted to .json using the
#   protoc json plugin `tools/sphinx/my-plugin.py`.
#   * All .json files are converted to .rst using a python script in
#   schemas/tools.


.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

CACHE_DIR:=${HOME}/.cache/ga4gh
JSON_DIR:=/tmp/ga4gh-${UID}/json
PROTO_BASE_DIR:=../../../src/main/proto
PROTO_DIR:=${PROTO_BASE_DIR}/ga4gh

AVPR2REST_PATH:=../../../tools/sphinx/protodoc2rst.py
PROTOC_PLUGIN_PATH:=../../../tools/sphinx/protobuf-json-docs.py

PROTO_BASENAMES:=$(subst ${PROTO_DIR}/,,$(wildcard ${PROTO_DIR}/*.proto))
AVPR_BASENAMES:=${PROTO_BASENAMES:.proto=.proto.json}
RST_BASENAMES:=${PROTO_BASENAMES:.proto=.rst}


default: ${RST_BASENAMES}

%.proto.json: ${PROTO_DIR}/%.proto
	mkdir -p ${JSON_DIR}
	protoc --proto_path ${PROTO_BASE_DIR} --plugin=protoc-gen-custom=${PROTOC_PLUGIN_PATH} --custom_out=${JSON_DIR} $<

%.rst: %.proto.json
	python ${AVPR2REST_PATH} ${JSON_DIR}/ga4gh/$< .

.PHONY: clean cleaner cleanest
clean:
	/bin/rm -f *~
cleaner: clean
	/bin/rm -f *.avpr
cleanest: cleaner
	/bin/rm -f ${RST_BASENAMES}