# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine GuestType API wrapper.

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


class GuestType(object):
    """Identity Services Engine GuestType API (version: 3.1.0).

    Wraps the Identity Services Engine GuestType
    API and exposes the API as native Python
    methods that return native Python objects.

    | Guest Type API allows the client to add, delete, update and search guest types.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.2                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | **Attribute**                    | **Type**  | **Required** | **Description**                                                               | **Default Values**           | **Example Values**                                                               |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | name                             | String    | Yes          | Resource Name                                                                 |                              | Contractor (default)                                                             |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | id                               | String    | No           | Resource UUID, mandatory for update                                           |                              | 9f03a151-8c01-11e6-996c-525400b48521                                             |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | description                      | String    | No           |                                                                               |                              | Default settings allow network access for up to a year.                          |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | accessTime                       | List      | No           |                                                                               |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - allowAccessOnSpecificDaysTimes | Boolean   | No           | Enable Specific Day Time Limits                                               | false                        |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - defaultDuration                | Integer   | No           |                                                                               | 90                           |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - durationTimeUnit               | Enum      | No           | Allowed values are:                                                           | DAYS                         |                                                                                  |
    |                                  |           |              | - DAYS,                                                                       |                              |                                                                                  |
    |                                  |           |              | - HOURS,                                                                      |                              |                                                                                  |
    |                                  |           |              | - MINUTES                                                                     |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - fromFirstLogin                 | Boolean   | No           | When Account Duration starts from first login or specified date               | false                        |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - maxAccountDuration             | Integer   | No           | Maximum value of Account Duration                                             | 365                          |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - dayTimeLimits                  | List      | No           | List of Time Ranges for account access                                        |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    |   - dayTimeLimit                 | List      | No           | Time Ranges for account access                                                |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    |     - startTime                  | String    | No           | Start time in HH:mm format                                                    | 09:00                        |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    |     - endTime                    | String    | No           | End time in HH:mm format                                                      | 17:00                        |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    |     - days                       | List      | No           | List of Days                                                                  |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    |       - day                      | Enum      | No           | Value should be one of Week day. Allowed values are:                          |                              |                                                                                  |
    |                                  |           |              | - Sunday,                                                                     |                              |                                                                                  |
    |                                  |           |              | - Monday,                                                                     |                              |                                                                                  |
    |                                  |           |              | - Tuesday,                                                                    |                              |                                                                                  |
    |                                  |           |              | - Wednesday,                                                                  |                              |                                                                                  |
    |                                  |           |              | - Thursday,                                                                   |                              |                                                                                  |
    |                                  |           |              | - Friday,                                                                     |                              |                                                                                  |
    |                                  |           |              | - Saturday                                                                    |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | loginOptions                     | List      | No           | Login options                                                                 |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - allowGuestPortalBypass         | Boolean   | No           |                                                                               | false                        |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - failureAction                  | Enum      | No           | When Guest Exceeds limit this action will be invoked, Allowed values are:     | Disconnect_Oldest_Connection |                                                                                  |
    |                                  |           |              | - Disconnect_Oldest_Connection,                                               |                              |                                                                                  |
    |                                  |           |              | - Disconnect_Newest_Connection                                                |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - identityGroupId                | String    | Yes          | ID of Guest Identity Group                                                    |                              | aa178bd0-8bff-11e6-996c-525400b48521                                             |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - limitSimultaneousLogins        | Boolean   | No           | Enable Simultaneous Logins                                                    | true                         |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - maxRegisteredDevices           | Integer   | No           | Maximum devices guests can register                                           | 5                            |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - maxSimultaneousLogins          | Integer   | No           | Number of Simultaneous Logins                                                 | 3                            |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | expirationNotification           | List      | No           | Expiration Notification Settings                                              |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - advanceNotificationDuration    | Integer   | No           | Send Account Expiration Notification Duration before ( Days, Hours, Minutes ) | 3                            |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - advanceNotificationUnits       | Enum      | No           | Allowed values are:                                                           | DAYS                         |                                                                                  |
    |                                  |           |              | - DAYS,                                                                       |                              |                                                                                  |
    |                                  |           |              | - HOURS,                                                                      |                              |                                                                                  |
    |                                  |           |              | - MINUTES                                                                     |                              |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - enableNotification             | Boolean   | No           | Enable Notification settings                                                  | false                        |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - sendEmailNotification          | Boolean   | No           | Enable Email Notification                                                     | false                        |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | - sendSmsNotification            | Integer   | No           | Maximum devices guests can register                                           | 5                            |                                                                                  |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+
    | sponsorGroups                    | List      | Yes          | List of Sponsor Groups                                                        |                              | ["GROUP_ACCOUNTS (default)", "ALL_ACCOUNTS (default)", "OWN_ACCOUNTS (default)"] |
    +----------------------------------+-----------+--------------+-------------------------------------------------------------------------------+------------------------------+----------------------------------------------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new GuestType
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(GuestType, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def update_guest_type_email(self,
                                id,
                                additional_data=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """This API allows the client to update a guest type email by ID.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
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
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cf310e621a395bb7bac7b90d7d4c8603_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/guesttype/email/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_cf310e621a395bb7bac7b90d7d4c8603_v3_1_0', _api_response)

    def update_email(self,
                     id,
                     additional_data=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_guest_type_email <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.update_guest_type_email>`_
        """
        return self.update_guest_type_email(
            id=id,
            additional_data=additional_data,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def update_guest_type_sms(self,
                              id,
                              additional_data=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """This API allows the client to update a guest type sms by ID.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
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
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eb42e79d5cc38bd1a6eef20613d6_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/guesttype/sms/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_eb42e79d5cc38bd1a6eef20613d6_v3_1_0', _api_response)

    def update_sms(self,
                   id,
                   additional_data=None,
                   headers=None,
                   payload=None,
                   active_validation=True,
                   **query_parameters):
        """Alias for `update_guest_type_sms <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.update_guest_type_sms>`_
        """
        return self.update_guest_type_sms(
            id=id,
            additional_data=additional_data,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_guest_type_by_id(self,
                             id,
                             headers=None,
                             **query_parameters):
        """This API allows the client to get a guest type by ID.

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

        e_url = ('/ers/config/guesttype/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_acb5a41fe395b158a3fe1cda996b0cf_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_guest_type_by_id <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.get_guest_type_by_id>`_
        """
        return self.get_guest_type_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_guest_type_by_id(self,
                                id,
                                access_time=None,
                                description=None,
                                expiration_notification=None,
                                is_default_type=None,
                                login_options=None,
                                name=None,
                                sponsor_groups=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """This API allows the client to update a guest type.

        Args:
            access_time(object): accessTime, property of the request
                body.
            description(string): description, property of the
                request body.
            expiration_notification(object): Expiration Notification
                Settings, property of the request body.
            id(string): id, property of the request body.
            is_default_type(boolean): isDefaultType, property of the
                request body.
            login_options(object): loginOptions, property of the
                request body.
            name(string): name, property of the request body.
            sponsor_groups(list): sponsorGroups, property of the
                request body (list of strings).
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
                'isDefaultType':
                    is_default_type,
                'accessTime':
                    access_time,
                'loginOptions':
                    login_options,
                'expirationNotification':
                    expiration_notification,
                'sponsorGroups':
                    sponsor_groups,
            }
            _payload = {
                'GuestType': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_bac6d4d95ac45a0a8933b8712dcbe70d_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/guesttype/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_bac6d4d95ac45a0a8933b8712dcbe70d_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     access_time=None,
                     description=None,
                     expiration_notification=None,
                     is_default_type=None,
                     login_options=None,
                     name=None,
                     sponsor_groups=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_guest_type_by_id <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.update_guest_type_by_id>`_
        """
        return self.update_guest_type_by_id(
            id=id,
            access_time=access_time,
            description=description,
            expiration_notification=expiration_notification,
            is_default_type=is_default_type,
            login_options=login_options,
            name=name,
            sponsor_groups=sponsor_groups,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_guest_type_by_id(self,
                                id,
                                headers=None,
                                **query_parameters):
        """This API deletes a guest type.

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

        e_url = ('/ers/config/guesttype/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_faa7211d68e5b329034e17c82b78694_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_guest_type_by_id <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.delete_guest_type_by_id>`_
        """
        return self.delete_guest_type_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_guest_type(self,
                       filter=None,
                       filter_type=None,
                       page=None,
                       size=None,
                       sortasc=None,
                       sortdsc=None,
                       headers=None,
                       **query_parameters):
        """This API allows the client to get all the guest types.   Filter:
        [name]   To search resources by using  toDate
        column,follow the format:   DD-MON-YY
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

        e_url = ('/ers/config/guesttype')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f41a1e47105581fabf212f259626903_v3_1_0', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_guest_type <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.get_guest_type>`_
        """
        return self.get_guest_type(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_guest_type_generator(self,
                                 filter=None,
                                 filter_type=None,
                                 page=None,
                                 size=None,
                                 sortasc=None,
                                 sortdsc=None,
                                 headers=None,
                                 **query_parameters):
        """This API allows the client to get all the guest types.   Filter:
        [name]   To search resources by using  toDate
        column,follow the format:   DD-MON-YY
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
            self.get_guest_type, dict(
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
        """Alias for `get_guest_type_generator <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.get_guest_type_generator>`_
        """
        yield from get_next_page(
            self.get_guest_type, dict(
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

    def create_guest_type(self,
                          access_time=None,
                          description=None,
                          expiration_notification=None,
                          is_default_type=None,
                          login_options=None,
                          name=None,
                          sponsor_groups=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """This API creates a guest type.

        Args:
            access_time(object): accessTime, property of the request
                body.
            description(string): description, property of the
                request body.
            expiration_notification(object): Expiration Notification
                Settings, property of the request body.
            is_default_type(boolean): isDefaultType, property of the
                request body.
            login_options(object): loginOptions, property of the
                request body.
            name(string): name, property of the request body.
            sponsor_groups(list): sponsorGroups, property of the
                request body (list of strings).
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
                'isDefaultType':
                    is_default_type,
                'accessTime':
                    access_time,
                'loginOptions':
                    login_options,
                'expirationNotification':
                    expiration_notification,
                'sponsorGroups':
                    sponsor_groups,
            }
            _payload = {
                'GuestType': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f46c01449d585b088490c4db530c56d5_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/guesttype')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f46c01449d585b088490c4db530c56d5_v3_1_0', _api_response)

    def create(self,
               access_time=None,
               description=None,
               expiration_notification=None,
               is_default_type=None,
               login_options=None,
               name=None,
               sponsor_groups=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_guest_type <#ciscoisesdk.
        api.v3_1_0.guest_type.
        GuestType.create_guest_type>`_
        """
        return self.create_guest_type(
            access_time=access_time,
            description=description,
            expiration_notification=expiration_notification,
            is_default_type=is_default_type,
            login_options=login_options,
            name=name,
            sponsor_groups=sponsor_groups,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the guest type.

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

        e_url = ('/ers/config/guesttype/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6bfaedfca185fb7b6a86621e866a5f6_v3_1_0', _api_response)
