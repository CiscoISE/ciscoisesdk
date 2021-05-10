# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_time_date_conditions API fixtures and tests.

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


def is_valid_get_device_admin_time_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f79ab23563d857e58e01a74e37333572_v3_0_0').validate(obj.response)
    return True


def get_device_admin_time_conditions(api):
    endpoint_result = api.device_administration_time_date_conditions.get_device_admin_time_conditions(

    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_get_device_admin_time_conditions(api, validator):
    try:
        assert is_valid_get_device_admin_time_conditions(
            validator,
            get_device_admin_time_conditions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_time_conditions_default(api):
    endpoint_result = api.device_administration_time_date_conditions.get_device_admin_time_conditions(

    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_get_device_admin_time_conditions_default(api, validator):
    try:
        assert is_valid_get_device_admin_time_conditions(
            validator,
            get_device_admin_time_conditions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_time_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_26a4d5b5da6a50bfaaecc180543fd952_v3_0_0').validate(obj.response)
    return True


def create_device_admin_time_condition(api):
    endpoint_result = api.device_administration_time_date_conditions.create_device_admin_time_condition(
        active_validation=False,
        attribute_id='string',
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True}],
        condition_type='string',
        dates_range={'startDate': 'string', 'endDate': 'string'},
        dates_range_exception={'startDate': 'string', 'endDate': 'string'},
        description='string',
        dictionary_name='string',
        dictionary_value='string',
        hours_range={'startTime': 'string', 'endTime': 'string'},
        hours_range_exception={'startTime': 'string', 'endTime': 'string'},
        id='string',
        is_negate=True,
        name='string',
        operator='string',
        payload=None,
        week_days=['string'],
        week_days_exception=['string']
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_create_device_admin_time_condition(api, validator):
    try:
        assert is_valid_create_device_admin_time_condition(
            validator,
            create_device_admin_time_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_admin_time_condition_default(api):
    endpoint_result = api.device_administration_time_date_conditions.create_device_admin_time_condition(
        active_validation=False,
        attribute_id=None,
        attribute_name=None,
        attribute_value=None,
        children=None,
        condition_type=None,
        dates_range=None,
        dates_range_exception=None,
        description=None,
        dictionary_name=None,
        dictionary_value=None,
        hours_range=None,
        hours_range_exception=None,
        id=None,
        is_negate=None,
        name=None,
        operator=None,
        payload=None,
        week_days=None,
        week_days_exception=None
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_create_device_admin_time_condition_default(api, validator):
    try:
        assert is_valid_create_device_admin_time_condition(
            validator,
            create_device_admin_time_condition_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_time_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a4af71bd9e705f1bb1d236b3c16e5f51_v3_0_0').validate(obj.response)
    return True


def get_device_admin_time_condition_by_condition_id(api):
    endpoint_result = api.device_administration_time_date_conditions.get_device_admin_time_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_get_device_admin_time_condition_by_condition_id(api, validator):
    try:
        assert is_valid_get_device_admin_time_condition_by_condition_id(
            validator,
            get_device_admin_time_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_time_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_time_date_conditions.get_device_admin_time_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_get_device_admin_time_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_time_condition_by_condition_id(
            validator,
            get_device_admin_time_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_time_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_38b9e7d29b0356b2b1d5fdb2e1069265_v3_0_0').validate(obj.response)
    return True


def update_device_admin_time_condition_by_condition_id(api):
    endpoint_result = api.device_administration_time_date_conditions.update_device_admin_time_condition_by_condition_id(
        active_validation=False,
        attribute_id='string',
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True}],
        condition_id='string',
        condition_type='string',
        dates_range={'startDate': 'string', 'endDate': 'string'},
        dates_range_exception={'startDate': 'string', 'endDate': 'string'},
        description='string',
        dictionary_name='string',
        dictionary_value='string',
        hours_range={'startTime': 'string', 'endTime': 'string'},
        hours_range_exception={'startTime': 'string', 'endTime': 'string'},
        id='string',
        is_negate=True,
        name='string',
        operator='string',
        payload=None,
        week_days=['string'],
        week_days_exception=['string']
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_update_device_admin_time_condition_by_condition_id(api, validator):
    try:
        assert is_valid_update_device_admin_time_condition_by_condition_id(
            validator,
            update_device_admin_time_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_admin_time_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_time_date_conditions.update_device_admin_time_condition_by_condition_id(
        active_validation=False,
        condition_id='string',
        attribute_id=None,
        attribute_name=None,
        attribute_value=None,
        children=None,
        condition_type=None,
        dates_range=None,
        dates_range_exception=None,
        description=None,
        dictionary_name=None,
        dictionary_value=None,
        hours_range=None,
        hours_range_exception=None,
        id=None,
        is_negate=None,
        name=None,
        operator=None,
        payload=None,
        week_days=None,
        week_days_exception=None
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_update_device_admin_time_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_update_device_admin_time_condition_by_condition_id(
            validator,
            update_device_admin_time_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_time_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9388e4ce332e5cdc97399fe9f01b163e_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_time_condition_by_condition_id(api):
    endpoint_result = api.device_administration_time_date_conditions.delete_device_admin_time_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_delete_device_admin_time_condition_by_condition_id(api, validator):
    try:
        assert is_valid_delete_device_admin_time_condition_by_condition_id(
            validator,
            delete_device_admin_time_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_time_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_time_date_conditions.delete_device_admin_time_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_delete_device_admin_time_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_time_condition_by_condition_id(
            validator,
            delete_device_admin_time_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
