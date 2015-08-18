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


from ..fetchers import NUAggregateMetadatasFetcher
from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUBridgeInterfacesFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUHostInterfacesFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUQOSsFetcher
from ..fetchers import NURedirectionTargetsFetcher
from ..fetchers import NUStatisticsFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUVirtualIPsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVMsFetcher
from ..fetchers import NUVPortMirrorsFetcher
from ..fetchers import NUVRSsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUVPort(NURESTObject):
    """ Represents a VPort in the VSD

        Notes:
            VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists on the hypervisor or gateway

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUVPort instead.
    """

    __rest_name__ = u"vport"

    def __init__(self, **kwargs):
        """ Initializes a VPort instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vport = NUVPort(id=u'xxxx-xxx-xxx-xxx', name=u'VPort')
                >>> vport = NUVPort(data=my_dict)
        """

        super(NUVPort, self).__init__()

        # Read/Write Attributes
        
        self._active = None
        self._address_spoofing = None
        self._associated_floating_ip_id = None
        self._associated_multicast_channel_map_id = None
        self._associated_send_multicast_channel_map_id = None
        self._description = None
        self._domain_id = None
        self._has_attached_interfaces = None
        self._multi_nic_vport_id = None
        self._multicast = None
        self._name = None
        self._operational_state = None
        self._system_type = None
        self._type = None
        self._vlanid = None
        self._zone_id = None
        
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"address_spoofing", remote_name=u"addressSpoofing", attribute_type=str, is_required=True, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"associated_floating_ip_id", remote_name=u"associatedFloatingIPID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_send_multicast_channel_map_id", remote_name=u"associatedSendMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"domain_id", remote_name=u"domainID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"has_attached_interfaces", remote_name=u"hasAttachedInterfaces", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"multi_nic_vport_id", remote_name=u"multiNICVPortID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"operational_state", remote_name=u"operationalState", attribute_type=str, is_required=False, is_unique=False, choices=[u'DOWN', u'INIT', u'UP'])
        self.expose_attribute(local_name=u"system_type", remote_name=u"systemType", attribute_type=str, is_required=False, is_unique=False, choices=[u'HARDWARE', u'HARDWARE_VTEP', u'NUAGE_1', u'NUAGE_2', u'NUAGE_VRSG', u'SOFTWARE'])
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str, is_required=True, is_unique=False, choices=[u'BRIDGE', u'HOST', u'VM'])
        self.expose_attribute(local_name=u"vlanid", remote_name=u"VLANID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"zone_id", remote_name=u"zoneID", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.aggregate_metadatas = NUAggregateMetadatasFetcher.fetcher_with_object(parent_object=self)
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self)
        
        self.bridge_interfaces = NUBridgeInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.host_interfaces = NUHostInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self)
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self)
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self)
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self)
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self)
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self)
        
        self.virtual_ips = NUVirtualIPsFetcher.fetcher_with_object(parent_object=self)
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self)
        
        self.vport_mirrors = NUVPortMirrorsFetcher.fetcher_with_object(parent_object=self)
        
        self.vrss = NUVRSsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_active(self):
        """ Get active value.

            Notes:
                Indicates if this vport is up or down

                
        """
        return self._active

    def _set_active(self, value):
        """ Set active value.

            Notes:
                Indicates if this vport is up or down

                
        """
        self._active = value

    active = property(_get_active, _set_active)
    
    def _get_address_spoofing(self):
        """ Get address_spoofing value.

            Notes:
                Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport Possible values are INHERITED, ENABLED, DISABLED, .

                
                This attribute is named `addressSpoofing` in VSD API.
                
        """
        return self._address_spoofing

    def _set_address_spoofing(self, value):
        """ Set address_spoofing value.

            Notes:
                Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport Possible values are INHERITED, ENABLED, DISABLED, .

                
                This attribute is named `addressSpoofing` in VSD API.
                
        """
        self._address_spoofing = value

    address_spoofing = property(_get_address_spoofing, _set_address_spoofing)
    
    def _get_associated_floating_ip_id(self):
        """ Get associated_floating_ip_id value.

            Notes:
                Id of Floating IP address associated to this vport

                
                This attribute is named `associatedFloatingIPID` in VSD API.
                
        """
        return self._associated_floating_ip_id

    def _set_associated_floating_ip_id(self, value):
        """ Set associated_floating_ip_id value.

            Notes:
                Id of Floating IP address associated to this vport

                
                This attribute is named `associatedFloatingIPID` in VSD API.
                
        """
        self._associated_floating_ip_id = value

    associated_floating_ip_id = property(_get_associated_floating_ip_id, _set_associated_floating_ip_id)
    
    def _get_associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    def _set_associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    associated_multicast_channel_map_id = property(_get_associated_multicast_channel_map_id, _set_associated_multicast_channel_map_id)
    
    def _get_associated_send_multicast_channel_map_id(self):
        """ Get associated_send_multicast_channel_map_id value.

            Notes:
                The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedSendMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_send_multicast_channel_map_id

    def _set_associated_send_multicast_channel_map_id(self, value):
        """ Set associated_send_multicast_channel_map_id value.

            Notes:
                The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedSendMulticastChannelMapID` in VSD API.
                
        """
        self._associated_send_multicast_channel_map_id = value

    associated_send_multicast_channel_map_id = property(_get_associated_send_multicast_channel_map_id, _set_associated_send_multicast_channel_map_id)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description for this vport

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description for this vport

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_domain_id(self):
        """ Get domain_id value.

            Notes:
                ID the Domain associated with the VPort

                
                This attribute is named `domainID` in VSD API.
                
        """
        return self._domain_id

    def _set_domain_id(self, value):
        """ Set domain_id value.

            Notes:
                ID the Domain associated with the VPort

                
                This attribute is named `domainID` in VSD API.
                
        """
        self._domain_id = value

    domain_id = property(_get_domain_id, _set_domain_id)
    
    def _get_has_attached_interfaces(self):
        """ Get has_attached_interfaces value.

            Notes:
                Indicates that this vport has attached interfaces

                
                This attribute is named `hasAttachedInterfaces` in VSD API.
                
        """
        return self._has_attached_interfaces

    def _set_has_attached_interfaces(self, value):
        """ Set has_attached_interfaces value.

            Notes:
                Indicates that this vport has attached interfaces

                
                This attribute is named `hasAttachedInterfaces` in VSD API.
                
        """
        self._has_attached_interfaces = value

    has_attached_interfaces = property(_get_has_attached_interfaces, _set_has_attached_interfaces)
    
    def _get_multi_nic_vport_id(self):
        """ Get multi_nic_vport_id value.

            Notes:
                ID of the Multi NIC VPort associated with the VPort

                
                This attribute is named `multiNICVPortID` in VSD API.
                
        """
        return self._multi_nic_vport_id

    def _set_multi_nic_vport_id(self, value):
        """ Set multi_nic_vport_id value.

            Notes:
                ID of the Multi NIC VPort associated with the VPort

                
                This attribute is named `multiNICVPortID` in VSD API.
                
        """
        self._multi_nic_vport_id = value

    multi_nic_vport_id = property(_get_multi_nic_vport_id, _set_multi_nic_vport_id)
    
    def _get_multicast(self):
        """ Get multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Vport. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        return self._multicast

    def _set_multicast(self, value):
        """ Set multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Vport. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        self._multicast = value

    multicast = property(_get_multicast, _set_multicast)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_operational_state(self):
        """ Get operational_state value.

            Notes:
                Operational State of the VPort - RUNNING/SHUTDOWN Possible values are INIT, UP, DOWN, .

                
                This attribute is named `operationalState` in VSD API.
                
        """
        return self._operational_state

    def _set_operational_state(self, value):
        """ Set operational_state value.

            Notes:
                Operational State of the VPort - RUNNING/SHUTDOWN Possible values are INIT, UP, DOWN, .

                
                This attribute is named `operationalState` in VSD API.
                
        """
        self._operational_state = value

    operational_state = property(_get_operational_state, _set_operational_state)
    
    def _get_system_type(self):
        """ Get system_type value.

            Notes:
                Indicates what system it is - SOFTWARE/HARDWARE_VTEP/HARDWARE/ (possible values)  Possible values are HARDWARE, SOFTWARE, HARDWARE_VTEP, NUAGE_1, NUAGE_2, NUAGE_VRSG, .

                
                This attribute is named `systemType` in VSD API.
                
        """
        return self._system_type

    def _set_system_type(self, value):
        """ Set system_type value.

            Notes:
                Indicates what system it is - SOFTWARE/HARDWARE_VTEP/HARDWARE/ (possible values)  Possible values are HARDWARE, SOFTWARE, HARDWARE_VTEP, NUAGE_1, NUAGE_2, NUAGE_VRSG, .

                
                This attribute is named `systemType` in VSD API.
                
        """
        self._system_type = value

    system_type = property(_get_system_type, _set_system_type)
    
    def _get_type(self):
        """ Get type value.

            Notes:
                Type of vport - possible values VM/HOST/BRIDGE Possible values are VM, HOST, BRIDGE, .

                
        """
        return self._type

    def _set_type(self, value):
        """ Set type value.

            Notes:
                Type of vport - possible values VM/HOST/BRIDGE Possible values are VM, HOST, BRIDGE, .

                
        """
        self._type = value

    type = property(_get_type, _set_type)
    
    def _get_vlanid(self):
        """ Get vlanid value.

            Notes:
                associated Vlan of this vport - applicable for type host/bridge

                
                This attribute is named `VLANID` in VSD API.
                
        """
        return self._vlanid

    def _set_vlanid(self, value):
        """ Set vlanid value.

            Notes:
                associated Vlan of this vport - applicable for type host/bridge

                
                This attribute is named `VLANID` in VSD API.
                
        """
        self._vlanid = value

    vlanid = property(_get_vlanid, _set_vlanid)
    
    def _get_zone_id(self):
        """ Get zone_id value.

            Notes:
                ID the Zone associated with the VPort

                
                This attribute is named `zoneID` in VSD API.
                
        """
        return self._zone_id

    def _set_zone_id(self, value):
        """ Set zone_id value.

            Notes:
                ID the Zone associated with the VPort

                
                This attribute is named `zoneID` in VSD API.
                
        """
        self._zone_id = value

    zone_id = property(_get_zone_id, _set_zone_id)
    