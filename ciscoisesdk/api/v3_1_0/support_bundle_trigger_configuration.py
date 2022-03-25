# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SupportBundleTriggerConfiguration API wrapper.

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


class SupportBundleTriggerConfiguration(object):
    """Identity Services Engine SupportBundleTriggerConfiguration API (version: 3.1.0).

    Wraps the Identity Services Engine SupportBundleTriggerConfiguration
    API and exposes the API as native Python
    methods that return native Python objects.

    | Support Bundle Trigger API allows clients to trigger support bundle provided the log settings are given using which the support needs to be generated.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | 0              | 1.0                  | 2.7                   | Initial Cisco ISE Version |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+

    |

    **Resource Definition**

    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | Attribute            | Type    | Required | Description                                                              | Default      Values                  |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | name                 | String  | Yes      | Resource      Name                                                       | supportBundle                        |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | id                   | String  | No       | Resource      UUID, mandatory for update                                 | 1af3d6e2-cc3b-4603-b80f-6827768335ab |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | description          | String  | No       | Support      Bundle Generation                                           |                                      |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | hostName             | String  | Yes      | This      parameter is hostName only, xxxx of xxxx.yyy.zz                | sampleHost                           |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | supportBundleOptions | List    | Yes      |                                                                          |                                      |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - includeConfigDB    | Boolean | Yes      | Set      to include Config DB in Support Bundle                          | false                                |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - includeDebugLogs   | Boolean | Yes      | Set      to include Debug logs in Support Bundle                         | false                                |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - includeLocalLogs   | Boolean | Yes      | Set      to include Local logs in Support Bundle                         | false                                |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - includeCoreFiles   | Boolean | Yes      | Set      to include Core files in Support Bundle                         | false                                |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - includeSystemLogs  | Boolean | Yes      | Set      to include System logs in Support Bundle                        | false                                |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - mntLogs            | Boolean | Yes      | Set      to include Monitoring and troublshooting logs in Support Bundle | false                                |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - policyXml          | Boolean | Yes      | Set      to include Policy XML in Support Bundle                         | false                                |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - fromDate           | Date    | No       | Date      from where support bundle should include the logs              | 04/21/2019                           |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+
    | - toDate             | Date    | No       | Date      upto where support bundle should include the logs              | 04/22/2019                           |
    +----------------------+---------+----------+--------------------------------------------------------------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SupportBundleTriggerConfiguration
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SupportBundleTriggerConfiguration, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_support_bundle(self,
                              description=None,
                              host_name=None,
                              name=None,
                              support_bundle_include_options=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """This API allows the client to create a support bundle trigger
        configuration.

        Args:
            description(string): description, property of the
                request body.
            host_name(string): This parameter is hostName only, xxxx
                of xxxx.yyy.zz, property of the request
                body.
            name(string): Resource Name, property of the request
                body.
            support_bundle_include_options(object):
                supportBundleIncludeOptions, property of
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
                'hostName':
                    host_name,
                'supportBundleIncludeOptions':
                    support_bundle_include_options,
            }
            _payload = {
                'SupportBundle': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fac48e5c63abfe2feec6fd1903_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/supportbundle')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_fac48e5c63abfe2feec6fd1903_v3_1_0', _api_response)

    def create(self,
               description=None,
               host_name=None,
               name=None,
               support_bundle_include_options=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_support_bundle <#ciscoisesdk.
        api.v3_1_0.support_bundle_trigger_configuration.
        SupportBundleTriggerConfiguration.create_support_bundle>`_
        """
        return self.create_support_bundle(
            description=description,
            host_name=host_name,
            name=name,
            support_bundle_include_options=support_bundle_include_options,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the support bundle trigger configuration.

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

        e_url = ('/ers/config/supportbundle/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a2b17c3c4eab52caa2fc7c811965c79d_v3_1_0', _api_response)
