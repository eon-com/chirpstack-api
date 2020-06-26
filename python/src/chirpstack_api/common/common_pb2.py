# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/common/common.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chirpstack-api/common/common.proto',
  package='common',
  syntax='proto3',
  serialized_options=b'Z.github.com/brocaar/chirpstack-api/go/v3/common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"chirpstack-api/common/common.proto\x12\x06\x63ommon\"1\n\x0bKeyEnvelope\x12\x11\n\tkek_label\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x65s_key\x18\x02 \x01(\x0c\"{\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\x12&\n\x06source\x18\x04 \x01(\x0e\x32\x16.common.LocationSource\x12\x10\n\x08\x61\x63\x63uracy\x18\x05 \x01(\r*\x1f\n\nModulation\x12\x08\n\x04LORA\x10\x00\x12\x07\n\x03\x46SK\x10\x01*v\n\x06Region\x12\t\n\x05\x45U868\x10\x00\x12\t\n\x05US915\x10\x02\x12\t\n\x05\x43N779\x10\x03\x12\t\n\x05\x45U433\x10\x04\x12\t\n\x05\x41U915\x10\x05\x12\t\n\x05\x43N470\x10\x06\x12\t\n\x05\x41S923\x10\x07\x12\t\n\x05KR920\x10\x08\x12\t\n\x05IN865\x10\t\x12\t\n\x05RU864\x10\n*\x8e\x01\n\x0eLocationSource\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03GPS\x10\x01\x12\n\n\x06\x43ONFIG\x10\x02\x12\x15\n\x11GEO_RESOLVER_TDOA\x10\x03\x12\x15\n\x11GEO_RESOLVER_RSSI\x10\x04\x12\x15\n\x11GEO_RESOLVER_GNSS\x10\x05\x12\x15\n\x11GEO_RESOLVER_WIFI\x10\x06\x42\x30Z.github.com/brocaar/chirpstack-api/go/v3/commonb\x06proto3'
)

_MODULATION = _descriptor.EnumDescriptor(
  name='Modulation',
  full_name='common.Modulation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LORA', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FSK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=222,
  serialized_end=253,
)
_sym_db.RegisterEnumDescriptor(_MODULATION)

Modulation = enum_type_wrapper.EnumTypeWrapper(_MODULATION)
_REGION = _descriptor.EnumDescriptor(
  name='Region',
  full_name='common.Region',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EU868', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='US915', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CN779', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EU433', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AU915', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CN470', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AS923', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KR920', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN865', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RU864', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=255,
  serialized_end=373,
)
_sym_db.RegisterEnumDescriptor(_REGION)

Region = enum_type_wrapper.EnumTypeWrapper(_REGION)
_LOCATIONSOURCE = _descriptor.EnumDescriptor(
  name='LocationSource',
  full_name='common.LocationSource',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONFIG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEO_RESOLVER_TDOA', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEO_RESOLVER_RSSI', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEO_RESOLVER_GNSS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEO_RESOLVER_WIFI', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=376,
  serialized_end=518,
)
_sym_db.RegisterEnumDescriptor(_LOCATIONSOURCE)

LocationSource = enum_type_wrapper.EnumTypeWrapper(_LOCATIONSOURCE)
LORA = 0
FSK = 1
EU868 = 0
US915 = 2
CN779 = 3
EU433 = 4
AU915 = 5
CN470 = 6
AS923 = 7
KR920 = 8
IN865 = 9
RU864 = 10
UNKNOWN = 0
GPS = 1
CONFIG = 2
GEO_RESOLVER_TDOA = 3
GEO_RESOLVER_RSSI = 4
GEO_RESOLVER_GNSS = 5
GEO_RESOLVER_WIFI = 6



_KEYENVELOPE = _descriptor.Descriptor(
  name='KeyEnvelope',
  full_name='common.KeyEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kek_label', full_name='common.KeyEnvelope.kek_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aes_key', full_name='common.KeyEnvelope.aes_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=95,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='common.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='common.Location.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='common.Location.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='common.Location.altitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='common.Location.source', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='common.Location.accuracy', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=220,
)

_LOCATION.fields_by_name['source'].enum_type = _LOCATIONSOURCE
DESCRIPTOR.message_types_by_name['KeyEnvelope'] = _KEYENVELOPE
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.enum_types_by_name['Modulation'] = _MODULATION
DESCRIPTOR.enum_types_by_name['Region'] = _REGION
DESCRIPTOR.enum_types_by_name['LocationSource'] = _LOCATIONSOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyEnvelope = _reflection.GeneratedProtocolMessageType('KeyEnvelope', (_message.Message,), {
  'DESCRIPTOR' : _KEYENVELOPE,
  '__module__' : 'chirpstack_api.common.common_pb2'
  # @@protoc_insertion_point(class_scope:common.KeyEnvelope)
  })
_sym_db.RegisterMessage(KeyEnvelope)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'chirpstack_api.common.common_pb2'
  # @@protoc_insertion_point(class_scope:common.Location)
  })
_sym_db.RegisterMessage(Location)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
