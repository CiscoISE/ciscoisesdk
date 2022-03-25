# -*- coding: utf-8 -*-
"""RestResponse class for representing the HTTP response.


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

import logging
from builtins import *

from .utils import extract_and_parse

logger = logging.getLogger(__name__)


# Main module interface
class RestResponse(object):
    """RestResponse to represent the response of the calls to the Identity Services Engine APIs."""

    def __init__(self, response):
        """Initialize a new RESTResponse object.

        """

        super(RestResponse, self).__init__()

        # Initialize attributes and properties
        self._headers = {**response.headers}
        self._content = bytes(response.content)
        self._text = str(response.text)
        self._response = extract_and_parse(response)
        self._status_code = response.status_code

    @property
    def headers(self):
        """The headers (MyDict) of the RestResponse."""
        return self._headers

    @property
    def content(self):
        """The content (bytes) of the RestResponse."""
        return self._content

    @property
    def text(self):
        """The text (str) of the RestResponse."""
        return self._text

    @property
    def response(self):
        """The response (MyDict) of the RestResponse."""
        return self._response

    @property
    def status_code(self):
        """The HTTP status code from the RestResponse."""
        return self._status_code

    @response.setter
    def response(self, value):
        """The response (MyDict) of the RestResponse."""
        self._response = value

    @headers.setter
    def headers(self, value):
        """The headers (MyDict) of the RestResponse."""
        self._headers = value
