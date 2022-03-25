# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine sgVnMapping API wrapper.

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


class SgVnMapping(object):
    """Identity Services Engine sgVnMapping API (version: 3.1.0).

    Wraps the Identity Services Engine sgVnMapping
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SgVnMapping
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SgVnMapping, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_sg_vn_mappings(self,
                           filter=None,
                           filter_type=None,
                           page=None,
                           size=None,
                           sort=None,
                           sort_by=None,
                           headers=None,
                           **query_parameters):
        """Get all Security Group and Virtual Network mappings.

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

        e_url = ('/api/v1/trustsec/sgvnmapping')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e69e3338166d5c1887e5fa82efb72a11_v3_1_0', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sort=None,
                sort_by=None,
                headers=None,
                **query_parameters):
        """Alias for `get_sg_vn_mappings <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.get_sg_vn_mappings>`_
        """
        return self.get_sg_vn_mappings(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sort=sort,
            sort_by=sort_by,
            headers=headers,
            **query_parameters
        )

    def get_sg_vn_mappings_generator(self,
                                     filter=None,
                                     filter_type=None,
                                     page=None,
                                     size=None,
                                     sort=None,
                                     sort_by=None,
                                     headers=None,
                                     **query_parameters):
        """Get all Security Group and Virtual Network mappings.

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
            self.get_sg_vn_mappings, dict(
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
        """Alias for `get_sg_vn_mappings_generator <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.get_sg_vn_mappings_generator>`_
        """
        yield from get_next_page(
            self.get_sg_vn_mappings, dict(
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

    def create_sg_vn_mapping(self,
                             id=None,
                             last_update=None,
                             sg_name=None,
                             sgt_id=None,
                             vn_id=None,
                             vn_name=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """Create Security Group and Virtual Network mapping.

        Args:
            id(string): Identifier of the SG-VN mapping, property of
                the request body.
            last_update(string): Timestamp for the last update of
                the SG-VN mapping, property of the
                request body.
            sg_name(string): Name of the associated Security Group
                to be used for identity if id is not
                provided, property of the request body.
            sgt_id(string): Identifier of the associated Security
                Group which is required unless its name
                is provided, property of the request
                body.
            vn_id(string): Identifier for the associated Virtual
                Network which is required unless its
                name is provided, property of the
                request body.
            vn_name(string): Name of the associated Virtual Network
                to be used for identity if id is not
                provided, property of the request body.
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
                'id':
                    id,
                'lastUpdate':
                    last_update,
                'sgName':
                    sg_name,
                'sgtId':
                    sgt_id,
                'vnId':
                    vn_id,
                'vnName':
                    vn_name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b050fff6a5302ace3e16674c8b19a_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/sgvnmapping')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b050fff6a5302ace3e16674c8b19a_v3_1_0', _api_response)

    def create(self,
               id=None,
               last_update=None,
               sg_name=None,
               sgt_id=None,
               vn_id=None,
               vn_name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_sg_vn_mapping <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.create_sg_vn_mapping>`_
        """
        return self.create_sg_vn_mapping(
            id=id,
            last_update=last_update,
            sg_name=sg_name,
            sgt_id=sgt_id,
            vn_id=vn_id,
            vn_name=vn_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def bulk_create_sg_vn_mappings(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Create SG-VN Mappings in bulk.

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
            self._request_validator('jsd_e81b5f00f35577dbad11186f70f25be_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/sgvnmapping/bulk/create')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e81b5f00f35577dbad11186f70f25be_v3_1_0', _api_response)

    def bulk_request_create(self,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Alias for `bulk_create_sg_vn_mappings <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.bulk_create_sg_vn_mappings>`_
        """
        return self.bulk_create_sg_vn_mappings(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def bulk_delete_sg_vn_mappings(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Delete SG-VN Mappings in bulk.

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
            self._request_validator('jsd_c5cad090a875d9d8bd87e59654c9d75_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/sgvnmapping/bulk/delete')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c5cad090a875d9d8bd87e59654c9d75_v3_1_0', _api_response)

    def bulk_request_delete(self,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Alias for `bulk_delete_sg_vn_mappings <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.bulk_delete_sg_vn_mappings>`_
        """
        return self.bulk_delete_sg_vn_mappings(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def bulk_update_sg_vn_mappings(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Update SG-VN Mappings in bulk.

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
            self._request_validator('jsd_c9c798a8ce58b88b3231575f5b8c98_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/sgvnmapping/bulk/update')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c9c798a8ce58b88b3231575f5b8c98_v3_1_0', _api_response)

    def bulk_request_update(self,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Alias for `bulk_update_sg_vn_mappings <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.bulk_update_sg_vn_mappings>`_
        """
        return self.bulk_update_sg_vn_mappings(
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_sg_vn_mapping_by_id(self,
                                id,
                                headers=None,
                                **query_parameters):
        """Get Security Group and Virtual Network mapping by id.

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

        e_url = ('/api/v1/trustsec/sgvnmapping/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fceb2944abb59e2a748b970ee79fbb7_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_sg_vn_mapping_by_id <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.get_sg_vn_mapping_by_id>`_
        """
        return self.get_sg_vn_mapping_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_sg_vn_mapping_by_id(self,
                                   id,
                                   last_update=None,
                                   sg_name=None,
                                   sgt_id=None,
                                   vn_id=None,
                                   vn_name=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Update Security Group and Virtual Network mapping.

        Args:
            id(string): Identifier of the SG-VN mapping, property of
                the request body.
            last_update(string): Timestamp for the last update of
                the SG-VN mapping, property of the
                request body.
            sg_name(string): Name of the associated Security Group
                to be used for identity if id is not
                provided, property of the request body.
            sgt_id(string): Identifier of the associated Security
                Group which is required unless its name
                is provided, property of the request
                body.
            vn_id(string): Identifier for the associated Virtual
                Network which is required unless its
                name is provided, property of the
                request body.
            vn_name(string): Name of the associated Virtual Network
                to be used for identity if id is not
                provided, property of the request body.
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
                'id':
                    id,
                'lastUpdate':
                    last_update,
                'sgName':
                    sg_name,
                'sgtId':
                    sgt_id,
                'vnId':
                    vn_id,
                'vnName':
                    vn_name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a66f9651fca28e85b97cf1b968_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/sgvnmapping/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a66f9651fca28e85b97cf1b968_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     last_update=None,
                     sg_name=None,
                     sgt_id=None,
                     vn_id=None,
                     vn_name=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_sg_vn_mapping_by_id <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.update_sg_vn_mapping_by_id>`_
        """
        return self.update_sg_vn_mapping_by_id(
            id=id,
            last_update=last_update,
            sg_name=sg_name,
            sgt_id=sgt_id,
            vn_id=vn_id,
            vn_name=vn_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_sg_vn_mapping_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """Delete Security Group and Virtual Network mapping.

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

        e_url = ('/api/v1/trustsec/sgvnmapping/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cb6b83a55dfb8f3536b43cfaf081_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_sg_vn_mapping_by_id <#ciscoisesdk.
        api.v3_1_0.sg_vn_mapping.
        SgVnMapping.delete_sg_vn_mapping_by_id>`_
        """
        return self.delete_sg_vn_mapping_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )
