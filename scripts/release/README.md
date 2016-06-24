Notes for release managers
---

This document describes how to make a GA4GH schemas release.

Setup your environment
1. Copy (or incorporate) the settings.xml file to ```~/.m2/settings.xml```
2. Create a GPG key, and add it to KEYS. Review [the Maven guidelines on working
with keys](http://central.sonatype.org/pages/working-with-pgp-signatures.html),
as there are gotcha's related to working with primary vs. sub keys, and
distributing your keys.
3. Edit the username, password, etc in ```~/.m2/settings.xml```

Once your environment is setup, you'll be able to do a release.

Then from the project root directory, run `./scripts/release/release.sh`.
If you have any problems, run `./scripts/release/rollback.sh`.

Once you've successfully published the release, you will need to "close" and "release" it following the instructions at
http://central.sonatype.org/pages/releasing-the-deployment.html#close-and-drop-or-release-your-staging-repository

After the release is rsynced to the Maven Central repository, confirm checksums match and verify signatures.
