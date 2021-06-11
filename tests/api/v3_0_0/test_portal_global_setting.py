# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI portal_global_setting API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_all_portal_global_settings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e9ce4a1e1cf955f098343646760e9d58_v3_0_0').validate(obj.response)
    return True


def get_all_portal_global_settings(api):
    endpoint_result = api.portal_global_setting.get_all_portal_global_settings(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.portal_global_setting
def test_get_all_portal_global_settings(api, validator):
    try:
        assert is_valid_get_all_portal_global_settings(
            validator,
            get_all_portal_global_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_portal_global_settings_default(api):
    endpoint_result = api.portal_global_setting.get_all_portal_global_settings(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.portal_global_setting
def test_get_all_portal_global_settings_default(api, validator):
    try:
        assert is_valid_get_all_portal_global_settings(
            validator,
            get_all_portal_global_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_portal_global_setting_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0ac243ecb8c157658a4bcfe77a102c14_v3_0_0').validate(obj.response)
    return True


def get_portal_global_setting_by_id(api):
    endpoint_result = api.portal_global_setting.get_portal_global_setting_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.portal_global_setting
def test_get_portal_global_setting_by_id(api, validator):
    try:
        assert is_valid_get_portal_global_setting_by_id(
            validator,
            get_portal_global_setting_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_portal_global_setting_by_id_default(api):
    endpoint_result = api.portal_global_setting.get_portal_global_setting_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.portal_global_setting
def test_get_portal_global_setting_by_id_default(api, validator):
    try:
        assert is_valid_get_portal_global_setting_by_id(
            validator,
            get_portal_global_setting_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_portal_global_setting_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c97e7851003e5a63a2a8005ac8807dc7_v3_0_0').validate(obj.response)
    return True


def update_portal_global_setting_by_id(api):
    endpoint_result = api.portal_global_setting.update_portal_global_setting_by_id(
        active_validation=False,
        customization='string',
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.portal_global_setting
def test_update_portal_global_setting_by_id(api, validator):
    try:
        assert is_valid_update_portal_global_setting_by_id(
            validator,
            update_portal_global_setting_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_portal_global_setting_by_id_default(api):
    endpoint_result = api.portal_global_setting.update_portal_global_setting_by_id(
        active_validation=False,
        id='string',
        customization=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.portal_global_setting
def test_update_portal_global_setting_by_id_default(api, validator):
    try:
        assert is_valid_update_portal_global_setting_by_id(
            validator,
            update_portal_global_setting_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
