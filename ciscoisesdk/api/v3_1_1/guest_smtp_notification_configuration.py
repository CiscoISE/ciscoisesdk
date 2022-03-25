# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine GuestSMTPNotificationConfiguration API wrapper.

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


class GuestSmtpNotificationConfiguration(object):
    """Identity Services Engine GuestSMTPNotificationConfiguration API (version: 3.1.1).

    Wraps the Identity Services Engine GuestSMTPNotificationConfiguration
    API and exposes the API as native Python
    methods that return native Python objects.

    | Guest SMTP notification configuration API is a global setting for enabling email notifications within guest application. These APIs allow to create, update and retrieve the notification settings. The create API may not be required to be used as of Cisco ISE Release 2.2 because the single SMTP notification configuration is the only one used and it always gets created during the Cisco ISE application initialization period.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.2                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | **Attribute**             | **Type** | **Required** | **Description**                                                                           | **Default Values**     | **Example Values**                   |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | name                      | String   | Yes          | Resource Name                                                                             |                        |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | id                        | String   | No           | Resource UUID, mandatory for update                                                       |                        | 9ecb5340-8c01-11e6-996c-525400b48521 |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | description               | String   | No           |                                                                                           |                        |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | defaultFromAddress        | String   | No           | The default from email address to be used to send emails from                             | donotreply@example.com |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | notificationEnabled       | Boolean  | No           | Indicates if the email notification service is to be enabled                              | true                   |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | smtpServer                | String   | No           | The SMTP server ip address or fqdn such as outbound.mycompany.com                         |                        |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | useDefaultFromAddress     | Boolean  | No           | If the default from address should be used rather than using a sponsor user email address | false                  |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | smtpPort                  | String   | No           | Port at which SMTP Secure Server is listening                                             | 25                     |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | connectionTimeout         | String   | No           | Interval in seconds for all the SMTP client connections                                   | 60                     |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | useTLSorSSLEncryption     | Boolean  | No           | If configured to true, SMTP server authentication will happen using TLS/SSL               | false                  |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | usePasswordAuthentication | Boolean  | No           | If configured to true, SMTP server authentication will happen using username/password     | false                  |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | userName                  | String   | No           | Username of Secure SMTP server                                                            |                        |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+
    | password                  | String   | No           | Password of Secure SMTP server                                                            |                        |                                      |
    +---------------------------+----------+--------------+-------------------------------------------------------------------------------------------+------------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new GuestSmtpNotificationConfiguration
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(GuestSmtpNotificationConfiguration, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_guest_smtp_notification_settings_by_id(self,
                                                   id,
                                                   headers=None,
                                                   **query_parameters):
        """This API allows the client to get a guest SMTP notification
        configuration by ID.

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

        e_url = ('/ers/config/guestsmtpnotificationsettings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ca28129793d1569bb50de9f43b0d0ee8_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_guest_smtp_notification_settings_by_id <#ciscoisesdk.
        api.v3_1_1.guest_smtp_notification_configuration.
        GuestSmtpNotificationConfiguration.get_guest_smtp_notification_settings_by_id>`_
        """
        return self.get_guest_smtp_notification_settings_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_guest_smtp_notification_settings_by_id(self,
                                                      id,
                                                      connection_timeout=None,
                                                      default_from_address=None,
                                                      notification_enabled=None,
                                                      password=None,
                                                      smtp_port=None,
                                                      smtp_server=None,
                                                      use_default_from_address=None,
                                                      use_password_authentication=None,
                                                      use_tlsor_ssl_encryption=None,
                                                      user_name=None,
                                                      headers=None,
                                                      payload=None,
                                                      active_validation=True,
                                                      **query_parameters):
        """This API allows the client to update a SMTP configuration
        setting.

        Args:
            connection_timeout(string): Interval in seconds for all
                the SMTP client connections, property of
                the request body.
            default_from_address(string): The default from email
                address to be used to send emails from,
                property of the request body.
            id(string): id, property of the request body.
            notification_enabled(boolean): Indicates if the email
                notification service is to be enabled,
                property of the request body.
            password(string): Password of Secure SMTP server,
                property of the request body.
            smtp_port(string): Port at which SMTP Secure Server is
                listening, property of the request body.
            smtp_server(string): The SMTP server ip address or fqdn
                such as outbound.mycompany.com, property
                of the request body.
            use_default_from_address(boolean): If the default from
                address should be used rather than using
                a sponsor user email address, property
                of the request body.
            use_password_authentication(boolean): If configured to
                true, SMTP server authentication will
                happen using username/password, property
                of the request body.
            use_tlsor_ssl_encryption(boolean): If configured to
                true, SMTP server authentication will
                happen using TLS/SSL, property of the
                request body.
            user_name(string): Username of Secure SMTP server,
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
                'smtpServer':
                    smtp_server,
                'notificationEnabled':
                    notification_enabled,
                'useDefaultFromAddress':
                    use_default_from_address,
                'defaultFromAddress':
                    default_from_address,
                'smtpPort':
                    smtp_port,
                'connectionTimeout':
                    connection_timeout,
                'useTLSorSSLEncryption':
                    use_tlsor_ssl_encryption,
                'usePasswordAuthentication':
                    use_password_authentication,
                'userName':
                    user_name,
                'password':
                    password,
            }
            _payload = {
                'ERSGuestSmtpNotificationSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a7500f6e473a50e19452683e303dd021_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/guestsmtpnotificationsettings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a7500f6e473a50e19452683e303dd021_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     connection_timeout=None,
                     default_from_address=None,
                     notification_enabled=None,
                     password=None,
                     smtp_port=None,
                     smtp_server=None,
                     use_default_from_address=None,
                     use_password_authentication=None,
                     use_tlsor_ssl_encryption=None,
                     user_name=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_guest_smtp_notification_settings_by_id <#ciscoisesdk.
        api.v3_1_1.guest_smtp_notification_configuration.
        GuestSmtpNotificationConfiguration.update_guest_smtp_notification_settings_by_id>`_
        """
        return self.update_guest_smtp_notification_settings_by_id(
            id=id,
            connection_timeout=connection_timeout,
            default_from_address=default_from_address,
            notification_enabled=notification_enabled,
            password=password,
            smtp_port=smtp_port,
            smtp_server=smtp_server,
            use_default_from_address=use_default_from_address,
            use_password_authentication=use_password_authentication,
            use_tlsor_ssl_encryption=use_tlsor_ssl_encryption,
            user_name=user_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_guest_smtp_notification_settings(self,
                                             filter=None,
                                             filter_type=None,
                                             page=None,
                                             size=None,
                                             sortasc=None,
                                             sortdsc=None,
                                             headers=None,
                                             **query_parameters):
        """This API allows the client to get all the guest SMTP
        notification configurations.   Filter:   [name]   To
        search guest users by using  toDate  column,follow the
        format:   DD-MON-YY (Example:13-SEP-18)     Day or
        Year:GET
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

        e_url = ('/ers/config/guestsmtpnotificationsettings')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e4c74e9b4e559e95c73e81183a6c7a_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_guest_smtp_notification_settings <#ciscoisesdk.
        api.v3_1_1.guest_smtp_notification_configuration.
        GuestSmtpNotificationConfiguration.get_guest_smtp_notification_settings>`_
        """
        return self.get_guest_smtp_notification_settings(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_guest_smtp_notification_settings_generator(self,
                                                       filter=None,
                                                       filter_type=None,
                                                       page=None,
                                                       size=None,
                                                       sortasc=None,
                                                       sortdsc=None,
                                                       headers=None,
                                                       **query_parameters):
        """This API allows the client to get all the guest SMTP
        notification configurations.   Filter:   [name]   To
        search guest users by using  toDate  column,follow the
        format:   DD-MON-YY (Example:13-SEP-18)     Day or
        Year:GET
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
            self.get_guest_smtp_notification_settings, dict(
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
        """Alias for `get_guest_smtp_notification_settings_generator <#ciscoisesdk.
        api.v3_1_1.guest_smtp_notification_configuration.
        GuestSmtpNotificationConfiguration.get_guest_smtp_notification_settings_generator>`_
        """
        yield from get_next_page(
            self.get_guest_smtp_notification_settings, dict(
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

    def create_guest_smtp_notification_settings(self,
                                                connection_timeout=None,
                                                default_from_address=None,
                                                notification_enabled=None,
                                                password=None,
                                                smtp_port=None,
                                                smtp_server=None,
                                                use_default_from_address=None,
                                                use_password_authentication=None,
                                                use_tlsor_ssl_encryption=None,
                                                user_name=None,
                                                headers=None,
                                                payload=None,
                                                active_validation=True,
                                                **query_parameters):
        """This API creates a guest SMTP notification configuration.

        Args:
            connection_timeout(string): Interval in seconds for all
                the SMTP client connections, property of
                the request body.
            default_from_address(string): The default from email
                address to be used to send emails from,
                property of the request body.
            notification_enabled(boolean): Indicates if the email
                notification service is to be enabled,
                property of the request body.
            password(string): Password of Secure SMTP server,
                property of the request body.
            smtp_port(string): Port at which SMTP Secure Server is
                listening, property of the request body.
            smtp_server(string): The SMTP server ip address or fqdn
                such as outbound.mycompany.com, property
                of the request body.
            use_default_from_address(boolean): If the default from
                address should be used rather than using
                a sponsor user email address, property
                of the request body.
            use_password_authentication(boolean): If configured to
                true, SMTP server authentication will
                happen using username/password, property
                of the request body.
            use_tlsor_ssl_encryption(boolean): If configured to
                true, SMTP server authentication will
                happen using TLS/SSL, property of the
                request body.
            user_name(string): Username of Secure SMTP server,
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
                'smtpServer':
                    smtp_server,
                'notificationEnabled':
                    notification_enabled,
                'useDefaultFromAddress':
                    use_default_from_address,
                'defaultFromAddress':
                    default_from_address,
                'smtpPort':
                    smtp_port,
                'connectionTimeout':
                    connection_timeout,
                'useTLSorSSLEncryption':
                    use_tlsor_ssl_encryption,
                'usePasswordAuthentication':
                    use_password_authentication,
                'userName':
                    user_name,
                'password':
                    password,
            }
            _payload = {
                'ERSGuestSmtpNotificationSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_de7c6f75f68b0d7df00dc72808d_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/guestsmtpnotificationsettings')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_de7c6f75f68b0d7df00dc72808d_v3_1_1', _api_response)

    def create(self,
               connection_timeout=None,
               default_from_address=None,
               notification_enabled=None,
               password=None,
               smtp_port=None,
               smtp_server=None,
               use_default_from_address=None,
               use_password_authentication=None,
               use_tlsor_ssl_encryption=None,
               user_name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_guest_smtp_notification_settings <#ciscoisesdk.
        api.v3_1_1.guest_smtp_notification_configuration.
        GuestSmtpNotificationConfiguration.create_guest_smtp_notification_settings>`_
        """
        return self.create_guest_smtp_notification_settings(
            connection_timeout=connection_timeout,
            default_from_address=default_from_address,
            notification_enabled=notification_enabled,
            password=password,
            smtp_port=smtp_port,
            smtp_server=smtp_server,
            use_default_from_address=use_default_from_address,
            use_password_authentication=use_password_authentication,
            use_tlsor_ssl_encryption=use_tlsor_ssl_encryption,
            user_name=user_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the guest smtp notification configuration.

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

        e_url = ('/ers/config/guestsmtpnotificationsettings/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a0c0e67aead55a2b4db67e9d068351a_v3_1_1', _api_response)
