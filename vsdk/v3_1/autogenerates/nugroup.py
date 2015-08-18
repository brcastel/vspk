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
from ..fetchers import NUUsersFetcher

from bambou import NURESTObject
from time import time


class NUGroup(NURESTObject):
    """ Represents a Group in the VSD

        Notes:
            Identifies a group within an enterprise

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUGroup instead.
    """

    __rest_name__ = u"group"

    def __init__(self, **kwargs):
        """ Initializes a Group instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> group = NUGroup(id=u'xxxx-xxx-xxx-xxx', name=u'Group')
                >>> group = NUGroup(data=my_dict)
        """

        super(NUGroup, self).__init__()

        # Read/Write Attributes
        
        self._account_restrictions = None
        self._description = None
        self._name = None
        self._private = None
        self._restriction_date = None
        self._role = None
        
        self.expose_attribute(local_name=u"account_restrictions", remote_name=u"accountRestrictions", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"private", remote_name=u"private", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"restriction_date", remote_name=u"restrictionDate", attribute_type=time, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"role", remote_name=u"role", attribute_type=str, is_required=False, is_unique=False, choices=[u'CMS', u'CSPOPERATOR', u'CSPROOT', u'JMS', u'ORGADMIN', u'ORGAPPDESIGNER', u'ORGNETWORKDESIGNER', u'ORGUSER', u'SYSTEM', u'UNKNOWN', u'USER'])
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.users = NUUsersFetcher.fetcher_with_object(parent_object=self)
        
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_account_restrictions(self):
        """ Get account_restrictions value.

            Notes:
                Determines whether group is disabled or not.

                
                This attribute is named `accountRestrictions` in VSD API.
                
        """
        return self._account_restrictions

    def _set_account_restrictions(self, value):
        """ Set account_restrictions value.

            Notes:
                Determines whether group is disabled or not.

                
                This attribute is named `accountRestrictions` in VSD API.
                
        """
        self._account_restrictions = value

    account_restrictions = property(_get_account_restrictions, _set_account_restrictions)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of the group

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of the group

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                A unique name of the group

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                A unique name of the group

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_private(self):
        """ Get private value.

            Notes:
                A private group is visible only by the owner of the group. Public groups are visible by all users in the enterprise

                
        """
        return self._private

    def _set_private(self, value):
        """ Set private value.

            Notes:
                A private group is visible only by the owner of the group. Public groups are visible by all users in the enterprise

                
        """
        self._private = value

    private = property(_get_private, _set_private)
    
    def _get_restriction_date(self):
        """ Get restriction_date value.

            Notes:
                When the group was disabled.

                
                This attribute is named `restrictionDate` in VSD API.
                
        """
        return self._restriction_date

    def _set_restriction_date(self, value):
        """ Set restriction_date value.

            Notes:
                When the group was disabled.

                
                This attribute is named `restrictionDate` in VSD API.
                
        """
        self._restriction_date = value

    restriction_date = property(_get_restriction_date, _set_restriction_date)
    
    def _get_role(self):
        """ Get role value.

            Notes:
                The role associated with this group - CSPROOT, CSPOPERATOR, ORGADMIN, ORGNETWORKDESIGNER, ORGUSER and USER Possible values are SYSTEM, JMS, CSPROOT, CMS, CSPOPERATOR, ORGADMIN, ORGAPPDESIGNER, ORGNETWORKDESIGNER, ORGUSER, USER, UNKNOWN, .

                
        """
        return self._role

    def _set_role(self, value):
        """ Set role value.

            Notes:
                The role associated with this group - CSPROOT, CSPOPERATOR, ORGADMIN, ORGNETWORKDESIGNER, ORGUSER and USER Possible values are SYSTEM, JMS, CSPROOT, CMS, CSPOPERATOR, ORGADMIN, ORGAPPDESIGNER, ORGNETWORKDESIGNER, ORGUSER, USER, UNKNOWN, .

                
        """
        self._role = value

    role = property(_get_role, _set_role)
    