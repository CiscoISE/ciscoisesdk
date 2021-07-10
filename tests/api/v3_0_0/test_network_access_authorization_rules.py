# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_authorization_rules API fixtures and tests.

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


def is_valid_get_network_access_policy_by_id_authorization_rule_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_565fef1c1b1c53eeb784322caec31573_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_by_id_authorization_rule_list(api):
    endpoint_result = api.network_access_authorization_rules.get_network_access_policy_by_id_authorization_rule_list(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_get_network_access_policy_by_id_authorization_rule_list(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authorization_rule_list(
            validator,
            get_network_access_policy_by_id_authorization_rule_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_by_id_authorization_rule_list_default(api):
    endpoint_result = api.network_access_authorization_rules.get_network_access_policy_by_id_authorization_rule_list(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_get_network_access_policy_by_id_authorization_rule_list_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authorization_rule_list(
            validator,
            get_network_access_policy_by_id_authorization_rule_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_policy_by_id_authorization_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b9de636ff2e25f849f468556c53b7b9a_v3_0_0').validate(obj.response)
    return True


def create_network_access_policy_by_id_authorization_rule(api):
    endpoint_result = api.network_access_authorization_rules.create_network_access_policy_by_id_authorization_rule(
        active_validation=False,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        profile=['string'],
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'},
        security_group='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_create_network_access_policy_by_id_authorization_rule(api, validator):
    try:
        assert is_valid_create_network_access_policy_by_id_authorization_rule(
            validator,
            create_network_access_policy_by_id_authorization_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_access_policy_by_id_authorization_rule_default(api):
    endpoint_result = api.network_access_authorization_rules.create_network_access_policy_by_id_authorization_rule(
        active_validation=False,
        policy_id='string',
        link=None,
        payload=None,
        profile=None,
        rule=None,
        security_group=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_create_network_access_policy_by_id_authorization_rule_default(api, validator):
    try:
        assert is_valid_create_network_access_policy_by_id_authorization_rule(
            validator,
            create_network_access_policy_by_id_authorization_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_network_access_policy_by_id_authorization_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e263dfc3d6e5513fa6ae916a22d14e5d_v3_0_0').validate(obj.response)
    return True


def reset_hit_counts_network_access_policy_by_id_authorization_rules(api):
    endpoint_result = api.network_access_authorization_rules.reset_hit_counts_network_access_policy_by_id_authorization_rules(
        active_validation=False,
        payload=None,
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_reset_hit_counts_network_access_policy_by_id_authorization_rules(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_policy_by_id_authorization_rules(
            validator,
            reset_hit_counts_network_access_policy_by_id_authorization_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reset_hit_counts_network_access_policy_by_id_authorization_rules_default(api):
    endpoint_result = api.network_access_authorization_rules.reset_hit_counts_network_access_policy_by_id_authorization_rules(
        active_validation=False,
        policy_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_reset_hit_counts_network_access_policy_by_id_authorization_rules_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_policy_by_id_authorization_rules(
            validator,
            reset_hit_counts_network_access_policy_by_id_authorization_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_policy_by_id_authorization_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b19f79dd969d5444a6ba7b2acbf0f3cf_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_by_id_authorization_rule_by_id(api):
    endpoint_result = api.network_access_authorization_rules.get_network_access_policy_by_id_authorization_rule_by_id(
        policy_id='string',
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_get_network_access_policy_by_id_authorization_rule_by_id(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authorization_rule_by_id(
            validator,
            get_network_access_policy_by_id_authorization_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_by_id_authorization_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_rules.get_network_access_policy_by_id_authorization_rule_by_id(
        policy_id='string',
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_get_network_access_policy_by_id_authorization_rule_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authorization_rule_by_id(
            validator,
            get_network_access_policy_by_id_authorization_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_policy_by_id_authorization_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a8c6432bf3c8523e9876c4ac9d92c8b5_v3_0_0').validate(obj.response)
    return True


def update_network_access_policy_by_id_authorization_rule_by_id(api):
    endpoint_result = api.network_access_authorization_rules.update_network_access_policy_by_id_authorization_rule_by_id(
        active_validation=False,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        profile=['string'],
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'},
        rule_id='string',
        security_group='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_update_network_access_policy_by_id_authorization_rule_by_id(api, validator):
    try:
        assert is_valid_update_network_access_policy_by_id_authorization_rule_by_id(
            validator,
            update_network_access_policy_by_id_authorization_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_access_policy_by_id_authorization_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_rules.update_network_access_policy_by_id_authorization_rule_by_id(
        active_validation=False,
        policy_id='string',
        rule_id='string',
        link=None,
        payload=None,
        profile=None,
        rule=None,
        security_group=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_update_network_access_policy_by_id_authorization_rule_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_policy_by_id_authorization_rule_by_id(
            validator,
            update_network_access_policy_by_id_authorization_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_policy_by_id_authorization_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0f8c47fa229d5f749f7432510709876c_v3_0_0').validate(obj.response)
    return True


def delete_network_access_policy_by_id_authorization_rule_by_id(api):
    endpoint_result = api.network_access_authorization_rules.delete_network_access_policy_by_id_authorization_rule_by_id(
        policy_id='string',
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_delete_network_access_policy_by_id_authorization_rule_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_policy_by_id_authorization_rule_by_id(
            validator,
            delete_network_access_policy_by_id_authorization_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_policy_by_id_authorization_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_rules.delete_network_access_policy_by_id_authorization_rule_by_id(
        policy_id='string',
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_rules
def test_delete_network_access_policy_by_id_authorization_rule_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_policy_by_id_authorization_rule_by_id(
            validator,
            delete_network_access_policy_by_id_authorization_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
