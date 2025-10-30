# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine ACI Connection API wrapper.

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


class AciConnection(object):
    """Identity Services Engine ACI Connection API (version: 3.5.0).

    Wraps the Identity Services Engine ACI Connection
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AciConnection
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AciConnection, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_aci_connections(self,
                            headers=None,
                            **query_parameters):
        """List all the ACI connections configured.

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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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

        e_url = ('/api/v1/trustsec/integration/aci-connection')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d13155a62a07e422109771c22_v3_5_0', _api_response)

    def save_aci_connection(self,
                            conn_mode=None,
                            domain=None,
                            error_reason=None,
                            hostname=None,
                            id=None,
                            learned_ips=None,
                            name=None,
                            name_conversion=None,
                            password=None,
                            selected_epgs=None,
                            sgt_ranges=None,
                            state=None,
                            used_sgt_ranges=None,
                            username=None,
                            validate_certificate=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """Saves ACI connection information with template and selected epg
        .

        Args:
            conn_mode(string): Out-of-Band/In-Band, property of the
                request body.
            domain(string): Auth Domain, property of the request
                body.
            error_reason(string): errorReason, property of the
                request body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): id, property of the request body.
            learned_ips(list): learnedIPs, property of the request
                body (list of objects).
            name(string): ACI name, property of the request body.
            name_conversion(object): Name conversion configuration,
                property of the request body.
            password(string): Password, property of the request
                body.
            selected_epgs(list): selectedEpgs, property of the
                request body (list of objects).
            sgt_ranges(list): sgtRanges, property of the request
                body (list of objects).
            state(string): Corresponding actions will change the
                state of the connection, property of the
                request body. Available values are
                'CONNECT', 'CONNECTING', 'DELETE_ERROR',
                'DELETING', 'ERROR', 'SUSPEND' and
                'UNDEPLOYED'.
            used_sgt_ranges(list): SGT ranges used by the
                connection, property of the request body
                (list of objects).
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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
                'connMode':
                    conn_mode,
                'domain':
                    domain,
                'errorReason':
                    error_reason,
                'hostname':
                    hostname,
                'id':
                    id,
                'learnedIPs':
                    learned_ips,
                'name':
                    name,
                'nameConversion':
                    name_conversion,
                'password':
                    password,
                'selectedEpgs':
                    selected_epgs,
                'sgtRanges':
                    sgt_ranges,
                'state':
                    state,
                'usedSgtRanges':
                    used_sgt_ranges,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f5532ce7f0c05f47bd404ee968336e04_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f5532ce7f0c05f47bd404ee968336e04_v3_5_0', _api_response)

    def action_aci_connector(self,
                             action=None,
                             connection_ids=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """ACI connection connect, suspend, delete multiple ACI
        connections.

        Args:
            connection_ids(list): ConnectionIDs, property of the
                request body (list of strings).
            action(string): action, property of the request body.
                Available values are 'Connect', 'Delete'
                and 'Suspend'.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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
                'ConnectionIDs':
                    connection_ids,
                'action':
                    action,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e18b485f51981a71887584f672_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/action')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e18b485f51981a71887584f672_v3_5_0', _api_response)

    def save_and_connect_to_aci(self,
                                conn_mode=None,
                                domain=None,
                                error_reason=None,
                                hostname=None,
                                id=None,
                                learned_ips=None,
                                name=None,
                                name_conversion=None,
                                password=None,
                                selected_epgs=None,
                                sgt_ranges=None,
                                state=None,
                                used_sgt_ranges=None,
                                username=None,
                                validate_certificate=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Save the ACI connection and connect to ACI.

        Args:
            conn_mode(string): Out-of-Band/In-Band, property of the
                request body.
            domain(string): Auth Domain, property of the request
                body.
            error_reason(string): errorReason, property of the
                request body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): id, property of the request body.
            learned_ips(list): learnedIPs, property of the request
                body (list of objects).
            name(string): ACI name, property of the request body.
            name_conversion(object): Name conversion configuration,
                property of the request body.
            password(string): Password, property of the request
                body.
            selected_epgs(list): selectedEpgs, property of the
                request body (list of objects).
            sgt_ranges(list): sgtRanges, property of the request
                body (list of objects).
            state(string): Corresponding actions will change the
                state of the connection, property of the
                request body. Available values are
                'CONNECT', 'CONNECTING', 'DELETE_ERROR',
                'DELETING', 'ERROR', 'SUSPEND' and
                'UNDEPLOYED'.
            used_sgt_ranges(list): SGT ranges used by the
                connection, property of the request body
                (list of objects).
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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
                'connMode':
                    conn_mode,
                'domain':
                    domain,
                'errorReason':
                    error_reason,
                'hostname':
                    hostname,
                'id':
                    id,
                'learnedIPs':
                    learned_ips,
                'name':
                    name,
                'nameConversion':
                    name_conversion,
                'password':
                    password,
                'selectedEpgs':
                    selected_epgs,
                'sgtRanges':
                    sgt_ranges,
                'state':
                    state,
                'usedSgtRanges':
                    used_sgt_ranges,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f1b4863b615b55866b8f7b292162f1_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/connect')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f1b4863b615b55866b8f7b292162f1_v3_5_0', _api_response)

    def get_contracts(self,
                      destinations=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **query_parameters):
        """Fetch contracts from ACI for the given Outbound SGT Domain Rules
        configuration.

        Args:
            destinations(list): destinations, property of the
                request body (list of objects).
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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
                'destinations':
                    destinations,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_be26438cd6a15c278e2daee272cfcc8c_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/contract/fetch')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_be26438cd6a15c278e2daee272cfcc8c_v3_5_0', _api_response)

    def get_auth_domains(self,
                         domain=None,
                         hostname=None,
                         id=None,
                         name=None,
                         password=None,
                         username=None,
                         validate_certificate=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **query_parameters):
        """Fetch Authentication Domains from ACI APIC.

        Args:
            domain(string): Auth Domain, property of the request
                body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): ID if connection is already created,
                property of the request body.
            name(string): ACI name, property of the request body.
            password(string): Password, property of the request
                body.
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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
                'domain':
                    domain,
                'hostname':
                    hostname,
                'id':
                    id,
                'name':
                    name,
                'password':
                    password,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e719b6f21b5a1ab15f559e1e73e2de_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/domain/fetch')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e719b6f21b5a1ab15f559e1e73e2de_v3_5_0', _api_response)

    def validate_aci_readiness(self,
                               headers=None,
                               **query_parameters):
        """Checks ISE readiness for ACI connection.

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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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

        e_url = ('/api/v1/trustsec/integration/aci-connection/ise-'
                 + 'readiness')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ad2c79167725c74a240370e8b165701_v3_5_0', _api_response)

    def get_reserved_sgt_ranges(self,
                                headers=None,
                                **query_parameters):
        """Get reserved SGT ranges list for given ACI connection.

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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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

        e_url = ('/api/v1/trustsec/integration/aci-connection/sgt-range')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ca9ab1d165256bfea36a5bca4eaad_v3_5_0', _api_response)

    def get_aci_connection_status(self,
                                  headers=None,
                                  **query_parameters):
        """ACI connection status of all ACI Connections.

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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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

        e_url = ('/api/v1/trustsec/integration/aci-connection/status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fb859850c8f85c0582a459952f74d565_v3_5_0', _api_response)

    def test_aci_connector(self,
                           domain=None,
                           hostname=None,
                           id=None,
                           name=None,
                           password=None,
                           username=None,
                           validate_certificate=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """ACI connection test the connection.

        Args:
            domain(string): Auth Domain, property of the request
                body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): ID if connection is already created,
                property of the request body.
            name(string): ACI name, property of the request body.
            password(string): Password, property of the request
                body.
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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
                'domain':
                    domain,
                'hostname':
                    hostname,
                'id':
                    id,
                'name':
                    name,
                'password':
                    password,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c58464984d9b51c2bc1f4e2634a19440_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-connection/test')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c58464984d9b51c2bc1f4e2634a19440_v3_5_0', _api_response)

    def get_aci_connection_by_id(self,
                                 connection_id,
                                 headers=None,
                                 **query_parameters):
        """Get ACI connection information based on connection id.

        Args:
            connection_id(str): connectionId path parameter. Unique
                id for ACI Connection.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connection_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectionId': connection_id,
        }

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/{connectionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d3d8977e55766a9570dfed93d612c_v3_5_0', _api_response)

    def update_aci_connection(self,
                              connection_id,
                              conn_mode=None,
                              domain=None,
                              error_reason=None,
                              hostname=None,
                              id=None,
                              learned_ips=None,
                              name=None,
                              name_conversion=None,
                              password=None,
                              selected_epgs=None,
                              sgt_ranges=None,
                              state=None,
                              used_sgt_ranges=None,
                              username=None,
                              validate_certificate=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Updates ACI connection information.

        Args:
            conn_mode(string): Out-of-Band/In-Band, property of the
                request body.
            domain(string): Auth Domain, property of the request
                body.
            error_reason(string): errorReason, property of the
                request body.
            hostname(string): ACI hostname or IP address, property
                of the request body.
            id(string): id, property of the request body.
            learned_ips(list): learnedIPs, property of the request
                body (list of objects).
            name(string): ACI name, property of the request body.
            name_conversion(object): Name conversion configuration,
                property of the request body.
            password(string): Password, property of the request
                body.
            selected_epgs(list): selectedEpgs, property of the
                request body (list of objects).
            sgt_ranges(list): sgtRanges, property of the request
                body (list of objects).
            state(string): Corresponding actions will change the
                state of the connection, property of the
                request body. Available values are
                'CONNECT', 'CONNECTING', 'DELETE_ERROR',
                'DELETING', 'ERROR', 'SUSPEND' and
                'UNDEPLOYED'.
            used_sgt_ranges(list): SGT ranges used by the
                connection, property of the request body
                (list of objects).
            username(string): Username, property of the request
                body.
            validate_certificate(boolean): ValidationCertificate,
                property of the request body.
            connection_id(str): connectionId path parameter. Unique
                id for ACI Connection.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

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
        check_type(connection_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectionId': connection_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'connMode':
                    conn_mode,
                'domain':
                    domain,
                'errorReason':
                    error_reason,
                'hostname':
                    hostname,
                'id':
                    id,
                'learnedIPs':
                    learned_ips,
                'name':
                    name,
                'nameConversion':
                    name_conversion,
                'password':
                    password,
                'selectedEpgs':
                    selected_epgs,
                'sgtRanges':
                    sgt_ranges,
                'state':
                    state,
                'usedSgtRanges':
                    used_sgt_ranges,
                'username':
                    username,
                'validateCertificate':
                    validate_certificate,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a2f9f1f682e153ed80b53a517454077e_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/{connectionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a2f9f1f682e153ed80b53a517454077e_v3_5_0', _api_response)

    def delete_aci_connection_by_id(self,
                                    connection_id,
                                    headers=None,
                                    **query_parameters):
        """delete ACI connection information based on connection id.

        Args:
            connection_id(str): connectionId path parameter. Unique
                id for ACI Connection.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connection_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectionId': connection_id,
        }

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/{connectionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fc810bd8c7375cc691087f0b3e749464_v3_5_0', _api_response)

    def connect_aci_connection_by_id(self,
                                     connection_id,
                                     headers=None,
                                     **query_parameters):
        """Connect to the ACI. Request body is optional to provide inbound
        and outbound rules during wizard flow.

        Args:
            connection_id(str): connectionId path parameter. Unique
                id for ACI Connection.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connection_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectionId': connection_id,
        }

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/{connectionId}/connect')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cde9587985761b57f7ca628e08df0_v3_5_0', _api_response)

    def get_connection_status_by_id(self,
                                    connection_id,
                                    headers=None,
                                    **query_parameters):
        """Returns the connection status by connection id.

        Args:
            connection_id(str): connectionId path parameter. Unique
                id for ACI Connection.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connection_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectionId': connection_id,
        }

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/{connectionId}/status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c85a93f936e359baa8d7e35dc4dcd13d_v3_5_0', _api_response)

    def suspend_aci_connection_by_id(self,
                                     connection_id,
                                     headers=None,
                                     **query_parameters):
        """Suspend ACI connection based on connection id.

        Args:
            connection_id(str): connectionId path parameter. Unique
                id for ACI Connection.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connection_id, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectionId': connection_id,
        }

        e_url = ('/api/v1/trustsec/integration/aci-'
                 + 'connection/{connectionId}/suspend')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a3836f43c1055fa839291fc91458827_v3_5_0', _api_response)
