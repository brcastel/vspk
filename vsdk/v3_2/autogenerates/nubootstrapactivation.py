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


class NUBootstrapActivation(NURESTObject):
    """ Represents a BootstrapActivation in the VSD

        Notes:
            NSG Gateway initiated Bootstrap Activation

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUBootstrapActivation instead.
    """

    __rest_name__ = u"bootstrapactivation"

    def __init__(self, **kwargs):
        """ Initializes a BootstrapActivation instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> bootstrapactivation = NUBootstrapActivation(id=u'xxxx-xxx-xxx-xxx', name=u'BootstrapActivation')
                >>> bootstrapactivation = NUBootstrapActivation(data=my_dict)
        """

        super(NUBootstrapActivation, self).__init__()

        # Read/Write Attributes
        
        self._action = None
        self._cacert = None
        self._cert = None
        self._config_url = None
        self._csr = None
        self._hash = None
        self._seed = None
        self._status = None
        
        self.expose_attribute(local_name=u"action", remote_name=u"action", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"cacert", remote_name=u"cacert", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"cert", remote_name=u"cert", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"config_url", remote_name=u"configURL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"csr", remote_name=u"csr", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"hash", remote_name=u"hash", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"seed", remote_name=u"seed", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_action(self):
        """ Get action value.

            Notes:
                The bootstrap action to perform

                
        """
        return self._action

    def _set_action(self, value):
        """ Set action value.

            Notes:
                The bootstrap action to perform

                
        """
        self._action = value

    action = property(_get_action, _set_action)
    
    def _get_cacert(self):
        """ Get cacert value.

            Notes:
                The CA Certificate Chain

                
        """
        return self._cacert

    def _set_cacert(self, value):
        """ Set cacert value.

            Notes:
                The CA Certificate Chain

                
        """
        self._cacert = value

    cacert = property(_get_cacert, _set_cacert)
    
    def _get_cert(self):
        """ Get cert value.

            Notes:
                The signed Certificate

                
        """
        return self._cert

    def _set_cert(self, value):
        """ Set cert value.

            Notes:
                The signed Certificate

                
        """
        self._cert = value

    cert = property(_get_cert, _set_cert)
    
    def _get_config_url(self):
        """ Get config_url value.

            Notes:
                The configuration URL

                
                This attribute is named `configURL` in VSD API.
                
        """
        return self._config_url

    def _set_config_url(self, value):
        """ Set config_url value.

            Notes:
                The configuration URL

                
                This attribute is named `configURL` in VSD API.
                
        """
        self._config_url = value

    config_url = property(_get_config_url, _set_config_url)
    
    def _get_csr(self):
        """ Get csr value.

            Notes:
                The CSR of the request

                
        """
        return self._csr

    def _set_csr(self, value):
        """ Set csr value.

            Notes:
                The CSR of the request

                
        """
        self._csr = value

    csr = property(_get_csr, _set_csr)
    
    def _get_hash(self):
        """ Get hash value.

            Notes:
                The authentication hash of this request

                
        """
        return self._hash

    def _set_hash(self, value):
        """ Set hash value.

            Notes:
                The authentication hash of this request

                
        """
        self._hash = value

    hash = property(_get_hash, _set_hash)
    
    def _get_seed(self):
        """ Get seed value.

            Notes:
                The random seed for this request

                
        """
        return self._seed

    def _set_seed(self, value):
        """ Set seed value.

            Notes:
                The random seed for this request

                
        """
        self._seed = value

    seed = property(_get_seed, _set_seed)
    
    def _get_status(self):
        """ Get status value.

            Notes:
                The agent status for the request

                
        """
        return self._status

    def _set_status(self, value):
        """ Set status value.

            Notes:
                The agent status for the request

                
        """
        self._status = value

    status = property(_get_status, _set_status)
    