# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/message.proto',
  package='zmq_message',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14protos/message.proto\x12\x0bzmq_message\"\x9e\x01\n\nZMQMessage\x12\x11\n\tclient_id\x18\x01 \x02(\x0c\x12\x0e\n\x06req_id\x18\x02 \x02(\x0c\x12\x0f\n\x07part_id\x18\x03 \x02(\x0c\x12\x10\n\x08num_part\x18\x04 \x02(\x0c\x12\x14\n\x0c\x63ontent_type\x18\x05 \x02(\x0c\x12\x10\n\x08msg_type\x18\x06 \x02(\x0c\x12\x13\n\x0bmsg_content\x18\x07 \x02(\x0c\x12\r\n\x05route\x18\x08 \x02(\x0c')
)




_ZMQMESSAGE = _descriptor.Descriptor(
  name='ZMQMessage',
  full_name='zmq_message.ZMQMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='zmq_message.ZMQMessage.client_id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='req_id', full_name='zmq_message.ZMQMessage.req_id', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='part_id', full_name='zmq_message.ZMQMessage.part_id', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_part', full_name='zmq_message.ZMQMessage.num_part', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='zmq_message.ZMQMessage.content_type', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='zmq_message.ZMQMessage.msg_type', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_content', full_name='zmq_message.ZMQMessage.msg_content', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route', full_name='zmq_message.ZMQMessage.route', index=7,
      number=8, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['ZMQMessage'] = _ZMQMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZMQMessage = _reflection.GeneratedProtocolMessageType('ZMQMessage', (_message.Message,), dict(
  DESCRIPTOR = _ZMQMESSAGE,
  __module__ = 'protos.message_pb2'
  # @@protoc_insertion_point(class_scope:zmq_message.ZMQMessage)
  ))
_sym_db.RegisterMessage(ZMQMessage)


# @@protoc_insertion_point(module_scope)