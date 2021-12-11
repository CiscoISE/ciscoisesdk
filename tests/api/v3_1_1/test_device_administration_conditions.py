# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_conditions API fixtures and tests.

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


def is_valid_get_device_admin_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e587c20317715a8c8543cb68579f47ae_v3_1_1').validate(obj.response)
    return True


def get_device_admin_conditions(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions(api, validator):
    try:
        assert is_valid_get_device_admin_conditions(
            validator,
            get_device_admin_conditions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_conditions_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_default(api, validator):
    try:
        assert is_valid_get_device_admin_conditions(
            validator,
            get_device_admin_conditions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_00fb0215d2d35317af508cc690d7fa95_v3_1_1').validate(obj.response)
    return True


def create_device_admin_condition(api):
    endpoint_result = api.device_administration_conditions.create_device_admin_condition(
        active_validation=False,
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}],
        condition_type='string',
        dates_range={'endDate': 'string', 'startDate': 'string'},
        dates_range_exception={'endDate': 'string', 'startDate': 'string'},
        description='string',
        dictionary_name='string',
        dictionary_value='string',
        hours_range={'endTime': 'string', 'startTime': 'string'},
        hours_range_exception={'endTime': 'string', 'startTime': 'string'},
        id='string',
        is_negate=True,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        operator='string',
        payload=None,
        week_days=['string'],
        week_days_exception=['string']
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_create_device_admin_condition(api, validator):
    try:
        assert is_valid_create_device_admin_condition(
            validator,
            create_device_admin_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_device_admin_condition_default(api):
    endpoint_result = api.device_administration_conditions.create_device_admin_condition(
        active_validation=False,
        attribute_name=None,
        attribute_value=None,
        children=None,
        condition_type=None,
        dates_range=None,
        dates_range_exception=None,
        description=None,
        dictionary_name=None,
        dictionary_value=None,
        hours_range=None,
        hours_range_exception=None,
        id=None,
        is_negate=None,
        link=None,
        name=None,
        operator=None,
        payload=None,
        week_days=None,
        week_days_exception=None
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_create_device_admin_condition_default(api, validator):
    try:
        assert is_valid_create_device_admin_condition(
            validator,
            create_device_admin_condition_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_conditions_for_authentication_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_dda48630706d56a485ed551392453ef9_v3_1_1').validate(obj.response)
    return True


def get_device_admin_conditions_for_authentication_rules(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authentication_rules(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authentication_rules(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authentication_rules(
            validator,
            get_device_admin_conditions_for_authentication_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_conditions_for_authentication_rules_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authentication_rules(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authentication_rules_default(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authentication_rules(
            validator,
            get_device_admin_conditions_for_authentication_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_conditions_for_authorization_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_5c3d54132e5b51d492a8dc703046ac43_v3_1_1').validate(obj.response)
    return True


def get_device_admin_conditions_for_authorization_rules(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authorization_rules(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authorization_rules(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authorization_rules(
            validator,
            get_device_admin_conditions_for_authorization_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_conditions_for_authorization_rules_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authorization_rules(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authorization_rules_default(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authorization_rules(
            validator,
            get_device_admin_conditions_for_authorization_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_condition_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c4671f7ef81e50338dc5e20250ea7989_v3_1_1').validate(obj.response)
    return True


def get_device_admin_condition_by_name(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_name(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_name(
            validator,
            get_device_admin_condition_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_condition_by_name_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_name_default(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_name(
            validator,
            get_device_admin_condition_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_condition_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6df1812adf495165bddf7b52a83cbc26_v3_1_1').validate(obj.response)
    return True


def update_device_admin_condition_by_name(api):
    endpoint_result = api.device_administration_conditions.update_device_admin_condition_by_name(
        active_validation=False,
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}],
        condition_type='string',
        dates_range={'endDate': 'string', 'startDate': 'string'},
        dates_range_exception={'endDate': 'string', 'startDate': 'string'},
        description='string',
        dictionary_name='string',
        dictionary_value='string',
        hours_range={'endTime': 'string', 'startTime': 'string'},
        hours_range_exception={'endTime': 'string', 'startTime': 'string'},
        id='string',
        is_negate=True,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        operator='string',
        payload=None,
        week_days=['string'],
        week_days_exception=['string']
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_update_device_admin_condition_by_name(api, validator):
    try:
        assert is_valid_update_device_admin_condition_by_name(
            validator,
            update_device_admin_condition_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_device_admin_condition_by_name_default(api):
    endpoint_result = api.device_administration_conditions.update_device_admin_condition_by_name(
        active_validation=False,
        name='string',
        attribute_name=None,
        attribute_value=None,
        children=None,
        condition_type=None,
        dates_range=None,
        dates_range_exception=None,
        description=None,
        dictionary_name=None,
        dictionary_value=None,
        hours_range=None,
        hours_range_exception=None,
        id=None,
        is_negate=None,
        link=None,
        operator=None,
        payload=None,
        week_days=None,
        week_days_exception=None
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_update_device_admin_condition_by_name_default(api, validator):
    try:
        assert is_valid_update_device_admin_condition_by_name(
            validator,
            update_device_admin_condition_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_condition_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6aede43577a158e8ad4cb8828d4a2439_v3_1_1').validate(obj.response)
    return True


def delete_device_admin_condition_by_name(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_name(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_name(
            validator,
            delete_device_admin_condition_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_device_admin_condition_by_name_default(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_name_default(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_name(
            validator,
            delete_device_admin_condition_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_conditions_for_policy_sets(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8cea876c7655519ebde8eb4946990414_v3_1_1').validate(obj.response)
    return True


def get_device_admin_conditions_for_policy_sets(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_policy_sets(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_policy_sets(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_policy_sets(
            validator,
            get_device_admin_conditions_for_policy_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_conditions_for_policy_sets_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_policy_sets(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_policy_sets_default(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_policy_sets(
            validator,
            get_device_admin_conditions_for_policy_sets_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e58982dd97b955dbaa83b1964abd1e38_v3_1_1').validate(obj.response)
    return True


def get_device_admin_condition_by_id(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_id(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_id(
            validator,
            get_device_admin_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_condition_by_id_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_id(
            validator,
            get_device_admin_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2e79f8beface5ea197839128bfba4b0e_v3_1_1').validate(obj.response)
    return True


def update_device_admin_condition_by_id(api):
    endpoint_result = api.device_administration_conditions.update_device_admin_condition_by_id(
        active_validation=False,
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}],
        condition_type='string',
        dates_range={'endDate': 'string', 'startDate': 'string'},
        dates_range_exception={'endDate': 'string', 'startDate': 'string'},
        description='string',
        dictionary_name='string',
        dictionary_value='string',
        hours_range={'endTime': 'string', 'startTime': 'string'},
        hours_range_exception={'endTime': 'string', 'startTime': 'string'},
        id='string',
        is_negate=True,
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        operator='string',
        payload=None,
        week_days=['string'],
        week_days_exception=['string']
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_update_device_admin_condition_by_id(api, validator):
    try:
        assert is_valid_update_device_admin_condition_by_id(
            validator,
            update_device_admin_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_device_admin_condition_by_id_default(api):
    endpoint_result = api.device_administration_conditions.update_device_admin_condition_by_id(
        active_validation=False,
        id='string',
        attribute_name=None,
        attribute_value=None,
        children=None,
        condition_type=None,
        dates_range=None,
        dates_range_exception=None,
        description=None,
        dictionary_name=None,
        dictionary_value=None,
        hours_range=None,
        hours_range_exception=None,
        is_negate=None,
        link=None,
        name=None,
        operator=None,
        payload=None,
        week_days=None,
        week_days_exception=None
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_update_device_admin_condition_by_id_default(api, validator):
    try:
        assert is_valid_update_device_admin_condition_by_id(
            validator,
            update_device_admin_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e866df55c3785f26930f3bc22e96cde5_v3_1_1').validate(obj.response)
    return True


def delete_device_admin_condition_by_id(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_id(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_id(
            validator,
            delete_device_admin_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_device_admin_condition_by_id_default(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_id(
            validator,
            delete_device_admin_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
