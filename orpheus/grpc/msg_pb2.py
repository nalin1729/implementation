# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\tmsg.proto\"\x07\n\x05\x45mpty\"\x19\n\nBasicReply\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x19\n\x06Record\x12\x0f\n\x07\x63olumns\x18\x01 \x03(\t\" \n\x07Records\x12\x15\n\x04rows\x18\x01 \x03(\x0b\x32\x07.Record\"\x1b\n\nRunRequest\x12\r\n\x05query\x18\x01 \x01(\t\"/\n\x08RunReply\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x16\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x08.Records\"<\n\x0bInitRequest\x12\x10\n\x08\x64\x61tafile\x18\x01 \x01(\t\x12\x0b\n\x03\x63vd\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t\"\x1a\n\x0b\x44ropRequest\x12\x0b\n\x03\x63vd\x18\x01 \x01(\t\"\x18\n\x08Versions\x12\x0c\n\x04vals\x18\x01 \x03(\x05\"\x8b\x01\n\x0f\x43heckoutRequest\x12\x0b\n\x03\x63vd\x18\x01 \x01(\t\x12\x1a\n\x07version\x18\x02 \x01(\x0b\x32\t.Versions\x12\x0c\n\x04\x66ile\x18\x03 \x01(\t\x12\r\n\x05table\x18\x04 \x01(\t\x12\x12\n\ndelimiters\x18\x05 \x01(\t\x12\x0e\n\x06header\x18\x06 \x01(\x08\x12\x0e\n\x06ignore\x18\x07 \x01(\x08\"a\n\rCommitRequest\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x12\n\ndelimiters\x18\x05 \x01(\t\x12\x0e\n\x06header\x18\x06 \x01(\x08\x32\xe9\x01\n\x07Orpheus\x12#\n\x04init\x12\x0c.InitRequest\x1a\x0b.BasicReply\"\x00\x12\x1d\n\x04list\x12\x06.Empty\x1a\x0b.BasicReply\"\x00\x12#\n\x04\x64rop\x12\x0c.DropRequest\x1a\x0b.BasicReply\"\x00\x12+\n\x08\x63heckout\x12\x10.CheckoutRequest\x1a\x0b.BasicReply\"\x00\x12\'\n\x06\x63ommit\x12\x0e.CommitRequest\x1a\x0b.BasicReply\"\x00\x12\x1f\n\x03run\x12\x0b.RunRequest\x1a\t.RunReply\"\x00\x62\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=20,
)


_BASICREPLY = _descriptor.Descriptor(
  name='BasicReply',
  full_name='BasicReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='BasicReply.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=47,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='Record.columns', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=74,
)


_RECORDS = _descriptor.Descriptor(
  name='Records',
  full_name='Records',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='Records.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=108,
)


_RUNREQUEST = _descriptor.Descriptor(
  name='RunRequest',
  full_name='RunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='RunRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=137,
)


_RUNREPLY = _descriptor.Descriptor(
  name='RunReply',
  full_name='RunReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='RunReply.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RunReply.data', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=186,
)


_INITREQUEST = _descriptor.Descriptor(
  name='InitRequest',
  full_name='InitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datafile', full_name='InitRequest.datafile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvd', full_name='InitRequest.cvd', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schema', full_name='InitRequest.schema', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=248,
)


_DROPREQUEST = _descriptor.Descriptor(
  name='DropRequest',
  full_name='DropRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cvd', full_name='DropRequest.cvd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=276,
)


_VERSIONS = _descriptor.Descriptor(
  name='Versions',
  full_name='Versions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vals', full_name='Versions.vals', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=302,
)


_CHECKOUTREQUEST = _descriptor.Descriptor(
  name='CheckoutRequest',
  full_name='CheckoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cvd', full_name='CheckoutRequest.cvd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='CheckoutRequest.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='CheckoutRequest.file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='CheckoutRequest.table', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delimiters', full_name='CheckoutRequest.delimiters', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='CheckoutRequest.header', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore', full_name='CheckoutRequest.ignore', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=444,
)


_COMMITREQUEST = _descriptor.Descriptor(
  name='CommitRequest',
  full_name='CommitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='CommitRequest.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='CommitRequest.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='CommitRequest.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delimiters', full_name='CommitRequest.delimiters', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='CommitRequest.header', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=543,
)

_RECORDS.fields_by_name['rows'].message_type = _RECORD
_RUNREPLY.fields_by_name['data'].message_type = _RECORDS
_CHECKOUTREQUEST.fields_by_name['version'].message_type = _VERSIONS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['BasicReply'] = _BASICREPLY
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['Records'] = _RECORDS
DESCRIPTOR.message_types_by_name['RunRequest'] = _RUNREQUEST
DESCRIPTOR.message_types_by_name['RunReply'] = _RUNREPLY
DESCRIPTOR.message_types_by_name['InitRequest'] = _INITREQUEST
DESCRIPTOR.message_types_by_name['DropRequest'] = _DROPREQUEST
DESCRIPTOR.message_types_by_name['Versions'] = _VERSIONS
DESCRIPTOR.message_types_by_name['CheckoutRequest'] = _CHECKOUTREQUEST
DESCRIPTOR.message_types_by_name['CommitRequest'] = _COMMITREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)

BasicReply = _reflection.GeneratedProtocolMessageType('BasicReply', (_message.Message,), dict(
  DESCRIPTOR = _BASICREPLY,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:BasicReply)
  ))
_sym_db.RegisterMessage(BasicReply)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Record)
  ))
_sym_db.RegisterMessage(Record)

Records = _reflection.GeneratedProtocolMessageType('Records', (_message.Message,), dict(
  DESCRIPTOR = _RECORDS,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Records)
  ))
_sym_db.RegisterMessage(Records)

RunRequest = _reflection.GeneratedProtocolMessageType('RunRequest', (_message.Message,), dict(
  DESCRIPTOR = _RUNREQUEST,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:RunRequest)
  ))
_sym_db.RegisterMessage(RunRequest)

RunReply = _reflection.GeneratedProtocolMessageType('RunReply', (_message.Message,), dict(
  DESCRIPTOR = _RUNREPLY,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:RunReply)
  ))
_sym_db.RegisterMessage(RunReply)

InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITREQUEST,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:InitRequest)
  ))
_sym_db.RegisterMessage(InitRequest)

DropRequest = _reflection.GeneratedProtocolMessageType('DropRequest', (_message.Message,), dict(
  DESCRIPTOR = _DROPREQUEST,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:DropRequest)
  ))
_sym_db.RegisterMessage(DropRequest)

Versions = _reflection.GeneratedProtocolMessageType('Versions', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONS,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Versions)
  ))
_sym_db.RegisterMessage(Versions)

CheckoutRequest = _reflection.GeneratedProtocolMessageType('CheckoutRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKOUTREQUEST,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:CheckoutRequest)
  ))
_sym_db.RegisterMessage(CheckoutRequest)

CommitRequest = _reflection.GeneratedProtocolMessageType('CommitRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMMITREQUEST,
  __module__ = 'msg_pb2'
  # @@protoc_insertion_point(class_scope:CommitRequest)
  ))
_sym_db.RegisterMessage(CommitRequest)



_ORPHEUS = _descriptor.ServiceDescriptor(
  name='Orpheus',
  full_name='Orpheus',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=546,
  serialized_end=779,
  methods=[
  _descriptor.MethodDescriptor(
    name='init',
    full_name='Orpheus.init',
    index=0,
    containing_service=None,
    input_type=_INITREQUEST,
    output_type=_BASICREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='Orpheus.list',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_BASICREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='drop',
    full_name='Orpheus.drop',
    index=2,
    containing_service=None,
    input_type=_DROPREQUEST,
    output_type=_BASICREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='checkout',
    full_name='Orpheus.checkout',
    index=3,
    containing_service=None,
    input_type=_CHECKOUTREQUEST,
    output_type=_BASICREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='commit',
    full_name='Orpheus.commit',
    index=4,
    containing_service=None,
    input_type=_COMMITREQUEST,
    output_type=_BASICREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='run',
    full_name='Orpheus.run',
    index=5,
    containing_service=None,
    input_type=_RUNREQUEST,
    output_type=_RUNREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORPHEUS)

DESCRIPTOR.services_by_name['Orpheus'] = _ORPHEUS

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class OrpheusStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.init = channel.unary_unary(
          '/Orpheus/init',
          request_serializer=InitRequest.SerializeToString,
          response_deserializer=BasicReply.FromString,
          )
      self.list = channel.unary_unary(
          '/Orpheus/list',
          request_serializer=Empty.SerializeToString,
          response_deserializer=BasicReply.FromString,
          )
      self.drop = channel.unary_unary(
          '/Orpheus/drop',
          request_serializer=DropRequest.SerializeToString,
          response_deserializer=BasicReply.FromString,
          )
      self.checkout = channel.unary_unary(
          '/Orpheus/checkout',
          request_serializer=CheckoutRequest.SerializeToString,
          response_deserializer=BasicReply.FromString,
          )
      self.commit = channel.unary_unary(
          '/Orpheus/commit',
          request_serializer=CommitRequest.SerializeToString,
          response_deserializer=BasicReply.FromString,
          )
      self.run = channel.unary_unary(
          '/Orpheus/run',
          request_serializer=RunRequest.SerializeToString,
          response_deserializer=RunReply.FromString,
          )


  class OrpheusServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def init(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def drop(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def checkout(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def commit(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def run(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_OrpheusServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'init': grpc.unary_unary_rpc_method_handler(
            servicer.init,
            request_deserializer=InitRequest.FromString,
            response_serializer=BasicReply.SerializeToString,
        ),
        'list': grpc.unary_unary_rpc_method_handler(
            servicer.list,
            request_deserializer=Empty.FromString,
            response_serializer=BasicReply.SerializeToString,
        ),
        'drop': grpc.unary_unary_rpc_method_handler(
            servicer.drop,
            request_deserializer=DropRequest.FromString,
            response_serializer=BasicReply.SerializeToString,
        ),
        'checkout': grpc.unary_unary_rpc_method_handler(
            servicer.checkout,
            request_deserializer=CheckoutRequest.FromString,
            response_serializer=BasicReply.SerializeToString,
        ),
        'commit': grpc.unary_unary_rpc_method_handler(
            servicer.commit,
            request_deserializer=CommitRequest.FromString,
            response_serializer=BasicReply.SerializeToString,
        ),
        'run': grpc.unary_unary_rpc_method_handler(
            servicer.run,
            request_deserializer=RunRequest.FromString,
            response_serializer=RunReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Orpheus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaOrpheusServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def init(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def list(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def drop(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def checkout(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def commit(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def run(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaOrpheusStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def init(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    init.future = None
    def list(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    list.future = None
    def drop(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    drop.future = None
    def checkout(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    checkout.future = None
    def commit(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    commit.future = None
    def run(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    run.future = None


  def beta_create_Orpheus_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Orpheus', 'checkout'): CheckoutRequest.FromString,
      ('Orpheus', 'commit'): CommitRequest.FromString,
      ('Orpheus', 'drop'): DropRequest.FromString,
      ('Orpheus', 'init'): InitRequest.FromString,
      ('Orpheus', 'list'): Empty.FromString,
      ('Orpheus', 'run'): RunRequest.FromString,
    }
    response_serializers = {
      ('Orpheus', 'checkout'): BasicReply.SerializeToString,
      ('Orpheus', 'commit'): BasicReply.SerializeToString,
      ('Orpheus', 'drop'): BasicReply.SerializeToString,
      ('Orpheus', 'init'): BasicReply.SerializeToString,
      ('Orpheus', 'list'): BasicReply.SerializeToString,
      ('Orpheus', 'run'): RunReply.SerializeToString,
    }
    method_implementations = {
      ('Orpheus', 'checkout'): face_utilities.unary_unary_inline(servicer.checkout),
      ('Orpheus', 'commit'): face_utilities.unary_unary_inline(servicer.commit),
      ('Orpheus', 'drop'): face_utilities.unary_unary_inline(servicer.drop),
      ('Orpheus', 'init'): face_utilities.unary_unary_inline(servicer.init),
      ('Orpheus', 'list'): face_utilities.unary_unary_inline(servicer.list),
      ('Orpheus', 'run'): face_utilities.unary_unary_inline(servicer.run),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Orpheus_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Orpheus', 'checkout'): CheckoutRequest.SerializeToString,
      ('Orpheus', 'commit'): CommitRequest.SerializeToString,
      ('Orpheus', 'drop'): DropRequest.SerializeToString,
      ('Orpheus', 'init'): InitRequest.SerializeToString,
      ('Orpheus', 'list'): Empty.SerializeToString,
      ('Orpheus', 'run'): RunRequest.SerializeToString,
    }
    response_deserializers = {
      ('Orpheus', 'checkout'): BasicReply.FromString,
      ('Orpheus', 'commit'): BasicReply.FromString,
      ('Orpheus', 'drop'): BasicReply.FromString,
      ('Orpheus', 'init'): BasicReply.FromString,
      ('Orpheus', 'list'): BasicReply.FromString,
      ('Orpheus', 'run'): RunReply.FromString,
    }
    cardinalities = {
      'checkout': cardinality.Cardinality.UNARY_UNARY,
      'commit': cardinality.Cardinality.UNARY_UNARY,
      'drop': cardinality.Cardinality.UNARY_UNARY,
      'init': cardinality.Cardinality.UNARY_UNARY,
      'list': cardinality.Cardinality.UNARY_UNARY,
      'run': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Orpheus', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)