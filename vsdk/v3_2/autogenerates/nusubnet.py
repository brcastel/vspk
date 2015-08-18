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


from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUIPReservationsFetcher
from ..fetchers import NUQOSsFetcher
from ..fetchers import NUVMResyncsFetcher
from ..fetchers import NUStatisticsFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUVirtualIPsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVMsFetcher
from ..fetchers import NUVPortsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUSubnet(NURESTObject):
    """ Represents a Subnet in the VSD

        Notes:
            This is the definition of a subnet associated with a zone

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUSubnet instead.
    """

    __rest_name__ = u"subnet"

    def __init__(self, **kwargs):
        """ Initializes a Subnet instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> subnet = NUSubnet(id=u'xxxx-xxx-xxx-xxx', name=u'Subnet')
                >>> subnet = NUSubnet(data=my_dict)
        """

        super(NUSubnet, self).__init__()

        # Read/Write Attributes
        
        self._address = None
        self._associated_application_id = None
        self._associated_application_object_id = None
        self._associated_application_object_type = None
        self._associated_multicast_channel_map_id = None
        self._associated_shared_network_resource_id = None
        self._default_action = None
        self._description = None
        self._encryption = None
        self._gateway = None
        self._gateway_mac_address = None
        self._ip_type = None
        self._maintenance_mode = None
        self._multicast = None
        self._name = None
        self._netmask = None
        self._pat_enabled = None
        self._policy_group_id = None
        self._proxy_arp = None
        self._public = None
        self._route_distinguisher = None
        self._route_target = None
        self._service_id = None
        self._split_subnet = None
        self._template_id = None
        self._vn_id = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"associated_application_id", remote_name=u"associatedApplicationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_application_object_id", remote_name=u"associatedApplicationObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_application_object_type", remote_name=u"associatedApplicationObjectType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_shared_network_resource_id", remote_name=u"associatedSharedNetworkResourceID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"default_action", remote_name=u"defaultAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'DROP_TRAFFIC', u'USE_UNDERLAY'])
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"encryption", remote_name=u"encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"gateway_mac_address", remote_name=u"gatewayMACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"pat_enabled", remote_name=u"PATEnabled", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"policy_group_id", remote_name=u"policyGroupID", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"proxy_arp", remote_name=u"proxyARP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"public", remote_name=u"public", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"route_distinguisher", remote_name=u"routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"route_target", remote_name=u"routeTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"service_id", remote_name=u"serviceID", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"split_subnet", remote_name=u"splitSubnet", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"vn_id", remote_name=u"vnId", attribute_type=long, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.address_ranges = NUAddressRangesFetcher.fetcher_with_object(parent_object=self)
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.ip_reservations = NUIPReservationsFetcher.fetcher_with_object(parent_object=self)
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self)
        
        self.vm_resyncs = NUVMResyncsFetcher.fetcher_with_object(parent_object=self)
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self)
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self)
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self)
        
        self.virtual_ips = NUVirtualIPsFetcher.fetcher_with_object(parent_object=self)
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self)
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_address(self):
        """ Get address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
        """
        return self._address

    def _set_address(self, value):
        """ Set address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_associated_application_id(self):
        """ Get associated_application_id value.

            Notes:
                The associated application ID.

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        return self._associated_application_id

    def _set_associated_application_id(self, value):
        """ Set associated_application_id value.

            Notes:
                The associated application ID.

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        self._associated_application_id = value

    associated_application_id = property(_get_associated_application_id, _set_associated_application_id)
    
    def _get_associated_application_object_id(self):
        """ Get associated_application_object_id value.

            Notes:
                The associated application object ID.

                
                This attribute is named `associatedApplicationObjectID` in VSD API.
                
        """
        return self._associated_application_object_id

    def _set_associated_application_object_id(self, value):
        """ Set associated_application_object_id value.

            Notes:
                The associated application object ID.

                
                This attribute is named `associatedApplicationObjectID` in VSD API.
                
        """
        self._associated_application_object_id = value

    associated_application_object_id = property(_get_associated_application_object_id, _set_associated_application_object_id)
    
    def _get_associated_application_object_type(self):
        """ Get associated_application_object_type value.

            Notes:
                The associated application object type. Refer to API section for supported types.

                
                This attribute is named `associatedApplicationObjectType` in VSD API.
                
        """
        return self._associated_application_object_type

    def _set_associated_application_object_type(self, value):
        """ Set associated_application_object_type value.

            Notes:
                The associated application object type. Refer to API section for supported types.

                
                This attribute is named `associatedApplicationObjectType` in VSD API.
                
        """
        self._associated_application_object_type = value

    associated_application_object_type = property(_get_associated_application_object_type, _set_associated_application_object_type)
    
    def _get_associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    def _set_associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    associated_multicast_channel_map_id = property(_get_associated_multicast_channel_map_id, _set_associated_multicast_channel_map_id)
    
    def _get_associated_shared_network_resource_id(self):
        """ Get associated_shared_network_resource_id value.

            Notes:
                The ID of public subnet that is associated with this subnet

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        return self._associated_shared_network_resource_id

    def _set_associated_shared_network_resource_id(self, value):
        """ Set associated_shared_network_resource_id value.

            Notes:
                The ID of public subnet that is associated with this subnet

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        self._associated_shared_network_resource_id = value

    associated_shared_network_resource_id = property(_get_associated_shared_network_resource_id, _set_associated_shared_network_resource_id)
    
    def _get_default_action(self):
        """ Get default_action value.

            Notes:
                If PAT is disabled then this flag indicates what to do if routes don't exist in overlay, will default to drop | possible values USE_UNDERLAY, DROP_TRAFFIC Possible values are USE_UNDERLAY, DROP_TRAFFIC, .

                
                This attribute is named `defaultAction` in VSD API.
                
        """
        return self._default_action

    def _set_default_action(self, value):
        """ Set default_action value.

            Notes:
                If PAT is disabled then this flag indicates what to do if routes don't exist in overlay, will default to drop | possible values USE_UNDERLAY, DROP_TRAFFIC Possible values are USE_UNDERLAY, DROP_TRAFFIC, .

                
                This attribute is named `defaultAction` in VSD API.
                
        """
        self._default_action = value

    default_action = property(_get_default_action, _set_default_action)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description field provided by the user that identifies the subnet

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description field provided by the user that identifies the subnet

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_encryption(self):
        """ Get encryption value.

            Notes:
                Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        return self._encryption

    def _set_encryption(self, value):
        """ Set encryption value.

            Notes:
                Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        self._encryption = value

    encryption = property(_get_encryption, _set_encryption)
    
    def _get_gateway(self):
        """ Get gateway value.

            Notes:
                The IP address of the gateway of this subnet

                
        """
        return self._gateway

    def _set_gateway(self, value):
        """ Set gateway value.

            Notes:
                The IP address of the gateway of this subnet

                
        """
        self._gateway = value

    gateway = property(_get_gateway, _set_gateway)
    
    def _get_gateway_mac_address(self):
        """ Get gateway_mac_address value.

            Notes:
                

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        return self._gateway_mac_address

    def _set_gateway_mac_address(self, value):
        """ Set gateway_mac_address value.

            Notes:
                

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        self._gateway_mac_address = value

    gateway_mac_address = property(_get_gateway_mac_address, _set_gateway_mac_address)
    
    def _get_ip_type(self):
        """ Get ip_type value.

            Notes:
                IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    def _set_ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    ip_type = property(_get_ip_type, _set_ip_type)
    
    def _get_maintenance_mode(self):
        """ Get maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        return self._maintenance_mode

    def _set_maintenance_mode(self, value):
        """ Set maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        self._maintenance_mode = value

    maintenance_mode = property(_get_maintenance_mode, _set_maintenance_mode)
    
    def _get_multicast(self):
        """ Get multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Subnet/Subnet Template. Possible values are ENABLED,DISABLED and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        return self._multicast

    def _set_multicast(self, value):
        """ Set multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Subnet/Subnet Template. Possible values are ENABLED,DISABLED and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        self._multicast = value

    multicast = property(_get_multicast, _set_multicast)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        return self._netmask

    def _set_netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        self._netmask = value

    netmask = property(_get_netmask, _set_netmask)
    
    def _get_pat_enabled(self):
        """ Get pat_enabled value.

            Notes:
                

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        return self._pat_enabled

    def _set_pat_enabled(self, value):
        """ Set pat_enabled value.

            Notes:
                

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        self._pat_enabled = value

    pat_enabled = property(_get_pat_enabled, _set_pat_enabled)
    
    def _get_policy_group_id(self):
        """ Get policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        return self._policy_group_id

    def _set_policy_group_id(self, value):
        """ Set policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        self._policy_group_id = value

    policy_group_id = property(_get_policy_group_id, _set_policy_group_id)
    
    def _get_proxy_arp(self):
        """ Get proxy_arp value.

            Notes:
                 when set VRS will act as  ARP Proxy

                
                This attribute is named `proxyARP` in VSD API.
                
        """
        return self._proxy_arp

    def _set_proxy_arp(self, value):
        """ Set proxy_arp value.

            Notes:
                 when set VRS will act as  ARP Proxy

                
                This attribute is named `proxyARP` in VSD API.
                
        """
        self._proxy_arp = value

    proxy_arp = property(_get_proxy_arp, _set_proxy_arp)
    
    def _get_public(self):
        """ Get public value.

            Notes:
                when set to true means public subnet under a public zone

                
        """
        return self._public

    def _set_public(self, value):
        """ Set public value.

            Notes:
                when set to true means public subnet under a public zone

                
        """
        self._public = value

    public = property(_get_public, _set_public)
    
    def _get_route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    def _set_route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    route_distinguisher = property(_get_route_distinguisher, _set_route_distinguisher)
    
    def _get_route_target(self):
        """ Get route_target value.

            Notes:
                The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        return self._route_target

    def _set_route_target(self, value):
        """ Set route_target value.

            Notes:
                The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        self._route_target = value

    route_target = property(_get_route_target, _set_route_target)
    
    def _get_service_id(self):
        """ Get service_id value.

            Notes:
                The service ID used by the VSCs to identify this subnet

                
                This attribute is named `serviceID` in VSD API.
                
        """
        return self._service_id

    def _set_service_id(self, value):
        """ Set service_id value.

            Notes:
                The service ID used by the VSCs to identify this subnet

                
                This attribute is named `serviceID` in VSD API.
                
        """
        self._service_id = value

    service_id = property(_get_service_id, _set_service_id)
    
    def _get_split_subnet(self):
        """ Get split_subnet value.

            Notes:
                Need to add correct description

                
                This attribute is named `splitSubnet` in VSD API.
                
        """
        return self._split_subnet

    def _set_split_subnet(self, value):
        """ Set split_subnet value.

            Notes:
                Need to add correct description

                
                This attribute is named `splitSubnet` in VSD API.
                
        """
        self._split_subnet = value

    split_subnet = property(_get_split_subnet, _set_split_subnet)
    
    def _get_template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the subnet template that this subnet object was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    def _set_template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the subnet template that this subnet object was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    template_id = property(_get_template_id, _set_template_id)
    
    def _get_vn_id(self):
        """ Get vn_id value.

            Notes:
                Current Network's  globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `vnId` in VSD API.
                
        """
        return self._vn_id

    def _set_vn_id(self, value):
        """ Set vn_id value.

            Notes:
                Current Network's  globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `vnId` in VSD API.
                
        """
        self._vn_id = value

    vn_id = property(_get_vn_id, _set_vn_id)
    