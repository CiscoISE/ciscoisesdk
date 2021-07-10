# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_policy_set API fixtures and tests.

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


def is_valid_get_device_admin_policy_set_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_923587ed5920513e92b1728b824771cc_v3_0_0').validate(obj.response)
    return True


def get_device_admin_policy_set_list(api):
    endpoint_result = api.device_administration_policy_set.get_device_admin_policy_set_list(

    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_get_device_admin_policy_set_list(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_list(
            validator,
            get_device_admin_policy_set_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_policy_set_list_default(api):
    endpoint_result = api.device_administration_policy_set.get_device_admin_policy_set_list(

    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_get_device_admin_policy_set_list_default(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_list(
            validator,
            get_device_admin_policy_set_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_policy_set(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_5767ac3ccf225801ad8ba0bb1ad9de0b_v3_0_0').validate(obj.response)
    return True


def create_device_admin_policy_set(api):
    endpoint_result = api.device_administration_policy_set.create_device_admin_policy_set(
        active_validation=False,
        condition={'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']},
        default=True,
        description='string',
        hit_counts=0,
        id='string',
        is_proxy=True,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        payload=None,
        rank=0,
        service_name='string',
        state='string'
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_create_device_admin_policy_set(api, validator):
    try:
        assert is_valid_create_device_admin_policy_set(
            validator,
            create_device_admin_policy_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_admin_policy_set_default(api):
    endpoint_result = api.device_administration_policy_set.create_device_admin_policy_set(
        active_validation=False,
        condition=None,
        default=None,
        description=None,
        hit_counts=None,
        id=None,
        is_proxy=None,
        link=None,
        name=None,
        payload=None,
        rank=None,
        service_name=None,
        state=None
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_create_device_admin_policy_set_default(api, validator):
    try:
        assert is_valid_create_device_admin_policy_set(
            validator,
            create_device_admin_policy_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_device_admin_policy_sets(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_ed47964d442d52dca1f7da967f37b3e2_v3_0_0').validate(obj.response)
    return True


def reset_hit_counts_device_admin_policy_sets(api):
    endpoint_result = api.device_administration_policy_set.reset_hit_counts_device_admin_policy_sets(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_reset_hit_counts_device_admin_policy_sets(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_policy_sets(
            validator,
            reset_hit_counts_device_admin_policy_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reset_hit_counts_device_admin_policy_sets_default(api):
    endpoint_result = api.device_administration_policy_set.reset_hit_counts_device_admin_policy_sets(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_reset_hit_counts_device_admin_policy_sets_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_policy_sets(
            validator,
            reset_hit_counts_device_admin_policy_sets_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_policy_set_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_49f36918d98a546ab6ca2618d1844984_v3_0_0').validate(obj.response)
    return True


def get_device_admin_policy_set_by_id(api):
    endpoint_result = api.device_administration_policy_set.get_device_admin_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_get_device_admin_policy_set_by_id(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_by_id(
            validator,
            get_device_admin_policy_set_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_policy_set_by_id_default(api):
    endpoint_result = api.device_administration_policy_set.get_device_admin_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_get_device_admin_policy_set_by_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_by_id(
            validator,
            get_device_admin_policy_set_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_policy_set_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b6cc40e0f4b45e8da5908776d124ed5a_v3_0_0').validate(obj.response)
    return True


def update_device_admin_policy_set_by_id(api):
    endpoint_result = api.device_administration_policy_set.update_device_admin_policy_set_by_id(
        active_validation=False,
        condition={'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']},
        default=True,
        description='string',
        hit_counts=0,
        id='string',
        is_proxy=True,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        payload=None,
        policy_id='string',
        rank=0,
        service_name='string',
        state='string'
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_update_device_admin_policy_set_by_id(api, validator):
    try:
        assert is_valid_update_device_admin_policy_set_by_id(
            validator,
            update_device_admin_policy_set_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_admin_policy_set_by_id_default(api):
    endpoint_result = api.device_administration_policy_set.update_device_admin_policy_set_by_id(
        active_validation=False,
        policy_id='string',
        condition=None,
        default=None,
        description=None,
        hit_counts=None,
        id=None,
        is_proxy=None,
        link=None,
        name=None,
        payload=None,
        rank=None,
        service_name=None,
        state=None
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_update_device_admin_policy_set_by_id_default(api, validator):
    try:
        assert is_valid_update_device_admin_policy_set_by_id(
            validator,
            update_device_admin_policy_set_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_policy_set_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f602e2f88378502a8d8bca6dff274afe_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_policy_set_by_id(api):
    endpoint_result = api.device_administration_policy_set.delete_device_admin_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_delete_device_admin_policy_set_by_id(api, validator):
    try:
        assert is_valid_delete_device_admin_policy_set_by_id(
            validator,
            delete_device_admin_policy_set_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_policy_set_by_id_default(api):
    endpoint_result = api.device_administration_policy_set.delete_device_admin_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_policy_set
def test_delete_device_admin_policy_set_by_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_policy_set_by_id(
            validator,
            delete_device_admin_policy_set_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
