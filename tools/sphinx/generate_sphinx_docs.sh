#!/bin/bash

set -beEu -o pipefail

# Script to generate the sphinx documentation
# Run from inside schemas/sphinx

# Expects sphinx and pypandoc to be installed

# Meant to bee run from the Maven build, so set our cwd

home=tools/sphinx

cd $home

# Generate AVPR files

# Are the Avro tools installed?
if [ ! -f avro-tools.jar ]
then
    # Download them if not
    echo -n Downloading Avro tools...
    curl -s -o avro-tools.jar  http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar
    echo " done."
fi

# Make a directory for all the .avpr files
mkdir -p ../target/schemas

# Make a place to put the documentation
mkdir -p ../target/documentation

echo Processing AVDL files...

for AVDL_FILE in ../../src/main/resources/avro/*.avdl
do
    # Make each AVDL file into a JSON AVPR file:

    # Get the name of the AVDL file without its extension or path
    SCHEMA_NAME=$(basename "$AVDL_FILE" .avdl)

    # Decide what AVPR file it will become.
    AVPR_FILE="../target/schemas/${SCHEMA_NAME}.avpr"

    # Compile the AVDL to the AVPR
    java -jar avro-tools.jar idl "${AVDL_FILE}" "${AVPR_FILE}"
done

echo Finished processing AVDL files. Writing HTML pages now.
echo This will take a moment...

# convert AVPR to reST, then use sphinx to generate docs
mkdir -p pages
python avpr2rest.py ../target/schemas/*.avpr pages/
make html

echo
echo "****"
echo Complete.  The HTML files are in `pwd`/_build/html.
echo Point your browser at file:`pwd`/_build/html/index.html .
echo "****"
