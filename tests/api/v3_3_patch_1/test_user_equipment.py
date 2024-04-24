# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI user_equipment API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.3_patch_1', reason='version does not match')


def is_valid_get_user_equipments(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b5d936170e535fb5a2e6742807081bb5_v3_3_patch_1').validate(obj.response)
    return True


def get_user_equipments(api):
    endpoint_result = api.user_equipment.get_user_equipments(
        filter='string',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipments(api, validator):
    try:
        assert is_valid_get_user_equipments(
            validator,
            get_user_equipments(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_user_equipments_default(api):
    endpoint_result = api.user_equipment.get_user_equipments(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipments_default(api, validator):
    try:
        assert is_valid_get_user_equipments(
            validator,
            get_user_equipments_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_user_equipment(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6a2770b9fac658769ca2c63ca6984b9e_v3_3_patch_1').validate(obj.response)
    return True


def create_user_equipment(api):
    endpoint_result = api.user_equipment.create_user_equipment(
        active_validation=False,
        description='string',
        device_group='string',
        imei='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_create_user_equipment(api, validator):
    try:
        assert is_valid_create_user_equipment(
            validator,
            create_user_equipment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_user_equipment_default(api):
    endpoint_result = api.user_equipment.create_user_equipment(
        active_validation=False,
        description=None,
        device_group=None,
        imei=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_create_user_equipment_default(api, validator):
    try:
        assert is_valid_create_user_equipment(
            validator,
            create_user_equipment_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_user_equipment_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b15aa7a86eb25690b0306e29e0acdc9d_v3_3_patch_1').validate(obj.response)
    return True


def get_user_equipment_by_id(api):
    endpoint_result = api.user_equipment.get_user_equipment_by_id(
        user_equipment_id='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipment_by_id(api, validator):
    try:
        assert is_valid_get_user_equipment_by_id(
            validator,
            get_user_equipment_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_user_equipment_by_id_default(api):
    endpoint_result = api.user_equipment.get_user_equipment_by_id(
        user_equipment_id='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipment_by_id_default(api, validator):
    try:
        assert is_valid_get_user_equipment_by_id(
            validator,
            get_user_equipment_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_user_equipment(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_cf803097098c5553a2f1e5ae0c526da5_v3_3_patch_1').validate(obj.response)
    return True


def update_user_equipment(api):
    endpoint_result = api.user_equipment.update_user_equipment(
        active_validation=False,
        description='string',
        device_group='string',
        payload=None,
        user_equipment_id='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_update_user_equipment(api, validator):
    try:
        assert is_valid_update_user_equipment(
            validator,
            update_user_equipment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_user_equipment_default(api):
    endpoint_result = api.user_equipment.update_user_equipment(
        active_validation=False,
        user_equipment_id='string',
        description=None,
        device_group=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_update_user_equipment_default(api, validator):
    try:
        assert is_valid_update_user_equipment(
            validator,
            update_user_equipment_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_user_equipment(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ebecb7076ea45c289951b77ba6de7508_v3_3_patch_1').validate(obj.response)
    return True


def delete_user_equipment(api):
    endpoint_result = api.user_equipment.delete_user_equipment(
        user_equipment_id='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_delete_user_equipment(api, validator):
    try:
        assert is_valid_delete_user_equipment(
            validator,
            delete_user_equipment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_user_equipment_default(api):
    endpoint_result = api.user_equipment.delete_user_equipment(
        user_equipment_id='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_delete_user_equipment_default(api, validator):
    try:
        assert is_valid_delete_user_equipment(
            validator,
            delete_user_equipment_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_user_equipments_by_subscriber_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d990d821a0885cc2a002144e1fa1a7eb_v3_3_patch_1').validate(obj.response)
    return True


def get_user_equipments_by_subscriber_id(api):
    endpoint_result = api.user_equipment.get_user_equipments_by_subscriber_id(
        subscriber_id='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipments_by_subscriber_id(api, validator):
    try:
        assert is_valid_get_user_equipments_by_subscriber_id(
            validator,
            get_user_equipments_by_subscriber_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_user_equipments_by_subscriber_id_default(api):
    endpoint_result = api.user_equipment.get_user_equipments_by_subscriber_id(
        subscriber_id='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipments_by_subscriber_id_default(api, validator):
    try:
        assert is_valid_get_user_equipments_by_subscriber_id(
            validator,
            get_user_equipments_by_subscriber_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_user_equipment_by_i_m_e_i(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b97cb90bda30562198f19eb20a343d2a_v3_3_patch_1').validate(obj.response)
    return True


def get_user_equipment_by_i_m_e_i(api):
    endpoint_result = api.user_equipment.get_user_equipment_by_i_m_e_i(
        imei='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipment_by_i_m_e_i(api, validator):
    try:
        assert is_valid_get_user_equipment_by_i_m_e_i(
            validator,
            get_user_equipment_by_i_m_e_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_user_equipment_by_i_m_e_i_default(api):
    endpoint_result = api.user_equipment.get_user_equipment_by_i_m_e_i(
        imei='string'
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipment_by_i_m_e_i_default(api, validator):
    try:
        assert is_valid_get_user_equipment_by_i_m_e_i(
            validator,
            get_user_equipment_by_i_m_e_i_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_user_equipments_from_c_s_v(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_06bc5a2ced485ac2a06f77d7cc36ee20_v3_3_patch_1').validate(obj.response)
    return True


def create_user_equipments_from_c_s_v(api):
    endpoint_result = api.user_equipment.create_user_equipments_from_c_s_v(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_create_user_equipments_from_c_s_v(api, validator):
    try:
        assert is_valid_create_user_equipments_from_c_s_v(
            validator,
            create_user_equipments_from_c_s_v(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_user_equipments_from_c_s_v_default(api):
    endpoint_result = api.user_equipment.create_user_equipments_from_c_s_v(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_create_user_equipments_from_c_s_v_default(api, validator):
    try:
        assert is_valid_create_user_equipments_from_c_s_v(
            validator,
            create_user_equipments_from_c_s_v_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_user_equipment_operation(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_79a3bd66e4d75f5f99198a5999e596a8_v3_3_patch_1').validate(obj.response)
    return True


def bulk_user_equipment_operation(api):
    endpoint_result = api.user_equipment.bulk_user_equipment_operation(
        active_validation=False,
        item_list=[{'imei': 'string', 'description': 'string', 'id': 'string', 'deviceGroup': 'string'}],
        operation='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_bulk_user_equipment_operation(api, validator):
    try:
        assert is_valid_bulk_user_equipment_operation(
            validator,
            bulk_user_equipment_operation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_user_equipment_operation_default(api):
    endpoint_result = api.user_equipment.bulk_user_equipment_operation(
        active_validation=False,
        item_list=None,
        operation=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_bulk_user_equipment_operation_default(api, validator):
    try:
        assert is_valid_bulk_user_equipment_operation(
            validator,
            bulk_user_equipment_operation_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
