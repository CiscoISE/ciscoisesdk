# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Authentication Rules API wrapper.

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


class NetworkAccessAuthenticationRules(object):
    """Identity Services Engine Network Access - Authentication Rules API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine Network Access - Authentication Rules
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessAuthenticationRules
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessAuthenticationRules, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_authentication_rules(self,
                                                policy_id,
                                                headers=None,
                                                **query_parameters):
        """Network Access Get authentication rules.

        Args:
            policy_id(basestring): policyId path parameter. Policy
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
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(policy_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
        }

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bee301e7f5ccfa2e788dcafbf92cc_v3_1_patch_1', _api_response)

    def get_all(self,
                policy_id,
                headers=None,
                **query_parameters):
        """Alias for `get_network_access_authentication_rules <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authentication_rules.
        NetworkAccessAuthenticationRules.get_network_access_authentication_rules>`_
        """
        return self.get_network_access_authentication_rules(
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )

    def create_network_access_authentication_rule(self,
                                                  policy_id,
                                                  identity_source_name=None,
                                                  if_auth_fail=None,
                                                  if_process_fail=None,
                                                  if_user_not_found=None,
                                                  link=None,
                                                  rule=None,
                                                  headers=None,
                                                  payload=None,
                                                  active_validation=True,
                                                  **query_parameters):
        """Network Access Create authentication rule:     Rule must include
        name and condition.     Condition has hierarchical
        structure which define a set of conditions for which
        authentication policy rule could be match.     Condition
        can be either reference to a stored Library condition,
        using model  ConditionReference    or dynamically built
        conditions which are not stored in the conditions
        Library, using models  ConditionAttributes,
        ConditionAndBlock, ConditionOrBlock .    .

        Args:
            identity_source_name(string): Identity source name from
                the identity stores, property of the
                request body.
            if_auth_fail(string): Action to perform when
                authentication fails such as Bad
                credentials, disabled user and so on,
                property of the request body.
            if_process_fail(string): Action to perform when ISE is
                uanble to access the identity database,
                property of the request body.
            if_user_not_found(string): Action to perform when user
                is not found in any of identity stores,
                property of the request body.
            link(object): link, property of the request body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            policy_id(basestring): policyId path parameter. Policy
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
        check_type(policy_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'identitySourceName':
                    identity_source_name,
                'ifAuthFail':
                    if_auth_fail,
                'ifProcessFail':
                    if_process_fail,
                'ifUserNotFound':
                    if_user_not_found,
                'link':
                    link,
                'rule':
                    rule,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f2fcf04554db9ea4cdc3a7024322_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authentication')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f2fcf04554db9ea4cdc3a7024322_v3_1_patch_1', _api_response)

    def create(self,
               policy_id,
               identity_source_name=None,
               if_auth_fail=None,
               if_process_fail=None,
               if_user_not_found=None,
               link=None,
               rule=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_network_access_authentication_rule <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authentication_rules.
        NetworkAccessAuthenticationRules.create_network_access_authentication_rule>`_
        """
        return self.create_network_access_authentication_rule(
            policy_id=policy_id,
            identity_source_name=identity_source_name,
            if_auth_fail=if_auth_fail,
            if_process_fail=if_process_fail,
            if_user_not_found=if_user_not_found,
            link=link,
            rule=rule,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def reset_hit_counts_network_access_authentication_rules(self,
                                                             policy_id,
                                                             headers=None,
                                                             **query_parameters):
        """Network Access Reset HitCount for Authentication Rules.

        Args:
            policy_id(basestring): policyId path parameter. Policy
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
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(policy_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
        }

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authentication/reset-hitcount')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cd727fc45ccf8607a744aa71df66_v3_1_patch_1', _api_response)

    def reset_hit_counts_by_id(self,
                               policy_id,
                               headers=None,
                               **query_parameters):
        """Alias for `reset_hit_counts_network_access_authentication_rules <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authentication_rules.
        NetworkAccessAuthenticationRules.reset_hit_counts_network_access_authentication_rules>`_
        """
        return self.reset_hit_counts_network_access_authentication_rules(
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )

    def get_network_access_authentication_rule_by_id(self,
                                                     id,
                                                     policy_id,
                                                     headers=None,
                                                     **query_parameters):
        """Network Access Get rule attributes.

        Args:
            policy_id(basestring): policyId path parameter. Policy
                id.
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
        check_type(policy_id, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
            'id': id,
        }

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authentication/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a588d29d5a527388ee8498f746d1f5_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  policy_id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_network_access_authentication_rule_by_id <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authentication_rules.
        NetworkAccessAuthenticationRules.get_network_access_authentication_rule_by_id>`_
        """
        return self.get_network_access_authentication_rule_by_id(
            id=id,
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )

    def update_network_access_authentication_rule_by_id(self,
                                                        id,
                                                        policy_id,
                                                        identity_source_name=None,
                                                        if_auth_fail=None,
                                                        if_process_fail=None,
                                                        if_user_not_found=None,
                                                        link=None,
                                                        rule=None,
                                                        headers=None,
                                                        payload=None,
                                                        active_validation=True,
                                                        **query_parameters):
        """Network Access Update rule.

        Args:
            identity_source_name(string): Identity source name from
                the identity stores, property of the
                request body.
            if_auth_fail(string): Action to perform when
                authentication fails such as Bad
                credentials, disabled user and so on,
                property of the request body.
            if_process_fail(string): Action to perform when ISE is
                uanble to access the identity database,
                property of the request body.
            if_user_not_found(string): Action to perform when user
                is not found in any of identity stores,
                property of the request body.
            link(object): link, property of the request body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            policy_id(basestring): policyId path parameter. Policy
                id.
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
        check_type(policy_id, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'identitySourceName':
                    identity_source_name,
                'ifAuthFail':
                    if_auth_fail,
                'ifProcessFail':
                    if_process_fail,
                'ifUserNotFound':
                    if_user_not_found,
                'link':
                    link,
                'rule':
                    rule,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_aa4daefaa3b95ecca521188a43eacbd9_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authentication/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_aa4daefaa3b95ecca521188a43eacbd9_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
                     policy_id,
                     identity_source_name=None,
                     if_auth_fail=None,
                     if_process_fail=None,
                     if_user_not_found=None,
                     link=None,
                     rule=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_network_access_authentication_rule_by_id <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authentication_rules.
        NetworkAccessAuthenticationRules.update_network_access_authentication_rule_by_id>`_
        """
        return self.update_network_access_authentication_rule_by_id(
            id=id,
            policy_id=policy_id,
            identity_source_name=identity_source_name,
            if_auth_fail=if_auth_fail,
            if_process_fail=if_process_fail,
            if_user_not_found=if_user_not_found,
            link=link,
            rule=rule,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_network_access_authentication_rule_by_id(self,
                                                        id,
                                                        policy_id,
                                                        headers=None,
                                                        **query_parameters):
        """Network Access Delete rule.

        Args:
            policy_id(basestring): policyId path parameter. Policy
                id.
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
        check_type(policy_id, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
            'id': id,
        }

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authentication/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af104d12b5c5e668af1504feca5c9b1_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     policy_id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_network_access_authentication_rule_by_id <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authentication_rules.
        NetworkAccessAuthenticationRules.delete_network_access_authentication_rule_by_id>`_
        """
        return self.delete_network_access_authentication_rule_by_id(
            id=id,
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )
