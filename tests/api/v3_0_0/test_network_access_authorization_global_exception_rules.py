# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_authorization_global_exception_rules API fixtures and tests.

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


def is_valid_get_network_access_policy_set_global_exception_rule_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8de9a19a8393543da5814b1dce75abf6_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_set_global_exception_rule_list(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_policy_set_global_exception_rule_list(

    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_policy_set_global_exception_rule_list(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_global_exception_rule_list(
            validator,
            get_network_access_policy_set_global_exception_rule_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_set_global_exception_rule_list_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_policy_set_global_exception_rule_list(

    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_policy_set_global_exception_rule_list_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_global_exception_rule_list(
            validator,
            get_network_access_policy_set_global_exception_rule_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_policy_set_global_exception_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f9df6a3c6cf953319db3b8c36720997d_v3_0_0').validate(obj.response)
    return True


def create_network_access_policy_set_global_exception_rule(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.create_network_access_policy_set_global_exception_rule(
        active_validation=False,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        profile=['string'],
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'},
        security_group='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_create_network_access_policy_set_global_exception_rule(api, validator):
    try:
        assert is_valid_create_network_access_policy_set_global_exception_rule(
            validator,
            create_network_access_policy_set_global_exception_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_access_policy_set_global_exception_rule_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.create_network_access_policy_set_global_exception_rule(
        active_validation=False,
        link=None,
        payload=None,
        profile=None,
        rule=None,
        security_group=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_create_network_access_policy_set_global_exception_rule_default(api, validator):
    try:
        assert is_valid_create_network_access_policy_set_global_exception_rule(
            validator,
            create_network_access_policy_set_global_exception_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_network_access_global_exceptions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_31254fb8a2895e8982180d5f9339f8e4_v3_0_0').validate(obj.response)
    return True


def reset_hit_counts_network_access_global_exceptions(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.reset_hit_counts_network_access_global_exceptions(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_reset_hit_counts_network_access_global_exceptions(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_global_exceptions(
            validator,
            reset_hit_counts_network_access_global_exceptions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reset_hit_counts_network_access_global_exceptions_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.reset_hit_counts_network_access_global_exceptions(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_reset_hit_counts_network_access_global_exceptions_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_global_exceptions(
            validator,
            reset_hit_counts_network_access_global_exceptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_policy_set_global_exception_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_cc29d2730d9b52708b34f59633aacfa0_v3_0_0').validate(obj.response)
    return True


def get_network_access_policy_set_global_exception_rule_by_id(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_policy_set_global_exception_rule_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_policy_set_global_exception_rule_by_id(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_global_exception_rule_by_id(
            validator,
            get_network_access_policy_set_global_exception_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_policy_set_global_exception_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_policy_set_global_exception_rule_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_policy_set_global_exception_rule_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_policy_set_global_exception_rule_by_id(
            validator,
            get_network_access_policy_set_global_exception_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_policy_set_global_exception_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_fccec47b460255028363021e7936d17a_v3_0_0').validate(obj.response)
    return True


def update_network_access_policy_set_global_exception_rule_by_id(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.update_network_access_policy_set_global_exception_rule_by_id(
        active_validation=False,
        id='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        profile=['string'],
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'},
        security_group='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_update_network_access_policy_set_global_exception_rule_by_id(api, validator):
    try:
        assert is_valid_update_network_access_policy_set_global_exception_rule_by_id(
            validator,
            update_network_access_policy_set_global_exception_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_access_policy_set_global_exception_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.update_network_access_policy_set_global_exception_rule_by_id(
        active_validation=False,
        id='string',
        link=None,
        payload=None,
        profile=None,
        rule=None,
        security_group=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_update_network_access_policy_set_global_exception_rule_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_policy_set_global_exception_rule_by_id(
            validator,
            update_network_access_policy_set_global_exception_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_policy_set_global_exception_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e7b62515c4dc5de18f9a8ebf019e76af_v3_0_0').validate(obj.response)
    return True


def delete_network_access_policy_set_global_exception_rule_by_id(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.delete_network_access_policy_set_global_exception_rule_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_delete_network_access_policy_set_global_exception_rule_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_policy_set_global_exception_rule_by_id(
            validator,
            delete_network_access_policy_set_global_exception_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_policy_set_global_exception_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.delete_network_access_policy_set_global_exception_rule_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_delete_network_access_policy_set_global_exception_rule_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_policy_set_global_exception_rule_by_id(
            validator,
            delete_network_access_policy_set_global_exception_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
