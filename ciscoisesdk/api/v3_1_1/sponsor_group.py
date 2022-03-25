# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SponsorGroup API wrapper.

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


class SponsorGroup(object):
    """Identity Services Engine SponsorGroup API (version: 3.1.1).

    Wraps the Identity Services Engine SponsorGroup
    API and exposes the API as native Python
    methods that return native Python objects.

    | Sponsor Group API allows the client to add, delete, update and search sponsor groups.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | 0              | 1.0                  | 2.2                   | Initial Cisco ISE Version |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+

    |

    **Resource Definition**

    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Attribute**                   | **Type**  | **Required** | **Description**                     | **Default Values** | **Example Values**                                                                                                                                              |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | name                            | String    | Yes          | Resource Name                       |                    | EmplALL_ACCOUNTS (default)oyees                                                                                                                                 |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | id                              | String    | No           | Resource UUID, mandatory for update |                    | 9f1eca71-8c01-11e6-996c-525400b48521                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | description                     | String    | No           |                                     |                    | Sponsors assigned to this group can manage all guest user accounts. By default, users in the ALL_ACCOUNTS user identity group are members of this sponsor group |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | isEnabled                       | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | isDefaultGroup                  | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | memberGroups                    | List      | No           |                                     |                    | ["ALL_ACCOUNTS (default)"]                                                                                                                                      |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | guestTypes                      | List      | No           |                                     |                    | ["Contractor (default)", "Daily (default)", "Weekly (default)" ]                                                                                                |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | locations                       | List      | No           |                                     |                    | ["San Jose"]                                                                                                                                                    |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | autoNotification                | Boolean   | No           |                                     |                    | false                                                                                                                                                           |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | managePermission                | Enum      | No           | Allowed values:                     |                    | ALLACCOUNTS, GROUPACCOUNTS, OWNACCOUNTS                                                                                                                         |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | createPermissions               | List      | No           |                                     |                    |                                                                                                                                                                 |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canImportMultipleAccounts     | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - importBatchSizeLimit          | Integer   | No           |                                     | 200                |                                                                                                                                                                 |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canCreateRandomAccounts       | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - randomBatchSizeLimit          | Integer   | No           |                                     | 200                |                                                                                                                                                                 |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - defaultUsernamePrefix         | String    | No           |                                     |                    |                                                                                                                                                                 |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canSpecifyUsernamePrefix      | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canSetFutureStartDate         | Boolean   | No           |                                     |                    | false                                                                                                                                                           |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - startDateFutureLimitDays      | Integer   | No           |                                     |                    | 1                                                                                                                                                               |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | otherPermissions                | List      | No           |                                     |                    |                                                                                                                                                                 |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canUpdateGuestContactInfo     | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canViewGuestPasswords         | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canSendSmsNotifications       | Boolean   | No           |                                     |                    | false                                                                                                                                                           |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canResetGuestPasswords        | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canExtendGuestAccounts        | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canDeleteGuestAccounts        | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canSuspendGuestAccounts       | Boolean   | Yes          |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - requireSuspensionReason       | Boolean   | No           |                                     |                    | false                                                                                                                                                           |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canReinstateSuspendedAccounts | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canApproveSelfregGuests       | Boolean   | No           |                                     |                    | true                                                                                                                                                            |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - limitApprovalToSponsorsGuests | Boolean   | Yes          |                                     |                    | false                                                                                                                                                           |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | - canAccessViaRest              | Boolean   | No           |                                     |                    | false                                                                                                                                                           |
    +---------------------------------+-----------+--------------+-------------------------------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SponsorGroup
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SponsorGroup, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_sponsor_group_by_id(self,
                                id,
                                headers=None,
                                **query_parameters):
        """This API allows the client to get a sponsor group by ID.

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

        e_url = ('/ers/config/sponsorgroup/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eaa0d7c339d152b688876c2e10f51fe7_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_sponsor_group_by_id <#ciscoisesdk.
        api.v3_1_1.sponsor_group.
        SponsorGroup.get_sponsor_group_by_id>`_
        """
        return self.get_sponsor_group_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_sponsor_group_by_id(self,
                                   id,
                                   auto_notification=None,
                                   create_permissions=None,
                                   description=None,
                                   guest_types=None,
                                   is_default_group=None,
                                   is_enabled=None,
                                   locations=None,
                                   manage_permission=None,
                                   member_groups=None,
                                   name=None,
                                   other_permissions=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """This API allows the client to update a sponsor group by ID.

        Args:
            auto_notification(boolean): autoNotification, property
                of the request body.
            create_permissions(object): createPermissions, property
                of the request body.
            description(string): description, property of the
                request body.
            guest_types(list): guestTypes, property of the request
                body (list of strings).
            id(string): id, property of the request body.
            is_default_group(boolean): isDefaultGroup, property of
                the request body.
            is_enabled(boolean): isEnabled, property of the request
                body.
            locations(list): locations, property of the request body
                (list of strings).
            manage_permission(string): managePermission, property of
                the request body.
            member_groups(list): memberGroups, property of the
                request body (list of strings).
            name(string): name, property of the request body.
            other_permissions(object): otherPermissions, property of
                the request body.
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
                'isEnabled':
                    is_enabled,
                'isDefaultGroup':
                    is_default_group,
                'memberGroups':
                    member_groups,
                'guestTypes':
                    guest_types,
                'locations':
                    locations,
                'autoNotification':
                    auto_notification,
                'createPermissions':
                    create_permissions,
                'managePermission':
                    manage_permission,
                'otherPermissions':
                    other_permissions,
            }
            _payload = {
                'SponsorGroup': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dfc44f7f24d153d789efa48e904b3832_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sponsorgroup/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_dfc44f7f24d153d789efa48e904b3832_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     auto_notification=None,
                     create_permissions=None,
                     description=None,
                     guest_types=None,
                     is_default_group=None,
                     is_enabled=None,
                     locations=None,
                     manage_permission=None,
                     member_groups=None,
                     name=None,
                     other_permissions=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_sponsor_group_by_id <#ciscoisesdk.
        api.v3_1_1.sponsor_group.
        SponsorGroup.update_sponsor_group_by_id>`_
        """
        return self.update_sponsor_group_by_id(
            id=id,
            auto_notification=auto_notification,
            create_permissions=create_permissions,
            description=description,
            guest_types=guest_types,
            is_default_group=is_default_group,
            is_enabled=is_enabled,
            locations=locations,
            manage_permission=manage_permission,
            member_groups=member_groups,
            name=name,
            other_permissions=other_permissions,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_sponsor_group_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """This API deletes a sponsor group by ID.

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

        e_url = ('/ers/config/sponsorgroup/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c28a45acf05fec98879d8d2ac51129_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_sponsor_group_by_id <#ciscoisesdk.
        api.v3_1_1.sponsor_group.
        SponsorGroup.delete_sponsor_group_by_id>`_
        """
        return self.delete_sponsor_group_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_sponsor_group(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sortasc=None,
                          sortdsc=None,
                          headers=None,
                          **query_parameters):
        """This API allows the client to get all the sponsor groups.
        Filter:   [name]   To search resources by using  toDate
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

        e_url = ('/ers/config/sponsorgroup')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f1196f1f6fde5978b0522f096926d443_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_sponsor_group <#ciscoisesdk.
        api.v3_1_1.sponsor_group.
        SponsorGroup.get_sponsor_group>`_
        """
        return self.get_sponsor_group(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_sponsor_group_generator(self,
                                    filter=None,
                                    filter_type=None,
                                    page=None,
                                    size=None,
                                    sortasc=None,
                                    sortdsc=None,
                                    headers=None,
                                    **query_parameters):
        """This API allows the client to get all the sponsor groups.
        Filter:   [name]   To search resources by using  toDate
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
            self.get_sponsor_group, dict(
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
        """Alias for `get_sponsor_group_generator <#ciscoisesdk.
        api.v3_1_1.sponsor_group.
        SponsorGroup.get_sponsor_group_generator>`_
        """
        yield from get_next_page(
            self.get_sponsor_group, dict(
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

    def create_sponsor_group(self,
                             auto_notification=None,
                             create_permissions=None,
                             description=None,
                             guest_types=None,
                             is_default_group=None,
                             is_enabled=None,
                             locations=None,
                             manage_permission=None,
                             member_groups=None,
                             name=None,
                             other_permissions=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """This API creates a sponsor group.

        Args:
            auto_notification(boolean): autoNotification, property
                of the request body.
            create_permissions(object): createPermissions, property
                of the request body.
            description(string): description, property of the
                request body.
            guest_types(list): guestTypes, property of the request
                body (list of strings).
            is_default_group(boolean): isDefaultGroup, property of
                the request body.
            is_enabled(boolean): isEnabled, property of the request
                body.
            locations(list): locations, property of the request body
                (list of strings).
            manage_permission(string): managePermission, property of
                the request body.
            member_groups(list): memberGroups, property of the
                request body (list of strings).
            name(string): name, property of the request body.
            other_permissions(object): otherPermissions, property of
                the request body.
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
                'isEnabled':
                    is_enabled,
                'isDefaultGroup':
                    is_default_group,
                'memberGroups':
                    member_groups,
                'guestTypes':
                    guest_types,
                'locations':
                    locations,
                'autoNotification':
                    auto_notification,
                'createPermissions':
                    create_permissions,
                'managePermission':
                    manage_permission,
                'otherPermissions':
                    other_permissions,
            }
            _payload = {
                'SponsorGroup': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_acd30d35ee2ae16ff23757de7d8_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sponsorgroup')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_acd30d35ee2ae16ff23757de7d8_v3_1_1', _api_response)

    def create(self,
               auto_notification=None,
               create_permissions=None,
               description=None,
               guest_types=None,
               is_default_group=None,
               is_enabled=None,
               locations=None,
               manage_permission=None,
               member_groups=None,
               name=None,
               other_permissions=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_sponsor_group <#ciscoisesdk.
        api.v3_1_1.sponsor_group.
        SponsorGroup.create_sponsor_group>`_
        """
        return self.create_sponsor_group(
            auto_notification=auto_notification,
            create_permissions=create_permissions,
            description=description,
            guest_types=guest_types,
            is_default_group=is_default_group,
            is_enabled=is_enabled,
            locations=locations,
            manage_permission=manage_permission,
            member_groups=member_groups,
            name=name,
            other_permissions=other_permissions,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the sponsor group.

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

        e_url = ('/ers/config/sponsorgroup/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e8d4001b740751e08cfc19e1fdc5fddf_v3_1_1', _api_response)
