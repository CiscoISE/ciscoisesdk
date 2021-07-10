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
    json_schema_validate('jsd_816bf923264c53f98d5c347fa50b9c15_v3_0_0').validate(obj.response)
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


def is_valid_post_device_admin_time_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_98b30f809e275589bd7154b5b4093d3f_v3_0_0').validate(obj.response)
    return True


def post_device_admin_time_condition(api):
    endpoint_result = api.device_administration_time_date_conditions.post_device_admin_time_condition(
        active_validation=False,
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}],
        condition_type='string',
        dates_range={'endDate': 'string', 'startDate': 'string'},
        dates_range_exception={'endDate': 'string', 'startDate': 'string'},
        description='string',
        dictionary_name='string',
        dictionary_value='string',
        hours_range={'endTime': 'string', 'startTime': 'string'},
        hours_range_exception={'endTime': 'string', 'startTime': 'string'},
        id='string',
        is_negate=True,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        operator='string',
        payload=None,
        week_days=['string'],
        week_days_exception=['string']
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_post_device_admin_time_condition(api, validator):
    try:
        assert is_valid_post_device_admin_time_condition(
            validator,
            post_device_admin_time_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def post_device_admin_time_condition_default(api):
    endpoint_result = api.device_administration_time_date_conditions.post_device_admin_time_condition(
        active_validation=False,
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
        link=None,
        name=None,
        operator=None,
        payload=None,
        week_days=None,
        week_days_exception=None
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_post_device_admin_time_condition_default(api, validator):
    try:
        assert is_valid_post_device_admin_time_condition(
            validator,
            post_device_admin_time_condition_default(api)
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
    json_schema_validate('jsd_15ffd94d339a5fea8a4777dccccb926f_v3_0_0').validate(obj.response)
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


def is_valid_put_device_admin_time_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e3241242740252b2814e0b474c314e9b_v3_0_0').validate(obj.response)
    return True


def put_device_admin_time_condition_by_condition_id(api):
    endpoint_result = api.device_administration_time_date_conditions.put_device_admin_time_condition_by_condition_id(
        active_validation=False,
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}],
        condition_id='string',
        condition_type='string',
        dates_range={'endDate': 'string', 'startDate': 'string'},
        dates_range_exception={'endDate': 'string', 'startDate': 'string'},
        description='string',
        dictionary_name='string',
        dictionary_value='string',
        hours_range={'endTime': 'string', 'startTime': 'string'},
        hours_range_exception={'endTime': 'string', 'startTime': 'string'},
        id='string',
        is_negate=True,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        operator='string',
        payload=None,
        week_days=['string'],
        week_days_exception=['string']
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_put_device_admin_time_condition_by_condition_id(api, validator):
    try:
        assert is_valid_put_device_admin_time_condition_by_condition_id(
            validator,
            put_device_admin_time_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_device_admin_time_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_time_date_conditions.put_device_admin_time_condition_by_condition_id(
        active_validation=False,
        condition_id='string',
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
        link=None,
        name=None,
        operator=None,
        payload=None,
        week_days=None,
        week_days_exception=None
    )
    return endpoint_result


@pytest.mark.device_administration_time_date_conditions
def test_put_device_admin_time_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_put_device_admin_time_condition_by_condition_id(
            validator,
            put_device_admin_time_condition_by_condition_id_default(api)
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
    json_schema_validate('jsd_cf9f01129179555aa60c446f0a65c65a_v3_0_0').validate(obj.response)
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
