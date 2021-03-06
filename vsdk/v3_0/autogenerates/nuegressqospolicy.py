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



from bambou import NURESTObject


class NUEgressQOSPolicy(NURESTObject):
    """ Represents a EgressQOSPolicy in the VSD

        Notes:
            The object manipulates Egress QoS parameters attached to a Access Port / VLAN or Network port

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUEgressQOSPolicy instead.
    """

    __rest_name__ = u"egressqospolicy"

    def __init__(self, **kwargs):
        """ Initializes a EgressQOSPolicy instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> egressqospolicy = NUEgressQOSPolicy(id=u'xxxx-xxx-xxx-xxx', name=u'EgressQOSPolicy')
                >>> egressqospolicy = NUEgressQOSPolicy(data=my_dict)
        """

        super(NUEgressQOSPolicy, self).__init__()

        # Read/Write Attributes
        
        self._assoc_egress_qos = None
        self._assoc_egress_qos_id = None
        self._description = None
        self._name = None
        self._parent_queue_associated_rate_limiter_id = None
        self._queue1_associated_rate_limiter_id = None
        self._queue1_forwarding_classes = None
        self._queue2_associated_rate_limiter_id = None
        self._queue2_forwarding_classes = None
        self._queue3_associated_rate_limiter_id = None
        self._queue3_forwarding_classes = None
        self._queue4_associated_rate_limiter_id = None
        self._queue4_forwarding_classes = None
        
        self.expose_attribute(local_name=u"assoc_egress_qos", remote_name=u"assocEgressQos", attribute_type=object, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"assoc_egress_qos_id", remote_name=u"assocEgressQosId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"parent_queue_associated_rate_limiter_id", remote_name=u"parentQueueAssociatedRateLimiterID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"queue1_associated_rate_limiter_id", remote_name=u"queue1AssociatedRateLimiterID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"queue1_forwarding_classes", remote_name=u"queue1ForwardingClasses", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name=u"queue2_associated_rate_limiter_id", remote_name=u"queue2AssociatedRateLimiterID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"queue2_forwarding_classes", remote_name=u"queue2ForwardingClasses", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name=u"queue3_associated_rate_limiter_id", remote_name=u"queue3AssociatedRateLimiterID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"queue3_forwarding_classes", remote_name=u"queue3ForwardingClasses", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name=u"queue4_associated_rate_limiter_id", remote_name=u"queue4AssociatedRateLimiterID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"queue4_forwarding_classes", remote_name=u"queue4ForwardingClasses", attribute_type=str, is_required=False, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_assoc_egress_qos(self):
        """ Get assoc_egress_qos value.

            Notes:
                Object associated with this Qos object.

                
                This attribute is named `assocEgressQos` in VSD API.
                
        """
        return self._assoc_egress_qos

    def _set_assoc_egress_qos(self, value):
        """ Set assoc_egress_qos value.

            Notes:
                Object associated with this Qos object.

                
                This attribute is named `assocEgressQos` in VSD API.
                
        """
        self._assoc_egress_qos = value

    assoc_egress_qos = property(_get_assoc_egress_qos, _set_assoc_egress_qos)
    
    def _get_assoc_egress_qos_id(self):
        """ Get assoc_egress_qos_id value.

            Notes:
                ID of object associated with this QoS object

                
                This attribute is named `assocEgressQosId` in VSD API.
                
        """
        return self._assoc_egress_qos_id

    def _set_assoc_egress_qos_id(self, value):
        """ Set assoc_egress_qos_id value.

            Notes:
                ID of object associated with this QoS object

                
                This attribute is named `assocEgressQosId` in VSD API.
                
        """
        self._assoc_egress_qos_id = value

    assoc_egress_qos_id = property(_get_assoc_egress_qos_id, _set_assoc_egress_qos_id)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the QoS object

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the QoS object

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                A unique name of the QoS object

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                A unique name of the QoS object

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_parent_queue_associated_rate_limiter_id(self):
        """ Get parent_queue_associated_rate_limiter_id value.

            Notes:
                ID of the parent rate limiter associated with this Egress QOS policy.

                
                This attribute is named `parentQueueAssociatedRateLimiterID` in VSD API.
                
        """
        return self._parent_queue_associated_rate_limiter_id

    def _set_parent_queue_associated_rate_limiter_id(self, value):
        """ Set parent_queue_associated_rate_limiter_id value.

            Notes:
                ID of the parent rate limiter associated with this Egress QOS policy.

                
                This attribute is named `parentQueueAssociatedRateLimiterID` in VSD API.
                
        """
        self._parent_queue_associated_rate_limiter_id = value

    parent_queue_associated_rate_limiter_id = property(_get_parent_queue_associated_rate_limiter_id, _set_parent_queue_associated_rate_limiter_id)
    
    def _get_queue1_associated_rate_limiter_id(self):
        """ Get queue1_associated_rate_limiter_id value.

            Notes:
                ID of the queue1 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue1AssociatedRateLimiterID` in VSD API.
                
        """
        return self._queue1_associated_rate_limiter_id

    def _set_queue1_associated_rate_limiter_id(self, value):
        """ Set queue1_associated_rate_limiter_id value.

            Notes:
                ID of the queue1 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue1AssociatedRateLimiterID` in VSD API.
                
        """
        self._queue1_associated_rate_limiter_id = value

    queue1_associated_rate_limiter_id = property(_get_queue1_associated_rate_limiter_id, _set_queue1_associated_rate_limiter_id)
    
    def _get_queue1_forwarding_classes(self):
        """ Get queue1_forwarding_classes value.

            Notes:
                Queue1 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue1ForwardingClasses` in VSD API.
                
        """
        return self._queue1_forwarding_classes

    def _set_queue1_forwarding_classes(self, value):
        """ Set queue1_forwarding_classes value.

            Notes:
                Queue1 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue1ForwardingClasses` in VSD API.
                
        """
        self._queue1_forwarding_classes = value

    queue1_forwarding_classes = property(_get_queue1_forwarding_classes, _set_queue1_forwarding_classes)
    
    def _get_queue2_associated_rate_limiter_id(self):
        """ Get queue2_associated_rate_limiter_id value.

            Notes:
                ID of the queue2 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue2AssociatedRateLimiterID` in VSD API.
                
        """
        return self._queue2_associated_rate_limiter_id

    def _set_queue2_associated_rate_limiter_id(self, value):
        """ Set queue2_associated_rate_limiter_id value.

            Notes:
                ID of the queue2 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue2AssociatedRateLimiterID` in VSD API.
                
        """
        self._queue2_associated_rate_limiter_id = value

    queue2_associated_rate_limiter_id = property(_get_queue2_associated_rate_limiter_id, _set_queue2_associated_rate_limiter_id)
    
    def _get_queue2_forwarding_classes(self):
        """ Get queue2_forwarding_classes value.

            Notes:
                Queue2 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue2ForwardingClasses` in VSD API.
                
        """
        return self._queue2_forwarding_classes

    def _set_queue2_forwarding_classes(self, value):
        """ Set queue2_forwarding_classes value.

            Notes:
                Queue2 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue2ForwardingClasses` in VSD API.
                
        """
        self._queue2_forwarding_classes = value

    queue2_forwarding_classes = property(_get_queue2_forwarding_classes, _set_queue2_forwarding_classes)
    
    def _get_queue3_associated_rate_limiter_id(self):
        """ Get queue3_associated_rate_limiter_id value.

            Notes:
                ID of the queue3 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue3AssociatedRateLimiterID` in VSD API.
                
        """
        return self._queue3_associated_rate_limiter_id

    def _set_queue3_associated_rate_limiter_id(self, value):
        """ Set queue3_associated_rate_limiter_id value.

            Notes:
                ID of the queue3 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue3AssociatedRateLimiterID` in VSD API.
                
        """
        self._queue3_associated_rate_limiter_id = value

    queue3_associated_rate_limiter_id = property(_get_queue3_associated_rate_limiter_id, _set_queue3_associated_rate_limiter_id)
    
    def _get_queue3_forwarding_classes(self):
        """ Get queue3_forwarding_classes value.

            Notes:
                Queue3 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue3ForwardingClasses` in VSD API.
                
        """
        return self._queue3_forwarding_classes

    def _set_queue3_forwarding_classes(self, value):
        """ Set queue3_forwarding_classes value.

            Notes:
                Queue3 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue3ForwardingClasses` in VSD API.
                
        """
        self._queue3_forwarding_classes = value

    queue3_forwarding_classes = property(_get_queue3_forwarding_classes, _set_queue3_forwarding_classes)
    
    def _get_queue4_associated_rate_limiter_id(self):
        """ Get queue4_associated_rate_limiter_id value.

            Notes:
                ID of the queue4 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue4AssociatedRateLimiterID` in VSD API.
                
        """
        return self._queue4_associated_rate_limiter_id

    def _set_queue4_associated_rate_limiter_id(self, value):
        """ Set queue4_associated_rate_limiter_id value.

            Notes:
                ID of the queue4 rate limiter associated with this Egress QOS policy.

                
                This attribute is named `queue4AssociatedRateLimiterID` in VSD API.
                
        """
        self._queue4_associated_rate_limiter_id = value

    queue4_associated_rate_limiter_id = property(_get_queue4_associated_rate_limiter_id, _set_queue4_associated_rate_limiter_id)
    
    def _get_queue4_forwarding_classes(self):
        """ Get queue4_forwarding_classes value.

            Notes:
                Queue4 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue4ForwardingClasses` in VSD API.
                
        """
        return self._queue4_forwarding_classes

    def _set_queue4_forwarding_classes(self, value):
        """ Set queue4_forwarding_classes value.

            Notes:
                Queue4 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `queue4ForwardingClasses` in VSD API.
                
        """
        self._queue4_forwarding_classes = value

    queue4_forwarding_classes = property(_get_queue4_forwarding_classes, _set_queue4_forwarding_classes)
    