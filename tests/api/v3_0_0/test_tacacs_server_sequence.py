# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI tacacs_server_sequence API fixtures and tests.

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


def is_valid_get_tacacs_server_sequence_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_493b03900a2e5027b615d9f1bdcf9f63_v3_0_0').validate(obj.response)
    return True


def get_tacacs_server_sequence_by_name(api):
    endpoint_result = api.tacacs_server_sequence.get_tacacs_server_sequence_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_get_tacacs_server_sequence_by_name(api, validator):
    try:
        assert is_valid_get_tacacs_server_sequence_by_name(
            validator,
            get_tacacs_server_sequence_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tacacs_server_sequence_by_name_default(api):
    endpoint_result = api.tacacs_server_sequence.get_tacacs_server_sequence_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_get_tacacs_server_sequence_by_name_default(api, validator):
    try:
        assert is_valid_get_tacacs_server_sequence_by_name(
            validator,
            get_tacacs_server_sequence_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tacacs_server_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f3b45b8e4089574c9912407f88b1a5d2_v3_0_0').validate(obj.response)
    return True


def get_tacacs_server_sequence_by_id(api):
    endpoint_result = api.tacacs_server_sequence.get_tacacs_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_get_tacacs_server_sequence_by_id(api, validator):
    try:
        assert is_valid_get_tacacs_server_sequence_by_id(
            validator,
            get_tacacs_server_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_tacacs_server_sequence_by_id_default(api):
    endpoint_result = api.tacacs_server_sequence.get_tacacs_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_get_tacacs_server_sequence_by_id_default(api, validator):
    try:
        assert is_valid_get_tacacs_server_sequence_by_id(
            validator,
            get_tacacs_server_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_tacacs_server_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_18f6de5797735bbd95dc8683c6a7aebf_v3_0_0').validate(obj.response)
    return True


def update_tacacs_server_sequence_by_id(api):
    endpoint_result = api.tacacs_server_sequence.update_tacacs_server_sequence_by_id(
        active_validation=False,
        description='string',
        id='string',
        local_accounting=True,
        name='string',
        payload=None,
        prefix_delimiter='string',
        prefix_strip=True,
        remote_accounting=True,
        server_list='string',
        suffix_delimiter='string',
        suffix_strip=True
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_update_tacacs_server_sequence_by_id(api, validator):
    try:
        assert is_valid_update_tacacs_server_sequence_by_id(
            validator,
            update_tacacs_server_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_tacacs_server_sequence_by_id_default(api):
    endpoint_result = api.tacacs_server_sequence.update_tacacs_server_sequence_by_id(
        active_validation=False,
        id='string',
        description=None,
        local_accounting=None,
        name=None,
        payload=None,
        prefix_delimiter=None,
        prefix_strip=None,
        remote_accounting=None,
        server_list=None,
        suffix_delimiter=None,
        suffix_strip=None
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_update_tacacs_server_sequence_by_id_default(api, validator):
    try:
        assert is_valid_update_tacacs_server_sequence_by_id(
            validator,
            update_tacacs_server_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_tacacs_server_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a1465b72911359bdbb1430469801d4be_v3_0_0').validate(obj.response)
    return True


def delete_tacacs_server_sequence_by_id(api):
    endpoint_result = api.tacacs_server_sequence.delete_tacacs_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_delete_tacacs_server_sequence_by_id(api, validator):
    try:
        assert is_valid_delete_tacacs_server_sequence_by_id(
            validator,
            delete_tacacs_server_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_tacacs_server_sequence_by_id_default(api):
    endpoint_result = api.tacacs_server_sequence.delete_tacacs_server_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_delete_tacacs_server_sequence_by_id_default(api, validator):
    try:
        assert is_valid_delete_tacacs_server_sequence_by_id(
            validator,
            delete_tacacs_server_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_tacacs_server_sequence(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_54187c189f2f5f6b8bab3931c206c949_v3_0_0').validate(obj.response)
    return True


def get_all_tacacs_server_sequence(api):
    endpoint_result = api.tacacs_server_sequence.get_all_tacacs_server_sequence(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_get_all_tacacs_server_sequence(api, validator):
    try:
        assert is_valid_get_all_tacacs_server_sequence(
            validator,
            get_all_tacacs_server_sequence(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_tacacs_server_sequence_default(api):
    endpoint_result = api.tacacs_server_sequence.get_all_tacacs_server_sequence(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_get_all_tacacs_server_sequence_default(api, validator):
    try:
        assert is_valid_get_all_tacacs_server_sequence(
            validator,
            get_all_tacacs_server_sequence_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_tacacs_server_sequence(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_5902a1e26e595667bd98f84dd29232e2_v3_0_0').validate(obj.response)
    return True


def create_tacacs_server_sequence(api):
    endpoint_result = api.tacacs_server_sequence.create_tacacs_server_sequence(
        active_validation=False,
        description='string',
        local_accounting=True,
        name='string',
        payload=None,
        prefix_delimiter='string',
        prefix_strip=True,
        remote_accounting=True,
        server_list='string',
        suffix_delimiter='string',
        suffix_strip=True
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_create_tacacs_server_sequence(api, validator):
    try:
        assert is_valid_create_tacacs_server_sequence(
            validator,
            create_tacacs_server_sequence(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_tacacs_server_sequence_default(api):
    endpoint_result = api.tacacs_server_sequence.create_tacacs_server_sequence(
        active_validation=False,
        description=None,
        local_accounting=None,
        name=None,
        payload=None,
        prefix_delimiter=None,
        prefix_strip=None,
        remote_accounting=None,
        server_list=None,
        suffix_delimiter=None,
        suffix_strip=None
    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_create_tacacs_server_sequence_default(api, validator):
    try:
        assert is_valid_create_tacacs_server_sequence(
            validator,
            create_tacacs_server_sequence_default(api)
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
    json_schema_validate('jsd_aa8e1dc47a445d44ab86020f421ee721_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.tacacs_server_sequence.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
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
    endpoint_result = api.tacacs_server_sequence.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_server_sequence
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
