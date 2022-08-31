# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network_telemetry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='network_telemetry.proto',
  package='v2.network_telemetry',
  syntax='proto3',
  serialized_options=b'\n\026io.moonsense.models.v2B\030NetworkTelemetryV2ProtosZ+moonsense.io/pkg/pb/v2/network-telemetry;v2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17network_telemetry.proto\x12\x14v2.network_telemetry\"\xb4\x01\n\x14SealedNetworkRequest\x12\x34\n\x07packets\x18\x01 \x03(\x0b\x32#.v2.network_telemetry.NetworkPacket\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\t\x12\x15\n\rcredential_id\x18\x03 \x01(\t\x12\x12\n\nsession_id\x18\x04 \x01(\t\x12\x0f\n\x07\x61ttempt\x18\x05 \x01(\x05\x12\x1a\n\x12server_time_millis\x18\x06 \x01(\x03\"\xbd\x01\n\rNetworkPacket\x12\x19\n\x11server_time_nanos\x18\x01 \x01(\x03\x12>\n\x08protocol\x18\x02 \x01(\x0e\x32,.v2.network_telemetry.NetworkPacket.Protocol\x12\x16\n\x0enetwork_layers\x18\x03 \x03(\t\x12\x0c\n\x04pcap\x18\x04 \x01(\x0c\"+\n\x08Protocol\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x42_\n\x16io.moonsense.models.v2B\x18NetworkTelemetryV2ProtosZ+moonsense.io/pkg/pb/v2/network-telemetry;v2b\x06proto3'
)



_NETWORKPACKET_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='v2.network_telemetry.NetworkPacket.Protocol',
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
      name='IPV4', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IPV6', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=379,
  serialized_end=422,
)
_sym_db.RegisterEnumDescriptor(_NETWORKPACKET_PROTOCOL)


_SEALEDNETWORKREQUEST = _descriptor.Descriptor(
  name='SealedNetworkRequest',
  full_name='v2.network_telemetry.SealedNetworkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='packets', full_name='v2.network_telemetry.SealedNetworkRequest.packets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='v2.network_telemetry.SealedNetworkRequest.app_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='credential_id', full_name='v2.network_telemetry.SealedNetworkRequest.credential_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='v2.network_telemetry.SealedNetworkRequest.session_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attempt', full_name='v2.network_telemetry.SealedNetworkRequest.attempt', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_time_millis', full_name='v2.network_telemetry.SealedNetworkRequest.server_time_millis', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=50,
  serialized_end=230,
)


_NETWORKPACKET = _descriptor.Descriptor(
  name='NetworkPacket',
  full_name='v2.network_telemetry.NetworkPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_time_nanos', full_name='v2.network_telemetry.NetworkPacket.server_time_nanos', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='v2.network_telemetry.NetworkPacket.protocol', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_layers', full_name='v2.network_telemetry.NetworkPacket.network_layers', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pcap', full_name='v2.network_telemetry.NetworkPacket.pcap', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKPACKET_PROTOCOL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=422,
)

_SEALEDNETWORKREQUEST.fields_by_name['packets'].message_type = _NETWORKPACKET
_NETWORKPACKET.fields_by_name['protocol'].enum_type = _NETWORKPACKET_PROTOCOL
_NETWORKPACKET_PROTOCOL.containing_type = _NETWORKPACKET
DESCRIPTOR.message_types_by_name['SealedNetworkRequest'] = _SEALEDNETWORKREQUEST
DESCRIPTOR.message_types_by_name['NetworkPacket'] = _NETWORKPACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SealedNetworkRequest = _reflection.GeneratedProtocolMessageType('SealedNetworkRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEALEDNETWORKREQUEST,
  '__module__' : 'network_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:v2.network_telemetry.SealedNetworkRequest)
  })
_sym_db.RegisterMessage(SealedNetworkRequest)

NetworkPacket = _reflection.GeneratedProtocolMessageType('NetworkPacket', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKPACKET,
  '__module__' : 'network_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:v2.network_telemetry.NetworkPacket)
  })
_sym_db.RegisterMessage(NetworkPacket)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)