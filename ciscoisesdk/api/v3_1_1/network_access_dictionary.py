# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Dictionary API wrapper.

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


class NetworkAccessDictionary(object):
    """Identity Services Engine Network Access - Dictionary API (version: 3.1.1).

    Wraps the Identity Services Engine Network Access - Dictionary
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessDictionary
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessDictionary, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_dictionaries(self,
                                        headers=None,
                                        **query_parameters):
        """Get all Dictionaries.

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

        e_url = ('/api/v1/policy/network-access/dictionaries')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e5a8315e699f55c09102e7c653333d4e_v3_1_1', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_network_access_dictionaries <#ciscoisesdk.
        api.v3_1_1.network_access_dictionary.
        NetworkAccessDictionary.get_network_access_dictionaries>`_
        """
        return self.get_network_access_dictionaries(
            headers=headers,
            **query_parameters
        )

    def create_network_access_dictionaries(self,
                                           description=None,
                                           dictionary_attr_type=None,
                                           id=None,
                                           link=None,
                                           name=None,
                                           version=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **query_parameters):
        """Network Access Create a new Dictionary.

        Args:
            description(string): The description of the Dictionary,
                property of the request body.
            dictionary_attr_type(string): The dictionary attribute
                type, property of the request body.
                Available values are 'ENTITY_ATTR',
                'MSG_ATTR' and 'PIP_ATTR'.
            id(string): Identifier for the dictionary, property of
                the request body.
            link(object): link, property of the request body.
            name(string): The dictionary name, property of the
                request body.
            version(string): The dictionary version, property of the
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
                'description':
                    description,
                'dictionaryAttrType':
                    dictionary_attr_type,
                'id':
                    id,
                'link':
                    link,
                'name':
                    name,
                'version':
                    version,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a57687cef65891a6f48dd17f456c4e_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/dictionaries')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a57687cef65891a6f48dd17f456c4e_v3_1_1', _api_response)

    def create(self,
               description=None,
               dictionary_attr_type=None,
               id=None,
               link=None,
               name=None,
               version=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_network_access_dictionaries <#ciscoisesdk.
        api.v3_1_1.network_access_dictionary.
        NetworkAccessDictionary.create_network_access_dictionaries>`_
        """
        return self.create_network_access_dictionaries(
            description=description,
            dictionary_attr_type=dictionary_attr_type,
            id=id,
            link=link,
            name=name,
            version=version,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_network_access_dictionary_by_name(self,
                                              name,
                                              headers=None,
                                              **query_parameters):
        """GET a dictionary by name.

        Args:
            name(basestring): name path parameter. the dictionary
                name.
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
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/api/v1/policy/network-access/dictionaries/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f1fd8e2bd1581aabf7cd87bff65137_v3_1_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_network_access_dictionary_by_name <#ciscoisesdk.
        api.v3_1_1.network_access_dictionary.
        NetworkAccessDictionary.get_network_access_dictionary_by_name>`_
        """
        return self.get_network_access_dictionary_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def update_network_access_dictionary_by_name(self,
                                                 name,
                                                 description=None,
                                                 dictionary_attr_type=None,
                                                 id=None,
                                                 link=None,
                                                 version=None,
                                                 headers=None,
                                                 payload=None,
                                                 active_validation=True,
                                                 **query_parameters):
        """Network Access Update a Dictionary.

        Args:
            description(string): The description of the Dictionary,
                property of the request body.
            dictionary_attr_type(string): The dictionary attribute
                type, property of the request body.
                Available values are 'ENTITY_ATTR',
                'MSG_ATTR' and 'PIP_ATTR'.
            id(string): Identifier for the dictionary, property of
                the request body.
            link(object): link, property of the request body.
            name(string): The dictionary name, property of the
                request body.
            version(string): The dictionary version, property of the
                request body.
            name(basestring): name path parameter. the dictionary
                name.
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
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'description':
                    description,
                'dictionaryAttrType':
                    dictionary_attr_type,
                'id':
                    id,
                'link':
                    link,
                'name':
                    name,
                'version':
                    version,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a4cccea3c9567498f6f688e0cf86e7_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/dictionaries/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a4cccea3c9567498f6f688e0cf86e7_v3_1_1', _api_response)

    def update_by_name(self,
                       name,
                       description=None,
                       dictionary_attr_type=None,
                       id=None,
                       link=None,
                       version=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **query_parameters):
        """Alias for `update_network_access_dictionary_by_name <#ciscoisesdk.
        api.v3_1_1.network_access_dictionary.
        NetworkAccessDictionary.update_network_access_dictionary_by_name>`_
        """
        return self.update_network_access_dictionary_by_name(
            name=name,
            description=description,
            dictionary_attr_type=dictionary_attr_type,
            id=id,
            link=link,
            version=version,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_network_access_dictionary_by_name(self,
                                                 name,
                                                 headers=None,
                                                 **query_parameters):
        """Network Access Delete a Dictionary.

        Args:
            name(basestring): name path parameter. the dictionary
                name.
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
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/api/v1/policy/network-access/dictionaries/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dfae2409eecc551298e9fa31d14f43d0_v3_1_1', _api_response)

    def delete_by_name(self,
                       name,
                       headers=None,
                       **query_parameters):
        """Alias for `delete_network_access_dictionary_by_name <#ciscoisesdk.
        api.v3_1_1.network_access_dictionary.
        NetworkAccessDictionary.delete_network_access_dictionary_by_name>`_
        """
        return self.delete_network_access_dictionary_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )
