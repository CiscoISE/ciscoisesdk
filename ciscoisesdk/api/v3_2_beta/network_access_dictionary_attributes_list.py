# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Dictionary Attributes List API wrapper.

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

from builtins import *
from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class NetworkAccessDictionaryAttributesList(object):
    """Identity Services Engine Network Access - Dictionary Attributes List API (version: 3.2_beta).

    Wraps the Identity Services Engine Network Access - Dictionary Attributes List
    API and exposes the API as native Python
    methods that return native Python objects.

    Policy APIs for manage Policy Sets, authorization policies, authentication policies, and policy elements.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessDictionaryAttributesList
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessDictionaryAttributesList, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_dictionaries_authentication(self,
                                                       headers=None,
                                                       **query_parameters):
        """Network Access Returns list of dictionary attributes for
        authentication.

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
                           str)

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

        e_url = ('/api/v1/policy/network-'
                 + 'access/dictionaries/authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab96d3d76de5d05bbac1f27feacb7b0_v3_2_beta', _api_response)

    def get_all_authentication(self,
                               headers=None,
                               **query_parameters):
        """Alias for `get_network_access_dictionaries_authentication <#ciscoisesdk.
        api.v3_2_beta.network_access_dictionary_attributes_list.
        NetworkAccessDictionaryAttributesList.get_network_access_dictionaries_authentication>`_
        """
        return self.get_network_access_dictionaries_authentication(
            headers=headers,
            **query_parameters
        )

    def get_network_access_dictionaries_authorization(self,
                                                      headers=None,
                                                      **query_parameters):
        """Network Access Returns list of dictionary attributes for
        authorization.

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
                           str)

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

        e_url = ('/api/v1/policy/network-access/dictionaries/authorization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f68aee0cdb425390b3ca90b0b46e6e2c_v3_2_beta', _api_response)

    def get_all_authorization(self,
                              headers=None,
                              **query_parameters):
        """Alias for `get_network_access_dictionaries_authorization <#ciscoisesdk.
        api.v3_2_beta.network_access_dictionary_attributes_list.
        NetworkAccessDictionaryAttributesList.get_network_access_dictionaries_authorization>`_
        """
        return self.get_network_access_dictionaries_authorization(
            headers=headers,
            **query_parameters
        )

    def get_network_access_dictionaries_policy_set(self,
                                                   headers=None,
                                                   **query_parameters):
        """Network Access Returns list of dictionary attributes for
        policyset.

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
                           str)

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

        e_url = ('/api/v1/policy/network-access/dictionaries/policyset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c53b22885f5e5d82fb8cadd0332136_v3_2_beta', _api_response)

    def get_all_policy_set(self,
                           headers=None,
                           **query_parameters):
        """Alias for `get_network_access_dictionaries_policy_set <#ciscoisesdk.
        api.v3_2_beta.network_access_dictionary_attributes_list.
        NetworkAccessDictionaryAttributesList.get_network_access_dictionaries_policy_set>`_
        """
        return self.get_network_access_dictionaries_policy_set(
            headers=headers,
            **query_parameters
        )
