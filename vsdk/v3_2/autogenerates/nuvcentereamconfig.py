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


class NUVCenterEAMConfig(NURESTObject):
    """ Represents a VCenterEAMConfig in the VSD

        Notes:
            The EAM solution configuration

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUVCenterEAMConfig instead.
    """

    __rest_name__ = u"eamconfig"

    def __init__(self, **kwargs):
        """ Initializes a VCenterEAMConfig instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vcentereamconfig = NUVCenterEAMConfig(id=u'xxxx-xxx-xxx-xxx', name=u'VCenterEAMConfig')
                >>> vcentereamconfig = NUVCenterEAMConfig(data=my_dict)
        """

        super(NUVCenterEAMConfig, self).__init__()

        # Read/Write Attributes
        
        self._eam_server_ip = None
        self._eam_server_port_number = None
        self._eam_server_port_type = None
        self._extension_key = None
        self._ovf_url = None
        self._vib_url = None
        
        self.expose_attribute(local_name=u"eam_server_ip", remote_name=u"eamServerIP", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"eam_server_port_number", remote_name=u"eamServerPortNumber", attribute_type=int, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"eam_server_port_type", remote_name=u"eamServerPortType", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"extension_key", remote_name=u"extensionKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"ovf_url", remote_name=u"ovfURL", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"vib_url", remote_name=u"vibURL", attribute_type=str, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_eam_server_ip(self):
        """ Get eam_server_ip value.

            Notes:
                The EAM server IP

                
                This attribute is named `eamServerIP` in VSD API.
                
        """
        return self._eam_server_ip

    def _set_eam_server_ip(self, value):
        """ Set eam_server_ip value.

            Notes:
                The EAM server IP

                
                This attribute is named `eamServerIP` in VSD API.
                
        """
        self._eam_server_ip = value

    eam_server_ip = property(_get_eam_server_ip, _set_eam_server_ip)
    
    def _get_eam_server_port_number(self):
        """ Get eam_server_port_number value.

            Notes:
                The EAM server port number

                
                This attribute is named `eamServerPortNumber` in VSD API.
                
        """
        return self._eam_server_port_number

    def _set_eam_server_port_number(self, value):
        """ Set eam_server_port_number value.

            Notes:
                The EAM server port number

                
                This attribute is named `eamServerPortNumber` in VSD API.
                
        """
        self._eam_server_port_number = value

    eam_server_port_number = property(_get_eam_server_port_number, _set_eam_server_port_number)
    
    def _get_eam_server_port_type(self):
        """ Get eam_server_port_type value.

            Notes:
                The EAM server port Type

                
                This attribute is named `eamServerPortType` in VSD API.
                
        """
        return self._eam_server_port_type

    def _set_eam_server_port_type(self, value):
        """ Set eam_server_port_type value.

            Notes:
                The EAM server port Type

                
                This attribute is named `eamServerPortType` in VSD API.
                
        """
        self._eam_server_port_type = value

    eam_server_port_type = property(_get_eam_server_port_type, _set_eam_server_port_type)
    
    def _get_extension_key(self):
        """ Get extension_key value.

            Notes:
                Key of the extension that the solution registers

                
                This attribute is named `extensionKey` in VSD API.
                
        """
        return self._extension_key

    def _set_extension_key(self, value):
        """ Set extension_key value.

            Notes:
                Key of the extension that the solution registers

                
                This attribute is named `extensionKey` in VSD API.
                
        """
        self._extension_key = value

    extension_key = property(_get_extension_key, _set_extension_key)
    
    def _get_ovf_url(self):
        """ Get ovf_url value.

            Notes:
                The url for the ovf

                
                This attribute is named `ovfURL` in VSD API.
                
        """
        return self._ovf_url

    def _set_ovf_url(self, value):
        """ Set ovf_url value.

            Notes:
                The url for the ovf

                
                This attribute is named `ovfURL` in VSD API.
                
        """
        self._ovf_url = value

    ovf_url = property(_get_ovf_url, _set_ovf_url)
    
    def _get_vib_url(self):
        """ Get vib_url value.

            Notes:
                The url for the optional vib

                
                This attribute is named `vibURL` in VSD API.
                
        """
        return self._vib_url

    def _set_vib_url(self, value):
        """ Set vib_url value.

            Notes:
                The url for the optional vib

                
                This attribute is named `vibURL` in VSD API.
                
        """
        self._vib_url = value

    vib_url = property(_get_vib_url, _set_vib_url)
    