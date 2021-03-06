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


from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUNetworkLayout(NURESTObject):
    """ Represents a NetworkLayout in the VSD

        Notes:
            This API defines the AS number that should be used in the data center as well as the IP address of the route reflector

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUNetworkLayout instead.
    """

    __rest_name__ = u"networklayout"

    def __init__(self, **kwargs):
        """ Initializes a NetworkLayout instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> networklayout = NUNetworkLayout(id=u'xxxx-xxx-xxx-xxx', name=u'NetworkLayout')
                >>> networklayout = NUNetworkLayout(data=my_dict)
        """

        super(NUNetworkLayout, self).__init__()

        # Read/Write Attributes
        
        self._autonomous_system_num = None
        self._route_reflector_ip = None
        self._service_type = None
        
        self.expose_attribute(local_name=u"autonomous_system_num", remote_name=u"autonomousSystemNum", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"route_reflector_ip", remote_name=u"routeReflectorIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"service_type", remote_name=u"serviceType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ROUTER_ONLY', u'ROUTER_SWITCH', u'SUBNET_ONLY'])
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_autonomous_system_num(self):
        """ Get autonomous_system_num value.

            Notes:
                The AS number associated with this data center

                
                This attribute is named `autonomousSystemNum` in VSD API.
                
        """
        return self._autonomous_system_num

    def _set_autonomous_system_num(self, value):
        """ Set autonomous_system_num value.

            Notes:
                The AS number associated with this data center

                
                This attribute is named `autonomousSystemNum` in VSD API.
                
        """
        self._autonomous_system_num = value

    autonomous_system_num = property(_get_autonomous_system_num, _set_autonomous_system_num)
    
    def _get_route_reflector_ip(self):
        """ Get route_reflector_ip value.

            Notes:
                The IP address of the route reflector that can be used by the VSCs

                
                This attribute is named `routeReflectorIP` in VSD API.
                
        """
        return self._route_reflector_ip

    def _set_route_reflector_ip(self, value):
        """ Set route_reflector_ip value.

            Notes:
                The IP address of the route reflector that can be used by the VSCs

                
                This attribute is named `routeReflectorIP` in VSD API.
                
        """
        self._route_reflector_ip = value

    route_reflector_ip = property(_get_route_reflector_ip, _set_route_reflector_ip)
    
    def _get_service_type(self):
        """ Get service_type value.

            Notes:
                Identifies whether L3 or L2 services are supported. Only L3services are supported in R1.0. Possible values are ROUTER_ONLY, ROUTER_SWITCH, SUBNET_ONLY, .

                
                This attribute is named `serviceType` in VSD API.
                
        """
        return self._service_type

    def _set_service_type(self, value):
        """ Set service_type value.

            Notes:
                Identifies whether L3 or L2 services are supported. Only L3services are supported in R1.0. Possible values are ROUTER_ONLY, ROUTER_SWITCH, SUBNET_ONLY, .

                
                This attribute is named `serviceType` in VSD API.
                
        """
        self._service_type = value

    service_type = property(_get_service_type, _set_service_type)
    