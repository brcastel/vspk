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


class NUVirtualIP(NURESTObject):
    """ Represents a VirtualIP in the VSD

        Notes:
            Virtual IP address

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUVirtualIP instead.
    """

    __rest_name__ = u"virtualip"

    def __init__(self, **kwargs):
        """ Initializes a VirtualIP instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> virtualip = NUVirtualIP(id=u'xxxx-xxx-xxx-xxx', name=u'VirtualIP')
                >>> virtualip = NUVirtualIP(data=my_dict)
        """

        super(NUVirtualIP, self).__init__()

        # Read/Write Attributes
        
        self._floating_ip_address_id = None
        self._mac = None
        self._subnet_id = None
        self._virtual_ip = None
        
        self.expose_attribute(local_name=u"floating_ip_address_id", remote_name=u"floatingIpAddressId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"mac", remote_name=u"mac", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"subnet_id", remote_name=u"subnetId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"virtual_ip", remote_name=u"virtualIP", attribute_type=str, is_required=True, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_floating_ip_address_id(self):
        """ Get floating_ip_address_id value.

            Notes:
                Id of Floating IP address associated to this virtual ip

                
                This attribute is named `floatingIpAddressId` in VSD API.
                
        """
        return self._floating_ip_address_id

    def _set_floating_ip_address_id(self, value):
        """ Set floating_ip_address_id value.

            Notes:
                Id of Floating IP address associated to this virtual ip

                
                This attribute is named `floatingIpAddressId` in VSD API.
                
        """
        self._floating_ip_address_id = value

    floating_ip_address_id = property(_get_floating_ip_address_id, _set_floating_ip_address_id)
    
    def _get_mac(self):
        """ Get mac value.

            Notes:
                The MAC address of the virtual port

                
        """
        return self._mac

    def _set_mac(self, value):
        """ Set mac value.

            Notes:
                The MAC address of the virtual port

                
        """
        self._mac = value

    mac = property(_get_mac, _set_mac)
    
    def _get_subnet_id(self):
        """ Get subnet_id value.

            Notes:
                Id of subnet to which this ip address belongs

                
                This attribute is named `subnetId` in VSD API.
                
        """
        return self._subnet_id

    def _set_subnet_id(self, value):
        """ Set subnet_id value.

            Notes:
                Id of subnet to which this ip address belongs

                
                This attribute is named `subnetId` in VSD API.
                
        """
        self._subnet_id = value

    subnet_id = property(_get_subnet_id, _set_subnet_id)
    
    def _get_virtual_ip(self):
        """ Get virtual_ip value.

            Notes:
                Virtual IP address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        return self._virtual_ip

    def _set_virtual_ip(self, value):
        """ Set virtual_ip value.

            Notes:
                Virtual IP address

                
                This attribute is named `virtualIP` in VSD API.
                
        """
        self._virtual_ip = value

    virtual_ip = property(_get_virtual_ip, _set_virtual_ip)
    