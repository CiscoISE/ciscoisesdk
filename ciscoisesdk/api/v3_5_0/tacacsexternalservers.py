# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine tacacsexternalservers API wrapper.

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


class Tacacsexternalservers(object):
    """Identity Services Engine tacacsexternalservers API (version: 3.5.0).

    Wraps the Identity Services Engine tacacsexternalservers
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Tacacsexternalservers
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Tacacsexternalservers, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_tacacsexternalservers(self,
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

        e_url = ('/ers/config/tacacsexternalservers/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a70502d05e8682736372bb52b0ca_v3_5_0', _api_response)

    def get_tacacsexternalservers_generator(self,
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
            self.get_tacacsexternalservers, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_tacacsexternalservers(self,
                                     connection_port=None,
                                     description=None,
                                     host_ip=None,
                                     id=None,
                                     name=None,
                                     shared_secret=None,
                                     single_connect=None,
                                     timeout=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Create.

        Args:
            connection_port(number): The port to connect the server,
                property of the request body.
            description(string): Description, property of the
                request body.
            host_ip(string): The server IPV4 address, property of
                the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            shared_secret(string): The server shared secret,
                property of the request body.
            single_connect(boolean): define the use of single
                connection, property of the request
                body.
            timeout(number): The server timeout, property of the
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
                'connectionPort':
                    connection_port,
                'singleConnect':
                    single_connect,
                'sharedSecret':
                    shared_secret,
                'timeout':
                    timeout,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'TacacsExternalServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e350672560a565392fbdafefd5f08a8_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsexternalservers/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e350672560a565392fbdafefd5f08a8_v3_5_0', _api_response)

    def get_tacacsexternalservers_name_by_name(self,
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

        e_url = ('/ers/config/tacacsexternalservers/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afe1108b1a59539ebe3de3e5652c9653_v3_5_0', _api_response)

    def get_tacacsexternalservers_by_id(self,
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

        e_url = ('/ers/config/tacacsexternalservers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b9eb9547216547cab8b9e686eee674b_v3_5_0', _api_response)

    def update_tacacsexternalservers_by_id(self,
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
        """Update.

        Args:
            connection_port(number): The port to connect the server,
                property of the request body.
            description(string): Description, property of the
                request body.
            host_ip(string): The server IPV4 address, property of
                the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            shared_secret(string): The server shared secret,
                property of the request body.
            single_connect(boolean): define the use of single
                connection, property of the request
                body.
            timeout(number): The server timeout, property of the
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
                'connectionPort':
                    connection_port,
                'singleConnect':
                    single_connect,
                'sharedSecret':
                    shared_secret,
                'timeout':
                    timeout,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'TacacsExternalServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a7cffe3bfae55aa81b7b4447519e4cd_v3_5_0')\
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

        return self._object_factory('bpm_a7cffe3bfae55aa81b7b4447519e4cd_v3_5_0', _api_response)

    def delete_tacacsexternalservers_by_id(self,
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

        e_url = ('/ers/config/tacacsexternalservers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_2564523798353b885b115048_v3_5_0', _api_response)

    def patch_tacacsexternalservers_by_id(self,
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
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            connection_port(number): The port to connect the server,
                property of the request body.
            description(string): Description, property of the
                request body.
            host_ip(string): The server IPV4 address, property of
                the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            shared_secret(string): The server shared secret,
                property of the request body.
            single_connect(boolean): define the use of single
                connection, property of the request
                body.
            timeout(number): The server timeout, property of the
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
                'connectionPort':
                    connection_port,
                'singleConnect':
                    single_connect,
                'sharedSecret':
                    shared_secret,
                'timeout':
                    timeout,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'TacacsExternalServer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_da64546331b051f984efb97c89c20400_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/tacacsexternalservers/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_da64546331b051f984efb97c89c20400_v3_5_0', _api_response)
