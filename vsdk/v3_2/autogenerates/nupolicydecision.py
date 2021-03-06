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


from ..fetchers import NUQOSsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUPolicyDecision(NURESTObject):
    """ Represents a PolicyDecision in the VSD

        Notes:
            This object is a read only object that provides the policy decisions for a particular VM interface

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUPolicyDecision instead.
    """

    __rest_name__ = u"policydecision"

    def __init__(self, **kwargs):
        """ Initializes a PolicyDecision instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> policydecision = NUPolicyDecision(id=u'xxxx-xxx-xxx-xxx', name=u'PolicyDecision')
                >>> policydecision = NUPolicyDecision(data=my_dict)
        """

        super(NUPolicyDecision, self).__init__()

        # Read/Write Attributes
        
        self._egress_acls = None
        self._egress_qos = None
        self._fip_acls = None
        self._ingress_acls = None
        self._ingress_adv_fwd = None
        self._ingress_external_service_acls = None
        self._qos = None
        self._stats = None
        
        self.expose_attribute(local_name=u"egress_acls", remote_name=u"egressACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"egress_qos", remote_name=u"egressQos", attribute_type=object, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"fip_acls", remote_name=u"fipACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ingress_acls", remote_name=u"ingressACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ingress_adv_fwd", remote_name=u"ingressAdvFwd", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ingress_external_service_acls", remote_name=u"ingressExternalServiceACLs", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"qos", remote_name=u"qos", attribute_type=object, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"stats", remote_name=u"stats", attribute_type=object, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_egress_acls(self):
        """ Get egress_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `egressACLs` in VSD API.
                
        """
        return self._egress_acls

    def _set_egress_acls(self, value):
        """ Set egress_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `egressACLs` in VSD API.
                
        """
        self._egress_acls = value

    egress_acls = property(_get_egress_acls, _set_egress_acls)
    
    def _get_egress_qos(self):
        """ Get egress_qos value.

            Notes:
                Egress QoS primitive that was selected

                
                This attribute is named `egressQos` in VSD API.
                
        """
        return self._egress_qos

    def _set_egress_qos(self, value):
        """ Set egress_qos value.

            Notes:
                Egress QoS primitive that was selected

                
                This attribute is named `egressQos` in VSD API.
                
        """
        self._egress_qos = value

    egress_qos = property(_get_egress_qos, _set_egress_qos)
    
    def _get_fip_acls(self):
        """ Get fip_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `fipACLs` in VSD API.
                
        """
        return self._fip_acls

    def _set_fip_acls(self, value):
        """ Set fip_acls value.

            Notes:
                List of actual Egress ACLs that will be applied on the interface of this VM

                
                This attribute is named `fipACLs` in VSD API.
                
        """
        self._fip_acls = value

    fip_acls = property(_get_fip_acls, _set_fip_acls)
    
    def _get_ingress_acls(self):
        """ Get ingress_acls value.

            Notes:
                List of actual Ingress ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressACLs` in VSD API.
                
        """
        return self._ingress_acls

    def _set_ingress_acls(self, value):
        """ Set ingress_acls value.

            Notes:
                List of actual Ingress ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressACLs` in VSD API.
                
        """
        self._ingress_acls = value

    ingress_acls = property(_get_ingress_acls, _set_ingress_acls)
    
    def _get_ingress_adv_fwd(self):
        """ Get ingress_adv_fwd value.

            Notes:
                List of actual Ingress Redirect ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressAdvFwd` in VSD API.
                
        """
        return self._ingress_adv_fwd

    def _set_ingress_adv_fwd(self, value):
        """ Set ingress_adv_fwd value.

            Notes:
                List of actual Ingress Redirect ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressAdvFwd` in VSD API.
                
        """
        self._ingress_adv_fwd = value

    ingress_adv_fwd = property(_get_ingress_adv_fwd, _set_ingress_adv_fwd)
    
    def _get_ingress_external_service_acls(self):
        """ Get ingress_external_service_acls value.

            Notes:
                List of actual Ingress External Service ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressExternalServiceACLs` in VSD API.
                
        """
        return self._ingress_external_service_acls

    def _set_ingress_external_service_acls(self, value):
        """ Set ingress_external_service_acls value.

            Notes:
                List of actual Ingress External Service ACLs that will be applied on the interface of this VM

                
                This attribute is named `ingressExternalServiceACLs` in VSD API.
                
        """
        self._ingress_external_service_acls = value

    ingress_external_service_acls = property(_get_ingress_external_service_acls, _set_ingress_external_service_acls)
    
    def _get_qos(self):
        """ Get qos value.

            Notes:
                QoS primitive that was selected based on inheritance policies

                
        """
        return self._qos

    def _set_qos(self, value):
        """ Set qos value.

            Notes:
                QoS primitive that was selected based on inheritance policies

                
        """
        self._qos = value

    qos = property(_get_qos, _set_qos)
    
    def _get_stats(self):
        """ Get stats value.

            Notes:
                Stats primitive that was selected based on inheritance policies

                
        """
        return self._stats

    def _set_stats(self, value):
        """ Set stats value.

            Notes:
                Stats primitive that was selected based on inheritance policies

                
        """
        self._stats = value

    stats = property(_get_stats, _set_stats)
    