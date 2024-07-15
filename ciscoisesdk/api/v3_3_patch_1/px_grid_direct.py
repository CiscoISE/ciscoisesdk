# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine pxGrid Direct API wrapper.

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

from builtins import *
from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class PxGridDirect(object):
    """Identity Services Engine pxGrid Direct API (version: 3.3_patch_1).

    Wraps the Identity Services Engine pxGrid Direct
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PxGridDirect
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PxGridDirect, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_connector_config(self,
                             headers=None,
                             **query_parameters):
        """pxGrid Direct Get ALL connectorConfig information.

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

        e_url = ('/api/v1/pxgrid-direct/connector-config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d1004b4485c06871c0c86358068cb_v3_3_patch_1', _api_response)

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
        """pxGrid Direct Configure connectorconfig information.

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
            self._request_validator('jsd_af9c8ad00e925e6885c3b3167dbdb4a3_v3_3_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/pxgrid-direct/connector-config')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_af9c8ad00e925e6885c3b3167dbdb4a3_v3_3_patch_1', _api_response)

    def get_connector_config_by_connector_name(self,
                                               connector_name,
                                               headers=None,
                                               **query_parameters):
        """pxGrid Direct Get connectorConfig information based on
        ConnectorName.

        Args:
            connector_name(str): connectorName path
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
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connector_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }

        e_url = ('/api/v1/pxgrid-direct/connector-config/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d4fedcc553a3966efb225bd927c6_v3_3_patch_1', _api_response)

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
        """pxGrid Direct update Configure connectorConfig information based
        on ConnectorName.

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
            connector_name(str): connectorName path
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
        check_type(connector_name, str,
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
            self._request_validator('jsd_dbcbf6ee965b90a47c157c87efef5f_v3_3_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/pxgrid-direct/connector-config/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_dbcbf6ee965b90a47c157c87efef5f_v3_3_patch_1', _api_response)

    def delete_connector_config_by_connector_name(self,
                                                  connector_name,
                                                  headers=None,
                                                  **query_parameters):
        """pxGrid Direct Delete Configure connectorConfig information based
        on ConnectorName.

        Args:
            connector_name(str): connectorName path
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
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(connector_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }

        e_url = ('/api/v1/pxgrid-direct/connector-config/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dbb36cd7f25770b884da5053decff4_v3_3_patch_1', _api_response)

    def getpxgrid_direct_dictionary_references(self,
                                               headers=None,
                                               **query_parameters):
        """pxGrid Direct Get a map of references to pxgrid-direct
        dictionaries.

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

        e_url = ('/api/v1/pxgrid-direct/dictionary-references')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a85e09e275340b9c39f9f0cc77902_v3_3_patch_1', _api_response)

    def get_connector_config_sync_now_status(self,
                                             connector_name,
                                             headers=None,
                                             **query_parameters):
        """This API is used to get the status for SyncNow Status    It
        returns the sync status as      syncstatus     QUEUED
        ,means its in  QUEUED state   SUBMITTED ,means its in
        Submited to fetch the data   INPROGRESS ,means its
        inprogress of fetching and saving in ISE   ERRORED
        ,means some internal error while fetching and saving in
        ISE further debugging logs will help   COMPLETED ,means
        its COMPLETED of fetching and saving in ISE
        SCH_INPROGRESS ,means its inprogress for schedule time
        fetch and saving in ISE   SCH_SUBMITTED ,means its
        submitted for schedule time fetch and will start to
        saving in ISE    CANCELED ,means its cancelled if any of
        ISE Service start when its in middle of
        QUEUED/SUBMITTED/INPROGRESS     connectorName    .

        Args:
            connector_name(str): connectorName path
                parameter. retrieve the connector
                syncnow status.
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
        check_type(connector_name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'connectorName': connector_name,
        }

        e_url = ('/api/v1/pxgrid-direct/syncNowStatus/{connectorName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f5ea29c9654f99a341aff1c064f9b_v3_3_patch_1', _api_response)

    def sync_now_connector(self,
                           connector_name=None,
                           description=None,
                           sync_type=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """  This syncNow is used on demand on a URLFetch Type connector
        only  Following parameters are present in the POST
        request body         PARAMETER   DESCRIPTION   EXAMPLE
        SyncType *required   its for FULL or INCREMENTAL
        "SyncType": "FULL or INCREMENTAL"       connectorName
        *required   Name of the Connector for only URLFetcher
        type   name of Connector       description   Decription
        of the Connector   "length": "256 character"
        NOTE:  For  Use syncNowStatus api to get the status of
        the connector    .

        Args:
            sync_type(string): connector Type list, property of the
                request body. Available values are
                'FULL' and 'INCREMENTAL'.
            connector_name(string): connectorName, property of the
                request body.
            description(string): description, property of the
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
            _tmp_payload = {
                'SyncType':
                    sync_type,
                'connectorName':
                    connector_name,
                'description':
                    description,
            }
            _payload = {
                'connector': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a83fbc2fed26547b964c13e5771038f7_v3_3_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/pxgrid-direct/syncnow')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a83fbc2fed26547b964c13e5771038f7_v3_3_patch_1', _api_response)

    def test_connector(self,
                       auth_type=None,
                       auth_values=None,
                       connector_name=None,
                       response_parsing=None,
                       skip_certificate_validations=None,
                       unique_id=None,
                       url=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **query_parameters):
        """pxGrid Direct test the Connector.

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
            skip_certificate_validations(boolean):
                skipCertificateValidations, property of
                the request body.
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
                'authType':
                    auth_type,
                'authValues':
                    auth_values,
                'connectorName':
                    connector_name,
                'responseParsing':
                    response_parsing,
                'skipCertificateValidations':
                    skip_certificate_validations,
                'uniqueID':
                    unique_id,
                'url':
                    url,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d4ff0e7ffab4526fbdb811b264bba36d_v3_3_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/pxgrid-direct/test-connector')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d4ff0e7ffab4526fbdb811b264bba36d_v3_3_patch_1', _api_response)
