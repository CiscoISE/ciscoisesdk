# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Classification rule API wrapper.

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


class Classificationrule(object):
    """Identity Services Engine Classification rule API (version: 3.5.0).

    Wraps the Identity Services Engine Classification rule
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Classificationrule
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Classificationrule, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_classification_rule_list(self,
                                     headers=None,
                                     **query_parameters):
        """Classification rule  ISE uses ACI policy objects as conditions
        to determine which context goes to which Primary Sgt and
        Secondary Sgts.

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

        e_url = ('/api/v1/trustsec/classification-policy')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cbbd6a8b24250a6b4cd0224469a474f_v3_5_0', _api_response)

    def create_classification_rule_configuration(self,
                                                 mappings_count=None,
                                                 primary_sgt=None,
                                                 rule=None,
                                                 secondary_sgts=None,
                                                 headers=None,
                                                 payload=None,
                                                 active_validation=True,
                                                 **query_parameters):
        """Classification rule  Create Classification rule :     Filter
        configuration must include name and condition.
        Condition has hierarchical structure which define a set
        of conditions for which authoriztion policy rule could
        be match.     Condition can be either reference to a
        stored Library condition, using model
        ConditionReference    or dynamically built conditions
        which are not stored in the conditions Library, using
        models  ConditionAttributes, ConditionAndBlock,
        ConditionOrBlock .    .

        Args:
            mappings_count(integer): mappingsCount, property of the
                request body.
            primary_sgt(string): primarySgt, property of the request
                body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            secondary_sgts(list): Secondary Sgts used in the
                Classification Rule destination
                configurations, property of the request
                body (list of strings).
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
                'mappingsCount':
                    mappings_count,
                'primarySgt':
                    primary_sgt,
                'rule':
                    rule,
                'secondarySgts':
                    secondary_sgts,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b3a8183dd45ea19a4857e14fe356ab_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/classification-policy')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b3a8183dd45ea19a4857e14fe356ab_v3_5_0', _api_response)

    def get_classification_rule_filter_preview(self,
                                               cdp_classification_rule=None,
                                               page_number=None,
                                               page_size=None,
                                               headers=None,
                                               payload=None,
                                               active_validation=True,
                                               **query_parameters):
        """Classification Policy Preview Classification Policy:     Filter
        configuration must include name and condition.
        Condition has hierarchical structure which define a set
        of conditions for which authoriztion policy rule could
        be match.     Condition can be either reference to a
        stored Library condition, using model
        ConditionReference    or dynamically built conditions
        which are not stored in the conditions Library, using
        models  ConditionAttributes, ConditionAndBlock,
        ConditionOrBlock .    .

        Args:
            page_number(integer): Page Number, property of the
                request body.
            page_size(integer): Page Size, property of the request
                body.
            cdp_classification_rule(object): Classification Rule
                details, property of the request body.
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
                'PageNumber':
                    page_number,
                'PageSize':
                    page_size,
                'cdpClassificationRule':
                    cdp_classification_rule,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f8a6116d2050518da89ba699dba15c5e_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/classification-policy/preview')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f8a6116d2050518da89ba699dba15c5e_v3_5_0', _api_response)

    def re_rank_classification_rules(self,
                                     classification_rule_rank_requests=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Classification rule  Re-rank Classification rules.     Provide
        list of existing Workload Classification Policies names,
        id, and newly desired rank    .

        Args:
            classification_rule_rank_requests(list):
                classificationRuleRankRequests, property
                of the request body (list of objects).
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
                'classificationRuleRankRequests':
                    classification_rule_rank_requests,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c7f3352e2b5ba2f0467835c8d_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/classification-policy/re-rank')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c7f3352e2b5ba2f0467835c8d_v3_5_0', _api_response)

    def get_classification_rule_by_id(self,
                                      filter_id,
                                      headers=None,
                                      **query_parameters):
        """Classification rule  Get Classification rule  attributes.

        Args:
            filter_id(str): filterId path parameter. Inbound /
                Outbound Rule id.
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
        check_type(filter_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'filterId': filter_id,
        }

        e_url = ('/api/v1/trustsec/classification-policy/{filterId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ff95abf7721528693f4f2c8ba9c3f46_v3_5_0', _api_response)

    def update_classification_rule_by_id(self,
                                         filter_id,
                                         mappings_count=None,
                                         primary_sgt=None,
                                         rule=None,
                                         secondary_sgts=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """Classification rule  Update Classification rule.

        Args:
            mappings_count(integer): mappingsCount, property of the
                request body.
            primary_sgt(string): primarySgt, property of the request
                body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            secondary_sgts(list): Secondary Sgts used in the
                Classification Rule destination
                configurations, property of the request
                body (list of strings).
            filter_id(str): filterId path parameter. Inbound /
                Outbound Rule id.
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
        check_type(filter_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'filterId': filter_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'mappingsCount':
                    mappings_count,
                'primarySgt':
                    primary_sgt,
                'rule':
                    rule,
                'secondarySgts':
                    secondary_sgts,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eb5bfbb2e9f75684b074f0cd62c5eeb9_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/classification-policy/{filterId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_eb5bfbb2e9f75684b074f0cd62c5eeb9_v3_5_0', _api_response)

    def delete_classification_rule_by_id(self,
                                         filter_id,
                                         headers=None,
                                         **query_parameters):
        """Classification rule  Delete Classification rule .

        Args:
            filter_id(str): filterId path parameter. Inbound /
                Outbound Rule id.
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
        check_type(filter_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'filterId': filter_id,
        }

        e_url = ('/api/v1/trustsec/classification-policy/{filterId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a074d2116f05cb097bb032f0a32c2da_v3_5_0', _api_response)
