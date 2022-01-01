# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: baseDocument.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import workspace_pb2 as workspace__pb2
import basicTypes_pb2 as basicTypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62\x61seDocument.proto\x12\x07rv.data\x1a\x0fworkspace.proto\x1a\x10\x62\x61sicTypes.proto\"\x9e\x01\n\x08\x44ocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12\x1b\n\x04uuid\x18\x02 \x01(\x0b\x32\r.rv.data.UUID\x12\x1a\n\x12uses_relative_urls\x18\x03 \x01(\x08\x12%\n\tworkspace\x18\n \x01(\x0b\x32\x12.rv.data.Workspace\"\x8e\x01\n\tCacheInfo\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12-\n\x13\x61pplication_version\x18\x02 \x01(\x0b\x32\x10.rv.data.Version\x12\x19\n\x03url\x18\x03 \x01(\x0b\x32\x0c.rv.data.URL\x12\x1a\n\x12last_modified_date\x18\x04 \x01(\x01\"\xd7\x04\n\x10PVPDocumentState\x12\x41\n\x10primary_playlist\x18\x01 \x01(\x0b\x32\'.rv.data.PVPDocumentState.PlaylistState\x12\x43\n\x12\x61lternate_playlist\x18\x02 \x01(\x0b\x32\'.rv.data.PVPDocumentState.PlaylistState\x12\"\n\x1aplaylist_split_is_vertical\x18\x03 \x01(\x08\x12%\n\x0etargeted_layer\x18\x04 \x01(\x0b\x32\r.rv.data.UUID\x12%\n\x0eselected_layer\x18\x05 \x01(\x0b\x32\r.rv.data.UUID\x12#\n\x0clocked_layer\x18\x06 \x01(\x0b\x32\r.rv.data.UUID\x12!\n\x19live_video_playlist_scale\x18\x07 \x01(\x01\x12#\n\x1bsplit_view_divider_position\x18\x08 \x01(\x01\x1a\xdb\x01\n\rPlaylistState\x12\x1b\n\x04uuid\x18\x02 \x01(\x0b\x32\r.rv.data.UUID\x12\x42\n\x06layout\x18\x03 \x01(\x0e\x32\x32.rv.data.PVPDocumentState.PlaylistState.LayoutType\x12\x12\n\nitem_scale\x18\x04 \x01(\x01\"U\n\nLayoutType\x12\x13\n\x0fLAYOUT_TYPE_CUE\x10\x00\x12\x16\n\x12LAYOUT_TYPE_ACTION\x10\x01\x12\x1a\n\x16LAYOUT_TYPE_LIVE_VIDEO\x10\x02\x62\x06proto3')



_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
_CACHEINFO = DESCRIPTOR.message_types_by_name['CacheInfo']
_PVPDOCUMENTSTATE = DESCRIPTOR.message_types_by_name['PVPDocumentState']
_PVPDOCUMENTSTATE_PLAYLISTSTATE = _PVPDOCUMENTSTATE.nested_types_by_name['PlaylistState']
_PVPDOCUMENTSTATE_PLAYLISTSTATE_LAYOUTTYPE = _PVPDOCUMENTSTATE_PLAYLISTSTATE.enum_types_by_name['LayoutType']
Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'baseDocument_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.Document)
  })
_sym_db.RegisterMessage(Document)

CacheInfo = _reflection.GeneratedProtocolMessageType('CacheInfo', (_message.Message,), {
  'DESCRIPTOR' : _CACHEINFO,
  '__module__' : 'baseDocument_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.CacheInfo)
  })
_sym_db.RegisterMessage(CacheInfo)

PVPDocumentState = _reflection.GeneratedProtocolMessageType('PVPDocumentState', (_message.Message,), {

  'PlaylistState' : _reflection.GeneratedProtocolMessageType('PlaylistState', (_message.Message,), {
    'DESCRIPTOR' : _PVPDOCUMENTSTATE_PLAYLISTSTATE,
    '__module__' : 'baseDocument_pb2'
    # @@protoc_insertion_point(class_scope:rv.data.PVPDocumentState.PlaylistState)
    })
  ,
  'DESCRIPTOR' : _PVPDOCUMENTSTATE,
  '__module__' : 'baseDocument_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.PVPDocumentState)
  })
_sym_db.RegisterMessage(PVPDocumentState)
_sym_db.RegisterMessage(PVPDocumentState.PlaylistState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOCUMENT._serialized_start=67
  _DOCUMENT._serialized_end=225
  _CACHEINFO._serialized_start=228
  _CACHEINFO._serialized_end=370
  _PVPDOCUMENTSTATE._serialized_start=373
  _PVPDOCUMENTSTATE._serialized_end=972
  _PVPDOCUMENTSTATE_PLAYLISTSTATE._serialized_start=753
  _PVPDOCUMENTSTATE_PLAYLISTSTATE._serialized_end=972
  _PVPDOCUMENTSTATE_PLAYLISTSTATE_LAYOUTTYPE._serialized_start=887
  _PVPDOCUMENTSTATE_PLAYLISTSTATE_LAYOUTTYPE._serialized_end=972
# @@protoc_insertion_point(module_scope)