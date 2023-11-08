# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Edda API wrapper.

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


class Edda(object):
    """Identity Services Engine Edda API (version: 3.2_beta).

    Wraps the Identity Services Engine Edda
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Edda
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Edda, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_connector_config(self,
                             headers=None,
                             **query_parameters):
        """EDDA Get ALL connectorConfig information.

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
                           basestring)

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

        e_url = ('/api/v1/edda/connector-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c8f79c0801555878ad94493ade34587_v3_2_beta', _api_response)

    def create_connector_config(self,
                                additional_properties=None,
                                attributes=None,
                                connector_name=None,
                                connector_type=None,
                                deltasync_schedule=None,
                                description=None,
                                enabled=None,
                                fullsync_schedule=None,
                                protocol=None,
                                skip_certificate_validations=None,
                                url=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """EDDA Configure connectorconfig information.

        Args:
            additional_properties(object): additionalProperties,
                property of the request body.
            attributes(object): connectorName, property of the
                request body.
            connector_name(string): connectorName, property of the
                request body.
            connector_type(string): connector Type list, property of
                the request body. Available values are
                'urlfetcher' and 'vmware'.
            deltasync_schedule(object): deltasyncSchedule, property
                of the request body.
            description(string): description, property of the
                request body.
            enabled(boolean): enabled, property of the request body.
            fullsync_schedule(object): fullsyncSchedule, property of
                the request body.
            protocol(string): protocol, property of the request
                body.
            skip_certificate_validations(boolean):
                skipCertificateValidations, property of
                the request body.
            url(object): url, property of the request body.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
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
                'additionalProperties':
                    additional_properties,
                'attributes':
                    attributes,
                'connectorName':
                    connector_name,
                'connectorType':
                    connector_type,
                'deltasyncSchedule':
                    deltasync_schedule,
                'description':
                    description,
                'enabled':
                    enabled,
                'fullsyncSchedule':
                    fullsync_schedule,
                'protocol':
                    protocol,
                'skipCertificateValidations':
                    skip_certificate_validations,
                'url':
                    url,
            }
            _payload = {
                'connector': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c89285c31159faa2fb8abee25ce4a4_v3_2_beta')\
                .validate(_payload)

        e_url = ('/api/v1/edda/connector-config')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c89285c31159faa2fb8abee25ce4a4_v3_2_beta', _api_response)

    def get_connector_config_by_connector_name(self,
                                               connector_name,
                                               headers=None,
                                               **query_parameters):
        """EDDA Get connectorConfig information based on ConnectorName.

        Args:
            connector_name(basestring): connectorName path
                parameter. update or delete or retrieve
                the connector config.
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
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connector_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }

        e_url = ('/api/v1/edda/connector-config/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a3c21e5b61d95a0b9acf313e3ea03ad7_v3_2_beta', _api_response)

    def update_connector_config_by_connector_name(self,
                                                  connector_name,
                                                  additional_properties=None,
                                                  attributes=None,
                                                  connector_type=None,
                                                  deltasync_schedule=None,
                                                  description=None,
                                                  enabled=None,
                                                  fullsync_schedule=None,
                                                  protocol=None,
                                                  skip_certificate_validations=None,
                                                  url=None,
                                                  headers=None,
                                                  payload=None,
                                                  active_validation=True,
                                                  **query_parameters):
        """EDDA update Configure connectorConfig information based on
        ConnectorName.

        Args:
            additional_properties(object): additionalProperties,
                property of the request body.
            attributes(object): connectorName, property of the
                request body.
            connector_name(string): connectorName, property of the
                request body.
            connector_type(string): connector Type list, property of
                the request body. Available values are
                'urlfetcher' and 'vmware'.
            deltasync_schedule(object): deltasyncSchedule, property
                of the request body.
            description(string): description, property of the
                request body.
            enabled(boolean): enabled, property of the request body.
            fullsync_schedule(object): fullsyncSchedule, property of
                the request body.
            protocol(string): protocol, property of the request
                body.
            skip_certificate_validations(boolean):
                skipCertificateValidations, property of
                the request body.
            url(object): url, property of the request body.
            connector_name(basestring): connectorName path
                parameter. update or delete or retrieve
                the connector config.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
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
        check_type(connector_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalProperties':
                    additional_properties,
                'attributes':
                    attributes,
                'connectorName':
                    connector_name,
                'connectorType':
                    connector_type,
                'deltasyncSchedule':
                    deltasync_schedule,
                'description':
                    description,
                'enabled':
                    enabled,
                'fullsyncSchedule':
                    fullsync_schedule,
                'protocol':
                    protocol,
                'skipCertificateValidations':
                    skip_certificate_validations,
                'url':
                    url,
            }
            _payload = {
                'connector': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f5b69ccd0075b18a3de9e72b9e450cb_v3_2_beta')\
                .validate(_payload)

        e_url = ('/api/v1/edda/connector-config/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f5b69ccd0075b18a3de9e72b9e450cb_v3_2_beta', _api_response)

    def delete_connector_config_by_connector_name(self,
                                                  connector_name,
                                                  headers=None,
                                                  **query_parameters):
        """EDDA Delete Configure connectorConfig information based on
        ConnectorName.

        Args:
            connector_name(basestring): connectorName path
                parameter. update or delete or retrieve
                the connector config.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connector_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }

        e_url = ('/api/v1/edda/connector-config/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b1f3a77153ee82dca51d2a94f5b9_v3_2_beta', _api_response)

    def get_edda_dictionary_references(self,
                                       headers=None,
                                       **query_parameters):
        """EDDA Get a map of references to EDDA dictionaries.

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
                           basestring)

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

        e_url = ('/api/v1/edda/dictionary-references')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bcc373fcfcd5bf69742d3d63dd6f92a_v3_2_beta', _api_response)

    def test_connector(self,
                       auth_type=None,
                       auth_values=None,
                       connector_name=None,
                       response_parsing=None,
                       unique_id=None,
                       url=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **query_parameters):
        """EDDA test the Connector.

        Args:
            auth_type(string): authentication Type list, property of
                the request body. Available values are
                'apikey' and 'basic'.
            auth_values(object): Request  to test Connector,
                property of the request body.
            connector_name(string): connectorName, property of the
                request body.
            response_parsing(string): uniqueness to identify,
                property of the request body.
            unique_id(string): uniqueness to identify, property of
                the request body.
            url(string): bulkUrl, property of the request body.
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
            _payload = {
                'authType':
                    auth_type,
                'authValues':
                    auth_values,
                'connectorName':
                    connector_name,
                'responseParsing':
                    response_parsing,
                'uniqueID':
                    unique_id,
                'url':
                    url,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ed122b5ef64b5ecabe3526490589e041_v3_2_beta')\
                .validate(_payload)

        e_url = ('/api/v1/edda/test-connector')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ed122b5ef64b5ecabe3526490589e041_v3_2_beta', _api_response)
