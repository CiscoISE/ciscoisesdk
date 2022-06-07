# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Network Access - Authorization Rules API wrapper.

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


class NetworkAccessAuthorizationRules(object):
    """Identity Services Engine Network Access - Authorization Rules API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine Network Access - Authorization Rules
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkAccessAuthorizationRules
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkAccessAuthorizationRules, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_access_authorization_rules(self,
                                               policy_id,
                                               headers=None,
                                               **query_parameters):
        """Network Access Get authorization rules.

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
                 + 'set/{policyId}/authorization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e623dba049b5569c83e13ccf4360e369_v3_1_patch_1', _api_response)

    def get_all(self,
                policy_id,
                headers=None,
                **query_parameters):
        """Alias for `get_network_access_authorization_rules <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authorization_rules.
        NetworkAccessAuthorizationRules.get_network_access_authorization_rules>`_
        """
        return self.get_network_access_authorization_rules(
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )

    def create_network_access_authorization_rule(self,
                                                 policy_id,
                                                 link=None,
                                                 profile=None,
                                                 rule=None,
                                                 security_group=None,
                                                 headers=None,
                                                 payload=None,
                                                 active_validation=True,
                                                 **query_parameters):
        """Network Access Create authorization rule:     Rule must include
        name and condition.     Condition has hierarchical
        structure which define a set of conditions for which
        authoriztion policy rule could be match.     Condition
        can be either reference to a stored Library condition,
        using model  ConditionReference    or dynamically built
        conditions which are not stored in the conditions
        Library, using models  ConditionAttributes,
        ConditionAndBlock, ConditionOrBlock .    .

        Args:
            link(object): link, property of the request body.
            profile(list): The authorization profile/s, property of
                the request body (list of strings).
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            security_group(string): Security group used in
                authorization policies, property of the
                request body.
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
                'link':
                    link,
                'profile':
                    profile,
                'rule':
                    rule,
                'securityGroup':
                    security_group,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eca5db5147b1e3b35a032ced4b_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authorization')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_eca5db5147b1e3b35a032ced4b_v3_1_patch_1', _api_response)

    def create(self,
               policy_id,
               link=None,
               profile=None,
               rule=None,
               security_group=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_network_access_authorization_rule <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authorization_rules.
        NetworkAccessAuthorizationRules.create_network_access_authorization_rule>`_
        """
        return self.create_network_access_authorization_rule(
            policy_id=policy_id,
            link=link,
            profile=profile,
            rule=rule,
            security_group=security_group,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def reset_hit_counts_network_access_authorization_rules(self,
                                                            policy_id,
                                                            headers=None,
                                                            **query_parameters):
        """Network Access Reset HitCount for Authorization Rules.

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
                 + 'set/{policyId}/authorization/reset-hitcount')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c860146231095e85839639db33c93cfe_v3_1_patch_1', _api_response)

    def reset_hit_counts_by_id(self,
                               policy_id,
                               headers=None,
                               **query_parameters):
        """Alias for `reset_hit_counts_network_access_authorization_rules <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authorization_rules.
        NetworkAccessAuthorizationRules.reset_hit_counts_network_access_authorization_rules>`_
        """
        return self.reset_hit_counts_network_access_authorization_rules(
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )

    def get_network_access_authorization_rule_by_id(self,
                                                    id,
                                                    policy_id,
                                                    headers=None,
                                                    **query_parameters):
        """Network Access Get authorization rule attributes.

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
                 + 'set/{policyId}/authorization/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fcf7754d5b45523a8227d37c476a1880_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  policy_id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_network_access_authorization_rule_by_id <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authorization_rules.
        NetworkAccessAuthorizationRules.get_network_access_authorization_rule_by_id>`_
        """
        return self.get_network_access_authorization_rule_by_id(
            id=id,
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )

    def update_network_access_authorization_rule_by_id(self,
                                                       id,
                                                       policy_id,
                                                       link=None,
                                                       profile=None,
                                                       rule=None,
                                                       security_group=None,
                                                       headers=None,
                                                       payload=None,
                                                       active_validation=True,
                                                       **query_parameters):
        """Network Access Update authorization rule.

        Args:
            link(object): link, property of the request body.
            profile(list): The authorization profile/s, property of
                the request body (list of strings).
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            security_group(string): Security group used in
                authorization policies, property of the
                request body.
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
                'link':
                    link,
                'profile':
                    profile,
                'rule':
                    rule,
                'securityGroup':
                    security_group,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fd9e7e03a6056d1b6e9705e3096d946_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/policy/network-access/policy-'
                 + 'set/{policyId}/authorization/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_fd9e7e03a6056d1b6e9705e3096d946_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
                     policy_id,
                     link=None,
                     profile=None,
                     rule=None,
                     security_group=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_network_access_authorization_rule_by_id <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authorization_rules.
        NetworkAccessAuthorizationRules.update_network_access_authorization_rule_by_id>`_
        """
        return self.update_network_access_authorization_rule_by_id(
            id=id,
            policy_id=policy_id,
            link=link,
            profile=profile,
            rule=rule,
            security_group=security_group,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_network_access_authorization_rule_by_id(self,
                                                       id,
                                                       policy_id,
                                                       headers=None,
                                                       **query_parameters):
        """Network Access Delete authorization rule.

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
                 + 'set/{policyId}/authorization/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dedf09f59e754c6ae5212d43b1c8fb2_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     policy_id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_network_access_authorization_rule_by_id <#ciscoisesdk.
        api.v3_1_patch_1.network_access_authorization_rules.
        NetworkAccessAuthorizationRules.delete_network_access_authorization_rule_by_id>`_
        """
        return self.delete_network_access_authorization_rule_by_id(
            id=id,
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )
