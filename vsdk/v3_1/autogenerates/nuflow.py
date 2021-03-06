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


from ..fetchers import NUFlowForwardingPoliciesFetcher
from ..fetchers import NUFlowSecurityPoliciesFetcher

from bambou import NURESTObject


class NUFlow(NURESTObject):
    """ Represents a Flow in the VSD

        Notes:
            Flow represents the traffic between two different tiers.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUFlow instead.
    """

    __rest_name__ = u"flow"

    def __init__(self, **kwargs):
        """ Initializes a Flow instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> flow = NUFlow(id=u'xxxx-xxx-xxx-xxx', name=u'Flow')
                >>> flow = NUFlow(data=my_dict)
        """

        super(NUFlow, self).__init__()

        # Read/Write Attributes
        
        self._description = None
        self._destination_tier_id = None
        self._metadata = None
        self._name = None
        self._origin_tier_id = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"destination_tier_id", remote_name=u"destinationTierID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"metadata", remote_name=u"metadata", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"origin_tier_id", remote_name=u"originTierID", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.flow_forwarding_policies = NUFlowForwardingPoliciesFetcher.fetcher_with_object(parent_object=self)
        
        self.flow_security_policies = NUFlowSecurityPoliciesFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of the flow.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of the flow.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_destination_tier_id(self):
        """ Get destination_tier_id value.

            Notes:
                Flow destination tier id.

                
                This attribute is named `destinationTierID` in VSD API.
                
        """
        return self._destination_tier_id

    def _set_destination_tier_id(self, value):
        """ Set destination_tier_id value.

            Notes:
                Flow destination tier id.

                
                This attribute is named `destinationTierID` in VSD API.
                
        """
        self._destination_tier_id = value

    destination_tier_id = property(_get_destination_tier_id, _set_destination_tier_id)
    
    def _get_metadata(self):
        """ Get metadata value.

            Notes:
                Metadata field to store flow related data.

                
        """
        return self._metadata

    def _set_metadata(self, value):
        """ Set metadata value.

            Notes:
                Metadata field to store flow related data.

                
        """
        self._metadata = value

    metadata = property(_get_metadata, _set_metadata)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the flow.

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the flow.

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_origin_tier_id(self):
        """ Get origin_tier_id value.

            Notes:
                Flow origin tier id.

                
                This attribute is named `originTierID` in VSD API.
                
        """
        return self._origin_tier_id

    def _set_origin_tier_id(self, value):
        """ Set origin_tier_id value.

            Notes:
                Flow origin tier id.

                
                This attribute is named `originTierID` in VSD API.
                
        """
        self._origin_tier_id = value

    origin_tier_id = property(_get_origin_tier_id, _set_origin_tier_id)
    