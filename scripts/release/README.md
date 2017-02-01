Notes for release managers
---

This document describes how to make a GA4GH schemas release.

Prerequisites:
1. Create a GPG key. Review [the Maven guidelines on working
with keys](http://central.sonatype.org/pages/working-with-pgp-signatures.html),
Setup your environment (add it to keys).
2. Obtain a sonatype login (request from the project manager).

Setup:
1. Add the GPG key to the KEYS file.
1. Copy (or incorporate) the settings.xml file to ```~/.m2/settings.xml``` and
   add your GPG key and sonatype login.

Release:
1. Update the version in pom.xml.
2. mvn deploy
3. From oss.sontaype.org#stagingRepositories, login and check the release just
   uploaded. If good, use the close button above the repository list to make it
   public. If there is a problem, the drop button will delete the release.

