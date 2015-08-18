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


class NUNATMapEntry(NURESTObject):
    """ Represents a NATMapEntry in the VSD

        Notes:
            Defines a MAP between the private ip and public ip

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUNATMapEntry instead.
    """

    __rest_name__ = u"natmapentry"

    def __init__(self, **kwargs):
        """ Initializes a NATMapEntry instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> natmapentry = NUNATMapEntry(id=u'xxxx-xxx-xxx-xxx', name=u'NATMapEntry')
                >>> natmapentry = NUNATMapEntry(data=my_dict)
        """

        super(NUNATMapEntry, self).__init__()

        # Read/Write Attributes
        
        self._associated_patnat_pool_id = None
        self._private_ip = None
        self._public_ip = None
        
        self.expose_attribute(local_name=u"associated_patnat_pool_id", remote_name=u"associatedPATNATPoolID", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"private_ip", remote_name=u"privateIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"public_ip", remote_name=u"publicIP", attribute_type=str, is_required=True, is_unique=False)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_associated_patnat_pool_id(self):
        """ Get associated_patnat_pool_id value.

            Notes:
                Read Only - Indicates which PATNATPool this entry belongs to

                
                This attribute is named `associatedPATNATPoolID` in VSD API.
                
        """
        return self._associated_patnat_pool_id

    def _set_associated_patnat_pool_id(self, value):
        """ Set associated_patnat_pool_id value.

            Notes:
                Read Only - Indicates which PATNATPool this entry belongs to

                
                This attribute is named `associatedPATNATPoolID` in VSD API.
                
        """
        self._associated_patnat_pool_id = value

    associated_patnat_pool_id = property(_get_associated_patnat_pool_id, _set_associated_patnat_pool_id)
    
    def _get_private_ip(self):
        """ Get private_ip value.

            Notes:
                Private IP address of the interface

                
                This attribute is named `privateIP` in VSD API.
                
        """
        return self._private_ip

    def _set_private_ip(self, value):
        """ Set private_ip value.

            Notes:
                Private IP address of the interface

                
                This attribute is named `privateIP` in VSD API.
                
        """
        self._private_ip = value

    private_ip = property(_get_private_ip, _set_private_ip)
    
    def _get_public_ip(self):
        """ Get public_ip value.

            Notes:
                Public IP address of the interface

                
                This attribute is named `publicIP` in VSD API.
                
        """
        return self._public_ip

    def _set_public_ip(self, value):
        """ Set public_ip value.

            Notes:
                Public IP address of the interface

                
                This attribute is named `publicIP` in VSD API.
                
        """
        self._public_ip = value

    public_ip = property(_get_public_ip, _set_public_ip)
    