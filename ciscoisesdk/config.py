# -*- coding: utf-8 -*-
# Package configuration.

# Copyright (c) 2021 Cisco and/or its affiliates.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Package Constants

#: **debug** default value.
DEFAULT_DEBUG = 'False'

#: **version** default value.
DEFAULT_VERSION = '3.0.0'

#: **base_url** default value.
DEFAULT_BASE_URL = 'https://dcloud-dna-ise-rtp.cisco.com'

#: **single_request_timeout** default value.
#: Timeout (in seconds) for the RESTful HTTP requests.
DEFAULT_SINGLE_REQUEST_TIMEOUT = 60

#: **wait_on_rate_limit** default value.
#: Enables or disables automatic rate-limit handling.
DEFAULT_WAIT_ON_RATE_LIMIT = True

#: **verify** default value.
#: Controls whether to verify the server's TLS certificate or not.
DEFAULT_VERIFY = True

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

#: **uses_api_gateway** default value.
#: Controls whether ISE use the gateway or not.
DEFAULT_USES_API_GATEWAY = True

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
