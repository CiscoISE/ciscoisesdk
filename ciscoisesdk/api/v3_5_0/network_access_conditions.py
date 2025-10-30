# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Conditions API wrapper.

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


class NetworkAccessConditions(object):
    """Identity Services Engine Network Access - Conditions API (version: 3.5.0).

    Wraps the Identity Services Engine Network Access - Conditions
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessConditions
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessConditions, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_conditions(self,
                                      headers=None,
                                      **query_parameters):
        """Network Access Returns all library conditions.

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

        e_url = ('/api/v1/policy/network-access/condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_df4fb303a3e5661ba12058f18b225af_v3_5_0', _api_response)

    def post_network_access_condition(self,
                                      condition_type=None,
                                      is_negate=None,
                                      link=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Network Access Creates a library condition:     Library
        Condition has hierarchical structure which define a set
        of condition for which authentication and authorization
        policy rules could be match.    Condition can be compose
        from single dictionary attribute name and value using
        model  LibraryConditionAttributes  , or from combination
        of dictionary attributes with logical operation of
        AND/OR between them, using models:
        LibraryConditionAndBlock  or  LibraryConditionOrBlock .
        When using AND/OR blocks, the condition will include
        inner layers inside these blocks, these layers are built
        using the inner condition models:  ConditionAttributes ,
        ConditionAndBlock ,  ConditionOrBlock , that represent
        dynamically built Conditions which are not stored in the
        conditions Library, or using  ConditionReference , which
        includes an ID to existing stored condition in the
        library.    The LibraryCondition models can only be used
        in the outer-most layer (root of the condition) and must
        always include the condition name.    When using one of
        the 3 inner condition models ( ConditionAttributes,
        ConditionAndBlock, ConditionOrBlock ), condition name
        cannot be included in the request, since these will not
        be stored in the conditions library, and used only as
        inner members of the root condition.    When using
        ConditionReference  model in inner layers, the condition
        name is not required.    ConditionReference objects can
        also include a reference ID to a condition of type
        TimeAndDate .    .

        Args:
            condition_type(string): Inidicates whether the record is
                the condition itself(data) or a
                logical(or,and) aggregation   Data type
                enum(reference,single) indicates than
                "conditonId" OR "ConditionAttrs" fields
                should contain condition data but not
                both   Logical aggreation(and,or) enum
                indicates that additional conditions are
                present under the children field,
                property of the request body. Available
                values are 'ConditionAndBlock',
                'ConditionAttributes',
                'ConditionOrBlock',
                'ConditionReference',
                'LibraryConditionAndBlock',
                'LibraryConditionAttributes',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
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
                'isNegate':
                    is_negate,
                'link':
                    link,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e7bd468ee94f53869e52e84454efd0e6_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/condition')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e7bd468ee94f53869e52e84454efd0e6_v3_5_0', _api_response)

    def get_network_access_conditions_for_authentication_rule(self,
                                                              headers=None,
                                                              **query_parameters):
        """Network Access Returns list of library conditions for
        Authentication rules scope.

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

        e_url = ('/api/v1/policy/network-access/condition/authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e34177d675622acd0a532f5b7c41b_v3_5_0', _api_response)

    def get_network_access_conditions_for_authorization_rule(self,
                                                             headers=None,
                                                             **query_parameters):
        """Network Access Returns list of library conditions for
        Authorization rules scope.

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

        e_url = ('/api/v1/policy/network-access/condition/authorization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fff985b5159a0aa52bfe9e62ba7_v3_5_0', _api_response)

    def get_network_access_condition_by_condition_name(self,
                                                       condition_name,
                                                       headers=None,
                                                       **query_parameters):
        """Network Access Returns a library condition.

        Args:
            condition_name(str): conditionName path parameter.
                Condition name.
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
        check_type(condition_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'conditionName': condition_name,
        }

        e_url = ('/api/v1/policy/network-access/condition/condition-by-'
                 + 'name/{conditionName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b2de4af8550598ddbd9d3d1da2dd_v3_5_0', _api_response)

    def put_network_access_condition_by_condition_name(self,
                                                       condition_name,
                                                       condition_type=None,
                                                       is_negate=None,
                                                       link=None,
                                                       headers=None,
                                                       payload=None,
                                                       active_validation=True,
                                                       **query_parameters):
        """Network Access Update library condition using condition name.

        Args:
            condition_type(string): Inidicates whether the record is
                the condition itself(data) or a
                logical(or,and) aggregation   Data type
                enum(reference,single) indicates than
                "conditonId" OR "ConditionAttrs" fields
                should contain condition data but not
                both   Logical aggreation(and,or) enum
                indicates that additional conditions are
                present under the children field,
                property of the request body. Available
                values are 'ConditionAndBlock',
                'ConditionAttributes',
                'ConditionOrBlock',
                'ConditionReference',
                'LibraryConditionAndBlock',
                'LibraryConditionAttributes',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
            condition_name(str): conditionName path parameter.
                Condition name.
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
        check_type(condition_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'conditionName': condition_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'conditionType':
                    condition_type,
                'isNegate':
                    is_negate,
                'link':
                    link,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f837e7a5fc075ee99d82f92501d2eaeb_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/condition/condition-by-'
                 + 'name/{conditionName}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f837e7a5fc075ee99d82f92501d2eaeb_v3_5_0', _api_response)

    def delete_network_access_condition_by_condition_name(self,
                                                          condition_name,
                                                          headers=None,
                                                          **query_parameters):
        """Network Access Delete a library condition using condition Name.

        Args:
            condition_name(str): conditionName path parameter.
                Condition name.
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
        check_type(condition_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'conditionName': condition_name,
        }

        e_url = ('/api/v1/policy/network-access/condition/condition-by-'
                 + 'name/{conditionName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afb9eeda941530e9276aafb2fb0211c_v3_5_0', _api_response)

    def get_network_access_conditions_for_policy_set(self,
                                                     headers=None,
                                                     **query_parameters):
        """Network Access Returns list of library conditions for PolicySet
        scope.

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

        e_url = ('/api/v1/policy/network-access/condition/policyset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c0984cde5e925c209ab87472ab905476_v3_5_0', _api_response)

    def get_network_access_condition_by_condition_id(self,
                                                     condition_id,
                                                     headers=None,
                                                     **query_parameters):
        """Network Access Returns a library condition.

        Args:
            condition_id(str): conditionId path parameter. Condition
                id.
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
        check_type(condition_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'conditionId': condition_id,
        }

        e_url = ('/api/v1/policy/network-access/condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e4686a7511884fd3eee7c582efb_v3_5_0', _api_response)

    def put_network_access_condition_by_condition_id(self,
                                                     condition_id,
                                                     condition_type=None,
                                                     is_negate=None,
                                                     link=None,
                                                     headers=None,
                                                     payload=None,
                                                     active_validation=True,
                                                     **query_parameters):
        """Network Access Update library condition.

        Args:
            condition_type(string): Inidicates whether the record is
                the condition itself(data) or a
                logical(or,and) aggregation   Data type
                enum(reference,single) indicates than
                "conditonId" OR "ConditionAttrs" fields
                should contain condition data but not
                both   Logical aggreation(and,or) enum
                indicates that additional conditions are
                present under the children field,
                property of the request body. Available
                values are 'ConditionAndBlock',
                'ConditionAttributes',
                'ConditionOrBlock',
                'ConditionReference',
                'LibraryConditionAndBlock',
                'LibraryConditionAttributes',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
            condition_id(str): conditionId path parameter. Condition
                id.
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
        check_type(condition_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'conditionId': condition_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'conditionType':
                    condition_type,
                'isNegate':
                    is_negate,
                'link':
                    link,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_3bfe54779ae1b3edccb16fa7_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_3bfe54779ae1b3edccb16fa7_v3_5_0', _api_response)

    def delete_network_access_condition_by_condition_id(self,
                                                        condition_id,
                                                        headers=None,
                                                        **query_parameters):
        """Network Access Delete a library condition.

        Args:
            condition_id(str): conditionId path parameter. Condition
                id.
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
        check_type(condition_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'conditionId': condition_id,
        }

        e_url = ('/api/v1/policy/network-access/condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d6d09f7a5084ac7036167214b0e1_v3_5_0', _api_response)
