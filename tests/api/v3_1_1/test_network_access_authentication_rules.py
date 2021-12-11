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
from ciscoisesdk.exceptions import ciscoisesdkException
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.1', reason='version does not match')


def is_valid_get_network_access_authentication_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_21bc064630335416850573ada235189c_v3_1_1').validate(obj.response)
    return True


def get_network_access_authentication_rules(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_authentication_rules(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_authentication_rules(api, validator):
    try:
        assert is_valid_get_network_access_authentication_rules(
            validator,
            get_network_access_authentication_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_authentication_rules_default(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_authentication_rules(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_authentication_rules_default(api, validator):
    try:
        assert is_valid_get_network_access_authentication_rules(
            validator,
            get_network_access_authentication_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_authentication_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1f1e5c8f6732560bb20989459018402b_v3_1_1').validate(obj.response)
    return True


def create_network_access_authentication_rule(api):
    endpoint_result = api.network_access_authentication_rules.create_network_access_authentication_rule(
        active_validation=False,
        identity_source_name='string',
        if_auth_fail='string',
        if_process_fail='string',
        if_user_not_found='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_create_network_access_authentication_rule(api, validator):
    try:
        assert is_valid_create_network_access_authentication_rule(
            validator,
            create_network_access_authentication_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_network_access_authentication_rule_default(api):
    endpoint_result = api.network_access_authentication_rules.create_network_access_authentication_rule(
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
def test_create_network_access_authentication_rule_default(api, validator):
    try:
        assert is_valid_create_network_access_authentication_rule(
            validator,
            create_network_access_authentication_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_network_access_authentication_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_931ce06ff96456e88f85943ed0572444_v3_1_1').validate(obj.response)
    return True


def reset_hit_counts_network_access_authentication_rules(api):
    endpoint_result = api.network_access_authentication_rules.reset_hit_counts_network_access_authentication_rules(
        active_validation=False,
        payload=None,
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_reset_hit_counts_network_access_authentication_rules(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_authentication_rules(
            validator,
            reset_hit_counts_network_access_authentication_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reset_hit_counts_network_access_authentication_rules_default(api):
    endpoint_result = api.network_access_authentication_rules.reset_hit_counts_network_access_authentication_rules(
        active_validation=False,
        policy_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_reset_hit_counts_network_access_authentication_rules_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_network_access_authentication_rules(
            validator,
            reset_hit_counts_network_access_authentication_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_97a0883ac517516c885241460293f6e4_v3_1_1').validate(obj.response)
    return True


def get_network_access_authentication_rule_by_id(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_get_network_access_authentication_rule_by_id(
            validator,
            get_network_access_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_authentication_rule_by_id_default(api):
    endpoint_result = api.network_access_authentication_rules.get_network_access_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_get_network_access_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_authentication_rule_by_id(
            validator,
            get_network_access_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e09eb5adcc5458a9a97153dcd6893c38_v3_1_1').validate(obj.response)
    return True


def update_network_access_authentication_rule_by_id(api):
    endpoint_result = api.network_access_authentication_rules.update_network_access_authentication_rule_by_id(
        active_validation=False,
        id='string',
        identity_source_name='string',
        if_auth_fail='string',
        if_process_fail='string',
        if_user_not_found='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        policy_id='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_update_network_access_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_update_network_access_authentication_rule_by_id(
            validator,
            update_network_access_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_network_access_authentication_rule_by_id_default(api):
    endpoint_result = api.network_access_authentication_rules.update_network_access_authentication_rule_by_id(
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
def test_update_network_access_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_authentication_rule_by_id(
            validator,
            update_network_access_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_82a0670269755446afd0d15e2d77eb5a_v3_1_1').validate(obj.response)
    return True


def delete_network_access_authentication_rule_by_id(api):
    endpoint_result = api.network_access_authentication_rules.delete_network_access_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_delete_network_access_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_authentication_rule_by_id(
            validator,
            delete_network_access_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_network_access_authentication_rule_by_id_default(api):
    endpoint_result = api.network_access_authentication_rules.delete_network_access_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authentication_rules
def test_delete_network_access_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_authentication_rule_by_id(
            validator,
            delete_network_access_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
