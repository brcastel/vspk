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
from ..fetchers import NUJobsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NURedirectionTargetTemplate(NURESTObject):
    """ Represents a RedirectionTargetTemplate in the VSD

        Notes:
            Template for a vporttag. Can be created only at the template level and available for all instances.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NURedirectionTargetTemplate instead.
    """

    __rest_name__ = u"redirectiontargettemplate"

    def __init__(self, **kwargs):
        """ Initializes a RedirectionTargetTemplate instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> redirectiontargettemplate = NURedirectionTargetTemplate(id=u'xxxx-xxx-xxx-xxx', name=u'RedirectionTargetTemplate')
                >>> redirectiontargettemplate = NURedirectionTargetTemplate(data=my_dict)
        """

        super(NURedirectionTargetTemplate, self).__init__()

        # Read/Write Attributes
        
        self._description = None
        self._end_point_type = None
        self._name = None
        self._redundancy_enabled = None
        self._trigger_type = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"end_point_type", remote_name=u"endPointType", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"redundancy_enabled", remote_name=u"redundancyEnabled", attribute_type=bool, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"trigger_type", remote_name=u"triggerType", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of this redirection target template

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of this redirection target template

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_end_point_type(self):
        """ Get end_point_type value.

            Notes:
                VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. Possible values are NONE, L3, VIRTUAL_WIRE.

                
                This attribute is named `endPointType` in VSD API.
                
        """
        return self._end_point_type

    def _set_end_point_type(self, value):
        """ Set end_point_type value.

            Notes:
                VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. Possible values are NONE, L3, VIRTUAL_WIRE.

                
                This attribute is named `endPointType` in VSD API.
                
        """
        self._end_point_type = value

    end_point_type = property(_get_end_point_type, _set_end_point_type)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of this redirection target template

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of this redirection target template

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_redundancy_enabled(self):
        """ Get redundancy_enabled value.

            Notes:
                Allow/Disallow redundant appliances and VIP

                
                This attribute is named `redundancyEnabled` in VSD API.
                
        """
        return self._redundancy_enabled

    def _set_redundancy_enabled(self, value):
        """ Set redundancy_enabled value.

            Notes:
                Allow/Disallow redundant appliances and VIP

                
                This attribute is named `redundancyEnabled` in VSD API.
                
        """
        self._redundancy_enabled = value

    redundancy_enabled = property(_get_redundancy_enabled, _set_redundancy_enabled)
    
    def _get_trigger_type(self):
        """ Get trigger_type value.

            Notes:
                Trigger type, could be NONE/GARP - THIS IS READONNLY

                
                This attribute is named `triggerType` in VSD API.
                
        """
        return self._trigger_type

    def _set_trigger_type(self, value):
        """ Set trigger_type value.

            Notes:
                Trigger type, could be NONE/GARP - THIS IS READONNLY

                
                This attribute is named `triggerType` in VSD API.
                
        """
        self._trigger_type = value

    trigger_type = property(_get_trigger_type, _set_trigger_type)
    