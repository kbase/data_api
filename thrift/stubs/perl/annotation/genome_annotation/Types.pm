#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
require 5.6.0;
use strict;
use warnings;
use Thrift;

package genome_annotation::ServiceException;
use base qw(Thrift::TException);
use base qw(Class::Accessor);
genome_annotation::ServiceException->mk_accessors( qw( message stacktrace inputs ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{message} = undef;
  $self->{stacktrace} = undef;
  $self->{inputs} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{message}) {
      $self->{message} = $vals->{message};
    }
    if (defined $vals->{stacktrace}) {
      $self->{stacktrace} = $vals->{stacktrace};
    }
    if (defined $vals->{inputs}) {
      $self->{inputs} = $vals->{inputs};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'ServiceException';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{message});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{stacktrace});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^3$/ && do{      if ($ftype == TType::MAP) {
        {
          my $_size0 = 0;
          $self->{inputs} = {};
          my $_ktype1 = 0;
          my $_vtype2 = 0;
          $xfer += $input->readMapBegin(\$_ktype1, \$_vtype2, \$_size0);
          for (my $_i4 = 0; $_i4 < $_size0; ++$_i4)
          {
            my $key5 = '';
            my $val6 = '';
            $xfer += $input->readString(\$key5);
            $xfer += $input->readString(\$val6);
            $self->{inputs}->{$key5} = $val6;
          }
          $xfer += $input->readMapEnd();
        }
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('ServiceException');
  if (defined $self->{message}) {
    $xfer += $output->writeFieldBegin('message', TType::STRING, 1);
    $xfer += $output->writeString($self->{message});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{stacktrace}) {
    $xfer += $output->writeFieldBegin('stacktrace', TType::STRING, 2);
    $xfer += $output->writeString($self->{stacktrace});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{inputs}) {
    $xfer += $output->writeFieldBegin('inputs', TType::MAP, 3);
    {
      $xfer += $output->writeMapBegin(TType::STRING, TType::STRING, scalar(keys %{$self->{inputs}}));
      {
        while( my ($kiter7,$viter8) = each %{$self->{inputs}}) 
        {
          $xfer += $output->writeString($kiter7);
          $xfer += $output->writeString($viter8);
        }
      }
      $xfer += $output->writeMapEnd();
    }
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

package genome_annotation::AuthorizationException;
use base qw(Thrift::TException);
use base qw(Class::Accessor);
genome_annotation::AuthorizationException->mk_accessors( qw( message stacktrace ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{message} = undef;
  $self->{stacktrace} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{message}) {
      $self->{message} = $vals->{message};
    }
    if (defined $vals->{stacktrace}) {
      $self->{stacktrace} = $vals->{stacktrace};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'AuthorizationException';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{message});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{stacktrace});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('AuthorizationException');
  if (defined $self->{message}) {
    $xfer += $output->writeFieldBegin('message', TType::STRING, 1);
    $xfer += $output->writeString($self->{message});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{stacktrace}) {
    $xfer += $output->writeFieldBegin('stacktrace', TType::STRING, 2);
    $xfer += $output->writeString($self->{stacktrace});
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

package genome_annotation::AuthenticationException;
use base qw(Thrift::TException);
use base qw(Class::Accessor);
genome_annotation::AuthenticationException->mk_accessors( qw( message stacktrace ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{message} = undef;
  $self->{stacktrace} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{message}) {
      $self->{message} = $vals->{message};
    }
    if (defined $vals->{stacktrace}) {
      $self->{stacktrace} = $vals->{stacktrace};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'AuthenticationException';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{message});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{stacktrace});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('AuthenticationException');
  if (defined $self->{message}) {
    $xfer += $output->writeFieldBegin('message', TType::STRING, 1);
    $xfer += $output->writeString($self->{message});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{stacktrace}) {
    $xfer += $output->writeFieldBegin('stacktrace', TType::STRING, 2);
    $xfer += $output->writeString($self->{stacktrace});
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

package genome_annotation::ObjectReferenceException;
use base qw(Thrift::TException);
use base qw(Class::Accessor);
genome_annotation::ObjectReferenceException->mk_accessors( qw( message stacktrace ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{message} = undef;
  $self->{stacktrace} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{message}) {
      $self->{message} = $vals->{message};
    }
    if (defined $vals->{stacktrace}) {
      $self->{stacktrace} = $vals->{stacktrace};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'ObjectReferenceException';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{message});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{stacktrace});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('ObjectReferenceException');
  if (defined $self->{message}) {
    $xfer += $output->writeFieldBegin('message', TType::STRING, 1);
    $xfer += $output->writeString($self->{message});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{stacktrace}) {
    $xfer += $output->writeFieldBegin('stacktrace', TType::STRING, 2);
    $xfer += $output->writeString($self->{stacktrace});
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

package genome_annotation::AttributeException;
use base qw(Thrift::TException);
use base qw(Class::Accessor);
genome_annotation::AttributeException->mk_accessors( qw( message stacktrace ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{message} = undef;
  $self->{stacktrace} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{message}) {
      $self->{message} = $vals->{message};
    }
    if (defined $vals->{stacktrace}) {
      $self->{stacktrace} = $vals->{stacktrace};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'AttributeException';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{message});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{stacktrace});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('AttributeException');
  if (defined $self->{message}) {
    $xfer += $output->writeFieldBegin('message', TType::STRING, 1);
    $xfer += $output->writeString($self->{message});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{stacktrace}) {
    $xfer += $output->writeFieldBegin('stacktrace', TType::STRING, 2);
    $xfer += $output->writeString($self->{stacktrace});
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

package genome_annotation::TypeException;
use base qw(Thrift::TException);
use base qw(Class::Accessor);
genome_annotation::TypeException->mk_accessors( qw( message stacktrace valid_types ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{message} = undef;
  $self->{stacktrace} = undef;
  $self->{valid_types} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{message}) {
      $self->{message} = $vals->{message};
    }
    if (defined $vals->{stacktrace}) {
      $self->{stacktrace} = $vals->{stacktrace};
    }
    if (defined $vals->{valid_types}) {
      $self->{valid_types} = $vals->{valid_types};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'TypeException';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{message});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{stacktrace});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^3$/ && do{      if ($ftype == TType::LIST) {
        {
          my $_size9 = 0;
          $self->{valid_types} = [];
          my $_etype12 = 0;
          $xfer += $input->readListBegin(\$_etype12, \$_size9);
          for (my $_i13 = 0; $_i13 < $_size9; ++$_i13)
          {
            my $elem14 = undef;
            $xfer += $input->readString(\$elem14);
            push(@{$self->{valid_types}},$elem14);
          }
          $xfer += $input->readListEnd();
        }
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('TypeException');
  if (defined $self->{message}) {
    $xfer += $output->writeFieldBegin('message', TType::STRING, 1);
    $xfer += $output->writeString($self->{message});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{stacktrace}) {
    $xfer += $output->writeFieldBegin('stacktrace', TType::STRING, 2);
    $xfer += $output->writeString($self->{stacktrace});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{valid_types}) {
    $xfer += $output->writeFieldBegin('valid_types', TType::LIST, 3);
    {
      $xfer += $output->writeListBegin(TType::STRING, scalar(@{$self->{valid_types}}));
      {
        foreach my $iter15 (@{$self->{valid_types}}) 
        {
          $xfer += $output->writeString($iter15);
        }
      }
      $xfer += $output->writeListEnd();
    }
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

package genome_annotation::Region;
use base qw(Class::Accessor);
genome_annotation::Region->mk_accessors( qw( contig_id strand start length ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{contig_id} = undef;
  $self->{strand} = undef;
  $self->{start} = undef;
  $self->{length} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{contig_id}) {
      $self->{contig_id} = $vals->{contig_id};
    }
    if (defined $vals->{strand}) {
      $self->{strand} = $vals->{strand};
    }
    if (defined $vals->{start}) {
      $self->{start} = $vals->{start};
    }
    if (defined $vals->{length}) {
      $self->{length} = $vals->{length};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'Region';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{contig_id});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{strand});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^3$/ && do{      if ($ftype == TType::I64) {
        $xfer += $input->readI64(\$self->{start});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^4$/ && do{      if ($ftype == TType::I64) {
        $xfer += $input->readI64(\$self->{length});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('Region');
  if (defined $self->{contig_id}) {
    $xfer += $output->writeFieldBegin('contig_id', TType::STRING, 1);
    $xfer += $output->writeString($self->{contig_id});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{strand}) {
    $xfer += $output->writeFieldBegin('strand', TType::STRING, 2);
    $xfer += $output->writeString($self->{strand});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{start}) {
    $xfer += $output->writeFieldBegin('start', TType::I64, 3);
    $xfer += $output->writeI64($self->{start});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{length}) {
    $xfer += $output->writeFieldBegin('length', TType::I64, 4);
    $xfer += $output->writeI64($self->{length});
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

package genome_annotation::AssemblyContig;
use base qw(Class::Accessor);
genome_annotation::AssemblyContig->mk_accessors( qw( contig_id sequence length gc_content md5 name description is_complete is_circular ) );

sub new {
  my $classname = shift;
  my $self      = {};
  my $vals      = shift || {};
  $self->{contig_id} = undef;
  $self->{sequence} = undef;
  $self->{length} = undef;
  $self->{gc_content} = undef;
  $self->{md5} = undef;
  $self->{name} = undef;
  $self->{description} = undef;
  $self->{is_complete} = undef;
  $self->{is_circular} = undef;
  if (UNIVERSAL::isa($vals,'HASH')) {
    if (defined $vals->{contig_id}) {
      $self->{contig_id} = $vals->{contig_id};
    }
    if (defined $vals->{sequence}) {
      $self->{sequence} = $vals->{sequence};
    }
    if (defined $vals->{length}) {
      $self->{length} = $vals->{length};
    }
    if (defined $vals->{gc_content}) {
      $self->{gc_content} = $vals->{gc_content};
    }
    if (defined $vals->{md5}) {
      $self->{md5} = $vals->{md5};
    }
    if (defined $vals->{name}) {
      $self->{name} = $vals->{name};
    }
    if (defined $vals->{description}) {
      $self->{description} = $vals->{description};
    }
    if (defined $vals->{is_complete}) {
      $self->{is_complete} = $vals->{is_complete};
    }
    if (defined $vals->{is_circular}) {
      $self->{is_circular} = $vals->{is_circular};
    }
  }
  return bless ($self, $classname);
}

sub getName {
  return 'AssemblyContig';
}

sub read {
  my ($self, $input) = @_;
  my $xfer  = 0;
  my $fname;
  my $ftype = 0;
  my $fid   = 0;
  $xfer += $input->readStructBegin(\$fname);
  while (1) 
  {
    $xfer += $input->readFieldBegin(\$fname, \$ftype, \$fid);
    if ($ftype == TType::STOP) {
      last;
    }
    SWITCH: for($fid)
    {
      /^1$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{contig_id});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^2$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{sequence});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^3$/ && do{      if ($ftype == TType::I64) {
        $xfer += $input->readI64(\$self->{length});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^4$/ && do{      if ($ftype == TType::DOUBLE) {
        $xfer += $input->readDouble(\$self->{gc_content});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^5$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{md5});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^6$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{name});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^7$/ && do{      if ($ftype == TType::STRING) {
        $xfer += $input->readString(\$self->{description});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^8$/ && do{      if ($ftype == TType::BOOL) {
        $xfer += $input->readBool(\$self->{is_complete});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
      /^9$/ && do{      if ($ftype == TType::BOOL) {
        $xfer += $input->readBool(\$self->{is_circular});
      } else {
        $xfer += $input->skip($ftype);
      }
      last; };
        $xfer += $input->skip($ftype);
    }
    $xfer += $input->readFieldEnd();
  }
  $xfer += $input->readStructEnd();
  return $xfer;
}

sub write {
  my ($self, $output) = @_;
  my $xfer   = 0;
  $xfer += $output->writeStructBegin('AssemblyContig');
  if (defined $self->{contig_id}) {
    $xfer += $output->writeFieldBegin('contig_id', TType::STRING, 1);
    $xfer += $output->writeString($self->{contig_id});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{sequence}) {
    $xfer += $output->writeFieldBegin('sequence', TType::STRING, 2);
    $xfer += $output->writeString($self->{sequence});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{length}) {
    $xfer += $output->writeFieldBegin('length', TType::I64, 3);
    $xfer += $output->writeI64($self->{length});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{gc_content}) {
    $xfer += $output->writeFieldBegin('gc_content', TType::DOUBLE, 4);
    $xfer += $output->writeDouble($self->{gc_content});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{md5}) {
    $xfer += $output->writeFieldBegin('md5', TType::STRING, 5);
    $xfer += $output->writeString($self->{md5});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{name}) {
    $xfer += $output->writeFieldBegin('name', TType::STRING, 6);
    $xfer += $output->writeString($self->{name});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{description}) {
    $xfer += $output->writeFieldBegin('description', TType::STRING, 7);
    $xfer += $output->writeString($self->{description});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{is_complete}) {
    $xfer += $output->writeFieldBegin('is_complete', TType::BOOL, 8);
    $xfer += $output->writeBool($self->{is_complete});
    $xfer += $output->writeFieldEnd();
  }
  if (defined $self->{is_circular}) {
    $xfer += $output->writeFieldBegin('is_circular', TType::BOOL, 9);
    $xfer += $output->writeBool($self->{is_circular});
    $xfer += $output->writeFieldEnd();
  }
  $xfer += $output->writeFieldStop();
  $xfer += $output->writeStructEnd();
  return $xfer;
}

1;
