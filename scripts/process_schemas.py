"""
A script to generate the schemas for the GA4GH protocol. These are generated
from a copy of the Protocol Buffers schema and use it to generate
the Python class definitions. These are also stored in revision
control to aid Travis building.
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import os.path
import subprocess
import fnmatch
import re
import argparse
import shlex


def createSchemaFiles(tempPath, schemasPath):
    """
    Create a hierarchy of proto files in a temporary directory, copied
    from the schemasPath hierarchy
    """
    ga4ghPath = os.path.join(tempPath, 'ga4gh')
    ga4ghSchemasPath = os.path.join(ga4ghPath, 'schemas')
    for root, dirs, files in os.walk(schemasPath):
        for protoFilePath in fnmatch.filter(files, '*.proto'):
            src = os.path.join(root, protoFilePath)
            dst = os.path.join(
                ga4ghSchemasPath,
                os.path.relpath(root, schemasPath), protoFilePath)
            copySchemaFile(src, dst)


def doLineReplacements(line):
    """
    Given a line of a proto file, replace the line with one that is
    appropriate for the hierarchy that we want to compile
    """
    # ga4gh packages
    packageString = 'package ga4gh;'
    if packageString in line:
        return line.replace(
            packageString,
            'package ga4gh.schemas.ga4gh;')
    importString = 'import "ga4gh/'
    if importString in line:
        return line.replace(
            importString,
            'import "ga4gh/schemas/ga4gh/')
    # google packages
    googlePackageString = 'package google.api;'
    if googlePackageString in line:
        return line.replace(
            googlePackageString,
            'package ga4gh.schemas.google.api;')
    googleImportString = 'import "google/api/'
    if googleImportString in line:
        return line.replace(
            googleImportString,
            'import "ga4gh/schemas/google/api/')
    optionString = 'option (google.api.http)'
    if optionString in line:
        return line.replace(
            optionString,
            'option (.ga4gh.schemas.google.api.http)')
    return line


def copySchemaFile(src, dst):
    """
    Copy a proto file to the temporary directory, with appropriate
    line replacements
    """
    with open(src) as srcFile, open(dst, 'w') as dstFile:
        srcLines = srcFile.readlines()
        for srcLine in srcLines:
            toWrite = doLineReplacements(srcLine)
            dstFile.write(toWrite)


def runCommandSplits(splits, silent=False, shell=False):
    """
    Run a shell command given the command's parsed command line
    """
    try:
        if silent:
            with open(os.devnull, 'w') as devnull:
                subprocess.check_call(
                    splits, stdout=devnull, stderr=devnull, shell=shell)
        else:
            subprocess.check_call(splits, shell=shell)
    except OSError, e:
        if e.errno == 2:  # cmd not found
            raise Exception(
                "Can't find command while trying to run {}".format(splits))
        else:
            raise


def runCommand(command, silent=False, shell=False):
    """
    Run a shell command
    """
    splits = shlex.split(command)
    runCommandSplits(splits, silent=silent, shell=shell)


class ProtobufGenerator(object):

    def __init__(self, version):
        self.version = version

    def _assertSchemasExist(self, schemas_path):
        if not os.path.exists(schemas_path):
            raise Exception(
                "Can't find schemas folder. " +
                "Thought it would be at {}".format(
                    os.path.realpath(schemas_path)))

    def _assertProtoDirectoryExists(self, source_path):
        if not os.path.exists(source_path):
            msg = "Can't find source proto directory {}".format(
                os.path.realpath(source_path))
            raise Exception(msg)

    def _find_in_path(self, cmd):
        PATH = os.environ.get("PATH", os.defpath).split(os.pathsep)
        for x in PATH:
            possible = os.path.join(x, cmd)
            if os.path.exists(possible):
                return possible
        return None

    # From http://stackoverflow.com/a/1714190/320546
    def _version_compare(self, version1, version2):
        def normalize(v):
            return [int(x) for x in re.sub(r'(\.0+)*$', '', v).split(".")]
        return cmp(normalize(version1), normalize(version2))

    def _getProtoc(self, destination_path):
        protocs = [
            os.path.realpath(x) for x in
            "{}/protobuf/src/protoc".format(destination_path),
            self._find_in_path("protoc")
            if x is not None]
        protoc = None
        for c in protocs:
            if not os.path.exists(c):
                continue
            output = subprocess.check_output([c, "--version"]).strip()
            try:
                (lib, version) = output.split(" ")
                if lib != "libprotoc":
                    raise Exception("lib didn't match 'libprotoc'")
                if self._version_compare("3.0.0", version) > 0:
                    raise Exception("version < 3.0.0")
                protoc = c
                break
            except Exception:
                print(
                    "Not using {path} because it returned " +
                    "'{version}' rather than \"libprotoc <version>\", where " +
                    "<version> >= 3.0.0").format(path=c, format=output)

        if protoc is None:
            raise Exception("Can't find a good protoc. Tried {}".format(
                protocs))
        print("Using protoc: '{}'".format(protoc))
        return protoc

    def _writePythonFiles(self, source_path, protoc, destination_path):
        protos = []
        for root, dirs, files in os.walk(source_path):
            protos.extend([
                os.path.join(root, f)
                for f in fnmatch.filter(files, "*.proto")])
        if len(protos) == 0:
            raise Exception(
                "Didn't find any proto files in ".format(source_path))
        print("Proto files source: '{}'".format(source_path))
        print("pb2 files destination: '{}'".format(destination_path))
        cmdString = (
            "{protoc} -I {source_path} -I ./src/main "
            "--python_out={destination_path} {proto_files}")
        cmd = cmdString.format(
            protoc=protoc, source_path=source_path,
            destination_path=destination_path,
            proto_files=" ".join(protos))
        runCommand(cmd)
        print("{} pb2 files written".format(len(protos)))

    def _writeVersionFile(self):
        versionFilePath = "python/ga4gh/schemas/_protocol_version.py"
        with open(versionFilePath, "w") as version_file:
            version_file.write(
                "# File generated by scripts/process_schemas.py; "
                "do not edit\n")
            version_file.write("version = '{}'\n".format(self.version))

    def run(self, args):
        script_path = os.path.dirname(os.path.realpath(__file__))
        destination_path = os.path.realpath(
            os.path.join(script_path, args.destpath))
        schemas_path = os.path.realpath(args.schemapath)
        protoc = self._getProtoc(destination_path)
        self._writePythonFiles(schemas_path, protoc, destination_path)
        self._writeVersionFile()


def main(args=None):
    defaultDestPath = "../python/"
    parser = argparse.ArgumentParser(
        description="Script to process GA4GH Protocol buffer schemas")
    parser.add_argument(
        "version", help="Version number of the schema we're compiling")
    parser.add_argument(
        "schemapath",
        help="Path to schemas.")
    parser.add_argument(
        "-d", "--destpath", default=defaultDestPath,
        help=(
            "the directory in which to write the compiled schema files "
            "(defaults to {})".format(defaultDestPath)))
    parsedArgs = parser.parse_args(args)
    pb = ProtobufGenerator(parsedArgs.version)
    pb.run(parsedArgs)


if __name__ == "__main__":
    main()
