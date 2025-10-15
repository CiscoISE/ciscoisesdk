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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.5.0', reason='version does not match')


def is_valid_get_user_equipments(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_user_equipments(api):
    endpoint_result = api.user_equipment.get_user_equipments(
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


def is_valid_get_user_equipments_generator(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_user_equipments_generator(api):
    endpoint_result = api.user_equipment.get_user_equipments_generator(
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipments_generator(api, validator):
    try:
        assert is_valid_get_user_equipments_generator(
            validator,
            get_user_equipments_generator(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_user_equipments_generator_default(api):
    endpoint_result = api.user_equipment.get_user_equipments_generator(
    )
    return endpoint_result


@pytest.mark.user_equipment
def test_get_user_equipments_generator_default(api, validator):
    try:
        assert is_valid_get_user_equipments_generator(
            validator,
            get_user_equipments_generator_default(api)
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
    return True


def create_user_equipment(api):
    endpoint_result = api.user_equipment.create_user_equipment(
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
    return True


def get_user_equipment_by_id(api):
    endpoint_result = api.user_equipment.get_user_equipment_by_id(
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
    return True


def update_user_equipment(api):
    endpoint_result = api.user_equipment.update_user_equipment(
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
    return True


def delete_user_equipment(api):
    endpoint_result = api.user_equipment.delete_user_equipment(
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
    return True


def get_user_equipments_by_subscriber_id(api):
    endpoint_result = api.user_equipment.get_user_equipments_by_subscriber_id(
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
    return True


def get_user_equipment_by_i_m_e_i(api):
    endpoint_result = api.user_equipment.get_user_equipment_by_i_m_e_i(
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
    return True


def create_user_equipments_from_c_s_v(api):
    endpoint_result = api.user_equipment.create_user_equipments_from_c_s_v(
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
    return True


def bulk_user_equipment_operation(api):
    endpoint_result = api.user_equipment.bulk_user_equipment_operation(
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


