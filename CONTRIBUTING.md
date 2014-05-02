## How to contribute to the GA4GH Schemas

----

Thank you for taking the time to contribute. We appreciate it!

There are two ways to contribute to this effort. They first way is to use this project's [Issues Page](https://github.com/ga4gh/ReadTaskTeam/issues), which we use as a forum to discuss both major and minor issues related to developing the GA4GH schemas and API definitions. Examples of the type of issues that can be submitted are: 

* Identify use cases that will shape the standards and APIs
* How to add or delete objects and/or object attributes
* How a particular attribute should be defined
* Report bugs you encounter when using the reference implementations


The [Issues Page](https://github.com/ga4gh/ReadTaskTeam/issues) serves as a public forum to discuss and debate topics related to the proposed standards, formats, and APIs. It also serves as the means for collaborating with the group and making contributions such as proposing changes to the formats and APIs. 

To directly contribute to the project, please refer to the [contributions section](#pull_request) below.

<a name="pull_request"></a>
## Contribute to the GA4GH Reads API Project 

The way to contribute to the project is via Github pull requests. Github provides a nice [overview on how to create a pull request](https://help.github.com/articles/creating-a-pull-request).

Some general rules to follow:

* [Fork](https://help.github.com/articles/fork-a-repo) the main project into your personal Github space to work on.
* Create a branch for each update that you're working on. These branches are often called "feature" or "topic" branches. Any changes that you push to your feature branch will automatically be shown in the pull request.
* Keep your pull requests as small as possible. Large pull requests are hard to review. Try to break up your changes into self-contained and incremental pull requests.
* The first line of commit messages should be a short (<80 character) summary, followed by an empty line and then any details that you want to share about the commit.
* Please try to follow the [existing syntax style](#syntax_style)

When you submit or change your pull request, the Travis build system will automatically run test to ensure valid schema syntax. If your pull request fails to pass tests, review the test log, make changes and then push them to your feature branch to be tested again.

<a name="syntax_style"></a>
## Syntax Style and Conventions

The current code conventions for the source files are as follows: 

* Two-space indentation, no tabs
* `UpperCamelCase` object names
* `lowerCamelCase` attribute or method names
* `CONSTANT_CASE` for global and constant values
* Comments are indented at the same level as the surrounding code
* One-line comments are prefixed using the `// ...` style
* Block and multi-line comments `/* ... */` and subsequent lines must start with `*` aligned with the `*` on the previous line.

