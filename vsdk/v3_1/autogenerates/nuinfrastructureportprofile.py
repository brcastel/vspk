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


class NUInfrastructurePortProfile(NURESTObject):
    """ Represents a InfrastructurePortProfile in the VSD

        Notes:
            Represents an Infrastructure Port Profile

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUInfrastructurePortProfile instead.
    """

    __rest_name__ = u"infrastructureportprofile"

    def __init__(self, **kwargs):
        """ Initializes a InfrastructurePortProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> infrastructureportprofile = NUInfrastructurePortProfile(id=u'xxxx-xxx-xxx-xxx', name=u'InfrastructurePortProfile')
                >>> infrastructureportprofile = NUInfrastructurePortProfile(data=my_dict)
        """

        super(NUInfrastructurePortProfile, self).__init__()

        # Read/Write Attributes
        
        self._description = None
        self._duplex = None
        self._enterprise_id = None
        self._mtu = None
        self._name = None
        self._speed = None
        self._uplink_tag = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"duplex", remote_name=u"duplex", attribute_type=str, is_required=False, is_unique=False, choices=[u'FULL', u'HALF', u'SIMPLEX'])
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"mtu", remote_name=u"mtu", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"speed", remote_name=u"speed", attribute_type=str, is_required=False, is_unique=False, choices=[u'AUTONEGOTIATE', u'BASET10', u'BASET1000', u'BASETX100', u'BASEX10G'])
        self.expose_attribute(local_name=u"uplink_tag", remote_name=u"uplinkTag", attribute_type=str, is_required=False, is_unique=False, choices=[u'PRIMARY', u'SECONDARY', u'TERTIARY', u'UNKNOWN'])
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the Profile instance created.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the Profile instance created.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_duplex(self):
        """ Get duplex value.

            Notes:
                Port Duplex :  Supported values are FULL where both parties can communicate to the other simultaneously and HALF where each party can only communicate to each other in one direction at a time. Possible values are FULL, HALF, SIMPLEX, .

                
        """
        return self._duplex

    def _set_duplex(self, value):
        """ Set duplex value.

            Notes:
                Port Duplex :  Supported values are FULL where both parties can communicate to the other simultaneously and HALF where each party can only communicate to each other in one direction at a time. Possible values are FULL, HALF, SIMPLEX, .

                
        """
        self._duplex = value

    duplex = property(_get_duplex, _set_duplex)
    
    def _get_enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    def _set_enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    enterprise_id = property(_get_enterprise_id, _set_enterprise_id)
    
    def _get_mtu(self):
        """ Get mtu value.

            Notes:
                Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.

                
        """
        return self._mtu

    def _set_mtu(self, value):
        """ Set mtu value.

            Notes:
                Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.

                
        """
        self._mtu = value

    mtu = property(_get_mtu, _set_mtu)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the Infrastructure Profile

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the Infrastructure Profile

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_speed(self):
        """ Get speed value.

            Notes:
                Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate. Possible values are BASET10, BASETX100, BASET1000, BASEX10G, AUTONEGOTIATE, .

                
        """
        return self._speed

    def _set_speed(self, value):
        """ Set speed value.

            Notes:
                Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate. Possible values are BASET10, BASETX100, BASET1000, BASEX10G, AUTONEGOTIATE, .

                
        """
        self._speed = value

    speed = property(_get_speed, _set_speed)
    
    def _get_uplink_tag(self):
        """ Get uplink_tag value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, .

                
                This attribute is named `uplinkTag` in VSD API.
                
        """
        return self._uplink_tag

    def _set_uplink_tag(self, value):
        """ Set uplink_tag value.

            Notes:
                To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, .

                
                This attribute is named `uplinkTag` in VSD API.
                
        """
        self._uplink_tag = value

    uplink_tag = property(_get_uplink_tag, _set_uplink_tag)
    