#!/bin/bash
# ensure that the specified version of protoc is installed in
# /tmp/proto$PROTO_VERSION/bin/protoc, which maybe cached

# bash tools/travis-install-protoc.sh 3.0.0-beta-3.1
#   


# make bash more robust.
set -beEux -o pipefail

if [ $# != 1 ] ; then
    echo "wrong # of args: $0 protoversion" >&2
    exit 1
fi

PROTO_VERSION="$1"
PROTO_DIR="/tmp/proto$PROTO_VERSION"

# Can't check for presence of directory as cache auto-creates it.
if [ ! -f "$PROTO_DIR/bin/protoc" ]; then
  wget -O - "https://github.com/google/protobuf/archive/v${PROTO_VERSION}.tar.gz" | tar xz -C /tmp
  cd "/tmp/protobuf-${PROTO_VERSION}"
  ./autogen.sh
  ./configure --prefix="$PROTO_DIR" --disable-shared
  make -j 4
  make install
fi

