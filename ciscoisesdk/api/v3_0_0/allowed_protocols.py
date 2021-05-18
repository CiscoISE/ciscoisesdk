# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine AllowedProtocols API wrapper.

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


class AllowedProtocols(object):
    """Identity Services Engine AllowedProtocols API (version: 3.0.0).

    Wraps the Identity Services Engine AllowedProtocols
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AllowedProtocols
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AllowedProtocols, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_allowed_protocols(self,
                                  page=None,
                                  size=None,
                                  headers=None,
                                  **query_parameters):
        """Get all Allowed Protocols.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
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
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))

        _params = {
            'page':
                page,
            'size':
                size,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/allowedprotocols')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d82fe0f9e4635b74af809beaaf98bd07_v3_0_0', _api_response)

    def get_all_allowed_protocols_generator(self,
                                            page=None,
                                            size=None,
                                            headers=None,
                                            **query_parameters):
        """Get all Allowed Protocols.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.
              + RestResponse: REST response with following properties:
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
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))

        _params = {
            'page':
                page,
            'size':
                size,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/allowedprotocols')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        yield self._object_factory('bpm_d82fe0f9e4635b74af809beaaf98bd07_v3_0_0', _api_response)
        if _api_response.response and _api_response.response.get("SearchResult", {}).get("nextPage", {}).get("href", ""):
            url = _api_response.response.get("SearchResult", {}).get("nextPage", {}).get("href", "")
            _query_params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            _size = _query_params.get('size')
            _page = _query_params.get('page')
            yield from self.get_all_allowed_protocols_generator(headers=headers,
                                                                page=_page,
                                                                size=_size,
                                                                **query_parameters)

    def create_allowed_protocol(self,
                                allow_chap=None,
                                allow_eap_fast=None,
                                allow_eap_md5=None,
                                allow_eap_tls=None,
                                allow_eap_ttls=None,
                                allow_leap=None,
                                allow_ms_chap_v1=None,
                                allow_ms_chap_v2=None,
                                allow_pap_ascii=None,
                                allow_peap=None,
                                allow_preferred_eap_protocol=None,
                                allow_teap=None,
                                allow_weak_ciphers_for_eap=None,
                                description=None,
                                eap_fast=None,
                                eap_tls=None,
                                eap_tls_l_bit=None,
                                eap_ttls=None,
                                name=None,
                                peap=None,
                                preferred_eap_protocol=None,
                                process_host_lookup=None,
                                require_message_auth=None,
                                teap=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Create Allowed Protocols.

        Args:
            allow_chap(boolean): allowChap, property of the request
                body.
            allow_eap_fast(boolean): allowEapFast, property of the
                request body.
            allow_eap_md5(boolean): allowEapMd5, property of the
                request body.
            allow_eap_tls(boolean): allowEapTls, property of the
                request body.
            allow_eap_ttls(boolean): allowEapTtls, property of the
                request body.
            allow_leap(boolean): allowLeap, property of the request
                body.
            allow_ms_chap_v1(boolean): allowMsChapV1, property of
                the request body.
            allow_ms_chap_v2(boolean): allowMsChapV2, property of
                the request body.
            allow_pap_ascii(boolean): allowPapAscii, property of the
                request body.
            allow_peap(boolean): allowPeap, property of the request
                body.
            allow_preferred_eap_protocol(boolean):
                allowPreferredEapProtocol, property of
                the request body.
            allow_teap(boolean): allowTeap, property of the request
                body.
            allow_weak_ciphers_for_eap(boolean):
                allowWeakCiphersForEap, property of the
                request body.
            description(string): description, property of the
                request body.
            eap_fast(object): eapFast, property of the request body.
            eap_tls(object): eapTls, property of the request body.
            eap_tls_l_bit(boolean): eapTlsLBit, property of the
                request body.
            eap_ttls(object): eapTtls, property of the request body.
            name(string): name, property of the request body.
            peap(object): peap, property of the request body.
            preferred_eap_protocol(string): preferredEapProtocol,
                property of the request body.
            process_host_lookup(boolean): processHostLookup,
                property of the request body.
            require_message_auth(boolean): requireMessageAuth,
                property of the request body.
            teap(object): teap, property of the request body.
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
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

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
            _tmp_payload = {
                'name':
                    name,
                'description':
                    description,
                'eapTls':
                    eap_tls,
                'peap':
                    peap,
                'eapFast':
                    eap_fast,
                'eapTtls':
                    eap_ttls,
                'teap':
                    teap,
                'processHostLookup':
                    process_host_lookup,
                'allowPapAscii':
                    allow_pap_ascii,
                'allowChap':
                    allow_chap,
                'allowMsChapV1':
                    allow_ms_chap_v1,
                'allowMsChapV2':
                    allow_ms_chap_v2,
                'allowEapMd5':
                    allow_eap_md5,
                'allowLeap':
                    allow_leap,
                'allowEapTls':
                    allow_eap_tls,
                'allowEapTtls':
                    allow_eap_ttls,
                'allowEapFast':
                    allow_eap_fast,
                'allowPeap':
                    allow_peap,
                'allowTeap':
                    allow_teap,
                'allowPreferredEapProtocol':
                    allow_preferred_eap_protocol,
                'preferredEapProtocol':
                    preferred_eap_protocol,
                'eapTlsLBit':
                    eap_tls_l_bit,
                'allowWeakCiphersForEap':
                    allow_weak_ciphers_for_eap,
                'requireMessageAuth':
                    require_message_auth,
            }
            _payload = {
                'AllowedProtocols': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b40ad23ab0a5a7b8adade320c8912e7_v3_0_0')\
                .validate(_payload)

        e_url = ('/ers/config/allowedprotocols')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b40ad23ab0a5a7b8adade320c8912e7_v3_0_0', _api_response)

    def get_allowed_protocol_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """Get Allowed Protocols by Id.

        Args:
            id(basestring): id path parameter.
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
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

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

        e_url = ('/ers/config/allowedprotocols/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e3ddfddd45e299f14ed194926f8de_v3_0_0', _api_response)

    def update_allowed_protocol_by_id(self,
                                      id,
                                      allow_chap=None,
                                      allow_eap_fast=None,
                                      allow_eap_md5=None,
                                      allow_eap_tls=None,
                                      allow_eap_ttls=None,
                                      allow_leap=None,
                                      allow_ms_chap_v1=None,
                                      allow_ms_chap_v2=None,
                                      allow_pap_ascii=None,
                                      allow_peap=None,
                                      allow_preferred_eap_protocol=None,
                                      allow_teap=None,
                                      allow_weak_ciphers_for_eap=None,
                                      description=None,
                                      eap_fast=None,
                                      eap_tls=None,
                                      eap_tls_l_bit=None,
                                      eap_ttls=None,
                                      name=None,
                                      peap=None,
                                      preferred_eap_protocol=None,
                                      process_host_lookup=None,
                                      require_message_auth=None,
                                      teap=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Update Allowed Protocols by Id.

        Args:
            allow_chap(boolean): allowChap, property of the request
                body.
            allow_eap_fast(boolean): allowEapFast, property of the
                request body.
            allow_eap_md5(boolean): allowEapMd5, property of the
                request body.
            allow_eap_tls(boolean): allowEapTls, property of the
                request body.
            allow_eap_ttls(boolean): allowEapTtls, property of the
                request body.
            allow_leap(boolean): allowLeap, property of the request
                body.
            allow_ms_chap_v1(boolean): allowMsChapV1, property of
                the request body.
            allow_ms_chap_v2(boolean): allowMsChapV2, property of
                the request body.
            allow_pap_ascii(boolean): allowPapAscii, property of the
                request body.
            allow_peap(boolean): allowPeap, property of the request
                body.
            allow_preferred_eap_protocol(boolean):
                allowPreferredEapProtocol, property of
                the request body.
            allow_teap(boolean): allowTeap, property of the request
                body.
            allow_weak_ciphers_for_eap(boolean):
                allowWeakCiphersForEap, property of the
                request body.
            description(string): description, property of the
                request body.
            eap_fast(object): eapFast, property of the request body.
            eap_tls(object): eapTls, property of the request body.
            eap_tls_l_bit(boolean): eapTlsLBit, property of the
                request body.
            eap_ttls(object): eapTtls, property of the request body.
            name(string): name, property of the request body.
            peap(object): peap, property of the request body.
            preferred_eap_protocol(string): preferredEapProtocol,
                property of the request body.
            process_host_lookup(boolean): processHostLookup,
                property of the request body.
            require_message_auth(boolean): requireMessageAuth,
                property of the request body.
            teap(object): teap, property of the request body.
            id(basestring): id path parameter.
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
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

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
            _tmp_payload = {
                'name':
                    name,
                'description':
                    description,
                'eapTls':
                    eap_tls,
                'peap':
                    peap,
                'eapFast':
                    eap_fast,
                'eapTtls':
                    eap_ttls,
                'teap':
                    teap,
                'processHostLookup':
                    process_host_lookup,
                'allowPapAscii':
                    allow_pap_ascii,
                'allowChap':
                    allow_chap,
                'allowMsChapV1':
                    allow_ms_chap_v1,
                'allowMsChapV2':
                    allow_ms_chap_v2,
                'allowEapMd5':
                    allow_eap_md5,
                'allowLeap':
                    allow_leap,
                'allowEapTls':
                    allow_eap_tls,
                'allowEapTtls':
                    allow_eap_ttls,
                'allowEapFast':
                    allow_eap_fast,
                'allowPeap':
                    allow_peap,
                'allowTeap':
                    allow_teap,
                'allowPreferredEapProtocol':
                    allow_preferred_eap_protocol,
                'preferredEapProtocol':
                    preferred_eap_protocol,
                'eapTlsLBit':
                    eap_tls_l_bit,
                'allowWeakCiphersForEap':
                    allow_weak_ciphers_for_eap,
                'requireMessageAuth':
                    require_message_auth,
            }
            _payload = {
                'AllowedProtocols': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a0b312f70257b1bfa90d0260f0c971_v3_0_0')\
                .validate(_payload)

        e_url = ('/ers/config/allowedprotocols/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a0b312f70257b1bfa90d0260f0c971_v3_0_0', _api_response)

    def delete_allowed_protocol_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """Delete Allowed Protocols by Id.

        Args:
            id(basestring): id path parameter.
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
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

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

        e_url = ('/ers/config/allowedprotocols/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6cbd2c420785cfcbdecc3495bca8af4_v3_0_0', _api_response)

    def get_allowed_protocol_by_name(self,
                                     name,
                                     headers=None,
                                     **query_parameters):
        """Get Allowed Protocols by name.

        Args:
            name(basestring): name path parameter.
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
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

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

        e_url = ('/ers/config/allowedprotocols/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ac8c8cb9b5007a1e1a6434a20a881_v3_0_0', _api_response)
