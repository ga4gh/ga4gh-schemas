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

import process_schemas

# run setup
# change travis


def doLineReplacements(line):
    if 'package ga4gh;' in line:
        return line.replace(
            'package ga4gh;',
            'package ga4gh.schemas.ga4gh;')
    if 'package google.api;' in line:
        return line.replace(
            'package google.api;',
            'package ga4gh.schemas.google.api;')
    if 'import "ga4gh/' in line:
        return line.replace(
            'import "ga4gh/',
            'import "ga4gh/schemas/ga4gh/')
    if 'import "google/api/' in line:
        return line.replace(
            'import "google/api/',
            'import "ga4gh/schemas/google/api/')
    if 'option (google.api.http)' in line:
        return line.replace(
            'option (google.api.http)',
            'option (.ga4gh.schemas.google.api.http)')
    return line


def copySchemaFile(src, dst):
    with open(src) as srcFile, open(dst, 'w') as dstFile:
        srcLines = srcFile.readlines()
        for srcLine in srcLines:
            toWrite = doLineReplacements(srcLine)
            dstFile.write(toWrite)


def createSchemaFiles(tempPath, schemasPath):
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


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Script to create a python package of the schemas")
    parser.add_argument(
        "version", help="Version number of the schema we're compiling")
    parsedArgs = parser.parse_args(args)

    # create modified proto files in a temporary directory
    tempPath = tempfile.mkdtemp('package_python')
    schemasPath = 'src/main/proto/'
    createSchemaFiles(tempPath, schemasPath)

    # create *_pb2.py files under the python directory
    process_schemas.main([parsedArgs.version, tempPath])

    # run sdist
    from distutils.core import run_setup
    os.chdir('python')
    run_setup('setup.py', script_args=['sdist'])


if __name__ == '__main__':
    main()
