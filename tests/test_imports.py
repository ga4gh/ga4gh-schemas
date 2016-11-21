"""
Tests for schemas
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

# similar to dev_glue.py
import ga4gh
ga4gh.__path__.insert(0, 'python/ga4gh')

import ga4gh.schemas._protocol_version as version  # NOQA
import ga4gh.schemas.google.api.http_pb2 as http_pb2  # NOQA
import ga4gh.schemas.ga4gh.common_pb2 as common_pb2  # NOQA
import ga4gh.schemas.pb as pb  # NOQA


class TestPb(unittest.TestCase):

    def testString(self):
        self.assertEqual(pb.DEFAULT_STRING, pb.string(None))
        self.assertEqual('A', pb.string('A'))

    def testInt(self):
        self.assertEqual(pb.DEFAULT_INT, pb.int(None))
        self.assertEqual(1, pb.int(1))


class TestSchemas(unittest.TestCase):

    def testVersion(self):
        version.version.split('.')
        self.assertIsNotNone(version.version)

    def testGa4ghCommon(self):
        self.assertIsNotNone(common_pb2.DESCRIPTOR)

    def testGoogle(self):
        self.assertIsNotNone(http_pb2.DESCRIPTOR)
