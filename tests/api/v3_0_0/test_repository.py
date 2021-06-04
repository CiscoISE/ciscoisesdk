# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI repository API fixtures and tests.

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


def is_valid_get_repositories(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8f9081a48e3c5f4fae5aa00f889216dd_v3_0_0').validate(obj.response)
    return True


def get_repositories(api):
    endpoint_result = api.repository.get_repositories(

    )
    return endpoint_result


@pytest.mark.repository
def test_get_repositories(api, validator):
    try:
        assert is_valid_get_repositories(
            validator,
            get_repositories(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_repositories_default(api):
    endpoint_result = api.repository.get_repositories(

    )
    return endpoint_result


@pytest.mark.repository
def test_get_repositories_default(api, validator):
    try:
        assert is_valid_get_repositories(
            validator,
            get_repositories_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_repository(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9a207a157244508c99bf3e9abb26aab8_v3_0_0').validate(obj.response)
    return True


def create_repository(api):
    endpoint_result = api.repository.create_repository(
        active_validation=False,
        enable_pki=True,
        name='string',
        password='string',
        path='string',
        payload=None,
        protocol='string',
        server_name='string',
        user_name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_create_repository(api, validator):
    try:
        assert is_valid_create_repository(
            validator,
            create_repository(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_repository_default(api):
    endpoint_result = api.repository.create_repository(
        active_validation=False,
        enable_pki=None,
        name=None,
        password=None,
        path=None,
        payload=None,
        protocol=None,
        server_name=None,
        user_name=None
    )
    return endpoint_result


@pytest.mark.repository
def test_create_repository_default(api, validator):
    try:
        assert is_valid_create_repository(
            validator,
            create_repository_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_repository_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_89c785067a5a5e3283f96dd5006c7865_v3_0_0').validate(obj.response)
    return True


def get_repository_by_name(api):
    endpoint_result = api.repository.get_repository_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_get_repository_by_name(api, validator):
    try:
        assert is_valid_get_repository_by_name(
            validator,
            get_repository_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_repository_by_name_default(api):
    endpoint_result = api.repository.get_repository_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_get_repository_by_name_default(api, validator):
    try:
        assert is_valid_get_repository_by_name(
            validator,
            get_repository_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_repository_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_386e380a5c1d585ab9012874ca959982_v3_0_0').validate(obj.response)
    return True


def update_repository_by_name(api):
    endpoint_result = api.repository.update_repository_by_name(
        active_validation=False,
        enable_pki=True,
        name='string',
        password='string',
        path='string',
        payload=None,
        protocol='string',
        server_name='string',
        user_name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_update_repository_by_name(api, validator):
    try:
        assert is_valid_update_repository_by_name(
            validator,
            update_repository_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_repository_by_name_default(api):
    endpoint_result = api.repository.update_repository_by_name(
        active_validation=False,
        name='string',
        enable_pki=None,
        password=None,
        path=None,
        payload=None,
        protocol=None,
        server_name=None,
        user_name=None
    )
    return endpoint_result


@pytest.mark.repository
def test_update_repository_by_name_default(api, validator):
    try:
        assert is_valid_update_repository_by_name(
            validator,
            update_repository_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_repository_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c3a2e8960455547da94117ef465db97f_v3_0_0').validate(obj.response)
    return True


def delete_repository_by_name(api):
    endpoint_result = api.repository.delete_repository_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_delete_repository_by_name(api, validator):
    try:
        assert is_valid_delete_repository_by_name(
            validator,
            delete_repository_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_repository_by_name_default(api):
    endpoint_result = api.repository.delete_repository_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_delete_repository_by_name_default(api, validator):
    try:
        assert is_valid_delete_repository_by_name(
            validator,
            delete_repository_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_repository_files(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c9dea644f40453fead2b003b06c4c52b_v3_0_0').validate(obj.response)
    return True


def get_repository_files(api):
    endpoint_result = api.repository.get_repository_files(
        name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_get_repository_files(api, validator):
    try:
        assert is_valid_get_repository_files(
            validator,
            get_repository_files(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_repository_files_default(api):
    endpoint_result = api.repository.get_repository_files(
        name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_get_repository_files_default(api, validator):
    try:
        assert is_valid_get_repository_files(
            validator,
            get_repository_files_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
