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
from ciscoisesdk.exceptions import ciscoisesdkException
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.3_patch_1', reason='version does not match')


def is_valid_get_repositories(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8f9081a48e3c5f4fae5aa00f889216dd_v3_3_patch_1').validate(obj.response)
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
            print("ERROR: {error}".format(error=original_e))
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9a207a157244508c99bf3e9abb26aab8_v3_3_patch_1').validate(obj.response)
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
            print("ERROR: {error}".format(error=original_e))
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


def is_valid_get_repository(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e4fd4586ad825f69843d9213e956cf81_v3_3_patch_1').validate(obj.response)
    return True


def get_repository(api):
    endpoint_result = api.repository.get_repository(
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_get_repository(api, validator):
    try:
        assert is_valid_get_repository(
            validator,
            get_repository(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_repository_default(api):
    endpoint_result = api.repository.get_repository(
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_get_repository_default(api, validator):
    try:
        assert is_valid_get_repository(
            validator,
            get_repository_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_repository(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f757b04825bb5c29a1b3475aae870d04_v3_3_patch_1').validate(obj.response)
    return True


def update_repository(api):
    endpoint_result = api.repository.update_repository(
        active_validation=False,
        enable_pki=True,
        name='string',
        password='string',
        path='string',
        payload=None,
        protocol='string',
        repository_name='string',
        server_name='string',
        user_name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_update_repository(api, validator):
    try:
        assert is_valid_update_repository(
            validator,
            update_repository(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_repository_default(api):
    endpoint_result = api.repository.update_repository(
        active_validation=False,
        repository_name='string',
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
def test_update_repository_default(api, validator):
    try:
        assert is_valid_update_repository(
            validator,
            update_repository_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_repository(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_12e3bcabbd0e5e899945592039694139_v3_3_patch_1').validate(obj.response)
    return True


def delete_repository(api):
    endpoint_result = api.repository.delete_repository(
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_delete_repository(api, validator):
    try:
        assert is_valid_delete_repository(
            validator,
            delete_repository(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_repository_default(api):
    endpoint_result = api.repository.delete_repository(
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.repository
def test_delete_repository_default(api, validator):
    try:
        assert is_valid_delete_repository(
            validator,
            delete_repository_default(api)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4c6f272fde105e50a210f88a9e3f032c_v3_3_patch_1').validate(obj.response)
    return True


def get_repository_files(api):
    endpoint_result = api.repository.get_repository_files(
        repository_name='string'
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
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_repository_files_default(api):
    endpoint_result = api.repository.get_repository_files(
        repository_name='string'
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
