#!/usr/bin/env bash
set -e

# Script to turn Avro IDL into a UML diagram. Requires Python 2.7, GNU sed,
# and GraphViz. Run from the contrib folder:
#
# $ contrib/update_uml.sh
#
# Excludes the methods files.
#
# The resulting UML will show up in doc/uml.png and doc/uml.dot
#
# If the edge autodetection fails, add new ID reference edges to 
# contrib/extra_edges.dot


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

for AVDL_FILE in ../src/main/resources/avro/*.avdl
do
    # Make each AVDL file into a JSON AVPR file.

    # Get the name of the AVDL file without its extension or path
    SCHEMA_NAME=$(basename "$AVDL_FILE" .avdl)

    # Decide what AVPR file it will become.
    AVPR_FILE="../target/schemas/${SCHEMA_NAME}.avpr"

    # Compile the AVDL to the AVPR
    java -jar avro-tools.jar idl "${AVDL_FILE}" "${AVPR_FILE}"

done

# Now make the DOT file
./avpr2uml.py `ls ../target/schemas/* | grep -v method` --dot ../doc/uml.dot

# Knock off the last line, which closed the graph. Must have GNU sed. See
# <http://stackoverflow.com/a/4881990/402891>
sed -i '$ d' ../doc/uml.dot

# Add in any manually defined ID reference edges
cat extra_edges.dot >> ../doc/uml.dot

# Add the closing brace back
echo "}" >> ../doc/uml.dot

# Make the picture
dot ../doc/uml.dot -T svg -o ../doc/uml.svg


