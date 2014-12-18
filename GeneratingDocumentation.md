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
