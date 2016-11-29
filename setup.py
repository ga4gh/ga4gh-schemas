# Don't import __future__ packages here; they make setup fail

# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
import tempfile
import os
import fnmatch
import shutil

import scripts.process_schemas as process_schemas

PROTOCOL_VERSION = "0.6.0a9"

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

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

with open("python/README.pypi.rst") as readmeFile:
    long_description = readmeFile.read()

install_requires = []
with open("python/requirements.txt") as requirementsFile:
    for line in requirementsFile:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinnedVersion = line.split()[0]
        install_requires.append(pinnedVersion)

tempPath = 'package_python'
try:
  shutil.rmtree(tempPath)
except Exception as e:
  print('tempfile directory does not exist, creating...')
shutil.copytree('python', tempPath)
schemasPath = 'src/main/proto/'
createSchemaFiles(tempPath, schemasPath)
process_schemas.main([PROTOCOL_VERSION, tempPath])

setup(
    name="ga4gh_schemas",
    description="GA4GH API Schemas",
    packages=[
        "ga4gh",
        "ga4gh.schemas",
        "ga4gh.schemas.ga4gh",
        "ga4gh.schemas.google",
        "ga4gh.schemas.google.api"
    ],
    namespace_packages=["ga4gh"],
    url="https://github.com/ga4gh/schemas",
    use_scm_version={"write_to": "python/ga4gh/schemas/_version.py"},
    entry_points={},
    package_dir={'': tempPath},
    long_description=long_description,
    install_requires=install_requires,
    license='Apache License 2.0',
    include_package_data=True,
    zip_safe=True,
    author="Global Alliance for Genomics and Health",
    author_email="theglobalalliance@genomicsandhealth.org",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    keywords=['genomics', 'reference'],
    # Use setuptools_scm to set the version number automatically from Git
    setup_requires=['setuptools_scm'],
)

shutil.rmtree('package_python')