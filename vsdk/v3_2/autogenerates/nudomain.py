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


from ..fetchers import NUBridgeInterfacesFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUDomainsFetcher
from ..fetchers import NUDomainTemplatesFetcher
from ..fetchers import NUEgressACLEntryTemplatesFetcher
from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUExternalAppServicesFetcher
from ..fetchers import NUFloatingIpsFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUHostInterfacesFetcher
from ..fetchers import NUIngressACLEntryTemplatesFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUIngressAdvFwdTemplatesFetcher
from ..fetchers import NUIngressExternalServiceTemplatesFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUQOSsFetcher
from ..fetchers import NURedirectionTargetsFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUStatisticsFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUSubnetsFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUUplinkRDsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVMsFetcher
from ..fetchers import NUVPNConnectionsFetcher
from ..fetchers import NUVPortsFetcher
from ..fetchers import NUZonesFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUDomain(NURESTObject):
    """ Represents a Domain in the VSD

        Notes:
            This object is used to manipulate domain state. A domain corresponds to a distributed Virtual Router and Switch (dVRS)

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUDomain instead.
    """

    __rest_name__ = u"domain"

    def __init__(self, **kwargs):
        """ Initializes a Domain instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> domain = NUDomain(id=u'xxxx-xxx-xxx-xxx', name=u'Domain')
                >>> domain = NUDomain(data=my_dict)
        """

        super(NUDomain, self).__init__()

        # Read/Write Attributes
        
        self._application_deployment_policy = None
        self._associated_multicast_channel_map_id = None
        self._back_haul_route_distinguisher = None
        self._back_haul_route_target = None
        self._back_haul_vnid = None
        self._customer_id = None
        self._description = None
        self._dhcp_behavior = None
        self._dhcp_server_address = None
        self._dhcp_server_addresses = None
        self._ecmp_count = None
        self._encryption = None
        self._export_route_target = None
        self._global_routing_enabled = None
        self._import_route_target = None
        self._label_id = None
        self._leaking_enabled = None
        self._maintenance_mode = None
        self._multicast = None
        self._name = None
        self._pat_enabled = None
        self._permitted_action = None
        self._policy_change_status = None
        self._route_distinguisher = None
        self._route_target = None
        self._secondary_dhcp_server_address = None
        self._service_id = None
        self._stretched = None
        self._template_id = None
        self._tunnel_type = None
        self._uplink_preference = None
        
        self.expose_attribute(local_name=u"application_deployment_policy", remote_name=u"applicationDeploymentPolicy", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'ZONE'])
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"back_haul_route_distinguisher", remote_name=u"backHaulRouteDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"back_haul_route_target", remote_name=u"backHaulRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"back_haul_vnid", remote_name=u"backHaulVNID", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"customer_id", remote_name=u"customerID", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"dhcp_behavior", remote_name=u"DHCPBehavior", attribute_type=str, is_required=False, is_unique=False, choices=[u'CONSUME', u'FLOOD', u'RELAY'])
        self.expose_attribute(local_name=u"dhcp_server_address", remote_name=u"DHCPServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"dhcp_server_addresses", remote_name=u"dhcpServerAddresses", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ecmp_count", remote_name=u"ECMPCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"encryption", remote_name=u"encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED'])
        self.expose_attribute(local_name=u"export_route_target", remote_name=u"exportRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"global_routing_enabled", remote_name=u"globalRoutingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"import_route_target", remote_name=u"importRouteTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"label_id", remote_name=u"labelID", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"leaking_enabled", remote_name=u"leakingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"pat_enabled", remote_name=u"PATEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name=u"policy_change_status", remote_name=u"policyChangeStatus", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name=u"route_distinguisher", remote_name=u"routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"route_target", remote_name=u"routeTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"secondary_dhcp_server_address", remote_name=u"secondaryDHCPServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"service_id", remote_name=u"serviceID", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"stretched", remote_name=u"stretched", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"tunnel_type", remote_name=u"tunnelType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DC_DEFAULT', u'GRE', u'VXLAN'])
        self.expose_attribute(local_name=u"uplink_preference", remote_name=u"uplinkPreference", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'PRIMARY_SECONDARY', u'SECONDARY', u'SECONDARY_PRIMARY', u'SYMMETRIC'])
        
        # Fetchers
        
        self.bridge_interfaces = NUBridgeInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self)
        
        self.domains = NUDomainsFetcher.fetcher_with_object(parent_object=self)
        
        self.domain_templates = NUDomainTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.egress_acl_entry_templates = NUEgressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.egress_acl_templates = NUEgressACLTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.external_app_services = NUExternalAppServicesFetcher.fetcher_with_object(parent_object=self)
        
        self.floating_ips = NUFloatingIpsFetcher.fetcher_with_object(parent_object=self)
        
        self.groups = NUGroupsFetcher.fetcher_with_object(parent_object=self)
        
        self.host_interfaces = NUHostInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_acl_entry_templates = NUIngressACLEntryTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_acl_templates = NUIngressACLTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_adv_fwd_templates = NUIngressAdvFwdTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.ingress_external_service_templates = NUIngressExternalServiceTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self)
        
        self.permitted_actions = NUPermittedActionsFetcher.fetcher_with_object(parent_object=self)
        
        self.policy_groups = NUPolicyGroupsFetcher.fetcher_with_object(parent_object=self)
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self)
        
        self.redirection_targets = NURedirectionTargetsFetcher.fetcher_with_object(parent_object=self)
        
        self.static_routes = NUStaticRoutesFetcher.fetcher_with_object(parent_object=self)
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self)
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self)
        
        self.subnets = NUSubnetsFetcher.fetcher_with_object(parent_object=self)
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self)
        
        self.uplink_rds = NUUplinkRDsFetcher.fetcher_with_object(parent_object=self)
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self)
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self)
        
        self.vpn_connections = NUVPNConnectionsFetcher.fetcher_with_object(parent_object=self)
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self)
        
        self.zones = NUZonesFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_application_deployment_policy(self):
        """ Get application_deployment_policy value.

            Notes:
                Application deployment policy. Possible values are NONE, ZONE, .

                
                This attribute is named `applicationDeploymentPolicy` in VSD API.
                
        """
        return self._application_deployment_policy

    def _set_application_deployment_policy(self, value):
        """ Set application_deployment_policy value.

            Notes:
                Application deployment policy. Possible values are NONE, ZONE, .

                
                This attribute is named `applicationDeploymentPolicy` in VSD API.
                
        """
        self._application_deployment_policy = value

    application_deployment_policy = property(_get_application_deployment_policy, _set_application_deployment_policy)
    
    def _get_associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this domain is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    def _set_associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this domain is associated with. This has to be set when  enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    associated_multicast_channel_map_id = property(_get_associated_multicast_channel_map_id, _set_associated_multicast_channel_map_id)
    
    def _get_back_haul_route_distinguisher(self):
        """ Get back_haul_route_distinguisher value.

            Notes:
                Route distinguisher associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteDistinguisher` in VSD API.
                
        """
        return self._back_haul_route_distinguisher

    def _set_back_haul_route_distinguisher(self, value):
        """ Set back_haul_route_distinguisher value.

            Notes:
                Route distinguisher associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteDistinguisher` in VSD API.
                
        """
        self._back_haul_route_distinguisher = value

    back_haul_route_distinguisher = property(_get_back_haul_route_distinguisher, _set_back_haul_route_distinguisher)
    
    def _get_back_haul_route_target(self):
        """ Get back_haul_route_target value.

            Notes:
                Route target associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteTarget` in VSD API.
                
        """
        return self._back_haul_route_target

    def _set_back_haul_route_target(self, value):
        """ Set back_haul_route_target value.

            Notes:
                Route target associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically

                
                This attribute is named `backHaulRouteTarget` in VSD API.
                
        """
        self._back_haul_route_target = value

    back_haul_route_target = property(_get_back_haul_route_target, _set_back_haul_route_target)
    
    def _get_back_haul_vnid(self):
        """ Get back_haul_vnid value.

            Notes:
                Current BackHaul Network's globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `backHaulVNID` in VSD API.
                
        """
        return self._back_haul_vnid

    def _set_back_haul_vnid(self, value):
        """ Set back_haul_vnid value.

            Notes:
                Current BackHaul Network's globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `backHaulVNID` in VSD API.
                
        """
        self._back_haul_vnid = value

    back_haul_vnid = property(_get_back_haul_vnid, _set_back_haul_vnid)
    
    def _get_customer_id(self):
        """ Get customer_id value.

            Notes:
                The customerID that is created in the VSC and identifies this dVRS. This is auto-generated by VSD

                
                This attribute is named `customerID` in VSD API.
                
        """
        return self._customer_id

    def _set_customer_id(self, value):
        """ Set customer_id value.

            Notes:
                The customerID that is created in the VSC and identifies this dVRS. This is auto-generated by VSD

                
                This attribute is named `customerID` in VSD API.
                
        """
        self._customer_id = value

    customer_id = property(_get_customer_id, _set_customer_id)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description string of the domain that is provided by the user

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description string of the domain that is provided by the user

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_dhcp_behavior(self):
        """ Get dhcp_behavior value.

            Notes:
                DHCPBehaviorType is an enum that indicates DHCP Behavior of VRS having VM's under this domain. Possible values are FLOOD, CONSUME ,RELAY Possible values are CONSUME, FLOOD, RELAY, .

                
                This attribute is named `DHCPBehavior` in VSD API.
                
        """
        return self._dhcp_behavior

    def _set_dhcp_behavior(self, value):
        """ Set dhcp_behavior value.

            Notes:
                DHCPBehaviorType is an enum that indicates DHCP Behavior of VRS having VM's under this domain. Possible values are FLOOD, CONSUME ,RELAY Possible values are CONSUME, FLOOD, RELAY, .

                
                This attribute is named `DHCPBehavior` in VSD API.
                
        """
        self._dhcp_behavior = value

    dhcp_behavior = property(_get_dhcp_behavior, _set_dhcp_behavior)
    
    def _get_dhcp_server_address(self):
        """ Get dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `DHCPServerAddress` in VSD API.
                
        """
        return self._dhcp_server_address

    def _set_dhcp_server_address(self, value):
        """ Set dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `DHCPServerAddress` in VSD API.
                
        """
        self._dhcp_server_address = value

    dhcp_server_address = property(_get_dhcp_server_address, _set_dhcp_server_address)
    
    def _get_dhcp_server_addresses(self):
        """ Get dhcp_server_addresses value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `dhcpServerAddresses` in VSD API.
                
        """
        return self._dhcp_server_addresses

    def _set_dhcp_server_addresses(self, value):
        """ Set dhcp_server_addresses value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `dhcpServerAddresses` in VSD API.
                
        """
        self._dhcp_server_addresses = value

    dhcp_server_addresses = property(_get_dhcp_server_addresses, _set_dhcp_server_addresses)
    
    def _get_ecmp_count(self):
        """ Get ecmp_count value.

            Notes:
                Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP

                
                This attribute is named `ECMPCount` in VSD API.
                
        """
        return self._ecmp_count

    def _set_ecmp_count(self, value):
        """ Set ecmp_count value.

            Notes:
                Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP

                
                This attribute is named `ECMPCount` in VSD API.
                
        """
        self._ecmp_count = value

    ecmp_count = property(_get_ecmp_count, _set_ecmp_count)
    
    def _get_encryption(self):
        """ Get encryption value.

            Notes:
                Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

                
        """
        return self._encryption

    def _set_encryption(self, value):
        """ Set encryption value.

            Notes:
                Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .

                
        """
        self._encryption = value

    encryption = property(_get_encryption, _set_encryption)
    
    def _get_export_route_target(self):
        """ Get export_route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `exportRouteTarget` in VSD API.
                
        """
        return self._export_route_target

    def _set_export_route_target(self, value):
        """ Set export_route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `exportRouteTarget` in VSD API.
                
        """
        self._export_route_target = value

    export_route_target = property(_get_export_route_target, _set_export_route_target)
    
    def _get_global_routing_enabled(self):
        """ Get global_routing_enabled value.

            Notes:
                Indicates if this domain is a globally routable domain or not - boolean true/false

                
                This attribute is named `globalRoutingEnabled` in VSD API.
                
        """
        return self._global_routing_enabled

    def _set_global_routing_enabled(self, value):
        """ Set global_routing_enabled value.

            Notes:
                Indicates if this domain is a globally routable domain or not - boolean true/false

                
                This attribute is named `globalRoutingEnabled` in VSD API.
                
        """
        self._global_routing_enabled = value

    global_routing_enabled = property(_get_global_routing_enabled, _set_global_routing_enabled)
    
    def _get_import_route_target(self):
        """ Get import_route_target value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `importRouteTarget` in VSD API.
                
        """
        return self._import_route_target

    def _set_import_route_target(self, value):
        """ Set import_route_target value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `importRouteTarget` in VSD API.
                
        """
        self._import_route_target = value

    import_route_target = property(_get_import_route_target, _set_import_route_target)
    
    def _get_label_id(self):
        """ Get label_id value.

            Notes:
                The label associated with the dVRS. This is a read only attribute

                
                This attribute is named `labelID` in VSD API.
                
        """
        return self._label_id

    def _set_label_id(self, value):
        """ Set label_id value.

            Notes:
                The label associated with the dVRS. This is a read only attribute

                
                This attribute is named `labelID` in VSD API.
                
        """
        self._label_id = value

    label_id = property(_get_label_id, _set_label_id)
    
    def _get_leaking_enabled(self):
        """ Get leaking_enabled value.

            Notes:
                Indicates if this domain is a leakable domain or not - boolean true/false

                
                This attribute is named `leakingEnabled` in VSD API.
                
        """
        return self._leaking_enabled

    def _set_leaking_enabled(self, value):
        """ Set leaking_enabled value.

            Notes:
                Indicates if this domain is a leakable domain or not - boolean true/false

                
                This attribute is named `leakingEnabled` in VSD API.
                
        """
        self._leaking_enabled = value

    leaking_enabled = property(_get_leaking_enabled, _set_leaking_enabled)
    
    def _get_maintenance_mode(self):
        """ Get maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        return self._maintenance_mode

    def _set_maintenance_mode(self, value):
        """ Set maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        self._maintenance_mode = value

    maintenance_mode = property(_get_maintenance_mode, _set_maintenance_mode)
    
    def _get_multicast(self):
        """ Get multicast value.

            Notes:
                multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        return self._multicast

    def _set_multicast(self, value):
        """ Set multicast value.

            Notes:
                multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .

                
        """
        self._multicast = value

    multicast = property(_get_multicast, _set_multicast)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_pat_enabled(self):
        """ Get pat_enabled value.

            Notes:
                Indicates whether PAT is enabled for the subnets in this domain - ENABLED/DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        return self._pat_enabled

    def _set_pat_enabled(self, value):
        """ Set pat_enabled value.

            Notes:
                Indicates whether PAT is enabled for the subnets in this domain - ENABLED/DISABLED Possible values are INHERITED, ENABLED, DISABLED, .

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        self._pat_enabled = value

    pat_enabled = property(_get_pat_enabled, _set_pat_enabled)
    
    def _get_permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/DEPLOY for the Domain Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    def _set_permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/DEPLOY for the Domain Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    permitted_action = property(_get_permitted_action, _set_permitted_action)
    
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
    
    def _get_route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    def _set_route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    route_distinguisher = property(_get_route_distinguisher, _set_route_distinguisher)
    
    def _get_route_target(self):
        """ Get route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        return self._route_target

    def _set_route_target(self, value):
        """ Set route_target value.

            Notes:
                Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        self._route_target = value

    route_target = property(_get_route_target, _set_route_target)
    
    def _get_secondary_dhcp_server_address(self):
        """ Get secondary_dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `secondaryDHCPServerAddress` in VSD API.
                
        """
        return self._secondary_dhcp_server_address

    def _set_secondary_dhcp_server_address(self, value):
        """ Set secondary_dhcp_server_address value.

            Notes:
                when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set

                
                This attribute is named `secondaryDHCPServerAddress` in VSD API.
                
        """
        self._secondary_dhcp_server_address = value

    secondary_dhcp_server_address = property(_get_secondary_dhcp_server_address, _set_secondary_dhcp_server_address)
    
    def _get_service_id(self):
        """ Get service_id value.

            Notes:
                The serviceID of the Virtual Router created in VSC and is associated with this object. This is auto-generated by VSD

                
                This attribute is named `serviceID` in VSD API.
                
        """
        return self._service_id

    def _set_service_id(self, value):
        """ Set service_id value.

            Notes:
                The serviceID of the Virtual Router created in VSC and is associated with this object. This is auto-generated by VSD

                
                This attribute is named `serviceID` in VSD API.
                
        """
        self._service_id = value

    service_id = property(_get_service_id, _set_service_id)
    
    def _get_stretched(self):
        """ Get stretched value.

            Notes:
                Indicates whether this domain is streched,if so remote VM resolutions will be allowed

                
        """
        return self._stretched

    def _set_stretched(self, value):
        """ Set stretched value.

            Notes:
                Indicates whether this domain is streched,if so remote VM resolutions will be allowed

                
        """
        self._stretched = value

    stretched = property(_get_stretched, _set_stretched)
    
    def _get_template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this domain was created from. This should be set when instantiating a domain

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    def _set_template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this domain was created from. This should be set when instantiating a domain

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    template_id = property(_get_template_id, _set_template_id)
    
    def _get_tunnel_type(self):
        """ Get tunnel_type value.

            Notes:
                Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        return self._tunnel_type

    def _set_tunnel_type(self, value):
        """ Set tunnel_type value.

            Notes:
                Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .

                
                This attribute is named `tunnelType` in VSD API.
                
        """
        self._tunnel_type = value

    tunnel_type = property(_get_tunnel_type, _set_tunnel_type)
    
    def _get_uplink_preference(self):
        """ Get uplink_preference value.

            Notes:
                Indicates the preferencial path selection for network traffic in this domain - Default is Primary 1 and Secondary 2. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .

                
                This attribute is named `uplinkPreference` in VSD API.
                
        """
        return self._uplink_preference

    def _set_uplink_preference(self, value):
        """ Set uplink_preference value.

            Notes:
                Indicates the preferencial path selection for network traffic in this domain - Default is Primary 1 and Secondary 2. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .

                
                This attribute is named `uplinkPreference` in VSD API.
                
        """
        self._uplink_preference = value

    uplink_preference = property(_get_uplink_preference, _set_uplink_preference)
    