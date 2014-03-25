How to contribute to the GA4GH Schemas
======================================

Thank you for taking the time to contribute. We appreciate it!

## Our mailing list

TODO: Put in information about mailing list

## Submit your pull request

Github provides a nice [overview on how to create a pull request](https://help.github.com/articles/creating-a-pull-request).

Some general rules to follow:

* Do your work in [a fork](https://help.github.com/articles/fork-a-repo) of the GA4GH repo.
* Create a branch for each update that you're working on. These branches are often called "feature" or "topic" branches. Any changes
that you push to your feature branch will automatically be shown in the pull request.
* Keep your pull requests as small as possible. Large pull requests are hard to review. Try to break up your changes
into self-contained and incremental pull requests.
* The first line of commit messages should be a short (<80 character) summary, followed by an empty line and then
any details that you want to share about the commit.
* Please try to follow the existing syntax style

When you submit or change your pull request, the Travis build system will automatically run tests
to ensure valid schema syntax. If your pull request fails to pass tests, review the test log, make changes and
then push them to your feature branch to be tested again.
