# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Dictionary Attributes API wrapper.

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


class NetworkAccessDictionaryAttributes(object):
    """Identity Services Engine Network Access - Dictionary Attributes API (version: 3.5.0).

    Wraps the Identity Services Engine Network Access - Dictionary Attributes
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessDictionaryAttributes
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessDictionaryAttributes, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_dictionary_attributes_by_dictionary_name(self,
                                                                    dictionary_name,
                                                                    headers=None,
                                                                    **query_parameters):
        """Returns a list of Dictionary Attributes for an existing
        Dictionary.

        Args:
            dictionary_name(str): dictionaryName path parameter. the
                name of the dictionary the dictionary
                attribute belongs to.
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
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(dictionary_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'dictionaryName': dictionary_name,
        }

        e_url = ('/api/v1/policy/network-'
                 + 'access/dictionaries/{dictionaryName}/attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d83302be1f7c528e8211524aeaacd66d_v3_5_0', _api_response)

    def post_network_access_dictionaries_by_dictionary_name_attribute(self,
                                                                      dictionary_name,
                                                                      allowed_values=None,
                                                                      data_type=None,
                                                                      description=None,
                                                                      direction_type=None,
                                                                      id=None,
                                                                      internal_name=None,
                                                                      name=None,
                                                                      headers=None,
                                                                      payload=None,
                                                                      active_validation=True,
                                                                      **query_parameters):
        """Create a new Dictionary Attribute for an existing Dictionary.

        Args:
            allowed_values(list): all of the allowed values for the
                dictionary attribute, property of the
                request body (list of objects).
            data_type(string): the data type for the dictionary
                attribute, property of the request body.
                Available values are 'BOOLEAN', 'DATE',
                'FLOAT', 'INT', 'IP', 'IPV4', 'IPV6',
                'IPV6INTERFACE', 'IPV6PREFIX', 'LONG',
                'OCTET_STRING', 'STRING', 'UINT64' and
                'UNIT32'.
            description(string): The description of the Dictionary
                attribute, property of the request body.
            dictionary_name(string): the name of the dictionary
                which the dictionary attribute belongs
                to, property of the request body.
            direction_type(string): the direction for the useage of
                the dictionary attribute, property of
                the request body. Available values are
                'BOTH', 'IN', 'NONE' and 'OUT'.
            id(string): Identifier for the dictionary attribute,
                property of the request body.
            internal_name(string): the internal name of the
                dictionary attribute, property of the
                request body.
            name(string): The dictionary attribute's name, property
                of the request body.
            dictionary_name(str): dictionaryName path parameter. the
                name of the dictionary the dictionary
                attribute belongs to.
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
                           str)

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
        check_type(dictionary_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'dictionaryName': dictionary_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'allowedValues':
                    allowed_values,
                'dataType':
                    data_type,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'directionType':
                    direction_type,
                'id':
                    id,
                'internalName':
                    internal_name,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f4508bb3352ff920dbdc229e0fc50_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-'
                 + 'access/dictionaries/{dictionaryName}/attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f4508bb3352ff920dbdc229e0fc50_v3_5_0', _api_response)

    def get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(self,
                                                                                       attribute_name,
                                                                                       dictionary_name,
                                                                                       headers=None,
                                                                                       **query_parameters):
        """Get a Dictionary Attribute.

        Args:
            attribute_name(str): attributeName path parameter. the
                dictionary attribute name.
            dictionary_name(str): dictionaryName path parameter. the
                name of the dictionary the dictionary
                attribute belongs to.
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
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(attribute_name, str,
                   may_be_none=False)
        check_type(dictionary_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'attributeName': attribute_name,
            'dictionaryName': dictionary_name,
        }

        e_url = ('/api/v1/policy/network-access/dictionaries/{dictionaryNa'
                 + 'me}/attribute/{attributeName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fbd7ec7052709e5d0e0a46dc7f68_v3_5_0', _api_response)

    def put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(self,
                                                                                       attribute_name,
                                                                                       dictionary_name,
                                                                                       allowed_values=None,
                                                                                       data_type=None,
                                                                                       description=None,
                                                                                       direction_type=None,
                                                                                       id=None,
                                                                                       internal_name=None,
                                                                                       name=None,
                                                                                       headers=None,
                                                                                       payload=None,
                                                                                       active_validation=True,
                                                                                       **query_parameters):
        """Update a Dictionary Attribute.

        Args:
            allowed_values(list): all of the allowed values for the
                dictionary attribute, property of the
                request body (list of objects).
            data_type(string): the data type for the dictionary
                attribute, property of the request body.
                Available values are 'BOOLEAN', 'DATE',
                'FLOAT', 'INT', 'IP', 'IPV4', 'IPV6',
                'IPV6INTERFACE', 'IPV6PREFIX', 'LONG',
                'OCTET_STRING', 'STRING', 'UINT64' and
                'UNIT32'.
            description(string): The description of the Dictionary
                attribute, property of the request body.
            dictionary_name(string): the name of the dictionary
                which the dictionary attribute belongs
                to, property of the request body.
            direction_type(string): the direction for the useage of
                the dictionary attribute, property of
                the request body. Available values are
                'BOTH', 'IN', 'NONE' and 'OUT'.
            id(string): Identifier for the dictionary attribute,
                property of the request body.
            internal_name(string): the internal name of the
                dictionary attribute, property of the
                request body.
            name(string): The dictionary attribute's name, property
                of the request body.
            attribute_name(str): attributeName path parameter. the
                dictionary attribute name.
            dictionary_name(str): dictionaryName path parameter. the
                name of the dictionary the dictionary
                attribute belongs to.
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
                           str)

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
        check_type(attribute_name, str,
                   may_be_none=False)
        check_type(dictionary_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'attributeName': attribute_name,
            'dictionaryName': dictionary_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'allowedValues':
                    allowed_values,
                'dataType':
                    data_type,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'directionType':
                    direction_type,
                'id':
                    id,
                'internalName':
                    internal_name,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fda64cd1ab7d53448962f61de0f76948_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/dictionaries/{dictionaryNa'
                 + 'me}/attribute/{attributeName}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_fda64cd1ab7d53448962f61de0f76948_v3_5_0', _api_response)

    def delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(self,
                                                                                          attribute_name,
                                                                                          dictionary_name,
                                                                                          headers=None,
                                                                                          **query_parameters):
        """Delete a Dictionary Attribute.

        Args:
            attribute_name(str): attributeName path parameter. the
                dictionary attribute name.
            dictionary_name(str): dictionaryName path parameter. the
                name of the dictionary the dictionary
                attribute belongs to.
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
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(attribute_name, str,
                   may_be_none=False)
        check_type(dictionary_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'attributeName': attribute_name,
            'dictionaryName': dictionary_name,
        }

        e_url = ('/api/v1/policy/network-access/dictionaries/{dictionaryNa'
                 + 'me}/attribute/{attributeName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c813c9b5a73b6d00cac1ca5a41f_v3_5_0', _api_response)
