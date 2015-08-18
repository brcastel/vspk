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


class NUEnterprisePermission(NURESTObject):
    """ Represents a EnterprisePermission in the VSD

        Notes:
            Represents Enterprise Permission for a CSP entity

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUEnterprisePermission instead.
    """

    __rest_name__ = u"enterprisepermission"

    def __init__(self, **kwargs):
        """ Initializes a EnterprisePermission instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> enterprisepermission = NUEnterprisePermission(id=u'xxxx-xxx-xxx-xxx', name=u'EnterprisePermission')
                >>> enterprisepermission = NUEnterprisePermission(data=my_dict)
        """

        super(NUEnterprisePermission, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._permitted_action = None
        self._permitted_entity_description = None
        self._permitted_entity_id = None
        self._permitted_entity_name = None
        self._permitted_entity_type = None
        
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str, is_required=True, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name=u"permitted_entity_description", remote_name=u"permittedEntityDescription", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"permitted_entity_id", remote_name=u"permittedEntityID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"permitted_entity_name", remote_name=u"permittedEntityName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"permitted_entity_type", remote_name=u"permittedEntityType", attribute_type=str, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the  Permission

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the  Permission

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    def _set_permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    permitted_action = property(_get_permitted_action, _set_permitted_action)
    
    def _get_permitted_entity_description(self):
        """ Get permitted_entity_description value.

            Notes:
                Description for the permittedEntity

                
                This attribute is named `permittedEntityDescription` in VSD API.
                
        """
        return self._permitted_entity_description

    def _set_permitted_entity_description(self, value):
        """ Set permitted_entity_description value.

            Notes:
                Description for the permittedEntity

                
                This attribute is named `permittedEntityDescription` in VSD API.
                
        """
        self._permitted_entity_description = value

    permitted_entity_description = property(_get_permitted_entity_description, _set_permitted_entity_description)
    
    def _get_permitted_entity_id(self):
        """ Get permitted_entity_id value.

            Notes:
                The enterprise permitted to use/extend  this Gateway

                
                This attribute is named `permittedEntityID` in VSD API.
                
        """
        return self._permitted_entity_id

    def _set_permitted_entity_id(self, value):
        """ Set permitted_entity_id value.

            Notes:
                The enterprise permitted to use/extend  this Gateway

                
                This attribute is named `permittedEntityID` in VSD API.
                
        """
        self._permitted_entity_id = value

    permitted_entity_id = property(_get_permitted_entity_id, _set_permitted_entity_id)
    
    def _get_permitted_entity_name(self):
        """ Get permitted_entity_name value.

            Notes:
                Name of the entity for which we have given permission.

                
                This attribute is named `permittedEntityName` in VSD API.
                
        """
        return self._permitted_entity_name

    def _set_permitted_entity_name(self, value):
        """ Set permitted_entity_name value.

            Notes:
                Name of the entity for which we have given permission.

                
                This attribute is named `permittedEntityName` in VSD API.
                
        """
        self._permitted_entity_name = value

    permitted_entity_name = property(_get_permitted_entity_name, _set_permitted_entity_name)
    
    def _get_permitted_entity_type(self):
        """ Get permitted_entity_type value.

            Notes:
                Type of the entity for which we have given permission.

                
                This attribute is named `permittedEntityType` in VSD API.
                
        """
        return self._permitted_entity_type

    def _set_permitted_entity_type(self, value):
        """ Set permitted_entity_type value.

            Notes:
                Type of the entity for which we have given permission.

                
                This attribute is named `permittedEntityType` in VSD API.
                
        """
        self._permitted_entity_type = value

    permitted_entity_type = property(_get_permitted_entity_type, _set_permitted_entity_type)
    