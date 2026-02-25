# -*- coding: utf-8 -*-
"""ciscoisesdk/restsession.py Fixtures & Tests

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


import logging
import warnings

import ciscoisesdk
import pytest

from ciscoisesdk.restsession import RestSession

logging.captureWarnings(True)


# Helper Functions
def rate_limit_detected(w):
    """Check to see if a rate-limit warning is in the warnings list."""
    while w:
        if issubclass(w.pop().category, ciscoisesdk.RateLimitWarning):
            return True
    return False


# Tests
@pytest.mark.ratelimit
def test_rate_limit_retry(api):
    # Save state and initialize test setup
    original_wait_on_rate_limit = api.wait_on_rate_limit
    api.wait_on_rate_limit = True
    api.reinitialize()

    with warnings.catch_warnings(record=True) as w:
        authorization_profiles = api.authorization_profile.get_all()
        i = 0
        while i < len(authorization_profiles.response.SearchResult.resources):
            # Try and trigger a rate-limit
            api.authorization_profile.get_by_id(authorization_profiles.response.SearchResult.resources[i].id)
            i += 1
            if rate_limit_detected(w):
                break
    api.wait_on_rate_limit = original_wait_on_rate_limit
    api.reinitialize()


def test_client_cert_and_key(tmp_path):
    cert_file = tmp_path / 'client.crt'
    key_file = tmp_path / 'client.key'
    cert_file.write_text('dummy cert')
    key_file.write_text('dummy key')

    session = RestSession(
        get_access_token=lambda: 'token',
        access_token='token',
        base_url='https://example.local',
        verify=True,
        client_cert=str(cert_file),
        client_key=str(key_file),
        version='3.3_patch_1',
        wait_on_rate_limit=False,
        uses_csrf_token=False,
    )

    assert session.cert == (str(cert_file), str(key_file))


def test_client_key_without_cert_raises(tmp_path):
    key_file = tmp_path / 'client.key'
    key_file.write_text('dummy key')

    with pytest.raises(ValueError):
        RestSession(
            get_access_token=lambda: 'token',
            access_token='token',
            base_url='https://example.local',
            verify=True,
            client_key=str(key_file),
            version='3.3_patch_1',
            wait_on_rate_limit=False,
            uses_csrf_token=False,
        )
