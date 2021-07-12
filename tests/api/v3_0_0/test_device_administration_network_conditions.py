# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_network_conditions API fixtures and tests.

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


def is_valid_get_device_admin_network_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b4ceac9ee830523ca5ddbfdf3e1b44be_v3_0_0').validate(obj.response)
    return True


def get_device_admin_network_conditions(api):
    endpoint_result = api.device_administration_network_conditions.get_device_admin_network_conditions(

    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_get_device_admin_network_conditions(api, validator):
    try:
        assert is_valid_get_device_admin_network_conditions(
            validator,
            get_device_admin_network_conditions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_network_conditions_default(api):
    endpoint_result = api.device_administration_network_conditions.get_device_admin_network_conditions(

    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_get_device_admin_network_conditions_default(api, validator):
    try:
        assert is_valid_get_device_admin_network_conditions(
            validator,
            get_device_admin_network_conditions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_network_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b95cf8c9aed95518b38be1fa4b514b67_v3_0_0').validate(obj.response)
    return True


def create_device_admin_network_condition(api):
    endpoint_result = api.device_administration_network_conditions.create_device_admin_network_condition(
        active_validation=False,
        cli_dnis_list=['string'],
        condition_type='string',
        description='string',
        device_group_list=['string'],
        device_list=['string'],
        id='string',
        ip_addr_list=['string'],
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        mac_addr_list=['string'],
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_create_device_admin_network_condition(api, validator):
    try:
        assert is_valid_create_device_admin_network_condition(
            validator,
            create_device_admin_network_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_admin_network_condition_default(api):
    endpoint_result = api.device_administration_network_conditions.create_device_admin_network_condition(
        active_validation=False,
        cli_dnis_list=None,
        condition_type=None,
        description=None,
        device_group_list=None,
        device_list=None,
        id=None,
        ip_addr_list=None,
        link=None,
        mac_addr_list=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_create_device_admin_network_condition_default(api, validator):
    try:
        assert is_valid_create_device_admin_network_condition(
            validator,
            create_device_admin_network_condition_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_network_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_33e9cc593c395c48b31b30149467c846_v3_0_0').validate(obj.response)
    return True


def get_device_admin_network_condition_by_condition_id(api):
    endpoint_result = api.device_administration_network_conditions.get_device_admin_network_condition_by_condition_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_get_device_admin_network_condition_by_condition_id(api, validator):
    try:
        assert is_valid_get_device_admin_network_condition_by_condition_id(
            validator,
            get_device_admin_network_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_network_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_network_conditions.get_device_admin_network_condition_by_condition_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_get_device_admin_network_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_network_condition_by_condition_id(
            validator,
            get_device_admin_network_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_network_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_23f78898b7d655b2b81085dc7c0a964e_v3_0_0').validate(obj.response)
    return True


def update_device_admin_network_condition_by_condition_id(api):
    endpoint_result = api.device_administration_network_conditions.update_device_admin_network_condition_by_condition_id(
        active_validation=False,
        cli_dnis_list=['string'],
        condition_type='string',
        description='string',
        device_group_list=['string'],
        device_list=['string'],
        id='string',
        ip_addr_list=['string'],
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        mac_addr_list=['string'],
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_update_device_admin_network_condition_by_condition_id(api, validator):
    try:
        assert is_valid_update_device_admin_network_condition_by_condition_id(
            validator,
            update_device_admin_network_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_admin_network_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_network_conditions.update_device_admin_network_condition_by_condition_id(
        active_validation=False,
        id='string',
        cli_dnis_list=None,
        condition_type=None,
        description=None,
        device_group_list=None,
        device_list=None,
        ip_addr_list=None,
        link=None,
        mac_addr_list=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_update_device_admin_network_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_update_device_admin_network_condition_by_condition_id(
            validator,
            update_device_admin_network_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_network_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7c0b4d1bbda75355912f208521362a41_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_network_condition_by_condition_id(api):
    endpoint_result = api.device_administration_network_conditions.delete_device_admin_network_condition_by_condition_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_delete_device_admin_network_condition_by_condition_id(api, validator):
    try:
        assert is_valid_delete_device_admin_network_condition_by_condition_id(
            validator,
            delete_device_admin_network_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_network_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_network_conditions.delete_device_admin_network_condition_by_condition_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_network_conditions
def test_delete_device_admin_network_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_network_condition_by_condition_id(
            validator,
            delete_device_admin_network_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
