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


from ..fetchers import NUApplicationServicesFetcher
from ..fetchers import NUAutoDiscoveredGatewaysFetcher
from ..fetchers import NUCloudMgmtSystemsFetcher
from ..fetchers import NUDomainsFetcher
from ..fetchers import NUEgressACLEntryTemplatesFetcher
from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUEgressQOSPoliciesFetcher
from ..fetchers import NUEnterpriseProfilesFetcher
from ..fetchers import NUEnterprisesFetcher
from ..fetchers import NUExternalAppServicesFetcher
from ..fetchers import NUFloatingIpsFetcher
from ..fetchers import NUGatewaysFetcher
from ..fetchers import NUGatewayTemplatesFetcher
from ..fetchers import NUHostInterfacesFetcher
from ..fetchers import NUInfrastructureGatewayProfilesFetcher
from ..fetchers import NUInfrastructurePortProfilesFetcher
from ..fetchers import NUIngressACLEntryTemplatesFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUIngressAdvFwdEntryTemplatesFetcher
from ..fetchers import NUL2DomainsFetcher
from ..fetchers import NULicensesFetcher
from ..fetchers import NUMirrorDestinationsFetcher
from ..fetchers import NUMultiCastChannelMapsFetcher
from ..fetchers import NUNetworkLayoutsFetcher
from ..fetchers import NUNSGatewaysFetcher
from ..fetchers import NUNSGatewayTemplatesFetcher
from ..fetchers import NUPATNATPoolsFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NURateLimitersFetcher
from ..fetchers import NURedirectionTargetsFetcher
from ..fetchers import NURedundancyGroupsFetcher
from ..fetchers import NUSharedNetworkResourcesFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUStatsCollectorInfosFetcher
from ..fetchers import NUSubnetsFetcher
from ..fetchers import NUSystemConfigsFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUVCenterHypervisorsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVMsFetcher
from ..fetchers import NUVSPsFetcher
from ..fetchers import NUZonesFetcher
from bambou import NURESTBasicUser


class NURESTUser(NURESTBasicUser):
    """ Represents a user that can login to the VSD.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NURESTUser instead.
    """

    __rest_name__ = u"me"

    def __init__(self, **kwargs):
        """ Initializes a RESTUser instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> restuser = NURESTUser(id=u'xxxx-xxx-xxx-xxx', name=u'RESTUser')
                >>> restuser = NURESTUser(data=my_dict)
        """

        super(NURESTUser, self).__init__()

        # Read/Write Attributes
        
        self._avatar_data = None
        self._avatar_type = None
        self._disabled = None
        self._email = None
        self._enterprise_id = None
        self._enterprise_name = None
        self._first_name = None
        self._last_name = None
        self._mobile_number = None
        self._password = None
        self._role = None
        self._user_name = None
        
        self.expose_attribute(local_name=u"avatar_data", remote_name=u"avatarData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"avatar_type", remote_name=u"avatarType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BASE64', u'COMPUTEDURL', u'URL'])
        self.expose_attribute(local_name=u"disabled", remote_name=u"disabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"email", remote_name=u"email", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"enterprise_name", remote_name=u"enterpriseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"first_name", remote_name=u"firstName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"last_name", remote_name=u"lastName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"mobile_number", remote_name=u"mobileNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"password", remote_name=u"password", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"role", remote_name=u"role", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=str, is_required=True, is_unique=False)
        
        # Fetchers
        
        self.application_services = NUApplicationServicesFetcher.fetcher_with_object(parent_object=self)
        
        self.auto_discovered_gateways = NUAutoDiscoveredGatewaysFetcher.fetcher_with_object(parent_object=self)
        
        self.cloud_mgmt_systems = NUCloudMgmtSystemsFetcher.fetcher_with_object(parent_object=self)
        
        self.domains = NUDomainsFetcher.fetcher_with_object(parent_object=self)
        
        self.egress_acl_entry_templates = NUEgressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.egress_acl_templates = NUEgressACLTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.egress_qos_policies = NUEgressQOSPoliciesFetcher.fetcher_with_object(parent_object=self)
        
        self.enterprise_profiles = NUEnterpriseProfilesFetcher.fetcher_with_object(parent_object=self)
        
        self.enterprises = NUEnterprisesFetcher.fetcher_with_object(parent_object=self)
        
        self.external_app_services = NUExternalAppServicesFetcher.fetcher_with_object(parent_object=self)
        
        self.floating_ips = NUFloatingIpsFetcher.fetcher_with_object(parent_object=self)
        
        self.gateways = NUGatewaysFetcher.fetcher_with_object(parent_object=self)
        
        self.gateway_templates = NUGatewayTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.host_interfaces = NUHostInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.infrastructure_gateway_profiles = NUInfrastructureGatewayProfilesFetcher.fetcher_with_object(parent_object=self)
        
        self.infrastructure_port_profiles = NUInfrastructurePortProfilesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_acl_entry_templates = NUIngressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_acl_templates = NUIngressACLTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_adv_fwd_entry_templates = NUIngressAdvFwdEntryTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.l2_domains = NUL2DomainsFetcher.fetcher_with_object(parent_object=self)
        
        self.licenses = NULicensesFetcher.fetcher_with_object(parent_object=self)
        
        self.mirror_destinations = NUMirrorDestinationsFetcher.fetcher_with_object(parent_object=self)
        
        self.multi_cast_channel_maps = NUMultiCastChannelMapsFetcher.fetcher_with_object(parent_object=self)
        
        self.network_layouts = NUNetworkLayoutsFetcher.fetcher_with_object(parent_object=self)
        
        self.ns_gateways = NUNSGatewaysFetcher.fetcher_with_object(parent_object=self)
        
        self.ns_gateway_templates = NUNSGatewayTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.patnat_pools = NUPATNATPoolsFetcher.fetcher_with_object(parent_object=self)
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self)
        
        self.rate_limiters = NURateLimitersFetcher.fetcher_with_object(parent_object=self)
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self)
        
        self.redundancy_groups = NURedundancyGroupsFetcher.fetcher_with_object(parent_object=self)
        
        self.shared_network_resources = NUSharedNetworkResourcesFetcher.fetcher_with_object(parent_object=self)
        
        self.static_routes = NUStaticRoutesFetcher.fetcher_with_object(parent_object=self)
        
        self.stats_collector_infos = NUStatsCollectorInfosFetcher.fetcher_with_object(parent_object=self)
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self)
        
        self.system_configs = NUSystemConfigsFetcher.fetcher_with_object(parent_object=self)
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self)
        
        self.vcenter_hypervisors = NUVCenterHypervisorsFetcher.fetcher_with_object(parent_object=self)
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self)
        
        self.vsps = NUVSPsFetcher.fetcher_with_object(parent_object=self)
        
        self.zones = NUZonesFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_avatar_data(self):
        """ Get avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        return self._avatar_data

    def _set_avatar_data(self, value):
        """ Set avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        self._avatar_data = value

    avatar_data = property(_get_avatar_data, _set_avatar_data)
    
    def _get_avatar_type(self):
        """ Get avatar_type value.

            Notes:
                Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .

                
                This attribute is named `avatarType` in VSD API.
                
        """
        return self._avatar_type

    def _set_avatar_type(self, value):
        """ Set avatar_type value.

            Notes:
                Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .

                
                This attribute is named `avatarType` in VSD API.
                
        """
        self._avatar_type = value

    avatar_type = property(_get_avatar_type, _set_avatar_type)
    
    def _get_disabled(self):
        """ Get disabled value.

            Notes:
                Status of the user account; true=disabled, false=not disabled; default value = false

                
        """
        return self._disabled

    def _set_disabled(self, value):
        """ Set disabled value.

            Notes:
                Status of the user account; true=disabled, false=not disabled; default value = false

                
        """
        self._disabled = value

    disabled = property(_get_disabled, _set_disabled)
    
    def _get_email(self):
        """ Get email value.

            Notes:
                Email address of the user

                
        """
        return self._email

    def _set_email(self, value):
        """ Set email value.

            Notes:
                Email address of the user

                
        """
        self._email = value

    email = property(_get_email, _set_email)
    
    def _get_enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Identifier of the enterprise.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    def _set_enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Identifier of the enterprise.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    enterprise_id = property(_get_enterprise_id, _set_enterprise_id)
    
    def _get_enterprise_name(self):
        """ Get enterprise_name value.

            Notes:
                Name of the enterprise.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        return self._enterprise_name

    def _set_enterprise_name(self, value):
        """ Set enterprise_name value.

            Notes:
                Name of the enterprise.

                
                This attribute is named `enterpriseName` in VSD API.
                
        """
        self._enterprise_name = value

    enterprise_name = property(_get_enterprise_name, _set_enterprise_name)
    
    def _get_first_name(self):
        """ Get first_name value.

            Notes:
                First name of the user

                
                This attribute is named `firstName` in VSD API.
                
        """
        return self._first_name

    def _set_first_name(self, value):
        """ Set first_name value.

            Notes:
                First name of the user

                
                This attribute is named `firstName` in VSD API.
                
        """
        self._first_name = value

    first_name = property(_get_first_name, _set_first_name)
    
    def _get_last_name(self):
        """ Get last_name value.

            Notes:
                Last name of the user

                
                This attribute is named `lastName` in VSD API.
                
        """
        return self._last_name

    def _set_last_name(self, value):
        """ Set last_name value.

            Notes:
                Last name of the user

                
                This attribute is named `lastName` in VSD API.
                
        """
        self._last_name = value

    last_name = property(_get_last_name, _set_last_name)
    
    def _get_mobile_number(self):
        """ Get mobile_number value.

            Notes:
                Mobile Number of the user

                
                This attribute is named `mobileNumber` in VSD API.
                
        """
        return self._mobile_number

    def _set_mobile_number(self, value):
        """ Set mobile_number value.

            Notes:
                Mobile Number of the user

                
                This attribute is named `mobileNumber` in VSD API.
                
        """
        self._mobile_number = value

    mobile_number = property(_get_mobile_number, _set_mobile_number)
    
    def _get_password(self):
        """ Get password value.

            Notes:
                User password stored as a hash (SHA-1 encrpted)

                
        """
        return self._password

    def _set_password(self, value):
        """ Set password value.

            Notes:
                User password stored as a hash (SHA-1 encrpted)

                
        """
        self._password = value

    password = property(_get_password, _set_password)
    
    def _get_role(self):
        """ Get role value.

            Notes:
                Role of the user.

                
        """
        return self._role

    def _set_role(self, value):
        """ Set role value.

            Notes:
                Role of the user.

                
        """
        self._role = value

    role = property(_get_role, _set_role)
    
    def _get_user_name(self):
        """ Get user_name value.

            Notes:
                Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

                
                This attribute is named `userName` in VSD API.
                
        """
        return self._user_name

    def _set_user_name(self, value):
        """ Set user_name value.

            Notes:
                Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

                
                This attribute is named `userName` in VSD API.
                
        """
        self._user_name = value

    user_name = property(_get_user_name, _set_user_name)
    
    # Methods

    @classmethod
    def is_resource_name_fixed(cls):
        """ Force resource name to True

            Returns:
                bool: always return True for NURESTUser objects

        """

        return True

    def get_resource_url(self):
        """ Get the resource url for the given object.

            Notes:
                This method overrides bambou.NURESTObject method.

            Returns:
                string: a url with NURESTUser specific resource name

            Example:
                >>> RESTUser.get_resource_url()
                https://.../nuage/api/v3_1/me
        """

        name = self.__class__.rest_resource_name
        url = self.__class__.rest_base_url()
        return "%s/%s" % (url, name)

    def get_resource_url_for_child_type(self, nurest_object_type):
        """ Get the resource url for NURESTUser's child objects.

            Notes:
                This method overrides bambou.NURESTObject method.

            Args:
                nurest_object_type (bambou.NURESTObject): type of child

            Returns:
                string: the url for the given object

            Example:
                >>> RESTUser.get_resource_url_for_child_type(NUEnterprise)
                https://.../nuage/api/v3_1/enterprises
        """

        return "%s/%s" % (self.__class__.rest_base_url(), nurest_object_type.rest_resource_name)