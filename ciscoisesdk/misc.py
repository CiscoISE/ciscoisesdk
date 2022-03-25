# -*- coding: utf-8 -*-
"""Package helper functions and classes.

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
native_str = str

from builtins import *

from past.builtins import basestring

from .exceptions import ApiError, RateLimitError
from .response_codes import RATE_LIMIT_RESPONSE_CODE


def check_response_code(response, expected_response_code, **kwargs):
    """Check response code against the expected code; raise ApiError.

    Checks the requests.response.status_code against the provided expected
    response code (erc), and raises a ApiError if they do not match.

    Args:
        response(requests.response): The response object returned by a request
            using the requests package.
        expected_response_code(int): The expected response code (HTTP response
            code).

    Raises:
        ApiError: If the requests.response.status_code does not match the
            provided expected response code (erc).

     """
    if response.status_code in expected_response_code:
        pass
    elif response.status_code == RATE_LIMIT_RESPONSE_CODE:
        raise RateLimitError(response, **kwargs)
    else:
        raise ApiError(response, **kwargs)
