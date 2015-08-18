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


from ..fetchers import NUEnterprisesFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUExternalServicesFetcher
from ..fetchers import NUMultiCastChannelMapsFetcher
from ..fetchers import NUMultiCastListsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUEnterpriseProfile(NURESTObject):
    """ Represents a EnterpriseProfile in the VSD

        Notes:
            Enterprise profile, used to store an enterprise's policies, quota etc

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUEnterpriseProfile instead.
    """

    __rest_name__ = u"enterpriseprofile"

    def __init__(self, **kwargs):
        """ Initializes a EnterpriseProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> enterpriseprofile = NUEnterpriseProfile(id=u'xxxx-xxx-xxx-xxx', name=u'EnterpriseProfile')
                >>> enterpriseprofile = NUEnterpriseProfile(data=my_dict)
        """

        super(NUEnterpriseProfile, self).__init__()

        # Read/Write Attributes
        
        self._allow_advanced_qos_configuration = None
        self._allow_gateway_management = None
        self._allow_trusted_forwarding_class = None
        self._allowed_forwarding_classes = None
        self._description = None
        self._dhcp_lease_interval = None
        self._encryption_management_mode = None
        self._floating_ips_quota = None
        self._name = None
        self._receive_multi_cast_list_id = None
        self._send_multi_cast_list_id = None
        
        self.expose_attribute(local_name=u"allow_advanced_qos_configuration", remote_name=u"allowAdvancedQOSConfiguration", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"allow_gateway_management", remote_name=u"allowGatewayManagement", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"allow_trusted_forwarding_class", remote_name=u"allowTrustedForwardingClass", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"allowed_forwarding_classes", remote_name=u"allowedForwardingClasses", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"dhcp_lease_interval", remote_name=u"DHCPLeaseInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"encryption_management_mode", remote_name=u"encryptionManagementMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'MANAGED'])
        self.expose_attribute(local_name=u"floating_ips_quota", remote_name=u"floatingIPsQuota", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"receive_multi_cast_list_id", remote_name=u"receiveMultiCastListID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"send_multi_cast_list_id", remote_name=u"sendMultiCastListID", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.enterprises = NUEnterprisesFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.external_services = NUExternalServicesFetcher.fetcher_with_object(parent_object=self)
        
        self.multi_cast_channel_maps = NUMultiCastChannelMapsFetcher.fetcher_with_object(parent_object=self)
        
        self.multi_cast_lists = NUMultiCastListsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_allow_advanced_qos_configuration(self):
        """ Get allow_advanced_qos_configuration value.

            Notes:
                Controls whether this enterprise has access to advanced QoS settings.

                
                This attribute is named `allowAdvancedQOSConfiguration` in VSD API.
                
        """
        return self._allow_advanced_qos_configuration

    def _set_allow_advanced_qos_configuration(self, value):
        """ Set allow_advanced_qos_configuration value.

            Notes:
                Controls whether this enterprise has access to advanced QoS settings.

                
                This attribute is named `allowAdvancedQOSConfiguration` in VSD API.
                
        """
        self._allow_advanced_qos_configuration = value

    allow_advanced_qos_configuration = property(_get_allow_advanced_qos_configuration, _set_allow_advanced_qos_configuration)
    
    def _get_allow_gateway_management(self):
        """ Get allow_gateway_management value.

            Notes:
                If set to true lets the enterprise admin create gateway templates and instances.

                
                This attribute is named `allowGatewayManagement` in VSD API.
                
        """
        return self._allow_gateway_management

    def _set_allow_gateway_management(self, value):
        """ Set allow_gateway_management value.

            Notes:
                If set to true lets the enterprise admin create gateway templates and instances.

                
                This attribute is named `allowGatewayManagement` in VSD API.
                
        """
        self._allow_gateway_management = value

    allow_gateway_management = property(_get_allow_gateway_management, _set_allow_gateway_management)
    
    def _get_allow_trusted_forwarding_class(self):
        """ Get allow_trusted_forwarding_class value.

            Notes:
                Controls whether QoS policies and templates created under this enterprise set the trusted flag to true

                
                This attribute is named `allowTrustedForwardingClass` in VSD API.
                
        """
        return self._allow_trusted_forwarding_class

    def _set_allow_trusted_forwarding_class(self, value):
        """ Set allow_trusted_forwarding_class value.

            Notes:
                Controls whether QoS policies and templates created under this enterprise set the trusted flag to true

                
                This attribute is named `allowTrustedForwardingClass` in VSD API.
                
        """
        self._allow_trusted_forwarding_class = value

    allow_trusted_forwarding_class = property(_get_allow_trusted_forwarding_class, _set_allow_trusted_forwarding_class)
    
    def _get_allowed_forwarding_classes(self):
        """ Get allowed_forwarding_classes value.

            Notes:
                Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `allowedForwardingClasses` in VSD API.
                
        """
        return self._allowed_forwarding_classes

    def _set_allowed_forwarding_classes(self, value):
        """ Set allowed_forwarding_classes value.

            Notes:
                Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `allowedForwardingClasses` in VSD API.
                
        """
        self._allowed_forwarding_classes = value

    allowed_forwarding_classes = property(_get_allowed_forwarding_classes, _set_allowed_forwarding_classes)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the enterprise/organisation profile.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the enterprise/organisation profile.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_dhcp_lease_interval(self):
        """ Get dhcp_lease_interval value.

            Notes:
                DHCP Lease Interval (in hours) to be used by an enterprise.

                
                This attribute is named `DHCPLeaseInterval` in VSD API.
                
        """
        return self._dhcp_lease_interval

    def _set_dhcp_lease_interval(self, value):
        """ Set dhcp_lease_interval value.

            Notes:
                DHCP Lease Interval (in hours) to be used by an enterprise.

                
                This attribute is named `DHCPLeaseInterval` in VSD API.
                
        """
        self._dhcp_lease_interval = value

    dhcp_lease_interval = property(_get_dhcp_lease_interval, _set_dhcp_lease_interval)
    
    def _get_encryption_management_mode(self):
        """ Get encryption_management_mode value.

            Notes:
                encryption management mode for this enterprise Possible values are DISABLED, MANAGED, .

                
                This attribute is named `encryptionManagementMode` in VSD API.
                
        """
        return self._encryption_management_mode

    def _set_encryption_management_mode(self, value):
        """ Set encryption_management_mode value.

            Notes:
                encryption management mode for this enterprise Possible values are DISABLED, MANAGED, .

                
                This attribute is named `encryptionManagementMode` in VSD API.
                
        """
        self._encryption_management_mode = value

    encryption_management_mode = property(_get_encryption_management_mode, _set_encryption_management_mode)
    
    def _get_floating_ips_quota(self):
        """ Get floating_ips_quota value.

            Notes:
                Quota set for the number of floating IPs to be used by an enterprise.

                
                This attribute is named `floatingIPsQuota` in VSD API.
                
        """
        return self._floating_ips_quota

    def _set_floating_ips_quota(self, value):
        """ Set floating_ips_quota value.

            Notes:
                Quota set for the number of floating IPs to be used by an enterprise.

                
                This attribute is named `floatingIPsQuota` in VSD API.
                
        """
        self._floating_ips_quota = value

    floating_ips_quota = property(_get_floating_ips_quota, _set_floating_ips_quota)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_receive_multi_cast_list_id(self):
        """ Get receive_multi_cast_list_id value.

            Notes:
                Readonly ID of the auto generated receive multicast list associated with this enterprise profile

                
                This attribute is named `receiveMultiCastListID` in VSD API.
                
        """
        return self._receive_multi_cast_list_id

    def _set_receive_multi_cast_list_id(self, value):
        """ Set receive_multi_cast_list_id value.

            Notes:
                Readonly ID of the auto generated receive multicast list associated with this enterprise profile

                
                This attribute is named `receiveMultiCastListID` in VSD API.
                
        """
        self._receive_multi_cast_list_id = value

    receive_multi_cast_list_id = property(_get_receive_multi_cast_list_id, _set_receive_multi_cast_list_id)
    
    def _get_send_multi_cast_list_id(self):
        """ Get send_multi_cast_list_id value.

            Notes:
                Readonly ID of the auto generated send multicast list associated with this enterprise profile

                
                This attribute is named `sendMultiCastListID` in VSD API.
                
        """
        return self._send_multi_cast_list_id

    def _set_send_multi_cast_list_id(self, value):
        """ Set send_multi_cast_list_id value.

            Notes:
                Readonly ID of the auto generated send multicast list associated with this enterprise profile

                
                This attribute is named `sendMultiCastListID` in VSD API.
                
        """
        self._send_multi_cast_list_id = value

    send_multi_cast_list_id = property(_get_send_multi_cast_list_id, _set_send_multi_cast_list_id)
    