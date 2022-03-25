# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Profiler API wrapper.

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


class Profiler(object):
    """Identity Services Engine Profiler API (version: 3.1.1).

    Wraps the Identity Services Engine Profiler
    API and exposes the API as native Python
    methods that return native Python objects.

    # Cisco ISE 3.0 pxGrid REST APIs


    ## License
    [Cisco Sample Code License](https://developer.cisco.com/site/license/cisco-sample-code-license/)


    ## Status
    These are the status icons for the requests so far.
    - ⌗ : must create resources to test
    - 🚧 : incomplete | untested
    - 🛑 : unsupported | bug

    ## Environment Variables
    This collection uses environment variables in scripts in the **Tests** tab to store data (`id`, `name`, `portalId`, etc.)  between requests. This allows you to `GET` or `POST` then immediately `GET {id}` on a resource. Using **No Environment** will cause this convenience functionality to fail so be sure to choose one.

    ## Collection Variables
    This collection includes some default variables that you will want to update or override with environment variables for your ISE deployment. Specifically, you will want to set:
    - `ise_pxg`: the ISE PAN node name or IP address. Default: `ise.securitydemo.net`
    - `rest_username`: the username for ERS API access. Must be a member of **SuperAdmin**, **ERSAdmin** or **ERSOperator** groups. Default: `admin` which is the ISE SuperAdmin
    - `rest_password`: Default: `C1sco12345`

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Profiler
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Profiler, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_profiles(self,
                     headers=None,
                     **query_parameters):
        """🚧 getProfiles.

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

        e_url = ('/pxgrid/ise/radius/ise/config/profiler/getProfiles')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dac693445cb95c6996cf6c7d85dece35_v3_1_1', _api_response)
