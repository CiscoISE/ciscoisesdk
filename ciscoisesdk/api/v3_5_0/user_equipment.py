# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine User Equipment API wrapper.

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


class UserEquipment(object):
    """Identity Services Engine User Equipment API (version: 3.5.0).

    Wraps the Identity Services Engine User Equipment
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new UserEquipment
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(UserEquipment, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_user_equipments(self,
                            filter=None,
                            filter_type=None,
                            page=None,
                            size=None,
                            sortasc=None,
                            sortby=None,
                            headers=None,
                            **query_parameters):
        """Get user equipments.

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

        e_url = ('/v1/fiveg/user-equipment')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c778156b01e7574bbcdd2b32704e6519_v3_5_0', _api_response)

    def get_user_equipments_generator(self,
                                      filter=None,
                                      filter_type=None,
                                      page=None,
                                      size=None,
                                      sortasc=None,
                                      sortby=None,
                                      headers=None,
                                      **query_parameters):
        """Get user equipments.

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
            self.get_user_equipments, dict(
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

    def create_user_equipment(self,
                              description=None,
                              device_group=None,
                              imei=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Create a user equipment.

        Args:
            description(string): Description for User Equipment,
                property of the request body.
            device_group(string): Device or Endpoint Group, property
                of the request body.
            imei(string): IMEI for User Equipment, property of the
                request body. Constraints: maxLength set
                to 15 and minLength set to 14.
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
                'description':
                    description,
                'deviceGroup':
                    device_group,
                'imei':
                    imei,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a438c5c8e8e85ed3992b4b207c1e880d_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/fiveg/user-equipment')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a438c5c8e8e85ed3992b4b207c1e880d_v3_5_0', _api_response)

    def get_user_equipment_by_id(self,
                                 user_equipment_id,
                                 headers=None,
                                 **query_parameters):
        """Get the user equipment for a given ID.

        Args:
            user_equipment_id(str): userEquipmentId path parameter.
                Unique ID for a user equipment object.
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
        check_type(user_equipment_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'userEquipmentId': user_equipment_id,
        }

        e_url = ('/v1/fiveg/user-equipment/{userEquipmentId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eb7751bd605264977bcce5b14fb889_v3_5_0', _api_response)

    def update_user_equipment(self,
                              user_equipment_id,
                              description=None,
                              device_group=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Update the user equipment for a given ID and request payload.

        Args:
            description(string): Description for User Equipment,
                property of the request body.
            device_group(string): Device or Endpoint Group, property
                of the request body.
            user_equipment_id(str): userEquipmentId path parameter.
                Unique ID for a user equipment object.
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
        check_type(user_equipment_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'userEquipmentId': user_equipment_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'description':
                    description,
                'deviceGroup':
                    device_group,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f7dd56c4a513c811cb9d8dbe79e92_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/fiveg/user-equipment/{userEquipmentId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f7dd56c4a513c811cb9d8dbe79e92_v3_5_0', _api_response)

    def delete_user_equipment(self,
                              user_equipment_id,
                              headers=None,
                              **query_parameters):
        """Delete the user equipment for a given ID.

        Args:
            user_equipment_id(str): userEquipmentId path parameter.
                Unique ID for a user equipment object.
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
        check_type(user_equipment_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'userEquipmentId': user_equipment_id,
        }

        e_url = ('/v1/fiveg/user-equipment/{userEquipmentId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a42f015bf5e53679ed0802ce77d5212_v3_5_0', _api_response)

    def get_user_equipments_by_subscriber_id(self,
                                             subscriber_id,
                                             headers=None,
                                             **query_parameters):
        """Get user equipments associated with a subscriber GUID.

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

        e_url = ('/v1/fiveg/user-equipment/subscriber/{subscriberId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b9bca0058945bf9b9346268536419bc_v3_5_0', _api_response)

    def get_user_equipment_by_i_m_e_i(self,
                                      imei,
                                      headers=None,
                                      **query_parameters):
        """Get a user equipment based on the IMEI.

        Args:
            imei(str): imei path parameter. IMEI for the user
                equipment object.
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
        check_type(imei, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'imei': imei,
        }

        e_url = ('/v1/fiveg/user-equipment/imei/{imei}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e4e4412c567850adae980b9b299dc38b_v3_5_0', _api_response)

    def create_user_equipments_from_c_s_v(self,
                                          headers=None,
                                          **query_parameters):
        """Create user equipments from a CSV file.

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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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

        e_url = ('/v1/fiveg/user-equipment/csv')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c9c4b28095037a548ab2c5302903f_v3_5_0', _api_response)

    def bulk_user_equipment_operation(self,
                                      item_list=None,
                                      operation=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Create, update and delete multiple user equipments.

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
            self._request_validator('jsd_e22bd55278af818b3e325fd95_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/fiveg/user-equipment/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e22bd55278af818b3e325fd95_v3_5_0', _api_response)
