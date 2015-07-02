# -*- coding: utf-8 -*-
"""
    avrodomain
    ~~~~~~~~~~

    Apache Avro domain.
"""

__version__ = "0.1"
# for this module's sphinx doc 
release = __version__
version = release.rsplit('.', 1)[0]

import re

from docutils import nodes
from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from sphinx.util.docfields import Field, GroupedField, TypedField

class AvroObject(ObjectDescription):
  """
  Description of a general Avro object.
  """
  has_arguments = False
  display_prefix = None

class AvroFixedField(AvroObject):
  pass

class AvroEnum(AvroObject):
  doc_field_types = [
    Field('values', label=l_('Values'),
          names=('values',))
  ]

class AvroRecord(AvroObject):
  doc_field_types = [
    TypedField('fields', label=l_('Fields'),
               names=('field','member'),
               typerolename='record')
  ]

class AvroError(AvroRecord):
  pass

class AvroRPCMessage(AvroObject):
  has_arguments = True
  doc_field_types = [
    TypedField('arguments', label=l_('Arguments'),
               names=('argument','arg','param'),
               typerolename='rpc'),
    GroupedField('errors', label=l_('Throws'),
                 names=('throws','throw')),
    Field('returntype', label=l_('Returns'),
          names=('returns','return'))
  ]

class AvroDomain(Domain):
  name = "avro"
  label = "Apache Avro"
  
  object_types = {
    'fixed':  ObjType(l_('fixed'),  'fixed'),
    'enum':   ObjType(l_('enum'),   'enum'),
    'record': ObjType(l_('record'), 'record'),
    'error':  ObjType(l_('error'),  'error'),
    'rpc':    ObjType(l_('rpc'),    'rpc'),
  }
  
  directives = {
    'fixed':  AvroFixedField,
    'enum':   AvroEnum,
    'record': AvroRecord,
    'error':  AvroError,
    'rpc':    AvroRPCMessage
  }
  
  roles = {
    'fixed':  XRefRole(),
    'enum':   XRefRole(),
    'record': XRefRole(),
    'error':  XRefRole(),
    'rpc':    XRefRole()
  }
  
  initial_data = {
    'objects': {}
  }

def setup(app):
  app.add_domain(AvroDomain)
