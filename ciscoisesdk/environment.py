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

#: name of the environment debug variable
DEBUG_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_DEBUG'

# Identity Services Engine API version. Format: MAJOR.MINOR.PATCH
#: name of the environment version variable
VERSION_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_VERSION'

#: name of the environment username variable
USERNAME_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_USERNAME'

#: name of the environment password variable
PASSWORD_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_PASSWORD'

#: name of the environment encoded_auth variable
ENCODED_AUTH_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_ENCODED_AUTH'

#: name of the environment base_url variable
BASE_URL_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_BASE_URL'

#: name of the environment single_request_timeout variable
SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE = \
    'IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT'

#: name of the environment wait_on_rate_limit variable
WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT'

#: name of the environment verify variable
VERIFY_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_VERIFY'

#: name of the environment verify variable
VERIFY_STRING_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_VERIFY_STRING'

#: name of the environment uses_api_gateway variable
USES_API_GATEWAY_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY'

#: name of the environment ui_base_url variable
UI_BASE_URL_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_UI_BASE_URL'

#: name of the environment ers_base_url variable
ERS_BASE_URL_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_ERS_BASE_URL'

#: name of the environment mnt_base_url variable
MNT_BASE_URL_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_MNT_BASE_URL'

#: name of the environment px_grid_base_url variable
PX_GRID_BASE_URL_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_PX_GRID_BASE_URL'

#: name of the envirorment use_csrf_token
USES_CSRF_TOKEN_ENVIRONMENT_VARIABLE = 'IDENTITY_SERVICES_ENGINE_USES_CSRF_TOKEN'


def is_bool(value):
    if isinstance(value, str):
        return 'true' in value.lower()
    else:
        return bool(value)


def _get_env_value(env_var, env_type, cast_func):
    env_var_value = os.getenv(env_var)
    if isinstance(env_var_value, env_type):
        return env_var_value
    elif env_var_value is not None:
        return cast_func(env_var_value)
    else:
        return env_var_value


def get_env_username():
    IDENTITY_SERVICES_ENGINE_USERNAME = os.getenv(USERNAME_ENVIRONMENT_VARIABLE)
    return IDENTITY_SERVICES_ENGINE_USERNAME


def get_env_password():
    IDENTITY_SERVICES_ENGINE_PASSWORD = os.getenv(PASSWORD_ENVIRONMENT_VARIABLE)
    return IDENTITY_SERVICES_ENGINE_PASSWORD


def get_env_encoded_auth():
    IDENTITY_SERVICES_ENGINE_ENCODED_AUTH = os.getenv(ENCODED_AUTH_ENVIRONMENT_VARIABLE)
    return IDENTITY_SERVICES_ENGINE_ENCODED_AUTH


def get_env_debug():
    IDENTITY_SERVICES_ENGINE_DEBUG = _get_env_value(
        DEBUG_ENVIRONMENT_VARIABLE,
        str, is_bool)
    return IDENTITY_SERVICES_ENGINE_DEBUG


def get_env_version():
    IDENTITY_SERVICES_ENGINE_VERSION = _get_env_value(
        VERSION_ENVIRONMENT_VARIABLE, str, str)
    return IDENTITY_SERVICES_ENGINE_VERSION


def get_env_base_url():
    IDENTITY_SERVICES_ENGINE_BASE_URL = _get_env_value(
        BASE_URL_ENVIRONMENT_VARIABLE, str, str)
    return IDENTITY_SERVICES_ENGINE_BASE_URL


def get_env_single_request_timeout():
    IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT = _get_env_value(
        SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE,
        int, int)
    return IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT


def get_env_wait_on_rate_limit():
    IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT = _get_env_value(
        WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE,
        bool, is_bool)
    return IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT


def get_env_verify():
    IDENTITY_SERVICES_ENGINE_VERIFY = _get_env_value(
        VERIFY_STRING_ENVIRONMENT_VARIABLE, str, str) or \
        _get_env_value(VERIFY_ENVIRONMENT_VARIABLE, bool, is_bool)
    return IDENTITY_SERVICES_ENGINE_VERIFY


def get_env_uses_api_gateway():
    IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY = _get_env_value(
        USES_API_GATEWAY_ENVIRONMENT_VARIABLE, str, is_bool)
    return IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY


def get_env_ui_base_url():
    IDENTITY_SERVICES_ENGINE_UI_BASE_URL = os.getenv(UI_BASE_URL_ENVIRONMENT_VARIABLE)
    return IDENTITY_SERVICES_ENGINE_UI_BASE_URL


def get_env_ers_base_url():
    IDENTITY_SERVICES_ENGINE_ERS_BASE_URL = os.getenv(ERS_BASE_URL_ENVIRONMENT_VARIABLE)
    return IDENTITY_SERVICES_ENGINE_ERS_BASE_URL


def get_env_mnt_base_url():
    IDENTITY_SERVICES_ENGINE_MNT_BASE_URL = os.getenv(MNT_BASE_URL_ENVIRONMENT_VARIABLE)
    return IDENTITY_SERVICES_ENGINE_MNT_BASE_URL


def get_env_px_grid_base_url():
    IDENTITY_SERVICES_ENGINE_PX_GRID_BASE_URL = os.getenv(PX_GRID_BASE_URL_ENVIRONMENT_VARIABLE)
    return IDENTITY_SERVICES_ENGINE_PX_GRID_BASE_URL


def get_env_uses_csrf_token():
    IDENTITY_SERVICES_ENGINE_USES_CSRF_TOKEN = _get_env_value(
        USES_CSRF_TOKEN_ENVIRONMENT_VARIABLE,
        bool, is_bool)
    return IDENTITY_SERVICES_ENGINE_USES_CSRF_TOKEN
