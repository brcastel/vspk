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


class NUKeyServerMonitorEncryptedSeed(NURESTObject):
    """ Represents a KeyServerMonitorEncryptedSeed in the VSD

        Notes:
            Represents a Keyserver Monitor Encrypted Seed Snapshot

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUKeyServerMonitorEncryptedSeed instead.
    """

    __rest_name__ = u"keyservermonitorencryptedseed"

    def __init__(self, **kwargs):
        """ Initializes a KeyServerMonitorEncryptedSeed instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> keyservermonitorencryptedseed = NUKeyServerMonitorEncryptedSeed(id=u'xxxx-xxx-xxx-xxx', name=u'KeyServerMonitorEncryptedSeed')
                >>> keyservermonitorencryptedseed = NUKeyServerMonitorEncryptedSeed(data=my_dict)
        """

        super(NUKeyServerMonitorEncryptedSeed, self).__init__()

        # Read/Write Attributes
        
        self._associated_key_server_monitor_seed_creation_time = None
        self._associated_key_server_monitor_seed_id = None
        self._associated_key_server_monitor_sek_creation_time = None
        self._associated_key_server_monitor_sekid = None
        self._enterprise_secured_data_id = None
        self._key_server_certificate_serial_number = None
        self._sek_creation_time = None
        
        self.expose_attribute(local_name=u"associated_key_server_monitor_seed_creation_time", remote_name=u"associatedKeyServerMonitorSeedCreationTime", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_key_server_monitor_seed_id", remote_name=u"associatedKeyServerMonitorSeedID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_key_server_monitor_sek_creation_time", remote_name=u"associatedKeyServerMonitorSEKCreationTime", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_key_server_monitor_sekid", remote_name=u"associatedKeyServerMonitorSEKID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"enterprise_secured_data_id", remote_name=u"enterpriseSecuredDataID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"key_server_certificate_serial_number", remote_name=u"keyServerCertificateSerialNumber", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"sek_creation_time", remote_name=u"SEKCreationTime", attribute_type=long, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_associated_key_server_monitor_seed_creation_time(self):
        """ Get associated_key_server_monitor_seed_creation_time value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedCreationTime` in VSD API.
                
        """
        return self._associated_key_server_monitor_seed_creation_time

    def _set_associated_key_server_monitor_seed_creation_time(self, value):
        """ Set associated_key_server_monitor_seed_creation_time value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedCreationTime` in VSD API.
                
        """
        self._associated_key_server_monitor_seed_creation_time = value

    associated_key_server_monitor_seed_creation_time = property(_get_associated_key_server_monitor_seed_creation_time, _set_associated_key_server_monitor_seed_creation_time)
    
    def _get_associated_key_server_monitor_seed_id(self):
        """ Get associated_key_server_monitor_seed_id value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedID` in VSD API.
                
        """
        return self._associated_key_server_monitor_seed_id

    def _set_associated_key_server_monitor_seed_id(self, value):
        """ Set associated_key_server_monitor_seed_id value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSeedID` in VSD API.
                
        """
        self._associated_key_server_monitor_seed_id = value

    associated_key_server_monitor_seed_id = property(_get_associated_key_server_monitor_seed_id, _set_associated_key_server_monitor_seed_id)
    
    def _get_associated_key_server_monitor_sek_creation_time(self):
        """ Get associated_key_server_monitor_sek_creation_time value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSEKCreationTime` in VSD API.
                
        """
        return self._associated_key_server_monitor_sek_creation_time

    def _set_associated_key_server_monitor_sek_creation_time(self, value):
        """ Set associated_key_server_monitor_sek_creation_time value.

            Notes:
                The ID of the associated KeyServer Monitor Seed ID

                
                This attribute is named `associatedKeyServerMonitorSEKCreationTime` in VSD API.
                
        """
        self._associated_key_server_monitor_sek_creation_time = value

    associated_key_server_monitor_sek_creation_time = property(_get_associated_key_server_monitor_sek_creation_time, _set_associated_key_server_monitor_sek_creation_time)
    
    def _get_associated_key_server_monitor_sekid(self):
        """ Get associated_key_server_monitor_sekid value.

            Notes:
                The ID of the associated KeyServer Monitor SEK ID

                
                This attribute is named `associatedKeyServerMonitorSEKID` in VSD API.
                
        """
        return self._associated_key_server_monitor_sekid

    def _set_associated_key_server_monitor_sekid(self, value):
        """ Set associated_key_server_monitor_sekid value.

            Notes:
                The ID of the associated KeyServer Monitor SEK ID

                
                This attribute is named `associatedKeyServerMonitorSEKID` in VSD API.
                
        """
        self._associated_key_server_monitor_sekid = value

    associated_key_server_monitor_sekid = property(_get_associated_key_server_monitor_sekid, _set_associated_key_server_monitor_sekid)
    
    def _get_enterprise_secured_data_id(self):
        """ Get enterprise_secured_data_id value.

            Notes:
                Enterprise Secured ID record this monitor represents

                
                This attribute is named `enterpriseSecuredDataID` in VSD API.
                
        """
        return self._enterprise_secured_data_id

    def _set_enterprise_secured_data_id(self, value):
        """ Set enterprise_secured_data_id value.

            Notes:
                Enterprise Secured ID record this monitor represents

                
                This attribute is named `enterpriseSecuredDataID` in VSD API.
                
        """
        self._enterprise_secured_data_id = value

    enterprise_secured_data_id = property(_get_enterprise_secured_data_id, _set_enterprise_secured_data_id)
    
    def _get_key_server_certificate_serial_number(self):
        """ Get key_server_certificate_serial_number value.

            Notes:
                KeyServer Certificate Serial Number

                
                This attribute is named `keyServerCertificateSerialNumber` in VSD API.
                
        """
        return self._key_server_certificate_serial_number

    def _set_key_server_certificate_serial_number(self, value):
        """ Set key_server_certificate_serial_number value.

            Notes:
                KeyServer Certificate Serial Number

                
                This attribute is named `keyServerCertificateSerialNumber` in VSD API.
                
        """
        self._key_server_certificate_serial_number = value

    key_server_certificate_serial_number = property(_get_key_server_certificate_serial_number, _set_key_server_certificate_serial_number)
    
    def _get_sek_creation_time(self):
        """ Get sek_creation_time value.

            Notes:
                SEK Creation Time

                
                This attribute is named `SEKCreationTime` in VSD API.
                
        """
        return self._sek_creation_time

    def _set_sek_creation_time(self, value):
        """ Set sek_creation_time value.

            Notes:
                SEK Creation Time

                
                This attribute is named `SEKCreationTime` in VSD API.
                
        """
        self._sek_creation_time = value

    sek_creation_time = property(_get_sek_creation_time, _set_sek_creation_time)
    