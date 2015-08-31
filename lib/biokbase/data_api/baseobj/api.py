"""
Module for base class for Data API objects.
"""

# Imports

# Stdlib
import json
import logging
import re
# Local
from biokbase.data_api.util import get_logger
from biokbase.data_api.util import log_start, log_end
from biokbase.data_api.util import get_auth_token
from . import thrift_service, ttypes

# Logging

_log = get_logger('object_api')
_log.setLevel(logging.DEBUG)

# Constants

NAMESPACE = 'Object'

REF_PATTERN = re.compile("(.+/.+(/[0-9].+)?)|(ws\.[1-9][0-9]+\.[1-9][0-9]+)")

# Classes and functions

class ObjectAPI(object):
    """API layer over the autogenerated Thrift interface.
    This can handle both local and remote modes by use of alternate
    implementations of the `client` parameter.
    """
    def __init__(self, client, ref):
        """Create API instance with an object reference and client

        Args:
          client (object):  Implementation of thrift_service.Iface
          ref (str): Object reference
        """
        assert isinstance(client, thrift_service.Iface)
        if not REF_PATTERN.match(ref):
            raise ValueError('Format error for "{}"'.format(ref))
        self._client, self._ref = client, ref

        # Set up client
        t0 = log_start(_log, 'client.init')
        auth_info = ttypes.AuthInfo(token=get_auth_token())
        self._client.init(auth_info)
        log_end(_log, t0, 'client.init')

        # Create internal state
        t0 = log_start(_log, 'client.get_info', kvp=dict(ref=ref))
        self._info = self._client.get_info(ref)
        log_end(_log, t0, 'client.get_info')
        self._id = self._info.object_id
        self._name = self._info.object_name
        self._typestring = self._info.type_string
        self._version = self._info.version

    def __str__(self):
        return str(self._info)

    def get_info(self, ref):
        raise RuntimeWarning('get_info() cannot be called directly')

    @property
    def typestring(self):
        return self._typestring

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        data_dict = json.loads(self._client.get_data())
        return data_dict

    def data_subset(self, path_list=None):
        return self._client.get_data_subset(path_list)

    @property
    def schema(self):
        return self._cached('schema')

    @property
    def history(self):
        return self._cached('history')

    @property
    def provenance(self):
        return self._cached('provenance')

    @property
    def referrers(self):
        return self._cached('referrers')

    def _cached(self, name):
        attr_name = '_' + name
        value = getattr(self, attr_name, None)
        if value is None:
            method_name = 'get_' + name
            value = getattr(self._client, method_name)()
            setattr(self, attr_name, value)
        return value
