# Don't import __future__ packages here; they make setup fail

# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

# this is a hack that allows us to run setup from the root schemas dir;
# it's better to run it from the python dir
import os
if os.path.split(os.getcwd())[1] != 'python':
    os.chdir('python')

with open("README.pypi.rst") as readmeFile:
    long_description = readmeFile.read()

install_requires = []
with open("requirements.txt") as requirementsFile:
    for line in requirementsFile:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinnedVersion = line.split()[0]
        install_requires.append(pinnedVersion)

setup(
    # END BOILERPLATE
    name="ga4gh_schemas",
    description="GA4GH api schemas",
    packages=[
        "ga4gh",
        "ga4gh.schemas",
        "ga4gh.schemas.elgoog",
        "ga4gh.schemas.elgoog.api",
    ],
    namespace_packages=["ga4gh"],
    url="https://github.com/ga4gh/schemas",
    use_scm_version={"write_to": "python/ga4gh/schemas/_version.py",
        "root": ".."},
    entry_points={},
    # BEGIN BOILERPLATE
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
