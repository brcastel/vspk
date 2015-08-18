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
from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUIngressAdvFwdTemplatesFetcher
from ..fetchers import NUIngressExternalServiceTemplatesFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUL2DomainsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUPolicyGroupTemplatesFetcher
from ..fetchers import NUQOSsFetcher
from ..fetchers import NURedirectionTargetTemplatesFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUL2DomainTemplate(NURESTObject):
    """ Represents a L2DomainTemplate in the VSD

        Notes:
            L2 Domain in VSD as derived by templates. This object describes the L2 Domain template

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUL2DomainTemplate instead.
    """

    __rest_name__ = u"l2domaintemplate"

    def __init__(self, **kwargs):
        """ Initializes a L2DomainTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> l2domaintemplate = NUL2DomainTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'L2DomainTemplate')
                >>> l2domaintemplate = NUL2DomainTemplate(data=my_dict)
        """

        super(NUL2DomainTemplate, self).__init__()

        # Read/Write Attributes
        
        self._address = None
        self._associated_multicast_channel_map_id = None
        self._description = None
        self._dhcp_managed = None
        self._gateway = None
        self._ip_type = None
        self._multicast = None
        self._name = None
        self._netmask = None
        self._policy_change_status = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"dhcp_managed", remote_name=u"DHCPManaged", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"policy_change_status", remote_name=u"policyChangeStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        
        # Fetchers
        
        self.address_ranges = NUAddressRangesFetcher.fetcher_with_object(parent_object=self)
        
        self.egress_acl_templates = NUEgressACLTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.groups = NUGroupsFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_acl_templates = NUIngressACLTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_adv_fwd_templates = NUIngressAdvFwdTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_external_service_templates = NUIngressExternalServiceTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self)
        
        self.l2_domains = NUL2DomainsFetcher.fetcher_with_object(parent_object=self)
        
        self.permitted_actions = NUPermittedActionsFetcher.fetcher_with_object(parent_object=self)
        
        self.policy_group_templates = NUPolicyGroupTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self)
        
        self.redirection_target_templates = NURedirectionTargetTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_address(self):
        """ Get address value.

            Notes:
                Network address of the L2Domain / L2Domain template defined. 

                
        """
        return self._address

    def _set_address(self, value):
        """ Set address value.

            Notes:
                Network address of the L2Domain / L2Domain template defined. 

                
        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    def _set_associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    associated_multicast_channel_map_id = property(_get_associated_multicast_channel_map_id, _set_associated_multicast_channel_map_id)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description field provided by the user that identifies the L2Domain / L2Domain template.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description field provided by the user that identifies the L2Domain / L2Domain template.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_dhcp_managed(self):
        """ Get dhcp_managed value.

            Notes:
                decides whether L2Domain / L2Domain template DHCP is managed by VSD

                
                This attribute is named `DHCPManaged` in VSD API.
                
        """
        return self._dhcp_managed

    def _set_dhcp_managed(self, value):
        """ Set dhcp_managed value.

            Notes:
                decides whether L2Domain / L2Domain template DHCP is managed by VSD

                
                This attribute is named `DHCPManaged` in VSD API.
                
        """
        self._dhcp_managed = value

    dhcp_managed = property(_get_dhcp_managed, _set_dhcp_managed)
    
    def _get_gateway(self):
        """ Get gateway value.

            Notes:
                The IP address of the gateway of this l2 domain

                
        """
        return self._gateway

    def _set_gateway(self, value):
        """ Set gateway value.

            Notes:
                The IP address of the gateway of this l2 domain

                
        """
        self._gateway = value

    gateway = property(_get_gateway, _set_gateway)
    
    def _get_ip_type(self):
        """ Get ip_type value.

            Notes:
                IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    def _set_ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    ip_type = property(_get_ip_type, _set_ip_type)
    
    def _get_multicast(self):
        """ Get multicast value.

            Notes:
                multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        return self._multicast

    def _set_multicast(self, value):
        """ Set multicast value.

            Notes:
                multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        self._multicast = value

    multicast = property(_get_multicast, _set_multicast)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the L2Domain / L2Domain template defined

                
        """
        return self._netmask

    def _set_netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the L2Domain / L2Domain template defined

                
        """
        self._netmask = value

    netmask = property(_get_netmask, _set_netmask)
    
    def _get_policy_change_status(self):
        """ Get policy_change_status value.

            Notes:
                

                
                This attribute is named `policyChangeStatus` in VSD API.
                
        """
        return self._policy_change_status

    def _set_policy_change_status(self, value):
        """ Set policy_change_status value.

            Notes:
                

                
                This attribute is named `policyChangeStatus` in VSD API.
                
        """
        self._policy_change_status = value

    policy_change_status = property(_get_policy_change_status, _set_policy_change_status)
    