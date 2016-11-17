"""
Tests for schemas
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

import ga4gh.schemas._protocol_version as version
import ga4gh.schemas.elgoog.api.http_pb2 as http_pb2
import ga4gh.schemas.common_pb2 as common_pb2
import ga4gh.schemas.pb as pb


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
