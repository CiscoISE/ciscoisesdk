# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine guestuser API wrapper.

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


class Guestuser(object):
    """Identity Services Engine guestuser API (version: 3.5.0).

    Wraps the Identity Services Engine guestuser
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Guestuser
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Guestuser, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_guestuser(self,
                      filter=None,
                      page=None,
                      size=None,
                      sortasc=None,
                      sortdsc=None,
                      headers=None,
                      **query_parameters):
        """Get-All.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[lastName, sponsor, creationTime,
                personBeingVisited, toDate, userName,
                firstName, emailAddress, phoneNumber,
                groupTag, name, company, guestType,
                status].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[firstName, lastName,
                emailAddress, name, description].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[firstName, lastName,
                emailAddress, name, description].
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
        check_type(filter, str)
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))
        check_type(sortdsc, str)
        check_type(sortasc, str)

        _params = {
            'filter':
                filter,
            'page':
                page,
            'size':
                size,
            'sortdsc':
                sortdsc,
            'sortasc':
                sortasc,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/guestuser/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cc79b953608d2945ac7baff28f_v3_5_0', _api_response)

    def get_guestuser_generator(self,
                                filter=None,
                                page=None,
                                size=None,
                                sortasc=None,
                                sortdsc=None,
                                headers=None,
                                **query_parameters):
        """Get-All.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[lastName, sponsor, creationTime,
                personBeingVisited, toDate, userName,
                firstName, emailAddress, phoneNumber,
                groupTag, name, company, guestType,
                status].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[firstName, lastName,
                emailAddress, name, description].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[firstName, lastName,
                emailAddress, name, description].
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
            self.get_guestuser, dict(
                filter=filter,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_guestuser(self,
                         custom_fields=None,
                         description=None,
                         guest_access_info=None,
                         guest_info=None,
                         guest_type=None,
                         id=None,
                         name=None,
                         person_being_visited=None,
                         portal_id=None,
                         reason_for_visit=None,
                         sponsor_user_id=None,
                         sponsor_user_name=None,
                         status=None,
                         status_reason=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **query_parameters):
        """Create.

        Args:
            custom_fields(object): Key value map, property of the
                request body.
            description(string): Description, property of the
                request body.
            guest_access_info(object): guestAccessInfo, property of
                the request body.
            guest_info(object): guestInfo, property of the request
                body.
            guest_type(string): guestType, property of the request
                body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            person_being_visited(string): personBeingVisited,
                property of the request body.
            portal_id(string): This field is applicable only for
                Create and Update operations not
                applicable for Get operation. Portal ID
                will be used to fetch configuration from
                Portal if missing from the Payload. For
                example Notification Language will be
                fetched from Portal if missing.,
                property of the request body.
            reason_for_visit(string): reasonForVisit, property of
                the request body.
            sponsor_user_id(string): This field is applicable only
                for Get operation not applicable for
                Create and Update operations., property
                of the request body.
            sponsor_user_name(string): This field is applicable for
                Get and Create operations not applicable
                for Update operation., property of the
                request body.
            status(string): This field is applicable only for Get
                operation not applicable for Create and
                Update operations., property of the
                request body.
            status_reason(string): statusReason, property of the
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
                'customFields':
                    custom_fields,
                'guestType':
                    guest_type,
                'status':
                    status,
                'reasonForVisit':
                    reason_for_visit,
                'personBeingVisited':
                    person_being_visited,
                'sponsorUserName':
                    sponsor_user_name,
                'sponsorUserId':
                    sponsor_user_id,
                'statusReason':
                    status_reason,
                'portalId':
                    portal_id,
                'guestAccessInfo':
                    guest_access_info,
                'guestInfo':
                    guest_info,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'GuestUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_af81d98c8c975c958b50606d164e2f57_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_af81d98c8c975c958b50606d164e2f57_v3_5_0', _api_response)

    def update_guestuser_deny_by_id(self,
                                    id,
                                    headers=None,
                                    **query_parameters):
        """deny.

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

        e_url = ('/ers/config/guestuser/deny/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1e5e2a187652018c59b10155ac973d_v3_5_0', _api_response)

    def update_guestuser_suspend_by_id(self,
                                       id,
                                       additional_data=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """suspendById.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of any objects).
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
        _payload = payload or {}
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_be5b1e320e55f4a181370417471d9e_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser/suspend/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_be5b1e320e55f4a181370417471d9e_v3_5_0', _api_response)

    def update_guestuser_approve_by_id(self,
                                       id,
                                       headers=None,
                                       **query_parameters):
        """approve.

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

        e_url = ('/ers/config/guestuser/approve/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c67b4dcffba052ae8ece775bc61a1c21_v3_5_0', _api_response)

    def get_guestuser_name_by_name(self,
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

        e_url = ('/ers/config/guestuser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bcb7ec29968e5d5899df4a90d94ed659_v3_5_0', _api_response)

    def update_guestuser_name_by_name(self,
                                      name,
                                      custom_fields=None,
                                      description=None,
                                      guest_access_info=None,
                                      guest_info=None,
                                      guest_type=None,
                                      id=None,
                                      person_being_visited=None,
                                      portal_id=None,
                                      reason_for_visit=None,
                                      sponsor_user_id=None,
                                      sponsor_user_name=None,
                                      status=None,
                                      status_reason=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """UpdateByName.

        Args:
            custom_fields(object): Key value map, property of the
                request body.
            description(string): Description, property of the
                request body.
            guest_access_info(object): guestAccessInfo, property of
                the request body.
            guest_info(object): guestInfo, property of the request
                body.
            guest_type(string): guestType, property of the request
                body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            person_being_visited(string): personBeingVisited,
                property of the request body.
            portal_id(string): This field is applicable only for
                Create and Update operations not
                applicable for Get operation. Portal ID
                will be used to fetch configuration from
                Portal if missing from the Payload. For
                example Notification Language will be
                fetched from Portal if missing.,
                property of the request body.
            reason_for_visit(string): reasonForVisit, property of
                the request body.
            sponsor_user_id(string): This field is applicable only
                for Get operation not applicable for
                Create and Update operations., property
                of the request body.
            sponsor_user_name(string): This field is applicable for
                Get and Create operations not applicable
                for Update operation., property of the
                request body.
            status(string): This field is applicable only for Get
                operation not applicable for Create and
                Update operations., property of the
                request body.
            status_reason(string): statusReason, property of the
                request body.
            name(str): name path parameter.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'customFields':
                    custom_fields,
                'guestType':
                    guest_type,
                'status':
                    status,
                'reasonForVisit':
                    reason_for_visit,
                'personBeingVisited':
                    person_being_visited,
                'sponsorUserName':
                    sponsor_user_name,
                'sponsorUserId':
                    sponsor_user_id,
                'statusReason':
                    status_reason,
                'portalId':
                    portal_id,
                'guestAccessInfo':
                    guest_access_info,
                'guestInfo':
                    guest_info,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'GuestUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f24049df29d059c48eef86d381ffad5d_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f24049df29d059c48eef86d381ffad5d_v3_5_0', _api_response)

    def delete_guestuser_name_by_name(self,
                                      name,
                                      headers=None,
                                      **query_parameters):
        """DeleteByName.

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

        e_url = ('/ers/config/guestuser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ef15d7c6b259f5859ee9675c38887c_v3_5_0', _api_response)

    def update_guestuser_sms_portalid_by_id(self,
                                            id,
                                            portal_id,
                                            headers=None,
                                            **query_parameters):
        """sms.

        Args:
            id(str): id path parameter.
            portal_id(str): portalId path parameter.
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
        check_type(portal_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
            'portalId': portal_id,
        }

        e_url = ('/ers/config/guestuser/sms/{id}/portalId/{portalId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ba14b751f98206ca2e19cff3fe_v3_5_0', _api_response)

    def update_guestuser_changesponsorpassword(self,
                                               portal_id,
                                               additional_data=None,
                                               headers=None,
                                               payload=None,
                                               active_validation=True,
                                               **query_parameters):
        """changeSponsorPassword.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of any objects).
            portal_id(str): portalId path parameter.
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
        check_type(portal_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'portalId': portal_id,
        }
        _payload = payload or {}
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eb3472c4de150828b2dae61e2285313_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser/changeSponsorPassword/{portalId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_eb3472c4de150828b2dae61e2285313_v3_5_0', _api_response)

    def update_guestuser_resetpassword_by_id(self,
                                             id,
                                             headers=None,
                                             **query_parameters):
        """resetpassword.

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

        e_url = ('/ers/config/guestuser/resetpassword/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea6ea4e41d85f83b6f6c10ce38bb9ed_v3_5_0', _api_response)

    def update_guestuser_email_portalid_by_id(self,
                                              id,
                                              portal_id,
                                              custom_fields=None,
                                              description=None,
                                              guest_access_info=None,
                                              guest_info=None,
                                              guest_type=None,
                                              name=None,
                                              person_being_visited=None,
                                              reason_for_visit=None,
                                              sponsor_user_id=None,
                                              sponsor_user_name=None,
                                              status=None,
                                              status_reason=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **query_parameters):
        """email.

        Args:
            custom_fields(object): Key value map, property of the
                request body.
            description(string): Description, property of the
                request body.
            guest_access_info(object): guestAccessInfo, property of
                the request body.
            guest_info(object): guestInfo, property of the request
                body.
            guest_type(string): guestType, property of the request
                body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            person_being_visited(string): personBeingVisited,
                property of the request body.
            portal_id(string): This field is applicable only for
                Create and Update operations not
                applicable for Get operation. Portal ID
                will be used to fetch configuration from
                Portal if missing from the Payload. For
                example Notification Language will be
                fetched from Portal if missing.,
                property of the request body.
            reason_for_visit(string): reasonForVisit, property of
                the request body.
            sponsor_user_id(string): This field is applicable only
                for Get operation not applicable for
                Create and Update operations., property
                of the request body.
            sponsor_user_name(string): This field is applicable for
                Get and Create operations not applicable
                for Update operation., property of the
                request body.
            status(string): This field is applicable only for Get
                operation not applicable for Create and
                Update operations., property of the
                request body.
            status_reason(string): statusReason, property of the
                request body.
            id(str): id path parameter.
            portal_id(str): portalId path parameter.
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
        check_type(portal_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
            'portalId': portal_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'customFields':
                    custom_fields,
                'guestType':
                    guest_type,
                'status':
                    status,
                'reasonForVisit':
                    reason_for_visit,
                'personBeingVisited':
                    person_being_visited,
                'sponsorUserName':
                    sponsor_user_name,
                'sponsorUserId':
                    sponsor_user_id,
                'statusReason':
                    status_reason,
                'portalId':
                    portal_id,
                'guestAccessInfo':
                    guest_access_info,
                'guestInfo':
                    guest_info,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'GuestUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a9fa9cbccbe50fcb1cd6a63fed47578_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser/email/{id}/portalId/{portalId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a9fa9cbccbe50fcb1cd6a63fed47578_v3_5_0', _api_response)

    def update_guestuser_reinstate_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """reinstateById.

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

        e_url = ('/ers/config/guestuser/reinstate/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dfcba4a0f685c168bdf2b5b2be317ac_v3_5_0', _api_response)

    def update_guestuser_reinstate_name_by_name(self,
                                                name,
                                                headers=None,
                                                **query_parameters):
        """reinstateByName.

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

        e_url = ('/ers/config/guestuser/reinstate/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b21045846d5097a82cd61cb3c7eaf1_v3_5_0', _api_response)

    def update_guestuser_suspend_name_by_name(self,
                                              name,
                                              headers=None,
                                              **query_parameters):
        """suspendByName.

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

        e_url = ('/ers/config/guestuser/suspend/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afcc8fe53b4824ae744a2ff3848_v3_5_0', _api_response)

    def get_guestuser_by_id(self,
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

        e_url = ('/ers/config/guestuser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c3c7d5a3a83d9f7441972d399_v3_5_0', _api_response)

    def update_guestuser_by_id(self,
                               id,
                               custom_fields=None,
                               description=None,
                               guest_access_info=None,
                               guest_info=None,
                               guest_type=None,
                               name=None,
                               person_being_visited=None,
                               portal_id=None,
                               reason_for_visit=None,
                               sponsor_user_id=None,
                               sponsor_user_name=None,
                               status=None,
                               status_reason=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """UpdateById.

        Args:
            custom_fields(object): Key value map, property of the
                request body.
            description(string): Description, property of the
                request body.
            guest_access_info(object): guestAccessInfo, property of
                the request body.
            guest_info(object): guestInfo, property of the request
                body.
            guest_type(string): guestType, property of the request
                body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            person_being_visited(string): personBeingVisited,
                property of the request body.
            portal_id(string): This field is applicable only for
                Create and Update operations not
                applicable for Get operation. Portal ID
                will be used to fetch configuration from
                Portal if missing from the Payload. For
                example Notification Language will be
                fetched from Portal if missing.,
                property of the request body.
            reason_for_visit(string): reasonForVisit, property of
                the request body.
            sponsor_user_id(string): This field is applicable only
                for Get operation not applicable for
                Create and Update operations., property
                of the request body.
            sponsor_user_name(string): This field is applicable for
                Get and Create operations not applicable
                for Update operation., property of the
                request body.
            status(string): This field is applicable only for Get
                operation not applicable for Create and
                Update operations., property of the
                request body.
            status_reason(string): statusReason, property of the
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
                'customFields':
                    custom_fields,
                'guestType':
                    guest_type,
                'status':
                    status,
                'reasonForVisit':
                    reason_for_visit,
                'personBeingVisited':
                    person_being_visited,
                'sponsorUserName':
                    sponsor_user_name,
                'sponsorUserId':
                    sponsor_user_id,
                'statusReason':
                    status_reason,
                'portalId':
                    portal_id,
                'guestAccessInfo':
                    guest_access_info,
                'guestInfo':
                    guest_info,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'GuestUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b9c7c5847b17684c49399ff95_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b9c7c5847b17684c49399ff95_v3_5_0', _api_response)

    def delete_guestuser_by_id(self,
                               id,
                               headers=None,
                               **query_parameters):
        """DeleteById.

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

        e_url = ('/ers/config/guestuser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e251b39f55d3ac2570a963a3ee9c_v3_5_0', _api_response)
