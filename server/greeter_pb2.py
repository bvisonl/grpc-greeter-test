# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgreeter.proto\x12\x07greeter\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2J\n\x0eGreeterService\x12\x38\n\x08SayHello\x12\x15.greeter.HelloRequest\x1a\x13.greeter.HelloReply\"\x00\x62\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLOREPLY = DESCRIPTOR.message_types_by_name['HelloReply']
HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'greeter_pb2'
  # @@protoc_insertion_point(class_scope:greeter.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'greeter_pb2'
  # @@protoc_insertion_point(class_scope:greeter.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

_GREETERSERVICE = DESCRIPTOR.services_by_name['GreeterService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=26
  _HELLOREQUEST._serialized_end=54
  _HELLOREPLY._serialized_start=56
  _HELLOREPLY._serialized_end=85
  _GREETERSERVICE._serialized_start=87
  _GREETERSERVICE._serialized_end=161
# @@protoc_insertion_point(module_scope)
