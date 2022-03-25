# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine PxGridSettings API wrapper.

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


class PxGridSettings(object):
    """Identity Services Engine PxGridSettings API (version: 3.1.1).

    Wraps the Identity Services Engine PxGridSettings
    API and exposes the API as native Python
    methods that return native Python objects.

    | pxGrid Settings API allows the client to change auto-approve settings for pxGrid nodes. **Note:** From Cisco ISE Release 3.1, all pxGrid connections must be based on pxGrid 2.0. pxGrid 1.0-based (XMPP-based) integrations will cease to work on Cisco ISE from Release 3.1 onwards. pxGrid Version 2.0, which is based on WebSockets, was introduced in Cisco ISE Release 2.4. We recommend that you plan and upgrade your other systems to pxGrid 2.0-compliant versions in order to prevent potential disruptions, if any, to integrations.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 3.0                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +------------------------------+----------+--------------+---------------------------------------------------+--------------------+--------------------+
    | **Attribute**                | **Type** | **Required** | **Description**                                   | **Default Values** | **Example Values** |
    +------------------------------+----------+--------------+---------------------------------------------------+--------------------+--------------------+
    | name                         | String   | Yes          | Resource Name                                     |                    |                    |
    +------------------------------+----------+--------------+---------------------------------------------------+--------------------+--------------------+
    | id                           | String   | No           | Resource UUID, mandatory for update               |                    |                    |
    +------------------------------+----------+--------------+---------------------------------------------------+--------------------+--------------------+
    | description                  | String   | No           |                                                   |                    |                    |
    +------------------------------+----------+--------------+---------------------------------------------------+--------------------+--------------------+
    | autoApproveCertBasedAccounts | Boolean  | Yes          | Auto approve certificate based accounts when true | false              | true               |
    +------------------------------+----------+--------------+---------------------------------------------------+--------------------+--------------------+
    | allowPasswordBasedAccounts   | Boolean  | Yes          | Allow password based acoounts when true           | false              |                    |
    +------------------------------+----------+--------------+---------------------------------------------------+--------------------+--------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PxGridSettings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PxGridSettings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def autoapprove_px_grid_settings(self,
                                     allow_password_based_accounts=None,
                                     auto_approve_cert_based_accounts=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """This API allows the client to auto approve the pxGrid settings.

        Args:
            allow_password_based_accounts(boolean): Allow password
                based accounts when true, property of
                the request body.
            auto_approve_cert_based_accounts(boolean): Auto approve
                certificate based accounts when true,
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
                'autoApproveCertBasedAccounts':
                    auto_approve_cert_based_accounts,
                'allowPasswordBasedAccounts':
                    allow_password_based_accounts,
            }
            _payload = {
                'PxgridSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e5dd9b5979a409b9f456265db0_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/pxgridsettings/autoapprove')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e5dd9b5979a409b9f456265db0_v3_1_1', _api_response)

    def autoapprove(self,
                    allow_password_based_accounts=None,
                    auto_approve_cert_based_accounts=None,
                    headers=None,
                    payload=None,
                    active_validation=True,
                    **query_parameters):
        """Alias for `autoapprove_px_grid_settings <#ciscoisesdk.
        api.v3_1_1.px_grid_settings.
        PxGridSettings.autoapprove_px_grid_settings>`_
        """
        return self.autoapprove_px_grid_settings(
            allow_password_based_accounts=allow_password_based_accounts,
            auto_approve_cert_based_accounts=auto_approve_cert_based_accounts,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the pxGrid settings.

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

        e_url = ('/ers/config/pxgridsettings/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bea00c7a4f9b5e1798ea078e123ff016_v3_1_1', _api_response)
