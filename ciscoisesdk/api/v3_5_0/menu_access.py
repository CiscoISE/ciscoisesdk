# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Menu Access API wrapper.

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


class MenuAccess(object):
    """Identity Services Engine Menu Access API (version: 3.5.0).

    Wraps the Identity Services Engine Menu Access
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new MenuAccess
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(MenuAccess, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def list_all_menu_access(self,
                             filter=None,
                             filter_type=None,
                             page=None,
                             size=None,
                             sort=None,
                             sort_by=None,
                             headers=None,
                             **query_parameters):
        """Get all the menu access created in Cisco ISE, example super
        admin menu access,Policy admin menu Access.

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

        e_url = ('/api/v1/rbac/menu-access')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a5a65aa6ac41185099dfcc2d_v3_5_0', _api_response)

    def list_all_menu_access_generator(self,
                                       filter=None,
                                       filter_type=None,
                                       page=None,
                                       size=None,
                                       sort=None,
                                       sort_by=None,
                                       headers=None,
                                       **query_parameters):
        """Get all the menu access created in Cisco ISE, example super
        admin menu access,Policy admin menu Access.

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
            self.list_all_menu_access, dict(
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

    def update_menu_access(self,
                           description=None,
                           menu_access_privileges=None,
                           name=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """Update details of menu access present in Cisco ISE based on the
        permissions required for specific tabs.

        Args:
            description(string): A brief description of the menu
                access request., property of the request
                body.
            menu_access_privileges(list): menuAccessPrivileges,
                property of the request body (list of
                objects).
            name(string): The name of the menu access request.,
                property of the request body.
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
                'description':
                    description,
                'menuAccessPrivileges':
                    menu_access_privileges,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_df8ee11dc4a85b46ad2fe44eb3a89475_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/rbac/menu-access')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_df8ee11dc4a85b46ad2fe44eb3a89475_v3_5_0', _api_response)

    def create_menu_access(self,
                           description=None,
                           menu_access_privileges=None,
                           name=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """Create  menu access in Cisco ISE based on the access permissions
        required to the tabs.

        Args:
            description(string): A brief description of the menu
                access request., property of the request
                body.
            menu_access_privileges(list): menuAccessPrivileges,
                property of the request body (list of
                objects).
            name(string): The name of the menu access request.,
                property of the request body.
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
                'description':
                    description,
                'menuAccessPrivileges':
                    menu_access_privileges,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c0c869427aa5cd9bfdbf2a1258a7179_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/rbac/menu-access')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c0c869427aa5cd9bfdbf2a1258a7179_v3_5_0', _api_response)

    def get_menu_access_by_name(self,
                                name,
                                headers=None,
                                **query_parameters):
        """Get details of requested menu access available in Cisco ISE,
        which has the details of all the accessible tabs.

        Args:
            name(str): name path parameter. The name of the menu
                access.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/api/v1/rbac/menu-access/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e78f56baa572caf543e9172a6654a_v3_5_0', _api_response)

    def delete_menu_access(self,
                           name,
                           headers=None,
                           **query_parameters):
        """Delete menu access API in Cisco ISE is used to delete menu
        access based on the role fulfilled.

        Args:
            name(str): name path parameter. The name of the menu
                access.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/api/v1/rbac/menu-access/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ac5a3d0038cc52548f6fb11df4bfa006_v3_5_0', _api_response)
