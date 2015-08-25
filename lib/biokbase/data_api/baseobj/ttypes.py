#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Metadata(object):
  """
  Default metadata for an object.

  Attributes:
   - object_id
   - object_name
   - object_reference
   - object_reference_versioned
   - type
   - save_date
   - version
   - saved_by
   - workspace_id
   - workspace_name
   - object_checksum
   - object_size
   - object_metadata
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'object_id', None, None, ), # 1
    (2, TType.STRING, 'object_name', None, None, ), # 2
    (3, TType.STRING, 'object_reference', None, None, ), # 3
    (4, TType.STRING, 'object_reference_versioned', None, None, ), # 4
    (5, TType.STRING, 'type', None, None, ), # 5
    (6, TType.STRING, 'save_date', None, None, ), # 6
    (7, TType.STRING, 'version', None, None, ), # 7
    (8, TType.STRING, 'saved_by', None, None, ), # 8
    (9, TType.STRING, 'workspace_id', None, None, ), # 9
    (10, TType.STRING, 'workspace_name', None, None, ), # 10
    (11, TType.I64, 'object_checksum', None, None, ), # 11
    (12, TType.I64, 'object_size', None, None, ), # 12
    (13, TType.STRING, 'object_metadata', None, None, ), # 13
  )

  def __init__(self, object_id=None, object_name=None, object_reference=None, object_reference_versioned=None, type=None, save_date=None, version=None, saved_by=None, workspace_id=None, workspace_name=None, object_checksum=None, object_size=None, object_metadata=None,):
    self.object_id = object_id
    self.object_name = object_name
    self.object_reference = object_reference
    self.object_reference_versioned = object_reference_versioned
    self.type = type
    self.save_date = save_date
    self.version = version
    self.saved_by = saved_by
    self.workspace_id = workspace_id
    self.workspace_name = workspace_name
    self.object_checksum = object_checksum
    self.object_size = object_size
    self.object_metadata = object_metadata

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.object_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.object_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.object_reference = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.object_reference_versioned = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.type = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.save_date = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.version = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.saved_by = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.workspace_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.workspace_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I64:
          self.object_checksum = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I64:
          self.object_size = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.STRING:
          self.object_metadata = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Metadata')
    if self.object_id is not None:
      oprot.writeFieldBegin('object_id', TType.STRING, 1)
      oprot.writeString(self.object_id)
      oprot.writeFieldEnd()
    if self.object_name is not None:
      oprot.writeFieldBegin('object_name', TType.STRING, 2)
      oprot.writeString(self.object_name)
      oprot.writeFieldEnd()
    if self.object_reference is not None:
      oprot.writeFieldBegin('object_reference', TType.STRING, 3)
      oprot.writeString(self.object_reference)
      oprot.writeFieldEnd()
    if self.object_reference_versioned is not None:
      oprot.writeFieldBegin('object_reference_versioned', TType.STRING, 4)
      oprot.writeString(self.object_reference_versioned)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.STRING, 5)
      oprot.writeString(self.type)
      oprot.writeFieldEnd()
    if self.save_date is not None:
      oprot.writeFieldBegin('save_date', TType.STRING, 6)
      oprot.writeString(self.save_date)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 7)
      oprot.writeString(self.version)
      oprot.writeFieldEnd()
    if self.saved_by is not None:
      oprot.writeFieldBegin('saved_by', TType.STRING, 8)
      oprot.writeString(self.saved_by)
      oprot.writeFieldEnd()
    if self.workspace_id is not None:
      oprot.writeFieldBegin('workspace_id', TType.STRING, 9)
      oprot.writeString(self.workspace_id)
      oprot.writeFieldEnd()
    if self.workspace_name is not None:
      oprot.writeFieldBegin('workspace_name', TType.STRING, 10)
      oprot.writeString(self.workspace_name)
      oprot.writeFieldEnd()
    if self.object_checksum is not None:
      oprot.writeFieldBegin('object_checksum', TType.I64, 11)
      oprot.writeI64(self.object_checksum)
      oprot.writeFieldEnd()
    if self.object_size is not None:
      oprot.writeFieldBegin('object_size', TType.I64, 12)
      oprot.writeI64(self.object_size)
      oprot.writeFieldEnd()
    if self.object_metadata is not None:
      oprot.writeFieldBegin('object_metadata', TType.STRING, 13)
      oprot.writeString(self.object_metadata)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.object_id)
    value = (value * 31) ^ hash(self.object_name)
    value = (value * 31) ^ hash(self.object_reference)
    value = (value * 31) ^ hash(self.object_reference_versioned)
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.save_date)
    value = (value * 31) ^ hash(self.version)
    value = (value * 31) ^ hash(self.saved_by)
    value = (value * 31) ^ hash(self.workspace_id)
    value = (value * 31) ^ hash(self.workspace_name)
    value = (value * 31) ^ hash(self.object_checksum)
    value = (value * 31) ^ hash(self.object_size)
    value = (value * 31) ^ hash(self.object_metadata)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class History(object):
  """
  Object history.

  Attributes:
   - events
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'events', (TType.STRING,None), None, ), # 1
  )

  def __init__(self, events=None,):
    self.events = events

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.events = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.events.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('History')
    if self.events is not None:
      oprot.writeFieldBegin('events', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.events))
      for iter6 in self.events:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.events)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Provenance(object):
  """
  Object provenance.

  Attributes:
   - where_i_came_from
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'where_i_came_from', None, None, ), # 1
  )

  def __init__(self, where_i_came_from=None,):
    self.where_i_came_from = where_i_came_from

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.where_i_came_from = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Provenance')
    if self.where_i_came_from is not None:
      oprot.writeFieldBegin('where_i_came_from', TType.STRING, 1)
      oprot.writeString(self.where_i_came_from)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.where_i_came_from)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AuthInfo(object):
  """
  Authorization info

  Attributes:
   - token
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'token', None, None, ), # 1
  )

  def __init__(self, token=None,):
    self.token = token

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.token = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AuthInfo')
    if self.token is not None:
      oprot.writeFieldBegin('token', TType.STRING, 1)
      oprot.writeString(self.token)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.token)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
