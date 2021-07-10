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
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_network_access_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_daaac00241cc57a1a360043cbce63df6_v3_0_0').validate(obj.response)
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
            print(original_e)
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


def is_valid_post_network_access_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_36e5dd2909045a90bdce4848865662c2_v3_0_0').validate(obj.response)
    return True


def post_network_access_condition(api):
    endpoint_result = api.network_access_conditions.post_network_access_condition(
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
def test_post_network_access_condition(api, validator):
    try:
        assert is_valid_post_network_access_condition(
            validator,
            post_network_access_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def post_network_access_condition_default(api):
    endpoint_result = api.network_access_conditions.post_network_access_condition(
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
def test_post_network_access_condition_default(api, validator):
    try:
        assert is_valid_post_network_access_condition(
            validator,
            post_network_access_condition_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_conditions_for_authentication_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3a155387e56e5f9ba511dc4e4c9f46b4_v3_0_0').validate(obj.response)
    return True


def get_network_access_conditions_for_authentication_rule(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authentication_rule(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authentication_rule(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authentication_rule(
            validator,
            get_network_access_conditions_for_authentication_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_conditions_for_authentication_rule_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authentication_rule(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authentication_rule_default(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authentication_rule(
            validator,
            get_network_access_conditions_for_authentication_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_conditions_for_authorization_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3e196799ee895b3981634d93ec48f58c_v3_0_0').validate(obj.response)
    return True


def get_network_access_conditions_for_authorization_rule(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authorization_rule(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authorization_rule(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authorization_rule(
            validator,
            get_network_access_conditions_for_authorization_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_conditions_for_authorization_rule_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_authorization_rule(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_authorization_rule_default(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_authorization_rule(
            validator,
            get_network_access_conditions_for_authorization_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_condition_by_condition_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9c98c10af4da50d99fb62c7097f07736_v3_0_0').validate(obj.response)
    return True


def get_network_access_condition_by_condition_name(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_condition_name(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_condition_name(
            validator,
            get_network_access_condition_by_condition_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_condition_by_condition_name_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_condition_name_default(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_condition_name(
            validator,
            get_network_access_condition_by_condition_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_put_network_access_condition_by_condition_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bbc720f738bf5b83a20de7e28e3c4c5f_v3_0_0').validate(obj.response)
    return True


def put_network_access_condition_by_condition_name(api):
    endpoint_result = api.network_access_conditions.put_network_access_condition_by_condition_name(
        active_validation=False,
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}],
        condition_name='string',
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
def test_put_network_access_condition_by_condition_name(api, validator):
    try:
        assert is_valid_put_network_access_condition_by_condition_name(
            validator,
            put_network_access_condition_by_condition_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_network_access_condition_by_condition_name_default(api):
    endpoint_result = api.network_access_conditions.put_network_access_condition_by_condition_name(
        active_validation=False,
        condition_name='string',
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
def test_put_network_access_condition_by_condition_name_default(api, validator):
    try:
        assert is_valid_put_network_access_condition_by_condition_name(
            validator,
            put_network_access_condition_by_condition_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_condition_by_condition_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1ccbc1ec86665500b4520ba48304eab7_v3_0_0').validate(obj.response)
    return True


def delete_network_access_condition_by_condition_name(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_condition_name(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_condition_name(
            validator,
            delete_network_access_condition_by_condition_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_condition_by_condition_name_default(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_condition_name_default(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_condition_name(
            validator,
            delete_network_access_condition_by_condition_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_conditions_for_policy_set(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_902bf0cf46ba5b60b00176d2897fc7d3_v3_0_0').validate(obj.response)
    return True


def get_network_access_conditions_for_policy_set(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_policy_set(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_policy_set(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_policy_set(
            validator,
            get_network_access_conditions_for_policy_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_conditions_for_policy_set_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_conditions_for_policy_set(

    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_conditions_for_policy_set_default(api, validator):
    try:
        assert is_valid_get_network_access_conditions_for_policy_set(
            validator,
            get_network_access_conditions_for_policy_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_150027701d3053acae2eb596718a9ca3_v3_0_0').validate(obj.response)
    return True


def get_network_access_condition_by_condition_id(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_condition_id(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_condition_id(
            validator,
            get_network_access_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_condition_by_condition_id_default(api):
    endpoint_result = api.network_access_conditions.get_network_access_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_get_network_access_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_get_network_access_condition_by_condition_id(
            validator,
            get_network_access_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_put_network_access_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1f0d3cb73c4e59208d9ee04ffa787b3c_v3_0_0').validate(obj.response)
    return True


def put_network_access_condition_by_condition_id(api):
    endpoint_result = api.network_access_conditions.put_network_access_condition_by_condition_id(
        active_validation=False,
        attribute_name='string',
        attribute_value='string',
        children=[{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}],
        condition_id='string',
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
def test_put_network_access_condition_by_condition_id(api, validator):
    try:
        assert is_valid_put_network_access_condition_by_condition_id(
            validator,
            put_network_access_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_network_access_condition_by_condition_id_default(api):
    endpoint_result = api.network_access_conditions.put_network_access_condition_by_condition_id(
        active_validation=False,
        condition_id='string',
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
def test_put_network_access_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_put_network_access_condition_by_condition_id(
            validator,
            put_network_access_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_010c97b4161c5b95a6a83b6917ce26d6_v3_0_0').validate(obj.response)
    return True


def delete_network_access_condition_by_condition_id(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_condition_id(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_condition_id(
            validator,
            delete_network_access_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_condition_by_condition_id_default(api):
    endpoint_result = api.network_access_conditions.delete_network_access_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.network_access_conditions
def test_delete_network_access_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_condition_by_condition_id(
            validator,
            delete_network_access_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
