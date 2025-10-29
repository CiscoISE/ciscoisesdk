# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine pxGrid Direct Push APIs API wrapper.

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


class PxGridDirectPushApis(object):
    """Identity Services Engine pxGrid Direct Push APIs API (version: 3.5.0).

    Wraps the Identity Services Engine pxGrid Direct Push APIs
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PxGridDirectPushApis
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PxGridDirectPushApis, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_push_connector_name(self,
                                    connector_name,
                                    page=None,
                                    size=None,
                                    headers=None,
                                    **query_parameters):
        """pxGrid Direct API Get endpoint attribute data using connector
        name, optional parameters for pagination.

        Args:
            connector_name(str): connectorName path parameter. Name
                of the connector.
            size(int): size query parameter. Number of objects
                returned per page.
            page(int): page query parameter. Page number.
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
        check_type(size, (int, str, list))
        check_type(page, (int, str, list))
        check_type(connector_name, str,
                   may_be_none=False)

        _params = {
            'size':
                size,
            'page':
                page,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }

        e_url = ('/api/v1/pxgrid-direct/push/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bc81bcfcb300532cb261cb95ed7e57e6_v3_5_0', _api_response)

    def get_all_push_connector_name_generator(self,
                                              connector_name,
                                              page=None,
                                              size=None,
                                              headers=None,
                                              **query_parameters):
        """pxGrid Direct API Get endpoint attribute data using connector
        name, optional parameters for pagination.

        Args:
            connector_name(str): connectorName path parameter. Name
                of the connector.
            size(int): size query parameter. Number of objects
                returned per page.
            page(int): page query parameter. Page number.
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
            self.get_all_push_connector_name, dict(
                connector_name=connector_name,
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def bulk_operation_push_connectors(self,
                                       connector_name,
                                       data=None,
                                       operation=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """pxGrid Direct Push Bulk operator based on create/update/delete
        for the provided connector name, endpoint attribute in
        json is an array.

        Args:
            data(list): data, property of the request body (list of
                objects).
            operation(string): operation, property of the request
                body.
            connector_name(str): connectorName path parameter. Name
                of the connector.
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
        check_type(connector_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'data':
                    data,
                'operation':
                    operation,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c8b5a1bd545d598b5373d4fe6fa04b_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/pxgrid-direct/push/{connectorName}/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c8b5a1bd545d598b5373d4fe6fa04b_v3_5_0', _api_response)

    def get_push_connector_by_unique_id(self,
                                        connector_name,
                                        unique_id,
                                        headers=None,
                                        **query_parameters):
        """pxGrid Direct Push Get endpoint attribute data Based on
        UniqueID.

        Args:
            connector_name(str): connectorName path parameter. Name
                of the connector.
            unique_id(str): uniqueId path parameter. Unique ID of
                the endpoint related to the Connector.
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
        check_type(connector_name, str,
                   may_be_none=False)
        check_type(unique_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
            'uniqueId': unique_id,
        }

        e_url = ('/api/v1/pxgrid-direct/push/{connectorName}/{uniqueId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ef5cac9dddec5f4bae104da058c2dcf0_v3_5_0', _api_response)

    def update_push_connector_by_unique_id(self,
                                           connector_name,
                                           unique_id,
                                           any_json_array=None,
                                           any_json_boolean=None,
                                           any_json_integer=None,
                                           any_json_number=None,
                                           any_json_object=None,
                                           any_json_string=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **query_parameters):
        """pxGrid Direct Push Update endpoint attribute data based on
        UniqueId for the given connector name.

        Args:
            any_json_array(list): any array, property of the request
                body (list of strings).
            any_json_boolean(boolean): any boolean value, property
                of the request body.
            any_json_integer(integer): any integer, property of the
                request body.
            any_json_number(number): any number, property of the
                request body.
            any_json_object(object): anyJsonObject, property of the
                request body.
            any_json_string(string): any string, property of the
                request body.
            connector_name(str): connectorName path parameter. Name
                of the connector.
            unique_id(str): uniqueId path parameter. Unique ID of
                the endpoint related to the Connector.
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
        check_type(connector_name, str,
                   may_be_none=False)
        check_type(unique_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
            'uniqueId': unique_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'anyJsonArray':
                    any_json_array,
                'anyJsonBoolean':
                    any_json_boolean,
                'anyJsonInteger':
                    any_json_integer,
                'anyJsonNumber':
                    any_json_number,
                'anyJsonObject':
                    any_json_object,
                'anyJsonString':
                    any_json_string,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ced06c1d6ed5b70a561088f462f1291_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/pxgrid-direct/push/{connectorName}/{uniqueId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_ced06c1d6ed5b70a561088f462f1291_v3_5_0', _api_response)

    def delete_push_connector_by_unique_id(self,
                                           connector_name,
                                           unique_id,
                                           headers=None,
                                           **query_parameters):
        """pxGrid Direct Push Delete endpoint attribute data based on
        UniqueId for the given connector name.

        Args:
            connector_name(str): connectorName path parameter. Name
                of the connector.
            unique_id(str): uniqueId path parameter. Unique ID of
                the endpoint related to the Connector.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connector_name, str,
                   may_be_none=False)
        check_type(unique_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
            'uniqueId': unique_id,
        }

        e_url = ('/api/v1/pxgrid-direct/push/{connectorName}/{uniqueId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a178ac9536565091b0a6532cd6d73301_v3_5_0', _api_response)
