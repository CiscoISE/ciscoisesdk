# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine allowedprotocols API wrapper.

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


class Allowedprotocols(object):
    """Identity Services Engine allowedprotocols API (version: 3.5.0).

    Wraps the Identity Services Engine allowedprotocols
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Allowedprotocols
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Allowedprotocols, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_allowedprotocols(self,
                             page=None,
                             size=None,
                             headers=None,
                             **query_parameters):
        """Get-All.

        Args:
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))

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

        e_url = ('/ers/config/allowedprotocols/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e1eed4bdb852aba52564401ac296b1_v3_5_0', _api_response)

    def get_allowedprotocols_generator(self,
                                       page=None,
                                       size=None,
                                       headers=None,
                                       **query_parameters):
        """Get-All.

        Args:
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.

              + RestResponse: REST response with following properties:

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

        yield from get_next_page(
            self.get_allowedprotocols, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_allowedprotocols(self,
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
                                display_additional_tls_params=None,
                                eap_fast=None,
                                eap_tls=None,
                                eap_tls_l_bit=None,
                                eap_ttls=None,
                                five_g=None,
                                id=None,
                                name=None,
                                peap=None,
                                preferred_eap_protocol=None,
                                process_host_lookup=None,
                                require_message_auth=None,
                                rsa_pss=None,
                                teap=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Create.

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
            description(string): Description, property of the
                request body.
            display_additional_tls_params(boolean):
                displayAdditionalTLSParams, property of
                the request body.
            eap_fast(object): eapFast, property of the request body.
            eap_tls(object): eapTls, property of the request body.
            eap_tls_l_bit(boolean): eapTlsLBit, property of the
                request body.
            eap_ttls(object): eapTtls, property of the request body.
            five_g(boolean): fiveG, property of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            peap(object): peap, property of the request body.
            preferred_eap_protocol(string): The preferredEapProtocol
                is required only if
                allowPreferredEapProtocol is true,
                otherwise it must be ignored. Allowed
                Values: EAP_FAST, PEAP, LEAP, EAP_MD5,
                EAP_TLS, EAP_TTLS, TEAP, property of the
                request body.
            process_host_lookup(boolean): processHostLookup,
                property of the request body.
            require_message_auth(boolean): requireMessageAuth,
                property of the request body.
            rsa_pss(boolean): rsaPss, property of the request body.
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
            pass

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
            _tmp_payload = {
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
                'eapTlsLBit':
                    eap_tls_l_bit,
                'allowWeakCiphersForEap':
                    allow_weak_ciphers_for_eap,
                'fiveG':
                    five_g,
                'rsaPss':
                    rsa_pss,
                'displayAdditionalTLSParams':
                    display_additional_tls_params,
                'requireMessageAuth':
                    require_message_auth,
                'preferredEapProtocol':
                    preferred_eap_protocol,
                'eapTls':
                    eap_tls,
                'peap':
                    peap,
                'eapTtls':
                    eap_ttls,
                'eapFast':
                    eap_fast,
                'teap':
                    teap,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'AllowedProtocols': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a4b5e3a38d175b5794e3d3f625351fe9_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/allowedprotocols/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a4b5e3a38d175b5794e3d3f625351fe9_v3_5_0', _api_response)

    def get_allowedprotocols_name_by_name(self,
                                          name,
                                          headers=None,
                                          **query_parameters):
        """Get-By-Name.

        Args:
            name(str): name path parameter.
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
            pass

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

        e_url = ('/ers/config/allowedprotocols/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ac8c8cb9b5007a1e1a6434a20a881_v3_5_0', _api_response)

    def get_allowedprotocols_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """Get-By-Id.

        Args:
            id(str): id path parameter.
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
            pass

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

        e_url = ('/ers/config/allowedprotocols/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e3ddfddd45e299f14ed194926f8de_v3_5_0', _api_response)

    def update_allowedprotocols_by_id(self,
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
                                      display_additional_tls_params=None,
                                      eap_fast=None,
                                      eap_tls=None,
                                      eap_tls_l_bit=None,
                                      eap_ttls=None,
                                      five_g=None,
                                      name=None,
                                      peap=None,
                                      preferred_eap_protocol=None,
                                      process_host_lookup=None,
                                      require_message_auth=None,
                                      rsa_pss=None,
                                      teap=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Update.

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
            description(string): Description, property of the
                request body.
            display_additional_tls_params(boolean):
                displayAdditionalTLSParams, property of
                the request body.
            eap_fast(object): eapFast, property of the request body.
            eap_tls(object): eapTls, property of the request body.
            eap_tls_l_bit(boolean): eapTlsLBit, property of the
                request body.
            eap_ttls(object): eapTtls, property of the request body.
            five_g(boolean): fiveG, property of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            peap(object): peap, property of the request body.
            preferred_eap_protocol(string): The preferredEapProtocol
                is required only if
                allowPreferredEapProtocol is true,
                otherwise it must be ignored. Allowed
                Values: EAP_FAST, PEAP, LEAP, EAP_MD5,
                EAP_TLS, EAP_TTLS, TEAP, property of the
                request body.
            process_host_lookup(boolean): processHostLookup,
                property of the request body.
            require_message_auth(boolean): requireMessageAuth,
                property of the request body.
            rsa_pss(boolean): rsaPss, property of the request body.
            teap(object): teap, property of the request body.
            id(str): id path parameter.
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
            pass

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
            _tmp_payload = {
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
                'eapTlsLBit':
                    eap_tls_l_bit,
                'allowWeakCiphersForEap':
                    allow_weak_ciphers_for_eap,
                'fiveG':
                    five_g,
                'rsaPss':
                    rsa_pss,
                'displayAdditionalTLSParams':
                    display_additional_tls_params,
                'requireMessageAuth':
                    require_message_auth,
                'preferredEapProtocol':
                    preferred_eap_protocol,
                'eapTls':
                    eap_tls,
                'peap':
                    peap,
                'eapTtls':
                    eap_ttls,
                'eapFast':
                    eap_fast,
                'teap':
                    teap,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'AllowedProtocols': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a0b312f70257b1bfa90d0260f0c971_v3_5_0')\
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

        return self._object_factory('bpm_a0b312f70257b1bfa90d0260f0c971_v3_5_0', _api_response)

    def delete_allowedprotocols_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """Delete.

        Args:
            id(str): id path parameter.
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
            pass

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

        e_url = ('/ers/config/allowedprotocols/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6cbd2c420785cfcbdecc3495bca8af4_v3_5_0', _api_response)

    def patch_allowedprotocols_by_id(self,
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
                                     display_additional_tls_params=None,
                                     eap_fast=None,
                                     eap_tls=None,
                                     eap_tls_l_bit=None,
                                     eap_ttls=None,
                                     five_g=None,
                                     name=None,
                                     peap=None,
                                     preferred_eap_protocol=None,
                                     process_host_lookup=None,
                                     require_message_auth=None,
                                     rsa_pss=None,
                                     teap=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

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
            description(string): Description, property of the
                request body.
            display_additional_tls_params(boolean):
                displayAdditionalTLSParams, property of
                the request body.
            eap_fast(object): eapFast, property of the request body.
            eap_tls(object): eapTls, property of the request body.
            eap_tls_l_bit(boolean): eapTlsLBit, property of the
                request body.
            eap_ttls(object): eapTtls, property of the request body.
            five_g(boolean): fiveG, property of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            peap(object): peap, property of the request body.
            preferred_eap_protocol(string): The preferredEapProtocol
                is required only if
                allowPreferredEapProtocol is true,
                otherwise it must be ignored. Allowed
                Values: EAP_FAST, PEAP, LEAP, EAP_MD5,
                EAP_TLS, EAP_TTLS, TEAP, property of the
                request body.
            process_host_lookup(boolean): processHostLookup,
                property of the request body.
            require_message_auth(boolean): requireMessageAuth,
                property of the request body.
            rsa_pss(boolean): rsaPss, property of the request body.
            teap(object): teap, property of the request body.
            id(str): id path parameter.
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
            pass

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
            _tmp_payload = {
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
                'eapTlsLBit':
                    eap_tls_l_bit,
                'allowWeakCiphersForEap':
                    allow_weak_ciphers_for_eap,
                'fiveG':
                    five_g,
                'rsaPss':
                    rsa_pss,
                'displayAdditionalTLSParams':
                    display_additional_tls_params,
                'requireMessageAuth':
                    require_message_auth,
                'preferredEapProtocol':
                    preferred_eap_protocol,
                'eapTls':
                    eap_tls,
                'peap':
                    peap,
                'eapTtls':
                    eap_ttls,
                'eapFast':
                    eap_fast,
                'teap':
                    teap,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'AllowedProtocols': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_da4eb995ac152158f324dfdef5e73d6_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/allowedprotocols/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_da4eb995ac152158f324dfdef5e73d6_v3_5_0', _api_response)
