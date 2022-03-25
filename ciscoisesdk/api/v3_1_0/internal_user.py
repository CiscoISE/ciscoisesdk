# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine InternalUser API wrapper.

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


class InternalUser(object):
    """Identity Services Engine InternalUser API (version: 3.1.0).

    Wraps the Identity Services Engine InternalUser
    API and exposes the API as native Python
    methods that return native Python objects.

    | Internal User API allows the client to add, delete, update and search internal users.

    **Revision History**

    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    | Revision # | Resource   Version | Cisco ISE Version | Description                              | Revision Modification | Revision Modification                |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    |            |                    |                   |                                          | Attribute             | Description                          |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    | 0          | 1.0                | 2.3               | Initial Cisco ISE Version                |                       |                                      |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+
    | 1          | 1.1                | 2.6               | Support new attribute Proxy Dead Timeout | proxyTimeout          | Added   int Attribute 'proxyTimeout' |
    +------------+--------------------+-------------------+------------------------------------------+-----------------------+--------------------------------------+

    |

    **Resource Definition**

    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | **Attribute**     | **Type** | **Required** | **Description**                                                                                                                                                                                 | **Default Values** | **Example Values**                   |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | name              | String   | Yes          | Resource Name                                                                                                                                                                                   |                    | name                                 |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | id                | String   | No           | Resource UUID, mandatory for update                                                                                                                                                             |                    | b24b09e2-16f8-4e48-ace1-2c262a9449f1 |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | description       | String   | No           |                                                                                                                                                                                                 |                    | description                          |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | changePassword    | Boolean  | Yes          |                                                                                                                                                                                                 | true               |                                      |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | email             | String   | No           |                                                                                                                                                                                                 |                    | email@domain.com                     |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | enablePassword    | String   | No           | EnablePassword field is added in ISE 2.0 to support T+                                                                                                                                          |                    | enablePassword                       |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | enabled           | Boolean  | Yes          | Whether the user is enabled/disabled. To use it as filter, the values should be 'Enabled' or 'Disabled'. The values are case sensitive. For example, '[ERSObjectURL]?filter=enabled.EQ.Enabled' |                    | true                                 |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | customAttributes  | String   | No           | Key value map                                                                                                                                                                                   |                    | {"key1" : "value1"}                  |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | firstName         | String   | No           |                                                                                                                                                                                                 |                    | firstName                            |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | identityGroups    | String   | No           | CSV of identity group IDs                                                                                                                                                                       |                    | identityGroups                       |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | lastName          | String   | No           |                                                                                                                                                                                                 |                    | lastName                             |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | password          | String   | No           |                                                                                                                                                                                                 |                    | password                             |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | passwordIDStore   | String   | Yes          | The id store where the internal user's password is kept                                                                                                                                         | Internal Users     |                                      |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | expiryDateEnabled | Boolean  | No           |                                                                                                                                                                                                 | false              |                                      |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | expiryDate        | String   | No           | To store the internal user's expiry date information. It's format is = 'YYYY-MM-DD'                                                                                                             |                    | 2021-05-19                           |
    +-------------------+----------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new InternalUser
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(InternalUser, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_internal_user_by_name(self,
                                  name,
                                  headers=None,
                                  **query_parameters):
        """This API allows the client to get an internal user by name.

        Args:
            name(basestring): name path parameter.
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
        check_type(name, basestring,
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

        return self._object_factory('bpm_f403dda9440503191536993f569cc6f_v3_1_0', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_internal_user_by_name <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.get_internal_user_by_name>`_
        """
        return self.get_internal_user_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def update_internal_user_by_name(self,
                                     name,
                                     change_password=None,
                                     custom_attributes=None,
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
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """This API allows the client to update an internal user by name.

        Args:
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(object): Key value map, property of
                the request body.
            description(string): description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): enablePassword, property of the
                request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): To store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD', property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            id(string): id, property of the request body.
            identity_groups(string): CSV of identity group IDs,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): The id store where the
                internal user's password is kept,
                property of the request body.
            name(basestring): name path parameter.
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
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(name, basestring,
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
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'enabled':
                    enabled,
                'email':
                    email,
                'password':
                    password,
                'firstName':
                    first_name,
                'lastName':
                    last_name,
                'changePassword':
                    change_password,
                'identityGroups':
                    identity_groups,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'enablePassword':
                    enable_password,
                'customAttributes':
                    custom_attributes,
                'passwordIDStore':
                    password_idstore,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_19d9509db339e3b27dc56b37_v3_1_0')\
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

        return self._object_factory('bpm_19d9509db339e3b27dc56b37_v3_1_0', _api_response)

    def update_by_name(self,
                       name,
                       change_password=None,
                       custom_attributes=None,
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
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **query_parameters):
        """Alias for `update_internal_user_by_name <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.update_internal_user_by_name>`_
        """
        return self.update_internal_user_by_name(
            name=name,
            change_password=change_password,
            custom_attributes=custom_attributes,
            description=description,
            email=email,
            enable_password=enable_password,
            enabled=enabled,
            expiry_date=expiry_date,
            expiry_date_enabled=expiry_date_enabled,
            first_name=first_name,
            id=id,
            identity_groups=identity_groups,
            last_name=last_name,
            password=password,
            password_idstore=password_idstore,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_internal_user_by_name(self,
                                     name,
                                     headers=None,
                                     **query_parameters):
        """This API deletes an internal user by name.

        Args:
            name(basestring): name path parameter.
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
        check_type(name, basestring,
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

        return self._object_factory('bpm_b4e2fc3e595aa1be86d6589614b9_v3_1_0', _api_response)

    def delete_by_name(self,
                       name,
                       headers=None,
                       **query_parameters):
        """Alias for `delete_internal_user_by_name <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.delete_internal_user_by_name>`_
        """
        return self.delete_internal_user_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_internal_user_by_id(self,
                                id,
                                headers=None,
                                **query_parameters):
        """This API allows the client to get an internal user by ID.

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

        e_url = ('/ers/config/internaluser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bacf1abfc35e509183c9a7f055cbbfec_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_internal_user_by_id <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.get_internal_user_by_id>`_
        """
        return self.get_internal_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_internal_user_by_id(self,
                                   id,
                                   change_password=None,
                                   custom_attributes=None,
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
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """This API allows the client to update an internal user by ID.

        Args:
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(object): Key value map, property of
                the request body.
            description(string): description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): enablePassword, property of the
                request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): To store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD', property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            id(string): id, property of the request body.
            identity_groups(string): CSV of identity group IDs,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): The id store where the
                internal user's password is kept,
                property of the request body.
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
            _tmp_payload = {
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'enabled':
                    enabled,
                'email':
                    email,
                'password':
                    password,
                'firstName':
                    first_name,
                'lastName':
                    last_name,
                'changePassword':
                    change_password,
                'identityGroups':
                    identity_groups,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'enablePassword':
                    enable_password,
                'customAttributes':
                    custom_attributes,
                'passwordIDStore':
                    password_idstore,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f7227b280b745b94bb801369b168a529_v3_1_0')\
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

        return self._object_factory('bpm_f7227b280b745b94bb801369b168a529_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     change_password=None,
                     custom_attributes=None,
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
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_internal_user_by_id <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.update_internal_user_by_id>`_
        """
        return self.update_internal_user_by_id(
            id=id,
            change_password=change_password,
            custom_attributes=custom_attributes,
            description=description,
            email=email,
            enable_password=enable_password,
            enabled=enabled,
            expiry_date=expiry_date,
            expiry_date_enabled=expiry_date_enabled,
            first_name=first_name,
            identity_groups=identity_groups,
            last_name=last_name,
            name=name,
            password=password,
            password_idstore=password_idstore,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_internal_user_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """This API deletes an internal user by ID.

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

        e_url = ('/ers/config/internaluser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dcf28db5184e51139b15f9ffccd10b67_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_internal_user_by_id <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.delete_internal_user_by_id>`_
        """
        return self.delete_internal_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_internal_user(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sortasc=None,
                          sortdsc=None,
                          headers=None,
                          **query_parameters):
        """This API allows the client to get all the internal users.
        Filter:   [firstName, lastName, identityGroup, name,
        description, email, enabled]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
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

        e_url = ('/ers/config/internaluser')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ccba98a61555ae495f6a05284e3b5ae_v3_1_0', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_internal_user <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.get_internal_user>`_
        """
        return self.get_internal_user(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_internal_user_generator(self,
                                    filter=None,
                                    filter_type=None,
                                    page=None,
                                    size=None,
                                    sortasc=None,
                                    sortdsc=None,
                                    headers=None,
                                    **query_parameters):
        """This API allows the client to get all the internal users.
        Filter:   [firstName, lastName, identityGroup, name,
        description, email, enabled]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
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
            self.get_internal_user, dict(
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
        """Alias for `get_internal_user_generator <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.get_internal_user_generator>`_
        """
        yield from get_next_page(
            self.get_internal_user, dict(
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

    def create_internal_user(self,
                             change_password=None,
                             custom_attributes=None,
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
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """This API creates an internal user.

        Args:
            change_password(boolean): changePassword, property of
                the request body.
            custom_attributes(object): Key value map, property of
                the request body.
            description(string): description, property of the
                request body.
            email(string): email, property of the request body.
            enable_password(string): enablePassword, property of the
                request body.
            enabled(boolean): Whether the user is enabled/disabled.
                To use it as filter, the values should
                be 'Enabled' or 'Disabled'. The values
                are case sensitive. For example, '[ERSOb
                jectURL]?filter=enabled.EQ.Enabled',
                property of the request body.
            expiry_date(string): To store the internal user's expiry
                date information. It's format is =
                'YYYY-MM-DD', property of the request
                body.
            expiry_date_enabled(boolean): expiryDateEnabled,
                property of the request body.
            first_name(string): firstName, property of the request
                body.
            identity_groups(string): CSV of identity group IDs,
                property of the request body.
            last_name(string): lastName, property of the request
                body.
            name(string): name, property of the request body.
            password(string): password, property of the request
                body.
            password_idstore(string): The id store where the
                internal user's password is kept,
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
            _tmp_payload = {
                'name':
                    name,
                'description':
                    description,
                'enabled':
                    enabled,
                'email':
                    email,
                'password':
                    password,
                'firstName':
                    first_name,
                'lastName':
                    last_name,
                'changePassword':
                    change_password,
                'identityGroups':
                    identity_groups,
                'expiryDateEnabled':
                    expiry_date_enabled,
                'expiryDate':
                    expiry_date,
                'enablePassword':
                    enable_password,
                'customAttributes':
                    custom_attributes,
                'passwordIDStore':
                    password_idstore,
            }
            _payload = {
                'InternalUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_bf175c04fcb051b9a6fd70a2252903fa_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/internaluser')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_bf175c04fcb051b9a6fd70a2252903fa_v3_1_0', _api_response)

    def create(self,
               change_password=None,
               custom_attributes=None,
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
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_internal_user <#ciscoisesdk.
        api.v3_1_0.internal_user.
        InternalUser.create_internal_user>`_
        """
        return self.create_internal_user(
            change_password=change_password,
            custom_attributes=custom_attributes,
            description=description,
            email=email,
            enable_password=enable_password,
            enabled=enabled,
            expiry_date=expiry_date,
            expiry_date_enabled=expiry_date_enabled,
            first_name=first_name,
            identity_groups=identity_groups,
            last_name=last_name,
            name=name,
            password=password,
            password_idstore=password_idstore,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the internal user.

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

        e_url = ('/ers/config/internaluser/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af99828533e58a2b84996b85bacc9ff_v3_1_0', _api_response)
