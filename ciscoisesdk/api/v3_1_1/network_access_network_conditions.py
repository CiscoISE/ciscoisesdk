# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Network Conditions API wrapper.

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


class NetworkAccessNetworkConditions(object):
    """Identity Services Engine Network Access - Network Conditions API (version: 3.1.1).

    Wraps the Identity Services Engine Network Access - Network Conditions
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessNetworkConditions
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessNetworkConditions, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_network_conditions(self,
                                              headers=None,
                                              **query_parameters):
        """Network Access Returns a list of network conditions.

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

        e_url = ('/api/v1/policy/network-access/network-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d43fec9e7dc556cbb9bf0ebd1dcd6aad_v3_1_1', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_network_access_network_conditions <#ciscoisesdk.
        api.v3_1_1.network_access_network_conditions.
        NetworkAccessNetworkConditions.get_network_access_network_conditions>`_
        """
        return self.get_network_access_network_conditions(
            headers=headers,
            **query_parameters
        )

    def create_network_access_network_condition(self,
                                                condition_type=None,
                                                conditions=None,
                                                description=None,
                                                id=None,
                                                link=None,
                                                name=None,
                                                headers=None,
                                                payload=None,
                                                active_validation=True,
                                                **query_parameters):
        """Network Access Creates network condition.

        Args:
            condition_type(string): This field determines the
                content of the conditions field,
                property of the request body. Available
                values are 'DeviceCondition',
                'DevicePortCondition' and
                'EndstationCondition'.
            conditions(list): conditions, property of the request
                body (list of objects).
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            link(object): link, property of the request body.
            name(string): Network Condition name, property of the
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
                'conditionType':
                    condition_type,
                'description':
                    description,
                'id':
                    id,
                'link':
                    link,
                'name':
                    name,
                'conditions':
                    conditions,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f4dbfb874b3b56d7a651d6732f1bd55e_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/network-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f4dbfb874b3b56d7a651d6732f1bd55e_v3_1_1', _api_response)

    def create(self,
               condition_type=None,
               conditions=None,
               description=None,
               id=None,
               link=None,
               name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_network_access_network_condition <#ciscoisesdk.
        api.v3_1_1.network_access_network_conditions.
        NetworkAccessNetworkConditions.create_network_access_network_condition>`_
        """
        return self.create_network_access_network_condition(
            condition_type=condition_type,
            conditions=conditions,
            description=description,
            id=id,
            link=link,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_network_access_network_condition_by_id(self,
                                                   id,
                                                   headers=None,
                                                   **query_parameters):
        """Network Access Returns a network condition.

        Args:
            id(basestring): id path parameter. Condition id.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/api/v1/policy/network-access/network-condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab015a9eb6d5f2b91002af068cb4ce2_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_network_access_network_condition_by_id <#ciscoisesdk.
        api.v3_1_1.network_access_network_conditions.
        NetworkAccessNetworkConditions.get_network_access_network_condition_by_id>`_
        """
        return self.get_network_access_network_condition_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_network_access_network_condition_by_id(self,
                                                      id,
                                                      condition_type=None,
                                                      conditions=None,
                                                      description=None,
                                                      link=None,
                                                      name=None,
                                                      headers=None,
                                                      payload=None,
                                                      active_validation=True,
                                                      **query_parameters):
        """Network Access Update network condition.

        Args:
            condition_type(string): This field determines the
                content of the conditions field,
                property of the request body. Available
                values are 'DeviceCondition',
                'DevicePortCondition' and
                'EndstationCondition'.
            conditions(list): conditions, property of the request
                body (list of objects).
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            link(object): link, property of the request body.
            name(string): Network Condition name, property of the
                request body.
            id(basestring): id path parameter. Condition id.
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
        check_type(id, basestring,
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
            _payload = {
                'conditionType':
                    condition_type,
                'description':
                    description,
                'id':
                    id,
                'link':
                    link,
                'name':
                    name,
                'conditions':
                    conditions,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cf65cd559628b26f6eb5ea20f14_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/network-condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_cf65cd559628b26f6eb5ea20f14_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     condition_type=None,
                     conditions=None,
                     description=None,
                     link=None,
                     name=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_network_access_network_condition_by_id <#ciscoisesdk.
        api.v3_1_1.network_access_network_conditions.
        NetworkAccessNetworkConditions.update_network_access_network_condition_by_id>`_
        """
        return self.update_network_access_network_condition_by_id(
            id=id,
            condition_type=condition_type,
            conditions=conditions,
            description=description,
            link=link,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_network_access_network_condition_by_id(self,
                                                      id,
                                                      headers=None,
                                                      **query_parameters):
        """Network Access Delete network condition.

        Args:
            id(basestring): id path parameter. Condition id.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/api/v1/policy/network-access/network-condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e92c6e47625711b9ce06f92bd4d219_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_network_access_network_condition_by_id <#ciscoisesdk.
        api.v3_1_1.network_access_network_conditions.
        NetworkAccessNetworkConditions.delete_network_access_network_condition_by_id>`_
        """
        return self.delete_network_access_network_condition_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )
