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


from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUVPortsFetcher

from bambou import NURESTObject


class NUPolicyGroup(NURESTObject):
    """ Represents a PolicyGroup in the VSD

        Notes:
            PolicyGroup is group of policys on which a user can policies like ACL, QoS etc.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUPolicyGroup instead.
    """

    __rest_name__ = u"policygroup"

    def __init__(self, **kwargs):
        """ Initializes a PolicyGroup instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> policygroup = NUPolicyGroup(id=u'xxxx-xxx-xxx-xxx', name=u'PolicyGroup')
                >>> policygroup = NUPolicyGroup(data=my_dict)
        """

        super(NUPolicyGroup, self).__init__()

        # Read/Write Attributes
        
        self._description = None
        self._evpn_community_tag = None
        self._external = None
        self._name = None
        self._policy_group_id = None
        self._template_id = None
        self._type = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"evpn_community_tag", remote_name=u"EVPNCommunityTag", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"external", remote_name=u"external", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"policy_group_id", remote_name=u"policyGroupId", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str, is_required=True, is_unique=False, choices=[u'HARDWARE', u'SOFTWARE'])
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Describes this policy group

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Describes this policy group

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_evpn_community_tag(self):
        """ Get evpn_community_tag value.

            Notes:
                Assigned by VSD. An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.

                
                This attribute is named `EVPNCommunityTag` in VSD API.
                
        """
        return self._evpn_community_tag

    def _set_evpn_community_tag(self, value):
        """ Set evpn_community_tag value.

            Notes:
                Assigned by VSD. An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.

                
                This attribute is named `EVPNCommunityTag` in VSD API.
                
        """
        self._evpn_community_tag = value

    evpn_community_tag = property(_get_evpn_community_tag, _set_evpn_community_tag)
    
    def _get_external(self):
        """ Get external value.

            Notes:
                Indicates whether this PG is internal to VSP or not.

                
        """
        return self._external

    def _set_external(self, value):
        """ Set external value.

            Notes:
                Indicates whether this PG is internal to VSP or not.

                
        """
        self._external = value

    external = property(_get_external, _set_external)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the policy group

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the policy group

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_policy_group_id(self):
        """ Get policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupId` in VSD API.
                
        """
        return self._policy_group_id

    def _set_policy_group_id(self, value):
        """ Set policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupId` in VSD API.
                
        """
        self._policy_group_id = value

    policy_group_id = property(_get_policy_group_id, _set_policy_group_id)
    
    def _get_template_id(self):
        """ Get template_id value.

            Notes:
                Determines which template ID this policy group belongs to.

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    def _set_template_id(self, value):
        """ Set template_id value.

            Notes:
                Determines which template ID this policy group belongs to.

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    template_id = property(_get_template_id, _set_template_id)
    
    def _get_type(self):
        """ Get type value.

            Notes:
                Type of policy group - possible values SOFTWARE/HARDWARE Possible values are SOFTWARE, HARDWARE, .

                
        """
        return self._type

    def _set_type(self, value):
        """ Set type value.

            Notes:
                Type of policy group - possible values SOFTWARE/HARDWARE Possible values are SOFTWARE, HARDWARE, .

                
        """
        self._type = value

    type = property(_get_type, _set_type)
    