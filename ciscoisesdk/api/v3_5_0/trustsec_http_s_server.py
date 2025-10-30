# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Trustsec HTTPS Server API wrapper.

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


class TrustsecHttpSServer(object):
    """Identity Services Engine Trustsec HTTPS Server API (version: 3.5.0).

    Wraps the Identity Services Engine Trustsec HTTPS Server
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new TrustsecHttpSServer
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(TrustsecHttpSServer, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_c_t_s_https_servers(self,
                                headers=None,
                                **query_parameters):
        """Get the list of Trustsec HTTPS Servers configured in ISE.

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

        e_url = ('/api/v1/trustsec/https-server')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a959fb44cec6579da186874ae3c62457_v3_5_0', _api_response)

    def create_c_t_s_https_server(self,
                                  cts_certificates=None,
                                  description=None,
                                  host_name=None,
                                  id=None,
                                  ipv4_addresses=None,
                                  ipv6_addresses=None,
                                  name=None,
                                  port=None,
                                  server_type=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Create Trustsec HTTPS Server in ISE.

        Args:
            cts_certificates(list): CtsCertificates, property of the
                request body (list of objects).
            description(string): description text, property of the
                request body.
            host_name(string): FQDN of CTS HTTPS Server, property of
                the request body.
            id(string): Identifier of the CTS HTTPS Server, property
                of the request body.
            ipv4_addresses(list): List of IPv4 addresses of CTS
                HTTPS Server, property of the request
                body (list of strings).
            ipv6_addresses(list): List of IPv6 addresses of CTS
                HTTPS Server, property of the request
                body (list of strings).
            name(string): Name of the CTS HTTPS Server, property of
                the request body.
            port(integer): port number, property of the request
                body.
            server_type(string): type of CTS HTTPS Server, property
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
                'CtsCertificates':
                    cts_certificates,
                'description':
                    description,
                'hostName':
                    host_name,
                'id':
                    id,
                'ipv4Addresses':
                    ipv4_addresses,
                'ipv6Addresses':
                    ipv6_addresses,
                'name':
                    name,
                'port':
                    port,
                'serverType':
                    server_type,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a344a579305e80871a99028d792d7c_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/https-server')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a344a579305e80871a99028d792d7c_v3_5_0', _api_response)

    def get_c_t_s_https_server_by_id(self,
                                     id,
                                     headers=None,
                                     **query_parameters):
        """Get Trustsec HTTPS Server by id.

        Args:
            id(str): id path parameter.
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

        e_url = ('/api/v1/trustsec/https-server/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_de3efb6df75e1dac7159d833de1275_v3_5_0', _api_response)

    def update_c_t_s_https_server(self,
                                  id,
                                  cts_certificates=None,
                                  description=None,
                                  host_name=None,
                                  ipv4_addresses=None,
                                  ipv6_addresses=None,
                                  name=None,
                                  port=None,
                                  server_type=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Update Trustsec HTTPS Server in ISE.

        Args:
            cts_certificates(list): CtsCertificates, property of the
                request body (list of objects).
            description(string): description text, property of the
                request body.
            host_name(string): FQDN of CTS HTTPS Server, property of
                the request body.
            id(string): Identifier of the CTS HTTPS Server, property
                of the request body.
            ipv4_addresses(list): List of IPv4 addresses of CTS
                HTTPS Server, property of the request
                body (list of strings).
            ipv6_addresses(list): List of IPv6 addresses of CTS
                HTTPS Server, property of the request
                body (list of strings).
            name(string): Name of the CTS HTTPS Server, property of
                the request body.
            port(integer): port number, property of the request
                body.
            server_type(string): type of CTS HTTPS Server, property
                of the request body.
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
                'CtsCertificates':
                    cts_certificates,
                'description':
                    description,
                'hostName':
                    host_name,
                'id':
                    id,
                'ipv4Addresses':
                    ipv4_addresses,
                'ipv6Addresses':
                    ipv6_addresses,
                'name':
                    name,
                'port':
                    port,
                'serverType':
                    server_type,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a7fd7c949f5d77b0ca0f73a277ab07_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/https-server/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a7fd7c949f5d77b0ca0f73a277ab07_v3_5_0', _api_response)

    def delete_c_t_s_https_server(self,
                                  id,
                                  headers=None,
                                  **query_parameters):
        """Delete Trustsec HTTPS Server in ISE.

        Args:
            id(str): id path parameter.
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

        e_url = ('/api/v1/trustsec/https-server/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b01af87dc97f5d99a09f13f668834e53_v3_5_0', _api_response)
