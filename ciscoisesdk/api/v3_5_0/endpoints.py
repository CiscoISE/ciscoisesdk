# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine endpoints API wrapper.

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


class Endpoints(object):
    """Identity Services Engine endpoints API (version: 3.5.0).

    Wraps the Identity Services Engine endpoints
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Endpoints
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Endpoints, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def list_1(self,
               filter=None,
               filter_type=None,
               page=None,
               size=None,
               sort=None,
               sort_by=None,
               headers=None,
               **query_parameters):
        """Get all endpoints.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(str): sort query parameter. sort type asc or desc.
            sort_by(str): sortBy query parameter. sort column by
                which objects needs to be sorted.
            filter(str): filter query parameter.        Simple
                filtering  should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or"  query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.            OPERATOR
                DESCRIPTION           EQ   Equals
                NEQ   Not Equals       GT   Greater Than
                LT   Less Then       STARTSW   Starts
                With       NSTARTSW   Not Starts With
                ENDSW   Ends With       NENDSW   Not
                Ends With       CONTAINS   Contains
                NCONTAINS   Not Contains         .
            filter_type(str): filterType query parameter. The
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
        check_type(sort, str)
        check_type(sort_by, str)
        check_type(filter, str)
        check_type(filter_type, str)

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

        e_url = ('/api/v1/endpoint')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_578154648184bcb37d211030_v3_5_0', _api_response)

    def list_1_generator(self,
                         filter=None,
                         filter_type=None,
                         page=None,
                         size=None,
                         sort=None,
                         sort_by=None,
                         headers=None,
                         **query_parameters):
        """Get all endpoints.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(str): sort query parameter. sort type asc or desc.
            sort_by(str): sortBy query parameter. sort column by
                which objects needs to be sorted.
            filter(str): filter query parameter.        Simple
                filtering  should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or"  query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.            OPERATOR
                DESCRIPTION           EQ   Equals
                NEQ   Not Equals       GT   Greater Than
                LT   Less Then       STARTSW   Starts
                With       NSTARTSW   Not Starts With
                ENDSW   Ends With       NENDSW   Not
                Ends With       CONTAINS   Contains
                NCONTAINS   Not Contains         .
            filter_type(str): filterType query parameter. The
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
            self.list_1, dict(
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

    def create_end_point(self,
                         connected_links=None,
                         custom_attributes=None,
                         description=None,
                         device_type=None,
                         group_id=None,
                         hardware_revision=None,
                         id=None,
                         identity_store=None,
                         identity_store_id=None,
                         ip_address=None,
                         mac=None,
                         mdm_attributes=None,
                         name=None,
                         portal_user=None,
                         product_id=None,
                         profile_id=None,
                         protocol=None,
                         serial_number=None,
                         software_revision=None,
                         static_group_assignment=None,
                         static_profile_assignment=None,
                         vendor=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **query_parameters):
        """Create Endpoint.

        Args:
            connected_links(object): connectedLinks, property of the
                request body.
            custom_attributes(object): customAttributes, property of
                the request body.
            description(string): description, property of the
                request body.
            device_type(string): deviceType, property of the request
                body.
            group_id(string): groupId, property of the request body.
            hardware_revision(string): hardwareRevision, property of
                the request body.
            id(string): id, property of the request body.
            identity_store(string): identityStore, property of the
                request body.
            identity_store_id(string): identityStoreId, property of
                the request body.
            ip_address(string): ipAddress, property of the request
                body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): mdmAttributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            product_id(string): productId, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            protocol(string): protocol, property of the request
                body.
            serial_number(string): serialNumber, property of the
                request body.
            software_revision(string): softwareRevision, property of
                the request body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            vendor(string): vendor, property of the request body.
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
            _payload = {
                'connectedLinks':
                    connected_links,
                'customAttributes':
                    custom_attributes,
                'description':
                    description,
                'deviceType':
                    device_type,
                'groupId':
                    group_id,
                'hardwareRevision':
                    hardware_revision,
                'id':
                    id,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'ipAddress':
                    ip_address,
                'mac':
                    mac,
                'mdmAttributes':
                    mdm_attributes,
                'name':
                    name,
                'portalUser':
                    portal_user,
                'productId':
                    product_id,
                'profileId':
                    profile_id,
                'protocol':
                    protocol,
                'serialNumber':
                    serial_number,
                'softwareRevision':
                    software_revision,
                'staticGroupAssignment':
                    static_group_assignment,
                'staticProfileAssignment':
                    static_profile_assignment,
                'vendor':
                    vendor,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a51ed0d2536b9df3968e4773abe6_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/endpoint')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a51ed0d2536b9df3968e4773abe6_v3_5_0', _api_response)

    def update_bulk_end_points(self,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """Update Endpoint in bulk.

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
            check_type(payload, str)
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
            self._request_validator('jsd_e076428d49535723a07a5bbcbcbd128d_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/endpoint/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e076428d49535723a07a5bbcbcbd128d_v3_5_0', _api_response)

    def create_bulk_end_points(self,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """Create Endpoint in bulk.

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
            check_type(payload, str)
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
            self._request_validator('jsd_dcda215550553980db1cd60c7314a7_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/endpoint/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_dcda215550553980db1cd60c7314a7_v3_5_0', _api_response)

    def delete_bulk_end_points(self,
                               headers=None,
                               **query_parameters):
        """Delete Endpoint in bulk.

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
            pass

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

        e_url = ('/api/v1/endpoint/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d43c525d23b5c4bba03a0c774d4d411_v3_5_0', _api_response)

    def get_device_type_summary(self,
                                headers=None,
                                **query_parameters):
        """Get aggregate of device types.

        Args:
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/endpoint/deviceType/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e06db5cda5ba7b82f14cbd46d262c_v3_5_0', _api_response)

    def get_1(self,
              value,
              headers=None,
              **query_parameters):
        """Get endpoint by id or MAC.

        Args:
            value(str): value path parameter. The id or MAC of the
                endpoint.
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
        check_type(value, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'value': value,
        }

        e_url = ('/api/v1/endpoint/{value}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f190d005d391514e97e04abe777a25f6_v3_5_0', _api_response)

    def update_endpoint(self,
                        value,
                        connected_links=None,
                        custom_attributes=None,
                        description=None,
                        device_type=None,
                        group_id=None,
                        hardware_revision=None,
                        id=None,
                        identity_store=None,
                        identity_store_id=None,
                        ip_address=None,
                        mac=None,
                        mdm_attributes=None,
                        name=None,
                        portal_user=None,
                        product_id=None,
                        profile_id=None,
                        protocol=None,
                        serial_number=None,
                        software_revision=None,
                        static_group_assignment=None,
                        static_profile_assignment=None,
                        vendor=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **query_parameters):
        """Update Endpoint by id or mac.

        Args:
            connected_links(object): connectedLinks, property of the
                request body.
            custom_attributes(object): customAttributes, property of
                the request body.
            description(string): description, property of the
                request body.
            device_type(string): deviceType, property of the request
                body.
            group_id(string): groupId, property of the request body.
            hardware_revision(string): hardwareRevision, property of
                the request body.
            id(string): id, property of the request body.
            identity_store(string): identityStore, property of the
                request body.
            identity_store_id(string): identityStoreId, property of
                the request body.
            ip_address(string): ipAddress, property of the request
                body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): mdmAttributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            product_id(string): productId, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            protocol(string): protocol, property of the request
                body.
            serial_number(string): serialNumber, property of the
                request body.
            software_revision(string): softwareRevision, property of
                the request body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            vendor(string): vendor, property of the request body.
            value(str): value path parameter. The id or MAC of the
                endpoint.
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
            check_type(payload, str)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(value, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'value': value,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'connectedLinks':
                    connected_links,
                'customAttributes':
                    custom_attributes,
                'description':
                    description,
                'deviceType':
                    device_type,
                'groupId':
                    group_id,
                'hardwareRevision':
                    hardware_revision,
                'id':
                    id,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'ipAddress':
                    ip_address,
                'mac':
                    mac,
                'mdmAttributes':
                    mdm_attributes,
                'name':
                    name,
                'portalUser':
                    portal_user,
                'productId':
                    product_id,
                'profileId':
                    profile_id,
                'protocol':
                    protocol,
                'serialNumber':
                    serial_number,
                'softwareRevision':
                    software_revision,
                'staticGroupAssignment':
                    static_group_assignment,
                'staticProfileAssignment':
                    static_profile_assignment,
                'vendor':
                    vendor,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ced9c2b976d053d898d9867def5eef28_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/endpoint/{value}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_ced9c2b976d053d898d9867def5eef28_v3_5_0', _api_response)

    def delete_endpoint(self,
                        value,
                        headers=None,
                        **query_parameters):
        """Delete endpoint by id or mac.

        Args:
            value(str): value path parameter. The id or MAC of the
                endpoint.
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
        check_type(value, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'value': value,
        }

        e_url = ('/api/v1/endpoint/{value}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_de74c081ab537aadfcb4843f33e4c7_v3_5_0', _api_response)

    def create_end_point_task(self,
                              connected_links=None,
                              custom_attributes=None,
                              description=None,
                              device_type=None,
                              group_id=None,
                              hardware_revision=None,
                              id=None,
                              identity_store=None,
                              identity_store_id=None,
                              ip_address=None,
                              mac=None,
                              mdm_attributes=None,
                              name=None,
                              portal_user=None,
                              product_id=None,
                              profile_id=None,
                              protocol=None,
                              serial_number=None,
                              software_revision=None,
                              static_group_assignment=None,
                              static_profile_assignment=None,
                              vendor=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Create Endpoint task.

        Args:
            connected_links(object): connectedLinks, property of the
                request body.
            custom_attributes(object): customAttributes, property of
                the request body.
            description(string): description, property of the
                request body.
            device_type(string): deviceType, property of the request
                body.
            group_id(string): groupId, property of the request body.
            hardware_revision(string): hardwareRevision, property of
                the request body.
            id(string): id, property of the request body.
            identity_store(string): identityStore, property of the
                request body.
            identity_store_id(string): identityStoreId, property of
                the request body.
            ip_address(string): ipAddress, property of the request
                body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): mdmAttributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            product_id(string): productId, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            protocol(string): protocol, property of the request
                body.
            serial_number(string): serialNumber, property of the
                request body.
            software_revision(string): softwareRevision, property of
                the request body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            vendor(string): vendor, property of the request body.
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
                'connectedLinks':
                    connected_links,
                'customAttributes':
                    custom_attributes,
                'description':
                    description,
                'deviceType':
                    device_type,
                'groupId':
                    group_id,
                'hardwareRevision':
                    hardware_revision,
                'id':
                    id,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'ipAddress':
                    ip_address,
                'mac':
                    mac,
                'mdmAttributes':
                    mdm_attributes,
                'name':
                    name,
                'portalUser':
                    portal_user,
                'productId':
                    product_id,
                'profileId':
                    profile_id,
                'protocol':
                    protocol,
                'serialNumber':
                    serial_number,
                'softwareRevision':
                    software_revision,
                'staticGroupAssignment':
                    static_group_assignment,
                'staticProfileAssignment':
                    static_profile_assignment,
                'vendor':
                    vendor,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a7b96eb91052e49e6fc7bfc499ba5f_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/endpointTask')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a7b96eb91052e49e6fc7bfc499ba5f_v3_5_0', _api_response)
