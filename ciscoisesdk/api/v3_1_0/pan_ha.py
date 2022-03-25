# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine PAN HA API wrapper.

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


class PanHa(object):
    """Identity Services Engine PAN HA API (version: 3.1.0).

    Wraps the Identity Services Engine PAN HA
    API and exposes the API as native Python
    methods that return native Python objects.

    APIs for the configuration, administration and monitoring of the nodes in an ISE cluster deployment.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PanHa
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PanHa, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_pan_ha_status(self,
                          headers=None,
                          **query_parameters):
        """In a high availability configuration, the Primary Administration
        Node (PAN) is in the active state. The Secondary PAN
        (backup PAN) is in the standby state, which means it
        receives all configuration updates from the Primary PAN,
        but is not active in the ISE network. You can configure
        ISE to automatically the promote the secondary PAN when
        the primary PAN becomes unavailable.

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
            pass

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

        e_url = ('/api/v1/deployment/pan-ha')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_daa171ab765a02a714c48376b3790d_v3_1_0', _api_response)

    def enable_pan_ha(self,
                      failed_attempts=None,
                      is_enabled=None,
                      polling_interval=None,
                      primary_health_check_node=None,
                      secondary_health_check_node=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **query_parameters):
        """To deploy the auto-failover feature, you must have at least
        three nodes, where two of the nodes assume the
        Administration persona, and one node acts as the health
        check node. A health check node is a non-administration
        node and can be a Policy Service, Monitoring, or pxGrid
        node, or a combination of these. If the PANs are in
        different data centers, you must have a health check
        node for each PAN.

        Args:
            failed_attempts(integer): failedAttempts, property of
                the request body.
            is_enabled(boolean): isEnabled, property of the request
                body.
            polling_interval(integer): pollingInterval, property of
                the request body.
            primary_health_check_node(string):
                primaryHealthCheckNode, property of the
                request body. Constraints: maxLength set
                to 64 and minLength set to 1.
            secondary_health_check_node(string):
                secondaryHealthCheckNode, property of
                the request body. Constraints: maxLength
                set to 64 and minLength set to 1.
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
            pass

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
                'isEnabled':
                    is_enabled,
                'primaryHealthCheckNode':
                    primary_health_check_node,
                'secondaryHealthCheckNode':
                    secondary_health_check_node,
                'pollingInterval':
                    polling_interval,
                'failedAttempts':
                    failed_attempts,
            }
            _payload = {
                'request': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fc9a4ee495785518bd2251b6b4fb41f4_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/deployment/pan-ha')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_fc9a4ee495785518bd2251b6b4fb41f4_v3_1_0', _api_response)

    def disable_pan_ha(self,
                       headers=None,
                       **query_parameters):
        """Disable the automatic PAN failover.

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
            pass

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

        e_url = ('/api/v1/deployment/pan-ha')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1e3cde0c3f254b39caaaf7c907ae67e_v3_1_0', _api_response)
