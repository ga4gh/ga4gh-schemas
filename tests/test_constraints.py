"""
Tests the constraints invariants
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

import ga4gh.common.utils as utils


class TestConstraints(unittest.TestCase):

    constraintsFilePath = 'python/constraints.txt'
    constraintsFileDefaultPath = 'python/constraints.txt.default'

    def testDefault(self):
        utils.assertFileContentsIdentical(
            self.constraintsFilePath, self.constraintsFileDefaultPath)
