# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine guestsmtpnotificationsettings API wrapper.

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


class Guestsmtpnotificationsettings(object):
    """Identity Services Engine guestsmtpnotificationsettings API (version: 3.5.0).

    Wraps the Identity Services Engine guestsmtpnotificationsettings
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Guestsmtpnotificationsettings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Guestsmtpnotificationsettings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_guestsmtpnotificationsettings(self,
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
                Fields:[name].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name, description].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name, description].
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

        e_url = ('/ers/config/guestsmtpnotificationsettings/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d758067dcf5c65a5dd3bc4e014c056_v3_5_0', _api_response)

    def get_guestsmtpnotificationsettings_generator(self,
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
                Fields:[name].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name, description].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name, description].
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
            self.get_guestsmtpnotificationsettings, dict(
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

    def create_guestsmtpnotificationsettings(self,
                                             connection_timeout=None,
                                             default_from_address=None,
                                             description=None,
                                             id=None,
                                             name=None,
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
        """Create.

        Args:
            connection_timeout(string): Interval in seconds for all
                the SMTP client connections, property of
                the request body.
            default_from_address(string): the default From email
                address to be used to send emails from,
                property of the request body.
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            notification_enabled(boolean): indicates if the email
                notification service is to be enabled,
                property of the request body.
            password(string): Password of Secure SMTP server,
                property of the request body.
            smtp_port(string): Port at which SMTP Secure Server is
                listening, property of the request body.
            smtp_server(string): the SMTP server ip address or fqdn
                such as outbound.mycompany.com, property
                of the request body.
            use_default_from_address(boolean): if the default from
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
                'defaultFromAddress':
                    default_from_address,
                'notificationEnabled':
                    notification_enabled,
                'smtpServer':
                    smtp_server,
                'useDefaultFromAddress':
                    use_default_from_address,
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
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSGuestSmtpNotificationSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f39be92053a15df8ba8cdb7e3c7f7a09_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestsmtpnotificationsettings/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f39be92053a15df8ba8cdb7e3c7f7a09_v3_5_0', _api_response)

    def get_guestsmtpnotificationsettings_by_id(self,
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

        e_url = ('/ers/config/guestsmtpnotificationsettings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ca28129793d1569bb50de9f43b0d0ee8_v3_5_0', _api_response)

    def update_guestsmtpnotificationsettings_by_id(self,
                                                   id,
                                                   connection_timeout=None,
                                                   default_from_address=None,
                                                   description=None,
                                                   name=None,
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
        """Update.

        Args:
            connection_timeout(string): Interval in seconds for all
                the SMTP client connections, property of
                the request body.
            default_from_address(string): the default From email
                address to be used to send emails from,
                property of the request body.
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            notification_enabled(boolean): indicates if the email
                notification service is to be enabled,
                property of the request body.
            password(string): Password of Secure SMTP server,
                property of the request body.
            smtp_port(string): Port at which SMTP Secure Server is
                listening, property of the request body.
            smtp_server(string): the SMTP server ip address or fqdn
                such as outbound.mycompany.com, property
                of the request body.
            use_default_from_address(boolean): if the default from
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
                'defaultFromAddress':
                    default_from_address,
                'notificationEnabled':
                    notification_enabled,
                'smtpServer':
                    smtp_server,
                'useDefaultFromAddress':
                    use_default_from_address,
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
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSGuestSmtpNotificationSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a7500f6e473a50e19452683e303dd021_v3_5_0')\
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

        return self._object_factory('bpm_a7500f6e473a50e19452683e303dd021_v3_5_0', _api_response)

    def patch_guestsmtpnotificationsettings_by_id(self,
                                                  id,
                                                  connection_timeout=None,
                                                  default_from_address=None,
                                                  description=None,
                                                  name=None,
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
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            connection_timeout(string): Interval in seconds for all
                the SMTP client connections, property of
                the request body.
            default_from_address(string): the default From email
                address to be used to send emails from,
                property of the request body.
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            notification_enabled(boolean): indicates if the email
                notification service is to be enabled,
                property of the request body.
            password(string): Password of Secure SMTP server,
                property of the request body.
            smtp_port(string): Port at which SMTP Secure Server is
                listening, property of the request body.
            smtp_server(string): the SMTP server ip address or fqdn
                such as outbound.mycompany.com, property
                of the request body.
            use_default_from_address(boolean): if the default from
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
                'defaultFromAddress':
                    default_from_address,
                'notificationEnabled':
                    notification_enabled,
                'smtpServer':
                    smtp_server,
                'useDefaultFromAddress':
                    use_default_from_address,
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
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSGuestSmtpNotificationSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b567b3c2e23f5ad6bff0528becdf8f4e_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/guestsmtpnotificationsettings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_b567b3c2e23f5ad6bff0528becdf8f4e_v3_5_0', _api_response)
