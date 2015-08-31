#!/usr/bin/env bash

# Script to generate the sphinx documentation
# Run from inside schemas/sphinx

# Expects sphinx and pypandoc to be installed

# generate AVPR files

# Are the Avro tools installed?
if [ ! -f avro-tools.jar ]
then
    # Download them
    curl -o avro-tools.jar  http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar
fi

# Make a directory for all the .avpr files
mkdir -p ../target/schemas

# Make a place to put the documentation
mkdir -p ../target/documentation

for AVDL_FILE in ../src/main/resources/avro/*.avdl
do
    # Make each AVDL file into a JSON AVPR file:

    # Get the name of the AVDL file without its extension or path
    SCHEMA_NAME=$(basename "$AVDL_FILE" .avdl)

    # Decide what AVPR file it will become.
    AVPR_FILE="../target/schemas/${SCHEMA_NAME}.avpr"

    # Compile the AVDL to the AVPR
    java -jar avro-tools.jar idl "${AVDL_FILE}" "${AVPR_FILE}"
done

# convert AVPR to reST, then use sphinx to generate docs
mkdir -p pages
python avpr2rest.py ../target/schemas/*.avpr pages/
make html
