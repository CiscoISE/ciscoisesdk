# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI pan_ha API fixtures and tests.

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
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_pan_ha_status(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_02daa171ab765a02a714c48376b3790d_v3_1_0').validate(obj.response)
    return True


def get_pan_ha_status(api):
    endpoint_result = api.pan_ha.get_pan_ha_status(

    )
    return endpoint_result


@pytest.mark.pan_ha
def test_get_pan_ha_status(api, validator):
    try:
        assert is_valid_get_pan_ha_status(
            validator,
            get_pan_ha_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_pan_ha_status_default(api):
    endpoint_result = api.pan_ha.get_pan_ha_status(

    )
    return endpoint_result


@pytest.mark.pan_ha
def test_get_pan_ha_status_default(api, validator):
    try:
        assert is_valid_get_pan_ha_status(
            validator,
            get_pan_ha_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_enable_pan_ha(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_fc9a4ee495785518bd2251b6b4fb41f4_v3_1_0').validate(obj.response)
    return True


def enable_pan_ha(api):
    endpoint_result = api.pan_ha.enable_pan_ha(
        active_validation=False,
        failed_attempts=0,
        is_enabled=True,
        payload=None,
        polling_interval=0,
        primary_health_check_node='string',
        secondary_health_check_node='string'
    )
    return endpoint_result


@pytest.mark.pan_ha
def test_enable_pan_ha(api, validator):
    try:
        assert is_valid_enable_pan_ha(
            validator,
            enable_pan_ha(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def enable_pan_ha_default(api):
    endpoint_result = api.pan_ha.enable_pan_ha(
        active_validation=False,
        failed_attempts=None,
        is_enabled=None,
        payload=None,
        polling_interval=None,
        primary_health_check_node=None,
        secondary_health_check_node=None
    )
    return endpoint_result


@pytest.mark.pan_ha
def test_enable_pan_ha_default(api, validator):
    try:
        assert is_valid_enable_pan_ha(
            validator,
            enable_pan_ha_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disable_pan_ha(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_a1e3cde0c3f254b39caaaf7c907ae67e_v3_1_0').validate(obj.response)
    return True


def disable_pan_ha(api):
    endpoint_result = api.pan_ha.disable_pan_ha(

    )
    return endpoint_result


@pytest.mark.pan_ha
def test_disable_pan_ha(api, validator):
    try:
        assert is_valid_disable_pan_ha(
            validator,
            disable_pan_ha(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disable_pan_ha_default(api):
    endpoint_result = api.pan_ha.disable_pan_ha(

    )
    return endpoint_result


@pytest.mark.pan_ha
def test_disable_pan_ha_default(api, validator):
    try:
        assert is_valid_disable_pan_ha(
            validator,
            disable_pan_ha_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
