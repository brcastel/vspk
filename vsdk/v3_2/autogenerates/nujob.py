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


class NUJob(NURESTObject):
    """ Represents a Job in the VSD

        Notes:
            Represents JOB entity. The job API accepts a command and parameters and executes the job and returns the results. Jobs API are typically used for long running tasks.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NUJob instead.
    """

    __rest_name__ = u"job"

    def __init__(self, **kwargs):
        """ Initializes a Job instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> job = NUJob(id=u'xxxx-xxx-xxx-xxx', name=u'Job')
                >>> job = NUJob(data=my_dict)
        """

        super(NUJob, self).__init__()

        # Read/Write Attributes
        
        self._assoc_entity_type = None
        self._command = None
        self._parameters = None
        self._progress = None
        self._result = None
        self._status = None
        
        self.expose_attribute(local_name=u"assoc_entity_type", remote_name=u"assocEntityType", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"command", remote_name=u"command", attribute_type=str, is_required=True, is_unique=False, choices=[u'APPLY_POLICY_CHANGES', u'BATCH_CRUD_REQUEST', u'BEGIN_POLICY_CHANGES', u'CERTIFICATE_NSG_RENEW', u'CERTIFICATE_NSG_REVOKE', u'DISCARD_POLICY_CHANGES', u'EXPORT', u'FORCE_KEYSERVER_UPDATE', u'FORCE_KEYSERVER_UPDATE_ACK', u'FORCE_KEYSERVER_VSD_RESYNC', u'GATEWAY_AUDIT', u'IMPORT', u'KEYSERVER_NOTIFICATION_TEST', u'NOTIFY_NSG_REGISTRATION', u'NOTIFY_NSG_REGISTRATION_ACK', u'NOTIFY_NSG_REGISTRATION_TEST', u'NSG_NOTIFICATION_TEST', u'RELOAD', u'RELOAD_GEO_REDUNDANT_INFO', u'RELOAD_NSG_CONFIG', u'VCENTER_RELOAD'])
        self.expose_attribute(local_name=u"parameters", remote_name=u"parameters", attribute_type=object, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"progress", remote_name=u"progress", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"result", remote_name=u"result", attribute_type=object, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILED', u'RUNNING', u'SUCCESS'])
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_assoc_entity_type(self):
        """ Get assoc_entity_type value.

            Notes:
                Entity with which this job is associated Refer to API section for supported types.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        return self._assoc_entity_type

    def _set_assoc_entity_type(self, value):
        """ Set assoc_entity_type value.

            Notes:
                Entity with which this job is associated Refer to API section for supported types.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        self._assoc_entity_type = value

    assoc_entity_type = property(_get_assoc_entity_type, _set_assoc_entity_type)
    
    def _get_command(self):
        """ Get command value.

            Notes:
                Name of the command. Possible values are GATEWAY_AUDIT, NOTIFY_NSG_REGISTRATION, NOTIFY_NSG_REGISTRATION_ACK, CERTIFICATE_NSG_REVOKE, CERTIFICATE_NSG_RENEW, RELOAD_NSG_CONFIG, RELOAD, EXPORT, IMPORT, BEGIN_POLICY_CHANGES, DISCARD_POLICY_CHANGES, APPLY_POLICY_CHANGES, RELOAD_GEO_REDUNDANT_INFO, FORCE_KEYSERVER_UPDATE, FORCE_KEYSERVER_UPDATE_ACK, FORCE_KEYSERVER_VSD_RESYNC, NSG_NOTIFICATION_TEST, KEYSERVER_NOTIFICATION_TEST, NOTIFY_NSG_REGISTRATION_TEST, BATCH_CRUD_REQUEST, VCENTER_RELOAD, .

                
        """
        return self._command

    def _set_command(self, value):
        """ Set command value.

            Notes:
                Name of the command. Possible values are GATEWAY_AUDIT, NOTIFY_NSG_REGISTRATION, NOTIFY_NSG_REGISTRATION_ACK, CERTIFICATE_NSG_REVOKE, CERTIFICATE_NSG_RENEW, RELOAD_NSG_CONFIG, RELOAD, EXPORT, IMPORT, BEGIN_POLICY_CHANGES, DISCARD_POLICY_CHANGES, APPLY_POLICY_CHANGES, RELOAD_GEO_REDUNDANT_INFO, FORCE_KEYSERVER_UPDATE, FORCE_KEYSERVER_UPDATE_ACK, FORCE_KEYSERVER_VSD_RESYNC, NSG_NOTIFICATION_TEST, KEYSERVER_NOTIFICATION_TEST, NOTIFY_NSG_REGISTRATION_TEST, BATCH_CRUD_REQUEST, VCENTER_RELOAD, .

                
        """
        self._command = value

    command = property(_get_command, _set_command)
    
    def _get_parameters(self):
        """ Get parameters value.

            Notes:
                Additional arguments required for the specific command. Differs based on types of command.

                
        """
        return self._parameters

    def _set_parameters(self, value):
        """ Set parameters value.

            Notes:
                Additional arguments required for the specific command. Differs based on types of command.

                
        """
        self._parameters = value

    parameters = property(_get_parameters, _set_parameters)
    
    def _get_progress(self):
        """ Get progress value.

            Notes:
                Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

                
        """
        return self._progress

    def _set_progress(self, value):
        """ Set progress value.

            Notes:
                Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

                
        """
        self._progress = value

    progress = property(_get_progress, _set_progress)
    
    def _get_result(self):
        """ Get result value.

            Notes:
                Results from the execution of the job

                
        """
        return self._result

    def _set_result(self, value):
        """ Set result value.

            Notes:
                Results from the execution of the job

                
        """
        self._result = value

    result = property(_get_result, _set_result)
    
    def _get_status(self):
        """ Get status value.

            Notes:
                Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

                
        """
        return self._status

    def _set_status(self, value):
        """ Set status value.

            Notes:
                Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

                
        """
        self._status = value

    status = property(_get_status, _set_status)
    