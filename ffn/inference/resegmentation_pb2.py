# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inference/resegmentation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils import vector_pb2 as utils_dot_vector__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='inference/resegmentation.proto',
  package='ffn',
  syntax='proto2',
  serialized_pb=_b('\n\x1einference/resegmentation.proto\x12\x03\x66\x66n\x1a\x12utils/vector.proto\"\xc1\x03\n\x1c\x45ndpointResegmentationResult\x12\n\n\x02id\x18\x01 \x01(\x04\x12\"\n\x05start\x18\x02 \x01(\x0b\x32\x13.ffn.proto.Vector3j\x12\x12\n\nnum_voxels\x18\x03 \x01(\x05\x12\x41\n\x08overlaps\x18\x04 \x03(\x0b\x32/.ffn.EndpointResegmentationResult.OverlapsEntry\x12=\n\x06source\x18\x05 \x01(\x0b\x32-.ffn.EndpointResegmentationResult.OverlapInfo\x12\x30\n\x13segmentation_radius\x18\x06 \x01(\x0b\x32\x13.ffn.proto.Vector3j\x12\x0b\n\x03tag\x18\x07 \x01(\t\x1a<\n\x0bOverlapInfo\x12\x17\n\x0fnum_overlapping\x18\x01 \x01(\x05\x12\x14\n\x0cnum_original\x18\x02 \x01(\x05\x1a^\n\rOverlapsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.ffn.EndpointResegmentationResult.OverlapInfo:\x02\x38\x01\"\x90\x05\n\x18PairResegmentationResult\x12\"\n\x05point\x18\x01 \x01(\x0b\x32\x13.ffn.proto.Vector3j\x12\x0c\n\x04id_a\x18\x02 \x01(\x04\x12\x0c\n\x04id_b\x18\x03 \x01(\x04\x12\x30\n\x13segmentation_radius\x18\x04 \x01(\x0b\x32\x13.ffn.proto.Vector3j\x12\x0b\n\x03tag\x18\x05 \x01(\t\x12\x36\n\x04\x65val\x18\x06 \x01(\x0b\x32(.ffn.PairResegmentationResult.EvalResult\x1a\xaf\x01\n\rSegmentResult\x12#\n\x06origin\x18\x01 \x01(\x0b\x32\x13.ffn.proto.Vector3j\x12\x12\n\nnum_voxels\x18\x02 \x01(\x05\x12\x16\n\x0e\x64\x65leted_voxels\x18\x03 \x01(\x05\x12\x1d\n\x15segment_a_consistency\x18\x04 \x01(\x02\x12\x1d\n\x15segment_b_consistency\x18\x05 \x01(\x02\x12\x0f\n\x07max_edt\x18\x06 \x01(\x02\x1a\x8a\x02\n\nEvalResult\x12#\n\x06radius\x18\x01 \x01(\x0b\x32\x13.ffn.proto.Vector3j\x12\x0b\n\x03iou\x18\x02 \x01(\x02\x12;\n\x06\x66rom_a\x18\x03 \x01(\x0b\x32+.ffn.PairResegmentationResult.SegmentResult\x12;\n\x06\x66rom_b\x18\x04 \x01(\x0b\x32+.ffn.PairResegmentationResult.SegmentResult\x12\x11\n\tmax_edt_a\x18\x05 \x01(\x02\x12\x11\n\tmax_edt_b\x18\x06 \x01(\x02\x12\x14\n\x0cnum_voxels_a\x18\x07 \x01(\x05\x12\x14\n\x0cnum_voxels_b\x18\x08 \x01(\x05')
  ,
  dependencies=[utils_dot_vector__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENDPOINTRESEGMENTATIONRESULT_OVERLAPINFO = _descriptor.Descriptor(
  name='OverlapInfo',
  full_name='ffn.EndpointResegmentationResult.OverlapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_overlapping', full_name='ffn.EndpointResegmentationResult.OverlapInfo.num_overlapping', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_original', full_name='ffn.EndpointResegmentationResult.OverlapInfo.num_original', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=413,
)

_ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY = _descriptor.Descriptor(
  name='OverlapsEntry',
  full_name='ffn.EndpointResegmentationResult.OverlapsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ffn.EndpointResegmentationResult.OverlapsEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ffn.EndpointResegmentationResult.OverlapsEntry.value', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=509,
)

_ENDPOINTRESEGMENTATIONRESULT = _descriptor.Descriptor(
  name='EndpointResegmentationResult',
  full_name='ffn.EndpointResegmentationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ffn.EndpointResegmentationResult.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ffn.EndpointResegmentationResult.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_voxels', full_name='ffn.EndpointResegmentationResult.num_voxels', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlaps', full_name='ffn.EndpointResegmentationResult.overlaps', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='ffn.EndpointResegmentationResult.source', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segmentation_radius', full_name='ffn.EndpointResegmentationResult.segmentation_radius', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='ffn.EndpointResegmentationResult.tag', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENDPOINTRESEGMENTATIONRESULT_OVERLAPINFO, _ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=509,
)


_PAIRRESEGMENTATIONRESULT_SEGMENTRESULT = _descriptor.Descriptor(
  name='SegmentResult',
  full_name='ffn.PairResegmentationResult.SegmentResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='ffn.PairResegmentationResult.SegmentResult.origin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_voxels', full_name='ffn.PairResegmentationResult.SegmentResult.num_voxels', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted_voxels', full_name='ffn.PairResegmentationResult.SegmentResult.deleted_voxels', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segment_a_consistency', full_name='ffn.PairResegmentationResult.SegmentResult.segment_a_consistency', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segment_b_consistency', full_name='ffn.PairResegmentationResult.SegmentResult.segment_b_consistency', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_edt', full_name='ffn.PairResegmentationResult.SegmentResult.max_edt', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=899,
)

_PAIRRESEGMENTATIONRESULT_EVALRESULT = _descriptor.Descriptor(
  name='EvalResult',
  full_name='ffn.PairResegmentationResult.EvalResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='radius', full_name='ffn.PairResegmentationResult.EvalResult.radius', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iou', full_name='ffn.PairResegmentationResult.EvalResult.iou', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_a', full_name='ffn.PairResegmentationResult.EvalResult.from_a', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_b', full_name='ffn.PairResegmentationResult.EvalResult.from_b', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_edt_a', full_name='ffn.PairResegmentationResult.EvalResult.max_edt_a', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_edt_b', full_name='ffn.PairResegmentationResult.EvalResult.max_edt_b', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_voxels_a', full_name='ffn.PairResegmentationResult.EvalResult.num_voxels_a', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_voxels_b', full_name='ffn.PairResegmentationResult.EvalResult.num_voxels_b', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=902,
  serialized_end=1168,
)

_PAIRRESEGMENTATIONRESULT = _descriptor.Descriptor(
  name='PairResegmentationResult',
  full_name='ffn.PairResegmentationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='ffn.PairResegmentationResult.point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id_a', full_name='ffn.PairResegmentationResult.id_a', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id_b', full_name='ffn.PairResegmentationResult.id_b', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segmentation_radius', full_name='ffn.PairResegmentationResult.segmentation_radius', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='ffn.PairResegmentationResult.tag', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval', full_name='ffn.PairResegmentationResult.eval', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PAIRRESEGMENTATIONRESULT_SEGMENTRESULT, _PAIRRESEGMENTATIONRESULT_EVALRESULT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=1168,
)

_ENDPOINTRESEGMENTATIONRESULT_OVERLAPINFO.containing_type = _ENDPOINTRESEGMENTATIONRESULT
_ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY.fields_by_name['value'].message_type = _ENDPOINTRESEGMENTATIONRESULT_OVERLAPINFO
_ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY.containing_type = _ENDPOINTRESEGMENTATIONRESULT
_ENDPOINTRESEGMENTATIONRESULT.fields_by_name['start'].message_type = utils_dot_vector__pb2._VECTOR3J
_ENDPOINTRESEGMENTATIONRESULT.fields_by_name['overlaps'].message_type = _ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY
_ENDPOINTRESEGMENTATIONRESULT.fields_by_name['source'].message_type = _ENDPOINTRESEGMENTATIONRESULT_OVERLAPINFO
_ENDPOINTRESEGMENTATIONRESULT.fields_by_name['segmentation_radius'].message_type = utils_dot_vector__pb2._VECTOR3J
_PAIRRESEGMENTATIONRESULT_SEGMENTRESULT.fields_by_name['origin'].message_type = utils_dot_vector__pb2._VECTOR3J
_PAIRRESEGMENTATIONRESULT_SEGMENTRESULT.containing_type = _PAIRRESEGMENTATIONRESULT
_PAIRRESEGMENTATIONRESULT_EVALRESULT.fields_by_name['radius'].message_type = utils_dot_vector__pb2._VECTOR3J
_PAIRRESEGMENTATIONRESULT_EVALRESULT.fields_by_name['from_a'].message_type = _PAIRRESEGMENTATIONRESULT_SEGMENTRESULT
_PAIRRESEGMENTATIONRESULT_EVALRESULT.fields_by_name['from_b'].message_type = _PAIRRESEGMENTATIONRESULT_SEGMENTRESULT
_PAIRRESEGMENTATIONRESULT_EVALRESULT.containing_type = _PAIRRESEGMENTATIONRESULT
_PAIRRESEGMENTATIONRESULT.fields_by_name['point'].message_type = utils_dot_vector__pb2._VECTOR3J
_PAIRRESEGMENTATIONRESULT.fields_by_name['segmentation_radius'].message_type = utils_dot_vector__pb2._VECTOR3J
_PAIRRESEGMENTATIONRESULT.fields_by_name['eval'].message_type = _PAIRRESEGMENTATIONRESULT_EVALRESULT
DESCRIPTOR.message_types_by_name['EndpointResegmentationResult'] = _ENDPOINTRESEGMENTATIONRESULT
DESCRIPTOR.message_types_by_name['PairResegmentationResult'] = _PAIRRESEGMENTATIONRESULT

EndpointResegmentationResult = _reflection.GeneratedProtocolMessageType('EndpointResegmentationResult', (_message.Message,), dict(

  OverlapInfo = _reflection.GeneratedProtocolMessageType('OverlapInfo', (_message.Message,), dict(
    DESCRIPTOR = _ENDPOINTRESEGMENTATIONRESULT_OVERLAPINFO,
    __module__ = 'inference.resegmentation_pb2'
    # @@protoc_insertion_point(class_scope:ffn.EndpointResegmentationResult.OverlapInfo)
    ))
  ,

  OverlapsEntry = _reflection.GeneratedProtocolMessageType('OverlapsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY,
    __module__ = 'inference.resegmentation_pb2'
    # @@protoc_insertion_point(class_scope:ffn.EndpointResegmentationResult.OverlapsEntry)
    ))
  ,
  DESCRIPTOR = _ENDPOINTRESEGMENTATIONRESULT,
  __module__ = 'inference.resegmentation_pb2'
  # @@protoc_insertion_point(class_scope:ffn.EndpointResegmentationResult)
  ))
_sym_db.RegisterMessage(EndpointResegmentationResult)
_sym_db.RegisterMessage(EndpointResegmentationResult.OverlapInfo)
_sym_db.RegisterMessage(EndpointResegmentationResult.OverlapsEntry)

PairResegmentationResult = _reflection.GeneratedProtocolMessageType('PairResegmentationResult', (_message.Message,), dict(

  SegmentResult = _reflection.GeneratedProtocolMessageType('SegmentResult', (_message.Message,), dict(
    DESCRIPTOR = _PAIRRESEGMENTATIONRESULT_SEGMENTRESULT,
    __module__ = 'inference.resegmentation_pb2'
    # @@protoc_insertion_point(class_scope:ffn.PairResegmentationResult.SegmentResult)
    ))
  ,

  EvalResult = _reflection.GeneratedProtocolMessageType('EvalResult', (_message.Message,), dict(
    DESCRIPTOR = _PAIRRESEGMENTATIONRESULT_EVALRESULT,
    __module__ = 'inference.resegmentation_pb2'
    # @@protoc_insertion_point(class_scope:ffn.PairResegmentationResult.EvalResult)
    ))
  ,
  DESCRIPTOR = _PAIRRESEGMENTATIONRESULT,
  __module__ = 'inference.resegmentation_pb2'
  # @@protoc_insertion_point(class_scope:ffn.PairResegmentationResult)
  ))
_sym_db.RegisterMessage(PairResegmentationResult)
_sym_db.RegisterMessage(PairResegmentationResult.SegmentResult)
_sym_db.RegisterMessage(PairResegmentationResult.EvalResult)


_ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY.has_options = True
_ENDPOINTRESEGMENTATIONRESULT_OVERLAPSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
