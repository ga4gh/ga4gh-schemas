#!/bin/bash -e
# For backward compatibility, this script will invoke the
# make-based doc build process

root_dir=$(dirname $0)/../..
cd $root_dir
exec make docs
