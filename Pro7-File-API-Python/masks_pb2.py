# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: masks.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import graphicsData_pb2 as graphicsData__pb2
import basicTypes_pb2 as basicTypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmasks.proto\x12\x07rv.data\x1a\x12graphicsData.proto\x1a\x10\x62\x61sicTypes.proto\"\xc9\x01\n\x04Mask\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1d\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x0e.rv.data.Color\x12 \n\x04mode\x18\x04 \x01(\x0e\x32\x12.rv.data.Mask.Mode\x12)\n\x06shapes\x18\x05 \x03(\x0b\x32\x19.rv.data.Graphics.Element\"*\n\x04Mode\x12\x10\n\x0cMODE_OVERLAY\x10\x00\x12\x10\n\x0cMODE_KEYHOLE\x10\x01\x62\x06proto3')



_MASK = DESCRIPTOR.message_types_by_name['Mask']
_MASK_MODE = _MASK.enum_types_by_name['Mode']
Mask = _reflection.GeneratedProtocolMessageType('Mask', (_message.Message,), {
  'DESCRIPTOR' : _MASK,
  '__module__' : 'masks_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Mask)
  })
_sym_db.RegisterMessage(Mask)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MASK._serialized_start=63
  _MASK._serialized_end=264
  _MASK_MODE._serialized_start=222
  _MASK_MODE._serialized_end=264
# @@protoc_insertion_point(module_scope)
