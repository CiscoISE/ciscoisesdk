# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine GuestUser API wrapper.

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


class GuestUser(object):
    """Identity Services Engine GuestUser API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine GuestUser
    API and exposes the API as native Python
    methods that return native Python objects.

    | Guest User API allows the client to add, delete, update and search guest users among other operations which are available from the sponsor portal. Please note that each API description shows whether the API is supported in bulk operation. The bulk section is showing only 'create' bulk operation. However, all other operation which are bulk supported can be used in the same way.

    **Revision History**

    +----------------+----------------------+-----------------------+-----------------------------------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**                                     |
    +----------------+----------------------+-----------------------+-----------------------------------------------------+
    | 0              | 1.0                  | 1.2                   | Initial Cisco ISE Version                           |
    +----------------+----------------------+-----------------------+-----------------------------------------------------+
    | 1              | 2.0                  | 1.3                   | Introducing new schema - not supporting 1.0 anymore |
    +----------------+----------------------+-----------------------+-----------------------------------------------------+

    |

    **Resource Definition**

    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | **Attribute**          | **Type** | **Required** | **Description**                                                                                                                                     | **Default Values** | **Example Values**                   |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | name                   | String   | Yes          | Resource Name                                                                                                                                       |                    | guestUser                            |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | id                     | String   | No           | Resource UUID, mandatory for update                                                                                                                 |                    | ab6deded-fcc2-47ff-8577-0014737c8fcf |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | description            | String   | No           |                                                                                                                                                     |                    | ERS Example user                     |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | customFields           | Map      | No           | Key value map                                                                                                                                       |                    | "some key" : "some value"            |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | guestType              | String   | No           |                                                                                                                                                     |                    | Contractor                           |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | status                 | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | reasonForVisit         | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | personBeingVisited     | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | sponsorUserName        | String   | No           |                                                                                                                                                     |                    | Mr Spons                             |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | sponsorUserId          | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | statusReason           | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | portalId               | String   | No           |                                                                                                                                                     |                    | 23423432523                          |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | guestAccessInfo        | List     | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - validDays            | Integer  | Yes          | Number of days guest user is valid. To validate validDays property, Cisco ISE considers only date (not time) between fromDate and toDate properites |                    | 90                                   |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - fromDate             | String   | No           |                                                                                                                                                     |                    | 07/29/2014 14:44                     |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - toDate               | String   | No           |                                                                                                                                                     |                    | 10/29/2014 17:30                     |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - location             | String   | No           |                                                                                                                                                     |                    | San Jose                             |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - ssid                 | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - groupTag             | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | GuestInfo              | List     | Yes          |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - emailAddress         | String   | No           |                                                                                                                                                     |                    | email@some.uri.com                   |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - enabled              | Boolean  | Yes          | This field is only for Get operation not applicable for Create, Update operations                                                                   | false              |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - password             | String   | Yes          |                                                                                                                                                     |                    | asdlkj324ew                          |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - phoneNumber          | String   | No           | Phone number should be E.164 format                                                                                                                 |                    | +13211239034                         |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - smsServiceProvider   | String   | No           |                                                                                                                                                     |                    | Global Default                       |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - userName             | String   | No           | If account needs be created with mobile number, please provide mobile number here                                                                   |                    | DS3ewdsa34wWE                        |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - firstName            | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - lastName             | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - company              | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - creationTime         | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | - notificationLanguage | String   | No           |                                                                                                                                                     |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new GuestUser
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(GuestUser, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def approve_guest_user_by_id(self,
                                 id,
                                 headers=None,
                                 **query_parameters):
        """This API allows the client to approve a guest user by ID.

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

        e_url = ('/ers/config/guestuser/approve/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c67b4dcffba052ae8ece775bc61a1c21_v3_1_patch_1', _api_response)

    def approve_by_id(self,
                      id,
                      headers=None,
                      **query_parameters):
        """Alias for `approve_guest_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.approve_guest_user_by_id>`_
        """
        return self.approve_guest_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def change_sponsor_password(self,
                                portal_id,
                                additional_data=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """This API allows the client to change the sponsor password.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            portal_id(basestring): portalId path parameter.
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
        check_type(portal_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'portalId': portal_id,
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
            self._request_validator('jsd_eb3472c4de150828b2dae61e2285313_v3_1_patch_1')\
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

        return self._object_factory('bpm_eb3472c4de150828b2dae61e2285313_v3_1_patch_1', _api_response)

    def suspend_guest_user_by_name(self,
                                   name,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to suspend a guest user by name.

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

        e_url = ('/ers/config/guestuser/suspend/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_afcc8fe53b4824ae744a2ff3848_v3_1_patch_1', _api_response)

    def suspend_by_name(self,
                        name,
                        headers=None,
                        **query_parameters):
        """Alias for `suspend_guest_user_by_name <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.suspend_guest_user_by_name>`_
        """
        return self.suspend_guest_user_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def reinstate_guest_user_by_name(self,
                                     name,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to reinstate a guest user by name.

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

        e_url = ('/ers/config/guestuser/reinstate/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b21045846d5097a82cd61cb3c7eaf1_v3_1_patch_1', _api_response)

    def reinstate_by_name(self,
                          name,
                          headers=None,
                          **query_parameters):
        """Alias for `reinstate_guest_user_by_name <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.reinstate_guest_user_by_name>`_
        """
        return self.reinstate_guest_user_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_guest_user_by_name(self,
                               name,
                               headers=None,
                               **query_parameters):
        """This API allows the client to get a guest user by name.

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

        e_url = ('/ers/config/guestuser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bcb7ec29968e5d5899df4a90d94ed659_v3_1_patch_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_guest_user_by_name <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.get_guest_user_by_name>`_
        """
        return self.get_guest_user_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def update_guest_user_by_name(self,
                                  name,
                                  custom_fields=None,
                                  description=None,
                                  guest_access_info=None,
                                  guest_info=None,
                                  guest_type=None,
                                  id=None,
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
        """This API allows the client to update a guest user by name.

        Args:
            custom_fields(object): Key value map, property of the
                request body.
            description(string): description, property of the
                request body.
            guest_access_info(object): guestAccessInfo, property of
                the request body.
            guest_info(object): guestInfo, property of the request
                body.
            guest_type(string): guestType, property of the request
                body.
            id(string): id, property of the request body.
            name(string): name, property of the request body.
            portal_id(string): portalId, property of the request
                body.
            reason_for_visit(string): reasonForVisit, property of
                the request body.
            sponsor_user_id(string): sponsorUserId, property of the
                request body.
            sponsor_user_name(string): sponsorUserName, property of
                the request body.
            status(string): status, property of the request body.
            status_reason(string): statusReason, property of the
                request body.
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
                'guestType':
                    guest_type,
                'status':
                    status,
                'statusReason':
                    status_reason,
                'reasonForVisit':
                    reason_for_visit,
                'sponsorUserId':
                    sponsor_user_id,
                'sponsorUserName':
                    sponsor_user_name,
                'guestInfo':
                    guest_info,
                'guestAccessInfo':
                    guest_access_info,
                'portalId':
                    portal_id,
                'customFields':
                    custom_fields,
            }
            _payload = {
                'GuestUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f24049df29d059c48eef86d381ffad5d_v3_1_patch_1')\
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

        return self._object_factory('bpm_f24049df29d059c48eef86d381ffad5d_v3_1_patch_1', _api_response)

    def update_by_name(self,
                       name,
                       custom_fields=None,
                       description=None,
                       guest_access_info=None,
                       guest_info=None,
                       guest_type=None,
                       id=None,
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
        """Alias for `update_guest_user_by_name <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.update_guest_user_by_name>`_
        """
        return self.update_guest_user_by_name(
            name=name,
            custom_fields=custom_fields,
            description=description,
            guest_access_info=guest_access_info,
            guest_info=guest_info,
            guest_type=guest_type,
            id=id,
            portal_id=portal_id,
            reason_for_visit=reason_for_visit,
            sponsor_user_id=sponsor_user_id,
            sponsor_user_name=sponsor_user_name,
            status=status,
            status_reason=status_reason,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_guest_user_by_name(self,
                                  name,
                                  headers=None,
                                  **query_parameters):
        """This API deletes a guest user.

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

        e_url = ('/ers/config/guestuser/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ef15d7c6b259f5859ee9675c38887c_v3_1_patch_1', _api_response)

    def delete_by_name(self,
                       name,
                       headers=None,
                       **query_parameters):
        """Alias for `delete_guest_user_by_name <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.delete_guest_user_by_name>`_
        """
        return self.delete_guest_user_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def reset_guest_user_password_by_id(self,
                                        id,
                                        headers=None,
                                        **query_parameters):
        """This API allows the client to reset the guest user password.

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

        e_url = ('/ers/config/guestuser/resetpassword/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea6ea4e41d85f83b6f6c10ce38bb9ed_v3_1_patch_1', _api_response)

    def reset_password_by_id(self,
                             id,
                             headers=None,
                             **query_parameters):
        """Alias for `reset_guest_user_password_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.reset_guest_user_password_by_id>`_
        """
        return self.reset_guest_user_password_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def reinstate_guest_user_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to reinstate a guest user by ID.

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

        e_url = ('/ers/config/guestuser/reinstate/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dfcba4a0f685c168bdf2b5b2be317ac_v3_1_patch_1', _api_response)

    def reinstate_by_id(self,
                        id,
                        headers=None,
                        **query_parameters):
        """Alias for `reinstate_guest_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.reinstate_guest_user_by_id>`_
        """
        return self.reinstate_guest_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_guest_user_email(self,
                                id,
                                portal_id,
                                additional_data=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """This API allows the client to update a guest user email by ID.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            portal_id(basestring): portalId path parameter.
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
        check_type(portal_id, basestring,
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
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a9fa9cbccbe50fcb1cd6a63fed47578_v3_1_patch_1')\
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

        return self._object_factory('bpm_a9fa9cbccbe50fcb1cd6a63fed47578_v3_1_patch_1', _api_response)

    def update_email(self,
                     id,
                     portal_id,
                     additional_data=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_guest_user_email <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.update_guest_user_email>`_
        """
        return self.update_guest_user_email(
            id=id,
            portal_id=portal_id,
            additional_data=additional_data,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def update_guest_user_sms(self,
                              id,
                              portal_id,
                              headers=None,
                              **query_parameters):
        """This API allows the client to update a guest user sms by ID.

        Args:
            id(basestring): id path parameter.
            portal_id(basestring): portalId path parameter.
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
        check_type(portal_id, basestring,
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

        return self._object_factory('bpm_ba14b751f98206ca2e19cff3fe_v3_1_patch_1', _api_response)

    def update_sms(self,
                   id,
                   portal_id,
                   headers=None,
                   **query_parameters):
        """Alias for `update_guest_user_sms <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.update_guest_user_sms>`_
        """
        return self.update_guest_user_sms(
            id=id,
            portal_id=portal_id,
            headers=headers,
            **query_parameters
        )

    def deny_guest_user_by_id(self,
                              id,
                              headers=None,
                              **query_parameters):
        """This API allows the client to deny a guest user by ID.

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

        e_url = ('/ers/config/guestuser/deny/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1e5e2a187652018c59b10155ac973d_v3_1_patch_1', _api_response)

    def deny_by_id(self,
                   id,
                   headers=None,
                   **query_parameters):
        """Alias for `deny_guest_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.deny_guest_user_by_id>`_
        """
        return self.deny_guest_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_guest_user_by_id(self,
                             id,
                             headers=None,
                             **query_parameters):
        """This API allows the client to get a guest user by ID.

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

        e_url = ('/ers/config/guestuser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c3c7d5a3a83d9f7441972d399_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_guest_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.get_guest_user_by_id>`_
        """
        return self.get_guest_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_guest_user_by_id(self,
                                id,
                                custom_fields=None,
                                description=None,
                                guest_access_info=None,
                                guest_info=None,
                                guest_type=None,
                                name=None,
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
        """This API allows the client to update a guest user by ID.

        Args:
            custom_fields(object): Key value map, property of the
                request body.
            description(string): description, property of the
                request body.
            guest_access_info(object): guestAccessInfo, property of
                the request body.
            guest_info(object): guestInfo, property of the request
                body.
            guest_type(string): guestType, property of the request
                body.
            id(string): id, property of the request body.
            name(string): name, property of the request body.
            portal_id(string): portalId, property of the request
                body.
            reason_for_visit(string): reasonForVisit, property of
                the request body.
            sponsor_user_id(string): sponsorUserId, property of the
                request body.
            sponsor_user_name(string): sponsorUserName, property of
                the request body.
            status(string): status, property of the request body.
            status_reason(string): statusReason, property of the
                request body.
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
                'guestType':
                    guest_type,
                'status':
                    status,
                'statusReason':
                    status_reason,
                'reasonForVisit':
                    reason_for_visit,
                'sponsorUserId':
                    sponsor_user_id,
                'sponsorUserName':
                    sponsor_user_name,
                'guestInfo':
                    guest_info,
                'guestAccessInfo':
                    guest_access_info,
                'portalId':
                    portal_id,
                'customFields':
                    custom_fields,
            }
            _payload = {
                'GuestUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b9c7c5847b17684c49399ff95_v3_1_patch_1')\
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

        return self._object_factory('bpm_b9c7c5847b17684c49399ff95_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
                     custom_fields=None,
                     description=None,
                     guest_access_info=None,
                     guest_info=None,
                     guest_type=None,
                     name=None,
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
        """Alias for `update_guest_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.update_guest_user_by_id>`_
        """
        return self.update_guest_user_by_id(
            id=id,
            custom_fields=custom_fields,
            description=description,
            guest_access_info=guest_access_info,
            guest_info=guest_info,
            guest_type=guest_type,
            name=name,
            portal_id=portal_id,
            reason_for_visit=reason_for_visit,
            sponsor_user_id=sponsor_user_id,
            sponsor_user_name=sponsor_user_name,
            status=status,
            status_reason=status_reason,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_guest_user_by_id(self,
                                id,
                                headers=None,
                                **query_parameters):
        """This API deletes a guest user by ID.

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

        e_url = ('/ers/config/guestuser/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e251b39f55d3ac2570a963a3ee9c_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_guest_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.delete_guest_user_by_id>`_
        """
        return self.delete_guest_user_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_guest_users(self,
                        filter=None,
                        filter_type=None,
                        page=None,
                        size=None,
                        sortasc=None,
                        sortdsc=None,
                        headers=None,
                        **query_parameters):
        """This API allows the client to get all the guest users.   Filter:
        [lastName, sponsor, creationTime, personBeingVisited,
        toDate, userName, firstName, emailAddress, phoneNumber,
        groupTag, name, company, guestType, status]   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [firstName, lastName, emailAddress, name,
        description].

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

        e_url = ('/ers/config/guestuser')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a5abd33eeaa52e39e926472751ef79e_v3_1_patch_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_guest_users <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.get_guest_users>`_
        """
        return self.get_guest_users(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_guest_users_generator(self,
                                  filter=None,
                                  filter_type=None,
                                  page=None,
                                  size=None,
                                  sortasc=None,
                                  sortdsc=None,
                                  headers=None,
                                  **query_parameters):
        """This API allows the client to get all the guest users.   Filter:
        [lastName, sponsor, creationTime, personBeingVisited,
        toDate, userName, firstName, emailAddress, phoneNumber,
        groupTag, name, company, guestType, status]   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [firstName, lastName, emailAddress, name,
        description].

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
            self.get_guest_users, dict(
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
        """Alias for `get_guest_users_generator <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.get_guest_users_generator>`_
        """
        yield from get_next_page(
            self.get_guest_users, dict(
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

    def create_guest_user(self,
                          custom_fields=None,
                          description=None,
                          guest_access_info=None,
                          guest_info=None,
                          guest_type=None,
                          name=None,
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
        """This API creates a guest user.

        Args:
            custom_fields(object): Key value map, property of the
                request body.
            description(string): description, property of the
                request body.
            guest_access_info(object): guestAccessInfo, property of
                the request body.
            guest_info(object): guestInfo, property of the request
                body.
            guest_type(string): guestType, property of the request
                body.
            name(string): name, property of the request body.
            portal_id(string): portalId, property of the request
                body.
            reason_for_visit(string): reasonForVisit, property of
                the request body.
            sponsor_user_id(string): sponsorUserId, property of the
                request body.
            sponsor_user_name(string): sponsorUserName, property of
                the request body.
            status(string): status, property of the request body.
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
                'guestType':
                    guest_type,
                'status':
                    status,
                'statusReason':
                    status_reason,
                'reasonForVisit':
                    reason_for_visit,
                'sponsorUserId':
                    sponsor_user_id,
                'sponsorUserName':
                    sponsor_user_name,
                'guestInfo':
                    guest_info,
                'guestAccessInfo':
                    guest_access_info,
                'portalId':
                    portal_id,
                'customFields':
                    custom_fields,
            }
            _payload = {
                'GuestUser': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f7cf06a1655d6da606ace9b0950bcf_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f7cf06a1655d6da606ace9b0950bcf_v3_1_patch_1', _api_response)

    def create(self,
               custom_fields=None,
               description=None,
               guest_access_info=None,
               guest_info=None,
               guest_type=None,
               name=None,
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
        """Alias for `create_guest_user <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.create_guest_user>`_
        """
        return self.create_guest_user(
            custom_fields=custom_fields,
            description=description,
            guest_access_info=guest_access_info,
            guest_info=guest_info,
            guest_type=guest_type,
            name=name,
            portal_id=portal_id,
            reason_for_visit=reason_for_visit,
            sponsor_user_id=sponsor_user_id,
            sponsor_user_name=sponsor_user_name,
            status=status,
            status_reason=status_reason,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def suspend_guest_user_by_id(self,
                                 id,
                                 additional_data=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **query_parameters):
        """This API allows the client to suspend a guest user by ID.

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
            self._request_validator('jsd_be5b1e320e55f4a181370417471d9e_v3_1_patch_1')\
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

        return self._object_factory('bpm_be5b1e320e55f4a181370417471d9e_v3_1_patch_1', _api_response)

    def suspend_by_id(self,
                      id,
                      additional_data=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **query_parameters):
        """Alias for `suspend_guest_user_by_id <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.suspend_guest_user_by_id>`_
        """
        return self.suspend_guest_user_by_id(
            id=id,
            additional_data=additional_data,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the guest user.

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

        e_url = ('/ers/config/guestuser/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_abe22ea0c45f619731bd568c9f57f4_v3_1_patch_1', _api_response)

    def bulk_request_for_guest_user(self,
                                    operation_type=None,
                                    resource_media_type=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """This API allows the client to submit the bulk request.

        Args:
            operation_type(string): operationType, property of the
                request body.
            resource_media_type(string): resourceMediaType, property
                of the request body.
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
                'operationType':
                    operation_type,
                'resourceMediaType':
                    resource_media_type,
            }
            _payload = {
                'GuestUserBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_edfca30e8e514d9bab840c3c2d4c0f_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/guestuser/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_edfca30e8e514d9bab840c3c2d4c0f_v3_1_patch_1', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_guest_user <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.bulk_request_for_guest_user>`_
        """
        return self.bulk_request_for_guest_user(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_guest_user(self,
                                       bulkid,
                                       headers=None,
                                       **query_parameters):
        """This API allows the client to monitor the bulk request.

        Args:
            bulkid(basestring): bulkid path parameter.
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
        check_type(bulkid, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'bulkid': bulkid,
        }

        e_url = ('/ers/config/guestuser/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e38a1af3ad835636a11375363528fa2e_v3_1_patch_1', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_guest_user <#ciscoisesdk.
        api.v3_1_patch_1.guest_user.
        GuestUser.monitor_bulk_status_guest_user>`_
        """
        return self.monitor_bulk_status_guest_user(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )
