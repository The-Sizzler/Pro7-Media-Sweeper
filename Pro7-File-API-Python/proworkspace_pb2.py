# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proworkspace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proscreen_pb2 as proscreen__pb2
import proAudienceLook_pb2 as proAudienceLook__pb2
import proMask_pb2 as proMask__pb2
import input_pb2 as input__pb2
import audio_pb2 as audio__pb2
import digitalAudio_pb2 as digitalAudio__pb2
import stage_pb2 as stage__pb2
import recording_pb2 as recording__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proworkspace.proto\x12\x07rv.data\x1a\x0fproscreen.proto\x1a\x15proAudienceLook.proto\x1a\rproMask.proto\x1a\x0binput.proto\x1a\x0b\x61udio.proto\x1a\x12\x64igitalAudio.proto\x1a\x0bstage.proto\x1a\x0frecording.proto\"\xdc\x04\n\x15ProPresenterWorkspace\x12\x30\n\x0bpro_screens\x18\x01 \x03(\x0b\x32\x1b.rv.data.ProPresenterScreen\x12\x30\n\x0e\x61udience_looks\x18\x02 \x03(\x0b\x32\x18.rv.data.ProAudienceLook\x12\x34\n\x12live_audience_look\x18\x03 \x01(\x0b\x32\x18.rv.data.ProAudienceLook\x12\x1f\n\x05masks\x18\x04 \x03(\x0b\x32\x10.rv.data.ProMask\x12(\n\x0bvideoInputs\x18\x05 \x03(\x0b\x32\x13.rv.data.VideoInput\x12>\n\x15stage_layout_mappings\x18\x06 \x03(\x0b\x32\x1f.rv.data.Stage.ScreenAssignment\x12\x37\n\x0e\x61udio_settings\x18\x07 \x01(\x0b\x32\x1f.rv.data.Audio.SettingsDocument\x12\x1d\n\x15selected_library_name\x18\x08 \x01(\t\x12<\n\x0frecord_settings\x18\t \x01(\x0b\x32#.rv.data.Recording.SettingsDocument\x12\x38\n\x13\x64igital_audio_setup\x18\n \x01(\x0b\x32\x1b.rv.data.DigitalAudio.Setup\x12)\n\x0c\x61udio_inputs\x18\x0b \x03(\x0b\x32\x13.rv.data.AudioInput\x12#\n\x1b\x61udio_input_transition_time\x18\x0c \x01(\x01\x62\x06proto3')



_PROPRESENTERWORKSPACE = DESCRIPTOR.message_types_by_name['ProPresenterWorkspace']
ProPresenterWorkspace = _reflection.GeneratedProtocolMessageType('ProPresenterWorkspace', (_message.Message,), {
  'DESCRIPTOR' : _PROPRESENTERWORKSPACE,
  '__module__' : 'proworkspace_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.ProPresenterWorkspace)
  })
_sym_db.RegisterMessage(ProPresenterWorkspace)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROPRESENTERWORKSPACE._serialized_start=163
  _PROPRESENTERWORKSPACE._serialized_end=767
# @@protoc_insertion_point(module_scope)
