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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)
import urllib.parse


class BackupAndRestore(object):
    """Identity Services Engine Backup And Restore API (version: 3.0.0).

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
        """Take the config DB backup now by providing the name of the
        backup,repository name and encryption key.

        Args:
            backup_encryption_key(string): The encyption key for the
                backed up file. Encryption key must
                satisfy the following criteria -
                Contains at least one uppercase letter
                [A-Z], Contains at least one lowercase
                letter [a-z], Contains at least one
                digit [0-9], Contain only
                [A-Z][a-z][0-9]_#, Has at least 8
                characters, Has not more than 15
                characters, Must not contain
                'CcIiSsCco', Must not begin with,
                property of the request body.
            backup_name(string): The backup file will get saved with
                this name., property of the request
                body.
            repository_name(string): Name of the repository where
                the generated backup file will get
                copied., property of the request body.
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
            pass

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
                'backupName':
                    backup_name,
                'repositoryName':
                    repository_name,
                'backupEncryptionKey':
                    backup_encryption_key,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_db1d9dda53369e35d33138b29c16_v3_0_0')\
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

        return self._object_factory('bpm_db1d9dda53369e35d33138b29c16_v3_0_0', _api_response)

    def restore_config_backup(self,
                              backup_encryption_key=None,
                              repository_name=None,
                              restore_file=None,
                              restore_include_adeos=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Restore a config DB backup by giving the name of the backup
        file, repository name and encryption key.

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
                ADE-OS configure is restored., property
                of the request body.
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
            pass

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
                'restoreFile':
                    restore_file,
                'repositoryName':
                    repository_name,
                'backupEncryptionKey':
                    backup_encryption_key,
                'restoreIncludeAdeos':
                    restore_include_adeos,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b8319a8b5d195348a8763acd95ca2967_v3_0_0')\
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

        return self._object_factory('bpm_b8319a8b5d195348a8763acd95ca2967_v3_0_0', _api_response)

    def cancel_backup(self,
                      headers=None,
                      **query_parameters):
        """Cancel the running backup.

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
            pass

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

        return self._object_factory('bpm_e155669bc74586e9ef2580ec5752902_v3_0_0', _api_response)

    def get_last_config_backup_status(self,
                                      headers=None,
                                      **query_parameters):
        """gives the last backup status.

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
            pass

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

        return self._object_factory('bpm_d388e26255a15233ac682c0406880cfb_v3_0_0', _api_response)

    def schedule_config_backup(self,
                               backup_description=None,
                               backup_encryption_key=None,
                               backup_name=None,
                               end_date=None,
                               frequency=None,
                               repository_name=None,
                               start_date=None,
                               time=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """Schedule the config backup.

        Args:
            backup_description(string): Description of the backup.,
                property of the request body.
            backup_encryption_key(string): The encyption key for the
                backed up file. Encryption key must
                satisfy the following criteria -
                Contains at least one uppercase letter
                [A-Z], Contains at least one lowercase
                letter [a-z], Contains at least one
                digit [0-9], Contain only
                [A-Z][a-z][0-9]_#, Has at least 8
                characters, Has not more than 15
                characters, Must not contain
                'CcIiSsCco', Must not begin with,
                property of the request body.
            backup_name(string): The backup file will get saved with
                this name., property of the request
                body.
            end_date(string): End date of the scheduled backup job.
                Allowed format YYYY-MM-DD. End date is
                not required in case of ONE_TIME
                frequency., property of the request
                body.
            frequency(string): Frequency with which the backup will
                get scheduled in the ISE node. Allowed
                values - ONE_TIME, DAILY, WEEKLY,
                MONTHLY, property of the request body.
                Available values are 'ONE_TIME',
                'DAILY', 'WEEKLY' and 'MONTHLY'.
            repository_name(string): Name of the repository where
                the generated backup file will get
                copied., property of the request body.
            start_date(string): Start date for scheduling the backup
                job. Allowed format YYYY-MM-DD.,
                property of the request body.
            time(string): Time at which backup job get scheduled.
                example- 12:00 AM, property of the
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
            pass

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
                'backupName':
                    backup_name,
                'backupDescription':
                    backup_description,
                'repositoryName':
                    repository_name,
                'backupEncryptionKey':
                    backup_encryption_key,
                'frequency':
                    frequency,
                'startDate':
                    start_date,
                'endDate':
                    end_date,
                'time':
                    time,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b994e6c8b8d53f29230686824c9fafa_v3_0_0')\
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

        return self._object_factory('bpm_b994e6c8b8d53f29230686824c9fafa_v3_0_0', _api_response)
