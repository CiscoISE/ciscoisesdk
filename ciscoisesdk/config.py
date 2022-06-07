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
DEFAULT_VERSION = '3.1_Patch_1'

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

#: **uses_api_gateway** default value.
#: Controls whether ISE use the gateway or not.
DEFAULT_USES_API_GATEWAY = True

#: **uses_csrf_token** default value.
#: Controls wheter we send the X-CSRF-Token to ISE' ERS APIs.
DEFAULT_USES_CSRF_TOKEN = False
