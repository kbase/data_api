#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:twisted
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ServiceException(TException):
  """
  Attributes:
   - message
   - stacktrace
   - inputs
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
    (2, TType.STRING, 'stacktrace', None, None, ), # 2
    (3, TType.MAP, 'inputs', (TType.STRING,None,TType.STRING,None), None, ), # 3
  )

  def __init__(self, message=None, stacktrace=None, inputs=None,):
    self.message = message
    self.stacktrace = stacktrace
    self.inputs = inputs

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
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stacktrace = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.inputs = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString();
            _val6 = iprot.readString();
            self.inputs[_key5] = _val6
          iprot.readMapEnd()
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
    oprot.writeStructBegin('ServiceException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.stacktrace is not None:
      oprot.writeFieldBegin('stacktrace', TType.STRING, 2)
      oprot.writeString(self.stacktrace)
      oprot.writeFieldEnd()
    if self.inputs is not None:
      oprot.writeFieldBegin('inputs', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.inputs))
      for kiter7,viter8 in self.inputs.items():
        oprot.writeString(kiter7)
        oprot.writeString(viter8)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.stacktrace)
    value = (value * 31) ^ hash(self.inputs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AuthorizationException(TException):
  """
  Attributes:
   - message
   - stacktrace
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
    (2, TType.STRING, 'stacktrace', None, None, ), # 2
  )

  def __init__(self, message=None, stacktrace=None,):
    self.message = message
    self.stacktrace = stacktrace

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
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stacktrace = iprot.readString();
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
    oprot.writeStructBegin('AuthorizationException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.stacktrace is not None:
      oprot.writeFieldBegin('stacktrace', TType.STRING, 2)
      oprot.writeString(self.stacktrace)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.stacktrace)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AuthenticationException(TException):
  """
  Attributes:
   - message
   - stacktrace
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
    (2, TType.STRING, 'stacktrace', None, None, ), # 2
  )

  def __init__(self, message=None, stacktrace=None,):
    self.message = message
    self.stacktrace = stacktrace

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
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stacktrace = iprot.readString();
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
    oprot.writeStructBegin('AuthenticationException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.stacktrace is not None:
      oprot.writeFieldBegin('stacktrace', TType.STRING, 2)
      oprot.writeString(self.stacktrace)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.stacktrace)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ObjectReferenceException(TException):
  """
  Attributes:
   - message
   - stacktrace
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
    (2, TType.STRING, 'stacktrace', None, None, ), # 2
  )

  def __init__(self, message=None, stacktrace=None,):
    self.message = message
    self.stacktrace = stacktrace

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
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stacktrace = iprot.readString();
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
    oprot.writeStructBegin('ObjectReferenceException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.stacktrace is not None:
      oprot.writeFieldBegin('stacktrace', TType.STRING, 2)
      oprot.writeString(self.stacktrace)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.stacktrace)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AttributeException(TException):
  """
  Attributes:
   - message
   - stacktrace
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
    (2, TType.STRING, 'stacktrace', None, None, ), # 2
  )

  def __init__(self, message=None, stacktrace=None,):
    self.message = message
    self.stacktrace = stacktrace

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
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stacktrace = iprot.readString();
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
    oprot.writeStructBegin('AttributeException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.stacktrace is not None:
      oprot.writeFieldBegin('stacktrace', TType.STRING, 2)
      oprot.writeString(self.stacktrace)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.stacktrace)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TypeException(TException):
  """
  Attributes:
   - message
   - stacktrace
   - valid_types
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
    (2, TType.STRING, 'stacktrace', None, None, ), # 2
    (3, TType.LIST, 'valid_types', (TType.STRING,None), None, ), # 3
  )

  def __init__(self, message=None, stacktrace=None, valid_types=None,):
    self.message = message
    self.stacktrace = stacktrace
    self.valid_types = valid_types

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
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stacktrace = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.valid_types = []
          (_etype12, _size9) = iprot.readListBegin()
          for _i13 in xrange(_size9):
            _elem14 = iprot.readString();
            self.valid_types.append(_elem14)
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
    oprot.writeStructBegin('TypeException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.stacktrace is not None:
      oprot.writeFieldBegin('stacktrace', TType.STRING, 2)
      oprot.writeString(self.stacktrace)
      oprot.writeFieldEnd()
    if self.valid_types is not None:
      oprot.writeFieldBegin('valid_types', TType.LIST, 3)
      oprot.writeListBegin(TType.STRING, len(self.valid_types))
      for iter15 in self.valid_types:
        oprot.writeString(iter15)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.stacktrace)
    value = (value * 31) ^ hash(self.valid_types)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Region:
  """
  Attributes:
   - contig_id
   - strand
   - start
   - length
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'contig_id', None, None, ), # 1
    (2, TType.STRING, 'strand', None, None, ), # 2
    (3, TType.I64, 'start', None, None, ), # 3
    (4, TType.I64, 'length', None, None, ), # 4
  )

  def __init__(self, contig_id=None, strand=None, start=None, length=None,):
    self.contig_id = contig_id
    self.strand = strand
    self.start = start
    self.length = length

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
          self.contig_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.strand = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.start = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.length = iprot.readI64();
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
    oprot.writeStructBegin('Region')
    if self.contig_id is not None:
      oprot.writeFieldBegin('contig_id', TType.STRING, 1)
      oprot.writeString(self.contig_id)
      oprot.writeFieldEnd()
    if self.strand is not None:
      oprot.writeFieldBegin('strand', TType.STRING, 2)
      oprot.writeString(self.strand)
      oprot.writeFieldEnd()
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I64, 3)
      oprot.writeI64(self.start)
      oprot.writeFieldEnd()
    if self.length is not None:
      oprot.writeFieldBegin('length', TType.I64, 4)
      oprot.writeI64(self.length)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.contig_id)
    value = (value * 31) ^ hash(self.strand)
    value = (value * 31) ^ hash(self.start)
    value = (value * 31) ^ hash(self.length)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AssemblyContig:
  """
  Attributes:
   - contig_id
   - sequence
   - length
   - gc_content
   - md5
   - name
   - description
   - is_complete
   - is_circular
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'contig_id', None, None, ), # 1
    (2, TType.STRING, 'sequence', None, None, ), # 2
    (3, TType.I64, 'length', None, None, ), # 3
    (4, TType.DOUBLE, 'gc_content', None, None, ), # 4
    (5, TType.STRING, 'md5', None, None, ), # 5
    (6, TType.STRING, 'name', None, None, ), # 6
    (7, TType.STRING, 'description', None, None, ), # 7
    (8, TType.BOOL, 'is_complete', None, None, ), # 8
    (9, TType.BOOL, 'is_circular', None, None, ), # 9
  )

  def __init__(self, contig_id=None, sequence=None, length=None, gc_content=None, md5=None, name=None, description=None, is_complete=None, is_circular=None,):
    self.contig_id = contig_id
    self.sequence = sequence
    self.length = length
    self.gc_content = gc_content
    self.md5 = md5
    self.name = name
    self.description = description
    self.is_complete = is_complete
    self.is_circular = is_circular

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
          self.contig_id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.sequence = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.length = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.gc_content = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.md5 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.description = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.is_complete = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.BOOL:
          self.is_circular = iprot.readBool();
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
    oprot.writeStructBegin('AssemblyContig')
    if self.contig_id is not None:
      oprot.writeFieldBegin('contig_id', TType.STRING, 1)
      oprot.writeString(self.contig_id)
      oprot.writeFieldEnd()
    if self.sequence is not None:
      oprot.writeFieldBegin('sequence', TType.STRING, 2)
      oprot.writeString(self.sequence)
      oprot.writeFieldEnd()
    if self.length is not None:
      oprot.writeFieldBegin('length', TType.I64, 3)
      oprot.writeI64(self.length)
      oprot.writeFieldEnd()
    if self.gc_content is not None:
      oprot.writeFieldBegin('gc_content', TType.DOUBLE, 4)
      oprot.writeDouble(self.gc_content)
      oprot.writeFieldEnd()
    if self.md5 is not None:
      oprot.writeFieldBegin('md5', TType.STRING, 5)
      oprot.writeString(self.md5)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 6)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.description is not None:
      oprot.writeFieldBegin('description', TType.STRING, 7)
      oprot.writeString(self.description)
      oprot.writeFieldEnd()
    if self.is_complete is not None:
      oprot.writeFieldBegin('is_complete', TType.BOOL, 8)
      oprot.writeBool(self.is_complete)
      oprot.writeFieldEnd()
    if self.is_circular is not None:
      oprot.writeFieldBegin('is_circular', TType.BOOL, 9)
      oprot.writeBool(self.is_circular)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.contig_id)
    value = (value * 31) ^ hash(self.sequence)
    value = (value * 31) ^ hash(self.length)
    value = (value * 31) ^ hash(self.gc_content)
    value = (value * 31) ^ hash(self.md5)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.description)
    value = (value * 31) ^ hash(self.is_complete)
    value = (value * 31) ^ hash(self.is_circular)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
