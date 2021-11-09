# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI radius_server_sequence API fixtures and tests.

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


def is_valid_get_radius_server_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_0d1df0e230765104863b8d63d5beb68e_v3_0_0').validate(obj.response)
    return True


def get_radius_server_sequence_by_id(api):
    endpoint_result = api.radius_server_sequence.get_radius_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_get_radius_server_sequence_by_id(api, validator):
    try:
        assert is_valid_get_radius_server_sequence_by_id(
            validator,
            get_radius_server_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_radius_server_sequence_by_id_default(api):
    endpoint_result = api.radius_server_sequence.get_radius_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_get_radius_server_sequence_by_id_default(api, validator):
    try:
        assert is_valid_get_radius_server_sequence_by_id(
            validator,
            get_radius_server_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_radius_server_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_df9ab8ff636353279d5c787585dcb6af_v3_0_0').validate(obj.response)
    return True


def update_radius_server_sequence_by_id(api):
    endpoint_result = api.radius_server_sequence.update_radius_server_sequence_by_id(
        active_validation=False,
        before_accept_attr_manipulators_list=[{'action': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string', 'changedVal': 'string'}],
        continue_authorz_policy=True,
        description='string',
        id='string',
        local_accounting=True,
        name='string',
        on_request_attr_manipulator_list=[{'action': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string', 'changedVal': 'string'}],
        payload=None,
        prefix_separator='string',
        radius_server_list=['string'],
        remote_accounting=True,
        strip_prefix=True,
        strip_suffix=True,
        suffix_separator='string',
        use_attr_set_before_acc=True,
        use_attr_set_on_request=True
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_update_radius_server_sequence_by_id(api, validator):
    try:
        assert is_valid_update_radius_server_sequence_by_id(
            validator,
            update_radius_server_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_radius_server_sequence_by_id_default(api):
    endpoint_result = api.radius_server_sequence.update_radius_server_sequence_by_id(
        active_validation=False,
        id='string',
        before_accept_attr_manipulators_list=None,
        continue_authorz_policy=None,
        description=None,
        local_accounting=None,
        name=None,
        on_request_attr_manipulator_list=None,
        payload=None,
        prefix_separator=None,
        radius_server_list=None,
        remote_accounting=None,
        strip_prefix=None,
        strip_suffix=None,
        suffix_separator=None,
        use_attr_set_before_acc=None,
        use_attr_set_on_request=None
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_update_radius_server_sequence_by_id_default(api, validator):
    try:
        assert is_valid_update_radius_server_sequence_by_id(
            validator,
            update_radius_server_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_radius_server_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_815b13838fa75d6e8d970f6eeb6a4510_v3_0_0').validate(obj.response)
    return True


def delete_radius_server_sequence_by_id(api):
    endpoint_result = api.radius_server_sequence.delete_radius_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_delete_radius_server_sequence_by_id(api, validator):
    try:
        assert is_valid_delete_radius_server_sequence_by_id(
            validator,
            delete_radius_server_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_radius_server_sequence_by_id_default(api):
    endpoint_result = api.radius_server_sequence.delete_radius_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_delete_radius_server_sequence_by_id_default(api, validator):
    try:
        assert is_valid_delete_radius_server_sequence_by_id(
            validator,
            delete_radius_server_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_radius_server_sequence(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_c6c330dace185a548f70f4e5d67776ea_v3_0_0').validate(obj.response)
    return True


def get_radius_server_sequence(api):
    endpoint_result = api.radius_server_sequence.get_radius_server_sequence(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_get_radius_server_sequence(api, validator):
    try:
        assert is_valid_get_radius_server_sequence(
            validator,
            get_radius_server_sequence(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_radius_server_sequence_default(api):
    endpoint_result = api.radius_server_sequence.get_radius_server_sequence(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_get_radius_server_sequence_default(api, validator):
    try:
        assert is_valid_get_radius_server_sequence(
            validator,
            get_radius_server_sequence_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_radius_server_sequence(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_83ad6ca0642c5750af6ca9905721a9d7_v3_0_0').validate(obj.response)
    return True


def create_radius_server_sequence(api):
    endpoint_result = api.radius_server_sequence.create_radius_server_sequence(
        active_validation=False,
        before_accept_attr_manipulators_list=[{'action': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string', 'changedVal': 'string'}],
        continue_authorz_policy=True,
        description='string',
        local_accounting=True,
        name='string',
        on_request_attr_manipulator_list=[{'action': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string', 'changedVal': 'string'}],
        payload=None,
        prefix_separator='string',
        radius_server_list=['string'],
        remote_accounting=True,
        strip_prefix=True,
        strip_suffix=True,
        suffix_separator='string',
        use_attr_set_before_acc=True,
        use_attr_set_on_request=True
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_create_radius_server_sequence(api, validator):
    try:
        assert is_valid_create_radius_server_sequence(
            validator,
            create_radius_server_sequence(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_radius_server_sequence_default(api):
    endpoint_result = api.radius_server_sequence.create_radius_server_sequence(
        active_validation=False,
        before_accept_attr_manipulators_list=None,
        continue_authorz_policy=None,
        description=None,
        local_accounting=None,
        name=None,
        on_request_attr_manipulator_list=None,
        payload=None,
        prefix_separator=None,
        radius_server_list=None,
        remote_accounting=None,
        strip_prefix=None,
        strip_suffix=None,
        suffix_separator=None,
        use_attr_set_before_acc=None,
        use_attr_set_on_request=None
    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_create_radius_server_sequence_default(api, validator):
    try:
        assert is_valid_create_radius_server_sequence(
            validator,
            create_radius_server_sequence_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_version(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_8fb1a72ded19590fa0aa85fc59ea8cfc_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.radius_server_sequence.get_version(

    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_get_version(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_version_default(api):
    endpoint_result = api.radius_server_sequence.get_version(

    )
    return endpoint_result


@pytest.mark.radius_server_sequence
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
