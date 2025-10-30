# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Device Administration - Time/Date Conditions API wrapper.

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


class DeviceAdministrationTimeDateConditions(object):
    """Identity Services Engine Device Administration - Time/Date Conditions API (version: 3.5.0).

    Wraps the Identity Services Engine Device Administration - Time/Date Conditions
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceAdministrationTimeDateConditions
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceAdministrationTimeDateConditions, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_device_admin_time_conditions(self,
                                         headers=None,
                                         **query_parameters):
        """Device Admin Returns a list of time and date conditions.

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

        e_url = ('/api/v1/policy/device-admin/time-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f79ab23563d857e58e01a74e37333572_v3_5_0', _api_response)

    def post_device_admin_time_condition(self,
                                         condition_type=None,
                                         dates_range=None,
                                         dates_range_exception=None,
                                         description=None,
                                         hours_range=None,
                                         hours_range_exception=None,
                                         id=None,
                                         is_negate=None,
                                         link=None,
                                         name=None,
                                         week_days=None,
                                         week_days_exception=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """Device Admin Creates time/date condition.

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
            dates_range(object): Defines for which date/s
                TimeAndDate condition will be matched
                Options are Date range, for specific
                date, the same date should be used for
                start/end date   Default no specific
                dates  In order to reset the dates to
                have no specific dates Date format yyyy-
                mm-dd (MM = month, dd = day, yyyy =
                year), property of the request body.
            dates_range_exception(object): Defines for which date/s
                TimeAndDate condition will be matched
                Options are Date range, for specific
                date, the same date should be used for
                start/end date   Default no specific
                dates  In order to reset the dates to
                have no specific dates Date format yyyy-
                mm-dd (MM = month, dd = day, yyyy =
                year), property of the request body.
            description(string): Condition description, property of
                the request body.
            hours_range(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time foramt hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            hours_range_exception(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time foramt hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
            name(string): Condition name, property of the request
                body.
            week_days(list): Defines for which days this condition
                will be matched  Days format Arrays of
                WeekDay enums   Default List of All week
                days, property of the request body (list
                of strings. Available values are
                'Friday', 'Monday', 'Saturday',
                'Sunday', 'Thursday', 'Tuesday' and
                'Wednesday').
            week_days_exception(list): Defines for which days this
                condition will NOT be matched  Days
                format Arrays of WeekDay enums   Default
                Not enabled, property of the request
                body (list of strings. Available values
                are 'Friday', 'Monday', 'Saturday',
                'Sunday', 'Thursday', 'Tuesday' and
                'Wednesday').
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
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
                'description':
                    description,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'id':
                    id,
                'isNegate':
                    is_negate,
                'link':
                    link,
                'name':
                    name,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a4d5b5da6a50bfaaecc180543fd952_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/time-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a4d5b5da6a50bfaaecc180543fd952_v3_5_0', _api_response)

    def get_device_admin_time_condition_by_condition_id(self,
                                                        condition_id,
                                                        headers=None,
                                                        **query_parameters):
        """Device Admin Returns a network condition.

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

        e_url = ('/api/v1/policy/device-admin/time-condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4af71bd9e705f1bb1d236b3c16e5f51_v3_5_0', _api_response)

    def put_device_admin_time_condition_by_condition_id(self,
                                                        condition_id,
                                                        condition_type=None,
                                                        dates_range=None,
                                                        dates_range_exception=None,
                                                        description=None,
                                                        hours_range=None,
                                                        hours_range_exception=None,
                                                        id=None,
                                                        is_negate=None,
                                                        link=None,
                                                        name=None,
                                                        week_days=None,
                                                        week_days_exception=None,
                                                        headers=None,
                                                        payload=None,
                                                        active_validation=True,
                                                        **query_parameters):
        """Device Admin Update network condition.

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
            dates_range(object): Defines for which date/s
                TimeAndDate condition will be matched
                Options are Date range, for specific
                date, the same date should be used for
                start/end date   Default no specific
                dates  In order to reset the dates to
                have no specific dates Date format yyyy-
                mm-dd (MM = month, dd = day, yyyy =
                year), property of the request body.
            dates_range_exception(object): Defines for which date/s
                TimeAndDate condition will be matched
                Options are Date range, for specific
                date, the same date should be used for
                start/end date   Default no specific
                dates  In order to reset the dates to
                have no specific dates Date format yyyy-
                mm-dd (MM = month, dd = day, yyyy =
                year), property of the request body.
            description(string): Condition description, property of
                the request body.
            hours_range(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time foramt hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            hours_range_exception(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time foramt hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
            name(string): Condition name, property of the request
                body.
            week_days(list): Defines for which days this condition
                will be matched  Days format Arrays of
                WeekDay enums   Default List of All week
                days, property of the request body (list
                of strings. Available values are
                'Friday', 'Monday', 'Saturday',
                'Sunday', 'Thursday', 'Tuesday' and
                'Wednesday').
            week_days_exception(list): Defines for which days this
                condition will NOT be matched  Days
                format Arrays of WeekDay enums   Default
                Not enabled, property of the request
                body (list of strings. Available values
                are 'Friday', 'Monday', 'Saturday',
                'Sunday', 'Thursday', 'Tuesday' and
                'Wednesday').
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
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
                'description':
                    description,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'id':
                    id,
                'isNegate':
                    is_negate,
                'link':
                    link,
                'name':
                    name,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b9e7d29b0356b2b1d5fdb2e1069265_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/time-condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b9e7d29b0356b2b1d5fdb2e1069265_v3_5_0', _api_response)

    def delete_device_admin_time_condition_by_condition_id(self,
                                                           condition_id,
                                                           headers=None,
                                                           **query_parameters):
        """Device Admin Delete Time/Date condition.

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

        e_url = ('/api/v1/policy/device-admin/time-condition/{conditionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e4ce332e5cdc97399fe9f01b163e_v3_5_0', _api_response)
