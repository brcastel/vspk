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
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUQOSsFetcher
from ..fetchers import NUSubnetsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUSubnetTemplate(NURESTObject):
    """ Represents a SubnetTemplate in the VSD

        Notes:
            As domain and zone objects, subnet objects are created in VSD as derived by templates. This object describes the subnet template

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUSubnetTemplate instead.
    """

    __rest_name__ = u"subnettemplate"

    def __init__(self, **kwargs):
        """ Initializes a SubnetTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> subnettemplate = NUSubnetTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'SubnetTemplate')
                >>> subnettemplate = NUSubnetTemplate(data=my_dict)
        """

        super(NUSubnetTemplate, self).__init__()

        # Read/Write Attributes
        
        self._address = None
        self._associated_multicast_channel_map_id = None
        self._description = None
        self._encryption = None
        self._gateway = None
        self._ip_type = None
        self._multicast = None
        self._name = None
        self._netmask = None
        self._proxy_arp = None
        self._split_subnet = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"encryption", remote_name=u"encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"proxy_arp", remote_name=u"proxyARP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"split_subnet", remote_name=u"splitSubnet", attribute_type=bool, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.address_ranges = NUAddressRangesFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self)
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self)
        
        
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
    