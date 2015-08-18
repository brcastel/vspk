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


class NUVPortMirror(NURESTObject):
    """ Represents a VPortMirror in the VSD

        Notes:
            VPort Mirror Object represents the relationship between a vport and a mirror destination.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUVPortMirror instead.
    """

    __rest_name__ = u"vportmirror"

    def __init__(self, **kwargs):
        """ Initializes a VPortMirror instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vportmirror = NUVPortMirror(id=u'xxxx-xxx-xxx-xxx', name=u'VPortMirror')
                >>> vportmirror = NUVPortMirror(data=my_dict)
        """

        super(NUVPortMirror, self).__init__()

        # Read/Write Attributes
        
        self._attached_network_type = None
        self._domain_name = None
        self._enterpise_name = None
        self._mirror_destination_id = None
        self._mirror_destination_name = None
        self._mirror_direction = None
        self._network_name = None
        self._vport_id = None
        self._vport_name = None
        
        self.expose_attribute(local_name=u"attached_network_type", remote_name=u"attachedNetworkType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"enterpise_name", remote_name=u"enterpiseName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"mirror_destination_id", remote_name=u"mirrorDestinationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"mirror_destination_name", remote_name=u"mirrorDestinationName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"mirror_direction", remote_name=u"mirrorDirection", attribute_type=str, is_required=False, is_unique=False, choices=[u'BOTH', u'EGRESS', u'INGRESS'])
        self.expose_attribute(local_name=u"network_name", remote_name=u"networkName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"vport_id", remote_name=u"vportId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"vport_name", remote_name=u"VPortName", attribute_type=str, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_attached_network_type(self):
        """ Get attached_network_type value.

            Notes:
                Type of the network attached - L2/L3

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        return self._attached_network_type

    def _set_attached_network_type(self, value):
        """ Set attached_network_type value.

            Notes:
                Type of the network attached - L2/L3

                
                This attribute is named `attachedNetworkType` in VSD API.
                
        """
        self._attached_network_type = value

    attached_network_type = property(_get_attached_network_type, _set_attached_network_type)
    
    def _get_domain_name(self):
        """ Get domain_name value.

            Notes:
                Domain name of the vport associated with the mirror destination

                
                This attribute is named `domainName` in VSD API.
                
        """
        return self._domain_name

    def _set_domain_name(self, value):
        """ Set domain_name value.

            Notes:
                Domain name of the vport associated with the mirror destination

                
                This attribute is named `domainName` in VSD API.
                
        """
        self._domain_name = value

    domain_name = property(_get_domain_name, _set_domain_name)
    
    def _get_enterpise_name(self):
        """ Get enterpise_name value.

            Notes:
                Enterprise to which the vport associated with the mirror destination belongs to.

                
                This attribute is named `enterpiseName` in VSD API.
                
        """
        return self._enterpise_name

    def _set_enterpise_name(self, value):
        """ Set enterpise_name value.

            Notes:
                Enterprise to which the vport associated with the mirror destination belongs to.

                
                This attribute is named `enterpiseName` in VSD API.
                
        """
        self._enterpise_name = value

    enterpise_name = property(_get_enterpise_name, _set_enterpise_name)
    
    def _get_mirror_destination_id(self):
        """ Get mirror_destination_id value.

            Notes:
                Destination ID of the mirror destination object.

                
                This attribute is named `mirrorDestinationID` in VSD API.
                
        """
        return self._mirror_destination_id

    def _set_mirror_destination_id(self, value):
        """ Set mirror_destination_id value.

            Notes:
                Destination ID of the mirror destination object.

                
                This attribute is named `mirrorDestinationID` in VSD API.
                
        """
        self._mirror_destination_id = value

    mirror_destination_id = property(_get_mirror_destination_id, _set_mirror_destination_id)
    
    def _get_mirror_destination_name(self):
        """ Get mirror_destination_name value.

            Notes:
                Name of the mirror destination

                
                This attribute is named `mirrorDestinationName` in VSD API.
                
        """
        return self._mirror_destination_name

    def _set_mirror_destination_name(self, value):
        """ Set mirror_destination_name value.

            Notes:
                Name of the mirror destination

                
                This attribute is named `mirrorDestinationName` in VSD API.
                
        """
        self._mirror_destination_name = value

    mirror_destination_name = property(_get_mirror_destination_name, _set_mirror_destination_name)
    
    def _get_mirror_direction(self):
        """ Get mirror_direction value.

            Notes:
                Describes what type of traffic needs to be mirrors - ingress/egress/both Possible values are BOTH, INGRESS, EGRESS, .

                
                This attribute is named `mirrorDirection` in VSD API.
                
        """
        return self._mirror_direction

    def _set_mirror_direction(self, value):
        """ Set mirror_direction value.

            Notes:
                Describes what type of traffic needs to be mirrors - ingress/egress/both Possible values are BOTH, INGRESS, EGRESS, .

                
                This attribute is named `mirrorDirection` in VSD API.
                
        """
        self._mirror_direction = value

    mirror_direction = property(_get_mirror_direction, _set_mirror_direction)
    
    def _get_network_name(self):
        """ Get network_name value.

            Notes:
                Name of the network to which the vport belongs to

                
                This attribute is named `networkName` in VSD API.
                
        """
        return self._network_name

    def _set_network_name(self, value):
        """ Set network_name value.

            Notes:
                Name of the network to which the vport belongs to

                
                This attribute is named `networkName` in VSD API.
                
        """
        self._network_name = value

    network_name = property(_get_network_name, _set_network_name)
    
    def _get_vport_id(self):
        """ Get vport_id value.

            Notes:
                Id of the vport to which the mirror destination is associated with.

                
                This attribute is named `vportId` in VSD API.
                
        """
        return self._vport_id

    def _set_vport_id(self, value):
        """ Set vport_id value.

            Notes:
                Id of the vport to which the mirror destination is associated with.

                
                This attribute is named `vportId` in VSD API.
                
        """
        self._vport_id = value

    vport_id = property(_get_vport_id, _set_vport_id)
    
    def _get_vport_name(self):
        """ Get vport_name value.

            Notes:
                Name of the vport to which the mirror destination is associated with.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        return self._vport_name

    def _set_vport_name(self, value):
        """ Set vport_name value.

            Notes:
                Name of the vport to which the mirror destination is associated with.

                
                This attribute is named `VPortName` in VSD API.
                
        """
        self._vport_name = value

    vport_name = property(_get_vport_name, _set_vport_name)
    