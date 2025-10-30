# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Trustsec Integration Rule - Dictionary Attributes API wrapper.

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


class TrustsecIntegrationRuleDictionaryAttributes(object):
    """Identity Services Engine Trustsec Integration Rule - Dictionary Attributes API (version: 3.5.0).

    Wraps the Identity Services Engine Trustsec Integration Rule - Dictionary Attributes
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new TrustsecIntegrationRuleDictionaryAttributes
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(TrustsecIntegrationRuleDictionaryAttributes, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_common_policy_classification_dictionary_attributes_by_dictionary_name(self,
                                                                                  dictionary_name,
                                                                                  headers=None,
                                                                                  **query_parameters):
        """Trustsec Integraion Rule Returns list of dictionary attributes
        for Classification.

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

        e_url = ('/api/v1/trustsec/classification-'
                 + 'policy/dictionaries/{dictionaryName}/attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f938a08c4be5975b3319c25f2f749c3_v3_5_0', _api_response)

    def get_common_policy_classification_attributes_by_dictionary_name_by_attribute_name(self,
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

        e_url = ('/api/v1/trustsec/classification-policy/dictionaries/{dic'
                 + 'tionaryName}/attribute/{attributeName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f0794e5915b4292abc09bec0dcdd0_v3_5_0', _api_response)

    def get_common_policy_ingress_dictionary_attributes_by_dictionary_name(self,
                                                                           dictionary_name,
                                                                           headers=None,
                                                                           **query_parameters):
        """Trustsec Integraion Rule Returns list of dictionary attributes
        for Inbound.

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

        e_url = ('/api/v1/trustsec/inbound-'
                 + 'rule/dictionaries/{dictionaryName}/attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f7a68260b928570b959ad0780acd181a_v3_5_0', _api_response)

    def get_common_policy_ingress_attributes_by_dictionary_name_by_attribute_name(self,
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

        e_url = ('/api/v1/trustsec/inbound-rule/dictionaries/{dictionaryNa'
                 + 'me}/attribute/{attributeName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fd7d76dbe07a59a0883dc85d75fee7d5_v3_5_0', _api_response)

    def get_common_policy_egress_dictionary_attributes_by_dictionary_name(self,
                                                                          dictionary_name,
                                                                          headers=None,
                                                                          **query_parameters):
        """Trustsec Integraion Rule Returns list of dictionary attributes
        for outbound.

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

        e_url = ('/api/v1/trustsec/outbound-'
                 + 'rule/dictionaries/{dictionaryName}/attribute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aa3278f5051c4aab573d7367ebd73_v3_5_0', _api_response)

    def get_common_policy_egress_attributes_by_dictionary_name_by_attribute_name(self,
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

        e_url = ('/api/v1/trustsec/outbound-rule/dictionaries/{dictionaryN'
                 + 'ame}/attribute/{attributeName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b64207755bd9ec36c74ef795317_v3_5_0', _api_response)
