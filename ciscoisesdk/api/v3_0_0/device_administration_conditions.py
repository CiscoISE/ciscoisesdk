# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Device Administration - Conditions API wrapper.

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


class DeviceAdministrationConditions(object):
    """Identity Services Engine Device Administration - Conditions API (version: 3.0.0).

    Wraps the Identity Services Engine Device Administration - Conditions
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceAdministrationConditions
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceAdministrationConditions, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_device_admin_conditions(self,
                                        headers=None,
                                        **query_parameters):
        """Device Admin - Returns list of library conditions.

        Args:
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

        e_url = ('/api/v1/policy/device-admin/condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_feb825519f98bd1541ef3c367d_v3_0_0', _api_response)

    def create_device_admin_condition(self,
                                      attribute_id=None,
                                      attribute_name=None,
                                      attribute_value=None,
                                      children=None,
                                      condition_type=None,
                                      dates_range=None,
                                      dates_range_exception=None,
                                      description=None,
                                      dictionary_name=None,
                                      dictionary_value=None,
                                      hours_range=None,
                                      hours_range_exception=None,
                                      id=None,
                                      is_negate=None,
                                      name=None,
                                      operator=None,
                                      week_days=None,
                                      week_days_exception=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Device Admin - Creates a library condition.

        Args:
            attribute_id(string): attributeId, property of the
                request body.
            attribute_name(string): attributeName, property of the
                request body.
            attribute_value(string): attributeValue, property of the
                request body.
            children(list): children, property of the request body
                (list of objects).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'ConditionReference',
                'ConditionAttributes',
                'LibraryConditionAttributes',
                'ConditionAndBlock',
                'LibraryConditionAndBlock',
                'ConditionOrBlock',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            dates_range(object): datesRange, property of the request
                body.
            dates_range_exception(object): datesRangeException,
                property of the request body.
            description(string): description, property of the
                request body.
            dictionary_name(string): dictionaryName, property of the
                request body.
            dictionary_value(string): dictionaryValue, property of
                the request body.
            hours_range(object): hoursRange, property of the request
                body.
            hours_range_exception(object): hoursRangeException,
                property of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): isNegate, property of the request
                body.
            name(string): name, property of the request body.
            operator(string): operator, property of the request
                body. Available values are 'equals',
                'notEquals', 'contains', 'notContains',
                'matches', 'in', 'notIn', 'startsWith',
                'notStartsWith', 'endsWith',
                'notEndsWith', 'greaterThan',
                'lessThan', 'greaterOrEquals',
                'lessOrEquals', 'macEquals',
                'macNotEquals', 'macNotIn', 'macIn',
                'macStartsWith', 'macNotStartsWith',
                'macEndsWith', 'macNotEndsWith',
                'macContains', 'macNotContains',
                'ipGreaterThan', 'ipLessThan',
                'ipEquals', 'ipNotEquals',
                'dateTimeMatches', 'dateLessThan',
                'dateLessThanOrEquals',
                'dateGreaterThan',
                'dateGreaterThanOrEquals', 'dateEquals'
                and 'dateNotEquals'.
            weekDays(list): weekDays, property of the request body
                (list of strings. Available values are
                'Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday' and
                'Saturday').
            weekDaysException(list): weekDaysException, property of
                the request body (list of strings.
                Available values are 'Sunday', 'Monday',
                'Tuesday', 'Wednesday', 'Thursday',
                'Friday' and 'Saturday').
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
                'isNegate':
                    is_negate,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'attributeName':
                    attribute_name,
                'attributeId':
                    attribute_id,
                'operator':
                    operator,
                'dictionaryValue':
                    dictionary_value,
                'attributeValue':
                    attribute_value,
                'children':
                    children,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_abc25887a5daab1216195e08cbd49_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/condition')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_abc25887a5daab1216195e08cbd49_v3_0_0', _api_response)

    def get_all_device_admin_conditions_for_policy_set(self,
                                                       headers=None,
                                                       **query_parameters):
        """Device Admin - Returns list of library conditions for policy
        sets.

        Args:
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

        e_url = ('/api/v1/policy/device-admin/condition/policyset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a40f9e169a95d6dbf3ebbb020291007_v3_0_0', _api_response)

    def get_all_device_admin_conditions_for_authentication_rule(self,
                                                                headers=None,
                                                                **query_parameters):
        """Device Admin - Returns list of library conditions for
        authentication rules.

        Args:
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

        e_url = ('/api/v1/policy/device-admin/condition/authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f1b8eaf23e795f1a8525eb5905187aa9_v3_0_0', _api_response)

    def get_all_device_admin_conditions_for_authorization_rule(self,
                                                               headers=None,
                                                               **query_parameters):
        """Device Admin - Returns list of library conditions for
        authorization rules.

        Args:
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

        e_url = ('/api/v1/policy/device-admin/condition/authorization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ecff2eb67fe5591f8d9026f928a0d8aa_v3_0_0', _api_response)

    def get_device_admin_condition_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """Device Admin - Returns a library condition.

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

        e_url = ('/api/v1/policy/device-admin/condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dec8e9d819b5bc088e351b69efd0369_v3_0_0', _api_response)

    def update_device_admin_condition_by_id(self,
                                            id,
                                            attribute_id=None,
                                            attribute_name=None,
                                            attribute_value=None,
                                            children=None,
                                            condition_type=None,
                                            dates_range=None,
                                            dates_range_exception=None,
                                            description=None,
                                            dictionary_name=None,
                                            dictionary_value=None,
                                            hours_range=None,
                                            hours_range_exception=None,
                                            is_negate=None,
                                            name=None,
                                            operator=None,
                                            week_days=None,
                                            week_days_exception=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """Device Admin - Update library condition.

        Args:
            attribute_id(string): attributeId, property of the
                request body.
            attribute_name(string): attributeName, property of the
                request body.
            attribute_value(string): attributeValue, property of the
                request body.
            children(list): children, property of the request body
                (list of objects).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'ConditionReference',
                'ConditionAttributes',
                'LibraryConditionAttributes',
                'ConditionAndBlock',
                'LibraryConditionAndBlock',
                'ConditionOrBlock',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            dates_range(object): datesRange, property of the request
                body.
            dates_range_exception(object): datesRangeException,
                property of the request body.
            description(string): description, property of the
                request body.
            dictionary_name(string): dictionaryName, property of the
                request body.
            dictionary_value(string): dictionaryValue, property of
                the request body.
            hours_range(object): hoursRange, property of the request
                body.
            hours_range_exception(object): hoursRangeException,
                property of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): isNegate, property of the request
                body.
            name(string): name, property of the request body.
            operator(string): operator, property of the request
                body. Available values are 'equals',
                'notEquals', 'contains', 'notContains',
                'matches', 'in', 'notIn', 'startsWith',
                'notStartsWith', 'endsWith',
                'notEndsWith', 'greaterThan',
                'lessThan', 'greaterOrEquals',
                'lessOrEquals', 'macEquals',
                'macNotEquals', 'macNotIn', 'macIn',
                'macStartsWith', 'macNotStartsWith',
                'macEndsWith', 'macNotEndsWith',
                'macContains', 'macNotContains',
                'ipGreaterThan', 'ipLessThan',
                'ipEquals', 'ipNotEquals',
                'dateTimeMatches', 'dateLessThan',
                'dateLessThanOrEquals',
                'dateGreaterThan',
                'dateGreaterThanOrEquals', 'dateEquals'
                and 'dateNotEquals'.
            weekDays(list): weekDays, property of the request body
                (list of strings. Available values are
                'Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday' and
                'Saturday').
            weekDaysException(list): weekDaysException, property of
                the request body (list of strings.
                Available values are 'Sunday', 'Monday',
                'Tuesday', 'Wednesday', 'Thursday',
                'Friday' and 'Saturday').
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
                'isNegate':
                    is_negate,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'attributeName':
                    attribute_name,
                'attributeId':
                    attribute_id,
                'operator':
                    operator,
                'dictionaryValue':
                    dictionary_value,
                'attributeValue':
                    attribute_value,
                'children':
                    children,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ed5bf99062d5dee87fe5cd96e360ec2_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_ed5bf99062d5dee87fe5cd96e360ec2_v3_0_0', _api_response)

    def delete_device_admin_condition_by_id(self,
                                            id,
                                            headers=None,
                                            **query_parameters):
        """Device Admin - Delete a library condition.

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

        e_url = ('/api/v1/policy/device-admin/condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea5b356b4bc053068a0052b6c807d286_v3_0_0', _api_response)

    def get_device_admin_condition_by_name(self,
                                           name,
                                           headers=None,
                                           **query_parameters):
        """Device Admin - Returns a library condition.

        Args:
            name(basestring): name path parameter. Condition name.
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

        e_url = ('/api/v1/policy/device-admin/condition-by-name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab7717877a539b9b87f499817aee15_v3_0_0', _api_response)

    def delete_device_admin_condition_by_name(self,
                                              name,
                                              headers=None,
                                              **query_parameters):
        """NDevice Admin - Delete a library condition using condition Name.

        Args:
            name(basestring): name path parameter. Condition name.
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

        e_url = ('/api/v1/policy/device-admin/condition-by-name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e56dd3caaf62589f9e827d03e8427467_v3_0_0', _api_response)

    def update_device_admin_condition_by_name(self,
                                              name,
                                              attribute_id=None,
                                              attribute_name=None,
                                              attribute_value=None,
                                              children=None,
                                              condition_type=None,
                                              dates_range=None,
                                              dates_range_exception=None,
                                              description=None,
                                              dictionary_name=None,
                                              dictionary_value=None,
                                              hours_range=None,
                                              hours_range_exception=None,
                                              id=None,
                                              is_negate=None,
                                              operator=None,
                                              week_days=None,
                                              week_days_exception=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **query_parameters):
        """Device Admin - Update library condition using condition name.

        Args:
            attribute_id(string): attributeId, property of the
                request body.
            attribute_name(string): attributeName, property of the
                request body.
            attribute_value(string): attributeValue, property of the
                request body.
            children(list): children, property of the request body
                (list of objects).
            condition_type(string): conditionType, property of the
                request body. Available values are
                'ConditionReference',
                'ConditionAttributes',
                'LibraryConditionAttributes',
                'ConditionAndBlock',
                'LibraryConditionAndBlock',
                'ConditionOrBlock',
                'LibraryConditionOrBlock' and
                'TimeAndDateCondition'.
            dates_range(object): datesRange, property of the request
                body.
            dates_range_exception(object): datesRangeException,
                property of the request body.
            description(string): description, property of the
                request body.
            dictionary_name(string): dictionaryName, property of the
                request body.
            dictionary_value(string): dictionaryValue, property of
                the request body.
            hours_range(object): hoursRange, property of the request
                body.
            hours_range_exception(object): hoursRangeException,
                property of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): isNegate, property of the request
                body.
            name(string): name, property of the request body.
            operator(string): operator, property of the request
                body. Available values are 'equals',
                'notEquals', 'contains', 'notContains',
                'matches', 'in', 'notIn', 'startsWith',
                'notStartsWith', 'endsWith',
                'notEndsWith', 'greaterThan',
                'lessThan', 'greaterOrEquals',
                'lessOrEquals', 'macEquals',
                'macNotEquals', 'macNotIn', 'macIn',
                'macStartsWith', 'macNotStartsWith',
                'macEndsWith', 'macNotEndsWith',
                'macContains', 'macNotContains',
                'ipGreaterThan', 'ipLessThan',
                'ipEquals', 'ipNotEquals',
                'dateTimeMatches', 'dateLessThan',
                'dateLessThanOrEquals',
                'dateGreaterThan',
                'dateGreaterThanOrEquals', 'dateEquals'
                and 'dateNotEquals'.
            weekDays(list): weekDays, property of the request body
                (list of strings. Available values are
                'Sunday', 'Monday', 'Tuesday',
                'Wednesday', 'Thursday', 'Friday' and
                'Saturday').
            weekDaysException(list): weekDaysException, property of
                the request body (list of strings.
                Available values are 'Sunday', 'Monday',
                'Tuesday', 'Wednesday', 'Thursday',
                'Friday' and 'Saturday').
            name(basestring): name path parameter. Condition name.
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
                'conditionType':
                    condition_type,
                'isNegate':
                    is_negate,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
                'dictionaryName':
                    dictionary_name,
                'attributeName':
                    attribute_name,
                'attributeId':
                    attribute_id,
                'operator':
                    operator,
                'dictionaryValue':
                    dictionary_value,
                'attributeValue':
                    attribute_value,
                'children':
                    children,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d1e1fc98a5588b8bbdda06c4fc012_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/condition-by-name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d1e1fc98a5588b8bbdda06c4fc012_v3_0_0', _api_response)
