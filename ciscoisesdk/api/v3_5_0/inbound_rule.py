# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Inbound Rule API wrapper.

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


class InboundRule(object):
    """Identity Services Engine Inbound Rule API (version: 3.5.0).

    Wraps the Identity Services Engine Inbound Rule
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new InboundRule
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(InboundRule, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_ingress_filter_list(self,
                                headers=None,
                                **query_parameters):
        """Inbound Rule ISE uses ACI policy objects as conditions to
        determine which context goes to which SXP domain.

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

        e_url = ('/api/v1/trustsec/inbound-rule')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cf3f20d6235078a72f754f49131a5a_v3_5_0', _api_response)

    def create_ingress_filter_configuration(self,
                                            mappings_count=None,
                                            rule=None,
                                            sxp_domains=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """Inbound Rule Create Inbound Rule:     Filter configuration must
        include name and condition.     Condition has
        hierarchical structure which define a set of conditions
        for which authoriztion policy rule could be match.
        Condition can be either reference to a stored Library
        condition, using model  ConditionReference    or
        dynamically built conditions which are not stored in the
        conditions Library, using models  ConditionAttributes,
        ConditionAndBlock, ConditionOrBlock .    .

        Args:
            mappings_count(integer): mappingsCount, property of the
                request body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            sxp_domains(list): Sxp Domains used in the inbound rule
                destination configurations, property of
                the request body (list of strings).
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
                'rule':
                    rule,
                'sxpDomains':
                    sxp_domains,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e84da9af36ab57bf8c3e4ae68be9f6c0_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/inbound-rule')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e84da9af36ab57bf8c3e4ae68be9f6c0_v3_5_0', _api_response)

    def get_inbound_rule_filter_preview(self,
                                        cdp_ingress_filter=None,
                                        page_number=None,
                                        page_size=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **query_parameters):
        """Inbound Rule Preview Inbound Rule:     Filter configuration must
        include name and condition.     Condition has
        hierarchical structure which define a set of conditions
        for which authoriztion policy rule could be match.
        Condition can be either reference to a stored Library
        condition, using model  ConditionReference    or
        dynamically built conditions which are not stored in the
        conditions Library, using models  ConditionAttributes,
        ConditionAndBlock, ConditionOrBlock .    .

        Args:
            page_number(integer): Page Number, property of the
                request body.
            page_size(integer): Page Size, property of the request
                body.
            cdp_ingress_filter(object): Inbound Rule details,
                property of the request body.
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
                'cdpIngressFilter':
                    cdp_ingress_filter,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e1576d5d61aedcc49b16304e0c_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/inbound-rule/preview')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e1576d5d61aedcc49b16304e0c_v3_5_0', _api_response)

    def get_inbound_rule_filter_preview_by_id(self,
                                              filter_id,
                                              cdp_ingress_filter=None,
                                              page_number=None,
                                              page_size=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **query_parameters):
        """Inbound Rule Preview Inbound Rule:     Filter configuration must
        include name and condition.     Condition has
        hierarchical structure which define a set of conditions
        for which authoriztion policy rule could be match.
        Condition can be either reference to a stored Library
        condition, using model  ConditionReference    or
        dynamically built conditions which are not stored in the
        conditions Library, using models  ConditionAttributes,
        ConditionAndBlock, ConditionOrBlock .    .

        Args:
            page_number(integer): Page Number, property of the
                request body.
            page_size(integer): Page Size, property of the request
                body.
            cdp_ingress_filter(object): Inbound Rule details,
                property of the request body.
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
                'PageNumber':
                    page_number,
                'PageSize':
                    page_size,
                'cdpIngressFilter':
                    cdp_ingress_filter,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fa01fb781615465af70aa8b3d5a0bfb_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/inbound-rule/preview/{filterId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_fa01fb781615465af70aa8b3d5a0bfb_v3_5_0', _api_response)

    def get_ingress_sxp_domains(self,
                                application_profile=None,
                                connection_name=None,
                                epg=None,
                                learned_by=None,
                                learned_from=None,
                                mode=None,
                                psns_involved=None,
                                selected_epg=None,
                                sgt=None,
                                sxp_domain=None,
                                tenant=None,
                                vn=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Get SXP Domains list for SGTs data.

        Args:
            application_profile(string): applicationProfile,
                property of the request body.
            connection_name(list): Connection name to be used to
                filter out the metadata, property of the
                request body (list of strings).
            epg(string): epg, property of the request body.
            learned_by(string): learnedBy, property of the request
                body.
            learned_from(string): learnedFrom, property of the
                request body.
            mode(string): mode, property of the request body.
            psns_involved(string): psnsInvolved, property of the
                request body.
            selected_epg(boolean): selectedEpg, property of the
                request body.
            sgt(list): sgt, property of the request body (list of
                strings).
            sxp_domain(string): sxpDomain, property of the request
                body.
            tenant(string): tenant, property of the request body.
            vn(string): vn, property of the request body.
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
                'applicationProfile':
                    application_profile,
                'connectionName':
                    connection_name,
                'epg':
                    epg,
                'learnedBy':
                    learned_by,
                'learnedFrom':
                    learned_from,
                'mode':
                    mode,
                'psnsInvolved':
                    psns_involved,
                'selectedEpg':
                    selected_epg,
                'sgt':
                    sgt,
                'sxpDomain':
                    sxp_domain,
                'tenant':
                    tenant,
                'vn':
                    vn,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_bcb9c0db457269208d40b7bc652b7_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/inbound-rule/sxp-domain')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_bcb9c0db457269208d40b7bc652b7_v3_5_0', _api_response)

    def get_ingress_filter_by_id(self,
                                 filter_id,
                                 headers=None,
                                 **query_parameters):
        """Inbound Rule Get Inbound Ruler attributes.

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

        e_url = ('/api/v1/trustsec/inbound-rule/{filterId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a04c9a11e589f99a5456c7228772e_v3_5_0', _api_response)

    def update_ingress_filter_by_id(self,
                                    filter_id,
                                    mappings_count=None,
                                    rule=None,
                                    sxp_domains=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """Inbound Rule Update Inbound Rule.

        Args:
            mappings_count(integer): mappingsCount, property of the
                request body.
            rule(object): Common attributes in rule
                authentication/authorization, property
                of the request body.
            sxp_domains(list): Sxp Domains used in the inbound rule
                destination configurations, property of
                the request body (list of strings).
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
                'rule':
                    rule,
                'sxpDomains':
                    sxp_domains,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_db2f29b2805ea387ac86e05642e69a_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/inbound-rule/{filterId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_db2f29b2805ea387ac86e05642e69a_v3_5_0', _api_response)

    def delete_ingress_filter_by_id(self,
                                    filter_id,
                                    headers=None,
                                    **query_parameters):
        """Inbound Rule Delete Inbound Rule.

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

        e_url = ('/api/v1/trustsec/inbound-rule/{filterId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d9909ae4b04751458eaa7090fa048975_v3_5_0', _api_response)
