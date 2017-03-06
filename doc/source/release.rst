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

++++++++++++++++++++
Development releases
++++++++++++++++++++

Version numbers are MAJOR.MINOR.PATCH triples. Minor version increments
happen when significant changes are required to the server codebase,
which will result in a significant departure from the previously
released version, either in code layout or in functionality. During
the normal process of development within a minor version series,
patch updates are routinely and regularly released.  (In some cases bugfix
releases can also come with a suffix, e.g. ``0.6.0a9.post1``.)

Making a release entails the following steps:

#. Create a PR against ``master`` that has the following changes:

   #. update the release notes in ``docs/status.rst`` with a description of what is in the release
   #. modify ``requirements.txt`` to pin the ga4gh packages to specific versions
   #. modify ``constraints.txt`` to comment out all the lines referencing ga4gh packages
   #. modify ``docs/environment.yml`` to pin the ga4gh packages to specific versions

#. Once this has been merged, tag the release on GitHub (on the `releases
   <https://github.com/ga4gh/server/releases>`_ page) with the
   appropriate version number.
#. Fetch the tag from the upstream repo, and checkout this tag.
#. Create the distribution tarball using ``python setup.py sdist``, and then
   upload the resulting tarball to PyPI using
   ``twine upload dist/ga4gh-$MAJOR.$MINOR.$PATCH.tar.gz`` (using
   the correct file name).
#. Verify that the documentation at
   http://ga4gh-reference-implementation.readthedocs.org/en/stable/
   is for the correct version (it may take a few minutes for this to
   happen after the release has been tagged on GitHub).  The release
   notes docs should have changed, so that is a good section to look at
   to confirm the change.

All of the above steps after the tag is dropped on the target commit are now
`automated <https://docs.travis-ci.com/user/deployment/pypi/>`_ using
Travis' capability to deploy to Pypi.

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
