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


class NUDHCPOption(NURESTObject):
    """ Represents a DHCPOption in the VSD

        Notes:
            Allows the definition of one or more DHCP options that will be provided to all VMs that are associated with a given domain. DHCP options are provided as Type- Length-Value (TLV). There is no validation by VSD on whether these options are valid or not. It is up to the user to guarantee that the options make sense for their application

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUDHCPOption instead.
    """

    __rest_name__ = u"dhcpoption"

    def __init__(self, **kwargs):
        """ Initializes a DHCPOption instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> dhcpoption = NUDHCPOption(id=u'xxxx-xxx-xxx-xxx', name=u'DHCPOption')
                >>> dhcpoption = NUDHCPOption(data=my_dict)
        """

        super(NUDHCPOption, self).__init__()

        # Read/Write Attributes
        
        self._actual_type = None
        self._actual_values = None
        self._length = None
        self._type = None
        self._value = None
        
        self.expose_attribute(local_name=u"actual_type", remote_name=u"actualType", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"actual_values", remote_name=u"actualValues", attribute_type=list, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"length", remote_name=u"length", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"value", remote_name=u"value", attribute_type=str, is_required=True, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_actual_type(self):
        """ Get actual_type value.

            Notes:
                This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute

                
                This attribute is named `actualType` in VSD API.
                
        """
        return self._actual_type

    def _set_actual_type(self, value):
        """ Set actual_type value.

            Notes:
                This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute

                
                This attribute is named `actualType` in VSD API.
                
        """
        self._actual_type = value

    actual_type = property(_get_actual_type, _set_actual_type)
    
    def _get_actual_values(self):
        """ Get actual_values value.

            Notes:
                This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute

                
                This attribute is named `actualValues` in VSD API.
                
        """
        return self._actual_values

    def _set_actual_values(self, value):
        """ Set actual_values value.

            Notes:
                This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute

                
                This attribute is named `actualValues` in VSD API.
                
        """
        self._actual_values = value

    actual_values = property(_get_actual_values, _set_actual_values)
    
    def _get_length(self):
        """ Get length value.

            Notes:
                DHCP option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')

                
        """
        return self._length

    def _set_length(self, value):
        """ Set length value.

            Notes:
                DHCP option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')

                
        """
        self._length = value

    length = property(_get_length, _set_length)
    
    def _get_type(self):
        """ Get type value.

            Notes:
                DHCP option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')

                
        """
        return self._type

    def _set_type(self, value):
        """ Set type value.

            Notes:
                DHCP option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')

                
        """
        self._type = value

    type = property(_get_type, _set_type)
    
    def _get_value(self):
        """ Get value value.

            Notes:
                DHCP option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')

                
        """
        return self._value

    def _set_value(self, value):
        """ Set value value.

            Notes:
                DHCP option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')

                
        """
        self._value = value

    value = property(_get_value, _set_value)
    