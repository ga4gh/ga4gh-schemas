###########
Development
###########



***************
Release process
***************

There are two types of releases: development releases, and stable
bugfix releases. Development releases happen as a matter of
course while we are working on a given minor version series, and
may be either a result of some new features being ready for use
or a minor bugfix. Stable bugfix releases occur when mainline development
has moved on to another minor version, and a bugfix is required for the
currently released version. These two cases are handled in different
ways.

+++++++++++++++++++++++++++
Development Python releases
+++++++++++++++++++++++++++

Version numbers are MAJOR.MINOR.PATCH triples. Minor version increments
happen when significant changes are required to the schema codebase,
which will result in a significant departure from the previously
released version, either in code layout or in functionality. During
the normal process of development within a minor version series,
patch updates are routinely and regularly released.  (In some cases bugfix
releases can also come with a suffix, e.g. ``0.6.0a9.post1``.)

Making a release entails the following steps:

#. Create a PR against ``master`` that has the following changes:

   #. update the release notes in ``doc/source/changelog.rst`` with a description of what is in the release
   #. modify ``python/requirements.txt`` to pin the ga4gh-common package to a specific version
   #. modify ``python/constraints.txt`` to comment out all the lines referencing ga4gh packages
   #. modify ``python/constraints.txt.default`` to have the identical contents as ``python/constraints.txt``

#. Once this has been merged, tag the release on GitHub (on the `releases
   <https://github.com/ga4gh/schemas/releases>`_ page) with the
   appropriate version number.
#. Fetch the tag from the upstream repo, and checkout this tag.
#. Create the distribution tarball using ``python setup.py sdist``, and then
   upload the resulting tarball to PyPI using
   ``twine upload dist/ga4gh-schemas-$MAJOR.$MINOR.$PATCH.tar.gz`` (using
   the correct file name).
#. Verify that the documentation at
   https://readthedocs.org/projects/ga4gh-schemas/en/stable/
   is for the correct version (it may take a few minutes for this to
   happen after the release has been tagged on GitHub).  The release
   notes docs should have changed, so that is a good section to look at
   to confirm the change.

All of the above steps after the tag is dropped on the target commit are now
`automated <https://docs.travis-ci.com/user/deployment/pypi/>`_ using
Travis' capability to deploy to Pypi.

When releasing the package to PyPi, the release manager should guarantee the
protocol version in ``setup.py`` matches the protocol version being released.

Since PyPi and the source code may provide different minor versions, release
notes for the PyPi package are maintained in ``python/README.rst``.

+++++++++++++++++++++
Stable bugfix release
+++++++++++++++++++++

When a minor version series has ended because of some significant shift
in the server internals, there will be a period when the ``master`` branch is not
in a releasable state. If a bugfix release is required during this period,
we create a release using the following process:

#. If it does not already exist, create a release branch called
   ``release-$MAJOR.$MINOR`` from the tag of the last release.
#. Fix the bug by either cherry picking the relevant commits
   from ``master``, or creating PRs against the ``release-$MAJOR.$MINOR``
   branch if the bug does not apply to ``master``.
#. Follow steps 1-5 in the process for `Development releases`_ above,
   except using the ``release-$MAJOR.$MINOR`` branch as the base
   instead of ``master``.
