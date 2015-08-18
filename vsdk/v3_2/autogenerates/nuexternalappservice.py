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


from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUExternalAppService(NURESTObject):
    """ Represents a ExternalAppService in the VSD

        Notes:
            Represents an External Service in the Application Designer

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUExternalAppService instead.
    """

    __rest_name__ = u"externalappservice"

    def __init__(self, **kwargs):
        """ Initializes a ExternalAppService instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> externalappservice = NUExternalAppService(id=u'xxxx-xxx-xxx-xxx', name=u'ExternalAppService')
                >>> externalappservice = NUExternalAppService(data=my_dict)
        """

        super(NUExternalAppService, self).__init__()

        # Read/Write Attributes
        
        self._associated_service_egress_group_id = None
        self._associated_service_egress_redirect_id = None
        self._associated_service_ingress_group_id = None
        self._associated_service_ingress_redirect_id = None
        self._description = None
        self._destination_nat_address = None
        self._destination_nat_enabled = None
        self._destination_nat_mask = None
        self._egress_type = None
        self._ingress_type = None
        self._metadata = None
        self._name = None
        self._source_nat_address = None
        self._source_nat_enabled = None
        self._virtual_ip = None
        self._virtual_ip_required = None
        
        self.expose_attribute(local_name=u"associated_service_egress_group_id", remote_name=u"associatedServiceEgressGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_service_egress_redirect_id", remote_name=u"associatedServiceEgressRedirectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_service_ingress_group_id", remote_name=u"associatedServiceIngressGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_service_ingress_redirect_id", remote_name=u"associatedServiceIngressRedirectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"destination_nat_address", remote_name=u"destinationNATAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"destination_nat_enabled", remote_name=u"destinationNATEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"destination_nat_mask", remote_name=u"destinationNATMask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"egress_type", remote_name=u"egressType", attribute_type=str, is_required=False, is_unique=False, choices=[u'REDIRECT', u'ROUTE'])
        self.expose_attribute(local_name=u"ingress_type", remote_name=u"ingressType", attribute_type=str, is_required=False, is_unique=False, choices=[u'REDIRECT', u'ROUTE'])
        self.expose_attribute(local_name=u"metadata", remote_name=u"metadata", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"source_nat_address", remote_name=u"sourceNATAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"source_nat_enabled", remote_name=u"sourceNATEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"virtual_ip", remote_name=u"virtualIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"virtual_ip_required", remote_name=u"virtualIPRequired", attribute_type=bool, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_associated_service_egress_group_id(self):
        """ Get associated_service_egress_group_id value.

            Notes:
                ID of service port group identifying the output ports

                
                This attribute is named `associatedServiceEgressGroupID` in VSD API.
                
        """
        return self._associated_service_egress_group_id

    def _set_associated_service_egress_group_id(self, value):
        """ Set associated_service_egress_group_id value.

            Notes:
                ID of service port group identifying the output ports

                
                This attribute is named `associatedServiceEgressGroupID` in VSD API.
                
        """
        self._associated_service_egress_group_id = value

    associated_service_egress_group_id = property(_get_associated_service_egress_group_id, _set_associated_service_egress_group_id)
    
    def _get_associated_service_egress_redirect_id(self):
        """ Get associated_service_egress_redirect_id value.

            Notes:
                the redirect target ID that identifies the output ports

                
                This attribute is named `associatedServiceEgressRedirectID` in VSD API.
                
        """
        return self._associated_service_egress_redirect_id

    def _set_associated_service_egress_redirect_id(self, value):
        """ Set associated_service_egress_redirect_id value.

            Notes:
                the redirect target ID that identifies the output ports

                
                This attribute is named `associatedServiceEgressRedirectID` in VSD API.
                
        """
        self._associated_service_egress_redirect_id = value

    associated_service_egress_redirect_id = property(_get_associated_service_egress_redirect_id, _set_associated_service_egress_redirect_id)
    
    def _get_associated_service_ingress_group_id(self):
        """ Get associated_service_ingress_group_id value.

            Notes:
                ID of service port group identifying the input ports

                
                This attribute is named `associatedServiceIngressGroupID` in VSD API.
                
        """
        return self._associated_service_ingress_group_id

    def _set_associated_service_ingress_group_id(self, value):
        """ Set associated_service_ingress_group_id value.

            Notes:
                ID of service port group identifying the input ports

                
                This attribute is named `associatedServiceIngressGroupID` in VSD API.
                
        """
        self._associated_service_ingress_group_id = value

    associated_service_ingress_group_id = property(_get_associated_service_ingress_group_id, _set_associated_service_ingress_group_id)
    
    def _get_associated_service_ingress_redirect_id(self):
        """ Get associated_service_ingress_redirect_id value.

            Notes:
                the redirect target ID that identifies the input ports

                
                This attribute is named `associatedServiceIngressRedirectID` in VSD API.
                
        """
        return self._associated_service_ingress_redirect_id

    def _set_associated_service_ingress_redirect_id(self, value):
        """ Set associated_service_ingress_redirect_id value.

            Notes:
                the redirect target ID that identifies the input ports

                
                This attribute is named `associatedServiceIngressRedirectID` in VSD API.
                
        """
        self._associated_service_ingress_redirect_id = value

    associated_service_ingress_redirect_id = property(_get_associated_service_ingress_redirect_id, _set_associated_service_ingress_redirect_id)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of the flow.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of the flow.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_destination_nat_address(self):
        """ Get destination_nat_address value.

            Notes:
                Destination NAT Address

                
                This attribute is named `destinationNATAddress` in VSD API.
                
        """
        return self._destination_nat_address

    def _set_destination_nat_address(self, value):
        """ Set destination_nat_address value.

            Notes:
                Destination NAT Address

                
                This attribute is named `destinationNATAddress` in VSD API.
                
        """
        self._destination_nat_address = value

    destination_nat_address = property(_get_destination_nat_address, _set_destination_nat_address)
    
    def _get_destination_nat_enabled(self):
        """ Get destination_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `destinationNATEnabled` in VSD API.
                
        """
        return self._destination_nat_enabled

    def _set_destination_nat_enabled(self, value):
        """ Set destination_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `destinationNATEnabled` in VSD API.
                
        """
        self._destination_nat_enabled = value

    destination_nat_enabled = property(_get_destination_nat_enabled, _set_destination_nat_enabled)
    
    def _get_destination_nat_mask(self):
        """ Get destination_nat_mask value.

            Notes:
                netmask of the Destination NAT

                
                This attribute is named `destinationNATMask` in VSD API.
                
        """
        return self._destination_nat_mask

    def _set_destination_nat_mask(self, value):
        """ Set destination_nat_mask value.

            Notes:
                netmask of the Destination NAT

                
                This attribute is named `destinationNATMask` in VSD API.
                
        """
        self._destination_nat_mask = value

    destination_nat_mask = property(_get_destination_nat_mask, _set_destination_nat_mask)
    
    def _get_egress_type(self):
        """ Get egress_type value.

            Notes:
                Egress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .

                
                This attribute is named `egressType` in VSD API.
                
        """
        return self._egress_type

    def _set_egress_type(self, value):
        """ Set egress_type value.

            Notes:
                Egress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .

                
                This attribute is named `egressType` in VSD API.
                
        """
        self._egress_type = value

    egress_type = property(_get_egress_type, _set_egress_type)
    
    def _get_ingress_type(self):
        """ Get ingress_type value.

            Notes:
                Ingress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .

                
                This attribute is named `ingressType` in VSD API.
                
        """
        return self._ingress_type

    def _set_ingress_type(self, value):
        """ Set ingress_type value.

            Notes:
                Ingress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .

                
                This attribute is named `ingressType` in VSD API.
                
        """
        self._ingress_type = value

    ingress_type = property(_get_ingress_type, _set_ingress_type)
    
    def _get_metadata(self):
        """ Get metadata value.

            Notes:
                metadata

                
        """
        return self._metadata

    def _set_metadata(self, value):
        """ Set metadata value.

            Notes:
                metadata

                
        """
        self._metadata = value

    metadata = property(_get_metadata, _set_metadata)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the flow.

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the flow.

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_source_nat_address(self):
        """ Get source_nat_address value.

            Notes:
                Source NAT Address

                
                This attribute is named `sourceNATAddress` in VSD API.
                
        """
        return self._source_nat_address

    def _set_source_nat_address(self, value):
        """ Set source_nat_address value.

            Notes:
                Source NAT Address

                
                This attribute is named `sourceNATAddress` in VSD API.
                
        """
        self._source_nat_address = value

    source_nat_address = property(_get_source_nat_address, _set_source_nat_address)
    
    def _get_source_nat_enabled(self):
        """ Get source_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `sourceNATEnabled` in VSD API.
                
        """
        return self._source_nat_enabled

    def _set_source_nat_enabled(self, value):
        """ Set source_nat_enabled value.

            Notes:
                Boolean flag to indicate whether source NAT is enabled

                
                This attribute is named `sourceNATEnabled` in VSD API.
                
        """
        self._source_nat_enabled = value

    source_nat_enabled = property(_get_source_nat_enabled, _set_source_nat_enabled)
    
    def _get_virtual_ip(self):
        """ Get virtual_ip value.

            Notes:
                Virtual IP Address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        return self._virtual_ip

    def _set_virtual_ip(self, value):
        """ Set virtual_ip value.

            Notes:
                Virtual IP Address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        self._virtual_ip = value

    virtual_ip = property(_get_virtual_ip, _set_virtual_ip)
    
    def _get_virtual_ip_required(self):
        """ Get virtual_ip_required value.

            Notes:
                Boolean flag to indicate whether we require a VIP

                
                This attribute is named `virtualIPRequired` in VSD API.
                
        """
        return self._virtual_ip_required

    def _set_virtual_ip_required(self, value):
        """ Set virtual_ip_required value.

            Notes:
                Boolean flag to indicate whether we require a VIP

                
                This attribute is named `virtualIPRequired` in VSD API.
                
        """
        self._virtual_ip_required = value

    virtual_ip_required = property(_get_virtual_ip_required, _set_virtual_ip_required)
    