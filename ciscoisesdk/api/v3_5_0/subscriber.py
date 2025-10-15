# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Subscriber API wrapper.

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


class Subscriber(object):
    """Identity Services Engine Subscriber API (version: 3.5.0).

    Wraps the Identity Services Engine Subscriber
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Subscriber
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Subscriber, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_subscribers(self,
                            filter=None,
                            filter_type=None,
                            page=None,
                            size=None,
                            sortasc=None,
                            sortby=None,
                            headers=None,
                            **query_parameters):
        """Get all subscribers.

        Args:
            page(int): page query parameter. Page number of the
                results to fetch. First page is 1.
            size(int): size query parameter. Number of results per
                page.
            filter(str): filter query parameter. Filter criteria for
                the query.  Format:
                attribute.operator.value Operators: EQ
                (equals), NEQ (not equals), GT (greater
                than), LT (less than),  STARTSW (starts
                with), NSTARTSW (not starts with), ENDSW
                (ends with),  NENDSW (not ends with),
                CONTAINS (contains), NCONTAINS (not
                contains) .
            filter_type(str): filterType query parameter. The
                logical operator for multiple filters
                (AND, OR).
            sortasc(bool): sortasc query parameter. Sort order (true
                for ascending, false for descending).
            sortby(str): sortby query parameter. Field name to sort
                by.
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
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))
        check_type(filter, str)
        check_type(filter_type, str)
        check_type(sortasc, bool)
        check_type(sortby, str)

        _params = {
            'page':
                page,
            'size':
                size,
            'filter':
                filter,
            'filterType':
                filter_type,
            'sortasc':
                sortasc,
            'sortby':
                sortby,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/fiveg/subscriber')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4ced5c1c5d35580993c5b5aefbb3c7b_v3_5_0', _api_response)

    def get_all_subscribers_generator(self,
                                      filter=None,
                                      filter_type=None,
                                      page=None,
                                      size=None,
                                      sortasc=None,
                                      sortby=None,
                                      headers=None,
                                      **query_parameters):
        """Get all subscribers.

        Args:
            page(int): page query parameter. Page number of the
                results to fetch. First page is 1.
            size(int): size query parameter. Number of results per
                page.
            filter(str): filter query parameter. Filter criteria for
                the query.  Format:
                attribute.operator.value Operators: EQ
                (equals), NEQ (not equals), GT (greater
                than), LT (less than),  STARTSW (starts
                with), NSTARTSW (not starts with), ENDSW
                (ends with),  NENDSW (not ends with),
                CONTAINS (contains), NCONTAINS (not
                contains) .
            filter_type(str): filterType query parameter. The
                logical operator for multiple filters
                (AND, OR).
            sortasc(bool): sortasc query parameter. Sort order (true
                for ascending, false for descending).
            sortby(str): sortby query parameter. Field name to sort
                by.
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
            self.get_all_subscribers, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortby=sortby,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def create_subscriber(self,
                          enabled=None,
                          friendly_name=None,
                          identity_groups=None,
                          imeis=None,
                          imsi=None,
                          ki=None,
                          opc=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """Create subscriber holding the IMEI.

        Args:
            enabled(boolean): Subscriber is enabled or not, property
                of the request body.
            friendly_name(string): Friendly name for the subscriber,
                property of the request body.
            identity_groups(string): Identity Groups. If you add
                more than one identity group, they need
                to be comma separated., property of the
                request body.
            imeis(string): IMEI to be attached to the subscriber,
                property of the request body.
            imsi(string): IMSI for subscriber, property of the
                request body.
            ki(string): KI, property of the request body.
            opc(string): OPC, property of the request body.
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
                'enabled':
                    enabled,
                'friendlyName':
                    friendly_name,
                'identityGroups':
                    identity_groups,
                'imeis':
                    imeis,
                'opc':
                    opc,
                'ki':
                    ki,
                'imsi':
                    imsi,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cd743fd78db5d9998053e6ed51bcc58_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/fiveg/subscriber')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_cd743fd78db5d9998053e6ed51bcc58_v3_5_0', _api_response)

    def get_subscriber_by_id(self,
                             subscriber_id,
                             headers=None,
                             **query_parameters):
        """Get the subscriber for a given ID.

        Args:
            subscriber_id(str): subscriberId path parameter. Unique
                ID for a subscriber object.
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
        check_type(subscriber_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'subscriberId': subscriber_id,
        }

        e_url = ('/v1/fiveg/subscriber/{subscriberId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a87a0d90be514e9fff9aba1a40039a_v3_5_0', _api_response)

    def update_subscriber(self,
                          subscriber_id,
                          enabled=None,
                          friendly_name=None,
                          identity_groups=None,
                          imeis=None,
                          ki=None,
                          opc=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """Update a subscriber for a given ID and the request payload.

        Args:
            enabled(boolean): Subscriber is enabled or not, property
                of the request body.
            friendly_name(string): Friendly name for the subscriber,
                property of the request body.
            identity_groups(string): Identity Groups. If you add
                more than one identity group, they need
                to be comma separated., property of the
                request body.
            imeis(string): IMEI to be attached to the subscriber,
                property of the request body.
            ki(string): KI, property of the request body.
            opc(string): OPC, property of the request body.
            subscriber_id(str): subscriberId path parameter. Unique
                ID for a subscriber object.
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
        check_type(subscriber_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'subscriberId': subscriber_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'enabled':
                    enabled,
                'friendlyName':
                    friendly_name,
                'identityGroups':
                    identity_groups,
                'imeis':
                    imeis,
                'opc':
                    opc,
                'ki':
                    ki,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d93e02951b665bf8ad6763d741820ccc_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/fiveg/subscriber/{subscriberId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d93e02951b665bf8ad6763d741820ccc_v3_5_0', _api_response)

    def delete_subscriber(self,
                          subscriber_id,
                          headers=None,
                          **query_parameters):
        """Delete the subscriber for a given ID.

        Args:
            subscriber_id(str): subscriberId path parameter. Unique
                ID for a subscriber object.
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
        check_type(subscriber_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'subscriberId': subscriber_id,
        }

        e_url = ('/v1/fiveg/subscriber/{subscriberId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c4940b5f19b09e1af373ade9bc_v3_5_0', _api_response)

    def get_subscriber_by_i_m_s_i(self,
                                  imsi,
                                  headers=None,
                                  **query_parameters):
        """Get a subscriber by IMSI.

        Args:
            imsi(str): imsi path parameter. IMSI parameter.
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
        check_type(imsi, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'imsi': imsi,
        }

        e_url = ('/v1/fiveg/subscriber/imsi/{imsi}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b5167b7471c65969ae93a5ef84217177_v3_5_0', _api_response)

    def bulk_subscriber_operation(self,
                                  item_list=None,
                                  operation=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Create, update and delete subscribers in bulk.

        Args:
            item_list(list): ItemList, property of the request body
                (list of objects).
            operation(): operation, property of the request body.
                Available values are 'Create', 'Update'
                and 'Delete'.
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
                'operation':
                    operation,
                'ItemList':
                    item_list,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c4d68e103f54a0a0090064773b8db9_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/fiveg/subscriber/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c4d68e103f54a0a0090064773b8db9_v3_5_0', _api_response)
