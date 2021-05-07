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


def is_valid_get_network_access_policy_sets(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_ed1ef503c091506aa8e446182e625365_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_sets(api):
    endpoint_result = api.network_access_policy_set.get_network_access_policy_sets(

    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_get_network_access_policy_sets(api, validator):
    try:
        assert is_valid_get_network_access_policy_sets(
            validator,
            get_network_access_policy_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_sets_default(api):
    endpoint_result = api.network_access_policy_set.get_network_access_policy_sets(

    )
    return endpoint_result


@pytest.mark.network_access_policy_set
def test_get_network_access_policy_sets_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_sets(
            validator,
            get_network_access_policy_sets_default(api)
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
    json_schema_validate('jsd_9dfe1db8729d541fb3a17d31d47d1881_v3_0_0').validate(obj.response)
    return True


def create_network_access_policy_set(api):
    endpoint_result = api.network_access_policy_set.create_network_access_policy_set(
        active_validation=False,
        condition={'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}},
        default=True,
        description='string',
        hit_counts=0,
        id='string',
        is_proxy=True,
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


def is_valid_get_network_access_policy_set_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_91b58a72c9ff567896a15555ecc9564f_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_set_by_id(api):
    endpoint_result = api.network_access_policy_set.get_network_access_policy_set_by_id(

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
    json_schema_validate('jsd_d5e00a8e6aa0577ea81e11e796912053_v3_0_0').validate(obj.response)
    return True


def update_network_access_policy_set_by_id(api):
    endpoint_result = api.network_access_policy_set.update_network_access_policy_set_by_id(
        active_validation=False,
        condition={'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}},
        default=True,
        description='string',
        hit_counts=0,
        id='string',
        is_proxy=True,
        name='string',
        payload=None,
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
        condition=None,
        default=None,
        description=None,
        hit_counts=None,
        id=None,
        is_proxy=None,
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
    json_schema_validate('jsd_f5175ff711535ff2b1b85a3a4525e886_v3_0_0').validate(obj.response)
    return True


def delete_network_access_policy_set_by_id(api):
    endpoint_result = api.network_access_policy_set.delete_network_access_policy_set_by_id(

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
