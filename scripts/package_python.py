"""
Creates a python pacakge of the current schemas compiled to python files
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import fnmatch
import os
import tempfile
from distutils.core import run_setup

import process_schemas


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


def createSchemaFiles(tempPath, schemasPath):
    """
    Create a hierarchy of proto files in a temporary directory, copied
    from the schemasPath hierarchy
    """
    ga4ghPath = os.path.join(tempPath, 'ga4gh')
    os.mkdir(ga4ghPath)
    ga4ghSchemasPath = os.path.join(ga4ghPath, 'schemas')
    os.mkdir(ga4ghSchemasPath)
    for root, dirs, files in os.walk(schemasPath):
        for dirPath in dirs:
            newDir = os.path.join(
                ga4ghSchemasPath,
                os.path.relpath(root, schemasPath), dirPath)
            os.mkdir(newDir)
        for protoFilePath in fnmatch.filter(files, '*.proto'):
            src = os.path.join(root, protoFilePath)
            dst = os.path.join(
                ga4ghSchemasPath,
                os.path.relpath(root, schemasPath), protoFilePath)
            copySchemaFile(src, dst)


def createPackage(wheel):
    """
    Invoke setup.py to create a package
    """
    if wheel:
        script_args = ['bdist_wheel', '--universal']
    else:
        script_args = ['sdist']
    run_setup('setup.py', script_args=script_args)


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Script to create a python package of the schemas")
    parser.add_argument(
        "version", help="Version number of the schema we're compiling")
    parser.add_argument(
        "--wheel", "-w", action="store_true",
        help="build a universal wheel instead of an sdist archive")
    parsedArgs = parser.parse_args(args)

    # create modified proto files in a temporary directory
    tempPath = tempfile.mkdtemp('package_python')
    schemasPath = 'src/main/proto/'
    createSchemaFiles(tempPath, schemasPath)

    # create *_pb2.py files under the python directory
    process_schemas.main([parsedArgs.version, tempPath])

    # create a package
    createPackage(parsedArgs.wheel)


if __name__ == '__main__':
    main()
