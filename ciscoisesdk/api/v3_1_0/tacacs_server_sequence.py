# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine TacacsServerSequence API wrapper.

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
from ...pagination import get_next_page


class TacacsServerSequence(object):
    """Identity Services Engine TacacsServerSequence API (version: 3.1.0).

    Wraps the Identity Services Engine TacacsServerSequence
    API and exposes the API as native Python
    methods that return native Python objects.

    | TACACS Server Sequence API aallows the client to add, delete, update, search and perform actions on TACACS server sequence.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.4                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | **Attribute**    | **Type** | **Required** | **Description**                                                                                                                                                | **Default Values** | **Example Values**                          |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | name             | String   | Yes          | Resource Name                                                                                                                                                  |                    | TacacsServerSequence1                       |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | id               | String   | No           | Resource UUID, mandatory for update                                                                                                                            |                    | 1af3d6e2-cc3b-4603-b80f-6827768335ab        |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | description      | String   | No           |                                                                                                                                                                |                    | TacacsServerSequenceForSDK                  |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | serverList       | String   | Yes          | The names of Tacacs external servers separated by commas. The order of the names in the string is the order of servers that will be used during authentication |                    | TacacsExternalServer1,TacacsExternalServer2 |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | localAccounting  | Boolean  | No           |                                                                                                                                                                | false              |                                             |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | remoteAccounting | Boolean  | No           |                                                                                                                                                                | true               |                                             |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | prefixStrip      | Boolean  | No           | Define if a delimiter will be used for prefix strip                                                                                                            | false              |                                             |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | suffixStrip      | Boolean  | No           | Define if a delimiter will be used for suffix strip                                                                                                            | false              |                                             |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | prefixDelimiter  | String   | No           | The delimiter that will be used for prefix strip                                                                                                               | \\                  |                                             |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+
    | suffixDelimiter  | String   | No           | The delimiter that will be used for suffix strip                                                                                                               | @                  |                                             |
    +------------------+----------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+---------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new TacacsServerSequence
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(TacacsServerSequence, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_tacacs_server_sequence_by_name(self,
                                           name,
                                           headers=None,
                                           **query_parameters):
        """This API allows the client to get a TACACS server sequence by
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

        e_url = ('/ers/config/tacacsserversequence/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b03900a2e5027b615d9f1bdcf9f63_v3_1_0', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_tacacs_server_sequence_by_name <#ciscoisesdk.
        api.v3_1_0.tacacs_server_sequence.
        TacacsServerSequence.get_tacacs_server_sequence_by_name>`_
        """
        return self.get_tacacs_server_sequence_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_tacacs_server_sequence_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """This API allows the client to get a TACACS server sequence by
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

        e_url = ('/ers/config/tacacsserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f3b45b8e4089574c9912407f88b1a5d2_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_tacacs_server_sequence_by_id <#ciscoisesdk.
        api.v3_1_0.tacacs_server_sequence.
        TacacsServerSequence.get_tacacs_server_sequence_by_id>`_
        """
        return self.get_tacacs_server_sequence_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_tacacs_server_sequence_by_id(self,
                                            id,
                                            description=None,
                                            local_accounting=None,
                                            name=None,
                                            prefix_delimiter=None,
                                            prefix_strip=None,
                                            remote_accounting=None,
                                            server_list=None,
                                            suffix_delimiter=None,
                                            suffix_strip=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """This API allows the client to update a TACACS server sequence.

        Args:
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            local_accounting(boolean): localAccounting, property of
                the request body.
            name(string): name, property of the request body.
            prefix_delimiter(string): The delimiter that will be
                used for prefix strip, property of the
                request body.
            prefix_strip(boolean): Define if a delimiter will be
                used for prefix strip, property of the
                request body.
            remote_accounting(boolean): remoteAccounting, property
                of the request body.
            server_list(string): The names of Tacacs external
                servers separated by commas. The order
                of the names in the string is the order
                of servers that will be used during
                authentication, property of the request
                body.
            suffix_delimiter(string): The delimiter that will be
                used for suffix strip, property of the
                request body.
            suffix_strip(boolean): Define if a delimiter will be
                used for suffix strip, property of the
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
                'serverList':
                    server_list,
                'localAccounting':
                    local_accounting,
                'remoteAccounting':
                    remote_accounting,
                'prefixStrip':
                    prefix_strip,
                'prefixDelimiter':
                    prefix_delimiter,
                'suffixStrip':
                    suffix_strip,
                'suffixDelimiter':
                    suffix_delimiter,
            }
            _payload = {
                'TacacsServerSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f6de5797735bbd95dc8683c6a7aebf_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f6de5797735bbd95dc8683c6a7aebf_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     description=None,
                     local_accounting=None,
                     name=None,
                     prefix_delimiter=None,
                     prefix_strip=None,
                     remote_accounting=None,
                     server_list=None,
                     suffix_delimiter=None,
                     suffix_strip=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_tacacs_server_sequence_by_id <#ciscoisesdk.
        api.v3_1_0.tacacs_server_sequence.
        TacacsServerSequence.update_tacacs_server_sequence_by_id>`_
        """
        return self.update_tacacs_server_sequence_by_id(
            id=id,
            description=description,
            local_accounting=local_accounting,
            name=name,
            prefix_delimiter=prefix_delimiter,
            prefix_strip=prefix_strip,
            remote_accounting=remote_accounting,
            server_list=server_list,
            suffix_delimiter=suffix_delimiter,
            suffix_strip=suffix_strip,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_tacacs_server_sequence_by_id(self,
                                            id,
                                            headers=None,
                                            **query_parameters):
        """This API deletes a TACACS server sequence.

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

        e_url = ('/ers/config/tacacsserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1465b72911359bdbb1430469801d4be_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_tacacs_server_sequence_by_id <#ciscoisesdk.
        api.v3_1_0.tacacs_server_sequence.
        TacacsServerSequence.delete_tacacs_server_sequence_by_id>`_
        """
        return self.delete_tacacs_server_sequence_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_tacacs_server_sequence(self,
                                   page=None,
                                   size=None,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to get all the TACACS server
        sequences.

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

        e_url = ('/ers/config/tacacsserversequence')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c189f2f5f6b8bab3931c206c949_v3_1_0', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_tacacs_server_sequence <#ciscoisesdk.
        api.v3_1_0.tacacs_server_sequence.
        TacacsServerSequence.get_tacacs_server_sequence>`_
        """
        return self.get_tacacs_server_sequence(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_tacacs_server_sequence_generator(self,
                                             page=None,
                                             size=None,
                                             headers=None,
                                             **query_parameters):
        """This API allows the client to get all the TACACS server
        sequences.

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
            self.get_tacacs_server_sequence, dict(
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
        """Alias for `get_tacacs_server_sequence_generator <#ciscoisesdk.
        api.v3_1_0.tacacs_server_sequence.
        TacacsServerSequence.get_tacacs_server_sequence_generator>`_
        """
        yield from get_next_page(
            self.get_tacacs_server_sequence, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_tacacs_server_sequence(self,
                                      description=None,
                                      local_accounting=None,
                                      name=None,
                                      prefix_delimiter=None,
                                      prefix_strip=None,
                                      remote_accounting=None,
                                      server_list=None,
                                      suffix_delimiter=None,
                                      suffix_strip=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """This API creates a TACACS server sequence.

        Args:
            description(string): description, property of the
                request body.
            local_accounting(boolean): localAccounting, property of
                the request body.
            name(string): name, property of the request body.
            prefix_delimiter(string): The delimiter that will be
                used for prefix strip, property of the
                request body.
            prefix_strip(boolean): Define if a delimiter will be
                used for prefix strip, property of the
                request body.
            remote_accounting(boolean): remoteAccounting, property
                of the request body.
            server_list(string): The names of Tacacs external
                servers separated by commas. The order
                of the names in the string is the order
                of servers that will be used during
                authentication, property of the request
                body.
            suffix_delimiter(string): The delimiter that will be
                used for suffix strip, property of the
                request body.
            suffix_strip(boolean): Define if a delimiter will be
                used for suffix strip, property of the
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
                'serverList':
                    server_list,
                'localAccounting':
                    local_accounting,
                'remoteAccounting':
                    remote_accounting,
                'prefixStrip':
                    prefix_strip,
                'prefixDelimiter':
                    prefix_delimiter,
                'suffixStrip':
                    suffix_strip,
                'suffixDelimiter':
                    suffix_delimiter,
            }
            _payload = {
                'TacacsServerSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a1e26e595667bd98f84dd29232e2_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsserversequence')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a1e26e595667bd98f84dd29232e2_v3_1_0', _api_response)

    def create(self,
               description=None,
               local_accounting=None,
               name=None,
               prefix_delimiter=None,
               prefix_strip=None,
               remote_accounting=None,
               server_list=None,
               suffix_delimiter=None,
               suffix_strip=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_tacacs_server_sequence <#ciscoisesdk.
        api.v3_1_0.tacacs_server_sequence.
        TacacsServerSequence.create_tacacs_server_sequence>`_
        """
        return self.create_tacacs_server_sequence(
            description=description,
            local_accounting=local_accounting,
            name=name,
            prefix_delimiter=prefix_delimiter,
            prefix_strip=prefix_strip,
            remote_accounting=remote_accounting,
            server_list=server_list,
            suffix_delimiter=suffix_delimiter,
            suffix_strip=suffix_strip,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the TACACS server sequence.

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

        e_url = ('/ers/config/tacacsserversequence/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aa8e1dc47a445d44ab86020f421ee721_v3_1_0', _api_response)
