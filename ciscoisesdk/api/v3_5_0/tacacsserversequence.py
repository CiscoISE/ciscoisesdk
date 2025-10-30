# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine tacacsserversequence API wrapper.

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



from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class Tacacsserversequence(object):
    """Identity Services Engine tacacsserversequence API (version: 3.5.0).

    Wraps the Identity Services Engine tacacsserversequence
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Tacacsserversequence
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Tacacsserversequence, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_tacacsserversequence(self,
                                 page=None,
                                 size=None,
                                 headers=None,
                                 **query_parameters):
        """Get-All.

        Args:
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))

        _params = {
            'page':
                page,
            'size':
                size,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/tacacsserversequence/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f9d0dd405fbe5d428378766c2b27fa8d_v3_5_0', _api_response)

    def get_tacacsserversequence_generator(self,
                                           page=None,
                                           size=None,
                                           headers=None,
                                           **query_parameters):
        """Get-All.

        Args:
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.

              + RestResponse: REST response with following properties:

                  - headers(MyDict): response headers.
                  - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
                    or the bracket notation.
                  - content(bytes): representation of the request's response
                  - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """

        yield from get_next_page(
            self.get_tacacsserversequence, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_tacacsserversequence(self,
                                    description=None,
                                    id=None,
                                    local_accounting=None,
                                    name=None,
                                    prefix_delimiter=None,
                                    prefix_strip=None,
                                    remote_accounting=None,
                                    server_list=None,
                                    suffix_delimiter=None,
                                    suffix_strip=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """Create.

        Args:
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            local_accounting(boolean): localAccounting, property of
                the request body.
            name(string): name, property of the request body.
            prefix_delimiter(string): The delimiter that will be
                used for prefix strip, property of the
                request body.
            prefix_strip(boolean): Define if a delimiter will be
                used for prefix strip, property of the
                request body.
            remote_accounting(boolean): remoteAccounting, property
                of the request body.
            server_list(string): The names of Tacacs external
                servers separated by commas. The order
                of the names in the string is the order
                of servers that will be used during
                authentication, property of the request
                body.
            suffix_delimiter(string): The delimiter that will be
                used for suffix strip, property of the
                request body.
            suffix_strip(boolean): Define if a delimiter will be
                used for suffix strip, property of the
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
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
            check_type(payload, str)
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
            _tmp_payload = {
                'serverList':
                    server_list,
                'localAccounting':
                    local_accounting,
                'remoteAccounting':
                    remote_accounting,
                'prefixStrip':
                    prefix_strip,
                'suffixStrip':
                    suffix_strip,
                'prefixDelimiter':
                    prefix_delimiter,
                'suffixDelimiter':
                    suffix_delimiter,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'TacacsServerSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f7a693dd83b7518d9adf5a3f29a0b3fe_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsserversequence/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f7a693dd83b7518d9adf5a3f29a0b3fe_v3_5_0', _api_response)

    def get_tacacsserversequence_name_by_name(self,
                                              name,
                                              headers=None,
                                              **query_parameters):
        """Get-By-Name.

        Args:
            name(str): name path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/ers/config/tacacsserversequence/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b03900a2e5027b615d9f1bdcf9f63_v3_5_0', _api_response)

    def get_tacacsserversequence_by_id(self,
                                       id,
                                       headers=None,
                                       **query_parameters):
        """Get-By-Id.

        Args:
            id(str): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
        check_type(id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/tacacsserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f3b45b8e4089574c9912407f88b1a5d2_v3_5_0', _api_response)

    def update_tacacsserversequence_by_id(self,
                                          id,
                                          description=None,
                                          local_accounting=None,
                                          name=None,
                                          prefix_delimiter=None,
                                          prefix_strip=None,
                                          remote_accounting=None,
                                          server_list=None,
                                          suffix_delimiter=None,
                                          suffix_strip=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **query_parameters):
        """Update.

        Args:
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            local_accounting(boolean): localAccounting, property of
                the request body.
            name(string): name, property of the request body.
            prefix_delimiter(string): The delimiter that will be
                used for prefix strip, property of the
                request body.
            prefix_strip(boolean): Define if a delimiter will be
                used for prefix strip, property of the
                request body.
            remote_accounting(boolean): remoteAccounting, property
                of the request body.
            server_list(string): The names of Tacacs external
                servers separated by commas. The order
                of the names in the string is the order
                of servers that will be used during
                authentication, property of the request
                body.
            suffix_delimiter(string): The delimiter that will be
                used for suffix strip, property of the
                request body.
            suffix_strip(boolean): Define if a delimiter will be
                used for suffix strip, property of the
                request body.
            id(str): id path parameter.
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
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
            check_type(payload, str)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'serverList':
                    server_list,
                'localAccounting':
                    local_accounting,
                'remoteAccounting':
                    remote_accounting,
                'prefixStrip':
                    prefix_strip,
                'suffixStrip':
                    suffix_strip,
                'prefixDelimiter':
                    prefix_delimiter,
                'suffixDelimiter':
                    suffix_delimiter,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'TacacsServerSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f6de5797735bbd95dc8683c6a7aebf_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f6de5797735bbd95dc8683c6a7aebf_v3_5_0', _api_response)

    def delete_tacacsserversequence_by_id(self,
                                          id,
                                          headers=None,
                                          **query_parameters):
        """Delete.

        Args:
            id(str): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
        check_type(id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/tacacsserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1465b72911359bdbb1430469801d4be_v3_5_0', _api_response)

    def patch_tacacsserversequence_by_id(self,
                                         id,
                                         description=None,
                                         local_accounting=None,
                                         name=None,
                                         prefix_delimiter=None,
                                         prefix_strip=None,
                                         remote_accounting=None,
                                         server_list=None,
                                         suffix_delimiter=None,
                                         suffix_strip=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            local_accounting(boolean): localAccounting, property of
                the request body.
            name(string): name, property of the request body.
            prefix_delimiter(string): The delimiter that will be
                used for prefix strip, property of the
                request body.
            prefix_strip(boolean): Define if a delimiter will be
                used for prefix strip, property of the
                request body.
            remote_accounting(boolean): remoteAccounting, property
                of the request body.
            server_list(string): The names of Tacacs external
                servers separated by commas. The order
                of the names in the string is the order
                of servers that will be used during
                authentication, property of the request
                body.
            suffix_delimiter(string): The delimiter that will be
                used for suffix strip, property of the
                request body.
            suffix_strip(boolean): Define if a delimiter will be
                used for suffix strip, property of the
                request body.
            id(str): id path parameter.
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
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
            check_type(payload, str)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'serverList':
                    server_list,
                'localAccounting':
                    local_accounting,
                'remoteAccounting':
                    remote_accounting,
                'prefixStrip':
                    prefix_strip,
                'suffixStrip':
                    suffix_strip,
                'prefixDelimiter':
                    prefix_delimiter,
                'suffixDelimiter':
                    suffix_delimiter,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'TacacsServerSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a9a1ce0f5d935704a56b49e69140c547_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_a9a1ce0f5d935704a56b49e69140c547_v3_5_0', _api_response)
