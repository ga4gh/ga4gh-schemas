.. _swagger:

Generating API Definitions
@@@@@@@@@@@@@@@@@@@@@@@@@@

There has been an effort to standardize the methods for generating HTTP API descriptions that allow developers to rapidly develop gateways into their data. Since the GA4GH schemas are defined using Google Protocol Buffers IDL, it is possible to use this definition to generate documentation and code.

In this document we will generate swagger definitions for the GA4GH API using a plugin for the `protoc` compiler. For more on installing the protocol buffers compiler see INSTALL.rst.

Installing Prerequisites
------------------------

Once you have the protocol buffers compiler installed, you'll need to install the `go` language bindings for your system. On Mac OS X this can be done using `homebrew <http://brew.sh>`_ .

::

  brew install go

Next create a directory that will contain the `go` packages we will install, and add it to your path. We will set that as our `GOPATH` and add it to the system `PATH`.

::

  mkdir ~/golang
  export GOPATH=~/golang
  export PATH=$PATH:$GOPATH/bin

We install the required packages packages. For more information see: `grpc-gateway <https://github.com/gengo/grpc-gateway>`_ 

::

  go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
  go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
  go get -u github.com/golang/protobuf/protoc-gen-go

Now that all of the prerequisites have been installed, we can generate swagger documents, which are JSON that describe the HTTP interface.


Compiling Swagger Documentation
-------------------------------

Now we can use the `protoc` compiler with the addition of the plugin. First, we create the target directory. Then we run protoc with a few arguments.

The first argument tells the compiler to include any `proto` definitions in the current source tree when compiling. The second instructs the compiler to run the `swagger_out` plugin that will write to `target/swagger` . Lastly, we instruct the compiler to compile each proto file that ends in the same `service`.

::

  $ mkdir -p target/swagger
  $ protoc -Isrc/main/proto \
  --swagger_out=logtostderr=true:target/swagger \
  src/main/proto/ga4gh/*service.proto

This will create a directory (target/swagger/ga4gh) of JSON files describing
the API that can be used with Open API Specification tools like `swagger-codegen <https://github.com/swagger-api/swagger-codegen>`_.


Using Generated Definitions
---------------------------

Swagger documents describe an HTTP interface and the messages it expects in a programmatic manner. This allows developers to use these generated documents to generate code and documentation. To quickly see what the generated documentation might look like, the contents of one the resulting JSON files can be pasted into the online editor at `editor.swagger.io <http://editor.swagger.io/#/>`_.

Using the online interface it is possible to export both client and server stubs in a number of languages. This service exposes the functionality of `swagger-codegen`, which we will install and provide an example of use.

`swagger-codegen` can be installed using `homebrew <http://brew.sh>`_ on a Mac: `brew install swagger-codegen`. The available language bindings can be observed by running `swagger-codegen` from a terminal. Then, to generate a python client for the Read Service we can run:

::

  $ swagger-codegen generate -i target/swagger/ga4gh/read_service.swagger.json -l python -o ga4gh-reads-client

This will create a directory `ga4gh-reads-client` that includes most of the boilerplate, including README, `.gitignore`, etc., required to create a GA4GH client. This client can then be customized, modified, and imported into other projects for use.