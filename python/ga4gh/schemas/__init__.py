"""
GA4GH schemas compiled to pb2 files
"""
# Don't include future imports here; we don't want to export them as
# part of the package

__version__ = "undefined"
try:
    from . import _version
    __version__ = _version.version
except ImportError:
    pass
