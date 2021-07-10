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
    json_schema_validate('jsd_bda58fc63575503b80c024dbe02cf547_v3_0_0').validate(obj.response)
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


def is_valid_post_device_admin_network_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_83ea4e38c44e5b1c90b19af25b88546e_v3_0_0').validate(obj.response)
    return True


def post_device_admin_network_condition(api):
    endpoint_result = api.device_administration_network_conditions.post_device_admin_network_condition(
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
def test_post_device_admin_network_condition(api, validator):
    try:
        assert is_valid_post_device_admin_network_condition(
            validator,
            post_device_admin_network_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def post_device_admin_network_condition_default(api):
    endpoint_result = api.device_administration_network_conditions.post_device_admin_network_condition(
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
def test_post_device_admin_network_condition_default(api, validator):
    try:
        assert is_valid_post_device_admin_network_condition(
            validator,
            post_device_admin_network_condition_default(api)
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
    json_schema_validate('jsd_a3640f918edb5df99d09001ca9e12688_v3_0_0').validate(obj.response)
    return True


def get_device_admin_network_condition_by_condition_id(api):
    endpoint_result = api.device_administration_network_conditions.get_device_admin_network_condition_by_condition_id(
        condition_id='string'
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
        condition_id='string'
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


def is_valid_put_device_admin_network_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b371441bddfd5d819a7aedfa215f4aeb_v3_0_0').validate(obj.response)
    return True


def put_device_admin_network_condition_by_condition_id(api):
    endpoint_result = api.device_administration_network_conditions.put_device_admin_network_condition_by_condition_id(
        active_validation=False,
        cli_dnis_list=['string'],
        condition_id='string',
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
def test_put_device_admin_network_condition_by_condition_id(api, validator):
    try:
        assert is_valid_put_device_admin_network_condition_by_condition_id(
            validator,
            put_device_admin_network_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_device_admin_network_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_network_conditions.put_device_admin_network_condition_by_condition_id(
        active_validation=False,
        condition_id='string',
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
def test_put_device_admin_network_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_put_device_admin_network_condition_by_condition_id(
            validator,
            put_device_admin_network_condition_by_condition_id_default(api)
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
    json_schema_validate('jsd_037e7b011df45066b55be86033ecd17a_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_network_condition_by_condition_id(api):
    endpoint_result = api.device_administration_network_conditions.delete_device_admin_network_condition_by_condition_id(
        condition_id='string'
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
        condition_id='string'
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
