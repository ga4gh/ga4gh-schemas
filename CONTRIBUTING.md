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

### Topic Branches

If you wish to collaborate on a new feature with other GA4GH members, you can ask that a topic branch be created in this repository. Since Github does not allow pull requests against branches that do not yet exist, you will have to create an issue asking for the topic branch to be created.

Once the topic branch exists, pull requests can be made against it in the usual way. It may also be brought up to date with new changes merged into master by anyone with commit access, if the changes produce merely a fast-forward merge. However, if changes from the master branch create a new merge commit, that commit needs to be reviewed in a pull request.

Changes made in a topic branch can be merged into master by creating and then [resolving in the normal way](#issue_resolution) a pull request against the master branch.

<a name="issue_resolution"></a>
## Issue Resolution

Once a pull request or issue have been submitted, anyone can comment or vote on an issue to express their opinion following the Apache voting system. Quick summary:

- **+1** something you agree with
- **-1** if you have a strong objection to an issue, which will be taken very seriously. A -1 vote should provide an alternative solution.
- **+0** or **-0** for neutral comments or weak opinions.
- It's okay to have input without voting
- Silence gives assent

A pull request with at least two **+1** votes, no **-1** votes, and that has been open for at least 3 days, is ready to be merged. The merge should be done by someone from a different organization than the submitter. (We sometimes waive the 3 days for cosmetic-only changes -- use good judgment.)

If an issue gets any **-1** votes, the comments on the issue need to reach consensus before the issue can be resolved one way or the other. There isn't any strict time limit on a contentious issue.

The project will strive for full consensus on everything until it runs into a problem with that model.

<a name="syntax_style"></a>
## Syntax Style and Conventions

The current code conventions for the source files are as follows:

* Use two-space indentation, and no tabs.
* Hard-wrap code to 80 characters per line.
* Use `UpperCamelCase` for object or record names.
* Use `lowerCamelCase` for attribute or method names.
* Use `CONSTANT_CASE` for global and constant values.
* Comments:
     * Comments should be indented at the same level as the surrounding code.
     * Comments should precede the code that they make a comment on.
       Documentation comments will not work otherwise.
     * Documentation comments, which are intended to be processed by avrodoc and
       displayed in the user-facing API documentation, must use the `/** ... */`
       style, and must not have a leading `*` on each internal line:
        
        ````
        /** 
        This documentation comment will be
        processed correctly by avrodoc.
        */
        ````

        ````
        /**
         * This documentation comment will have a
         * bullet point at the start of every line
         * when processed by avrodoc.
         */
        ````
        
     * Block and multi-line non-documentation comments, intended for schema
       developers only, must use the `/* ... */` style.
     
        ````
        /*
        This multi-line comment will not appear in the
        avrodoc documentation and is intended for
        schema developers.
        */
        ````
     
     * All multi-line comments should have the comment text at the same indent
       level as the comment delimeters.
     * One-line non-documentation comments, intended for schema developers only,
       must use the `// ...` style.

<a name="retired_task_teams"></a>
## Retired Task Teams

As projects mature, the need to have a standing [Data Working Group](http://ga4gh.org) task team with regular teleconferences and meetings will decline. Mature task teams will enter a *maintenance mode which will entail the following:

* A task team chair will be appointed to regularly review the `ga4gh#schemas` Github Issues for issue that would effect the outcomes of the retired task team
* The task team chair will tag those issues with the retired group's label
* Minor pull requests (e.g. documentation enhancements) would follow the same [issue resolution](#issue_resolution) process as outlined above
* Major pull requeusts (e.g. API additions or changes) would be escalated for approval by a larger group that *must* vote in on the issue for it to come to consensus

Issue escalation would proceed as follows: 

* The retired task team chair will label the issue as "Major Enchancement"
* The retired task team chair will add a **-1** vote on the issue and list the members of the community that must vote **+1** to remove the associated **-1** vote
* The retired task team chair will reach out to that list of DWG members and request comment on the issue
* [Issue resolution](#issue_resolution) will proceed as normal from there

