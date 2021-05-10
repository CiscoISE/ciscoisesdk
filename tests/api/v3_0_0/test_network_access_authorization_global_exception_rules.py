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


def is_valid_get_network_access_global_exception_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_19a11a1ff1ee5387b669bcde99f86fbf_v3_0_0').validate(obj.response)
    return True


def get_network_access_global_exception_rules(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_global_exception_rules(

    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_global_exception_rules(api, validator):
    try:
        assert is_valid_get_network_access_global_exception_rules(
            validator,
            get_network_access_global_exception_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_global_exception_rules_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_global_exception_rules(

    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_global_exception_rules_default(api, validator):
    try:
        assert is_valid_get_network_access_global_exception_rules(
            validator,
            get_network_access_global_exception_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_global_exception_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3c5c9b7ab72b5442ae7026a5dcc0fec3_v3_0_0').validate(obj.response)
    return True


def create_network_access_global_exception_rule(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.create_network_access_global_exception_rule(
        active_validation=False,
        payload=None,
        profile=['string'],
        rule={'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}},
        security_group='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_create_network_access_global_exception_rule(api, validator):
    try:
        assert is_valid_create_network_access_global_exception_rule(
            validator,
            create_network_access_global_exception_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_access_global_exception_rule_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.create_network_access_global_exception_rule(
        active_validation=False,
        payload=None,
        profile=None,
        rule=None,
        security_group=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_create_network_access_global_exception_rule_default(api, validator):
    try:
        assert is_valid_create_network_access_global_exception_rule(
            validator,
            create_network_access_global_exception_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_global_exception_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_ac3aa12d3b5551638c3867aa9584f87b_v3_0_0').validate(obj.response)
    return True


def get_network_access_global_exception_rule_by_id(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_global_exception_rule_by_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_global_exception_rule_by_id(api, validator):
    try:
        assert is_valid_get_network_access_global_exception_rule_by_id(
            validator,
            get_network_access_global_exception_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_global_exception_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.get_network_access_global_exception_rule_by_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_get_network_access_global_exception_rule_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_global_exception_rule_by_id(
            validator,
            get_network_access_global_exception_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_global_exception_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_5d6be8d877485969954d2574f0448247_v3_0_0').validate(obj.response)
    return True


def update_network_access_global_exception_rule_by_id(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.update_network_access_global_exception_rule_by_id(
        active_validation=False,
        payload=None,
        profile=['string'],
        rule={'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}},
        rule_id='string',
        security_group='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_update_network_access_global_exception_rule_by_id(api, validator):
    try:
        assert is_valid_update_network_access_global_exception_rule_by_id(
            validator,
            update_network_access_global_exception_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_access_global_exception_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.update_network_access_global_exception_rule_by_id(
        active_validation=False,
        rule_id='string',
        payload=None,
        profile=None,
        rule=None,
        security_group=None
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_update_network_access_global_exception_rule_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_global_exception_rule_by_id(
            validator,
            update_network_access_global_exception_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_global_exception_rule_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6e43a67028515bf193c102cd077ea764_v3_0_0').validate(obj.response)
    return True


def delete_network_access_global_exception_rule_by_id(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.delete_network_access_global_exception_rule_by_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_delete_network_access_global_exception_rule_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_global_exception_rule_by_id(
            validator,
            delete_network_access_global_exception_rule_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_global_exception_rule_by_id_default(api):
    endpoint_result = api.network_access_authorization_global_exception_rules.delete_network_access_global_exception_rule_by_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_authorization_global_exception_rules
def test_delete_network_access_global_exception_rule_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_global_exception_rule_by_id(
            validator,
            delete_network_access_global_exception_rule_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
