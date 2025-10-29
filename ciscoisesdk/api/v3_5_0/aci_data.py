# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine ACI Data API wrapper.

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


class AciData(object):
    """Identity Services Engine ACI Data API (version: 3.5.0).

    Wraps the Identity Services Engine ACI Data
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AciData
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AciData, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_application_profiles_prefetch(self,
                                          domain=None,
                                          hostname=None,
                                          id=None,
                                          name=None,
                                          password=None,
                                          username=None,
                                          validate_certificate=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **query_parameters):
        """Get application profile list from ACI.

        Args:
            domain(string): Auth Domain, property of the request
                body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): ID if connection is already created,
                property of the request body.
            name(string): ACI name, property of the request body.
            password(string): Password, property of the request
                body.
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
                'domain':
                    domain,
                'hostname':
                    hostname,
                'id':
                    id,
                'name':
                    name,
                'password':
                    password,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_db75c59d5d0287aa025ad4eff0d4_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/application-'
                 + 'profile/fetch')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_db75c59d5d0287aa025ad4eff0d4_v3_5_0', _api_response)

    def get_epgs_prefetch(self,
                          domain=None,
                          hostname=None,
                          id=None,
                          name=None,
                          name_conversion=None,
                          password=None,
                          username=None,
                          validate_certificate=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """Get EPG list from ACI.

        Args:
            domain(string): Auth Domain, property of the request
                body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): ID if connection is already created,
                property of the request body.
            name(string): ACI name, property of the request body.
            name_conversion(object): Name conversion configuration,
                property of the request body.
            password(string): Password, property of the request
                body.
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
                'domain':
                    domain,
                'hostname':
                    hostname,
                'id':
                    id,
                'name':
                    name,
                'nameConversion':
                    name_conversion,
                'password':
                    password,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fd7d52bfee55ea9906743bfa9d23abb_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/epg/fetch')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_fd7d52bfee55ea9906743bfa9d23abb_v3_5_0', _api_response)

    def get_application_profiles_filter(self,
                                        ap=None,
                                        connection_name=None,
                                        epg=None,
                                        sgt_name=None,
                                        sxp_domain=None,
                                        tn=None,
                                        vn=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **query_parameters):
        """Get application profiles from selected EPGs with filters.

        Args:
            ap(list): ap, property of the request body (list of
                strings).
            connection_name(list): connectionName, property of the
                request body (list of strings).
            epg(list): epg, property of the request body (list of
                strings).
            sgt_name(list): sgtName, property of the request body
                (list of strings).
            sxp_domain(list): sxpDomain, property of the request
                body (list of strings).
            tn(list): tn, property of the request body (list of
                strings).
            vn(list): vn, property of the request body (list of
                strings).
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
                'ap':
                    ap,
                'connectionName':
                    connection_name,
                'epg':
                    epg,
                'sgtName':
                    sgt_name,
                'sxpDomain':
                    sxp_domain,
                'tn':
                    tn,
                'vn':
                    vn,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d4de9ab855aa5d1b91a320bb3c915e0f_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/selected-'
                 + 'epg/application-profile/get')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d4de9ab855aa5d1b91a320bb3c915e0f_v3_5_0', _api_response)

    def get_epgs_filter(self,
                        ap=None,
                        connection_name=None,
                        epg=None,
                        sgt_name=None,
                        sxp_domain=None,
                        tn=None,
                        vn=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **query_parameters):
        """Get EPGs from selected EPGs with filters.

        Args:
            ap(list): ap, property of the request body (list of
                strings).
            connection_name(list): connectionName, property of the
                request body (list of strings).
            epg(list): epg, property of the request body (list of
                strings).
            sgt_name(list): sgtName, property of the request body
                (list of strings).
            sxp_domain(list): sxpDomain, property of the request
                body (list of strings).
            tn(list): tn, property of the request body (list of
                strings).
            vn(list): vn, property of the request body (list of
                strings).
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
                'ap':
                    ap,
                'connectionName':
                    connection_name,
                'epg':
                    epg,
                'sgtName':
                    sgt_name,
                'sxpDomain':
                    sxp_domain,
                'tn':
                    tn,
                'vn':
                    vn,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b842ca9a8f5bea86df8ea64781bf15_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/selected-'
                 + 'epg/epg/get')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b842ca9a8f5bea86df8ea64781bf15_v3_5_0', _api_response)

    def get_security_groups_filter(self,
                                   ap=None,
                                   connection_name=None,
                                   epg=None,
                                   sgt_name=None,
                                   sxp_domain=None,
                                   tn=None,
                                   vn=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Get EPGs from selected EPGs with filters.

        Args:
            ap(list): ap, property of the request body (list of
                strings).
            connection_name(list): connectionName, property of the
                request body (list of strings).
            epg(list): epg, property of the request body (list of
                strings).
            sgt_name(list): sgtName, property of the request body
                (list of strings).
            sxp_domain(list): sxpDomain, property of the request
                body (list of strings).
            tn(list): tn, property of the request body (list of
                strings).
            vn(list): vn, property of the request body (list of
                strings).
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
                'ap':
                    ap,
                'connectionName':
                    connection_name,
                'epg':
                    epg,
                'sgtName':
                    sgt_name,
                'sxpDomain':
                    sxp_domain,
                'tn':
                    tn,
                'vn':
                    vn,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d6862b2e55e5012a882b528487a9092_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/selected-'
                 + 'epg/security-group/get')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d6862b2e55e5012a882b528487a9092_v3_5_0', _api_response)

    def get_tenants_filter(self,
                           ap=None,
                           connection_name=None,
                           epg=None,
                           sgt_name=None,
                           sxp_domain=None,
                           tn=None,
                           vn=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """Get tenants from selected EPGs with filters.

        Args:
            ap(list): ap, property of the request body (list of
                strings).
            connection_name(list): connectionName, property of the
                request body (list of strings).
            epg(list): epg, property of the request body (list of
                strings).
            sgt_name(list): sgtName, property of the request body
                (list of strings).
            sxp_domain(list): sxpDomain, property of the request
                body (list of strings).
            tn(list): tn, property of the request body (list of
                strings).
            vn(list): vn, property of the request body (list of
                strings).
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
                'ap':
                    ap,
                'connectionName':
                    connection_name,
                'epg':
                    epg,
                'sgtName':
                    sgt_name,
                'sxpDomain':
                    sxp_domain,
                'tn':
                    tn,
                'vn':
                    vn,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e2e6459313865bd4b40b2eb2fc693eae_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/selected-'
                 + 'epg/tenant/get')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e2e6459313865bd4b40b2eb2fc693eae_v3_5_0', _api_response)

    def get_virtual_networks_filter(self,
                                    ap=None,
                                    connection_name=None,
                                    epg=None,
                                    sgt_name=None,
                                    sxp_domain=None,
                                    tn=None,
                                    vn=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """Get virtual networks from selected EPGs with filters.

        Args:
            ap(list): ap, property of the request body (list of
                strings).
            connection_name(list): connectionName, property of the
                request body (list of strings).
            epg(list): epg, property of the request body (list of
                strings).
            sgt_name(list): sgtName, property of the request body
                (list of strings).
            sxp_domain(list): sxpDomain, property of the request
                body (list of strings).
            tn(list): tn, property of the request body (list of
                strings).
            vn(list): vn, property of the request body (list of
                strings).
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
                'ap':
                    ap,
                'connectionName':
                    connection_name,
                'epg':
                    epg,
                'sgtName':
                    sgt_name,
                'sxpDomain':
                    sxp_domain,
                'tn':
                    tn,
                'vn':
                    vn,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d7d557f336c581188d1a0e404387a08_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/selected-'
                 + 'epg/virtual-network/get')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d7d557f336c581188d1a0e404387a08_v3_5_0', _api_response)

    def get_tenants_prefetch(self,
                             domain=None,
                             hostname=None,
                             id=None,
                             name=None,
                             password=None,
                             username=None,
                             validate_certificate=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """Get tenant list from ACI.

        Args:
            domain(string): Auth Domain, property of the request
                body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): ID if connection is already created,
                property of the request body.
            name(string): ACI name, property of the request body.
            password(string): Password, property of the request
                body.
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
                'domain':
                    domain,
                'hostname':
                    hostname,
                'id':
                    id,
                'name':
                    name,
                'password':
                    password,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b5677aed60f956c8b944b1decf74b1af_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/tenant/fetch')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b5677aed60f956c8b944b1decf74b1af_v3_5_0', _api_response)

    def get_vns_prefetch(self,
                         domain=None,
                         hostname=None,
                         id=None,
                         name=None,
                         password=None,
                         username=None,
                         validate_certificate=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **query_parameters):
        """Get VN list from ACI.

        Args:
            domain(string): Auth Domain, property of the request
                body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): ID if connection is already created,
                property of the request body.
            name(string): ACI name, property of the request body.
            password(string): Password, property of the request
                body.
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
                'domain':
                    domain,
                'hostname':
                    hostname,
                'id':
                    id,
                'name':
                    name,
                'password':
                    password,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ebb9da748475a76b5ca7c822b441f48_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/virtual-'
                 + 'network/fetch')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ebb9da748475a76b5ca7c822b441f48_v3_5_0', _api_response)

    def get_aci_connection_l3out(self,
                                 connection_id,
                                 headers=None,
                                 **query_parameters):
        """Get l3Out from ACI connection.

        Args:
            connection_id(str): connectionId path parameter. Unique
                id for ACI Connection.
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
        check_type(connection_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectionId': connection_id,
        }

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/{connectionId}/l3out')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ba151a993da55bca8e6476f194943dae_v3_5_0', _api_response)
