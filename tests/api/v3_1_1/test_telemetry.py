# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI telemetry API fixtures and tests.

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
from fastjsonschema.exceptions import JsonSchemaException
from ciscoisesdk.exceptions import MalformedRequest
from ciscoisesdk.exceptions import ciscoisesdkException
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.1', reason='version does not match')


def is_valid_get_transport_gateway(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5f8b7d18b20e59428e711c8c762216ab_v3_1_1').validate(obj.response)
    return True


def get_transport_gateway(api):
    endpoint_result = api.telemetry.get_transport_gateway(

    )
    return endpoint_result


@pytest.mark.telemetry
def test_get_transport_gateway(api, validator):
    try:
        assert is_valid_get_transport_gateway(
            validator,
            get_transport_gateway(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_transport_gateway_default(api):
    endpoint_result = api.telemetry.get_transport_gateway(

    )
    return endpoint_result


@pytest.mark.telemetry
def test_get_transport_gateway_default(api, validator):
    try:
        assert is_valid_get_transport_gateway(
            validator,
            get_transport_gateway_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_transport_gateway(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b5d7c38199c9502f9f4233d5002cb7f6_v3_1_1').validate(obj.response)
    return True


def update_transport_gateway(api):
    endpoint_result = api.telemetry.update_transport_gateway(
        active_validation=False,
        enable_transport_gateway=True,
        payload=None,
        url='string'
    )
    return endpoint_result


@pytest.mark.telemetry
def test_update_transport_gateway(api, validator):
    try:
        assert is_valid_update_transport_gateway(
            validator,
            update_transport_gateway(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_transport_gateway_default(api):
    endpoint_result = api.telemetry.update_transport_gateway(
        active_validation=False,
        enable_transport_gateway=None,
        payload=None,
        url=None
    )
    return endpoint_result


@pytest.mark.telemetry
def test_update_transport_gateway_default(api, validator):
    try:
        assert is_valid_update_transport_gateway(
            validator,
            update_transport_gateway_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
