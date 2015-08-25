"""
Module for base class for Data API objects.
"""
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO as StringIO

import biokbase.workspace.client
from . import thrift_service

class ObjectImpl(thrift_service.Iface):
    def __init__(self, services=None):
        print("IN ObjectImpl")
        if services is None or type(services) != type({}):
            raise TypeError("You must provide a service configuration "
                            "dictionary! Found {0}".format(type(services)))
        elif not services.has_key("workspace_service_url"):
            raise KeyError("Expecting workspace_service_url key!")
        
        self.services = services
        self.ws_client = None

    def init(self, auth):
        token = auth.token
        self.ws_client = biokbase.workspace.client.Workspace(
            self.services["workspace_service_url"], token=token)


    def get_info(self, ref):
        print("IN get_info: {}".format(ref))
        try:
            info_values = self.ws_client.get_object_info_new({
                "objects": [{"ref": ref}],
                "includeMetadata": 0,
                "ignoreErrors": 0})[0]
        except Exception as err:
            print('get_object_info_new failed: {}'.format(err))
            raise # XXX
        info = {
            "object_id": info_values[0],
            "object_name": info_values[1],
            "object_reference": "{0}/{1}".format(info_values[6],info_values[0]),
            "object_reference_versioned": "{0}/{1}/{2}".format(info_values[6],info_values[0],info_values[4]),
            "type_string": info_values[2],
            "save_date": info_values[3],
            "version": info_values[4],
            "saved_by": info_values[5],
            "workspace_id": info_values[6],
            "workspace_name": info_values[7],
            "object_checksum": info_values[8],
            "object_size": info_values[9],
            "object_metadata": info_values[10]
        }
        return info

    def get_schema(self, ref):
        return self.ws_client.get_type_info(self.get_info(ref)["type_string"])

    def get_history(self):
        return  self.ws_client.get_object_history({"ref": self.ref})

    def get_provenance(self):
        return self.ws_client.get_object_provenance([{"ref": self.ref}])

    def get_data(self):
        return self.ws_client.get_objects([{"ref": self.ref}])[0]["data"]

    def get_data_subset(self, path_list=None):
        return self.ws_client.get_object_subset([{"ref": self.ref,
                        "included": path_list}])[0]["data"]
    
    def get_referrers(self):
        referrers = self.ws_client.list_referencing_objects(
            [{"ref": self.ref}])[0]
        object_refs_by_type = dict()        
        for x in referrers:
            typestring = self.ws_client.translate_to_MD5_types(
                [x[2]]).values()[0]
            if typestring not in object_refs_by_type:
                object_refs_by_type[typestring] = list()
            object_refs_by_type[typestring].append(str(x[6]) + "/" +
                                                   str(x[0]) + "/" +
                                                   str(x[4]))
        return object_refs_by_type

    def translate_to_MD5_types(self, type_list):
        return self.ws_client.translate_to_MD5_types(type_list)