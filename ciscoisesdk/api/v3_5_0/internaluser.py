# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine internaluser API wrapper.

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


class Internaluser(object):
    """Identity Services Engine internaluser API (version: 3.5.0).

    Wraps the Identity Services Engine internaluser
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Internaluser
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Internaluser, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_internaluser(self,
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
                Fields:[firstName, lastName,
                identityGroup, name, description, email,
                enabled].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[daysTillPasswdExpiry,
                dateCreated, name, description,
                dateEnabled, dateModified].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[daysTillPasswdExpiry,
                dateCreated, name, description,
                dateEnabled, dateModified].
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

        e_url = ('/ers/config/internaluser/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c2892b453a29e791ef44472725b_v3_5_0', _api_response)

    def get_internaluser_generator(self,
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
                Fields:[firstName, lastName,
                identityGroup, name, description, email,
                enabled].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[daysTillPasswdExpiry,
                dateCreated, name, description,
                dateEnabled, dateModified].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[daysTillPasswdExpiry,
                dateCreated, name, description,
                dateEnabled, dateModified].
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
            self.get_internaluser, dict(
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

    def create_internaluser(self,
                            account_name_alias=None,
                            change_password=None,
                            custom_attributes=None,
                            date_created=None,
                            date_modified=None,
                            days_for_password_expiration=None,
                            description=None,
                            email=None,
                            enable_password=None,
                            enabled=None,
                            expiry_date=None,
                            expiry_date_enabled=None,
                            first_name=None,
                            id=None,
                            identity_groups=None,
                            last_name=None,
                            name=None,
                            password=None,
                            password_idstore=None,
                            password_never_expires=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Create.

        Args:
            account_name_alias(string): The Account Name Alias will
                be used to send email notifications
                about password expiration, property of
                the request body.
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(string): Key value map, property of
                the request body.
            date_created(string): The date of the user creation,
                formatted as 'YYYY-MM-DD'. Read-only.,
                property of the request body.
            date_modified(string): The date of the last user
                modification by admin, formatted as
                'YYYY-MM-DD'. Read-only., property of
                the request body.
            days_for_password_expiration(number): This field is for
                read only, property of the request body.
            description(string): Description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): EnablePassword field is added
                in ISE 2.0 to support T+, property of
                the request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): to store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD' , property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            id(string): Id, property of the request body.
            identity_groups(string): CSV of identity group IDs.,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): the id store where the
                internal user's password is kept,
                property of the request body.
            password_never_expires(boolean): Set TRUE to indicate
                the user password never expires. This
                will not apply to Users who are also ISE
                Admins, property of the request body.
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
                'changePassword':
                    change_password,
                'email':
                    email,
                'accountNameAlias':
                    account_name_alias,
                'enablePassword':
                    enable_password,
                'enabled':
                    enabled,
                'passwordNeverExpires':
                    password_never_expires,
                'daysForPasswordExpiration':
                    days_for_password_expiration,
                'customAttributes':
                    custom_attributes,
                'firstName':
                    first_name,
                'identityGroups':
                    identity_groups,
                'lastName':
                    last_name,
                'password':
                    password,
                'passwordIDStore':
                    password_idstore,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'dateModified':
                    date_modified,
                'dateCreated':
                    date_created,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d70f5bcf7885af7b2df100e10b4c88e_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/internaluser/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d70f5bcf7885af7b2df100e10b4c88e_v3_5_0', _api_response)

    def get_internaluser_name_by_name(self,
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

        e_url = ('/ers/config/internaluser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f403dda9440503191536993f569cc6f_v3_5_0', _api_response)

    def update_internaluser_name_by_name(self,
                                         name,
                                         account_name_alias=None,
                                         change_password=None,
                                         custom_attributes=None,
                                         date_created=None,
                                         date_modified=None,
                                         days_for_password_expiration=None,
                                         description=None,
                                         email=None,
                                         enable_password=None,
                                         enabled=None,
                                         expiry_date=None,
                                         expiry_date_enabled=None,
                                         first_name=None,
                                         id=None,
                                         identity_groups=None,
                                         last_name=None,
                                         password=None,
                                         password_idstore=None,
                                         password_never_expires=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """Update-By-Name.

        Args:
            account_name_alias(string): The Account Name Alias will
                be used to send email notifications
                about password expiration, property of
                the request body.
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(string): Key value map, property of
                the request body.
            date_created(string): The date of the user creation,
                formatted as 'YYYY-MM-DD'. Read-only.,
                property of the request body.
            date_modified(string): The date of the last user
                modification by admin, formatted as
                'YYYY-MM-DD'. Read-only., property of
                the request body.
            days_for_password_expiration(number): This field is for
                read only, property of the request body.
            description(string): Description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): EnablePassword field is added
                in ISE 2.0 to support T+, property of
                the request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): to store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD' , property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            id(string): Id, property of the request body.
            identity_groups(string): CSV of identity group IDs.,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): the id store where the
                internal user's password is kept,
                property of the request body.
            password_never_expires(boolean): Set TRUE to indicate
                the user password never expires. This
                will not apply to Users who are also ISE
                Admins, property of the request body.
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
                'changePassword':
                    change_password,
                'email':
                    email,
                'accountNameAlias':
                    account_name_alias,
                'enablePassword':
                    enable_password,
                'enabled':
                    enabled,
                'passwordNeverExpires':
                    password_never_expires,
                'daysForPasswordExpiration':
                    days_for_password_expiration,
                'customAttributes':
                    custom_attributes,
                'firstName':
                    first_name,
                'identityGroups':
                    identity_groups,
                'lastName':
                    last_name,
                'password':
                    password,
                'passwordIDStore':
                    password_idstore,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'dateModified':
                    date_modified,
                'dateCreated':
                    date_created,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_19d9509db339e3b27dc56b37_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/internaluser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_19d9509db339e3b27dc56b37_v3_5_0', _api_response)

    def delete_internaluser_name_by_name(self,
                                         name,
                                         headers=None,
                                         **query_parameters):
        """Delete-By-Name.

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

        e_url = ('/ers/config/internaluser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b4e2fc3e595aa1be86d6589614b9_v3_5_0', _api_response)

    def patch_internaluser_name_by_name(self,
                                        name,
                                        account_name_alias=None,
                                        change_password=None,
                                        custom_attributes=None,
                                        date_created=None,
                                        date_modified=None,
                                        days_for_password_expiration=None,
                                        description=None,
                                        email=None,
                                        enable_password=None,
                                        enabled=None,
                                        expiry_date=None,
                                        expiry_date_enabled=None,
                                        first_name=None,
                                        id=None,
                                        identity_groups=None,
                                        last_name=None,
                                        password=None,
                                        password_idstore=None,
                                        password_never_expires=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            account_name_alias(string): The Account Name Alias will
                be used to send email notifications
                about password expiration, property of
                the request body.
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(string): Key value map, property of
                the request body.
            date_created(string): The date of the user creation,
                formatted as 'YYYY-MM-DD'. Read-only.,
                property of the request body.
            date_modified(string): The date of the last user
                modification by admin, formatted as
                'YYYY-MM-DD'. Read-only., property of
                the request body.
            days_for_password_expiration(number): This field is for
                read only, property of the request body.
            description(string): Description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): EnablePassword field is added
                in ISE 2.0 to support T+, property of
                the request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): to store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD' , property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            id(string): Id, property of the request body.
            identity_groups(string): CSV of identity group IDs.,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): the id store where the
                internal user's password is kept,
                property of the request body.
            password_never_expires(boolean): Set TRUE to indicate
                the user password never expires. This
                will not apply to Users who are also ISE
                Admins, property of the request body.
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
                'changePassword':
                    change_password,
                'email':
                    email,
                'accountNameAlias':
                    account_name_alias,
                'enablePassword':
                    enable_password,
                'enabled':
                    enabled,
                'passwordNeverExpires':
                    password_never_expires,
                'daysForPasswordExpiration':
                    days_for_password_expiration,
                'customAttributes':
                    custom_attributes,
                'firstName':
                    first_name,
                'identityGroups':
                    identity_groups,
                'lastName':
                    last_name,
                'password':
                    password,
                'passwordIDStore':
                    password_idstore,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'dateModified':
                    date_modified,
                'dateCreated':
                    date_created,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b243462eb0589d866791af0b0d700d_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/internaluser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_b243462eb0589d866791af0b0d700d_v3_5_0', _api_response)

    def get_internaluser_by_id(self,
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

        e_url = ('/ers/config/internaluser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bacf1abfc35e509183c9a7f055cbbfec_v3_5_0', _api_response)

    def update_internaluser_by_id(self,
                                  id,
                                  account_name_alias=None,
                                  change_password=None,
                                  custom_attributes=None,
                                  date_created=None,
                                  date_modified=None,
                                  days_for_password_expiration=None,
                                  description=None,
                                  email=None,
                                  enable_password=None,
                                  enabled=None,
                                  expiry_date=None,
                                  expiry_date_enabled=None,
                                  first_name=None,
                                  identity_groups=None,
                                  last_name=None,
                                  name=None,
                                  password=None,
                                  password_idstore=None,
                                  password_never_expires=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Update.

        Args:
            account_name_alias(string): The Account Name Alias will
                be used to send email notifications
                about password expiration, property of
                the request body.
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(string): Key value map, property of
                the request body.
            date_created(string): The date of the user creation,
                formatted as 'YYYY-MM-DD'. Read-only.,
                property of the request body.
            date_modified(string): The date of the last user
                modification by admin, formatted as
                'YYYY-MM-DD'. Read-only., property of
                the request body.
            days_for_password_expiration(number): This field is for
                read only, property of the request body.
            description(string): Description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): EnablePassword field is added
                in ISE 2.0 to support T+, property of
                the request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): to store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD' , property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            id(string): Id, property of the request body.
            identity_groups(string): CSV of identity group IDs.,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): the id store where the
                internal user's password is kept,
                property of the request body.
            password_never_expires(boolean): Set TRUE to indicate
                the user password never expires. This
                will not apply to Users who are also ISE
                Admins, property of the request body.
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
                'changePassword':
                    change_password,
                'email':
                    email,
                'accountNameAlias':
                    account_name_alias,
                'enablePassword':
                    enable_password,
                'enabled':
                    enabled,
                'passwordNeverExpires':
                    password_never_expires,
                'daysForPasswordExpiration':
                    days_for_password_expiration,
                'customAttributes':
                    custom_attributes,
                'firstName':
                    first_name,
                'identityGroups':
                    identity_groups,
                'lastName':
                    last_name,
                'password':
                    password,
                'passwordIDStore':
                    password_idstore,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'dateModified':
                    date_modified,
                'dateCreated':
                    date_created,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f7227b280b745b94bb801369b168a529_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/internaluser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f7227b280b745b94bb801369b168a529_v3_5_0', _api_response)

    def delete_internaluser_by_id(self,
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

        e_url = ('/ers/config/internaluser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dcf28db5184e51139b15f9ffccd10b67_v3_5_0', _api_response)

    def patch_internaluser_by_id(self,
                                 id,
                                 account_name_alias=None,
                                 change_password=None,
                                 custom_attributes=None,
                                 date_created=None,
                                 date_modified=None,
                                 days_for_password_expiration=None,
                                 description=None,
                                 email=None,
                                 enable_password=None,
                                 enabled=None,
                                 expiry_date=None,
                                 expiry_date_enabled=None,
                                 first_name=None,
                                 identity_groups=None,
                                 last_name=None,
                                 name=None,
                                 password=None,
                                 password_idstore=None,
                                 password_never_expires=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            account_name_alias(string): The Account Name Alias will
                be used to send email notifications
                about password expiration, property of
                the request body.
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(string): Key value map, property of
                the request body.
            date_created(string): The date of the user creation,
                formatted as 'YYYY-MM-DD'. Read-only.,
                property of the request body.
            date_modified(string): The date of the last user
                modification by admin, formatted as
                'YYYY-MM-DD'. Read-only., property of
                the request body.
            days_for_password_expiration(number): This field is for
                read only, property of the request body.
            description(string): Description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): EnablePassword field is added
                in ISE 2.0 to support T+, property of
                the request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): to store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD' , property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            id(string): Id, property of the request body.
            identity_groups(string): CSV of identity group IDs.,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): the id store where the
                internal user's password is kept,
                property of the request body.
            password_never_expires(boolean): Set TRUE to indicate
                the user password never expires. This
                will not apply to Users who are also ISE
                Admins, property of the request body.
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
                'changePassword':
                    change_password,
                'email':
                    email,
                'accountNameAlias':
                    account_name_alias,
                'enablePassword':
                    enable_password,
                'enabled':
                    enabled,
                'passwordNeverExpires':
                    password_never_expires,
                'daysForPasswordExpiration':
                    days_for_password_expiration,
                'customAttributes':
                    custom_attributes,
                'firstName':
                    first_name,
                'identityGroups':
                    identity_groups,
                'lastName':
                    last_name,
                'password':
                    password,
                'passwordIDStore':
                    password_idstore,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'dateModified':
                    date_modified,
                'dateCreated':
                    date_created,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cd1bba62cec58edb1b2511ec2b15f00_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/internaluser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_cd1bba62cec58edb1b2511ec2b15f00_v3_5_0', _api_response)
