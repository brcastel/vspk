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


from ..fetchers import NUIngressAdvFwdEntryTemplatesFetcher

from bambou import NURESTObject


class NUIngressAdvFwdTemplate(NURESTObject):
    """ Represents a IngressAdvFwdTemplate in the VSD

        Notes:
            Defines the template for an Ingress Advanced Forwarding

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUIngressAdvFwdTemplate instead.
    """

    __rest_name__ = u"ingressadvfwdtemplate"

    def __init__(self, **kwargs):
        """ Initializes a IngressAdvFwdTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ingressadvfwdtemplate = NUIngressAdvFwdTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'IngressAdvFwdTemplate')
                >>> ingressadvfwdtemplate = NUIngressAdvFwdTemplate(data=my_dict)
        """

        super(NUIngressAdvFwdTemplate, self).__init__()

        # Read/Write Attributes
        
        self._active = None
        self._description = None
        self._master_id = None
        self._name = None
        self._policy_state = None
        self._priority = None
        self._priority_type = None
        
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"master_id", remote_name=u"masterId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"policy_state", remote_name=u"policyState", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"priority", remote_name=u"priority", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"priority_type", remote_name=u"priorityType", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.ingress_adv_fwd_entry_templates = NUIngressAdvFwdEntryTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_active(self):
        """ Get active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        return self._active

    def _set_active(self, value):
        """ Set active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        self._active = value

    active = property(_get_active, _set_active)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the entity

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the entity

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
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
    
    def _get_name(self):
        """ Get name value.

            Notes:
                The name of the entity

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                The name of the entity

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
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
    
    def _get_priority_type(self):
        """ Get priority_type value.

            Notes:
                

                
                This attribute is named `priorityType` in VSD API.
                
        """
        return self._priority_type

    def _set_priority_type(self, value):
        """ Set priority_type value.

            Notes:
                

                
                This attribute is named `priorityType` in VSD API.
                
        """
        self._priority_type = value

    priority_type = property(_get_priority_type, _set_priority_type)
    