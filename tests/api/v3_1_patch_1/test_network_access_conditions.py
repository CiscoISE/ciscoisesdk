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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1_Patch_1', reason='version does not match')


def is_valid_get_network_access_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6df4fb303a3e5661ba12058f18b225af_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e7bd468ee94f53869e52e84454efd0e6_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_104e34177d675622acd0a532f5b7c41b_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_83852fff985b5159a0aa52bfe9e62ba7_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f3b949de4363575398dc1c9e681630bb_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bea2910401185295a9715d65cb1c07c9_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0ea1c05d19955fd4801e6c996705f3fc_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c0984cde5e925c209ab87472ab905476_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f2b0a67d389a592dba005895594b77cc_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e405a20316825460a1f37a2f161e7ac5_v3_1_patch_1').validate(obj.response)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_99d87a24994c514d955149d33e1a99fb_v3_1_patch_1').validate(obj.response)
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
