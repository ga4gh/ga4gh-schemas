"""
Runs tests that ensure protocol invariants

TODO add other tests including:
- some CI on postSignatures
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

import avro.schema

import compile_schemas


class TestValidateSchemas(unittest.TestCase):
    """
    Ensure the schemas conform to certain rules
    """
    @classmethod
    def setupClass(cls):
        args = cls._makeArgs()
        cls.schemaProcessor = compile_schemas.SchemaProcessor(args)
        cls.schemaProcessor.run()

    @classmethod
    def tearDownClass(cls):
        cls.schemaProcessor.cleanup()

    @classmethod
    def getClasses(cls):
        return cls.schemaProcessor.getClasses()

    @classmethod
    def _makeArgs(self):
        class FakeArgs(object):
            pass
        args = FakeArgs()
        args.version = "test"
        args.avro_tools_jar = None
        return args

    def testSchemaProperties(self):
        for schemaClass in self.getClasses():
            self._checkProperties(schemaClass)

    def _checkProperties(self, schemaClass):
        """
        Checks that the class schema satisfies certain properties:
        - every union must have null as the first type
        """
        if isinstance(schemaClass.schema, avro.schema.RecordSchema):
            for field in schemaClass.getFields():
                pass
