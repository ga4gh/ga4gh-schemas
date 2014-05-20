## How to contribute to the GA4GH Schemas

Thank you for taking the time to contribute. We appreciate it!

There are two ways to contribute to this effort. The first way is to use this project's [Issues Page](https://github.com/ga4gh/ReadTaskTeam/issues), which we use as a forum to discuss both major and minor issues related to developing the GA4GH schemas and API definitions. Examples of the type of issues that can be submitted are:

* Identify use cases that will shape the standards and APIs
* How to add or delete objects and/or object attributes
* How a particular attribute should be defined
* Report bugs you encounter when using the reference implementations


The [Issues Page](https://github.com/ga4gh/ReadTaskTeam/issues) serves as a public forum to discuss and debate topics related to the proposed standards, formats, and APIs. It also serves as the means for collaborating with the group and making contributions such as proposing changes to the formats and APIs. See the [Issue Resolution](#issue_resolution) section below for specifics on how issues are resolved by the community.

A second way to contribute to the project is to directly contribute development effort. Please refer to the next section, [Contributions and Pull Request](#pull_request), for more details.

<a name="pull_request"></a>
## Contributions and Pull Requests

The way to contribute development effort and code to the project is via GitHub pull requests. GitHub provides a nice [overview on how to create a pull request](https://help.github.com/articles/creating-a-pull-request).

Some general rules to follow:

* [Fork](https://help.github.com/articles/fork-a-repo) the main project into your personal GitHub space to work on.
* Create a branch for each update that you're working on. These branches are often called "feature" or "topic" branches. Any changes that you push to your feature branch will automatically be shown in the pull request.
* Keep your pull requests as small as possible. Large pull requests are hard to review. Try to break up your changes into self-contained and incremental pull requests.
* The first line of commit messages should be a short (<80 character) summary, followed by an empty line and then any details that you want to share about the commit.
* Please try to follow the [existing syntax style](#syntax_style)

When you submit or change your pull request, the Travis build system will automatically run tests to ensure valid schema syntax. If your pull request fails to pass tests, review the test log, make changes and then push them to your feature branch to be tested again.


<a name="issue_resolution"></a>
## Issue Resolution

Once a pull request or issue have been submitted, anyone can comment or vote on an issue to express their opinion following the Apache voting system. Quick summary:

- **+1** something you agree with
- **-1** if you have a strong objection to an issue, which will be taken very seriously. A -1 vote should provide an alternative solution.
- **+0** or **-0** for neutral comments or weak opinions.
- It's okay to have input without voting
- Silence gives assent

A pull request with at least two **+1** votes, and no **-1** votes, is ready to be merged. The merge should be done by someone from a different organization than the submitter.

If an issue gets any **-1** votes, the comments on the issue need to reach consensus before the issue can be resolved one way or the other. There isn't any strict time limit on a contentious issue.

The project will strive for full consensus on everything until it runs into a problem with that model.

<a name="syntax_style"></a>
## Syntax Style and Conventions

The current code conventions for the source files are as follows:

* Two-space indentation, no tabs
* `UpperCamelCase` for object or record names
* `lowerCamelCase` attribute or method names
* `CONSTANT_CASE` for global and constant values
* Comments:
     * Indented at the same level as the surrounding code
     * Precede the code that they make a comment on
     * Documentation comments use the `/** ... */` style
     * Block and multi-line comments must use the `/** ... */` style.
     * One-line comments prefixed using the `// ...` style will not be output to documentation and are intended for developers of the project only
