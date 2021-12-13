# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI vn_vlan_mapping API fixtures and tests.

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


def is_valid_get_vn_vlan_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d2274589b635566d9762368adf0e841a_v3_1_1').validate(obj.response)
    return True


def get_vn_vlan_mappings(api):
    endpoint_result = api.vn_vlan_mapping.get_vn_vlan_mappings(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_get_vn_vlan_mappings(api, validator):
    try:
        assert is_valid_get_vn_vlan_mappings(
            validator,
            get_vn_vlan_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_vn_vlan_mappings_default(api):
    endpoint_result = api.vn_vlan_mapping.get_vn_vlan_mappings(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_get_vn_vlan_mappings_default(api, validator):
    try:
        assert is_valid_get_vn_vlan_mappings(
            validator,
            get_vn_vlan_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_vn_vlan_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6b06fcd396bc5494be66e198df78e1b2_v3_1_1').validate(obj.response)
    return True


def create_vn_vlan_mapping(api):
    endpoint_result = api.vn_vlan_mapping.create_vn_vlan_mapping(
        active_validation=False,
        id='string',
        is_data=True,
        is_default_vlan=True,
        last_update='string',
        max_value=0,
        name='string',
        payload=None,
        vn_id='string',
        vn_name='string'
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_create_vn_vlan_mapping(api, validator):
    try:
        assert is_valid_create_vn_vlan_mapping(
            validator,
            create_vn_vlan_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_vn_vlan_mapping_default(api):
    endpoint_result = api.vn_vlan_mapping.create_vn_vlan_mapping(
        active_validation=False,
        id=None,
        is_data=None,
        is_default_vlan=None,
        last_update=None,
        max_value=None,
        name=None,
        payload=None,
        vn_id=None,
        vn_name=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_create_vn_vlan_mapping_default(api, validator):
    try:
        assert is_valid_create_vn_vlan_mapping(
            validator,
            create_vn_vlan_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_create_vn_vlan_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_539fd28158d85d37ab1a1d616c56448c_v3_1_1').validate(obj.response)
    return True


def bulk_create_vn_vlan_mappings(api):
    endpoint_result = api.vn_vlan_mapping.bulk_create_vn_vlan_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_bulk_create_vn_vlan_mappings(api, validator):
    try:
        assert is_valid_bulk_create_vn_vlan_mappings(
            validator,
            bulk_create_vn_vlan_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_create_vn_vlan_mappings_default(api):
    endpoint_result = api.vn_vlan_mapping.bulk_create_vn_vlan_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_bulk_create_vn_vlan_mappings_default(api, validator):
    try:
        assert is_valid_bulk_create_vn_vlan_mappings(
            validator,
            bulk_create_vn_vlan_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_delete_vn_vlan_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_67dcb60f20b95a999fa1f4918ad1a9e3_v3_1_1').validate(obj.response)
    return True


def bulk_delete_vn_vlan_mappings(api):
    endpoint_result = api.vn_vlan_mapping.bulk_delete_vn_vlan_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_bulk_delete_vn_vlan_mappings(api, validator):
    try:
        assert is_valid_bulk_delete_vn_vlan_mappings(
            validator,
            bulk_delete_vn_vlan_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_delete_vn_vlan_mappings_default(api):
    endpoint_result = api.vn_vlan_mapping.bulk_delete_vn_vlan_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_bulk_delete_vn_vlan_mappings_default(api, validator):
    try:
        assert is_valid_bulk_delete_vn_vlan_mappings(
            validator,
            bulk_delete_vn_vlan_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_update_vn_vlan_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bc2c834bbed356fcafd18fd78d900c0b_v3_1_1').validate(obj.response)
    return True


def bulk_update_vn_vlan_mappings(api):
    endpoint_result = api.vn_vlan_mapping.bulk_update_vn_vlan_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_bulk_update_vn_vlan_mappings(api, validator):
    try:
        assert is_valid_bulk_update_vn_vlan_mappings(
            validator,
            bulk_update_vn_vlan_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_update_vn_vlan_mappings_default(api):
    endpoint_result = api.vn_vlan_mapping.bulk_update_vn_vlan_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_bulk_update_vn_vlan_mappings_default(api, validator):
    try:
        assert is_valid_bulk_update_vn_vlan_mappings(
            validator,
            bulk_update_vn_vlan_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_vn_vlan_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bad1af5249925176a0694e6e9f170ffb_v3_1_1').validate(obj.response)
    return True


def get_vn_vlan_mapping_by_id(api):
    endpoint_result = api.vn_vlan_mapping.get_vn_vlan_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_get_vn_vlan_mapping_by_id(api, validator):
    try:
        assert is_valid_get_vn_vlan_mapping_by_id(
            validator,
            get_vn_vlan_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_vn_vlan_mapping_by_id_default(api):
    endpoint_result = api.vn_vlan_mapping.get_vn_vlan_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_get_vn_vlan_mapping_by_id_default(api, validator):
    try:
        assert is_valid_get_vn_vlan_mapping_by_id(
            validator,
            get_vn_vlan_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_vn_vlan_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c3d67df26a4d58f5a5efc6083ba187eb_v3_1_1').validate(obj.response)
    return True


def update_vn_vlan_mapping_by_id(api):
    endpoint_result = api.vn_vlan_mapping.update_vn_vlan_mapping_by_id(
        active_validation=False,
        id='string',
        is_data=True,
        is_default_vlan=True,
        last_update='string',
        max_value=0,
        name='string',
        payload=None,
        vn_id='string',
        vn_name='string'
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_update_vn_vlan_mapping_by_id(api, validator):
    try:
        assert is_valid_update_vn_vlan_mapping_by_id(
            validator,
            update_vn_vlan_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_vn_vlan_mapping_by_id_default(api):
    endpoint_result = api.vn_vlan_mapping.update_vn_vlan_mapping_by_id(
        active_validation=False,
        id='string',
        is_data=None,
        is_default_vlan=None,
        last_update=None,
        max_value=None,
        name=None,
        payload=None,
        vn_id=None,
        vn_name=None
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_update_vn_vlan_mapping_by_id_default(api, validator):
    try:
        assert is_valid_update_vn_vlan_mapping_by_id(
            validator,
            update_vn_vlan_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_vn_vlan_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_97fae20bb0ed56cd9a07518b06fdf67f_v3_1_1').validate(obj.response)
    return True


def delete_vn_vlan_mapping_by_id(api):
    endpoint_result = api.vn_vlan_mapping.delete_vn_vlan_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_delete_vn_vlan_mapping_by_id(api, validator):
    try:
        assert is_valid_delete_vn_vlan_mapping_by_id(
            validator,
            delete_vn_vlan_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_vn_vlan_mapping_by_id_default(api):
    endpoint_result = api.vn_vlan_mapping.delete_vn_vlan_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.vn_vlan_mapping
def test_delete_vn_vlan_mapping_by_id_default(api, validator):
    try:
        assert is_valid_delete_vn_vlan_mapping_by_id(
            validator,
            delete_vn_vlan_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
