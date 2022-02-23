# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI downloadable_acl API fixtures and tests.

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


def is_valid_get_downloadable_acl_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_dfa8f48210e85715beebb44e62fac408_v3_1_1').validate(obj.response)
    return True


def get_downloadable_acl_by_id(api):
    endpoint_result = api.downloadable_acl.get_downloadable_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_get_downloadable_acl_by_id(api, validator):
    try:
        assert is_valid_get_downloadable_acl_by_id(
            validator,
            get_downloadable_acl_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_downloadable_acl_by_id_default(api):
    endpoint_result = api.downloadable_acl.get_downloadable_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_get_downloadable_acl_by_id_default(api, validator):
    try:
        assert is_valid_get_downloadable_acl_by_id(
            validator,
            get_downloadable_acl_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_downloadable_acl_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2d8c7ba0cb8f56d99135e16d2d973d11_v3_1_1').validate(obj.response)
    return True


def update_downloadable_acl_by_id(api):
    endpoint_result = api.downloadable_acl.update_downloadable_acl_by_id(
        active_validation=False,
        dacl='string',
        dacl_type='string',
        description='string',
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_update_downloadable_acl_by_id(api, validator):
    try:
        assert is_valid_update_downloadable_acl_by_id(
            validator,
            update_downloadable_acl_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_downloadable_acl_by_id_default(api):
    endpoint_result = api.downloadable_acl.update_downloadable_acl_by_id(
        active_validation=False,
        id='string',
        dacl=None,
        dacl_type=None,
        description=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_update_downloadable_acl_by_id_default(api, validator):
    try:
        assert is_valid_update_downloadable_acl_by_id(
            validator,
            update_downloadable_acl_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_downloadable_acl_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_42b3db444eaa50678218c29f88de60e8_v3_1_1').validate(obj.response)
    return True


def delete_downloadable_acl_by_id(api):
    endpoint_result = api.downloadable_acl.delete_downloadable_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_delete_downloadable_acl_by_id(api, validator):
    try:
        assert is_valid_delete_downloadable_acl_by_id(
            validator,
            delete_downloadable_acl_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_downloadable_acl_by_id_default(api):
    endpoint_result = api.downloadable_acl.delete_downloadable_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_delete_downloadable_acl_by_id_default(api, validator):
    try:
        assert is_valid_delete_downloadable_acl_by_id(
            validator,
            delete_downloadable_acl_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_downloadable_acl(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9191bc200af85d598885a990ff9bcbf8_v3_1_1').validate(obj.response)
    return True


def get_downloadable_acl(api):
    endpoint_result = api.downloadable_acl.get_downloadable_acl(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_get_downloadable_acl(api, validator):
    try:
        assert is_valid_get_downloadable_acl(
            validator,
            get_downloadable_acl(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_downloadable_acl_default(api):
    endpoint_result = api.downloadable_acl.get_downloadable_acl(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_get_downloadable_acl_default(api, validator):
    try:
        assert is_valid_get_downloadable_acl(
            validator,
            get_downloadable_acl_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_downloadable_acl(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_adcf947c42fe5588b7b82d9c43a3bbf0_v3_1_1').validate(obj.response)
    return True


def create_downloadable_acl(api):
    endpoint_result = api.downloadable_acl.create_downloadable_acl(
        active_validation=False,
        dacl='string',
        dacl_type='string',
        description='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_create_downloadable_acl(api, validator):
    try:
        assert is_valid_create_downloadable_acl(
            validator,
            create_downloadable_acl(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_downloadable_acl_default(api):
    endpoint_result = api.downloadable_acl.create_downloadable_acl(
        active_validation=False,
        dacl=None,
        dacl_type=None,
        description=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_create_downloadable_acl_default(api, validator):
    try:
        assert is_valid_create_downloadable_acl(
            validator,
            create_downloadable_acl_default(api)
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
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d10b7914625e5da0861cbeab4cf6440e_v3_1_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.downloadable_acl.get_version(

    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_get_version(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_version_default(api):
    endpoint_result = api.downloadable_acl.get_version(

    )
    return endpoint_result


@pytest.mark.downloadable_acl
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
