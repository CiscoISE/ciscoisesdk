# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI fixtures and tests.

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

import pytest
from ciscoisesdk import IdentityServicesEngineAPI
from tests.config import (
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_VERIFY,
    DEFAULT_WAIT_ON_RATE_LIMIT
)
from tests.environment import (
    IDENTITY_SERVICES_ENGINE_ENCODED_AUTH,
    IDENTITY_SERVICES_ENGINE_PASSWORD,
    IDENTITY_SERVICES_ENGINE_USERNAME,
    IDENTITY_SERVICES_ENGINE_VERSION,
)
from tests.mock.mock import get_free_port, get_mock_url, start_mock_server
from tests.models.schema_validator import SchemaValidator


# Fixtures
@pytest.fixture(scope="session")
def free_port():
    return get_free_port()


@pytest.fixture(scope="session")
def base_url(free_port):
    return get_mock_url(free_port)


@pytest.fixture(scope="session")
def mock_identity_services_engine_server(free_port):
    start_mock_server(free_port, IDENTITY_SERVICES_ENGINE_VERSION)
    return


@pytest.fixture(scope="session")
def api(mock_identity_services_engine_server, base_url):
    return IdentityServicesEngineAPI(username=IDENTITY_SERVICES_ENGINE_USERNAME,
                                     password=IDENTITY_SERVICES_ENGINE_PASSWORD,
                                     encoded_auth=IDENTITY_SERVICES_ENGINE_ENCODED_AUTH,
                                     base_url=base_url,
                                     single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                                     wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT,
                                     verify=DEFAULT_VERIFY,
                                     version=IDENTITY_SERVICES_ENGINE_VERSION,
                                     uses_api_gateway=True)


@pytest.fixture(scope="session")
def validator():
    return SchemaValidator(IDENTITY_SERVICES_ENGINE_VERSION).json_schema_validate
