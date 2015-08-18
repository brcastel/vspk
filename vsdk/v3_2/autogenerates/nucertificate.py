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


class NUCertificate(NURESTObject):
    """ Represents a Certificate in the VSD

        Notes:
            This object represents a X509 Certificate Request

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUCertificate instead.
    """

    __rest_name__ = u"certificate"

    def __init__(self, **kwargs):
        """ Initializes a Certificate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> certificate = NUCertificate(id=u'xxxx-xxx-xxx-xxx', name=u'Certificate')
                >>> certificate = NUCertificate(data=my_dict)
        """

        super(NUCertificate, self).__init__()

        # Read/Write Attributes
        
        self._issuer_dn = None
        self._pem_encoded = None
        self._public_key = None
        self._serial_number = None
        self._subject_dn = None
        
        self.expose_attribute(local_name=u"issuer_dn", remote_name=u"issuerDN", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"pem_encoded", remote_name=u"pemEncoded", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"public_key", remote_name=u"publicKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"serial_number", remote_name=u"serialNumber", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"subject_dn", remote_name=u"subjectDN", attribute_type=str, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_issuer_dn(self):
        """ Get issuer_dn value.

            Notes:
                The distinguished name of the authority that issued this certificate.

                
                This attribute is named `issuerDN` in VSD API.
                
        """
        return self._issuer_dn

    def _set_issuer_dn(self, value):
        """ Set issuer_dn value.

            Notes:
                The distinguished name of the authority that issued this certificate.

                
                This attribute is named `issuerDN` in VSD API.
                
        """
        self._issuer_dn = value

    issuer_dn = property(_get_issuer_dn, _set_issuer_dn)
    
    def _get_pem_encoded(self):
        """ Get pem_encoded value.

            Notes:
                The PEM encoded certificate.

                
                This attribute is named `pemEncoded` in VSD API.
                
        """
        return self._pem_encoded

    def _set_pem_encoded(self, value):
        """ Set pem_encoded value.

            Notes:
                The PEM encoded certificate.

                
                This attribute is named `pemEncoded` in VSD API.
                
        """
        self._pem_encoded = value

    pem_encoded = property(_get_pem_encoded, _set_pem_encoded)
    
    def _get_public_key(self):
        """ Get public_key value.

            Notes:
                The public key contained in this certificate.

                
                This attribute is named `publicKey` in VSD API.
                
        """
        return self._public_key

    def _set_public_key(self, value):
        """ Set public_key value.

            Notes:
                The public key contained in this certificate.

                
                This attribute is named `publicKey` in VSD API.
                
        """
        self._public_key = value

    public_key = property(_get_public_key, _set_public_key)
    
    def _get_serial_number(self):
        """ Get serial_number value.

            Notes:
                The serial number of this certificate.

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        return self._serial_number

    def _set_serial_number(self, value):
        """ Set serial_number value.

            Notes:
                The serial number of this certificate.

                
                This attribute is named `serialNumber` in VSD API.
                
        """
        self._serial_number = value

    serial_number = property(_get_serial_number, _set_serial_number)
    
    def _get_subject_dn(self):
        """ Get subject_dn value.

            Notes:
                The distinguished name of this certificate's end entity.

                
                This attribute is named `subjectDN` in VSD API.
                
        """
        return self._subject_dn

    def _set_subject_dn(self, value):
        """ Set subject_dn value.

            Notes:
                The distinguished name of this certificate's end entity.

                
                This attribute is named `subjectDN` in VSD API.
                
        """
        self._subject_dn = value

    subject_dn = property(_get_subject_dn, _set_subject_dn)
    