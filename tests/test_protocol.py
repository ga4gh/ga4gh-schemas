"""
Tests for protocol.py
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import unittest

import google.protobuf.message as message

import ga4gh.schemas.protocol as protocol
import ga4gh.schemas.ga4gh.common_pb2 as common

from ga4gh.schemas.ga4gh.datasets_pb2 import Dataset


class TestProtocol(unittest.TestCase):
    """
    Test the methods in protocol.py
    """

    # TODO this suite is not very sophisticated right now due to
    # using empty instead of instantiated protobuf classes to test various
    # aspects of the protocol module...
    # an improvement would be to use an avrotools-like class instantiator
    # to generate dummy instantiations that could be tested

    def testGetValueListName(self):
        for clazz in protocol.getProtocolClasses():
            if len(clazz.DESCRIPTOR.fields_by_number) > 0:
                self.assertIsInstance(protocol.getValueListName(clazz), str)

    def testConvertDatetime(self):
        datetime_ = datetime.datetime.fromordinal(1234567)
        converted = protocol.convertDatetime(datetime_)
        self.assertEqual(converted, 44530905600000)

    def testGetValueFromValue(self):
        with self.assertRaises(TypeError):
            protocol.getValueFromValue(5)
        val = common.AttributeValue()
        with self.assertRaises(AttributeError):
            protocol.getValueFromValue(val)
        read = protocol.ReadAlignment()
        expected = "1"
        read.attributes.attr['key'].values.add().string_value = expected
        tag, value = read.attributes.attr.items()[0]
        result = protocol.getValueFromValue(value.values[0])
        self.assertEquals(result, expected)

    def testToJsonAndFromJson(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            jsonStr = protocol.toJson(obj)
            obj2 = protocol.fromJson(jsonStr, clazz)
            self.assertTrue(obj, obj2)

    def testToJsonDict(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            jsonDict = protocol.toJsonDict(obj)
            self.assertIsInstance(jsonDict, dict)

    def testValidate(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            jsonStr = protocol.toJson(obj)
            protocol.validate(jsonStr, clazz)

    def testGetProtocolClasses(self):
        classes = protocol.getProtocolClasses()
        self.assertGreater(len(classes), 0)
        for clazz in classes:
            self.assertTrue(issubclass(clazz, message.Message))

    def testPostMethods(self):
        for postMethod in protocol.postMethods:
            self.assertEqual(len(postMethod), 3)
            self.assertIsInstance(postMethod[0], unicode)
            self.assertTrue(issubclass(postMethod[1], message.Message))
            self.assertTrue(issubclass(postMethod[2], message.Message))

    def testSetAttribute(self):
        expected = 5
        read = protocol.ReadAlignment()
        values = read.attributes.attr['key'].values
        protocol.setAttribute(values, expected)
        tag, value = read.attributes.attr.items()[0]
        result = value.values[0].int32_value
        self.assertEqual(result, expected)

    def testEncodeValue(self):
        expected = "5"
        result = protocol.encodeValue(expected)
        self.assertEquals(result[0].string_value, expected)
        listExpected = ["5", "6"]
        listResult = protocol.encodeValue(listExpected)
        self.assertEquals(listResult[0].string_value, listExpected[0])
        self.assertEquals(listResult[1].string_value, listExpected[1])

    def testDeepGetAttr(self):
        class Object(object):
            pass
        b = Object()
        setattr(b, "c", 42)
        a = Object()
        setattr(a, "b", b)
        obj = Object()
        setattr(obj, "a", a)
        setattr(obj, "d", 12)
        self.assertEquals(protocol.deepGetAttr(obj, "a.b.c"), 42)
        self.assertEquals(protocol.deepGetAttr(obj, "d"), 12)
        self.assertRaises(AttributeError,
                          protocol.deepGetAttr, obj, "a.b.x")
        self.assertRaises(AttributeError, protocol.deepGetAttr, obj, "e")

    def testDeepSetAttr(self):
        class Object(object):
            pass
        b = Object()
        setattr(b, "c", 42)
        a = Object()
        setattr(a, "b", b)
        obj = Object()
        setattr(obj, "a", a)
        protocol.deepSetAttr(obj, 'a.b.c', 43)
        self.assertEquals(obj.a.b.c, 43)
        protocol.deepSetAttr(obj, 'a.b.x', 12)
        self.assertEquals(obj.a.b.x, 12)
        self.assertRaises(AttributeError,
                          protocol.deepSetAttr, obj, "a.x.c", 42)


class TestRoundTrip(unittest.TestCase):
    """
    Instantiate the protocol classes and convert them to and from json
    and test if the values are preserved
    """
    def testRoundTripDataset(self):
        id_ = "id"
        name = "name"
        description = "description"
        dataset = protocol.Dataset()
        dataset.id = id_
        dataset.name = name
        dataset.description = description
        jsonStr = protocol.toJson(dataset)
        newDataset = protocol.fromJson(jsonStr, Dataset)
        self.assertEquals(dataset.id, id_)
        self.assertEquals(dataset.name, name)
        self.assertEquals(dataset.description, description)
        datasetDict = protocol.toJsonDict(newDataset)
        self.assertEquals(datasetDict['id'], id_)
        self.assertEquals(datasetDict['name'], name)
        self.assertEquals(datasetDict['description'], description)
