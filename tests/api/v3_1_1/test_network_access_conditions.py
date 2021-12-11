# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_conditions API fixtures and tests.

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


def is_valid_get_network_access_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8c513fa483ee5144bbea860bf9e449d6_v3_1_1').validate(obj.response)
    return True


def get_network_access_conditions(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions(api, validator):
    try:
        assert is_valid_get_network_access_conditions(
            validator,
            get_network_access_conditions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_conditions_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_default(api, validator):
    try:
        assert is_valid_get_network_access_conditions(
            validator,
            get_network_access_conditions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_ec901d2e3f635112bfbc494932ec29aa_v3_1_1').validate(obj.response)
    return True


def create_network_access_condition(api):
    endpoint_result = api.network_access_conditions.create_network_access_condition(
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


@pytest.mark.network_access_conditions
def test_create_network_access_condition(api, validator):
    try:
        assert is_valid_create_network_access_condition(
            validator,
            create_network_access_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_network_access_condition_default(api):
    endpoint_result = api.network_access_conditions.create_network_access_condition(
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


@pytest.mark.network_access_conditions
def test_create_network_access_condition_default(api, validator):
    try:
        assert is_valid_create_network_access_condition(
            validator,
            create_network_access_condition_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_conditions_for_authentication_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f70bb7d0d53a51f4b95d62d76768bc78_v3_1_1').validate(obj.response)
    return True


def get_network_access_conditions_for_authentication_rules(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authentication_rules(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authentication_rules(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authentication_rules(
            validator,
            get_network_access_conditions_for_authentication_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_conditions_for_authentication_rules_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authentication_rules(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authentication_rules_default(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authentication_rules(
            validator,
            get_network_access_conditions_for_authentication_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_conditions_for_authorization_rules(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c9ecd05ddcd054e1b26d5efbd668527d_v3_1_1').validate(obj.response)
    return True


def get_network_access_conditions_for_authorization_rules(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authorization_rules(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authorization_rules(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authorization_rules(
            validator,
            get_network_access_conditions_for_authorization_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_conditions_for_authorization_rules_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authorization_rules(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authorization_rules_default(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authorization_rules(
            validator,
            get_network_access_conditions_for_authorization_rules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_condition_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_385f96e2cbe85ebe9c534ced3ef81f49_v3_1_1').validate(obj.response)
    return True


def get_network_access_condition_by_name(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_name(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_name(
            validator,
            get_network_access_condition_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_condition_by_name_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_name_default(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_name(
            validator,
            get_network_access_condition_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_condition_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_54085117007c5a2b8fc09b7eb812b06f_v3_1_1').validate(obj.response)
    return True


def update_network_access_condition_by_name(api):
    endpoint_result = api.network_access_conditions.update_network_access_condition_by_name(
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


@pytest.mark.network_access_conditions
def test_update_network_access_condition_by_name(api, validator):
    try:
        assert is_valid_update_network_access_condition_by_name(
            validator,
            update_network_access_condition_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_network_access_condition_by_name_default(api):
    endpoint_result = api.network_access_conditions.update_network_access_condition_by_name(
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


@pytest.mark.network_access_conditions
def test_update_network_access_condition_by_name_default(api, validator):
    try:
        assert is_valid_update_network_access_condition_by_name(
            validator,
            update_network_access_condition_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_condition_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_55795416735e5581a04692b267521132_v3_1_1').validate(obj.response)
    return True


def delete_network_access_condition_by_name(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_name(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_name(
            validator,
            delete_network_access_condition_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_network_access_condition_by_name_default(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_name_default(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_name(
            validator,
            delete_network_access_condition_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_conditions_for_policy_sets(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_308fe01bf5cb5f1a9d0ce514cbb90521_v3_1_1').validate(obj.response)
    return True


def get_network_access_conditions_for_policy_sets(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_policy_sets(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_policy_sets(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_policy_sets(
            validator,
            get_network_access_conditions_for_policy_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_conditions_for_policy_sets_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_policy_sets(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_policy_sets_default(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_policy_sets(
            validator,
            get_network_access_conditions_for_policy_sets_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_11df324efb035cd5997bc0a6326438a0_v3_1_1').validate(obj.response)
    return True


def get_network_access_condition_by_id(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_id(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_id(
            validator,
            get_network_access_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_condition_by_id_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_id(
            validator,
            get_network_access_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d4249c8c63015955bd934d594049cfd3_v3_1_1').validate(obj.response)
    return True


def update_network_access_condition_by_id(api):
    endpoint_result = api.network_access_conditions.update_network_access_condition_by_id(
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


@pytest.mark.network_access_conditions
def test_update_network_access_condition_by_id(api, validator):
    try:
        assert is_valid_update_network_access_condition_by_id(
            validator,
            update_network_access_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_network_access_condition_by_id_default(api):
    endpoint_result = api.network_access_conditions.update_network_access_condition_by_id(
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


@pytest.mark.network_access_conditions
def test_update_network_access_condition_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_condition_by_id(
            validator,
            update_network_access_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_98a7e97c382f5ece8efd82e7e86f8b7b_v3_1_1').validate(obj.response)
    return True


def delete_network_access_condition_by_id(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_id(
            validator,
            delete_network_access_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_network_access_condition_by_id_default(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_id(
            validator,
            delete_network_access_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
