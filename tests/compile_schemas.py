"""
Compiles avro schemas into python representations of those schemas
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import glob
import shutil
import os.path
import tempfile
import re

import avro.schema

import utils


class SchemaClass(object):
    """
    Representation of an avro class
    """
    def __init__(self, sourceFile):
        self.sourceFile = sourceFile
        with open(sourceFile) as sf:
            self.schemaSource = sf.read()
            self.schema = avro.schema.parse(self.schemaSource)
        self.name = self.schema.name

    def getFields(self):
        """
        Returns the list of avro fields sorted in order of name.
        """
        return sorted(self.schema.fields, key=lambda f: f.name)

    def isSearchRequest(self):
        """
        Returns True if the class we are converting is a subclass of
        SearchRequest, and False otherwise.
        """
        return re.search('Search.+Request', self.name) is not None

    def isSearchResponse(self):
        """
        Returns True if the class we are converting is a subclass of
        SearchResponse, and False otherwise.
        """
        return re.search('Search.+Response', self.name) is not None


class SchemaProcessor(object):
    """
    Compiles avro schemas into python classes
    """
    def __init__(self, args):
        self.version = args.version
        self.verbosity = args.verbose
        self.tmpDir = tempfile.mkdtemp(prefix="ga4gh_")
        self.avroJarPath = args.avro_tools_jar
        # Note! The tarball does not contain the leading v
        string = "schemas-{0}".format(self.version[1:])
        self.schemaDir = os.path.join(self.tmpDir, string)
        self.avroJar = os.path.join(self.schemaDir, "avro-tools.jar")
        self.avroPath = "src/main/resources/avro"
        self.avdlDirectory = os.path.join(self.schemaDir, self.avroPath)

    def run(self):
        self._getSchemaFromLocal()
        self._compileSchemas()
        self._initClasses()
        self._initPostSignatures()

    def cleanup(self):
        if self.verbosity > 1:
            utils.log("Cleaning up tmp dir {}".format(self.tmpDir))
        shutil.rmtree(self.tmpDir)

    def getClasses(self):
        return self.classes

    def getPostSignatures(self):
        return self.postSignatures

    def _compileSchemas(self):
        url = "http://www.carfab.com/apachesoftware/avro/stable/java/"\
            "avro-tools-1.7.7.jar"
        fileDownloader = utils.FileDownloader(url, self.avroJar)
        fileDownloader.download()
        cwd = os.getcwd()
        os.chdir(self.avdlDirectory)
        for avdlFile in glob.glob("*.avdl"):
            self._convertAvro(avdlFile)
        os.chdir(cwd)

    def _convertAvro(self, avdlFile):
        args = ["java", "-jar", self.avroJar, "idl2schemata", avdlFile]
        if self.verbosity > 0:
            utils.log("converting {}".format(avdlFile))
        if self.verbosity > 1:
            utils.log("running: {}".format(" ".join(args)))
        if self.verbosity > 1:
            utils.runCommandSplits(args)
        else:
            utils.runCommandSplits(args, silent=True)

    def _getSchemaFromLocal(self):
        if not os.path.exists(self.avdlDirectory):
            os.makedirs(self.avdlDirectory)
        avdlFiles = glob.iglob(os.path.join(self.avroPath, "*.avdl"))
        for avdlFile in avdlFiles:
            if os.path.isfile(avdlFile):
                shutil.copy2(avdlFile, self.avdlDirectory)

    def _initClasses(self):
        self.classes = []
        for avscFile in glob.glob(os.path.join(self.avdlDirectory, "*.avsc")):
            self.classes.append(SchemaClass(avscFile))
        self.requestClassNames = [
            cls.name for cls in self.classes if cls.isSearchRequest()]
        self.responseClassNames = [
            cls.name for cls in self.classes if cls.isSearchResponse()]

    def _initPostSignatures(self):
        self.postSignatures = []
        for request, response in zip(
                self.requestClassNames, self.responseClassNames):
            objname = re.search('Search(.+)Request', request).groups()[0]
            url = '/{0}/search'.format(objname.lower())
            tup = (url, request, response)
            self.postSignatures.append(tup)
        self.postSignatures.sort()
