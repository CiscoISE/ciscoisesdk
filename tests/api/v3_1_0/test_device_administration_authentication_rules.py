# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_authentication_rules API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_device_admin_authentication_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_141b9e8541f25c4ea29944f659f68994_v3_1_0').validate(obj.response)
    return True


def get_device_admin_authentication_rules(api):
    endpoint_result = api.device_administration_authentication_rules.get_device_admin_authentication_rules(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_get_device_admin_authentication_rules(api, validator):
    try:
        assert is_valid_get_device_admin_authentication_rules(
            validator,
            get_device_admin_authentication_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_authentication_rules_default(api):
    endpoint_result = api.device_administration_authentication_rules.get_device_admin_authentication_rules(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_get_device_admin_authentication_rules_default(api, validator):
    try:
        assert is_valid_get_device_admin_authentication_rules(
            validator,
            get_device_admin_authentication_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_authentication_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f1ff2b82953f5131884f0779db37190c_v3_1_0').validate(obj.response)
    return True


def create_device_admin_authentication_rule(api):
    endpoint_result = api.device_administration_authentication_rules.create_device_admin_authentication_rule(
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


@pytest.mark.device_administration_authentication_rules
def test_create_device_admin_authentication_rule(api, validator):
    try:
        assert is_valid_create_device_admin_authentication_rule(
            validator,
            create_device_admin_authentication_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_device_admin_authentication_rule_default(api):
    endpoint_result = api.device_administration_authentication_rules.create_device_admin_authentication_rule(
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


@pytest.mark.device_administration_authentication_rules
def test_create_device_admin_authentication_rule_default(api, validator):
    try:
        assert is_valid_create_device_admin_authentication_rule(
            validator,
            create_device_admin_authentication_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_device_admin_authentication_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_dd2d3e1f258252579386f21705613d26_v3_1_0').validate(obj.response)
    return True


def reset_hit_counts_device_admin_authentication_rules(api):
    endpoint_result = api.device_administration_authentication_rules.reset_hit_counts_device_admin_authentication_rules(
        active_validation=False,
        payload=None,
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_reset_hit_counts_device_admin_authentication_rules(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_authentication_rules(
            validator,
            reset_hit_counts_device_admin_authentication_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reset_hit_counts_device_admin_authentication_rules_default(api):
    endpoint_result = api.device_administration_authentication_rules.reset_hit_counts_device_admin_authentication_rules(
        active_validation=False,
        policy_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_reset_hit_counts_device_admin_authentication_rules_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_authentication_rules(
            validator,
            reset_hit_counts_device_admin_authentication_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_97a160f293375ae9924d8240c4efdc6a_v3_1_0').validate(obj.response)
    return True


def get_device_admin_authentication_rule_by_id(api):
    endpoint_result = api.device_administration_authentication_rules.get_device_admin_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_get_device_admin_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_get_device_admin_authentication_rule_by_id(
            validator,
            get_device_admin_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_authentication_rule_by_id_default(api):
    endpoint_result = api.device_administration_authentication_rules.get_device_admin_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_get_device_admin_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_authentication_rule_by_id(
            validator,
            get_device_admin_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1269ca61ff725fedb94fba602d7afe46_v3_1_0').validate(obj.response)
    return True


def update_device_admin_authentication_rule_by_id(api):
    endpoint_result = api.device_administration_authentication_rules.update_device_admin_authentication_rule_by_id(
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


@pytest.mark.device_administration_authentication_rules
def test_update_device_admin_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_update_device_admin_authentication_rule_by_id(
            validator,
            update_device_admin_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_device_admin_authentication_rule_by_id_default(api):
    endpoint_result = api.device_administration_authentication_rules.update_device_admin_authentication_rule_by_id(
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


@pytest.mark.device_administration_authentication_rules
def test_update_device_admin_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_update_device_admin_authentication_rule_by_id(
            validator,
            update_device_admin_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_authentication_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_30085a9f1f24542dbd244e31691a2e09_v3_1_0').validate(obj.response)
    return True


def delete_device_admin_authentication_rule_by_id(api):
    endpoint_result = api.device_administration_authentication_rules.delete_device_admin_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_delete_device_admin_authentication_rule_by_id(api, validator):
    try:
        assert is_valid_delete_device_admin_authentication_rule_by_id(
            validator,
            delete_device_admin_authentication_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_device_admin_authentication_rule_by_id_default(api):
    endpoint_result = api.device_administration_authentication_rules.delete_device_admin_authentication_rule_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authentication_rules
def test_delete_device_admin_authentication_rule_by_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_authentication_rule_by_id(
            validator,
            delete_device_admin_authentication_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
