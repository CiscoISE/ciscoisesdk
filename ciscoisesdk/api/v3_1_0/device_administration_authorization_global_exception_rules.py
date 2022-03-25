# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Device Administration - Authorization Global Exception Rules API wrapper.

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


class DeviceAdministrationAuthorizationGlobalExceptionRules(object):
    """Identity Services Engine Device Administration - Authorization Global Exception Rules API (version: 3.1.0).

    Wraps the Identity Services Engine Device Administration - Authorization Global Exception Rules
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceAdministrationAuthorizationGlobalExceptionRules
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceAdministrationAuthorizationGlobalExceptionRules, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_device_admin_policy_set_global_exception_rules(self,
                                                           headers=None,
                                                           **query_parameters):
        """Device Admin Get global execption rules.

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

        e_url = ('/api/v1/policy/device-admin/policy-set/global-exception')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e75d766151e85011870229f30e4f5ec3_v3_1_0', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_device_admin_policy_set_global_exception_rules <#ciscoisesdk.
        api.v3_1_0.device_administration_authorization_global_exception_rules.
        DeviceAdministrationAuthorizationGlobalExceptionRules.get_device_admin_policy_set_global_exception_rules>`_
        """
        return self.get_device_admin_policy_set_global_exception_rules(
            headers=headers,
            **query_parameters
        )

    def create_device_admin_policy_set_global_exception(self,
                                                        commands=None,
                                                        link=None,
                                                        profile=None,
                                                        rule=None,
                                                        headers=None,
                                                        payload=None,
                                                        active_validation=True,
                                                        **query_parameters):
        """Device Admin Create global exception authorization rule:
        Rule must include name and condition.     Condition has
        hierarchical structure which define a set of conditions
        for which authoriztion policy rule could be match.
        Condition can be either reference to a stored Library
        condition, using model  ConditionReference    or
        dynamically built conditions which are not stored in the
        conditions Library, using models  ConditionAttributes,
        ConditionAndBlock, ConditionOrBlock .    .

        Args:
            commands(list): Command sets enforce the specified list
                of commands that can be executed by a
                device administrator, property of the
                request body (list of strings).
            link(object): link, property of the request body.
            profile(string): Device admin profiles control the
                initial login session of the device
                administrator, property of the request
                body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
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
                'commands':
                    commands,
                'link':
                    link,
                'profile':
                    profile,
                'rule':
                    rule,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_da0a59db7654cfa89df49ca3ac3414_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/policy-set/global-exception')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_da0a59db7654cfa89df49ca3ac3414_v3_1_0', _api_response)

    def create(self,
               commands=None,
               link=None,
               profile=None,
               rule=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_device_admin_policy_set_global_exception <#ciscoisesdk.
        api.v3_1_0.device_administration_authorization_global_exception_rules.
        DeviceAdministrationAuthorizationGlobalExceptionRules.create_device_admin_policy_set_global_exception>`_
        """
        return self.create_device_admin_policy_set_global_exception(
            commands=commands,
            link=link,
            profile=profile,
            rule=rule,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def reset_hit_counts_device_admin_global_exceptions(self,
                                                        headers=None,
                                                        **query_parameters):
        """Device Admin Reset HitCount for Global Exceptions.

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

        e_url = ('/api/v1/policy/device-admin/policy-set/global-'
                 + 'exception/reset-hitcount')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bd8a6c63d0235f3699f2669ca4734c13_v3_1_0', _api_response)

    def reset_hit_counts(self,
                         headers=None,
                         **query_parameters):
        """Alias for `reset_hit_counts_device_admin_global_exceptions <#ciscoisesdk.
        api.v3_1_0.device_administration_authorization_global_exception_rules.
        DeviceAdministrationAuthorizationGlobalExceptionRules.reset_hit_counts_device_admin_global_exceptions>`_
        """
        return self.reset_hit_counts_device_admin_global_exceptions(
            headers=headers,
            **query_parameters
        )

    def get_device_admin_policy_set_global_exception_by_rule_id(self,
                                                                id,
                                                                headers=None,
                                                                **query_parameters):
        """Device Admin Get global exception rule attribute.

        Args:
            id(basestring): id path parameter. Rule id.
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

        e_url = ('/api/v1/policy/device-admin/policy-set/global-'
                 + 'exception/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b3d905ee2883501281de916733b4025c_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_device_admin_policy_set_global_exception_by_rule_id <#ciscoisesdk.
        api.v3_1_0.device_administration_authorization_global_exception_rules.
        DeviceAdministrationAuthorizationGlobalExceptionRules.get_device_admin_policy_set_global_exception_by_rule_id>`_
        """
        return self.get_device_admin_policy_set_global_exception_by_rule_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_device_admin_policy_set_global_exception_by_rule_id(self,
                                                                   id,
                                                                   commands=None,
                                                                   link=None,
                                                                   profile=None,
                                                                   rule=None,
                                                                   headers=None,
                                                                   payload=None,
                                                                   active_validation=True,
                                                                   **query_parameters):
        """Device Admin Update global exception authorization rule.

        Args:
            commands(list): Command sets enforce the specified list
                of commands that can be executed by a
                device administrator, property of the
                request body (list of strings).
            link(object): link, property of the request body.
            profile(string): Device admin profiles control the
                initial login session of the device
                administrator, property of the request
                body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            id(basestring): id path parameter. Rule id.
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
                'commands':
                    commands,
                'link':
                    link,
                'profile':
                    profile,
                'rule':
                    rule,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d9ddc2557a495493bca08b8b973601aa_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/policy/device-admin/policy-set/global-'
                 + 'exception/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d9ddc2557a495493bca08b8b973601aa_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     commands=None,
                     link=None,
                     profile=None,
                     rule=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_device_admin_policy_set_global_exception_by_rule_id <#ciscoisesdk.
        api.v3_1_0.device_administration_authorization_global_exception_rules.
        DeviceAdministrationAuthorizationGlobalExceptionRules.update_device_admin_policy_set_global_exception_by_rule_id>`_
        """
        return self.update_device_admin_policy_set_global_exception_by_rule_id(
            id=id,
            commands=commands,
            link=link,
            profile=profile,
            rule=rule,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_device_admin_policy_set_global_exception_by_rule_id(self,
                                                                   id,
                                                                   headers=None,
                                                                   **query_parameters):
        """Device Admin Delete global exception authorization rule.

        Args:
            id(basestring): id path parameter. Rule id.
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

        e_url = ('/api/v1/policy/device-admin/policy-set/global-'
                 + 'exception/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f16d14057660520dba53cc0df60db4a8_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_device_admin_policy_set_global_exception_by_rule_id <#ciscoisesdk.
        api.v3_1_0.device_administration_authorization_global_exception_rules.
        DeviceAdministrationAuthorizationGlobalExceptionRules.delete_device_admin_policy_set_global_exception_by_rule_id>`_
        """
        return self.delete_device_admin_policy_set_global_exception_by_rule_id(
            id=id,
            headers=headers,
            **query_parameters
        )
