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


from ..fetchers import NUKeyServerMonitorEncryptedSeedsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUKeyServerMonitorSeed(NURESTObject):
    """ Represents a KeyServerMonitorSeed in the VSD

        Notes:
            Represents a Keyserver Monitor Seed Snapshot

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUKeyServerMonitorSeed instead.
    """

    __rest_name__ = u"keyservermonitorseed"

    def __init__(self, **kwargs):
        """ Initializes a KeyServerMonitorSeed instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> keyservermonitorseed = NUKeyServerMonitorSeed(id=u'xxxx-xxx-xxx-xxx', name=u'KeyServerMonitorSeed')
                >>> keyservermonitorseed = NUKeyServerMonitorSeed(data=my_dict)
        """

        super(NUKeyServerMonitorSeed, self).__init__()

        # Read/Write Attributes
        
        self._creation_time = None
        self._lifetime = None
        self._seed_traffic_authentication_algorithm = None
        self._seed_traffic_encryption_algorithm = None
        self._seed_traffic_encryption_key_lifetime = None
        self._start_time = None
        
        self.expose_attribute(local_name=u"creation_time", remote_name=u"creationTime", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"lifetime", remote_name=u"lifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"seed_traffic_authentication_algorithm", remote_name=u"seedTrafficAuthenticationAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'HMAC_MD5', u'HMAC_SHA1', u'HMAC_SHA256', u'HMAC_SHA384', u'HMAC_SHA512'])
        self.expose_attribute(local_name=u"seed_traffic_encryption_algorithm", remote_name=u"seedTrafficEncryptionAlgorithm", attribute_type=str, is_required=False, is_unique=False, choices=[u'AES_128_CBC', u'AES_192_CBC', u'AES_256_CBC', u'TRIPLE_DES_CBC'])
        self.expose_attribute(local_name=u"seed_traffic_encryption_key_lifetime", remote_name=u"seedTrafficEncryptionKeyLifetime", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"start_time", remote_name=u"startTime", attribute_type=long, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.key_server_monitor_encrypted_seeds = NUKeyServerMonitorEncryptedSeedsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_creation_time(self):
        """ Get creation_time value.

            Notes:
                The time this entry was created (milliseconds since epoch)

                
                This attribute is named `creationTime` in VSD API.
                
        """
        return self._creation_time

    def _set_creation_time(self, value):
        """ Set creation_time value.

            Notes:
                The time this entry was created (milliseconds since epoch)

                
                This attribute is named `creationTime` in VSD API.
                
        """
        self._creation_time = value

    creation_time = property(_get_creation_time, _set_creation_time)
    
    def _get_lifetime(self):
        """ Get lifetime value.

            Notes:
                The lifetime of this entry (seconds)

                
        """
        return self._lifetime

    def _set_lifetime(self, value):
        """ Set lifetime value.

            Notes:
                The lifetime of this entry (seconds)

                
        """
        self._lifetime = value

    lifetime = property(_get_lifetime, _set_lifetime)
    
    def _get_seed_traffic_authentication_algorithm(self):
        """ Get seed_traffic_authentication_algorithm value.

            Notes:
                Seed traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .

                
                This attribute is named `seedTrafficAuthenticationAlgorithm` in VSD API.
                
        """
        return self._seed_traffic_authentication_algorithm

    def _set_seed_traffic_authentication_algorithm(self, value):
        """ Set seed_traffic_authentication_algorithm value.

            Notes:
                Seed traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .

                
                This attribute is named `seedTrafficAuthenticationAlgorithm` in VSD API.
                
        """
        self._seed_traffic_authentication_algorithm = value

    seed_traffic_authentication_algorithm = property(_get_seed_traffic_authentication_algorithm, _set_seed_traffic_authentication_algorithm)
    
    def _get_seed_traffic_encryption_algorithm(self):
        """ Get seed_traffic_encryption_algorithm value.

            Notes:
                Seed traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .

                
                This attribute is named `seedTrafficEncryptionAlgorithm` in VSD API.
                
        """
        return self._seed_traffic_encryption_algorithm

    def _set_seed_traffic_encryption_algorithm(self, value):
        """ Set seed_traffic_encryption_algorithm value.

            Notes:
                Seed traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .

                
                This attribute is named `seedTrafficEncryptionAlgorithm` in VSD API.
                
        """
        self._seed_traffic_encryption_algorithm = value

    seed_traffic_encryption_algorithm = property(_get_seed_traffic_encryption_algorithm, _set_seed_traffic_encryption_algorithm)
    
    def _get_seed_traffic_encryption_key_lifetime(self):
        """ Get seed_traffic_encryption_key_lifetime value.

            Notes:
                Seed Traffic Encryption Key Lifetime in Seconds

                
                This attribute is named `seedTrafficEncryptionKeyLifetime` in VSD API.
                
        """
        return self._seed_traffic_encryption_key_lifetime

    def _set_seed_traffic_encryption_key_lifetime(self, value):
        """ Set seed_traffic_encryption_key_lifetime value.

            Notes:
                Seed Traffic Encryption Key Lifetime in Seconds

                
                This attribute is named `seedTrafficEncryptionKeyLifetime` in VSD API.
                
        """
        self._seed_traffic_encryption_key_lifetime = value

    seed_traffic_encryption_key_lifetime = property(_get_seed_traffic_encryption_key_lifetime, _set_seed_traffic_encryption_key_lifetime)
    
    def _get_start_time(self):
        """ Get start_time value.

            Notes:
                The time this entry  was activated (milliseconds since epoch)

                
                This attribute is named `startTime` in VSD API.
                
        """
        return self._start_time

    def _set_start_time(self, value):
        """ Set start_time value.

            Notes:
                The time this entry  was activated (milliseconds since epoch)

                
                This attribute is named `startTime` in VSD API.
                
        """
        self._start_time = value

    start_time = property(_get_start_time, _set_start_time)
    