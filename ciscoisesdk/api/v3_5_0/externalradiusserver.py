# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine externalradiusserver API wrapper.

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


class Externalradiusserver(object):
    """Identity Services Engine externalradiusserver API (version: 3.5.0).

    Wraps the Identity Services Engine externalradiusserver
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Externalradiusserver
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Externalradiusserver, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_externalradiusserver(self,
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

        e_url = ('/ers/config/externalradiusserver/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea682db0036e5030a5c2f0a4267ab4b8_v3_5_0', _api_response)

    def get_externalradiusserver_generator(self,
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
            self.get_externalradiusserver, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_externalradiusserver(self,
                                    accounting_port=None,
                                    authentication_port=None,
                                    authenticator_key=None,
                                    description=None,
                                    enable_key_wrap=None,
                                    encryption_key=None,
                                    host_ip=None,
                                    id=None,
                                    key_input_format=None,
                                    msg_auth_is_required_on_response=None,
                                    name=None,
                                    proxy_timeout=None,
                                    retries=None,
                                    shared_secret=None,
                                    timeout=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """Create.

        Args:
            accounting_port(object): Valid Range 1 to 65535,
                property of the request body.
            authentication_port(object): Valid Range 1 to 65535,
                property of the request body.
            authenticator_key(string): The authenticatorKey is
                required only if enableKeyWrap is true,
                otherwise it must be ignored or empty.
                The maximum length is 20 ASCII
                characters or 40 HEXADECIMAL characters
                (depend on selection in field
                'keyInputFormat'), property of the
                request body.
            description(string): Description, property of the
                request body.
            enable_key_wrap(boolean): KeyWrap may only be enabled if
                it is supported on the device. When
                running in FIPS mode this option should
                be enabled for such devices, property of
                the request body.
            encryption_key(string): The encryptionKey is required
                only if enableKeyWrap is true, otherwise
                it must be ignored or empty. The maximum
                length is 16 ASCII characters or 32
                HEXADECIMAL characters (depend on
                selection in field 'keyInputFormat'),
                property of the request body.
            host_ip(string): The IP of the host must be a valid IPV4
                address, property of the request body.
            id(string): Id, property of the request body.
            key_input_format(string): Specifies the format of the
                input for fields 'encryptionKey' and
                'authenticatorKey'. Allowed Values:
                ASCII or HEXADECIMAL, property of the
                request body.
            msg_auth_is_required_on_response(boolean): Should ISE
                validate the existence of Message-
                Authenticator on responses from the
                eternal RADIUS server, property of the
                request body.
            name(string): name, property of the request body.
            proxy_timeout(object): Valid Range 1 to 600, property of
                the request body.
            retries(object): Valid Range 1 to 9, property of the
                request body.
            shared_secret(string): Shared secret maximum length is
                128 characters, property of the request
                body.
            timeout(object): Valid Range 1 to 120, property of the
                request body.
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
                'hostIP':
                    host_ip,
                'sharedSecret':
                    shared_secret,
                'enableKeyWrap':
                    enable_key_wrap,
                'encryptionKey':
                    encryption_key,
                'authenticatorKey':
                    authenticator_key,
                'keyInputFormat':
                    key_input_format,
                'authenticationPort':
                    authentication_port,
                'accountingPort':
                    accounting_port,
                'timeout':
                    timeout,
                'retries':
                    retries,
                'proxyTimeout':
                    proxy_timeout,
                'msgAuthIsRequiredOnResponse':
                    msg_auth_is_required_on_response,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ExternalRadiusServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_aa9ea10d15964aad77591aacd55d5_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/externalradiusserver/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_aa9ea10d15964aad77591aacd55d5_v3_5_0', _api_response)

    def get_externalradiusserver_name_by_name(self,
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

        e_url = ('/ers/config/externalradiusserver/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afa6d7527045ebc928ee7e30ad3092a_v3_5_0', _api_response)

    def get_externalradiusserver_by_id(self,
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

        e_url = ('/ers/config/externalradiusserver/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af14464cc6a05f6f87bbe7c174b6d5f6_v3_5_0', _api_response)

    def update_externalradiusserver_by_id(self,
                                          id,
                                          accounting_port=None,
                                          authentication_port=None,
                                          authenticator_key=None,
                                          description=None,
                                          enable_key_wrap=None,
                                          encryption_key=None,
                                          host_ip=None,
                                          key_input_format=None,
                                          msg_auth_is_required_on_response=None,
                                          name=None,
                                          proxy_timeout=None,
                                          retries=None,
                                          shared_secret=None,
                                          timeout=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **query_parameters):
        """Update.

        Args:
            accounting_port(object): Valid Range 1 to 65535,
                property of the request body.
            authentication_port(object): Valid Range 1 to 65535,
                property of the request body.
            authenticator_key(string): The authenticatorKey is
                required only if enableKeyWrap is true,
                otherwise it must be ignored or empty.
                The maximum length is 20 ASCII
                characters or 40 HEXADECIMAL characters
                (depend on selection in field
                'keyInputFormat'), property of the
                request body.
            description(string): Description, property of the
                request body.
            enable_key_wrap(boolean): KeyWrap may only be enabled if
                it is supported on the device. When
                running in FIPS mode this option should
                be enabled for such devices, property of
                the request body.
            encryption_key(string): The encryptionKey is required
                only if enableKeyWrap is true, otherwise
                it must be ignored or empty. The maximum
                length is 16 ASCII characters or 32
                HEXADECIMAL characters (depend on
                selection in field 'keyInputFormat'),
                property of the request body.
            host_ip(string): The IP of the host must be a valid IPV4
                address, property of the request body.
            id(string): Id, property of the request body.
            key_input_format(string): Specifies the format of the
                input for fields 'encryptionKey' and
                'authenticatorKey'. Allowed Values:
                ASCII or HEXADECIMAL, property of the
                request body.
            msg_auth_is_required_on_response(boolean): Should ISE
                validate the existence of Message-
                Authenticator on responses from the
                eternal RADIUS server, property of the
                request body.
            name(string): name, property of the request body.
            proxy_timeout(object): Valid Range 1 to 600, property of
                the request body.
            retries(object): Valid Range 1 to 9, property of the
                request body.
            shared_secret(string): Shared secret maximum length is
                128 characters, property of the request
                body.
            timeout(object): Valid Range 1 to 120, property of the
                request body.
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
                'hostIP':
                    host_ip,
                'sharedSecret':
                    shared_secret,
                'enableKeyWrap':
                    enable_key_wrap,
                'encryptionKey':
                    encryption_key,
                'authenticatorKey':
                    authenticator_key,
                'keyInputFormat':
                    key_input_format,
                'authenticationPort':
                    authentication_port,
                'accountingPort':
                    accounting_port,
                'timeout':
                    timeout,
                'retries':
                    retries,
                'proxyTimeout':
                    proxy_timeout,
                'msgAuthIsRequiredOnResponse':
                    msg_auth_is_required_on_response,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ExternalRadiusServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c6536d17325c84a54189f46d4bbad2_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/externalradiusserver/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c6536d17325c84a54189f46d4bbad2_v3_5_0', _api_response)

    def delete_externalradiusserver_by_id(self,
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

        e_url = ('/ers/config/externalradiusserver/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d86e3201f9b0561db13a9eb1b1d59bd5_v3_5_0', _api_response)

    def patch_externalradiusserver_by_id(self,
                                         id,
                                         accounting_port=None,
                                         authentication_port=None,
                                         authenticator_key=None,
                                         description=None,
                                         enable_key_wrap=None,
                                         encryption_key=None,
                                         host_ip=None,
                                         key_input_format=None,
                                         msg_auth_is_required_on_response=None,
                                         name=None,
                                         proxy_timeout=None,
                                         retries=None,
                                         shared_secret=None,
                                         timeout=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            accounting_port(object): Valid Range 1 to 65535,
                property of the request body.
            authentication_port(object): Valid Range 1 to 65535,
                property of the request body.
            authenticator_key(string): The authenticatorKey is
                required only if enableKeyWrap is true,
                otherwise it must be ignored or empty.
                The maximum length is 20 ASCII
                characters or 40 HEXADECIMAL characters
                (depend on selection in field
                'keyInputFormat'), property of the
                request body.
            description(string): Description, property of the
                request body.
            enable_key_wrap(boolean): KeyWrap may only be enabled if
                it is supported on the device. When
                running in FIPS mode this option should
                be enabled for such devices, property of
                the request body.
            encryption_key(string): The encryptionKey is required
                only if enableKeyWrap is true, otherwise
                it must be ignored or empty. The maximum
                length is 16 ASCII characters or 32
                HEXADECIMAL characters (depend on
                selection in field 'keyInputFormat'),
                property of the request body.
            host_ip(string): The IP of the host must be a valid IPV4
                address, property of the request body.
            id(string): Id, property of the request body.
            key_input_format(string): Specifies the format of the
                input for fields 'encryptionKey' and
                'authenticatorKey'. Allowed Values:
                ASCII or HEXADECIMAL, property of the
                request body.
            msg_auth_is_required_on_response(boolean): Should ISE
                validate the existence of Message-
                Authenticator on responses from the
                eternal RADIUS server, property of the
                request body.
            name(string): name, property of the request body.
            proxy_timeout(object): Valid Range 1 to 600, property of
                the request body.
            retries(object): Valid Range 1 to 9, property of the
                request body.
            shared_secret(string): Shared secret maximum length is
                128 characters, property of the request
                body.
            timeout(object): Valid Range 1 to 120, property of the
                request body.
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
                'hostIP':
                    host_ip,
                'sharedSecret':
                    shared_secret,
                'enableKeyWrap':
                    enable_key_wrap,
                'encryptionKey':
                    encryption_key,
                'authenticatorKey':
                    authenticator_key,
                'keyInputFormat':
                    key_input_format,
                'authenticationPort':
                    authentication_port,
                'accountingPort':
                    accounting_port,
                'timeout':
                    timeout,
                'retries':
                    retries,
                'proxyTimeout':
                    proxy_timeout,
                'msgAuthIsRequiredOnResponse':
                    msg_auth_is_required_on_response,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ExternalRadiusServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d7468254be85e97a56521bff13da212_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/externalradiusserver/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_d7468254be85e97a56521bff13da212_v3_5_0', _api_response)
