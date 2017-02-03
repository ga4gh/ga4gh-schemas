# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/common.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n ga4gh/schemas/ga4gh/common.proto\x12\x13ga4gh.schemas.ga4gh\x1a\x1cgoogle/protobuf/struct.proto\"2\n\x0bGAException\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"a\n\x08Position\x12\x16\n\x0ereference_name\x18\x01 \x01(\t\x12\x10\n\x08position\x18\x02 \x01(\x03\x12+\n\x06strand\x18\x03 \x01(\x0e\x32\x1b.ga4gh.schemas.ga4gh.Strand\"K\n\x12\x45xternalIdentifier\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"\x86\x03\n\nExperiment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1b\n\x13message_create_time\x18\x04 \x01(\t\x12\x1b\n\x13message_update_time\x18\x05 \x01(\t\x12\x10\n\x08run_time\x18\x06 \x01(\t\x12\x10\n\x08molecule\x18\x07 \x01(\t\x12\x10\n\x08strategy\x18\x08 \x01(\t\x12\x11\n\tselection\x18\t \x01(\t\x12\x0f\n\x07library\x18\n \x01(\t\x12\x16\n\x0elibrary_layout\x18\x0b \x01(\t\x12\x18\n\x10instrument_model\x18\x0c \x01(\t\x12\x1c\n\x14instrument_data_file\x18\r \x01(\t\x12\x19\n\x11sequencing_center\x18\x0e \x01(\t\x12\x15\n\rplatform_unit\x18\x0f \x01(\t\x12\x33\n\nattributes\x18\x11 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"\xb0\x01\n\x08\x41nalysis\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x0f\n\x07updated\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x10\n\x08software\x18\x07 \x03(\t\x12\x33\n\nattributes\x18\t \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"-\n\x0cOntologyTerm\x12\x0f\n\x07term_id\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\t\"c\n\x07Program\x12\x14\n\x0c\x63ommand_line\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x17\n\x0fprev_program_id\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\"\xdc\x04\n\x0e\x41ttributeValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bint32_value\x18\x03 \x01(\x05H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12\x46\n\x13\x65xternal_identifier\x18\x06 \x01(\x0b\x32\'.ga4gh.schemas.ga4gh.ExternalIdentifierH\x00\x12:\n\rontology_term\x18\x07 \x01(\x0b\x32!.ga4gh.schemas.ga4gh.OntologyTermH\x00\x12\x35\n\nexperiment\x18\x08 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.ExperimentH\x00\x12/\n\x07program\x18\t \x01(\x0b\x32\x1c.ga4gh.schemas.ga4gh.ProgramH\x00\x12\x31\n\x08\x61nalysis\x18\n \x01(\x0b\x32\x1d.ga4gh.schemas.ga4gh.AnalysisH\x00\x12\x34\n\nnull_value\x18\x0b \x01(\x0e\x32\x1e.ga4gh.schemas.ga4gh.NullValueH\x00\x12\x35\n\nattributes\x18\x0c \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.AttributesH\x00\x12\x41\n\x0e\x61ttribute_list\x18\r \x01(\x0b\x32\'.ga4gh.schemas.ga4gh.AttributeValueListH\x00\x42\x07\n\x05value\"I\n\x12\x41ttributeValueList\x12\x33\n\x06values\x18\x01 \x03(\x0b\x32#.ga4gh.schemas.ga4gh.AttributeValue\"\x9b\x01\n\nAttributes\x12\x37\n\x04\x61ttr\x18\x01 \x03(\x0b\x32).ga4gh.schemas.ga4gh.Attributes.AttrEntry\x1aT\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.ga4gh.schemas.ga4gh.AttributeValueList:\x02\x38\x01*@\n\x06Strand\x12\x16\n\x12STRAND_UNSPECIFIED\x10\x00\x12\x0e\n\nNEG_STRAND\x10\x01\x12\x0e\n\nPOS_STRAND\x10\x02*\x1b\n\tNullValue\x12\x0e\n\nNULL_VALUE\x10\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_STRAND = _descriptor.EnumDescriptor(
  name='Strand',
  full_name='ga4gh.schemas.ga4gh.Strand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRAND_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEG_STRAND', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POS_STRAND', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1875,
  serialized_end=1939,
)
_sym_db.RegisterEnumDescriptor(_STRAND)

Strand = enum_type_wrapper.EnumTypeWrapper(_STRAND)
_NULLVALUE = _descriptor.EnumDescriptor(
  name='NullValue',
  full_name='ga4gh.schemas.ga4gh.NullValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NULL_VALUE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1941,
  serialized_end=1968,
)
_sym_db.RegisterEnumDescriptor(_NULLVALUE)

NullValue = enum_type_wrapper.EnumTypeWrapper(_NULLVALUE)
STRAND_UNSPECIFIED = 0
NEG_STRAND = 1
POS_STRAND = 2
NULL_VALUE = 0



_GAEXCEPTION = _descriptor.Descriptor(
  name='GAException',
  full_name='ga4gh.schemas.ga4gh.GAException',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='ga4gh.schemas.ga4gh.GAException.error_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ga4gh.schemas.ga4gh.GAException.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=137,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='ga4gh.schemas.ga4gh.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh.schemas.ga4gh.Position.reference_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='ga4gh.schemas.ga4gh.Position.position', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strand', full_name='ga4gh.schemas.ga4gh.Position.strand', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=236,
)


_EXTERNALIDENTIFIER = _descriptor.Descriptor(
  name='ExternalIdentifier',
  full_name='ga4gh.schemas.ga4gh.ExternalIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database', full_name='ga4gh.schemas.ga4gh.ExternalIdentifier.database', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='ga4gh.schemas.ga4gh.ExternalIdentifier.identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='ga4gh.schemas.ga4gh.ExternalIdentifier.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=313,
)


_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='ga4gh.schemas.ga4gh.Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Experiment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.Experiment.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.schemas.ga4gh.Experiment.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_create_time', full_name='ga4gh.schemas.ga4gh.Experiment.message_create_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_update_time', full_name='ga4gh.schemas.ga4gh.Experiment.message_update_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='run_time', full_name='ga4gh.schemas.ga4gh.Experiment.run_time', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='molecule', full_name='ga4gh.schemas.ga4gh.Experiment.molecule', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='ga4gh.schemas.ga4gh.Experiment.strategy', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='selection', full_name='ga4gh.schemas.ga4gh.Experiment.selection', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='library', full_name='ga4gh.schemas.ga4gh.Experiment.library', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='library_layout', full_name='ga4gh.schemas.ga4gh.Experiment.library_layout', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrument_model', full_name='ga4gh.schemas.ga4gh.Experiment.instrument_model', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrument_data_file', full_name='ga4gh.schemas.ga4gh.Experiment.instrument_data_file', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequencing_center', full_name='ga4gh.schemas.ga4gh.Experiment.sequencing_center', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform_unit', full_name='ga4gh.schemas.ga4gh.Experiment.platform_unit', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.Experiment.attributes', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=706,
)


_ANALYSIS = _descriptor.Descriptor(
  name='Analysis',
  full_name='ga4gh.schemas.ga4gh.Analysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Analysis.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.Analysis.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.schemas.ga4gh.Analysis.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='ga4gh.schemas.ga4gh.Analysis.created', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='ga4gh.schemas.ga4gh.Analysis.updated', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ga4gh.schemas.ga4gh.Analysis.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='software', full_name='ga4gh.schemas.ga4gh.Analysis.software', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.Analysis.attributes', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=709,
  serialized_end=885,
)


_ONTOLOGYTERM = _descriptor.Descriptor(
  name='OntologyTerm',
  full_name='ga4gh.schemas.ga4gh.OntologyTerm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term_id', full_name='ga4gh.schemas.ga4gh.OntologyTerm.term_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='term', full_name='ga4gh.schemas.ga4gh.OntologyTerm.term', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=932,
)


_PROGRAM = _descriptor.Descriptor(
  name='Program',
  full_name='ga4gh.schemas.ga4gh.Program',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_line', full_name='ga4gh.schemas.ga4gh.Program.command_line', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Program.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.Program.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_program_id', full_name='ga4gh.schemas.ga4gh.Program.prev_program_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='ga4gh.schemas.ga4gh.Program.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=934,
  serialized_end=1033,
)


_ATTRIBUTEVALUE = _descriptor.Descriptor(
  name='AttributeValue',
  full_name='ga4gh.schemas.ga4gh.AttributeValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_value', full_name='ga4gh.schemas.ga4gh.AttributeValue.string_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='ga4gh.schemas.ga4gh.AttributeValue.int64_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='ga4gh.schemas.ga4gh.AttributeValue.int32_value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='ga4gh.schemas.ga4gh.AttributeValue.bool_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='ga4gh.schemas.ga4gh.AttributeValue.double_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_identifier', full_name='ga4gh.schemas.ga4gh.AttributeValue.external_identifier', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ontology_term', full_name='ga4gh.schemas.ga4gh.AttributeValue.ontology_term', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiment', full_name='ga4gh.schemas.ga4gh.AttributeValue.experiment', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program', full_name='ga4gh.schemas.ga4gh.AttributeValue.program', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysis', full_name='ga4gh.schemas.ga4gh.AttributeValue.analysis', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='null_value', full_name='ga4gh.schemas.ga4gh.AttributeValue.null_value', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.AttributeValue.attributes', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute_list', full_name='ga4gh.schemas.ga4gh.AttributeValue.attribute_list', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='ga4gh.schemas.ga4gh.AttributeValue.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1036,
  serialized_end=1640,
)


_ATTRIBUTEVALUELIST = _descriptor.Descriptor(
  name='AttributeValueList',
  full_name='ga4gh.schemas.ga4gh.AttributeValueList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ga4gh.schemas.ga4gh.AttributeValueList.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1642,
  serialized_end=1715,
)


_ATTRIBUTES_ATTRENTRY = _descriptor.Descriptor(
  name='AttrEntry',
  full_name='ga4gh.schemas.ga4gh.Attributes.AttrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ga4gh.schemas.ga4gh.Attributes.AttrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.schemas.ga4gh.Attributes.AttrEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1789,
  serialized_end=1873,
)

_ATTRIBUTES = _descriptor.Descriptor(
  name='Attributes',
  full_name='ga4gh.schemas.ga4gh.Attributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attr', full_name='ga4gh.schemas.ga4gh.Attributes.attr', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTES_ATTRENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1718,
  serialized_end=1873,
)

_POSITION.fields_by_name['strand'].enum_type = _STRAND
_EXPERIMENT.fields_by_name['attributes'].message_type = _ATTRIBUTES
_ANALYSIS.fields_by_name['attributes'].message_type = _ATTRIBUTES
_ATTRIBUTEVALUE.fields_by_name['external_identifier'].message_type = _EXTERNALIDENTIFIER
_ATTRIBUTEVALUE.fields_by_name['ontology_term'].message_type = _ONTOLOGYTERM
_ATTRIBUTEVALUE.fields_by_name['experiment'].message_type = _EXPERIMENT
_ATTRIBUTEVALUE.fields_by_name['program'].message_type = _PROGRAM
_ATTRIBUTEVALUE.fields_by_name['analysis'].message_type = _ANALYSIS
_ATTRIBUTEVALUE.fields_by_name['null_value'].enum_type = _NULLVALUE
_ATTRIBUTEVALUE.fields_by_name['attributes'].message_type = _ATTRIBUTES
_ATTRIBUTEVALUE.fields_by_name['attribute_list'].message_type = _ATTRIBUTEVALUELIST
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['string_value'])
_ATTRIBUTEVALUE.fields_by_name['string_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['int64_value'])
_ATTRIBUTEVALUE.fields_by_name['int64_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['int32_value'])
_ATTRIBUTEVALUE.fields_by_name['int32_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['bool_value'])
_ATTRIBUTEVALUE.fields_by_name['bool_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['double_value'])
_ATTRIBUTEVALUE.fields_by_name['double_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['external_identifier'])
_ATTRIBUTEVALUE.fields_by_name['external_identifier'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['ontology_term'])
_ATTRIBUTEVALUE.fields_by_name['ontology_term'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['experiment'])
_ATTRIBUTEVALUE.fields_by_name['experiment'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['program'])
_ATTRIBUTEVALUE.fields_by_name['program'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['analysis'])
_ATTRIBUTEVALUE.fields_by_name['analysis'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['null_value'])
_ATTRIBUTEVALUE.fields_by_name['null_value'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['attributes'])
_ATTRIBUTEVALUE.fields_by_name['attributes'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUE.oneofs_by_name['value'].fields.append(
  _ATTRIBUTEVALUE.fields_by_name['attribute_list'])
_ATTRIBUTEVALUE.fields_by_name['attribute_list'].containing_oneof = _ATTRIBUTEVALUE.oneofs_by_name['value']
_ATTRIBUTEVALUELIST.fields_by_name['values'].message_type = _ATTRIBUTEVALUE
_ATTRIBUTES_ATTRENTRY.fields_by_name['value'].message_type = _ATTRIBUTEVALUELIST
_ATTRIBUTES_ATTRENTRY.containing_type = _ATTRIBUTES
_ATTRIBUTES.fields_by_name['attr'].message_type = _ATTRIBUTES_ATTRENTRY
DESCRIPTOR.message_types_by_name['GAException'] = _GAEXCEPTION
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['ExternalIdentifier'] = _EXTERNALIDENTIFIER
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.message_types_by_name['Analysis'] = _ANALYSIS
DESCRIPTOR.message_types_by_name['OntologyTerm'] = _ONTOLOGYTERM
DESCRIPTOR.message_types_by_name['Program'] = _PROGRAM
DESCRIPTOR.message_types_by_name['AttributeValue'] = _ATTRIBUTEVALUE
DESCRIPTOR.message_types_by_name['AttributeValueList'] = _ATTRIBUTEVALUELIST
DESCRIPTOR.message_types_by_name['Attributes'] = _ATTRIBUTES
DESCRIPTOR.enum_types_by_name['Strand'] = _STRAND
DESCRIPTOR.enum_types_by_name['NullValue'] = _NULLVALUE

GAException = _reflection.GeneratedProtocolMessageType('GAException', (_message.Message,), dict(
  DESCRIPTOR = _GAEXCEPTION,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GAException)
  ))
_sym_db.RegisterMessage(GAException)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Position)
  ))
_sym_db.RegisterMessage(Position)

ExternalIdentifier = _reflection.GeneratedProtocolMessageType('ExternalIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _EXTERNALIDENTIFIER,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ExternalIdentifier)
  ))
_sym_db.RegisterMessage(ExternalIdentifier)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Experiment)
  ))
_sym_db.RegisterMessage(Experiment)

Analysis = _reflection.GeneratedProtocolMessageType('Analysis', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSIS,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Analysis)
  ))
_sym_db.RegisterMessage(Analysis)

OntologyTerm = _reflection.GeneratedProtocolMessageType('OntologyTerm', (_message.Message,), dict(
  DESCRIPTOR = _ONTOLOGYTERM,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.OntologyTerm)
  ))
_sym_db.RegisterMessage(OntologyTerm)

Program = _reflection.GeneratedProtocolMessageType('Program', (_message.Message,), dict(
  DESCRIPTOR = _PROGRAM,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Program)
  ))
_sym_db.RegisterMessage(Program)

AttributeValue = _reflection.GeneratedProtocolMessageType('AttributeValue', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTEVALUE,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.AttributeValue)
  ))
_sym_db.RegisterMessage(AttributeValue)

AttributeValueList = _reflection.GeneratedProtocolMessageType('AttributeValueList', (_message.Message,), dict(
  DESCRIPTOR = _ATTRIBUTEVALUELIST,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.AttributeValueList)
  ))
_sym_db.RegisterMessage(AttributeValueList)

Attributes = _reflection.GeneratedProtocolMessageType('Attributes', (_message.Message,), dict(

  AttrEntry = _reflection.GeneratedProtocolMessageType('AttrEntry', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTES_ATTRENTRY,
    __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
    # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Attributes.AttrEntry)
    ))
  ,
  DESCRIPTOR = _ATTRIBUTES,
  __module__ = 'ga4gh.schemas.ga4gh.common_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Attributes)
  ))
_sym_db.RegisterMessage(Attributes)
_sym_db.RegisterMessage(Attributes.AttrEntry)


_ATTRIBUTES_ATTRENTRY.has_options = True
_ATTRIBUTES_ATTRENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
