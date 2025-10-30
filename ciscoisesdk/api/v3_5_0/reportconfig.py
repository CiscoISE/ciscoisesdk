# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine reportconfig API wrapper.

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


class Reportconfig(object):
    """Identity Services Engine reportconfig API (version: 3.5.0).

    Wraps the Identity Services Engine reportconfig
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Reportconfig
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Reportconfig, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_reportconfig(self,
                            contains_manual_defs=None,
                            contains_values=None,
                            policy_ver_id=None,
                            policy_ver_id_on_ise=None,
                            pull_id=None,
                            report_data=None,
                            report_type=None,
                            validation_result=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **query_parameters):
        """TrustSec-Query.

        Args:
            contains_manual_defs(string): containsManualDefs,
                property of the request body.
            contains_values(string): containsValues, property of the
                request body.
            policy_ver_id(string): policyVerId, property of the
                request body.
            policy_ver_id_on_ise(string): policyVerIdOnISE, property
                of the request body.
            pull_id(string): pullId, property of the request body.
            report_data(object): reportData, property of the request
                body.
            report_type(string): allowed values: DISABLED,
                DELTA_WITH_GEN_ID, DELTA_WITH_VALUES,
                FULL_WITH_GEN_ID, FULL_WITH_VALUES,
                FULL_INCLUDE_MANUAL_RULES,
                POLICY_VERSION_ID, property of the
                request body.
            validation_result(string): validationResult, property of
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
                'pullId':
                    pull_id,
                'policyVerId':
                    policy_ver_id,
                'policyVerIdOnISE':
                    policy_ver_id_on_ise,
                'validationResult':
                    validation_result,
                'reportType':
                    report_type,
                'containsValues':
                    contains_values,
                'containsManualDefs':
                    contains_manual_defs,
                'reportData':
                    report_data,
            }
            _payload = {
                'CTSReportConfig': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d79da2aa5ac9ad351ccd771ec6d3_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/reportconfig/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d79da2aa5ac9ad351ccd771ec6d3_v3_5_0', _api_response)
