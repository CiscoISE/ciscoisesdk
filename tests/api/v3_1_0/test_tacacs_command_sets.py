# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI tacacs_command_sets API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_tacacs_command_sets_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_34f8ba0e97135ca6bacff94d5a76df97_v3_0_0').validate(obj.response)
    return True


def get_tacacs_command_sets_by_name(api):
    endpoint_result = api.tacacs_command_sets.get_tacacs_command_sets_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_get_tacacs_command_sets_by_name(api, validator):
    try:
        assert is_valid_get_tacacs_command_sets_by_name(
            validator,
            get_tacacs_command_sets_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tacacs_command_sets_by_name_default(api):
    endpoint_result = api.tacacs_command_sets.get_tacacs_command_sets_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_get_tacacs_command_sets_by_name_default(api, validator):
    try:
        assert is_valid_get_tacacs_command_sets_by_name(
            validator,
            get_tacacs_command_sets_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tacacs_command_sets_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2caefe2cb042513ab4a4a76f227330cb_v3_0_0').validate(obj.response)
    return True


def get_tacacs_command_sets_by_id(api):
    endpoint_result = api.tacacs_command_sets.get_tacacs_command_sets_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_get_tacacs_command_sets_by_id(api, validator):
    try:
        assert is_valid_get_tacacs_command_sets_by_id(
            validator,
            get_tacacs_command_sets_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tacacs_command_sets_by_id_default(api):
    endpoint_result = api.tacacs_command_sets.get_tacacs_command_sets_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_get_tacacs_command_sets_by_id_default(api, validator):
    try:
        assert is_valid_get_tacacs_command_sets_by_id(
            validator,
            get_tacacs_command_sets_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_tacacs_command_sets_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_20eb6323be425816a4116eea48f16f4b_v3_0_0').validate(obj.response)
    return True


def update_tacacs_command_sets_by_id(api):
    endpoint_result = api.tacacs_command_sets.update_tacacs_command_sets_by_id(
        active_validation=False,
        commands={'commandList': [{'grant': 'string', 'command': 'string', 'arguments': 'string'}]},
        description='string',
        id='string',
        name='string',
        payload=None,
        permit_unmatched=True
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_update_tacacs_command_sets_by_id(api, validator):
    try:
        assert is_valid_update_tacacs_command_sets_by_id(
            validator,
            update_tacacs_command_sets_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_tacacs_command_sets_by_id_default(api):
    endpoint_result = api.tacacs_command_sets.update_tacacs_command_sets_by_id(
        active_validation=False,
        id='string',
        commands=None,
        description=None,
        name=None,
        payload=None,
        permit_unmatched=None
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_update_tacacs_command_sets_by_id_default(api, validator):
    try:
        assert is_valid_update_tacacs_command_sets_by_id(
            validator,
            update_tacacs_command_sets_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_tacacs_command_sets_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4a319a83b14252eba0f00bb4c4ab0d7c_v3_0_0').validate(obj.response)
    return True


def delete_tacacs_command_sets_by_id(api):
    endpoint_result = api.tacacs_command_sets.delete_tacacs_command_sets_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_delete_tacacs_command_sets_by_id(api, validator):
    try:
        assert is_valid_delete_tacacs_command_sets_by_id(
            validator,
            delete_tacacs_command_sets_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_tacacs_command_sets_by_id_default(api):
    endpoint_result = api.tacacs_command_sets.delete_tacacs_command_sets_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_delete_tacacs_command_sets_by_id_default(api, validator):
    try:
        assert is_valid_delete_tacacs_command_sets_by_id(
            validator,
            delete_tacacs_command_sets_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tacacs_command_sets(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c9a67d3e9015580f93a52627f19e9916_v3_0_0').validate(obj.response)
    return True


def get_tacacs_command_sets(api):
    endpoint_result = api.tacacs_command_sets.get_tacacs_command_sets(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_get_tacacs_command_sets(api, validator):
    try:
        assert is_valid_get_tacacs_command_sets(
            validator,
            get_tacacs_command_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tacacs_command_sets_default(api):
    endpoint_result = api.tacacs_command_sets.get_tacacs_command_sets(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_get_tacacs_command_sets_default(api, validator):
    try:
        assert is_valid_get_tacacs_command_sets(
            validator,
            get_tacacs_command_sets_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_tacacs_command_sets(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d9cc879878ee5a34ac1c32f2f0cb8c6d_v3_0_0').validate(obj.response)
    return True


def create_tacacs_command_sets(api):
    endpoint_result = api.tacacs_command_sets.create_tacacs_command_sets(
        active_validation=False,
        commands={'commandList': [{'grant': 'string', 'command': 'string', 'arguments': 'string'}]},
        description='string',
        name='string',
        payload=None,
        permit_unmatched=True
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_create_tacacs_command_sets(api, validator):
    try:
        assert is_valid_create_tacacs_command_sets(
            validator,
            create_tacacs_command_sets(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_tacacs_command_sets_default(api):
    endpoint_result = api.tacacs_command_sets.create_tacacs_command_sets(
        active_validation=False,
        commands=None,
        description=None,
        name=None,
        payload=None,
        permit_unmatched=None
    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_create_tacacs_command_sets_default(api, validator):
    try:
        assert is_valid_create_tacacs_command_sets(
            validator,
            create_tacacs_command_sets_default(api)
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
    json_schema_validate('jsd_5865f0adb7f554eb810687bd8699149a_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.tacacs_command_sets.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
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
    endpoint_result = api.tacacs_command_sets.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_command_sets
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
