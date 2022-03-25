# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine virtualNetwork API wrapper.

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


class VirtualNetwork(object):
    """Identity Services Engine virtualNetwork API (version: 3.1.0).

    Wraps the Identity Services Engine virtualNetwork
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new VirtualNetwork
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(VirtualNetwork, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_virtual_networks(self,
                             filter=None,
                             filter_type=None,
                             page=None,
                             size=None,
                             sort=None,
                             sort_by=None,
                             headers=None,
                             **query_parameters):
        """Get all Virtual Networks.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring): filter query parameter.
                Simple filtering  should be available
                through the filter query string
                parameter. The structure of a filter is
                a triplet of field operator and value
                separated with dots. More than one
                filter can be sent. The logical operator
                common to ALL filter criteria will be by
                default AND, and can be changed by using
                the  "filterType=or"  query string
                parameter. Each resource Data model
                description should specify if an
                attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
                .
            filter_type(basestring): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sort, basestring)
        check_type(sort_by, basestring)
        check_type(filter, basestring)
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sort':
                sort,
            'sortBy':
                sort_by,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/trustsec/virtualnetwork')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bd42dc595dd68ab56120039f89f1_v3_1_0', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sort=None,
                sort_by=None,
                headers=None,
                **query_parameters):
        """Alias for `get_virtual_networks <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.get_virtual_networks>`_
        """
        return self.get_virtual_networks(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sort=sort,
            sort_by=sort_by,
            headers=headers,
            **query_parameters
        )

    def get_virtual_networks_generator(self,
                                       filter=None,
                                       filter_type=None,
                                       page=None,
                                       size=None,
                                       sort=None,
                                       sort_by=None,
                                       headers=None,
                                       **query_parameters):
        """Get all Virtual Networks.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring): filter query parameter.
                Simple filtering  should be available
                through the filter query string
                parameter. The structure of a filter is
                a triplet of field operator and value
                separated with dots. More than one
                filter can be sent. The logical operator
                common to ALL filter criteria will be by
                default AND, and can be changed by using
                the  "filterType=or"  query string
                parameter. Each resource Data model
                description should specify if an
                attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
                .
            filter_type(basestring): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
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
            self.get_virtual_networks, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sort=sort,
                sort_by=sort_by,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def get_all_generator(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sort=None,
                          sort_by=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_virtual_networks_generator <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.get_virtual_networks_generator>`_
        """
        yield from get_next_page(
            self.get_virtual_networks, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sort=sort,
                sort_by=sort_by,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def create_virtual_network(self,
                               additional_attributes=None,
                               id=None,
                               last_update=None,
                               name=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """Create Virtual Network.

        Args:
            additional_attributes(string): JSON String of additional
                attributes for the Virtual Network,
                property of the request body.
            id(string): Identifier of the Virtual Network, property
                of the request body.
            last_update(string): Timestamp for the last update of
                the Virtual Network, property of the
                request body.
            name(string): Name of the Virtual Network, property of
                the request body.
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
            pass

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
            _payload = {
                'additionalAttributes':
                    additional_attributes,
                'id':
                    id,
                'lastUpdate':
                    last_update,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fe478ea1775758638d714efe1b67eec2_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/virtualnetwork')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_fe478ea1775758638d714efe1b67eec2_v3_1_0', _api_response)

    def create(self,
               additional_attributes=None,
               id=None,
               last_update=None,
               name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_virtual_network <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.create_virtual_network>`_
        """
        return self.create_virtual_network(
            additional_attributes=additional_attributes,
            id=id,
            last_update=last_update,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def bulk_create_virtual_networks(self,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Create Virtual Network in bulk.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, list)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f7253733d7025c8b8459478b159e84fc_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/virtualnetwork/bulk/create')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f7253733d7025c8b8459478b159e84fc_v3_1_0', _api_response)

    def bulk_request_create(self,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Alias for `bulk_create_virtual_networks <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.bulk_create_virtual_networks>`_
        """
        return self.bulk_create_virtual_networks(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def bulk_delete_virtual_networks(self,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Delete Virtual Network in bulk.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, list)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b6cdd5dd57b95d8bac87ce9600a84b5d_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/virtualnetwork/bulk/delete')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b6cdd5dd57b95d8bac87ce9600a84b5d_v3_1_0', _api_response)

    def bulk_request_delete(self,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Alias for `bulk_delete_virtual_networks <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.bulk_delete_virtual_networks>`_
        """
        return self.bulk_delete_virtual_networks(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def bulk_update_virtual_networks(self,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Update Virtual Network in bulk.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, list)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e3c62bba9f9e5344a38479f6437cf8b4_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/virtualnetwork/bulk/update')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e3c62bba9f9e5344a38479f6437cf8b4_v3_1_0', _api_response)

    def bulk_request_update(self,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Alias for `bulk_update_virtual_networks <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.bulk_update_virtual_networks>`_
        """
        return self.bulk_update_virtual_networks(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_virtual_network_by_id(self,
                                  id,
                                  headers=None,
                                  **query_parameters):
        """Get Virtual Network by id.

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
            pass

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

        e_url = ('/api/v1/trustsec/virtualnetwork/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d89686dd9cb05c02833cdefc5d3ba9f2_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_virtual_network_by_id <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.get_virtual_network_by_id>`_
        """
        return self.get_virtual_network_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_virtual_network_by_id(self,
                                     id,
                                     additional_attributes=None,
                                     last_update=None,
                                     name=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Update Virtual Network.

        Args:
            additional_attributes(string): JSON String of additional
                attributes for the Virtual Network,
                property of the request body.
            id(string): Identifier of the Virtual Network, property
                of the request body.
            last_update(string): Timestamp for the last update of
                the Virtual Network, property of the
                request body.
            name(string): Name of the Virtual Network, property of
                the request body.
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
            pass

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
            _payload = {
                'additionalAttributes':
                    additional_attributes,
                'id':
                    id,
                'lastUpdate':
                    last_update,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d02f9a7ed46581b8baf07e182f80695_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/virtualnetwork/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d02f9a7ed46581b8baf07e182f80695_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     additional_attributes=None,
                     last_update=None,
                     name=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_virtual_network_by_id <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.update_virtual_network_by_id>`_
        """
        return self.update_virtual_network_by_id(
            id=id,
            additional_attributes=additional_attributes,
            last_update=last_update,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_virtual_network_by_id(self,
                                     id,
                                     headers=None,
                                     **query_parameters):
        """Delete Virtual Network.

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
            pass

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

        e_url = ('/api/v1/trustsec/virtualnetwork/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f7fda88868581085da6ac8c0e04b5c_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_virtual_network_by_id <#ciscoisesdk.
        api.v3_1_0.virtual_network.
        VirtualNetwork.delete_virtual_network_by_id>`_
        """
        return self.delete_virtual_network_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )
