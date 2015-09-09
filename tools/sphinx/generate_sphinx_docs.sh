#!/bin/bash

set -beEu -o pipefail

# Script to generate the sphinx documentation
# Run from inside schemas/sphinx

# Expects sphinx and pypandoc to be installed

# Meant to be run from the Maven build, so set our cwd relative to the top-level dir
cd doc

# Generate the hand-written documentation
make html

# Generate AVPR files

# Are the Avro tools installed?
AVRO_TOOLS_LOC=../target/avro-tools
if [ ! -f $AVRO_TOOLS_LOC/avro-tools.jar ]
then
    # Download them if not
    echo -n Downloading Avro tools...
    mkdir -p $AVRO_TOOLS_LOC
    curl -s -o $AVRO_TOOLS_LOC/avro-tools.jar http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar
    echo " done."
fi

# Make a directory for all the .avpr files
mkdir -p ../target/schemas

echo Processing AVDL files...

for AVDL_FILE in ../src/main/resources/avro/*.avdl
do
    # Make each AVDL file into a JSON AVPR file:

    # Get the name of the AVDL file without its extension or path
    SCHEMA_NAME=$(basename "$AVDL_FILE" .avdl)

    # Decide what AVPR file it will become.
    AVPR_FILE="../target/schemas/${SCHEMA_NAME}.avpr"

    # Compile the AVDL to the AVPR
    java -jar $AVRO_TOOLS_LOC/avro-tools.jar idl "${AVDL_FILE}" "${AVPR_FILE}"
done

echo Finished processing AVDL files.
echo
echo Writing HTML pages. This will take a moment...

# convert AVPR to reST, then use sphinx to generate docs
HTML_LOC=../target/avro-pages

mkdir -p $HTML_LOC
python ../tools/sphinx/avpr2rest.py ../target/schemas/*.avpr $HTML_LOC
(cd ../tools/sphinx; make html)

echo
echo Complete!
echo
