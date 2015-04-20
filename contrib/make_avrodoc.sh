#!/usr/bin/env bash

# Script to make the avrodoc documentation. Run from the contrib folder:
# $ contrib/make_avrodoc.sh
# Depends on avrodoc already being on the PATH.
# Can install the Avro command line tools jar itself.

if [ -d contrib ]
then
    # Make sure we are in the contrib directory.
    cd contrib
fi

if [ ! -f avro-tools.jar ]
then

    # Download the Avro tools
    curl -o avro-tools.jar  http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar
fi

# Make a directory for all the .avpr files
mkdir -p ../target/schemas

# Make a place to put the documentation
mkdir -p ../target/documentation

for AVDL_FILE in ../src/main/resources/avro/*.avdl
do
    # Make each AVDL file into a JSON AVPR file.

    # Get the name of the AVDL file without its extension or path
    SCHEMA_NAME=$(basename "$AVDL_FILE" .avdl)

    # Decide what AVPR file it will become.
    AVPR_FILE="../target/schemas/${SCHEMA_NAME}.avpr"

    # Compile the AVDL to the AVPR
    java -jar avro-tools.jar idl "${AVDL_FILE}" "${AVPR_FILE}"

    # Use Avrodoc to make a per-API documentation file.
    HTML_FILE="../target/documentation/${SCHEMA_NAME}.html"
    avrodoc "${AVPR_FILE}" > "${HTML_FILE}"

done



