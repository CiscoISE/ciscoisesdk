# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI system_health API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_healths(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0f67f5c0641d55708b20ffc56f374854_v3_1_0').validate(obj.response)
    return True


def get_healths(api):
    endpoint_result = api.system_health.get_healths(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.system_health
def test_get_healths(api, validator):
    try:
        assert is_valid_get_healths(
            validator,
            get_healths(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_healths_default(api):
    endpoint_result = api.system_health.get_healths(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.system_health
def test_get_healths_default(api, validator):
    try:
        assert is_valid_get_healths(
            validator,
            get_healths_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_performances(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_048aadb0c21d5146a207994d493fe9a5_v3_1_0').validate(obj.response)
    return True


def get_performances(api):
    endpoint_result = api.system_health.get_performances(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.system_health
def test_get_performances(api, validator):
    try:
        assert is_valid_get_performances(
            validator,
            get_performances(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_performances_default(api):
    endpoint_result = api.system_health.get_performances(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.system_health
def test_get_performances_default(api, validator):
    try:
        assert is_valid_get_performances(
            validator,
            get_performances_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
