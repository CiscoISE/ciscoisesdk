# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_authentication_rules API fixtures and tests.

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


def is_valid_get_network_access_policy_by_id_authentication_rule_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7956d836da955609bd9a5243101f3536_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_by_id_authentication_rule_list(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_policy_by_id_authentication_rule_list(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_policy_by_id_authentication_rule_list(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authentication_rule_list(
            validator,
            get_network_access_policy_by_id_authentication_rule_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_by_id_authentication_rule_list_default(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_policy_by_id_authentication_rule_list(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_policy_by_id_authentication_rule_list_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authentication_rule_list(
            validator,
            get_network_access_policy_by_id_authentication_rule_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_policy_by_id_authentication_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c26e318c3c405713a55b4e162be8c890_v3_0_0').validate(obj.response)
    return True


def create_network_access_policy_by_id_authentication_rule(api):
    endpoint_result = api.network_access_authentication_rules.create_network_access_policy_by_id_authentication_rule(
        active_validation=False,
        identity_source_name='string',
        if_auth_fail='string',
        if_process_fail='string',
        if_user_not_found='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_create_network_access_policy_by_id_authentication_rule(api, validator):
    try:
        assert is_valid_create_network_access_policy_by_id_authentication_rule(
            validator,
            create_network_access_policy_by_id_authentication_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_access_policy_by_id_authentication_rule_default(api):
    endpoint_result = api.network_access_authentication_rules.create_network_access_policy_by_id_authentication_rule(
        active_validation=False,
        policy_id='string',
        identity_source_name=None,
        if_auth_fail=None,
        if_process_fail=None,
        if_user_not_found=None,
        link=None,
        payload=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_create_network_access_policy_by_id_authentication_rule_default(api, validator):
    try:
        assert is_valid_create_network_access_policy_by_id_authentication_rule(
            validator,
            create_network_access_policy_by_id_authentication_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_network_access_policy_by_id_authentication_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_362ffc5178ed53749ebcaadd1c2af785_v3_0_0').validate(obj.response)
    return True


def reset_hit_counts_network_access_policy_by_id_authentication_rules(api):
    endpoint_result = api.network_access_authentication_rules.reset_hit_counts_network_access_policy_by_id_authentication_rules(
        active_validation=False,
        payload=None,
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_reset_hit_counts_network_access_policy_by_id_authentication_rules(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_policy_by_id_authentication_rules(
            validator,
            reset_hit_counts_network_access_policy_by_id_authentication_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reset_hit_counts_network_access_policy_by_id_authentication_rules_default(api):
    endpoint_result = api.network_access_authentication_rules.reset_hit_counts_network_access_policy_by_id_authentication_rules(
        active_validation=False,
        policy_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_reset_hit_counts_network_access_policy_by_id_authentication_rules_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_policy_by_id_authentication_rules(
            validator,
            reset_hit_counts_network_access_policy_by_id_authentication_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_policy_by_id_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_db7274c43d695aa7af540ecced06c02c_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_by_id_authentication_rule_by_id(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_policy_by_id_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_policy_by_id_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authentication_rule_by_id(
            validator,
            get_network_access_policy_by_id_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_by_id_authentication_rule_by_id_default(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_policy_by_id_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_policy_by_id_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_by_id_authentication_rule_by_id(
            validator,
            get_network_access_policy_by_id_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_policy_by_id_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b9500d6c2f365927aa3dbe6d7ecbae22_v3_0_0').validate(obj.response)
    return True


def update_network_access_policy_by_id_authentication_rule_by_id(api):
    endpoint_result = api.network_access_authentication_rules.update_network_access_policy_by_id_authentication_rule_by_id(
        active_validation=False,
        id='string',
        identity_source_name='string',
        if_auth_fail='string',
        if_process_fail='string',
        if_user_not_found='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_update_network_access_policy_by_id_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_update_network_access_policy_by_id_authentication_rule_by_id(
            validator,
            update_network_access_policy_by_id_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_access_policy_by_id_authentication_rule_by_id_default(api):
    endpoint_result = api.network_access_authentication_rules.update_network_access_policy_by_id_authentication_rule_by_id(
        active_validation=False,
        id='string',
        policy_id='string',
        identity_source_name=None,
        if_auth_fail=None,
        if_process_fail=None,
        if_user_not_found=None,
        link=None,
        payload=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_update_network_access_policy_by_id_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_policy_by_id_authentication_rule_by_id(
            validator,
            update_network_access_policy_by_id_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_policy_by_id_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4bac6ffe32d85cbeac3b12a2e85b094b_v3_0_0').validate(obj.response)
    return True


def delete_network_access_policy_by_id_authentication_rule_by_id(api):
    endpoint_result = api.network_access_authentication_rules.delete_network_access_policy_by_id_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_delete_network_access_policy_by_id_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_policy_by_id_authentication_rule_by_id(
            validator,
            delete_network_access_policy_by_id_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_policy_by_id_authentication_rule_by_id_default(api):
    endpoint_result = api.network_access_authentication_rules.delete_network_access_policy_by_id_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_delete_network_access_policy_by_id_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_policy_by_id_authentication_rule_by_id(
            validator,
            delete_network_access_policy_by_id_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
