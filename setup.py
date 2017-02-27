# Don't import __future__ packages here; they make setup fail

import scripts.process_schemas as process_schemas

PROTOCOL_VERSION = "0.6.0a9"

# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

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

dependency_links = []
try:
    with open("python/constraints.txt") as constraintsFile:
        for line in constraintsFile:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            dependency_links.append(line)
except EnvironmentError:
    print('No constraints file found, proceeding without '
          'creating dependency links.')

try:
    process_schemas.main([PROTOCOL_VERSION])
except Exception:
    print("Couldn't find a good protoc, using precompiled protobuf.")

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
    package_dir={'': 'python'},
    long_description=long_description,
    install_requires=install_requires,
    dependency_links=dependency_links,
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
