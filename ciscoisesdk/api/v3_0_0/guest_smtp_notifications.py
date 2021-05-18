# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine GuestSMTPNotifications API wrapper.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)
import urllib.parse


class GuestSmtpNotifications(object):
    """Identity Services Engine GuestSMTPNotifications API (version: 3.0.0).

    Wraps the Identity Services Engine GuestSMTPNotifications
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new GuestSmtpNotifications
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(GuestSmtpNotifications, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_guest_smtp_notification_settings(self,
                                                 filter=None,
                                                 filter_type=None,
                                                 page=None,
                                                 size=None,
                                                 sortasc=None,
                                                 sortdec=None,
                                                 headers=None,
                                                 **query_parameters):
        """Get all Guest SMTP Notifications Settings.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdec(basestring): sortdec query parameter. sort desc.
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

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sortasc, basestring)
        check_type(sortdec, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sortasc':
                sortasc,
            'sortdec':
                sortdec,
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

        return self._object_factory('bpm_e4c74e9b4e559e95c73e81183a6c7a_v3_0_0', _api_response)

    def get_all_guest_smtp_notification_settings_generator(self,
                                                           filter=None,
                                                           filter_type=None,
                                                           page=None,
                                                           size=None,
                                                           sortasc=None,
                                                           sortdec=None,
                                                           headers=None,
                                                           **query_parameters):
        """Get all Guest SMTP Notifications Settings.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdec(basestring): sortdec query parameter. sort desc.
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
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sortasc, basestring)
        check_type(sortdec, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sortasc':
                sortasc,
            'sortdec':
                sortdec,
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

        yield self._object_factory('bpm_e4c74e9b4e559e95c73e81183a6c7a_v3_0_0', _api_response)
        if _api_response.response and _api_response.response.get("SearchResult", {}).get("nextPage", {}).get("href", ""):
            url = _api_response.response.get("SearchResult", {}).get("nextPage", {}).get("href", "")
            _query_params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            _size = _query_params.get('size')
            _page = _query_params.get('page')
            yield from self.get_all_guest_smtp_notification_settings_generator(headers=headers,
                                                                               filter=filter,
                                                                               filter_type=filter_type,
                                                                               sortasc=sortasc,
                                                                               sortdec=sortdec,
                                                                               page=_page,
                                                                               size=_size,
                                                                               **query_parameters)

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
        """Create Guest SMTP Notifications Settings.

        Args:
            connection_timeout(string): connectionTimeout, property
                of the request body.
            default_from_address(string): defaultFromAddress,
                property of the request body.
            notification_enabled(boolean): notificationEnabled,
                property of the request body.
            password(string): password, property of the request
                body.
            smtp_port(string): smtpPort, property of the request
                body.
            smtp_server(string): smtpServer, property of the request
                body.
            use_default_from_address(boolean):
                useDefaultFromAddress, property of the
                request body.
            use_password_authentication(boolean):
                usePasswordAuthentication, property of
                the request body.
            use_tlsor_ssl_encryption(boolean):
                useTLSorSSLEncryption, property of the
                request body.
            user_name(string): userName, property of the request
                body.
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
            self._request_validator('jsd_de7c6f75f68b0d7df00dc72808d_v3_0_0')\
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

        return self._object_factory('bpm_de7c6f75f68b0d7df00dc72808d_v3_0_0', _api_response)

    def get_guest_smtp_notification_settings_by_id(self,
                                                   id,
                                                   headers=None,
                                                   **query_parameters):
        """Get Guest SMTP Notifications Settings by Id.

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

        return self._object_factory('bpm_ca28129793d1569bb50de9f43b0d0ee8_v3_0_0', _api_response)

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
        """Update Guest SMTP Notifications Settings.

        Args:
            connection_timeout(string): connectionTimeout, property
                of the request body.
            default_from_address(string): defaultFromAddress,
                property of the request body.
            notification_enabled(boolean): notificationEnabled,
                property of the request body.
            password(string): password, property of the request
                body.
            smtp_port(string): smtpPort, property of the request
                body.
            smtp_server(string): smtpServer, property of the request
                body.
            use_default_from_address(boolean):
                useDefaultFromAddress, property of the
                request body.
            use_password_authentication(boolean):
                usePasswordAuthentication, property of
                the request body.
            use_tlsor_ssl_encryption(boolean):
                useTLSorSSLEncryption, property of the
                request body.
            user_name(string): userName, property of the request
                body.
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
            self._request_validator('jsd_a7500f6e473a50e19452683e303dd021_v3_0_0')\
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

        return self._object_factory('bpm_a7500f6e473a50e19452683e303dd021_v3_0_0', _api_response)
