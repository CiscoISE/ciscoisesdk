# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_policy_set API fixtures and tests.

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


def is_valid_get_network_access_policy_set_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_229b904117c35daf8833398c262c403d_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_set_list(api):
    endpoint_result = api.network_access_policy_set.get_network_access_policy_set_list(

    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_get_network_access_policy_set_list(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_list(
            validator,
            get_network_access_policy_set_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_set_list_default(api):
    endpoint_result = api.network_access_policy_set.get_network_access_policy_set_list(

    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_get_network_access_policy_set_list_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_list(
            validator,
            get_network_access_policy_set_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_policy_set(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_42e1af4e392c5790a01685b9687208c0_v3_0_0').validate(obj.response)
    return True


def create_network_access_policy_set(api):
    endpoint_result = api.network_access_policy_set.create_network_access_policy_set(
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


@pytest.mark.network_access_policy_set
def test_create_network_access_policy_set(api, validator):
    try:
        assert is_valid_create_network_access_policy_set(
            validator,
            create_network_access_policy_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_access_policy_set_default(api):
    endpoint_result = api.network_access_policy_set.create_network_access_policy_set(
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


@pytest.mark.network_access_policy_set
def test_create_network_access_policy_set_default(api, validator):
    try:
        assert is_valid_create_network_access_policy_set(
            validator,
            create_network_access_policy_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_network_access_policy_sets(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_678aef73e11e56edb468869d663b5e85_v3_0_0').validate(obj.response)
    return True


def reset_hit_counts_network_access_policy_sets(api):
    endpoint_result = api.network_access_policy_set.reset_hit_counts_network_access_policy_sets(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_reset_hit_counts_network_access_policy_sets(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_policy_sets(
            validator,
            reset_hit_counts_network_access_policy_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reset_hit_counts_network_access_policy_sets_default(api):
    endpoint_result = api.network_access_policy_set.reset_hit_counts_network_access_policy_sets(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_reset_hit_counts_network_access_policy_sets_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_policy_sets(
            validator,
            reset_hit_counts_network_access_policy_sets_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_policy_set_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1fb3b6363bad54678ae56dc699e8c7e8_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_set_by_id(api):
    endpoint_result = api.network_access_policy_set.get_network_access_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_get_network_access_policy_set_by_id(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_by_id(
            validator,
            get_network_access_policy_set_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_set_by_id_default(api):
    endpoint_result = api.network_access_policy_set.get_network_access_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_get_network_access_policy_set_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_by_id(
            validator,
            get_network_access_policy_set_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_policy_set_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4068064fa27e5a779143ed557b417535_v3_0_0').validate(obj.response)
    return True


def update_network_access_policy_set_by_id(api):
    endpoint_result = api.network_access_policy_set.update_network_access_policy_set_by_id(
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


@pytest.mark.network_access_policy_set
def test_update_network_access_policy_set_by_id(api, validator):
    try:
        assert is_valid_update_network_access_policy_set_by_id(
            validator,
            update_network_access_policy_set_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_access_policy_set_by_id_default(api):
    endpoint_result = api.network_access_policy_set.update_network_access_policy_set_by_id(
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


@pytest.mark.network_access_policy_set
def test_update_network_access_policy_set_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_policy_set_by_id(
            validator,
            update_network_access_policy_set_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_policy_set_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c1d0c2c01a5856fa8be5af8e2b07e420_v3_0_0').validate(obj.response)
    return True


def delete_network_access_policy_set_by_id(api):
    endpoint_result = api.network_access_policy_set.delete_network_access_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_delete_network_access_policy_set_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_policy_set_by_id(
            validator,
            delete_network_access_policy_set_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_policy_set_by_id_default(api):
    endpoint_result = api.network_access_policy_set.delete_network_access_policy_set_by_id(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_delete_network_access_policy_set_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_policy_set_by_id(
            validator,
            delete_network_access_policy_set_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
