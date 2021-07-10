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
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_device_admin_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_fdfa9b301f925a34a848f29f223e5b8d_v3_0_0').validate(obj.response)
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
            print(original_e)
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


def is_valid_post_device_admin_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b84dbd77c49f5056b9bf3c1e496ebe5f_v3_0_0').validate(obj.response)
    return True


def post_device_admin_condition(api):
    endpoint_result = api.device_administration_conditions.post_device_admin_condition(
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
def test_post_device_admin_condition(api, validator):
    try:
        assert is_valid_post_device_admin_condition(
            validator,
            post_device_admin_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def post_device_admin_condition_default(api):
    endpoint_result = api.device_administration_conditions.post_device_admin_condition(
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
def test_post_device_admin_condition_default(api, validator):
    try:
        assert is_valid_post_device_admin_condition(
            validator,
            post_device_admin_condition_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_conditions_for_authentication_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_316863dcb2ca563999b2d3691e1def79_v3_0_0').validate(obj.response)
    return True


def get_device_admin_conditions_for_authentication_rule(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authentication_rule(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authentication_rule(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authentication_rule(
            validator,
            get_device_admin_conditions_for_authentication_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_conditions_for_authentication_rule_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authentication_rule(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authentication_rule_default(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authentication_rule(
            validator,
            get_device_admin_conditions_for_authentication_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_conditions_for_authorization_rule(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e67076b912ef5362949be22842642596_v3_0_0').validate(obj.response)
    return True


def get_device_admin_conditions_for_authorization_rule(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authorization_rule(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authorization_rule(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authorization_rule(
            validator,
            get_device_admin_conditions_for_authorization_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_conditions_for_authorization_rule_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_authorization_rule(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_authorization_rule_default(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_authorization_rule(
            validator,
            get_device_admin_conditions_for_authorization_rule_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_condition_by_condition_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3d9fe67eb28858609eca3907c8343015_v3_0_0').validate(obj.response)
    return True


def get_device_admin_condition_by_condition_name(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_condition_name(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_condition_name(
            validator,
            get_device_admin_condition_by_condition_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_condition_by_condition_name_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_condition_name_default(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_condition_name(
            validator,
            get_device_admin_condition_by_condition_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_put_device_admin_condition_by_condition_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f0540adc16725e00adffdf57b67fb6ba_v3_0_0').validate(obj.response)
    return True


def put_device_admin_condition_by_condition_name(api):
    endpoint_result = api.device_administration_conditions.put_device_admin_condition_by_condition_name(
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


@pytest.mark.device_administration_conditions
def test_put_device_admin_condition_by_condition_name(api, validator):
    try:
        assert is_valid_put_device_admin_condition_by_condition_name(
            validator,
            put_device_admin_condition_by_condition_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_device_admin_condition_by_condition_name_default(api):
    endpoint_result = api.device_administration_conditions.put_device_admin_condition_by_condition_name(
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


@pytest.mark.device_administration_conditions
def test_put_device_admin_condition_by_condition_name_default(api, validator):
    try:
        assert is_valid_put_device_admin_condition_by_condition_name(
            validator,
            put_device_admin_condition_by_condition_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_condition_by_condition_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c276cf1dc9545d45ae3f871966cb664b_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_condition_by_condition_name(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_condition_name(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_condition_name(
            validator,
            delete_device_admin_condition_by_condition_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_condition_by_condition_name_default(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_condition_name(
        condition_name='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_condition_name_default(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_condition_name(
            validator,
            delete_device_admin_condition_by_condition_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_conditions_for_policy_set(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_68b404b307a35c2d9438da695bb49c54_v3_0_0').validate(obj.response)
    return True


def get_device_admin_conditions_for_policy_set(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_policy_set(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_policy_set(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_policy_set(
            validator,
            get_device_admin_conditions_for_policy_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_conditions_for_policy_set_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_conditions_for_policy_set(

    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_conditions_for_policy_set_default(api, validator):
    try:
        assert is_valid_get_device_admin_conditions_for_policy_set(
            validator,
            get_device_admin_conditions_for_policy_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_27c0cf6ab73353ffa2b6986a9b16c54e_v3_0_0').validate(obj.response)
    return True


def get_device_admin_condition_by_condition_id(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_condition_id(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_condition_id(
            validator,
            get_device_admin_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_conditions.get_device_admin_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_get_device_admin_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_condition_by_condition_id(
            validator,
            get_device_admin_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_put_device_admin_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3b9b1bfd0f4151eb9812b474e4e4fa3c_v3_0_0').validate(obj.response)
    return True


def put_device_admin_condition_by_condition_id(api):
    endpoint_result = api.device_administration_conditions.put_device_admin_condition_by_condition_id(
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


@pytest.mark.device_administration_conditions
def test_put_device_admin_condition_by_condition_id(api, validator):
    try:
        assert is_valid_put_device_admin_condition_by_condition_id(
            validator,
            put_device_admin_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_device_admin_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_conditions.put_device_admin_condition_by_condition_id(
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


@pytest.mark.device_administration_conditions
def test_put_device_admin_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_put_device_admin_condition_by_condition_id(
            validator,
            put_device_admin_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_condition_by_condition_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2a6c1759c65b51a09ed7981397ece5c6_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_condition_by_condition_id(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_condition_id(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_condition_id(
            validator,
            delete_device_admin_condition_by_condition_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_condition_by_condition_id_default(api):
    endpoint_result = api.device_administration_conditions.delete_device_admin_condition_by_condition_id(
        condition_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_conditions
def test_delete_device_admin_condition_by_condition_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_condition_by_condition_id(
            validator,
            delete_device_admin_condition_by_condition_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
