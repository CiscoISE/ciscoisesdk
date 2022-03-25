# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Backup And Restore API wrapper.

Copyright (c) 2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import *

from past.builtins import basestring

from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class BackupAndRestore(object):
    """Identity Services Engine Backup And Restore API (version: 3.1.1).

    Wraps the Identity Services Engine Backup And Restore
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new BackupAndRestore
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(BackupAndRestore, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def config_backup(self,
                      backup_encryption_key=None,
                      backup_name=None,
                      repository_name=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **query_parameters):
        """Triggers on demand configuration backup on the ISE node. The API
        returns the task ID. Use the Task Service status API to
        get the status of the backup job.

        Args:
            backup_encryption_key(string): The encyption key for the
                backed up file. Encryption key must
                satisfy the following criteria Contains
                at least one uppercase letter [A-Z],
                Contains at least one lowercase letter
                [a-z], Contains at least one digit
                [0-9], Contain only [A-Z][a-z][0-9]_#,
                Has at least 8 characters, Has not more
                than 15 characters, Must not contain
                'CcIiSsCco', Must not begin with,
                property of the request body.
            backup_name(string): The backup file will get saved with
                this name., property of the request
                body.
            repository_name(string): Name of the configured
                repository where the generated backup
                file will get copied., property of the
                request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'backupEncryptionKey':
                    backup_encryption_key,
                'backupName':
                    backup_name,
                'repositoryName':
                    repository_name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_db1d9dda53369e35d33138b29c16_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/backup-restore/config/backup')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_db1d9dda53369e35d33138b29c16_v3_1_1', _api_response)

    def config(self,
               backup_encryption_key=None,
               backup_name=None,
               repository_name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `config_backup <#ciscoisesdk.
        api.v3_1_1.backup_and_restore.
        BackupAndRestore.config_backup>`_
        """
        return self.config_backup(
            backup_encryption_key=backup_encryption_key,
            backup_name=backup_name,
            repository_name=repository_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def cancel_backup(self,
                      headers=None,
                      **query_parameters):
        """Cancels the backup job running on the node.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/backup-restore/config/cancel-backup')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e155669bc74586e9ef2580ec5752902_v3_1_1', _api_response)

    def cancel(self,
               headers=None,
               **query_parameters):
        """Alias for `cancel_backup <#ciscoisesdk.
        api.v3_1_1.backup_and_restore.
        BackupAndRestore.cancel_backup>`_
        """
        return self.cancel_backup(
            headers=headers,
            **query_parameters
        )

    def get_last_config_backup_status(self,
                                      headers=None,
                                      **query_parameters):
        """Gives the last backup status.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/backup-restore/config/last-backup-status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d388e26255a15233ac682c0406880cfb_v3_1_1', _api_response)

    def get_last_status(self,
                        headers=None,
                        **query_parameters):
        """Alias for `get_last_config_backup_status <#ciscoisesdk.
        api.v3_1_1.backup_and_restore.
        BackupAndRestore.get_last_config_backup_status>`_
        """
        return self.get_last_config_backup_status(
            headers=headers,
            **query_parameters
        )

    def restore_config_backup(self,
                              backup_encryption_key=None,
                              repository_name=None,
                              restore_file=None,
                              restore_include_adeos=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Triggers a configuration DB restore job on the ISE node. The API
        returns the task ID. Use the Task Service status API to
        get the status of the backup job.

        Args:
            backup_encryption_key(string): The encryption key which
                was provided at the time of taking
                backup., property of the request body.
            repository_name(string): Name of the configred
                repository where the backup file
                exists., property of the request body.
            restore_file(string): Name of the backup file to be
                restored on ISE node., property of the
                request body.
            restore_include_adeos(string): Determines whether the
                ADE-OS configure is restored. Possible
                values true, false, property of the
                request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'backupEncryptionKey':
                    backup_encryption_key,
                'repositoryName':
                    repository_name,
                'restoreFile':
                    restore_file,
                'restoreIncludeAdeos':
                    restore_include_adeos,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b8319a8b5d195348a8763acd95ca2967_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/backup-restore/config/restore')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b8319a8b5d195348a8763acd95ca2967_v3_1_1', _api_response)

    def restore(self,
                backup_encryption_key=None,
                repository_name=None,
                restore_file=None,
                restore_include_adeos=None,
                headers=None,
                payload=None,
                active_validation=True,
                **query_parameters):
        """Alias for `restore_config_backup <#ciscoisesdk.
        api.v3_1_1.backup_and_restore.
        BackupAndRestore.restore_config_backup>`_
        """
        return self.restore_config_backup(
            backup_encryption_key=backup_encryption_key,
            repository_name=repository_name,
            restore_file=restore_file,
            restore_include_adeos=restore_include_adeos,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def update_scheduled_config_backup(self,
                                       backup_description=None,
                                       backup_encryption_key=None,
                                       backup_name=None,
                                       end_date=None,
                                       frequency=None,
                                       month_day=None,
                                       repository_name=None,
                                       start_date=None,
                                       status=None,
                                       time=None,
                                       week_day=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """Update the Schedule of the configuration backup on the ISE node
        as per the input parameters. This API only helps in
        editing the schedule.

        Args:
            backup_description(string): Description of the backup.,
                property of the request body.
            backup_encryption_key(string): The encyption key for the
                backed up file. Encryption key must
                satisfy the following criteria Contains
                at least one uppercase letter [A-Z],
                Contains at least one lowercase letter
                [a-z], Contains at least one digit
                [0-9], Contain only [A-Z][a-z][0-9]_#,
                Has at least 8 characters, Has not more
                than 15 characters, Must not contain
                'CcIiSsCco', Must not begin with,
                property of the request body.
            backup_name(string): The backup file will get saved with
                this name., property of the request
                body.
            end_date(string): End date of the scheduled backup job.
                Allowed format MM/DD/YYYY. End date is
                not required in case of ONE_TIME
                frequency., property of the request
                body.
            frequency(string): frequency, property of the request
                body. Available values are 'DAILY',
                'MONTHLY', 'ONCE' and 'WEEKLY'.
            month_day(string): Day of month you want backup to be
                performed on when scheduled frequency is
                MONTHLY. Allowed values from 1 to 28.,
                property of the request body.
            repository_name(string): Name of the configured
                repository where the generated backup
                file will get copied., property of the
                request body.
            start_date(string): Start date for scheduling the backup
                job. Allowed format MM/DD/YYYY.,
                property of the request body.
            status(string): status, property of the request body.
                Available values are 'DISABLE' and
                'ENABLE'.
            time(string): Time at which backup job get scheduled.
                example12:00 AM, property of the request
                body.
            week_day(string): weekDay, property of the request body.
                Available values are 'FRI', 'MON',
                'SAT', 'SUN', 'THU', 'TUE' and 'WED'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'backupDescription':
                    backup_description,
                'backupEncryptionKey':
                    backup_encryption_key,
                'backupName':
                    backup_name,
                'endDate':
                    end_date,
                'frequency':
                    frequency,
                'monthDay':
                    month_day,
                'repositoryName':
                    repository_name,
                'startDate':
                    start_date,
                'status':
                    status,
                'time':
                    time,
                'weekDay':
                    week_day,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fc7103b05336a7960d9f34033eca_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/backup-restore/config/schedule-config-backup')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_fc7103b05336a7960d9f34033eca_v3_1_1', _api_response)

    def update(self,
               backup_description=None,
               backup_encryption_key=None,
               backup_name=None,
               end_date=None,
               frequency=None,
               month_day=None,
               repository_name=None,
               start_date=None,
               status=None,
               time=None,
               week_day=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `update_scheduled_config_backup <#ciscoisesdk.
        api.v3_1_1.backup_and_restore.
        BackupAndRestore.update_scheduled_config_backup>`_
        """
        return self.update_scheduled_config_backup(
            backup_description=backup_description,
            backup_encryption_key=backup_encryption_key,
            backup_name=backup_name,
            end_date=end_date,
            frequency=frequency,
            month_day=month_day,
            repository_name=repository_name,
            start_date=start_date,
            status=status,
            time=time,
            week_day=week_day,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def create_scheduled_config_backup(self,
                                       backup_description=None,
                                       backup_encryption_key=None,
                                       backup_name=None,
                                       end_date=None,
                                       frequency=None,
                                       month_day=None,
                                       repository_name=None,
                                       start_date=None,
                                       status=None,
                                       time=None,
                                       week_day=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """Schedules the configuration backup on the ISE node as per the
        input parameters. This API helps in creating the
        schedule for the first time.

        Args:
            backup_description(string): Description of the backup.,
                property of the request body.
            backup_encryption_key(string): The encyption key for the
                backed up file. Encryption key must
                satisfy the following criteria Contains
                at least one uppercase letter [A-Z],
                Contains at least one lowercase letter
                [a-z], Contains at least one digit
                [0-9], Contain only [A-Z][a-z][0-9]_#,
                Has at least 8 characters, Has not more
                than 15 characters, Must not contain
                'CcIiSsCco', Must not begin with,
                property of the request body.
            backup_name(string): The backup file will get saved with
                this name., property of the request
                body.
            end_date(string): End date of the scheduled backup job.
                Allowed format MM/DD/YYYY. End date is
                not required in case of ONE_TIME
                frequency., property of the request
                body.
            frequency(string): frequency, property of the request
                body. Available values are 'DAILY',
                'MONTHLY', 'ONCE' and 'WEEKLY'.
            month_day(string): Day of month you want backup to be
                performed on when scheduled frequency is
                MONTHLY. Allowed values from 1 to 28.,
                property of the request body.
            repository_name(string): Name of the configured
                repository where the generated backup
                file will get copied., property of the
                request body.
            start_date(string): Start date for scheduling the backup
                job. Allowed format MM/DD/YYYY.,
                property of the request body.
            status(string): status, property of the request body.
                Available values are 'DISABLE' and
                'ENABLE'.
            time(string): Time at which backup job get scheduled.
                example12:00 AM, property of the request
                body.
            week_day(string): weekDay, property of the request body.
                Available values are 'FRI', 'MON',
                'SAT', 'SUN', 'THU', 'TUE' and 'WED'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'backupDescription':
                    backup_description,
                'backupEncryptionKey':
                    backup_encryption_key,
                'backupName':
                    backup_name,
                'endDate':
                    end_date,
                'frequency':
                    frequency,
                'monthDay':
                    month_day,
                'repositoryName':
                    repository_name,
                'startDate':
                    start_date,
                'status':
                    status,
                'time':
                    time,
                'weekDay':
                    week_day,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b994e6c8b8d53f29230686824c9fafa_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/backup-restore/config/schedule-config-backup')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b994e6c8b8d53f29230686824c9fafa_v3_1_1', _api_response)

    def create(self,
               backup_description=None,
               backup_encryption_key=None,
               backup_name=None,
               end_date=None,
               frequency=None,
               month_day=None,
               repository_name=None,
               start_date=None,
               status=None,
               time=None,
               week_day=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_scheduled_config_backup <#ciscoisesdk.
        api.v3_1_1.backup_and_restore.
        BackupAndRestore.create_scheduled_config_backup>`_
        """
        return self.create_scheduled_config_backup(
            backup_description=backup_description,
            backup_encryption_key=backup_encryption_key,
            backup_name=backup_name,
            end_date=end_date,
            frequency=frequency,
            month_day=month_day,
            repository_name=repository_name,
            start_date=start_date,
            status=status,
            time=time,
            week_day=week_day,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )
