"""
Hack for getting a handle to the top-level google module, etc.
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import google.protobuf.json_format as json_format
import google.protobuf.message as message
import google.protobuf.struct_pb2 as struct_pb2


def getJsonFormat():
    """
    Returns the module google.protobuf.json_format
    """
    return json_format


def getMessage():
    """
    Returns the module google.protobuf.message
    """
    return message


def getStructPb2():
    """
    Returns the module google.protobuf.struct_pb2
    """
    return struct_pb2
