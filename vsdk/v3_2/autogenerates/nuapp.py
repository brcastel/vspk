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
from ..fetchers import NUFlowsFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUTiersFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUApp(NURESTObject):
    """ Represents a App in the VSD

        Notes:
            Represents a real life application like a vendor website, or a social network.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUApp instead.
    """

    __rest_name__ = u"application"

    def __init__(self, **kwargs):
        """ Initializes a App instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> app = NUApp(id=u'xxxx-xxx-xxx-xxx', name=u'App')
                >>> app = NUApp(data=my_dict)
        """

        super(NUApp, self).__init__()

        # Read/Write Attributes
        
        self._assoc_egress_acl_template_id = None
        self._assoc_ingress_acl_template_id = None
        self._associated_domain_id = None
        self._associated_domain_type = None
        self._associated_network_object_id = None
        self._associated_network_object_type = None
        self._description = None
        self._name = None
        
        self.expose_attribute(local_name=u"assoc_egress_acl_template_id", remote_name=u"assocEgressACLTemplateId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"assoc_ingress_acl_template_id", remote_name=u"assocIngressACLTemplateId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_domain_id", remote_name=u"associatedDomainID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"associated_domain_type", remote_name=u"associatedDomainType", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"associated_network_object_id", remote_name=u"associatedNetworkObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_network_object_type", remote_name=u"associatedNetworkObjectType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.flows = NUFlowsFetcher.fetcher_with_object(parent_object=self)
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self)
        
        self.tiers = NUTiersFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_assoc_egress_acl_template_id(self):
        """ Get assoc_egress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to

                
                This attribute is named `assocEgressACLTemplateId` in VSD API.
                
        """
        return self._assoc_egress_acl_template_id

    def _set_assoc_egress_acl_template_id(self, value):
        """ Set assoc_egress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to

                
                This attribute is named `assocEgressACLTemplateId` in VSD API.
                
        """
        self._assoc_egress_acl_template_id = value

    assoc_egress_acl_template_id = property(_get_assoc_egress_acl_template_id, _set_assoc_egress_acl_template_id)
    
    def _get_assoc_ingress_acl_template_id(self):
        """ Get assoc_ingress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to

                
                This attribute is named `assocIngressACLTemplateId` in VSD API.
                
        """
        return self._assoc_ingress_acl_template_id

    def _set_assoc_ingress_acl_template_id(self, value):
        """ Set assoc_ingress_acl_template_id value.

            Notes:
                The ID of the ACL template that this application is pointing to

                
                This attribute is named `assocIngressACLTemplateId` in VSD API.
                
        """
        self._assoc_ingress_acl_template_id = value

    assoc_ingress_acl_template_id = property(_get_assoc_ingress_acl_template_id, _set_assoc_ingress_acl_template_id)
    
    def _get_associated_domain_id(self):
        """ Get associated_domain_id value.

            Notes:
                Domain id where the application is running.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        return self._associated_domain_id

    def _set_associated_domain_id(self, value):
        """ Set associated_domain_id value.

            Notes:
                Domain id where the application is running.

                
                This attribute is named `associatedDomainID` in VSD API.
                
        """
        self._associated_domain_id = value

    associated_domain_id = property(_get_associated_domain_id, _set_associated_domain_id)
    
    def _get_associated_domain_type(self):
        """ Get associated_domain_type value.

            Notes:
                Type of domain (DOMAIN, L2DOMAIN). Refer to API section for supported types.

                
                This attribute is named `associatedDomainType` in VSD API.
                
        """
        return self._associated_domain_type

    def _set_associated_domain_type(self, value):
        """ Set associated_domain_type value.

            Notes:
                Type of domain (DOMAIN, L2DOMAIN). Refer to API section for supported types.

                
                This attribute is named `associatedDomainType` in VSD API.
                
        """
        self._associated_domain_type = value

    associated_domain_type = property(_get_associated_domain_type, _set_associated_domain_type)
    
    def _get_associated_network_object_id(self):
        """ Get associated_network_object_id value.

            Notes:
                ID of the network object that this App is associated with.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        return self._associated_network_object_id

    def _set_associated_network_object_id(self, value):
        """ Set associated_network_object_id value.

            Notes:
                ID of the network object that this App is associated with.

                
                This attribute is named `associatedNetworkObjectID` in VSD API.
                
        """
        self._associated_network_object_id = value

    associated_network_object_id = property(_get_associated_network_object_id, _set_associated_network_object_id)
    
    def _get_associated_network_object_type(self):
        """ Get associated_network_object_type value.

            Notes:
                Type of network object this App is associated with (ENTERPRISE, DOMAIN) Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        return self._associated_network_object_type

    def _set_associated_network_object_type(self, value):
        """ Set associated_network_object_type value.

            Notes:
                Type of network object this App is associated with (ENTERPRISE, DOMAIN) Refer to API section for supported types.

                
                This attribute is named `associatedNetworkObjectType` in VSD API.
                
        """
        self._associated_network_object_type = value

    associated_network_object_type = property(_get_associated_network_object_type, _set_associated_network_object_type)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of the application.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of the application.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the application.

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the application.

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    