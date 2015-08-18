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


from ..fetchers import NUStatisticsFetcher

from bambou import NURESTObject


class NUEgressACLEntryTemplate(NURESTObject):
    """ Represents a EgressACLEntryTemplate in the VSD

        Notes:
            Defines the template of Egress ACL Template entries

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUEgressACLEntryTemplate instead.
    """

    __rest_name__ = u"egressaclentrytemplate"

    def __init__(self, **kwargs):
        """ Initializes a EgressACLEntryTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> egressaclentrytemplate = NUEgressACLEntryTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'EgressACLEntryTemplate')
                >>> egressaclentrytemplate = NUEgressACLEntryTemplate(data=my_dict)
        """

        super(NUEgressACLEntryTemplate, self).__init__()

        # Read/Write Attributes
        
        self._action = None
        self._address_override = None
        self._associated_application_id = None
        self._associated_application_object_id = None
        self._associated_application_object_type = None
        self._description = None
        self._destination_port = None
        self._dscp = None
        self._ether_type = None
        self._flow_logging_enabled = None
        self._location_id = None
        self._location_type = None
        self._master_id = None
        self._network_id = None
        self._network_type = None
        self._policy_state = None
        self._priority = None
        self._protocol = None
        self._reflexive = None
        self._source_port = None
        self._stats_id = None
        self._stats_logging_enabled = None
        
        self.expose_attribute(local_name=u"action", remote_name=u"action", attribute_type=str, is_required=True, is_unique=False, choices=[u'DROP', u'FORWARD', u'REDIRECT'])
        self.expose_attribute(local_name=u"address_override", remote_name=u"addressOverride", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_application_id", remote_name=u"associatedApplicationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_application_object_id", remote_name=u"associatedApplicationObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_application_object_type", remote_name=u"associatedApplicationObjectType", attribute_type=str, is_required=False, is_unique=False, choices=[u'DROP', u'FORWARD', u'REDIRECT'])
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"destination_port", remote_name=u"destinationPort", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"dscp", remote_name=u"DSCP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"ether_type", remote_name=u"etherType", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"flow_logging_enabled", remote_name=u"flowLoggingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"location_id", remote_name=u"locationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"location_type", remote_name=u"locationType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ANY', u'POLICYGROUP', u'REDIRECTIONTARGET', u'SUBNET', u'VPORTTAG', u'ZONE'])
        self.expose_attribute(local_name=u"master_id", remote_name=u"masterId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"network_id", remote_name=u"networkID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"network_type", remote_name=u"networkType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ANY', u'ENDPOINT_DOMAIN', u'ENDPOINT_SUBNET', u'ENDPOINT_ZONE', u'ENTERPRISE_NETWORK', u'INTERNET_POLICYGROUP', u'NETWORK_MACRO_GROUP', u'POLICYGROUP', u'PUBLIC_NETWORK', u'SUBNET', u'ZONE'])
        self.expose_attribute(local_name=u"policy_state", remote_name=u"policyState", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"priority", remote_name=u"priority", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"protocol", remote_name=u"protocol", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"reflexive", remote_name=u"reflexive", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"source_port", remote_name=u"sourcePort", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"stats_id", remote_name=u"statsId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"stats_logging_enabled", remote_name=u"statsLoggingEnabled", attribute_type=bool, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_action(self):
        """ Get action value.

            Notes:
                The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry Possible values are DROP, FORWARD, REDIRECT, .

                
        """
        return self._action

    def _set_action(self, value):
        """ Set action value.

            Notes:
                The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry Possible values are DROP, FORWARD, REDIRECT, .

                
        """
        self._action = value

    action = property(_get_action, _set_action)
    
    def _get_address_override(self):
        """ Get address_override value.

            Notes:
                Overrides the source IP macentries will use this adress as the match criteria.

                
                This attribute is named `addressOverride` in VSD API.
                
        """
        return self._address_override

    def _set_address_override(self, value):
        """ Set address_override value.

            Notes:
                Overrides the source IP macentries will use this adress as the match criteria.

                
                This attribute is named `addressOverride` in VSD API.
                
        """
        self._address_override = value

    address_override = property(_get_address_override, _set_address_override)
    
    def _get_associated_application_id(self):
        """ Get associated_application_id value.

            Notes:
                The associated application ID

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        return self._associated_application_id

    def _set_associated_application_id(self, value):
        """ Set associated_application_id value.

            Notes:
                The associated application ID

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        self._associated_application_id = value

    associated_application_id = property(_get_associated_application_id, _set_associated_application_id)
    
    def _get_associated_application_object_id(self):
        """ Get associated_application_object_id value.

            Notes:
                The associated application object ID

                
                This attribute is named `associatedApplicationObjectID` in VSD API.
                
        """
        return self._associated_application_object_id

    def _set_associated_application_object_id(self, value):
        """ Set associated_application_object_id value.

            Notes:
                The associated application object ID

                
                This attribute is named `associatedApplicationObjectID` in VSD API.
                
        """
        self._associated_application_object_id = value

    associated_application_object_id = property(_get_associated_application_object_id, _set_associated_application_object_id)
    
    def _get_associated_application_object_type(self):
        """ Get associated_application_object_type value.

            Notes:
                The associated application object type Refer to API section for supported types.

                
                This attribute is named `associatedApplicationObjectType` in VSD API.
                
        """
        return self._associated_application_object_type

    def _set_associated_application_object_type(self, value):
        """ Set associated_application_object_type value.

            Notes:
                The associated application object type Refer to API section for supported types.

                
                This attribute is named `associatedApplicationObjectType` in VSD API.
                
        """
        self._associated_application_object_type = value

    associated_application_object_type = property(_get_associated_application_object_type, _set_associated_application_object_type)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of the ACL entry

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of the ACL entry

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_destination_port(self):
        """ Get destination_port value.

            Notes:
                The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range

                
                This attribute is named `destinationPort` in VSD API.
                
        """
        return self._destination_port

    def _set_destination_port(self, value):
        """ Set destination_port value.

            Notes:
                The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range

                
                This attribute is named `destinationPort` in VSD API.
                
        """
        self._destination_port = value

    destination_port = property(_get_destination_port, _set_destination_port)
    
    def _get_dscp(self):
        """ Get dscp value.

            Notes:
                DSCP match condition to be set in the rule. It is either * or from 0-63

                
                This attribute is named `DSCP` in VSD API.
                
        """
        return self._dscp

    def _set_dscp(self, value):
        """ Set dscp value.

            Notes:
                DSCP match condition to be set in the rule. It is either * or from 0-63

                
                This attribute is named `DSCP` in VSD API.
                
        """
        self._dscp = value

    dscp = property(_get_dscp, _set_dscp)
    
    def _get_ether_type(self):
        """ Get ether_type value.

            Notes:
                Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

                
                This attribute is named `etherType` in VSD API.
                
        """
        return self._ether_type

    def _set_ether_type(self, value):
        """ Set ether_type value.

            Notes:
                Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value

                
                This attribute is named `etherType` in VSD API.
                
        """
        self._ether_type = value

    ether_type = property(_get_ether_type, _set_ether_type)
    
    def _get_flow_logging_enabled(self):
        """ Get flow_logging_enabled value.

            Notes:
                Is flow logging enabled for this particular template

                
                This attribute is named `flowLoggingEnabled` in VSD API.
                
        """
        return self._flow_logging_enabled

    def _set_flow_logging_enabled(self, value):
        """ Set flow_logging_enabled value.

            Notes:
                Is flow logging enabled for this particular template

                
                This attribute is named `flowLoggingEnabled` in VSD API.
                
        """
        self._flow_logging_enabled = value

    flow_logging_enabled = property(_get_flow_logging_enabled, _set_flow_logging_enabled)
    
    def _get_location_id(self):
        """ Get location_id value.

            Notes:
                The ID of the location entity (Subnet/Zone/VportTag)

                
                This attribute is named `locationID` in VSD API.
                
        """
        return self._location_id

    def _set_location_id(self, value):
        """ Set location_id value.

            Notes:
                The ID of the location entity (Subnet/Zone/VportTag)

                
                This attribute is named `locationID` in VSD API.
                
        """
        self._location_id = value

    location_id = property(_get_location_id, _set_location_id)
    
    def _get_location_type(self):
        """ Get location_type value.

            Notes:
                Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG Possible values are ANY, SUBNET, ZONE, POLICYGROUP, REDIRECTIONTARGET, VPORTTAG, .

                
                This attribute is named `locationType` in VSD API.
                
        """
        return self._location_type

    def _set_location_type(self, value):
        """ Set location_type value.

            Notes:
                Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG Possible values are ANY, SUBNET, ZONE, POLICYGROUP, REDIRECTIONTARGET, VPORTTAG, .

                
                This attribute is named `locationType` in VSD API.
                
        """
        self._location_type = value

    location_type = property(_get_location_type, _set_location_type)
    
    def _get_master_id(self):
        """ Get master_id value.

            Notes:
                In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

                
                This attribute is named `masterId` in VSD API.
                
        """
        return self._master_id

    def _set_master_id(self, value):
        """ Set master_id value.

            Notes:
                In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.

                
                This attribute is named `masterId` in VSD API.
                
        """
        self._master_id = value

    master_id = property(_get_master_id, _set_master_id)
    
    def _get_network_id(self):
        """ Get network_id value.

            Notes:
                The destination network entity that is referenced(subnet/zone/macro)

                
                This attribute is named `networkID` in VSD API.
                
        """
        return self._network_id

    def _set_network_id(self, value):
        """ Set network_id value.

            Notes:
                The destination network entity that is referenced(subnet/zone/macro)

                
                This attribute is named `networkID` in VSD API.
                
        """
        self._network_id = value

    network_id = property(_get_network_id, _set_network_id)
    
    def _get_network_type(self):
        """ Get network_type value.

            Notes:
                Type of the source network -  VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY Possible values are ENDPOINT_SUBNET, ENDPOINT_ZONE, ENDPOINT_DOMAIN, SUBNET, ZONE, ENTERPRISE_NETWORK, PUBLIC_NETWORK, POLICYGROUP, NETWORK_MACRO_GROUP, ANY, INTERNET_POLICYGROUP, .

                
                This attribute is named `networkType` in VSD API.
                
        """
        return self._network_type

    def _set_network_type(self, value):
        """ Set network_type value.

            Notes:
                Type of the source network -  VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY Possible values are ENDPOINT_SUBNET, ENDPOINT_ZONE, ENDPOINT_DOMAIN, SUBNET, ZONE, ENTERPRISE_NETWORK, PUBLIC_NETWORK, POLICYGROUP, NETWORK_MACRO_GROUP, ANY, INTERNET_POLICYGROUP, .

                
                This attribute is named `networkType` in VSD API.
                
        """
        self._network_type = value

    network_type = property(_get_network_type, _set_network_type)
    
    def _get_policy_state(self):
        """ Get policy_state value.

            Notes:
                

                
                This attribute is named `policyState` in VSD API.
                
        """
        return self._policy_state

    def _set_policy_state(self, value):
        """ Set policy_state value.

            Notes:
                

                
                This attribute is named `policyState` in VSD API.
                
        """
        self._policy_state = value

    policy_state = property(_get_policy_state, _set_policy_state)
    
    def _get_priority(self):
        """ Get priority value.

            Notes:
                The priority of the ACL entry that determines the order of entries

                
        """
        return self._priority

    def _set_priority(self, value):
        """ Set priority value.

            Notes:
                The priority of the ACL entry that determines the order of entries

                
        """
        self._priority = value

    priority = property(_get_priority, _set_priority)
    
    def _get_protocol(self):
        """ Get protocol value.

            Notes:
                Protocol number that must be matched

                
        """
        return self._protocol

    def _set_protocol(self, value):
        """ Set protocol value.

            Notes:
                Protocol number that must be matched

                
        """
        self._protocol = value

    protocol = property(_get_protocol, _set_protocol)
    
    def _get_reflexive(self):
        """ Get reflexive value.

            Notes:
                true means that this ACL entry is reflexive, so there will be a corresponding egress rule that will be created by OVS in the network. false means that there is no corresponding egress rule created by OVS in the network

                
        """
        return self._reflexive

    def _set_reflexive(self, value):
        """ Set reflexive value.

            Notes:
                true means that this ACL entry is reflexive, so there will be a corresponding egress rule that will be created by OVS in the network. false means that there is no corresponding egress rule created by OVS in the network

                
        """
        self._reflexive = value

    reflexive = property(_get_reflexive, _set_reflexive)
    
    def _get_source_port(self):
        """ Get source_port value.

            Notes:
                Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range

                
                This attribute is named `sourcePort` in VSD API.
                
        """
        return self._source_port

    def _set_source_port(self, value):
        """ Set source_port value.

            Notes:
                Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range

                
                This attribute is named `sourcePort` in VSD API.
                
        """
        self._source_port = value

    source_port = property(_get_source_port, _set_source_port)
    
    def _get_stats_id(self):
        """ Get stats_id value.

            Notes:
                The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD

                
                This attribute is named `statsId` in VSD API.
                
        """
        return self._stats_id

    def _set_stats_id(self, value):
        """ Set stats_id value.

            Notes:
                The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD

                
                This attribute is named `statsId` in VSD API.
                
        """
        self._stats_id = value

    stats_id = property(_get_stats_id, _set_stats_id)
    
    def _get_stats_logging_enabled(self):
        """ Get stats_logging_enabled value.

            Notes:
                Is stats logging enabled for this particular template

                
                This attribute is named `statsLoggingEnabled` in VSD API.
                
        """
        return self._stats_logging_enabled

    def _set_stats_logging_enabled(self, value):
        """ Set stats_logging_enabled value.

            Notes:
                Is stats logging enabled for this particular template

                
                This attribute is named `statsLoggingEnabled` in VSD API.
                
        """
        self._stats_logging_enabled = value

    stats_logging_enabled = property(_get_stats_logging_enabled, _set_stats_logging_enabled)
    