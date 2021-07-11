# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_authorization_rules API fixtures and tests.

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


def is_valid_get_device_admin_policy_by_id_authorization_rule_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4e4ac2543c3b53b5982168169f0b29b4_v3_0_0').validate(obj.response)
    return True


def get_device_admin_policy_by_id_authorization_rule_list(api):
    endpoint_result = api.device_administration_authorization_rules.get_device_admin_policy_by_id_authorization_rule_list(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_get_device_admin_policy_by_id_authorization_rule_list(api, validator):
    try:
        assert is_valid_get_device_admin_policy_by_id_authorization_rule_list(
            validator,
            get_device_admin_policy_by_id_authorization_rule_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_policy_by_id_authorization_rule_list_default(api):
    endpoint_result = api.device_administration_authorization_rules.get_device_admin_policy_by_id_authorization_rule_list(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_get_device_admin_policy_by_id_authorization_rule_list_default(api, validator):
    try:
        assert is_valid_get_device_admin_policy_by_id_authorization_rule_list(
            validator,
            get_device_admin_policy_by_id_authorization_rule_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_policy_by_id_authorization_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8440a5fd2b5d5306b9941387f400c7a0_v3_0_0').validate(obj.response)
    return True


def create_device_admin_policy_by_id_authorization_rule(api):
    endpoint_result = api.device_administration_authorization_rules.create_device_admin_policy_by_id_authorization_rule(
        active_validation=False,
        commands=['string'],
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        profile='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_create_device_admin_policy_by_id_authorization_rule(api, validator):
    try:
        assert is_valid_create_device_admin_policy_by_id_authorization_rule(
            validator,
            create_device_admin_policy_by_id_authorization_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_admin_policy_by_id_authorization_rule_default(api):
    endpoint_result = api.device_administration_authorization_rules.create_device_admin_policy_by_id_authorization_rule(
        active_validation=False,
        policy_id='string',
        commands=None,
        link=None,
        payload=None,
        profile=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_create_device_admin_policy_by_id_authorization_rule_default(api, validator):
    try:
        assert is_valid_create_device_admin_policy_by_id_authorization_rule(
            validator,
            create_device_admin_policy_by_id_authorization_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_device_admin_policy_by_id_authorization_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_38edb17577d9503ba1155c2916dcf663_v3_0_0').validate(obj.response)
    return True


def reset_hit_counts_device_admin_policy_by_id_authorization_rules(api):
    endpoint_result = api.device_administration_authorization_rules.reset_hit_counts_device_admin_policy_by_id_authorization_rules(
        active_validation=False,
        payload=None,
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_reset_hit_counts_device_admin_policy_by_id_authorization_rules(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_policy_by_id_authorization_rules(
            validator,
            reset_hit_counts_device_admin_policy_by_id_authorization_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reset_hit_counts_device_admin_policy_by_id_authorization_rules_default(api):
    endpoint_result = api.device_administration_authorization_rules.reset_hit_counts_device_admin_policy_by_id_authorization_rules(
        active_validation=False,
        policy_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_reset_hit_counts_device_admin_policy_by_id_authorization_rules_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_policy_by_id_authorization_rules(
            validator,
            reset_hit_counts_device_admin_policy_by_id_authorization_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_policy_by_id_authorization_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b61dd057422755baa748a72973cbc6f0_v3_0_0').validate(obj.response)
    return True


def get_device_admin_policy_by_id_authorization_rule_by_id(api):
    endpoint_result = api.device_administration_authorization_rules.get_device_admin_policy_by_id_authorization_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_get_device_admin_policy_by_id_authorization_rule_by_id(api, validator):
    try:
        assert is_valid_get_device_admin_policy_by_id_authorization_rule_by_id(
            validator,
            get_device_admin_policy_by_id_authorization_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_policy_by_id_authorization_rule_by_id_default(api):
    endpoint_result = api.device_administration_authorization_rules.get_device_admin_policy_by_id_authorization_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_get_device_admin_policy_by_id_authorization_rule_by_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_policy_by_id_authorization_rule_by_id(
            validator,
            get_device_admin_policy_by_id_authorization_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_policy_by_id_authorization_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b5151e49a2b65befb488985ed973fed2_v3_0_0').validate(obj.response)
    return True


def update_device_admin_policy_by_id_authorization_rule_by_id(api):
    endpoint_result = api.device_administration_authorization_rules.update_device_admin_policy_by_id_authorization_rule_by_id(
        active_validation=False,
        commands=['string'],
        id='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        profile='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_update_device_admin_policy_by_id_authorization_rule_by_id(api, validator):
    try:
        assert is_valid_update_device_admin_policy_by_id_authorization_rule_by_id(
            validator,
            update_device_admin_policy_by_id_authorization_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_admin_policy_by_id_authorization_rule_by_id_default(api):
    endpoint_result = api.device_administration_authorization_rules.update_device_admin_policy_by_id_authorization_rule_by_id(
        active_validation=False,
        id='string',
        policy_id='string',
        commands=None,
        link=None,
        payload=None,
        profile=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_update_device_admin_policy_by_id_authorization_rule_by_id_default(api, validator):
    try:
        assert is_valid_update_device_admin_policy_by_id_authorization_rule_by_id(
            validator,
            update_device_admin_policy_by_id_authorization_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_policy_by_id_authorization_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7ae9522fa1505322b5da072346d58e92_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_policy_by_id_authorization_rule_by_id(api):
    endpoint_result = api.device_administration_authorization_rules.delete_device_admin_policy_by_id_authorization_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_delete_device_admin_policy_by_id_authorization_rule_by_id(api, validator):
    try:
        assert is_valid_delete_device_admin_policy_by_id_authorization_rule_by_id(
            validator,
            delete_device_admin_policy_by_id_authorization_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_policy_by_id_authorization_rule_by_id_default(api):
    endpoint_result = api.device_administration_authorization_rules.delete_device_admin_policy_by_id_authorization_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_rules
def test_delete_device_admin_policy_by_id_authorization_rule_by_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_policy_by_id_authorization_rule_by_id(
            validator,
            delete_device_admin_policy_by_id_authorization_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
