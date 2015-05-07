"""
Script to imitate a Travis CI run
"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import glob
import shlex
import subprocess

import yaml

import utils


class TravisSimulator(object):

    logStrPrefix = '***'

    yamlFileLocation = '.travis.yml'

    def parseTestCommands(self):
        yamlFile = file(self.yamlFileLocation)
        yamlData = yaml.load(yamlFile)
        return yamlData['script']

    def expandCommand(self, command):
        # subprocess.check_call doesn't expand globs by default, unless
        # shell=True is passed, which is a security hazzard.
        # This gets around that limitation by implementing some shell features
        # which should be enough for our purposes.  See:
        # https://docs.python.org/2/library/subprocess.html
        # #frequently-used-arguments
        if '*' not in command:
            return command
        splits = shlex.split(command)
        expandedSplits = []
        for split in splits:
            if '*' in split:
                files = glob.glob(split)
                expandedSplits.extend(files)
            else:
                expandedSplits.append(split)
        return ' '.join(expandedSplits)

    def runTests(self):
        testCommands = self.parseTestCommands()
        for command in testCommands:
            expandedCommand = self.expandCommand(command)
            self.log('Running: "{0}"'.format(expandedCommand))
            try:
                utils.runCommand(expandedCommand)
            except subprocess.CalledProcessError:
                self.log('ERROR')
                return
        self.log('SUCCESS')

    def log(self, logStr):
        utils.log("{0} {1}".format(self.logStrPrefix, logStr))


if __name__ == '__main__':
    travisSimulator = TravisSimulator()
    travisSimulator.runTests()
