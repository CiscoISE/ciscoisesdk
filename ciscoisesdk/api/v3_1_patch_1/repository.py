# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Repository API wrapper.

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


class Repository(object):
    """Identity Services Engine Repository API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine Repository
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Repository
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Repository, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_repositories(self,
                         headers=None,
                         **query_parameters):
        """This will get the full list of repository definitions on the
        system. .

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

        e_url = ('/api/v1/repository')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f9081a48e3c5f4fae5aa00f889216dd_v3_1_patch_1', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_repositories <#ciscoisesdk.
        api.v3_1_patch_1.repository.
        Repository.get_repositories>`_
        """
        return self.get_repositories(
            headers=headers,
            **query_parameters
        )

    def create_repository(self,
                          enable_pki=None,
                          name=None,
                          password=None,
                          path=None,
                          protocol=None,
                          server_name=None,
                          user_name=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """Create a new repository in the system. The name provided for the
        repository must be unique. .

        Args:
            enable_pki(boolean): enablePki, property of the request
                body.
            name(string): Repository name should be less than 80
                characters and can contain alphanumeric,
                underscore, hyphen and dot characters.,
                property of the request body.
            password(string): Password can contain alphanumeric
                and/or special characters., property of
                the request body.
            path(string): Path should always start with "/" and can
                contain alphanumeric, underscore, hyphen
                and dot characters., property of the
                request body.
            protocol(string): protocol, property of the request
                body. Available values are 'CDROM',
                'DISK', 'FTP', 'HTTP', 'HTTPS', 'NFS',
                'SFTP' and 'TFTP'.
            server_name(string): serverName, property of the request
                body.
            user_name(string): Username may contain alphanumeric and
                _-./@\\$ characters., property of the
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
                'name':
                    name,
                'protocol':
                    protocol,
                'path':
                    path,
                'password':
                    password,
                'serverName':
                    server_name,
                'userName':
                    user_name,
                'enablePki':
                    enable_pki,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a207a157244508c99bf3e9abb26aab8_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/repository')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a207a157244508c99bf3e9abb26aab8_v3_1_patch_1', _api_response)

    def create(self,
               enable_pki=None,
               name=None,
               password=None,
               path=None,
               protocol=None,
               server_name=None,
               user_name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_repository <#ciscoisesdk.
        api.v3_1_patch_1.repository.
        Repository.create_repository>`_
        """
        return self.create_repository(
            enable_pki=enable_pki,
            name=name,
            password=password,
            path=path,
            protocol=protocol,
            server_name=server_name,
            user_name=user_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_repository(self,
                       repository_name,
                       headers=None,
                       **query_parameters):
        """Get a specific repository identified by the name passed in the
        URL. .

        Args:
            repository_name(basestring): repositoryName path
                parameter. Unique name for a repository.
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
        check_type(repository_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'repositoryName': repository_name,
        }

        e_url = ('/api/v1/repository/{repositoryName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e4fd4586ad825f69843d9213e956cf81_v3_1_patch_1', _api_response)

    def get_by_name(self,
                    repository_name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_repository <#ciscoisesdk.
        api.v3_1_patch_1.repository.
        Repository.get_repository>`_
        """
        return self.get_repository(
            repository_name=repository_name,
            headers=headers,
            **query_parameters
        )

    def update_repository(self,
                          repository_name,
                          enable_pki=None,
                          name=None,
                          password=None,
                          path=None,
                          protocol=None,
                          server_name=None,
                          user_name=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """Update the definition of a specific repository, providing ALL
        parameters for the repository. .

        Args:
            enable_pki(boolean): enablePki, property of the request
                body.
            name(string): Repository name should be less than 80
                characters and can contain alphanumeric,
                underscore, hyphen and dot characters.,
                property of the request body.
            password(string): Password can contain alphanumeric
                and/or special characters., property of
                the request body.
            path(string): Path should always start with "/" and can
                contain alphanumeric, underscore, hyphen
                and dot characters., property of the
                request body.
            protocol(string): protocol, property of the request
                body. Available values are 'CDROM',
                'DISK', 'FTP', 'HTTP', 'HTTPS', 'NFS',
                'SFTP' and 'TFTP'.
            server_name(string): serverName, property of the request
                body.
            user_name(string): Username may contain alphanumeric and
                _-./@\\$ characters., property of the
                request body.
            repository_name(basestring): repositoryName path
                parameter. Unique name for a repository.
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
        check_type(repository_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'repositoryName': repository_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'name':
                    name,
                'protocol':
                    protocol,
                'path':
                    path,
                'password':
                    password,
                'serverName':
                    server_name,
                'userName':
                    user_name,
                'enablePki':
                    enable_pki,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f757b04825bb5c29a1b3475aae870d04_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/repository/{repositoryName}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f757b04825bb5c29a1b3475aae870d04_v3_1_patch_1', _api_response)

    def update_by_name(self,
                       repository_name,
                       enable_pki=None,
                       name=None,
                       password=None,
                       path=None,
                       protocol=None,
                       server_name=None,
                       user_name=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **query_parameters):
        """Alias for `update_repository <#ciscoisesdk.
        api.v3_1_patch_1.repository.
        Repository.update_repository>`_
        """
        return self.update_repository(
            repository_name=repository_name,
            enable_pki=enable_pki,
            name=name,
            password=password,
            path=path,
            protocol=protocol,
            server_name=server_name,
            user_name=user_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_repository(self,
                          repository_name,
                          headers=None,
                          **query_parameters):
        """Long description TBD .

        Args:
            repository_name(basestring): repositoryName path
                parameter. Unique name for a repository.
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
        check_type(repository_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'repositoryName': repository_name,
        }

        e_url = ('/api/v1/repository/{repositoryName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e3bcabbd0e5e899945592039694139_v3_1_patch_1', _api_response)

    def delete_by_name(self,
                       repository_name,
                       headers=None,
                       **query_parameters):
        """Alias for `delete_repository <#ciscoisesdk.
        api.v3_1_patch_1.repository.
        Repository.delete_repository>`_
        """
        return self.delete_repository(
            repository_name=repository_name,
            headers=headers,
            **query_parameters
        )

    def get_repository_files(self,
                             repository_name,
                             headers=None,
                             **query_parameters):
        """This will get the full list of files present in the named
        repository. .

        Args:
            repository_name(basestring): repositoryName path
                parameter. Unique name for a repository.
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
        check_type(repository_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'repositoryName': repository_name,
        }

        e_url = ('/api/v1/repository/{repositoryName}/files')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c6f272fde105e50a210f88a9e3f032c_v3_1_patch_1', _api_response)

    def get_files(self,
                  repository_name,
                  headers=None,
                  **query_parameters):
        """Alias for `get_repository_files <#ciscoisesdk.
        api.v3_1_patch_1.repository.
        Repository.get_repository_files>`_
        """
        return self.get_repository_files(
            repository_name=repository_name,
            headers=headers,
            **query_parameters
        )
