## Generating API Documentation

----

We rely on the [Avrodoc](https://github.com/ept/avrodoc) project to generate static HTML pages for documentation.

Assuming that you have [Node.js](http://nodejs.org/) and [NPM](https://www.npmjs.org/) installed and configured, you can install the avrodoc command line tool like:  

```shell
npm install avrodoc --global
```

The `avrodoc` tool expects Avro schemas in JSON format. The Maven plugin we use for generation of artifacts and tests does not produce the JSON formatted Avro schema. You will need to download the [Avro tools JAR file](http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar)

```shell
# For a full list of mirrors, see http://www.apache.org/dyn/closer.cgi/avro/

curl -o /opt/avro-tools.jar  http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar

```

Once you have dowloaded the Avro tools, you can use them to create JSON formatted Avro schema like so:

```shell
java -jar avro-tools.jar idl /path/to/avro/idl/file.avdl /path/to/avro/json/file.avpr
```

You would then use that output to create the html file like so:

```shell

avrodoc input.avpr > output.html
```

### Putting it all together

```shell
# download and install avrodoc
npm install avrodoc --global

# download the Avro tools
curl -o /opt/avro-tools.jar  http://www.us.apache.org/dist/avro/avro-1.7.7/java/avro-tools-1.7.7.jar

# assumes that $CWD is the ga4gh/schemas project dir

# creating the JSON schema for the reads API
mkdir -p target/schemas
java -jar /opt/avro-tools.jar idl src/main/resources/avro/reads.avdl target/schemas/reads.avpr

# creating the documentation for the reads API
mkdir -p target/documentation
avrodoc target/schemas/reads.avpr > target/documentation/reads.html

```

### Automating the process

Once you have installed Avrodoc, you can run the `contrib/make_avrodoc.sh` script to automate the above process, building Avrodoc HTML files for each `.avdl` in `target/documentation`:

```shell
contrib/make_avrodoc.sh
```

## UML Diagrams

There is a UML diagram in `doc/uml.svg`, with GraphViz source in `doc/uml.dot`. These files are generated from the Avro IDL files by the script `contrib/make_uml.sh`, which means that their layout may be slightly confusing, but that they will track changes to the Avro source automatically.

The UML generator, which lives mostly in `contrib/avpr2uml.py`, attempts to autodetect ID reference relationships between objects, by guessing based on field names. If it misses a relationship that it should find, add it to `contrib/extra_edges.dot`. If it finds a spurious reference relationship that does not really exist, you will have to fix the script to get rid of it.

To re-generate the automatic diagrams:

```shell
contrib/make_uml.sh
```

Watch the warnings; if it thinks there is an ID reference but it can't find what is being referenced, it will tell you.

### Manual UML Diagrams

There is also a manually curated UML diagram, `doc/manual_uml.dia` and `doc/manual_uml.svg`, that describes the layout of the GA4GH data model. This diagram is more likely to be outdated, but is also probably easier to read.

This diagram was generated from the schemas by using [Doxygen](http://www.doxygen.org/) to generate XML, and then using [Dia](http://live.gnome.org/Dia) to generate a UML from that XML output. Unfortunately, this only imports the Avro types: dependencies and layout still need to be done manually.

The `contrib` folder contains a `Doxyfile` and a rudimentary filter (`avdlDoxyFilter.py`) that can be used to generate Doxygen XML that DIA can import. To use them, simply do:

```shell
# Go into the contrib directory
cd contrib

# run Doxygen, which will put XML docs in ../doc/doxygen/XML
doxygen
```

Then, open up Dia, do `File -> Open`, set the input file type to `Dox2UML (Multiple)`, and open `doc/doxygen/XML/index.xml`. Dia will generate UML classes for all the schema types, which you can lay out into a UML class diagram.
