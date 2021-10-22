# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI security_groups_acls API fixtures and tests.

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


def is_valid_get_security_groups_acl_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a50d1bd34d5f593aadf8eb02083c67b0_v3_0_0').validate(obj.response)
    return True


def get_security_groups_acl_by_id(api):
    endpoint_result = api.security_groups_acls.get_security_groups_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_get_security_groups_acl_by_id(api, validator):
    try:
        assert is_valid_get_security_groups_acl_by_id(
            validator,
            get_security_groups_acl_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_groups_acl_by_id_default(api):
    endpoint_result = api.security_groups_acls.get_security_groups_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_get_security_groups_acl_by_id_default(api, validator):
    try:
        assert is_valid_get_security_groups_acl_by_id(
            validator,
            get_security_groups_acl_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_security_groups_acl_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_afc81cd1e25c50319f75606b97c23b3d_v3_0_0').validate(obj.response)
    return True


def update_security_groups_acl_by_id(api):
    endpoint_result = api.security_groups_acls.update_security_groups_acl_by_id(
        aclcontent='string',
        active_validation=False,
        description='string',
        generation_id='string',
        id='string',
        ip_version='string',
        is_read_only=True,
        modelled_content={},
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_update_security_groups_acl_by_id(api, validator):
    try:
        assert is_valid_update_security_groups_acl_by_id(
            validator,
            update_security_groups_acl_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_security_groups_acl_by_id_default(api):
    endpoint_result = api.security_groups_acls.update_security_groups_acl_by_id(
        active_validation=False,
        id='string',
        aclcontent=None,
        description=None,
        generation_id=None,
        ip_version=None,
        is_read_only=None,
        modelled_content=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_update_security_groups_acl_by_id_default(api, validator):
    try:
        assert is_valid_update_security_groups_acl_by_id(
            validator,
            update_security_groups_acl_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_security_groups_acl_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b0a2bea8bfec52b68663ef3f7ac6d7a7_v3_0_0').validate(obj.response)
    return True


def delete_security_groups_acl_by_id(api):
    endpoint_result = api.security_groups_acls.delete_security_groups_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_delete_security_groups_acl_by_id(api, validator):
    try:
        assert is_valid_delete_security_groups_acl_by_id(
            validator,
            delete_security_groups_acl_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_security_groups_acl_by_id_default(api):
    endpoint_result = api.security_groups_acls.delete_security_groups_acl_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_delete_security_groups_acl_by_id_default(api, validator):
    try:
        assert is_valid_delete_security_groups_acl_by_id(
            validator,
            delete_security_groups_acl_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_groups_acl(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_999b22d6ad9f595ab7e3eee5cf44de8a_v3_0_0').validate(obj.response)
    return True


def get_security_groups_acl(api):
    endpoint_result = api.security_groups_acls.get_security_groups_acl(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_get_security_groups_acl(api, validator):
    try:
        assert is_valid_get_security_groups_acl(
            validator,
            get_security_groups_acl(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_groups_acl_default(api):
    endpoint_result = api.security_groups_acls.get_security_groups_acl(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_get_security_groups_acl_default(api, validator):
    try:
        assert is_valid_get_security_groups_acl(
            validator,
            get_security_groups_acl_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_security_groups_acl(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9ab61f24bdaf508590f7686e1130913f_v3_0_0').validate(obj.response)
    return True


def create_security_groups_acl(api):
    endpoint_result = api.security_groups_acls.create_security_groups_acl(
        aclcontent='string',
        active_validation=False,
        description='string',
        generation_id='string',
        ip_version='string',
        is_read_only=True,
        modelled_content={},
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_create_security_groups_acl(api, validator):
    try:
        assert is_valid_create_security_groups_acl(
            validator,
            create_security_groups_acl(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_security_groups_acl_default(api):
    endpoint_result = api.security_groups_acls.create_security_groups_acl(
        active_validation=False,
        aclcontent=None,
        description=None,
        generation_id=None,
        ip_version=None,
        is_read_only=None,
        modelled_content=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_create_security_groups_acl_default(api, validator):
    try:
        assert is_valid_create_security_groups_acl(
            validator,
            create_security_groups_acl_default(api)
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
    json_schema_validate('jsd_6704e67a1131578aa794d8377da9a1de_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.security_groups_acls.get_version(

    )
    return endpoint_result


@pytest.mark.security_groups_acls
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
    endpoint_result = api.security_groups_acls.get_version(

    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_security_groups_acl(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7da250e23ac05e6a8dcf32a81effcee9_v3_0_0').validate(obj.response)
    return True


def bulk_request_for_security_groups_acl(api):
    endpoint_result = api.security_groups_acls.bulk_request_for_security_groups_acl(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_bulk_request_for_security_groups_acl(api, validator):
    try:
        assert is_valid_bulk_request_for_security_groups_acl(
            validator,
            bulk_request_for_security_groups_acl(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_request_for_security_groups_acl_default(api):
    endpoint_result = api.security_groups_acls.bulk_request_for_security_groups_acl(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_bulk_request_for_security_groups_acl_default(api, validator):
    try:
        assert is_valid_bulk_request_for_security_groups_acl(
            validator,
            bulk_request_for_security_groups_acl_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_security_groups_acl(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_07af5ee576605a5a915d888924c1e804_v3_0_0').validate(obj.response)
    return True


def monitor_bulk_status_security_groups_acl(api):
    endpoint_result = api.security_groups_acls.monitor_bulk_status_security_groups_acl(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_monitor_bulk_status_security_groups_acl(api, validator):
    try:
        assert is_valid_monitor_bulk_status_security_groups_acl(
            validator,
            monitor_bulk_status_security_groups_acl(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def monitor_bulk_status_security_groups_acl_default(api):
    endpoint_result = api.security_groups_acls.monitor_bulk_status_security_groups_acl(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.security_groups_acls
def test_monitor_bulk_status_security_groups_acl_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_security_groups_acl(
            validator,
            monitor_bulk_status_security_groups_acl_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
