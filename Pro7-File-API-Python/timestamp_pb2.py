# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timestamp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftimestamp.proto\x12\x07rv.data\"+\n\tTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\x62\x06proto3')



_TIMESTAMP = DESCRIPTOR.message_types_by_name['Timestamp']
Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'timestamp_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TIMESTAMP._serialized_start=28
  _TIMESTAMP._serialized_end=71
# @@protoc_insertion_point(module_scope)
