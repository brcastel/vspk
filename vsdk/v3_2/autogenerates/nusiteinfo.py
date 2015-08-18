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


class NUSiteInfo(NURESTObject):
    """ Represents a SiteInfo in the VSD

        Notes:
            Remote Site info

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUSiteInfo instead.
    """

    __rest_name__ = u"site"

    def __init__(self, **kwargs):
        """ Initializes a SiteInfo instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> siteinfo = NUSiteInfo(id=u'xxxx-xxx-xxx-xxx', name=u'SiteInfo')
                >>> siteinfo = NUSiteInfo(data=my_dict)
        """

        super(NUSiteInfo, self).__init__()

        # Read/Write Attributes
        
        self._address = None
        self._description = None
        self._name = None
        self._site_identifier = None
        self._xmpp_domain = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"site_identifier", remote_name=u"siteIdentifier", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"xmpp_domain", remote_name=u"xmppDomain", attribute_type=str, is_required=True, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_address(self):
        """ Get address value.

            Notes:
                unique fqdn/address of the remote site

                
        """
        return self._address

    def _set_address(self, value):
        """ Set address value.

            Notes:
                unique fqdn/address of the remote site

                
        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of the Remote Site.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of the Remote Site.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                name of the Remote Site.

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                name of the Remote Site.

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_site_identifier(self):
        """ Get site_identifier value.

            Notes:
                unique identifier of the remote site

                
                This attribute is named `siteIdentifier` in VSD API.
                
        """
        return self._site_identifier

    def _set_site_identifier(self, value):
        """ Set site_identifier value.

            Notes:
                unique identifier of the remote site

                
                This attribute is named `siteIdentifier` in VSD API.
                
        """
        self._site_identifier = value

    site_identifier = property(_get_site_identifier, _set_site_identifier)
    
    def _get_xmpp_domain(self):
        """ Get xmpp_domain value.

            Notes:
                unique xmpp domain name of the remote site

                
                This attribute is named `xmppDomain` in VSD API.
                
        """
        return self._xmpp_domain

    def _set_xmpp_domain(self, value):
        """ Set xmpp_domain value.

            Notes:
                unique xmpp domain name of the remote site

                
                This attribute is named `xmppDomain` in VSD API.
                
        """
        self._xmpp_domain = value

    xmpp_domain = property(_get_xmpp_domain, _set_xmpp_domain)
    