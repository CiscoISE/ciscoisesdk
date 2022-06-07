# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine TACACSExternalServers API wrapper.

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


class TacacsExternalServers(object):
    """Identity Services Engine TACACSExternalServers API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine TACACSExternalServers
    API and exposes the API as native Python
    methods that return native Python objects.

    | TACACS External Servers API allows the client to add, delete, update, search and perform actions on TACACS external servers.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.4                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | **Attribute**  | **Type** | **Required** | **Description**                     | **Default Values** | **Example Values**                   |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | name           | String   | Yes          | Resource Name                       |                    | TacacsExternalServer1                |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | id             | String   | No           | Resource UUID, mandatory for update |                    | 1af3d6e2-cc3b-4603-b80f-6827768335ab |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | description    | String   | No           |                                     |                    | TacacsExternalServerForSDK           |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | hostIP         | String   | Yes          | The server IPV4 address             |                    | 1.1.1.1                              |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | connectionPort | Integer  | No           | The port to connect the server      | 49                 |                                      |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | singleConnect  | Boolean  | No           | Define the use of single connection | true               |                                      |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | sharedSecret   | String   | Yes          | The server shared secret            |                    | SharedSecret                         |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+
    | timeout        | Integer  | No           | The server timeout                  | 20                 |                                      |
    +----------------+----------+--------------+-------------------------------------+--------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new TacacsExternalServers
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(TacacsExternalServers, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_tacacs_external_servers_by_name(self,
                                            name,
                                            headers=None,
                                            **query_parameters):
        """This API allows the client to get TACACS external servers by
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

        e_url = ('/ers/config/tacacsexternalservers/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afe1108b1a59539ebe3de3e5652c9653_v3_1_patch_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_tacacs_external_servers_by_name <#ciscoisesdk.
        api.v3_1_patch_1.tacacs_external_servers.
        TacacsExternalServers.get_tacacs_external_servers_by_name>`_
        """
        return self.get_tacacs_external_servers_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_tacacs_external_servers_by_id(self,
                                          id,
                                          headers=None,
                                          **query_parameters):
        """This API allows the client to get TACACS external servers by ID.

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

        e_url = ('/ers/config/tacacsexternalservers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b9eb9547216547cab8b9e686eee674b_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_tacacs_external_servers_by_id <#ciscoisesdk.
        api.v3_1_patch_1.tacacs_external_servers.
        TacacsExternalServers.get_tacacs_external_servers_by_id>`_
        """
        return self.get_tacacs_external_servers_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_tacacs_external_servers_by_id(self,
                                             id,
                                             connection_port=None,
                                             description=None,
                                             host_ip=None,
                                             name=None,
                                             shared_secret=None,
                                             single_connect=None,
                                             timeout=None,
                                             headers=None,
                                             payload=None,
                                             active_validation=True,
                                             **query_parameters):
        """This API allows the client to update TACACS external servers.

        Args:
            connection_port(integer): The port to connect the
                server, property of the request body.
            description(string): description, property of the
                request body.
            host_ip(string): The server IPV4 address, property of
                the request body.
            id(string): id, property of the request body.
            name(string): name, property of the request body.
            shared_secret(string): The server shared secret,
                property of the request body.
            single_connect(boolean): Define the use of single
                connection, property of the request
                body.
            timeout(integer): The server timeout, property of the
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
                'connectionPort':
                    connection_port,
                'singleConnect':
                    single_connect,
                'sharedSecret':
                    shared_secret,
                'timeout':
                    timeout,
            }
            _payload = {
                'TacacsExternalServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a7cffe3bfae55aa81b7b4447519e4cd_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsexternalservers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a7cffe3bfae55aa81b7b4447519e4cd_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
                     connection_port=None,
                     description=None,
                     host_ip=None,
                     name=None,
                     shared_secret=None,
                     single_connect=None,
                     timeout=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_tacacs_external_servers_by_id <#ciscoisesdk.
        api.v3_1_patch_1.tacacs_external_servers.
        TacacsExternalServers.update_tacacs_external_servers_by_id>`_
        """
        return self.update_tacacs_external_servers_by_id(
            id=id,
            connection_port=connection_port,
            description=description,
            host_ip=host_ip,
            name=name,
            shared_secret=shared_secret,
            single_connect=single_connect,
            timeout=timeout,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_tacacs_external_servers_by_id(self,
                                             id,
                                             headers=None,
                                             **query_parameters):
        """This API deletes TACACS external servers.

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

        e_url = ('/ers/config/tacacsexternalservers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_2564523798353b885b115048_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_tacacs_external_servers_by_id <#ciscoisesdk.
        api.v3_1_patch_1.tacacs_external_servers.
        TacacsExternalServers.delete_tacacs_external_servers_by_id>`_
        """
        return self.delete_tacacs_external_servers_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_tacacs_external_servers(self,
                                    page=None,
                                    size=None,
                                    headers=None,
                                    **query_parameters):
        """This API allows the client to get all the TACACS external
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

        e_url = ('/ers/config/tacacsexternalservers')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c6c2a4908ee5f48b7e9cae7572f6a94_v3_1_patch_1', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_tacacs_external_servers <#ciscoisesdk.
        api.v3_1_patch_1.tacacs_external_servers.
        TacacsExternalServers.get_tacacs_external_servers>`_
        """
        return self.get_tacacs_external_servers(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_tacacs_external_servers_generator(self,
                                              page=None,
                                              size=None,
                                              headers=None,
                                              **query_parameters):
        """This API allows the client to get all the TACACS external
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
            self.get_tacacs_external_servers, dict(
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
        """Alias for `get_tacacs_external_servers_generator <#ciscoisesdk.
        api.v3_1_patch_1.tacacs_external_servers.
        TacacsExternalServers.get_tacacs_external_servers_generator>`_
        """
        yield from get_next_page(
            self.get_tacacs_external_servers, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_tacacs_external_servers(self,
                                       connection_port=None,
                                       description=None,
                                       host_ip=None,
                                       name=None,
                                       shared_secret=None,
                                       single_connect=None,
                                       timeout=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """This API creates TACACS external servers.

        Args:
            connection_port(integer): The port to connect the
                server, property of the request body.
            description(string): description, property of the
                request body.
            host_ip(string): The server IPV4 address, property of
                the request body.
            name(string): name, property of the request body.
            shared_secret(string): The server shared secret,
                property of the request body.
            single_connect(boolean): Define the use of single
                connection, property of the request
                body.
            timeout(integer): The server timeout, property of the
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
                'connectionPort':
                    connection_port,
                'singleConnect':
                    single_connect,
                'sharedSecret':
                    shared_secret,
                'timeout':
                    timeout,
            }
            _payload = {
                'TacacsExternalServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b5097e4db7505ba390914b50b1c2046b_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsexternalservers')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b5097e4db7505ba390914b50b1c2046b_v3_1_patch_1', _api_response)

    def create(self,
               connection_port=None,
               description=None,
               host_ip=None,
               name=None,
               shared_secret=None,
               single_connect=None,
               timeout=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_tacacs_external_servers <#ciscoisesdk.
        api.v3_1_patch_1.tacacs_external_servers.
        TacacsExternalServers.create_tacacs_external_servers>`_
        """
        return self.create_tacacs_external_servers(
            connection_port=connection_port,
            description=description,
            host_ip=host_ip,
            name=name,
            shared_secret=shared_secret,
            single_connect=single_connect,
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
        the TACACS external servers.

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

        e_url = ('/ers/config/tacacsexternalservers/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d3e106d187b35547bf1f0463e4fc832f_v3_1_patch_1', _api_response)
