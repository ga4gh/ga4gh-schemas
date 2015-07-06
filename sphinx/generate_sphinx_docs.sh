#!/usr/bin/env bash

# Script to generate the sphinx documentation
# Run from inside schemas/sphinx

# Expects sphinx and pypandoc to be installed

# generate AVPR files
pushd ../contrib
./make_avrodoc.sh

# convert AVPR to reST, then use sphinx to generate docs
popd
mkdir -p pages
python avpr2rest.py ../target/schemas/*.avpr pages/
make html
