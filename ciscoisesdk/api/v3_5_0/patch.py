# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Patch API wrapper.

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


class Patch(object):
    """Identity Services Engine Patch API (version: 3.5.0).

    Wraps the Identity Services Engine Patch
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Patch
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Patch, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def run_patch_pre_checks(self,
                             hostnames=None,
                             patch_bundle_name=None,
                             pre_check_report_id=None,
                             pre_checks=None,
                             re_trigger=None,
                             repo_name=None,
                             upgrade_type=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """Initiates prechecks execution on PPAN for complete deployment.
        It returns a precheck report id, which can be used to
        trigger patch installation later. Patch installation can
        happen in three modes :    Full Patch Installation ->
        Hostname needs to be an empty array. First patch will
        get installed on PPAN and then it will get installed on
        all other nodes parallelly.   Sequential Patch
        Installation -> Hostname needs to be an empty array.
        First patch will get installed on PPAN and then it will
        get installed on all other nodes sequentially.   Split
        -> This will happen in batches / iterations. Host name
        is mandatory. In first iteration only PPAN should be
        sent as part of hostname. Once the PPAN installation is
        successfull then remaining nodes can be sent in batches.
        upgradeType param can be specified as FULL_PATCH for
        full patch installation, SPLIT_PATCH for split patch
        installation and SEQUENTIAL_PATCH for sequential patch
        installation. upgrade type, patch bundle name,
        repository name are mandatory parameters. .

        Args:
            hostnames(list): hostnames, property of the request body
                (list of strings).
            patch_bundle_name(string): patchBundleName, property of
                the request body.
            pre_check_report_id(string): preCheckReportID, property
                of the request body.
            pre_checks(list): Array of prechecks that needs to be
                executed., property of the request body
                (list of strings).
            re_trigger(boolean): reTrigger, property of the request
                body.
            repo_name(string): repoName, property of the request
                body.
            upgrade_type(string): upgradeType, property of the
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
                'preChecks':
                    pre_checks,
                'hostnames':
                    hostnames,
                'upgradeType':
                    upgrade_type,
                'repoName':
                    repo_name,
                'patchBundleName':
                    patch_bundle_name,
                'preCheckReportID':
                    pre_check_report_id,
                'reTrigger':
                    re_trigger,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d7b50bf7b27578687ff200a936326ff_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/upgrade-patch/patch-install/pre-checks')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d7b50bf7b27578687ff200a936326ff_v3_5_0', _api_response)

    def get_patch_precheck_status(self,
                                  pre_check_report_id=None,
                                  precheck_name=None,
                                  headers=None,
                                  **query_parameters):
        """Get the latest precheck report. User can get status of an
        individual check by passing check's name. .

        Args:
            pre_check_report_id(str): preCheckReportID query
                parameter. Precheck report's id.
            precheck_name(str): precheckName query parameter.
                Precheck name.
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
        check_type(pre_check_report_id, str)
        check_type(precheck_name, str)

        _params = {
            'preCheckReportID':
                pre_check_report_id,
            'precheckName':
                precheck_name,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/upgrade-patch/patch-install/pre-checks-status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab6c86344ca598c80d41e7b0d329248_v3_5_0', _api_response)

    def install_patch(self,
                      headers=None,
                      **query_parameters):
        """Trigger patch installation on the Cisco ISE nodes.    In Full
        patch installation, patch will be installed on PPAN
        first, and then on following nodes.    In Split patch
        installation, patch will be installed on PPAN first, and
        then on the nodes in batches of the remaining
        iterations.     A task ID is returned which can be used
        to monitor the progress of the patch installation
        process. As the patch installation triggers the Cisco
        ISE to restart, the task API becomes unavailable for a
        certain period of time. When installation is going on
        PPAN, then monitor the progress on SPAN GUI. .

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

        e_url = ('/v1/upgrade-patch/patch-install')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d654ff67c54be93a6b720f73dc1dc_v3_5_0', _api_response)

    def patch_install_status(self,
                             pre_check_report_id=None,
                             headers=None,
                             **query_parameters):
        """Get the status of patch installation for the requested nodes.
        Precheck report Id obtained by running the precheck API
        can be passed to get the status. .

        Args:
            pre_check_report_id(str): preCheckReportID query
                parameter. Precheck report's id.
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
        check_type(pre_check_report_id, str)

        _params = {
            'preCheckReportID':
                pre_check_report_id,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/upgrade-patch/patch-install/get-status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b57abb188e75202ad3d10caa7cdf6a8_v3_5_0', _api_response)

    def get_installed_patches(self,
                              headers=None,
                              **query_parameters):
        """List all the installed patches in the system with the date of
        installation. .

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

        e_url = ('/v1/upgrade-patch/patch-install/list-patch')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aa7722a68b0b5f838831b3f9ea174bbe_v3_5_0', _api_response)

    def patch_rollback_info(self,
                            headers=None,
                            **query_parameters):
        """Get current and previous patch installed information.

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

        e_url = ('/v1/rollback/patch-rollback')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b662d1fe97b65f9a994c8d20388d403f_v3_5_0', _api_response)

    def rollback_patch(self,
                       pre_check_report_id=None,
                       headers=None,
                       **query_parameters):
        """Trigger patch rollback on the Cisco ISE nodes. Patch will be
        rolled back in other nodes first followed by P-PAN.
        Precheck report Id is mandatory which has been obtained
        by running patch rollback pre-checks API. Patch rollback
        progress can be monitored using patch rollback get
        status API.  When rollback is going on PPAN, then
        monitor the progress on SPAN GUI. .

        Args:
            pre_check_report_id(str): preCheckReportID query
                parameter. Precheck report's id.
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
        check_type(pre_check_report_id, str)

        _params = {
            'preCheckReportID':
                pre_check_report_id,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/rollback/patch-rollback')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fc25cd5d4d8662f06ae821d213_v3_5_0', _api_response)

    def run_rollback_pre_checks(self,
                                pre_check_report_id=None,
                                pre_checks=None,
                                re_trigger=None,
                                upgrade_type=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Initiates prechecks execution on PPAN for complete deployment.
        It returns a precheck report id, which can be used to
        trigger patch rollback later. Patch rollback can happen
        in two modes :    Full Patch Rollback -> Hostname needs
        to be an empty array. First patch will get installed on
        PPAN and then it will get installed on all other nodes
        parallelly.   Sequential Patch Rollback -> Hostname
        needs to be an empty array. First patch will get
        installed on PPAN and then it will get installed on all
        other nodes sequentially.    upgradeType param can be
        specified as PATCH_ROLLBACK for full patch rollback,
        PATCH_ROLLBACK_SEQUENTIAL for sequential patch rollback.
        upgrade type is mandatory parameter. .

        Args:
            pre_check_report_id(string): preCheckReportID, property
                of the request body.
            pre_checks(list): Array of prechecks that needs to be
                executed., property of the request body
                (list of strings).
            re_trigger(boolean): reTrigger, property of the request
                body.
            upgrade_type(string): upgradeType, property of the
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
                'upgradeType':
                    upgrade_type,
                'preChecks':
                    pre_checks,
                'preCheckReportID':
                    pre_check_report_id,
                'reTrigger':
                    re_trigger,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_bd5f6c29764549995d7f64a8aca4f43_v3_5_0')\
                .validate(_payload)

        e_url = ('/v1/rollback/patch-rollback/pre-checks')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_bd5f6c29764549995d7f64a8aca4f43_v3_5_0', _api_response)

    def get_rollback_precheck_status(self,
                                     pre_check_id=None,
                                     pre_check_report_id=None,
                                     headers=None,
                                     **query_parameters):
        """Get the latest precheck report. .

        Args:
            pre_check_report_id(str): preCheckReportID query
                parameter. Precheck report's id.
            pre_check_id(str): preCheckID query parameter.
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
        check_type(pre_check_report_id, str)
        check_type(pre_check_id, str)

        _params = {
            'preCheckReportID':
                pre_check_report_id,
            'preCheckID':
                pre_check_id,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/rollback/patch-rollback/pre-checks-status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e99695845f5491ebff92ac67af49_v3_5_0', _api_response)

    def patch_rollback_summary(self,
                               headers=None,
                               **query_parameters):
        """get the summary of patch rollback .

        Args:
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/rollback/patch-rollback/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ee0526c3e57252a19342978b5fd3477b_v3_5_0', _api_response)

    def patch_rollback_proceed_status(self,
                                      pre_check_report_id=None,
                                      headers=None,
                                      **query_parameters):
        """Get the status of patch rollback for the requested nodes.
        Precheck report Id obtained by running the precheck API
        is mandatory to get the status. .

        Args:
            pre_check_report_id(str): preCheckReportID query
                parameter. Precheck report's id.
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
        check_type(pre_check_report_id, str)

        _params = {
            'preCheckReportID':
                pre_check_report_id,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/rollback/patch-rollback/get-status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f4aba05786145944866f064786b4c9c5_v3_5_0', _api_response)

    def patch_summary(self,
                      headers=None,
                      **query_parameters):
        """get the summary of patch install process .

        Args:
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/upgrade-patch/patch-install/get-summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bb836f58f1d153c1837f25f9a660600c_v3_5_0', _api_response)
