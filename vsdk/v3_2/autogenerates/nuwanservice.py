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


from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEnterprisePermissionsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUWANService(NURESTObject):
    """ Represents a WANService in the VSD

        Notes:
            Represents WAN Service Object.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUWANService instead.
    """

    __rest_name__ = u"service"

    def __init__(self, **kwargs):
        """ Initializes a WANService instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> wanservice = NUWANService(id=u'xxxx-xxx-xxx-xxx', name=u'WANService')
                >>> wanservice = NUWANService(data=my_dict)
        """

        super(NUWANService, self).__init__()

        # Read/Write Attributes
        
        self._associated_domain_id = None
        self._associated_vpn_connect_id = None
        self._config_type = None
        self._description = None
        self._domain_name = None
        self._enterprise_name = None
        self._external_route_target = None
        self._irb_enabled = None
        self._name = None
        self._orphan = None
        self._permitted_action = None
        self._service_policy = None
        self._service_type = None
        self._tunnel_type = None
        self._use_user_mnemonic = None
        self._user_mnemonic = None
        self._vn_id = None
        self._wan_service_identifier = None
        
        self.expose_attribute(local_name=u"associated_domain_id", remote_name=u"associatedDomainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_vpn_connect_id", remote_name=u"associatedVPNConnectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"config_type", remote_name=u"configType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DYNAMIC', u'STATIC'])
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"enterprise_name", remote_name=u"enterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"external_route_target", remote_name=u"externalRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"irb_enabled", remote_name=u"IRBEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"orphan", remote_name=u"orphan", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name=u"service_policy", remote_name=u"servicePolicy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"service_type", remote_name=u"serviceType", attribute_type=str, is_required=True, is_unique=False, choices=[u'L2', u'L3'])
        self.expose_attribute(local_name=u"tunnel_type", remote_name=u"tunnelType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC_DEFAULT', u'GRE', u'VXLAN'])
        self.expose_attribute(local_name=u"use_user_mnemonic", remote_name=u"useUserMnemonic", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"user_mnemonic", remote_name=u"userMnemonic", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"vn_id", remote_name=u"vnId", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"wan_service_identifier", remote_name=u"WANServiceIdentifier", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self)
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.permitted_actions = NUPermittedActionsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    def _set_associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    associated_domain_id = property(_get_associated_domain_id, _set_associated_domain_id)
    
    def _get_associated_vpn_connect_id(self):
        """ Get associated_vpn_connect_id value.

            Notes:
                The associated vpn connect ID.

                
                This attribute is named `associatedVPNConnectID` in VSD API.
                
        """
        return self._associated_vpn_connect_id

    def _set_associated_vpn_connect_id(self, value):
        """ Set associated_vpn_connect_id value.

            Notes:
                The associated vpn connect ID.

                
                This attribute is named `associatedVPNConnectID` in VSD API.
                
        """
        self._associated_vpn_connect_id = value

    associated_vpn_connect_id = property(_get_associated_vpn_connect_id, _set_associated_vpn_connect_id)
    
    def _get_config_type(self):
        """ Get config_type value.

            Notes:
                Type of the CONFIG -  STATIC Possible values are STATIC, DYNAMIC, .

                
                This attribute is named `configType` in VSD API.
                
        """
        return self._config_type

    def _set_config_type(self, value):
        """ Set config_type value.

            Notes:
                Type of the CONFIG -  STATIC Possible values are STATIC, DYNAMIC, .

                
                This attribute is named `configType` in VSD API.
                
        """
        self._config_type = value

    config_type = property(_get_config_type, _set_config_type)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the WAN Service

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the WAN Service

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_domain_name(self):
        """ Get domain_name value.

            Notes:
                The associated domain name.

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    def _set_domain_name(self, value):
        """ Set domain_name value.

            Notes:
                The associated domain name.

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    domain_name = property(_get_domain_name, _set_domain_name)
    
    def _get_enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                The associated enterprise name.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    def _set_enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                The associated enterprise name.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    enterprise_name = property(_get_enterprise_name, _set_enterprise_name)
    
    def _get_external_route_target(self):
        """ Get external_route_target value.

            Notes:
                Route target associated with the WAN. It is an optional parameterthat can be provided by the user

                
                This attribute is named `externalRouteTarget` in VSD API.
                
        """
        return self._external_route_target

    def _set_external_route_target(self, value):
        """ Set external_route_target value.

            Notes:
                Route target associated with the WAN. It is an optional parameterthat can be provided by the user

                
                This attribute is named `externalRouteTarget` in VSD API.
                
        """
        self._external_route_target = value

    external_route_target = property(_get_external_route_target, _set_external_route_target)
    
    def _get_irb_enabled(self):
        """ Get irb_enabled value.

            Notes:
                Determines whether Integrated Routing and Bridging is enabled on the WAN Service

                
                This attribute is named `IRBEnabled` in VSD API.
                
        """
        return self._irb_enabled

    def _set_irb_enabled(self, value):
        """ Set irb_enabled value.

            Notes:
                Determines whether Integrated Routing and Bridging is enabled on the WAN Service

                
                This attribute is named `IRBEnabled` in VSD API.
                
        """
        self._irb_enabled = value

    irb_enabled = property(_get_irb_enabled, _set_irb_enabled)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the WAN Service

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the WAN Service

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_orphan(self):
        """ Get orphan value.

            Notes:
                Indicates if this WAN Service is orphan or not.

                
        """
        return self._orphan

    def _set_orphan(self, value):
        """ Set orphan value.

            Notes:
                Indicates if this WAN Service is orphan or not.

                
        """
        self._orphan = value

    orphan = property(_get_orphan, _set_orphan)
    
    def _get_permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    def _set_permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    permitted_action = property(_get_permitted_action, _set_permitted_action)
    
    def _get_service_policy(self):
        """ Get service_policy value.

            Notes:
                Name of 7X50 Policy assoicated with service

                
                This attribute is named `servicePolicy` in VSD API.
                
        """
        return self._service_policy

    def _set_service_policy(self, value):
        """ Set service_policy value.

            Notes:
                Name of 7X50 Policy assoicated with service

                
                This attribute is named `servicePolicy` in VSD API.
                
        """
        self._service_policy = value

    service_policy = property(_get_service_policy, _set_service_policy)
    
    def _get_service_type(self):
        """ Get service_type value.

            Notes:
                Type of the SERVICE -  L3,L2 Possible values are L3, L2, .

                
                This attribute is named `serviceType` in VSD API.
                
        """
        return self._service_type

    def _set_service_type(self, value):
        """ Set service_type value.

            Notes:
                Type of the SERVICE -  L3,L2 Possible values are L3, L2, .

                
                This attribute is named `serviceType` in VSD API.
                
        """
        self._service_type = value

    service_type = property(_get_service_type, _set_service_type)
    
    def _get_tunnel_type(self):
        """ Get tunnel_type value.

            Notes:
                Type of the SERVICE - GRE,VXLAN Possible values are DC_DEFAULT, GRE, VXLAN, .

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        return self._tunnel_type

    def _set_tunnel_type(self, value):
        """ Set tunnel_type value.

            Notes:
                Type of the SERVICE - GRE,VXLAN Possible values are DC_DEFAULT, GRE, VXLAN, .

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        self._tunnel_type = value

    tunnel_type = property(_get_tunnel_type, _set_tunnel_type)
    
    def _get_use_user_mnemonic(self):
        """ Get use_user_mnemonic value.

            Notes:
                Determines whether to use user mnemonic of the WAN Service

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        return self._use_user_mnemonic

    def _set_use_user_mnemonic(self, value):
        """ Set use_user_mnemonic value.

            Notes:
                Determines whether to use user mnemonic of the WAN Service

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        self._use_user_mnemonic = value

    use_user_mnemonic = property(_get_use_user_mnemonic, _set_use_user_mnemonic)
    
    def _get_user_mnemonic(self):
        """ Get user_mnemonic value.

            Notes:
                user mnemonic of the WAN Service

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        return self._user_mnemonic

    def _set_user_mnemonic(self, value):
        """ Set user_mnemonic value.

            Notes:
                user mnemonic of the WAN Service

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        self._user_mnemonic = value

    user_mnemonic = property(_get_user_mnemonic, _set_user_mnemonic)
    
    def _get_vn_id(self):
        """ Get vn_id value.

            Notes:
                VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated

                
                This attribute is named `vnId` in VSD API.
                
        """
        return self._vn_id

    def _set_vn_id(self, value):
        """ Set vn_id value.

            Notes:
                VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated

                
                This attribute is named `vnId` in VSD API.
                
        """
        self._vn_id = value

    vn_id = property(_get_vn_id, _set_vn_id)
    
    def _get_wan_service_identifier(self):
        """ Get wan_service_identifier value.

            Notes:
                Identifier of the WAN Service

                
                This attribute is named `WANServiceIdentifier` in VSD API.
                
        """
        return self._wan_service_identifier

    def _set_wan_service_identifier(self, value):
        """ Set wan_service_identifier value.

            Notes:
                Identifier of the WAN Service

                
                This attribute is named `WANServiceIdentifier` in VSD API.
                
        """
        self._wan_service_identifier = value

    wan_service_identifier = property(_get_wan_service_identifier, _set_wan_service_identifier)
    