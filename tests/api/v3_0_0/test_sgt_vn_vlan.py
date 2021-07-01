# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sgt_vn_vlan API fixtures and tests.

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


def is_valid_get_all_security_groups_to_vn_to_vlan(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e51b6e745cdb5bdda4de26a27b8d92bb_v3_0_0').validate(obj.response)
    return True


def get_all_security_groups_to_vn_to_vlan(api):
    endpoint_result = api.sgt_vn_vlan.get_all_security_groups_to_vn_to_vlan(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_get_all_security_groups_to_vn_to_vlan(api, validator):
    try:
        assert is_valid_get_all_security_groups_to_vn_to_vlan(
            validator,
            get_all_security_groups_to_vn_to_vlan(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_security_groups_to_vn_to_vlan_default(api):
    endpoint_result = api.sgt_vn_vlan.get_all_security_groups_to_vn_to_vlan(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_get_all_security_groups_to_vn_to_vlan_default(api, validator):
    try:
        assert is_valid_get_all_security_groups_to_vn_to_vlan(
            validator,
            get_all_security_groups_to_vn_to_vlan_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_security_groups_to_vn_to_vlan(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_97830a0710ba581da4d3fd00e84d59e3_v3_0_0').validate(obj.response)
    return True


def create_security_groups_to_vn_to_vlan(api):
    endpoint_result = api.sgt_vn_vlan.create_security_groups_to_vn_to_vlan(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        sgt_id='string',
        virtualnetworklist=[{'id': 'string', 'name': 'string', 'description': 'string', 'defaultVirtualNetwork': True, 'vlans': [{'id': 'string', 'name': 'string', 'description': 'string', 'defaultVlan': True, 'maxValue': 0, 'data': True}]}]
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_create_security_groups_to_vn_to_vlan(api, validator):
    try:
        assert is_valid_create_security_groups_to_vn_to_vlan(
            validator,
            create_security_groups_to_vn_to_vlan(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_security_groups_to_vn_to_vlan_default(api):
    endpoint_result = api.sgt_vn_vlan.create_security_groups_to_vn_to_vlan(
        active_validation=False,
        description=None,
        id=None,
        name=None,
        payload=None,
        sgt_id=None,
        virtualnetworklist=None
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_create_security_groups_to_vn_to_vlan_default(api, validator):
    try:
        assert is_valid_create_security_groups_to_vn_to_vlan(
            validator,
            create_security_groups_to_vn_to_vlan_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_groups_to_vn_to_vlan_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2112393ea0a65da3ae0346b912a9efac_v3_0_0').validate(obj.response)
    return True


def get_security_groups_to_vn_to_vlan_by_id(api):
    endpoint_result = api.sgt_vn_vlan.get_security_groups_to_vn_to_vlan_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_get_security_groups_to_vn_to_vlan_by_id(api, validator):
    try:
        assert is_valid_get_security_groups_to_vn_to_vlan_by_id(
            validator,
            get_security_groups_to_vn_to_vlan_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_groups_to_vn_to_vlan_by_id_default(api):
    endpoint_result = api.sgt_vn_vlan.get_security_groups_to_vn_to_vlan_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_get_security_groups_to_vn_to_vlan_by_id_default(api, validator):
    try:
        assert is_valid_get_security_groups_to_vn_to_vlan_by_id(
            validator,
            get_security_groups_to_vn_to_vlan_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_security_groups_to_vn_to_vlan_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_eae98db0c24b5ecca77cce8279e20785_v3_0_0').validate(obj.response)
    return True


def update_security_groups_to_vn_to_vlan_by_id(api):
    endpoint_result = api.sgt_vn_vlan.update_security_groups_to_vn_to_vlan_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        sgt_id='string',
        virtualnetworklist=[{'id': 'string', 'name': 'string', 'description': 'string', 'defaultVirtualNetwork': True, 'vlans': [{'id': 'string', 'name': 'string', 'description': 'string', 'defaultVlan': True, 'maxValue': 0, 'data': True}]}]
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_update_security_groups_to_vn_to_vlan_by_id(api, validator):
    try:
        assert is_valid_update_security_groups_to_vn_to_vlan_by_id(
            validator,
            update_security_groups_to_vn_to_vlan_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_security_groups_to_vn_to_vlan_by_id_default(api):
    endpoint_result = api.sgt_vn_vlan.update_security_groups_to_vn_to_vlan_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        payload=None,
        sgt_id=None,
        virtualnetworklist=None
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_update_security_groups_to_vn_to_vlan_by_id_default(api, validator):
    try:
        assert is_valid_update_security_groups_to_vn_to_vlan_by_id(
            validator,
            update_security_groups_to_vn_to_vlan_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_security_groups_to_vn_to_vlan_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9462680497c852dbb953860bef3326e0_v3_0_0').validate(obj.response)
    return True


def delete_security_groups_to_vn_to_vlan_by_id(api):
    endpoint_result = api.sgt_vn_vlan.delete_security_groups_to_vn_to_vlan_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_delete_security_groups_to_vn_to_vlan_by_id(api, validator):
    try:
        assert is_valid_delete_security_groups_to_vn_to_vlan_by_id(
            validator,
            delete_security_groups_to_vn_to_vlan_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_security_groups_to_vn_to_vlan_by_id_default(api):
    endpoint_result = api.sgt_vn_vlan.delete_security_groups_to_vn_to_vlan_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_delete_security_groups_to_vn_to_vlan_by_id_default(api, validator):
    try:
        assert is_valid_delete_security_groups_to_vn_to_vlan_by_id(
            validator,
            delete_security_groups_to_vn_to_vlan_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_security_groups_to_vn_to_vlan(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_86bd1af169fa52c59cbc87b010c36f9e_v3_0_0').validate(obj.response)
    return True


def bulk_request_for_security_groups_to_vn_to_vlan(api):
    endpoint_result = api.sgt_vn_vlan.bulk_request_for_security_groups_to_vn_to_vlan(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_bulk_request_for_security_groups_to_vn_to_vlan(api, validator):
    try:
        assert is_valid_bulk_request_for_security_groups_to_vn_to_vlan(
            validator,
            bulk_request_for_security_groups_to_vn_to_vlan(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_request_for_security_groups_to_vn_to_vlan_default(api):
    endpoint_result = api.sgt_vn_vlan.bulk_request_for_security_groups_to_vn_to_vlan(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_bulk_request_for_security_groups_to_vn_to_vlan_default(api, validator):
    try:
        assert is_valid_bulk_request_for_security_groups_to_vn_to_vlan(
            validator,
            bulk_request_for_security_groups_to_vn_to_vlan_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_security_groups_to_vn_to_vlan(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_10ea793a0b1b5ac498f7bc74a0aba257_v3_0_0').validate(obj.response)
    return True


def monitor_bulk_status_security_groups_to_vn_to_vlan(api):
    endpoint_result = api.sgt_vn_vlan.monitor_bulk_status_security_groups_to_vn_to_vlan(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_monitor_bulk_status_security_groups_to_vn_to_vlan(api, validator):
    try:
        assert is_valid_monitor_bulk_status_security_groups_to_vn_to_vlan(
            validator,
            monitor_bulk_status_security_groups_to_vn_to_vlan(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def monitor_bulk_status_security_groups_to_vn_to_vlan_default(api):
    endpoint_result = api.sgt_vn_vlan.monitor_bulk_status_security_groups_to_vn_to_vlan(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.sgt_vn_vlan
def test_monitor_bulk_status_security_groups_to_vn_to_vlan_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_security_groups_to_vn_to_vlan(
            validator,
            monitor_bulk_status_security_groups_to_vn_to_vlan_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
