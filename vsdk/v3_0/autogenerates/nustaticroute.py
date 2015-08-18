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

from bambou import NURESTObject


class NUStaticRoute(NURESTObject):
    """ Represents a StaticRoute in the VSD

        Notes:
            Static routes allow end users to define how traffic is routed through the dVRS in addition to the routes learned by VSC through VM activation. By using static routes, end users can define for example that all traffic with a destination address towards a specific subnet must be forwarded to a specific VM attached in the dVRS and this VM could be a firewall

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUStaticRoute instead.
    """

    __rest_name__ = u"staticroute"

    def __init__(self, **kwargs):
        """ Initializes a StaticRoute instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> staticroute = NUStaticRoute(id=u'xxxx-xxx-xxx-xxx', name=u'StaticRoute')
                >>> staticroute = NUStaticRoute(data=my_dict)
        """

        super(NUStaticRoute, self).__init__()

        # Read/Write Attributes
        
        self._address = None
        self._ip_type = None
        self._netmask = None
        self._next_hop_ip = None
        self._route_distinguisher = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"next_hop_ip", remote_name=u"nextHopIp", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"route_distinguisher", remote_name=u"routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_address(self):
        """ Get address value.

            Notes:
                IP address of the route

                
        """
        return self._address

    def _set_address(self, value):
        """ Set address value.

            Notes:
                IP address of the route

                
        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_ip_type(self):
        """ Get ip_type value.

            Notes:
                IPv4 or IPv6 (only IPv4 supported in R1.0) Possible values are IPV4, IPV6, .

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    def _set_ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IPv4 or IPv6 (only IPv4 supported in R1.0) Possible values are IPV4, IPV6, .

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    ip_type = property(_get_ip_type, _set_ip_type)
    
    def _get_netmask(self):
        """ Get netmask value.

            Notes:
                Netmask associated with the route

                
        """
        return self._netmask

    def _set_netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask associated with the route

                
        """
        self._netmask = value

    netmask = property(_get_netmask, _set_netmask)
    
    def _get_next_hop_ip(self):
        """ Get next_hop_ip value.

            Notes:
                IP address of the next hop. This must be a VM attached to the dVRS

                
                This attribute is named `nextHopIp` in VSD API.
                
        """
        return self._next_hop_ip

    def _set_next_hop_ip(self, value):
        """ Set next_hop_ip value.

            Notes:
                IP address of the next hop. This must be a VM attached to the dVRS

                
                This attribute is named `nextHopIp` in VSD API.
                
        """
        self._next_hop_ip = value

    next_hop_ip = property(_get_next_hop_ip, _set_next_hop_ip)
    
    def _get_route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                Route distinguisher associated with the nexthop. System generates this identifier automatically

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    def _set_route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                Route distinguisher associated with the nexthop. System generates this identifier automatically

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    route_distinguisher = property(_get_route_distinguisher, _set_route_distinguisher)
    