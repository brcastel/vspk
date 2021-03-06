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
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUVMsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUUser(NURESTObject):
    """ Represents a User in the VSD

        Notes:
            Object that identifies the user functions

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUUser instead.
    """

    __rest_name__ = u"user"

    def __init__(self, **kwargs):
        """ Initializes a User instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> user = NUUser(id=u'xxxx-xxx-xxx-xxx', name=u'User')
                >>> user = NUUser(data=my_dict)
        """

        super(NUUser, self).__init__()

        # Read/Write Attributes
        
        self._avatar_data = None
        self._avatar_type = None
        self._disabled = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._mobile_number = None
        self._password = None
        self._user_name = None
        
        self.expose_attribute(local_name=u"avatar_data", remote_name=u"avatarData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"avatar_type", remote_name=u"avatarType", attribute_type=str, is_required=False, is_unique=False, choices=[u'BASE64', u'COMPUTEDURL', u'URL'])
        self.expose_attribute(local_name=u"disabled", remote_name=u"disabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"email", remote_name=u"email", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"first_name", remote_name=u"firstName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"last_name", remote_name=u"lastName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"mobile_number", remote_name=u"mobileNumber", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"password", remote_name=u"password", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=str, is_required=True, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.groups = NUGroupsFetcher.fetcher_with_object(parent_object=self)
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_avatar_data(self):
        """ Get avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        return self._avatar_data

    def _set_avatar_data(self, value):
        """ Set avatar_data value.

            Notes:
                URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image

                
                This attribute is named `avatarData` in VSD API.
                
        """
        self._avatar_data = value

    avatar_data = property(_get_avatar_data, _set_avatar_data)
    
    def _get_avatar_type(self):
        """ Get avatar_type value.

            Notes:
                Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .

                
                This attribute is named `avatarType` in VSD API.
                
        """
        return self._avatar_type

    def _set_avatar_type(self, value):
        """ Set avatar_type value.

            Notes:
                Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .

                
                This attribute is named `avatarType` in VSD API.
                
        """
        self._avatar_type = value

    avatar_type = property(_get_avatar_type, _set_avatar_type)
    
    def _get_disabled(self):
        """ Get disabled value.

            Notes:
                Status of the user account; true=disabled, false=not disabled; default value = false

                
        """
        return self._disabled

    def _set_disabled(self, value):
        """ Set disabled value.

            Notes:
                Status of the user account; true=disabled, false=not disabled; default value = false

                
        """
        self._disabled = value

    disabled = property(_get_disabled, _set_disabled)
    
    def _get_email(self):
        """ Get email value.

            Notes:
                Email address of the user

                
        """
        return self._email

    def _set_email(self, value):
        """ Set email value.

            Notes:
                Email address of the user

                
        """
        self._email = value

    email = property(_get_email, _set_email)
    
    def _get_first_name(self):
        """ Get first_name value.

            Notes:
                First name of the user

                
                This attribute is named `firstName` in VSD API.
                
        """
        return self._first_name

    def _set_first_name(self, value):
        """ Set first_name value.

            Notes:
                First name of the user

                
                This attribute is named `firstName` in VSD API.
                
        """
        self._first_name = value

    first_name = property(_get_first_name, _set_first_name)
    
    def _get_last_name(self):
        """ Get last_name value.

            Notes:
                Last name of the user

                
                This attribute is named `lastName` in VSD API.
                
        """
        return self._last_name

    def _set_last_name(self, value):
        """ Set last_name value.

            Notes:
                Last name of the user

                
                This attribute is named `lastName` in VSD API.
                
        """
        self._last_name = value

    last_name = property(_get_last_name, _set_last_name)
    
    def _get_mobile_number(self):
        """ Get mobile_number value.

            Notes:
                Mobile Number of the user

                
                This attribute is named `mobileNumber` in VSD API.
                
        """
        return self._mobile_number

    def _set_mobile_number(self, value):
        """ Set mobile_number value.

            Notes:
                Mobile Number of the user

                
                This attribute is named `mobileNumber` in VSD API.
                
        """
        self._mobile_number = value

    mobile_number = property(_get_mobile_number, _set_mobile_number)
    
    def _get_password(self):
        """ Get password value.

            Notes:
                User password stored as a hash (SHA-1 encrpted)

                
        """
        return self._password

    def _set_password(self, value):
        """ Set password value.

            Notes:
                User password stored as a hash (SHA-1 encrpted)

                
        """
        self._password = value

    password = property(_get_password, _set_password)
    
    def _get_user_name(self):
        """ Get user_name value.

            Notes:
                Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

                
                This attribute is named `userName` in VSD API.
                
        """
        return self._user_name

    def _set_user_name(self, value):
        """ Set user_name value.

            Notes:
                Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).

                
                This attribute is named `userName` in VSD API.
                
        """
        self._user_name = value

    user_name = property(_get_user_name, _set_user_name)
    