# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUFlowSecurityPolicy(NURESTObject):
    """ Represents a FlowSecurityPolicy in the VSD

        Notes:
            The security policy on the flow.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUFlowSecurityPolicy instead.
    """

    __rest_name__ = u"flowsecuritypolicy"

    def __init__(self, **kwargs):
        """ Initializes a FlowSecurityPolicy instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> flowsecuritypolicy = NUFlowSecurityPolicy(id=u'xxxx-xxx-xxx-xxx', name=u'FlowSecurityPolicy')
                >>> flowsecuritypolicy = NUFlowSecurityPolicy(data=my_dict)
        """

        super(NUFlowSecurityPolicy, self).__init__()

        # Read/Write Attributes
        
        self._action = None
        self._associated_application_service_id = None
        self._associated_network_object_id = None
        self._associated_network_object_type = None
        self._destination_address_overwrite = None
        self._flow_id = None
        self._priority = None
        self._source_address_overwrite = None
        
        self.expose_attribute(local_name=u"action", remote_name=u"action", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_application_service_id", remote_name=u"associatedApplicationServiceID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_network_object_id", remote_name=u"associatedNetworkObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_network_object_type", remote_name=u"associatedNetworkObjectType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"destination_address_overwrite", remote_name=u"destinationAddressOverwrite", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"flow_id", remote_name=u"flowID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"priority", remote_name=u"priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"source_address_overwrite", remote_name=u"sourceAddressOverwrite", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_action(self):
        """ Get action value.

            Notes:
                The flow action. The action can be either FORWARD or DROP.

                
        """
        return self._action

    def _set_action(self, value):
        """ Set action value.

            Notes:
                The flow action. The action can be either FORWARD or DROP.

                
        """
        self._action = value

    action = property(_get_action, _set_action)
    
    def _get_associated_application_service_id(self):
        """ Get associated_application_service_id value.

            Notes:
                The associated service id.

                
                This attribute is named `associatedApplicationServiceID` in VSD API.
                
        """
        return self._associated_application_service_id

    def _set_associated_application_service_id(self, value):
        """ Set associated_application_service_id value.

            Notes:
                The associated service id.

                
                This attribute is named `associatedApplicationServiceID` in VSD API.
                
        """
        self._associated_application_service_id = value

    associated_application_service_id = property(_get_associated_application_service_id, _set_associated_application_service_id)
    
    def _get_associated_network_object_id(self):
        """ Get associated_network_object_id value.

            Notes:
                The associated network object id.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        return self._associated_network_object_id

    def _set_associated_network_object_id(self, value):
        """ Set associated_network_object_id value.

            Notes:
                The associated network object id.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        self._associated_network_object_id = value

    associated_network_object_id = property(_get_associated_network_object_id, _set_associated_network_object_id)
    
    def _get_associated_network_object_type(self):
        """ Get associated_network_object_type value.

            Notes:
                The associated network object type. Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        return self._associated_network_object_type

    def _set_associated_network_object_type(self, value):
        """ Set associated_network_object_type value.

            Notes:
                The associated network object type. Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        self._associated_network_object_type = value

    associated_network_object_type = property(_get_associated_network_object_type, _set_associated_network_object_type)
    
    def _get_destination_address_overwrite(self):
        """ Get destination_address_overwrite value.

            Notes:
                The destination address overwrite. Needs to be in CIDR format x.x.x.x/n

                
                This attribute is named `destinationAddressOverwrite` in VSD API.
                
        """
        return self._destination_address_overwrite

    def _set_destination_address_overwrite(self, value):
        """ Set destination_address_overwrite value.

            Notes:
                The destination address overwrite. Needs to be in CIDR format x.x.x.x/n

                
                This attribute is named `destinationAddressOverwrite` in VSD API.
                
        """
        self._destination_address_overwrite = value

    destination_address_overwrite = property(_get_destination_address_overwrite, _set_destination_address_overwrite)
    
    def _get_flow_id(self):
        """ Get flow_id value.

            Notes:
                The associated service id.

                
                This attribute is named `flowID` in VSD API.
                
        """
        return self._flow_id

    def _set_flow_id(self, value):
        """ Set flow_id value.

            Notes:
                The associated service id.

                
                This attribute is named `flowID` in VSD API.
                
        """
        self._flow_id = value

    flow_id = property(_get_flow_id, _set_flow_id)
    
    def _get_priority(self):
        """ Get priority value.

            Notes:
                The priority of the flow security policy that determines the order of entries.

                
        """
        return self._priority

    def _set_priority(self, value):
        """ Set priority value.

            Notes:
                The priority of the flow security policy that determines the order of entries.

                
        """
        self._priority = value

    priority = property(_get_priority, _set_priority)
    
    def _get_source_address_overwrite(self):
        """ Get source_address_overwrite value.

            Notes:
                The source address overwrite. Needs to be in CIDR format x.x.x.x/n

                
                This attribute is named `sourceAddressOverwrite` in VSD API.
                
        """
        return self._source_address_overwrite

    def _set_source_address_overwrite(self, value):
        """ Set source_address_overwrite value.

            Notes:
                The source address overwrite. Needs to be in CIDR format x.x.x.x/n

                
                This attribute is named `sourceAddressOverwrite` in VSD API.
                
        """
        self._source_address_overwrite = value

    source_address_overwrite = property(_get_source_address_overwrite, _set_source_address_overwrite)
    