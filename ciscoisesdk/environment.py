# -*- coding: utf-8 -*-
"""Package environment variables.

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
    USERNAME_ENVIRONMENT_VARIABLE,
    PASSWORD_ENVIRONMENT_VARIABLE,
    ENCODED_AUTH_ENVIRONMENT_VARIABLE,
    DEBUG_ENVIRONMENT_VARIABLE,
    VERSION_ENVIRONMENT_VARIABLE,
    BASE_URL_ENVIRONMENT_VARIABLE,
    SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE,
    WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE,
    VERIFY_ENVIRONMENT_VARIABLE,
    VERIFY_STRING_ENVIRONMENT_VARIABLE,
    DEFAULT_DEBUG,
    DEFAULT_VERSION,
    DEFAULT_BASE_URL,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT,
    DEFAULT_VERIFY,
    DEFAULT_USES_API_GATEWAY,
    USES_API_GATEWAY_ENVIRONMENT_VARIABLE,
    UI_BASE_URL_ENVIRONMENT_VARIABLE,
    ERS_BASE_URL_ENVIRONMENT_VARIABLE,
    MNT_BASE_URL_ENVIRONMENT_VARIABLE,
    PX_GRID_BASE_URL_ENVIRONMENT_VARIABLE,
)


def is_bool(value):
    if isinstance(value, str):
        return 'true' in value.lower()
    else:
        return bool(value)


def _get_env_value(env_var, default_value, env_type, cast_func):
    env_var_value = os.getenv(env_var, default_value)
    if isinstance(env_var_value, env_type):
        return env_var_value
    elif env_var_value is not None:
        return cast_func(env_var_value)
    else:
        return env_var_value


IDENTITY_SERVICES_ENGINE_USERNAME = os.getenv(USERNAME_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_PASSWORD = os.getenv(PASSWORD_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_ENCODED_AUTH = os.getenv(ENCODED_AUTH_ENVIRONMENT_VARIABLE)

IDENTITY_SERVICES_ENGINE_DEBUG = _get_env_value(
    DEBUG_ENVIRONMENT_VARIABLE, DEFAULT_DEBUG,
    str, is_bool)
IDENTITY_SERVICES_ENGINE_VERSION = _get_env_value(
    VERSION_ENVIRONMENT_VARIABLE, DEFAULT_VERSION, str, str)
IDENTITY_SERVICES_ENGINE_BASE_URL = _get_env_value(
    BASE_URL_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL, str, str)
IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT = _get_env_value(
    SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE,
    DEFAULT_SINGLE_REQUEST_TIMEOUT, int, int)
IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT = _get_env_value(
    WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE,
    DEFAULT_WAIT_ON_RATE_LIMIT, bool, is_bool)
IDENTITY_SERVICES_ENGINE_VERIFY = _get_env_value(
    VERIFY_STRING_ENVIRONMENT_VARIABLE, None, str, str) or \
    _get_env_value(VERIFY_ENVIRONMENT_VARIABLE, DEFAULT_VERIFY, bool, is_bool)
IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY = _get_env_value(
    USES_API_GATEWAY_ENVIRONMENT_VARIABLE, DEFAULT_USES_API_GATEWAY,
    str, is_bool)
IDENTITY_SERVICES_ENGINE_UI_BASE_URL = os.getenv(UI_BASE_URL_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_ERS_BASE_URL = os.getenv(ERS_BASE_URL_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_MNT_BASE_URL = os.getenv(MNT_BASE_URL_ENVIRONMENT_VARIABLE)
IDENTITY_SERVICES_ENGINE_PX_GRID_BASE_URL = os.getenv(PX_GRID_BASE_URL_ENVIRONMENT_VARIABLE)
