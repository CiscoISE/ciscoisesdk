# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine ExternalRADIUSServer API wrapper.

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


class ExternalRadiusServer(object):
    """Identity Services Engine ExternalRADIUSServer API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine ExternalRADIUSServer
    API and exposes the API as native Python
    methods that return native Python objects.

    | External RADIUS Server API allows the client to add, delete, update, search and perform actions on external RADIUS server.

    **Revision History**


    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    | Revision # | Resource   Version | Cisco ISE Version | Description                              | Revision Modification | Revision Modification                |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    |            |                    |                   |                                          | Attribute             | Description                          |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    | 0          | 1.0                | 2.3               | Initial Cisco ISE Version                |                       |                                      |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    | 1          | 1.1                | 2.6               | Support new attribute Proxy Dead Timeout | proxyTimeout          | Added   int Attribute 'proxyTimeout' |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+

    |

    **Resource Definition**

    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | **Attribute**      | **Type**  | **Required** | **Description**                                                                                                                                                                                                               | **Default Values** | **Example Values**                   |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | name               | String    | Yes          | Resource Name. Allowed charactera are alphanumeric and _ (underscore).                                                                                                                                                        |                    | externalRadiusServer1                |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | id                 | String    | No           | Resource UUID, mandatory for update                                                                                                                                                                                           |                    | da095377-dce8-486e-933a-6ea788bbf51a |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | description        | String    | No           |                                                                                                                                                                                                                               |                    | example external radius server       |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | hostIP             | String    | Yes          | The IP of the host - must be a valid IPV4 address                                                                                                                                                                             |                    | 1.1.1.1                              |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | sharedSecret       | String    | Yes          | Shared secret maximum length is 128 characters                                                                                                                                                                                |                    | sharedSecret                         |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | enableKeyWrap      | Boolean   | Yes          | KeyWrap may only be enabled if it is supported on the device. When running in FIPS mode this option should be enabled for such devices                                                                                        |                    | true                                 |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | encryptionKey      | String    | No           | The encryptionKey is required only if enableKeyWrap is true, otherwise it must be ignored or empty. The maximum length is 16 ASCII characters or 32 HEXADECIMAL characters (depend on selection in field 'keyInputFormat')    |                    | 1616161616161616                     |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | authenticatorKey   | String    | No           | The authenticatorKey is required only if enableKeyWrap is true, otherwise it must be ignored or empty. The maximum length is 20 ASCII characters or 40 HEXADECIMAL characters (depend on selection in field 'keyInputFormat') |                    | 20202020202020202020                 |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | keyInputFormat     | Enum      | Yes          | Specifies the format of the input for fields 'encryptionKey' and 'authenticatorKey'. Allowed Values: ASCII, HEXADECIMAL                                                                                                       |                    | ASCII                                |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | authenticationPort | Integer   | Yes          | Valid Range 1 to 65535                                                                                                                                                                                                        |                    | 1812                                 |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | accountingPort     | Integer   | Yes          | Valid Range 1 to 65535                                                                                                                                                                                                        |                    | 1813                                 |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | timeout            | Integer   | Yes          | Valid Range 1 to 120                                                                                                                                                                                                          |                    | 5                                    |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | retries            | Integer   | Yes          | Valid Range 1 to 9                                                                                                                                                                                                            |                    | 3                                    |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | proxyTimeout       | Integer   | No           | Valid Range 1 to 600                                                                                                                                                                                                          | 300                |                                      |
    +--------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ExternalRadiusServer
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ExternalRadiusServer, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_external_radius_server_by_name(self,
                                           name,
                                           headers=None,
                                           **query_parameters):
        """This API allows the client to get an external RADIUS server by
        name.

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
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
                           basestring)

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

        e_url = ('/ers/config/externalradiusserver/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afa6d7527045ebc928ee7e30ad3092a_v3_1_patch_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_external_radius_server_by_name <#ciscoisesdk.
        api.v3_1_patch_1.external_radius_server.
        ExternalRadiusServer.get_external_radius_server_by_name>`_
        """
        return self.get_external_radius_server_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_external_radius_server_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """This API allows the client to get an external RADIUS server by
        ID.

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
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
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

        e_url = ('/ers/config/externalradiusserver/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af14464cc6a05f6f87bbe7c174b6d5f6_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_external_radius_server_by_id <#ciscoisesdk.
        api.v3_1_patch_1.external_radius_server.
        ExternalRadiusServer.get_external_radius_server_by_id>`_
        """
        return self.get_external_radius_server_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_external_radius_server_by_id(self,
                                            id,
                                            accounting_port=None,
                                            authentication_port=None,
                                            authenticator_key=None,
                                            description=None,
                                            enable_key_wrap=None,
                                            encryption_key=None,
                                            host_ip=None,
                                            key_input_format=None,
                                            name=None,
                                            proxy_timeout=None,
                                            retries=None,
                                            shared_secret=None,
                                            timeout=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """This API allows the client to update an external RADIUS server.

        Args:
            accounting_port(integer): Valid Range 1 to 65535,
                property of the request body.
            authentication_port(integer): Valid Range 1 to 65535,
                property of the request body.
            authenticator_key(string): The authenticatorKey is
                required only if enableKeyWrap is true,
                otherwise it must be ignored or empty.
                The maximum length is 20 ASCII
                characters or 40 HEXADECIMAL characters
                (depend on selection in field
                'keyInputFormat'), property of the
                request body.
            description(string): description, property of the
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
            id(string): id, property of the request body.
            key_input_format(string): Specifies the format of the
                input for fields 'encryptionKey' and
                'authenticatorKey'. Allowed Values:
                ASCII HEXADECIMAL, property of the
                request body.
            name(string): Resource Name. Allowed charactera are
                alphanumeric and _ (underscore).,
                property of the request body.
            proxy_timeout(integer): Valid Range 1 to 600, property
                of the request body.
            retries(integer): Valid Range 1 to 9, property of the
                request body.
            shared_secret(string): Shared secret maximum length is
                128 characters, property of the request
                body.
            timeout(integer): Valid Range 1 to 120, property of the
                request body.
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
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
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
            _tmp_payload = {
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
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
            }
            _payload = {
                'ExternalRadiusServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c6536d17325c84a54189f46d4bbad2_v3_1_patch_1')\
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

        return self._object_factory('bpm_c6536d17325c84a54189f46d4bbad2_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
                     accounting_port=None,
                     authentication_port=None,
                     authenticator_key=None,
                     description=None,
                     enable_key_wrap=None,
                     encryption_key=None,
                     host_ip=None,
                     key_input_format=None,
                     name=None,
                     proxy_timeout=None,
                     retries=None,
                     shared_secret=None,
                     timeout=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_external_radius_server_by_id <#ciscoisesdk.
        api.v3_1_patch_1.external_radius_server.
        ExternalRadiusServer.update_external_radius_server_by_id>`_
        """
        return self.update_external_radius_server_by_id(
            id=id,
            accounting_port=accounting_port,
            authentication_port=authentication_port,
            authenticator_key=authenticator_key,
            description=description,
            enable_key_wrap=enable_key_wrap,
            encryption_key=encryption_key,
            host_ip=host_ip,
            key_input_format=key_input_format,
            name=name,
            proxy_timeout=proxy_timeout,
            retries=retries,
            shared_secret=shared_secret,
            timeout=timeout,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_external_radius_server_by_id(self,
                                            id,
                                            headers=None,
                                            **query_parameters):
        """This API deletes an external RADIUS server.

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
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
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

        e_url = ('/ers/config/externalradiusserver/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d86e3201f9b0561db13a9eb1b1d59bd5_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_external_radius_server_by_id <#ciscoisesdk.
        api.v3_1_patch_1.external_radius_server.
        ExternalRadiusServer.delete_external_radius_server_by_id>`_
        """
        return self.delete_external_radius_server_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_external_radius_server(self,
                                   page=None,
                                   size=None,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to get all the external RADIUS
        servers.

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
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
                           basestring)

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

        e_url = ('/ers/config/externalradiusserver')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b641825a9555ecba105cabbdf50fc78_v3_1_patch_1', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_external_radius_server <#ciscoisesdk.
        api.v3_1_patch_1.external_radius_server.
        ExternalRadiusServer.get_external_radius_server>`_
        """
        return self.get_external_radius_server(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_external_radius_server_generator(self,
                                             page=None,
                                             size=None,
                                             headers=None,
                                             **query_parameters):
        """This API allows the client to get all the external RADIUS
        servers.

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

        yield from get_next_page(
            self.get_external_radius_server, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          page=None,
                          size=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_external_radius_server_generator <#ciscoisesdk.
        api.v3_1_patch_1.external_radius_server.
        ExternalRadiusServer.get_external_radius_server_generator>`_
        """
        yield from get_next_page(
            self.get_external_radius_server, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_external_radius_server(self,
                                      accounting_port=None,
                                      authentication_port=None,
                                      authenticator_key=None,
                                      description=None,
                                      enable_key_wrap=None,
                                      encryption_key=None,
                                      host_ip=None,
                                      key_input_format=None,
                                      name=None,
                                      proxy_timeout=None,
                                      retries=None,
                                      shared_secret=None,
                                      timeout=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """This API creates an external RADIUS server.

        Args:
            accounting_port(integer): Valid Range 1 to 65535,
                property of the request body.
            authentication_port(integer): Valid Range 1 to 65535,
                property of the request body.
            authenticator_key(string): The authenticatorKey is
                required only if enableKeyWrap is true,
                otherwise it must be ignored or empty.
                The maximum length is 20 ASCII
                characters or 40 HEXADECIMAL characters
                (depend on selection in field
                'keyInputFormat'), property of the
                request body.
            description(string): description, property of the
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
            key_input_format(string): Specifies the format of the
                input for fields 'encryptionKey' and
                'authenticatorKey'. Allowed Values:
                ASCII HEXADECIMAL, property of the
                request body.
            name(string): Resource Name. Allowed charactera are
                alphanumeric and _ (underscore).,
                property of the request body.
            proxy_timeout(integer): Valid Range 1 to 600, property
                of the request body.
            retries(integer): Valid Range 1 to 9, property of the
                request body.
            shared_secret(string): Shared secret maximum length is
                128 characters, property of the request
                body.
            timeout(integer): Valid Range 1 to 120, property of the
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
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
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
            _tmp_payload = {
                'name':
                    name,
                'description':
                    description,
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
            }
            _payload = {
                'ExternalRadiusServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fc1c74b35ae5050b4f7fd702570ad5b_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/externalradiusserver')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_fc1c74b35ae5050b4f7fd702570ad5b_v3_1_patch_1', _api_response)

    def create(self,
               accounting_port=None,
               authentication_port=None,
               authenticator_key=None,
               description=None,
               enable_key_wrap=None,
               encryption_key=None,
               host_ip=None,
               key_input_format=None,
               name=None,
               proxy_timeout=None,
               retries=None,
               shared_secret=None,
               timeout=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_external_radius_server <#ciscoisesdk.
        api.v3_1_patch_1.external_radius_server.
        ExternalRadiusServer.create_external_radius_server>`_
        """
        return self.create_external_radius_server(
            accounting_port=accounting_port,
            authentication_port=authentication_port,
            authenticator_key=authenticator_key,
            description=description,
            enable_key_wrap=enable_key_wrap,
            encryption_key=encryption_key,
            host_ip=host_ip,
            key_input_format=key_input_format,
            name=name,
            proxy_timeout=proxy_timeout,
            retries=retries,
            shared_secret=shared_secret,
            timeout=timeout,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the external RADIUS server.

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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/externalradiusserver/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6c3ffe72746500b88be3a5418ead4ba_v3_1_patch_1', _api_response)
