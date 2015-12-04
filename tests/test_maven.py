"""
Runs the maven tests
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import shlex
import subprocess
import unittest

import utils


class TestMaven(unittest.TestCase):
    """
    Uses maven to run tests
    """
    def testMaven(self):
        # ensure the maven tests don't fail or issue warnings
        mvnInstall = \
            "mvn install -DskipTests=true -Dmaven.javadoc.skip=true -B -V"
        self.runCommandCheckWarnings(mvnInstall)
        mvnTest = "mvn test -B"
        self.runCommandCheckWarnings(mvnTest)

    def runCommandCheckWarnings(self, cmd):
        utils.log("Running '{}'".format(cmd))
        splits = shlex.split(cmd)
        output = subprocess.check_output(splits).split('\n')
        utils.ensureNoWarnings(output, cmd)
