# -*- coding: utf-8 -*-
"""Test suite environment variables.

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

import os

from .config import (
    USERNAME_ENVIRONMENT_VARIABLE, PASSWORD_ENVIRONMENT_VARIABLE,
    ENCODED_AUTH_ENVIRONMENT_VARIABLE, DEBUG_ENVIRONMENT_VARIABLE,
    VERSION_ENVIRONMENT_VARIABLE,
)

IDENTITY_SERVICES_ENGINE_USERNAME = os.getenv(USERNAME_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_PASSWORD = os.getenv(PASSWORD_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_ENCODED_AUTH = os.getenv(ENCODED_AUTH_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_DEBUG = os.getenv(DEBUG_ENVIRONMENT_VARIABLE, 'False')
IDENTITY_SERVICES_ENGINE_VERSION = os.getenv(VERSION_ENVIRONMENT_VARIABLE, '3.1.1')

if (IDENTITY_SERVICES_ENGINE_USERNAME is None or IDENTITY_SERVICES_ENGINE_PASSWORD is None)\
   and IDENTITY_SERVICES_ENGINE_ENCODED_AUTH is None:
    raise RuntimeError(
        "You must set {} and {} environment variables"
        " or set {} environment variable to run the test suite"
        "".format(USERNAME_ENVIRONMENT_VARIABLE,
                  PASSWORD_ENVIRONMENT_VARIABLE,
                  ENCODED_AUTH_ENVIRONMENT_VARIABLE)
    )
