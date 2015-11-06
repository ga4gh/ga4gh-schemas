#!/bin/bash

set -beEu -o pipefail

# Script to generate the sphinx documentation
#
# Instead of running this script, you probably want to run "mvn package" from
# the root of the repository.

# Expects sphinx and pypandoc to be installed

# This script expects to run from the repository root.

GENERATED_DOCS_LOC=target/generated-docs
RST_LOC=$GENERATED_DOCS_LOC/rst
RST_SCHEMAS_LOC=$RST_LOC/schemas
# HTML_LOC is where the final output goes.  It's relative to $GENERATED_DOCS_LOC.
HTML_LOC=merged

# Create a home for all the merged .rst files: the written ones and the generated ones

mkdir -p $RST_SCHEMAS_LOC

# Generate AVPR files

# Are the Avro tools installed?
AVRO_TOOLS_LOC=target/avro-tools
if [ ! -f $AVRO_TOOLS_LOC/avro-tools.jar ]
then
    # Download them if not
    echo -n Downloading Avro tools...
    mkdir -p $AVRO_TOOLS_LOC
    curl -s -o $AVRO_TOOLS_LOC/avro-tools.jar http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar
    echo " done."
fi

# Make a directory for all the .avpr files
mkdir -p target/schemas

echo Processing AVDL files...

for AVDL_FILE in src/main/resources/avro/*.avdl
do
    # Make each AVDL file into a JSON AVPR file:

    # Get the name of the AVDL file without its extension or path
    SCHEMA_NAME=$(basename "$AVDL_FILE" .avdl)

    # Decide what AVPR file it will become.
    AVPR_FILE="target/schemas/${SCHEMA_NAME}.avpr"

    # Compile the AVDL to the AVPR
    java -jar $AVRO_TOOLS_LOC/avro-tools.jar idl "${AVDL_FILE}" "${AVPR_FILE}"
done

echo Finished processing AVDL files.
echo
echo Writing HTML pages. This will take a few moments...

# copy the written documentation to the merged directory
cp -pr doc/source/* $RST_LOC

# convert AVPR to reST, then use sphinx to generate all the docs
python tools/sphinx/avpr2rest.py target/schemas/*.avpr $RST_SCHEMAS_LOC
cp doc/Makefile $GENERATED_DOCS_LOC
(cd $GENERATED_DOCS_LOC; make html BUILDDIR=$HTML_LOC)

echo
echo Complete! Your documentation is available in $GENERATED_DOCS_LOC/$HTML_LOC/html
echo
