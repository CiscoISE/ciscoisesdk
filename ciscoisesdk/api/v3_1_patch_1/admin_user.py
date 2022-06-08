# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine AdminUser API wrapper.

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


class AdminUser(object):
    """Identity Services Engine AdminUser API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine AdminUser
    API and exposes the API as native Python
    methods that return native Python objects.

    | The Admin User API allows to retrieve information related to admin users configured on Cisco ISE.

    **Revision History**

    +----------------+----------------------+-----------------------+----------------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**                  |
    +----------------+----------------------+-----------------------+----------------------------------+
    | 0              | 1.0                  | 1.2                   | Initial Cisco ISE Version        |
    +----------------+----------------------+-----------------------+----------------------------------+
    | 1              | 1.1                  | 2.0                   | Cisco ISE Release 2.3 Admin User |
    +----------------+----------------------+-----------------------+----------------------------------+

    |

    **Resource Definition**

    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | **Attribute**                | **Type** | **Required** | **Description**                                                                                           | **Example Values**                   | **Default Value** |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | name                         | String   | Yes          | Resource Name                                                                                             |                                      |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | id                           | String   | Yes          | Resource UUID                                                                                             | f9269682-dcaf-11e3-ad0a-5bdcd2d9fd69 |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | description                  | String   | No           |                                                                                                           |                                      |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | changePassword               | Boolean  | Yes          |                                                                                                           | true                                 | true              |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | email                        | String   | No           |                                                                                                           | email1@domain.com                    |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | includeSystemAlarmsInEmail   | Boolean  | No           |                                                                                                           | false                                |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | inactiveAccountNeverDisabled | Boolean  | No           |                                                                                                           | true                                 |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | enabled                      | Boolean  | Yes          |                                                                                                           | false                                |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | external                     | Boolean  | No           |                                                                                                           | true                                 |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | customAttributes             | String   | No           | Key Value Map                                                                                             | {"MyCustomAttribute" : "Value1"}     |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | firstName                    | String   | No           |                                                                                                           |                                      |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | adminGroups                  | String   | No           | Admin Group Names                                                                                         | Super Admin                          |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | lastName                     | String   | No           |                                                                                                           |                                      |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+
    | password                     | String   | No           | The password field doesn't show the actual password configured. It is hidden with the asterisk (*) symbol |                                      |                   |
    +------------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------+-------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AdminUser
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AdminUser, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_admin_user_by_id(self,
                             id,
                             headers=None,
                             **query_parameters):
        """This API allows the client to get an admin user by ID.

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

        e_url = ('/ers/config/adminuser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_adac9b81d9235be3b656acf9436583dd_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_admin_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.admin_user.
        AdminUser.get_admin_user_by_id>`_
        """
        return self.get_admin_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_admin_users(self,
                        filter=None,
                        filter_type=None,
                        page=None,
                        size=None,
                        sortasc=None,
                        sortdsc=None,
                        headers=None,
                        **query_parameters):
        """This API allows the client to get all the admin users.   Filter:
        [firstName, lastName, adminGroups, name, description,
        inactiveAccountNeverDisabled,
        includeSystemAlarmsInEmail, email, enabled]   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [name, description].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
            filter(basestring, list, set, tuple): filter query
                parameter.               **Simple
                filtering** should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or" query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.              (Operator:
                Description),
                (EQ: Equals),               (NEQ: Not
                Equals),               (GT: Greater
                Than),               (LT: Less Then),
                (STARTSW: Starts With),
                (NSTARTSW: Not Starts With),
                (ENDSW: Ends With),
                (NENDSW: Not Ends With),
                (CONTAINS: Contains),
                (NCONTAINS: Not Contains),
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
        check_type(sortasc, basestring)
        check_type(sortdsc, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sortasc':
                sortasc,
            'sortdsc':
                sortdsc,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/adminuser')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a109d72fa5ac0a64d357302f26669_v3_1_patch_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_admin_users <#ciscoisesdk.
        api.v3_1_patch_1.admin_user.
        AdminUser.get_admin_users>`_
        """
        return self.get_admin_users(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_admin_users_generator(self,
                                  filter=None,
                                  filter_type=None,
                                  page=None,
                                  size=None,
                                  sortasc=None,
                                  sortdsc=None,
                                  headers=None,
                                  **query_parameters):
        """This API allows the client to get all the admin users.   Filter:
        [firstName, lastName, adminGroups, name, description,
        inactiveAccountNeverDisabled,
        includeSystemAlarmsInEmail, email, enabled]   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [name, description].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
            filter(basestring, list, set, tuple): filter query
                parameter.               **Simple
                filtering** should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or" query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.              (Operator:
                Description),
                (EQ: Equals),               (NEQ: Not
                Equals),               (GT: Greater
                Than),               (LT: Less Then),
                (STARTSW: Starts With),
                (NSTARTSW: Not Starts With),
                (ENDSW: Ends With),
                (NENDSW: Not Ends With),
                (CONTAINS: Contains),
                (NCONTAINS: Not Contains),
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
            self.get_admin_users, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sortasc=None,
                          sortdsc=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_admin_users_generator <#ciscoisesdk.
        api.v3_1_patch_1.admin_user.
        AdminUser.get_admin_users_generator>`_
        """
        yield from get_next_page(
            self.get_admin_users, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the admin user.

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

        e_url = ('/ers/config/adminuser/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a5edeb5057839d702e0f490dc28f_v3_1_patch_1', _api_response)
