"""
Utility methods for handling protocol buffer
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

DEFAULT_STRING = ''
DEFAULT_INT = 0


def string(val):
    """
    Default value for "string" fields
    """
    return DEFAULT_STRING if val is None else val


def int(val):
    """
    Default value for "int32" or "int64 fields
    """
    return DEFAULT_INT if val is None else val
