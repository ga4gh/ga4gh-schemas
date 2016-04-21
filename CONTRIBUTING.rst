How to contribute to the GA4GH Schemas
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Thank you for taking the time to contribute. We appreciate it!

The GA4GH schemas define an API for sharing genomic and phenotypic
data.  Supporting the schemas is a `reference server
<https://github.com/ga4gh/server>`__, which acts as a useful, complete
implementation of the API, and a `compliance suite
<https://github.com/ga4gh/compliance>`__, which provides data and
functions to test an API implementation. Development of these three
aspects of the project are coordinated, so that changes to the schemas
are reflected in the creation of a working prototype within the
reference server and compliance tests that establish conformance.
Coordination in this way ensures the alliance is building software and
standards that work for genomics.

There are two ways to contribute to the effort - via issues, which are
used for discussion, and pull requests, which are concrete proposals of
change.

Issues
@@@@@@

The project's `Issues Page
<https://github.com/ga4gh/schemas/issues>`__ is a forum to discuss
both major and minor issues related to developing the standards,
formats, and APIs. It also serves as the means for collaborating with
the group and discussing contributions that will ultimately lead to
changes to the formats and APIs. See the `Issue <#issue_resolution>`__
section below for specifics on how issues are resolved by the
community. Examples of the type of issues that can be submitted are:

-  Identify use cases that will shape the standards and APIs
-  How to add or delete objects and/or object attributes
-  How a particular attribute should be defined
-  Report bugs you encounter when using the reference implementations

Pull Requests
@@@@@@@@@@@@@

The way to contribute development effort and code to the project is via
GitHub pull requests. GitHub provides a nice `overview on how to create
a pull
request <https://help.github.com/articles/creating-a-pull-request>`__.
Contributions typically require pull requests to each of the schemas,
server and compliance repositories, although pull requests to the server
may merely improve the code without affecting the API, and therefore
changing the schemas or compliance tests. A set of branches across the
repositories each with the same name is a branch set, e.g. the master
branch in each repository forms the master branch set.

Some general rules to follow:

- `Fork <https://help.github.com/articles/fork-a-repo>`__ the main
  project into your personal GitHub space to work on.
- Create a branch for each update that you're working on. These
  branches are often called "feature" or "topic" branches. Any changes
  that you push to your feature branch will automatically be shown in
  the pull request.
- If necessary, replicate the last two steps' fork-and-branch process
  for each of the compliance and server repositories to create a
  branch set - each constituent repository branch will be identically
  named.
- Coordinate pull requests across the branch set by making them as
  simultaneously as possible, and `cross referencing them
  <http://stackoverflow.com/questions/23019608/github-commit-syntax-to-link-a-pull-request-issue>`__.
- Keep your pull requests as small as possible. Large pull requests
  are hard to review. Try to break up your changes into self-contained
  and incremental pull requests.
- The first line of commit messages should be a short (<80 character)
  summary, followed by an empty line and then any details that you
  want to share about the commit.
- Please try to follow the `existing syntax style <#syntax_style>`__

When you submit or change your pull request, the Travis build system
will automatically run tests to ensure valid schema syntax. If your
pull request fails to pass tests, review the test log, make changes
and then push them to your feature branch to be tested again.

Issue Resolution
@@@@@@@@@@@@@@@@

Once a pull request or issue have been submitted, anyone can comment or
vote on to express their opinion following the Apache voting system.
Quick summary:

- **+1** something you agree with
- **-1** if you have a strong objection to an issue, which will be
  taken very seriously. A -1 vote should provide an alternative
  solution.
- **+0** or **-0** for neutral comments or weak opinions.
- It's okay to have input without voting
- Silence gives assent

A pull request with at least two **+1** votes, no **-1** votes, that has
been open for at least 3 days, and whose cross-referenced pull requests
to server and compliance have similarly been upvoted is ready to be
merged. The merge should be done by someone from a different
organization than the submitter. (We sometimes waive the 3 days for
cosmetic-only changes -- use good judgment.) A pull request to either
the schemas, servers or compliance repository that involves changes to
the others should not be merged without coordinating, mergable pull
requests to the other repositories. Conversely, when merging a pull
request the other pull requests in the branch set must be merged at the
same time (In practise, when merging a branch set including the schemas
repository, merge the pull request to schemas first to avoid the
continuous integration build issues). If an issue gets any **-1** votes,
the comments on the issue need to reach consensus before the issue can
be resolved one way or the other. There isn't any strict time limit on a
contentious issue.

The project will strive for full consensus on everything until it runs
into a problem with this model.

Syntax Style and Conventions
@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The current code conventions for the source files are as follows:

- Use two-space indentation, and no tabs.
- Hard-wrap code to 80 characters per line.
- Use ``UpperCamelCase`` for object or record names.
- Use ``lowerCamelCase`` for attribute or method names.
- Use ``CONSTANT_CASE`` for global and constant values.
- Comments:

  - Comments should be indented at the same level as the surrounding
    code.
  - Comments should precede the code that they make a comment on.
    Documentation comments will not work otherwise.
  - Documentation comments, which are intended to be processed by
    avrodoc and displayed in the user-facing API documentation, must use
    the ``/** ... */`` style, and must not have a leading ``*`` on each
    internal line:

    ::

       /**
       This documentation comment will be
       processed correctly by avrodoc.
       */

    ::

       /**
       * This documentation comment will have a
       * bullet point at the start of every line
       * when processed by avrodoc.
       */

  - Block and multi-line non-documentation comments, intended for schema
    developers only, must use the ``/* ... */`` style.

    ::

       /*
       This multi-line comment will not appear in the
       avrodoc documentation and is intended for
       schema developers.
       */

  - All multi-line comments should have the comment text at the same
    indent level as the comment delimeters.
  - One-line non-documentation comments, intended for schema developers
    only, must use the ``// ...`` style.
  - Comments may use `reStructuredText
    <http://docutils.sourceforge.net/rst.html>`__ mark up.

Documentation
@@@@@@@@@@@@@

The goal of GA4GH is to define an interoperable API specification.  To achieve
this, the intent, rationale, and semantics of all data objects and operations
need to be clearly and precisely defined. Decisions that are not captured in
documentation are lost.

All schemas defined in GA4GH must include normative documentation.  This
should consist of overview and design documentation as well as documentation
in the schemas.  This documentation should explain the goals, overall design,
and rationale for decisions that were made.  It must be addressed to both
client and server developer audiences.  It may cite published papers or stable
web documentation.

Overview documentation should be in ReStructuredText markdown format
(`*.rst`) in the `doc/source/` directory.  This format was chosen for inclusion
in a Sphinx-based documentation system that is under development.
Graphics are encouraged and should have a source to drawings in
SVG format that will be converted to PNG by the documentation build.

Developers are encouraged to get feedback on design documentation before
developing and implementing schemas.

Topic Branches
@@@@@@@@@@@@@@

If you wish to collaborate on a new feature with other GA4GH members you
can ask that a topic branch set be created. This will generally involve
the creation of identically named topic branches for each of the schema,
compliance and server repositories. Since Github does not allow pull
requests against branches that do not yet exist, you will have to create
an issue asking for the topic branch set to be created.

Once a topic branch set exists, pull requests can be made against it in
the usual way. It may also be brought up to date with new changes merged
into master by anyone with commit access, if the changes produce merely
a fast-forward merge for each constituent branch. However, if changes
from the master branch create a new merge commit in or or more of the
repositories, that commit needs to be reviewed in a pull request.

Changes made in a topic branch set can be merged into master by creating
and then `resolving in the normal way <#issue_resolution>`__ a pull
request against the master branch set, irrespective of ownership by a
task-team (see below) or not.

Topic branch sets that have been merged into master and that are no
longer being developed upon should be `deleted
<https://github.com/blog/1335-tidying-up-after-pull-requests>`__ (they
will still appear in the git history), this can be achieved by
consensus of those working on the topic branch set, e.g. a specific
task-team.

Task Team Topic Branch Sets
###########################

Frequently topic branch sets are developed by members working within a
task team of the `Data Working Group <http://ga4gh.org>`__. Topic
branch sets developed by a task team should be prefixed with the task
team's name followed by a dash, e.g. reads-foo, refVar-bar. To enable
speedy development, task-teams may set their own rules for
contribution to the topic branch sets they own. This allows task-teams
to develop features in the view of the larger group, while potentially
being unencumbered by the more lengthy process of standard `issue
resolution <#issue%20resolution>`__.

Release Branches
@@@@@@@@@@@@@@@@

From time to time the group will make a release. This is achieved by
creating a branch set including all the repositories named
"release-foo", where foo is the release name. Only bug fixes are allowed
to release branch sets. To refer to a specific version of a release
branch set either the commit id can be used, or alternatively (better),
a tag can be created (which should be replicated across repositories).

Retired Task Teams
@@@@@@@@@@@@@@@@@@

As projects mature, the need to have a standing `Data Working
Group <http://ga4gh.org>`__ task team with regular teleconferences and
meetings will decline. Mature task teams will enter a \*maintenance mode
which will entail the following:

- A task team chair will be appointed to regularly review the
  ``ga4gh#schemas`` Github Issues for issue that would effect the
  outcomes of the retired task team.
- The task team chair will tag those issues with the retired group's
  label.
- Minor pull requests (e.g. documentation enhancements) would follow
  the same `issue resolution <#issue_resolution>`__ process as
  outlined above.
- Major pull requeusts (e.g. API additions or changes) would be
  additionally labeled 'major change', and the retired task team chair
  will reach out to that list of DWG members and request comment on
  the issue.
