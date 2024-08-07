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

from builtins import *
from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class DeviceAdministrationConditions(object):
    """Identity Services Engine Device Administration - Conditions API (version: 3.1_Patch_1).

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

    def get_device_admin_conditions(self,
                                    headers=None,
                                    **query_parameters):
        """Device Admin Returns list of library conditions.

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

        e_url = ('/api/v1/policy/device-admin/condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_feb825519f98bd1541ef3c367d_v3_1_patch_1', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_device_admin_conditions <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.get_device_admin_conditions>`_
        """
        return self.get_device_admin_conditions(
            headers=headers,
            **query_parameters
        )

    def create_device_admin_condition(self,
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
                                      link=None,
                                      name=None,
                                      operator=None,
                                      week_days=None,
                                      week_days_exception=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Device Admin Creates a library condition:     Library Condition
        has hierarchical structure which define a set of
        condition for which authentication and authorization
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
            attribute_name(string): Dictionary attribute name,
                property of the request body.
            attribute_value(string): Attribute value for condition
                Value type is specified in dictionary
                object   if multiple values allowed is
                specified in dictionary object, property
                of the request body.
            children(list): In case type is andBlock or orBlock
                addtional conditions will be aggregated
                under this logical (OR/AND) condition,
                property of the request body (list of
                objects).
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
            dictionary_name(string): Dictionary name, property of
                the request body.
            dictionary_value(string): Dictionary value, property of
                the request body.
            hours_range(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time format hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            hours_range_exception(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time format hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
            name(string): Condition name, property of the request
                body.
            operator(string): Equality operator, property of the
                request body. Available values are
                'contains', 'endsWith', 'equals',
                'greaterOrEquals', 'greaterThan', 'in',
                'ipEquals', 'ipGreaterThan',
                'ipLessThan', 'ipNotEquals',
                'lessOrEquals', 'lessThan', 'matches',
                'notContains', 'notEndsWith',
                'notEquals', 'notIn', 'notStartsWith'
                and 'startsWith'.
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
                'isNegate':
                    is_negate,
                'link':
                    link,
                'description':
                    description,
                'id':
                    id,
                'name':
                    name,
                'attributeName':
                    attribute_name,
                'attributeValue':
                    attribute_value,
                'dictionaryName':
                    dictionary_name,
                'dictionaryValue':
                    dictionary_value,
                'operator':
                    operator,
                'children':
                    children,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_abc25887a5daab1216195e08cbd49_v3_1_patch_1')\
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

        return self._object_factory('bpm_abc25887a5daab1216195e08cbd49_v3_1_patch_1', _api_response)

    def create(self,
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
               link=None,
               name=None,
               operator=None,
               week_days=None,
               week_days_exception=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_device_admin_condition <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.create_device_admin_condition>`_
        """
        return self.create_device_admin_condition(
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            children=children,
            condition_type=condition_type,
            dates_range=dates_range,
            dates_range_exception=dates_range_exception,
            description=description,
            dictionary_name=dictionary_name,
            dictionary_value=dictionary_value,
            hours_range=hours_range,
            hours_range_exception=hours_range_exception,
            id=id,
            is_negate=is_negate,
            link=link,
            name=name,
            operator=operator,
            week_days=week_days,
            week_days_exception=week_days_exception,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_device_admin_conditions_for_authentication_rules(self,
                                                             headers=None,
                                                             **query_parameters):
        """Device Admin Returns list of library conditions for
        authentication rules.

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

        e_url = ('/api/v1/policy/device-admin/condition/authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f1b8eaf23e795f1a8525eb5905187aa9_v3_1_patch_1', _api_response)

    def get_all_authentication_rules(self,
                                     headers=None,
                                     **query_parameters):
        """Alias for `get_device_admin_conditions_for_authentication_rules <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.get_device_admin_conditions_for_authentication_rules>`_
        """
        return self.get_device_admin_conditions_for_authentication_rules(
            headers=headers,
            **query_parameters
        )

    def get_device_admin_conditions_for_authorization_rules(self,
                                                            headers=None,
                                                            **query_parameters):
        """Device Admin Returns list of library conditions for
        authorization rules.

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

        e_url = ('/api/v1/policy/device-admin/condition/authorization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ecff2eb67fe5591f8d9026f928a0d8aa_v3_1_patch_1', _api_response)

    def get_all_authorization_rules(self,
                                    headers=None,
                                    **query_parameters):
        """Alias for `get_device_admin_conditions_for_authorization_rules <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.get_device_admin_conditions_for_authorization_rules>`_
        """
        return self.get_device_admin_conditions_for_authorization_rules(
            headers=headers,
            **query_parameters
        )

    def get_device_admin_condition_by_name(self,
                                           name,
                                           headers=None,
                                           **query_parameters):
        """Device Admin Returns a library condition.

        Args:
            name(str): name path parameter. Condition name.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/api/v1/policy/device-admin/condition/condition-by-'
                 + 'name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a47bbc05a3e056fcad73f2cb5b894dae_v3_1_patch_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_device_admin_condition_by_name <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.get_device_admin_condition_by_name>`_
        """
        return self.get_device_admin_condition_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def update_device_admin_condition_by_name(self,
                                              name,
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
                                              link=None,
                                              operator=None,
                                              week_days=None,
                                              week_days_exception=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **query_parameters):
        """Device Admin Update library condition using condition name.

        Args:
            attribute_name(string): Dictionary attribute name,
                property of the request body.
            attribute_value(string): Attribute value for condition
                Value type is specified in dictionary
                object   if multiple values allowed is
                specified in dictionary object, property
                of the request body.
            children(list): In case type is andBlock or orBlock
                addtional conditions will be aggregated
                under this logical (OR/AND) condition,
                property of the request body (list of
                objects).
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
            dictionary_name(string): Dictionary name, property of
                the request body.
            dictionary_value(string): Dictionary value, property of
                the request body.
            hours_range(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time format hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            hours_range_exception(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time format hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
            name(string): Condition name, property of the request
                body.
            operator(string): Equality operator, property of the
                request body. Available values are
                'contains', 'endsWith', 'equals',
                'greaterOrEquals', 'greaterThan', 'in',
                'ipEquals', 'ipGreaterThan',
                'ipLessThan', 'ipNotEquals',
                'lessOrEquals', 'lessThan', 'matches',
                'notContains', 'notEndsWith',
                'notEquals', 'notIn', 'notStartsWith'
                and 'startsWith'.
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
            name(str): name path parameter. Condition name.
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
        check_type(name, str,
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
                'link':
                    link,
                'description':
                    description,
                'id':
                    id,
                'name':
                    name,
                'attributeName':
                    attribute_name,
                'attributeValue':
                    attribute_value,
                'dictionaryName':
                    dictionary_name,
                'dictionaryValue':
                    dictionary_value,
                'operator':
                    operator,
                'children':
                    children,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d17bf558051575aba9f7435c7fcbe05_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/condition/condition-by-'
                 + 'name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d17bf558051575aba9f7435c7fcbe05_v3_1_patch_1', _api_response)

    def update_by_name(self,
                       name,
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
                       link=None,
                       operator=None,
                       week_days=None,
                       week_days_exception=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **query_parameters):
        """Alias for `update_device_admin_condition_by_name <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.update_device_admin_condition_by_name>`_
        """
        return self.update_device_admin_condition_by_name(
            name=name,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            children=children,
            condition_type=condition_type,
            dates_range=dates_range,
            dates_range_exception=dates_range_exception,
            description=description,
            dictionary_name=dictionary_name,
            dictionary_value=dictionary_value,
            hours_range=hours_range,
            hours_range_exception=hours_range_exception,
            id=id,
            is_negate=is_negate,
            link=link,
            operator=operator,
            week_days=week_days,
            week_days_exception=week_days_exception,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_device_admin_condition_by_name(self,
                                              name,
                                              headers=None,
                                              **query_parameters):
        """NDevice Admin Delete a library condition using condition Name.

        Args:
            name(str): name path parameter. Condition name.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/api/v1/policy/device-admin/condition/condition-by-'
                 + 'name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea7a58e36047592d8f37a4ec4e15701d_v3_1_patch_1', _api_response)

    def delete_by_name(self,
                       name,
                       headers=None,
                       **query_parameters):
        """Alias for `delete_device_admin_condition_by_name <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.delete_device_admin_condition_by_name>`_
        """
        return self.delete_device_admin_condition_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_device_admin_conditions_for_policy_sets(self,
                                                    headers=None,
                                                    **query_parameters):
        """Device Admin Returns list of library conditions for policy sets.

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

        e_url = ('/api/v1/policy/device-admin/condition/policyset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a40f9e169a95d6dbf3ebbb020291007_v3_1_patch_1', _api_response)

    def get_all_for_policy_sets(self,
                                headers=None,
                                **query_parameters):
        """Alias for `get_device_admin_conditions_for_policy_sets <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.get_device_admin_conditions_for_policy_sets>`_
        """
        return self.get_device_admin_conditions_for_policy_sets(
            headers=headers,
            **query_parameters
        )

    def get_device_admin_condition_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """Device Admin Returns a library condition.

        Args:
            id(str): id path parameter. Condition id.
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
        check_type(id, str,
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

        return self._object_factory('bpm_dec8e9d819b5bc088e351b69efd0369_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_device_admin_condition_by_id <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.get_device_admin_condition_by_id>`_
        """
        return self.get_device_admin_condition_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_device_admin_condition_by_id(self,
                                            id,
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
                                            link=None,
                                            name=None,
                                            operator=None,
                                            week_days=None,
                                            week_days_exception=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """Device Admin Update library condition.

        Args:
            attribute_name(string): Dictionary attribute name,
                property of the request body.
            attribute_value(string): Attribute value for condition
                Value type is specified in dictionary
                object   if multiple values allowed is
                specified in dictionary object, property
                of the request body.
            children(list): In case type is andBlock or orBlock
                addtional conditions will be aggregated
                under this logical (OR/AND) condition,
                property of the request body (list of
                objects).
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
            dictionary_name(string): Dictionary name, property of
                the request body.
            dictionary_value(string): Dictionary value, property of
                the request body.
            hours_range(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time format hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            hours_range_exception(object): Defines for which hours a
                TimeAndDate condition will be matched
                Time format hh:mm  ( h = hour , mm =
                minutes )   Default All Day , property
                of the request body.
            id(string): id, property of the request body.
            is_negate(boolean): Indicates whereas this condition is
                in negate mode, property of the request
                body.
            link(object): link, property of the request body.
            name(string): Condition name, property of the request
                body.
            operator(string): Equality operator, property of the
                request body. Available values are
                'contains', 'endsWith', 'equals',
                'greaterOrEquals', 'greaterThan', 'in',
                'ipEquals', 'ipGreaterThan',
                'ipLessThan', 'ipNotEquals',
                'lessOrEquals', 'lessThan', 'matches',
                'notContains', 'notEndsWith',
                'notEquals', 'notIn', 'notStartsWith'
                and 'startsWith'.
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
            id(str): id path parameter. Condition id.
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
            _payload = {
                'conditionType':
                    condition_type,
                'isNegate':
                    is_negate,
                'link':
                    link,
                'description':
                    description,
                'id':
                    id,
                'name':
                    name,
                'attributeName':
                    attribute_name,
                'attributeValue':
                    attribute_value,
                'dictionaryName':
                    dictionary_name,
                'dictionaryValue':
                    dictionary_value,
                'operator':
                    operator,
                'children':
                    children,
                'datesRange':
                    dates_range,
                'datesRangeException':
                    dates_range_exception,
                'hoursRange':
                    hours_range,
                'hoursRangeException':
                    hours_range_exception,
                'weekDays':
                    week_days,
                'weekDaysException':
                    week_days_exception,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ed5bf99062d5dee87fe5cd96e360ec2_v3_1_patch_1')\
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

        return self._object_factory('bpm_ed5bf99062d5dee87fe5cd96e360ec2_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
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
                     link=None,
                     name=None,
                     operator=None,
                     week_days=None,
                     week_days_exception=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_device_admin_condition_by_id <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.update_device_admin_condition_by_id>`_
        """
        return self.update_device_admin_condition_by_id(
            id=id,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            children=children,
            condition_type=condition_type,
            dates_range=dates_range,
            dates_range_exception=dates_range_exception,
            description=description,
            dictionary_name=dictionary_name,
            dictionary_value=dictionary_value,
            hours_range=hours_range,
            hours_range_exception=hours_range_exception,
            is_negate=is_negate,
            link=link,
            name=name,
            operator=operator,
            week_days=week_days,
            week_days_exception=week_days_exception,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_device_admin_condition_by_id(self,
                                            id,
                                            headers=None,
                                            **query_parameters):
        """Device Admin Delete a library condition.

        Args:
            id(str): id path parameter. Condition id.
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
        check_type(id, str,
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

        return self._object_factory('bpm_ea5b356b4bc053068a0052b6c807d286_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_device_admin_condition_by_id <#ciscoisesdk.
        api.v3_1_patch_1.device_administration_conditions.
        DeviceAdministrationConditions.delete_device_admin_condition_by_id>`_
        """
        return self.delete_device_admin_condition_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )
