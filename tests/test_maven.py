"""
Runs the maven tests
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import shlex
import subprocess
import unittest

import ga4gh.common.utils as utils


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
        self.ensureNoWarnings(output, cmd)

    def ensureNoWarnings(self, lines, streamName):
        pattern = '[WARNING]'
        matchingLines = []
        for line in lines:
            if pattern in line:
                matchingLines.append(line[:-1])
        if len(matchingLines) != 0:
            raise Exception("warning(s) detected in {}:\n{}".format(
                streamName, '\n'.join(matchingLines)))
