# -*- coding: utf-8 -*-
"""Identity Services Engine Authentication API wrapper.

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

from future import standard_library

standard_library.install_aliases()

from base64 import b64encode
from builtins import *

from past.builtins import basestring

from ..utils import check_type, validate_base_url


class Authentication(object):
    """Identity Services Engine Authentication API.

    Wraps the Identity Services Engine Authentication API and exposes the API as native
    Python methods that return native Python objects.

    """

    def __init__(self, base_url, object_factory, single_request_timeout=None,
                 verify=True):
        """Initialize an Authentication
        object with the provided RestSession.

        Args:
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes.
            object_factory(callable): The factory function to use to create
                Python objects from the returned Identity Services Engine JSON data objects.
            single_request_timeout(int): Timeout in seconds for the API
                requests.
            verify(bool,basestring): Controls whether we verify the server's
                TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(base_url, basestring, may_be_none=False)
        check_type(single_request_timeout, int)
        check_type(verify, (bool, basestring), may_be_none=False)

        super(Authentication, self).__init__()

        self._base_url = str(validate_base_url(base_url))
        self._single_request_timeout = single_request_timeout
        self._verify = verify
        self._request_kwargs = {"timeout": single_request_timeout,
                                "verify": verify}
        self._object_factory = object_factory

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._verify

    @property
    def base_url(self):
        """The base URL for the API endpoints."""
        return self._base_url

    @property
    def single_request_timeout(self):
        """Timeout in seconds for the API requests."""
        return self._single_request_timeout

    @verify.setter
    def verify(self, value):
        """The verify (TLS Certificate) for the API endpoints."""
        check_type(value, (bool, basestring), may_be_none=False)
        self._verify = value
        self._request_kwargs = {"timeout": self._single_request_timeout,
                                "verify": self._verify}

    @base_url.setter
    def base_url(self, value):
        """The base URL for the API endpoints."""
        check_type(value, basestring, may_be_none=False)
        self._base_url = str(validate_base_url(value))

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """The timeout (seconds) for a single HTTP REST API request."""
        check_type(value, int)
        assert value is None or value > 0
        self._single_request_timeout = value
        self._request_kwargs = {"timeout": self._single_request_timeout,
                                "verify": self._verify}

    def authentication_api(self, username, password, encoded_auth=None):
        """Exchange basic auth data for a Authorization Basic encoded value
        that can be used to invoke the APIs.

        Args:
            username(basestring): HTTP Basic Auth username.
            password(basestring): HTTP Basic Auth password.
            encoded_auth(basestring): HTTP Basic Auth base64 encoded string.

        Returns:
            AccessToken: An AccessToken object with the access token provided
            by the Identity Services Engine cloud.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        if encoded_auth is not None:
            check_type(encoded_auth, basestring, may_be_none=False)
            if isinstance(encoded_auth, str):
                encoded_auth = bytes(encoded_auth, 'utf-8')
        else:
            check_type(username, basestring, may_be_none=False)
            check_type(password, basestring, may_be_none=False)
            encoded_auth = b64encode(bytes(username + ':' + password, "utf-8"))

        if isinstance(encoded_auth, bytes):
            encoded_auth = encoded_auth.decode('utf-8')

        json_data = {'Token': encoded_auth}
        return self._object_factory('bpm_ac8ae94c4e69a09d', json_data)
