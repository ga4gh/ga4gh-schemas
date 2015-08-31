# Generating API Documentation

----

## Install prerequisites
To use the Sphinx/Avro documentation generator, you must install some software package prerequisites.


#### Java
We use a small Java program to process the schemas.

##### Ubuntu

```
$ sudo apt-get install openjdk-7-jre-headless
```

##### CentOS/Fedora

```
$ sudo yum install java-1.7.0-openjdk-devel
```

##### Mac OS X

Download the `Java SE Development Kit 8` from [here](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).
Double-click the `.dmg` disk image file and follow the installation instructions.

#### Python/PIP
We use some Python utility programs also.

Install the Python installer `pip`.

##### Ubuntu
```
$ sudo apt-get install python-pip
```

##### CentOS/Fedora
```
$ sudo yum install python-pip
```

##### Mac OS X

Download `pip` from [here](https://bootstrap.pypa.io/get-pip.py) and run it:

```
$ python get-pip.py
```

__Running it__: Do this once to install all required Python packages:

```
$ sudo pip install -r requirements.txt
```

## Generate the documentation

With those prerequisites out of the way, do this anytime you wish to generate the documentation:

```
$ cd sphinx
$ ./generate_sphinx_docs.sh
```
