# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: air.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='air.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tair.proto\"%\n\x0e\x41irTemperature\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x32\x62\n\x03\x41ir\x12,\n\x06turnOn\x12\x0f.AirTemperature\x1a\x0f.AirTemperature\"\x00\x12-\n\x07turnOff\x12\x0f.AirTemperature\x1a\x0f.AirTemperature\"\x00\x62\x06proto3'
)




_AIRTEMPERATURE = _descriptor.Descriptor(
  name='AirTemperature',
  full_name='AirTemperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperature', full_name='AirTemperature.temperature', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=13,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['AirTemperature'] = _AIRTEMPERATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AirTemperature = _reflection.GeneratedProtocolMessageType('AirTemperature', (_message.Message,), {
  'DESCRIPTOR' : _AIRTEMPERATURE,
  '__module__' : 'air_pb2'
  # @@protoc_insertion_point(class_scope:AirTemperature)
  })
_sym_db.RegisterMessage(AirTemperature)



_AIR = _descriptor.ServiceDescriptor(
  name='Air',
  full_name='Air',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=52,
  serialized_end=150,
  methods=[
  _descriptor.MethodDescriptor(
    name='turnOn',
    full_name='Air.turnOn',
    index=0,
    containing_service=None,
    input_type=_AIRTEMPERATURE,
    output_type=_AIRTEMPERATURE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='turnOff',
    full_name='Air.turnOff',
    index=1,
    containing_service=None,
    input_type=_AIRTEMPERATURE,
    output_type=_AIRTEMPERATURE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AIR)

DESCRIPTOR.services_by_name['Air'] = _AIR

# @@protoc_insertion_point(module_scope)