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


from ..fetchers import NUVLANTemplatesFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUNSPortTemplate(NURESTObject):
    """ Represents a NSPortTemplate in the VSD

        Notes:
            Represents Port Template object under a given gateway template object

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUNSPortTemplate instead.
    """

    __rest_name__ = u"nsporttemplate"

    def __init__(self, **kwargs):
        """ Initializes a NSPortTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsporttemplate = NUNSPortTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'NSPortTemplate')
                >>> nsporttemplate = NUNSPortTemplate(data=my_dict)
        """

        super(NUNSPortTemplate, self).__init__()

        # Read/Write Attributes
        
        self._associated_egress_qos_policy_id = None
        self._associated_vsc_profile_id = None
        self._description = None
        self._infrastructure_profile_id = None
        self._name = None
        self._physical_name = None
        self._port_type = None
        self._vlan_range = None
        
        self.expose_attribute(local_name=u"associated_egress_qos_policy_id", remote_name=u"associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_vsc_profile_id", remote_name=u"associatedVSCProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"infrastructure_profile_id", remote_name=u"infrastructureProfileID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"physical_name", remote_name=u"physicalName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"port_type", remote_name=u"portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS', u'NETWORK'])
        self.expose_attribute(local_name=u"vlan_range", remote_name=u"VLANRange", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.vlan_templates = NUVLANTemplatesFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_associated_egress_qos_policy_id(self):
        """ Get associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        return self._associated_egress_qos_policy_id

    def _set_associated_egress_qos_policy_id(self, value):
        """ Set associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        self._associated_egress_qos_policy_id = value

    associated_egress_qos_policy_id = property(_get_associated_egress_qos_policy_id, _set_associated_egress_qos_policy_id)
    
    def _get_associated_vsc_profile_id(self):
        """ Get associated_vsc_profile_id value.

            Notes:
                The ID of the infrastructure VSC profile this is associated with this instance of a port or port template.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        return self._associated_vsc_profile_id

    def _set_associated_vsc_profile_id(self, value):
        """ Set associated_vsc_profile_id value.

            Notes:
                The ID of the infrastructure VSC profile this is associated with this instance of a port or port template.

                
                This attribute is named `associatedVSCProfileID` in VSD API.
                
        """
        self._associated_vsc_profile_id = value

    associated_vsc_profile_id = property(_get_associated_vsc_profile_id, _set_associated_vsc_profile_id)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the Port

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the Port

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_infrastructure_profile_id(self):
        """ Get infrastructure_profile_id value.

            Notes:
                The ID of the infrastructure profile this instance is associated with.

                
                This attribute is named `infrastructureProfileID` in VSD API.
                
        """
        return self._infrastructure_profile_id

    def _set_infrastructure_profile_id(self, value):
        """ Set infrastructure_profile_id value.

            Notes:
                The ID of the infrastructure profile this instance is associated with.

                
                This attribute is named `infrastructureProfileID` in VSD API.
                
        """
        self._infrastructure_profile_id = value

    infrastructure_profile_id = property(_get_infrastructure_profile_id, _set_infrastructure_profile_id)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the Port

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the Port

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_physical_name(self):
        """ Get physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        return self._physical_name

    def _set_physical_name(self, value):
        """ Set physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        self._physical_name = value

    physical_name = property(_get_physical_name, _set_physical_name)
    
    def _get_port_type(self):
        """ Get port_type value.

            Notes:
                Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .

                
                This attribute is named `portType` in VSD API.
                
        """
        return self._port_type

    def _set_port_type(self, value):
        """ Set port_type value.

            Notes:
                Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .

                
                This attribute is named `portType` in VSD API.
                
        """
        self._port_type = value

    port_type = property(_get_port_type, _set_port_type)
    
    def _get_vlan_range(self):
        """ Get vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        return self._vlan_range

    def _set_vlan_range(self, value):
        """ Set vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        self._vlan_range = value

    vlan_range = property(_get_vlan_range, _set_vlan_range)
    