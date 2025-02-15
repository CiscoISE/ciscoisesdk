# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI endpoint_identity_group API fixtures and tests.

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


def is_valid_get_endpoint_group_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2590f64c3c08518e9eef83a92d69cde3_v3_3_patch_1').validate(obj.response)
    return True


def get_endpoint_group_by_name(api):
    endpoint_result = api.endpoint_identity_group.get_endpoint_group_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_get_endpoint_group_by_name(api, validator):
    try:
        assert is_valid_get_endpoint_group_by_name(
            validator,
            get_endpoint_group_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_endpoint_group_by_name_default(api):
    endpoint_result = api.endpoint_identity_group.get_endpoint_group_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_get_endpoint_group_by_name_default(api, validator):
    try:
        assert is_valid_get_endpoint_group_by_name(
            validator,
            get_endpoint_group_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoint_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5e4bfa620f76545d9887045cd24d99a2_v3_3_patch_1').validate(obj.response)
    return True


def get_endpoint_group_by_id(api):
    endpoint_result = api.endpoint_identity_group.get_endpoint_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_get_endpoint_group_by_id(api, validator):
    try:
        assert is_valid_get_endpoint_group_by_id(
            validator,
            get_endpoint_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_endpoint_group_by_id_default(api):
    endpoint_result = api.endpoint_identity_group.get_endpoint_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_get_endpoint_group_by_id_default(api, validator):
    try:
        assert is_valid_get_endpoint_group_by_id(
            validator,
            get_endpoint_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_endpoint_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_189979b4e8d45639975c226dacd53e7b_v3_3_patch_1').validate(obj.response)
    return True


def update_endpoint_group_by_id(api):
    endpoint_result = api.endpoint_identity_group.update_endpoint_group_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        system_defined=True
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_update_endpoint_group_by_id(api, validator):
    try:
        assert is_valid_update_endpoint_group_by_id(
            validator,
            update_endpoint_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_endpoint_group_by_id_default(api):
    endpoint_result = api.endpoint_identity_group.update_endpoint_group_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        payload=None,
        system_defined=None
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_update_endpoint_group_by_id_default(api, validator):
    try:
        assert is_valid_update_endpoint_group_by_id(
            validator,
            update_endpoint_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_endpoint_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f7b0aab2a65652feae637779bfb20d2d_v3_3_patch_1').validate(obj.response)
    return True


def delete_endpoint_group_by_id(api):
    endpoint_result = api.endpoint_identity_group.delete_endpoint_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_delete_endpoint_group_by_id(api, validator):
    try:
        assert is_valid_delete_endpoint_group_by_id(
            validator,
            delete_endpoint_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_endpoint_group_by_id_default(api):
    endpoint_result = api.endpoint_identity_group.delete_endpoint_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_delete_endpoint_group_by_id_default(api, validator):
    try:
        assert is_valid_delete_endpoint_group_by_id(
            validator,
            delete_endpoint_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoint_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_cd429bb8ff3556a796570480f742028b_v3_3_patch_1').validate(obj.response)
    return True


def get_endpoint_groups(api):
    endpoint_result = api.endpoint_identity_group.get_endpoint_groups(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_get_endpoint_groups(api, validator):
    try:
        assert is_valid_get_endpoint_groups(
            validator,
            get_endpoint_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_endpoint_groups_default(api):
    endpoint_result = api.endpoint_identity_group.get_endpoint_groups(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_get_endpoint_groups_default(api, validator):
    try:
        assert is_valid_get_endpoint_groups(
            validator,
            get_endpoint_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_endpoint_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b14d63c641e95ac0a8c2da2fb65909c7_v3_3_patch_1').validate(obj.response)
    return True


def create_endpoint_group(api):
    endpoint_result = api.endpoint_identity_group.create_endpoint_group(
        active_validation=False,
        description='string',
        name='string',
        payload=None,
        system_defined=True
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_create_endpoint_group(api, validator):
    try:
        assert is_valid_create_endpoint_group(
            validator,
            create_endpoint_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_endpoint_group_default(api):
    endpoint_result = api.endpoint_identity_group.create_endpoint_group(
        active_validation=False,
        description=None,
        name=None,
        payload=None,
        system_defined=None
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_create_endpoint_group_default(api, validator):
    try:
        assert is_valid_create_endpoint_group(
            validator,
            create_endpoint_group_default(api)
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
    json_schema_validate('jsd_1d553cc3b48d5689ac45a582a5d98f9b_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.endpoint_identity_group.get_version(

    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
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
    endpoint_result = api.endpoint_identity_group.get_version(

    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_endpoint_group_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_072aa2f78896596894e1bdceee801e7e_v3_3_patch_1').validate(obj.response)
    return True


def patch_endpoint_group_id(api):
    endpoint_result = api.endpoint_identity_group.patch_endpoint_group_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        parent_id='string',
        payload=None,
        system_defined=True
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_patch_endpoint_group_id(api, validator):
    try:
        assert is_valid_patch_endpoint_group_id(
            validator,
            patch_endpoint_group_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_endpoint_group_id_default(api):
    endpoint_result = api.endpoint_identity_group.patch_endpoint_group_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        parent_id=None,
        payload=None,
        system_defined=None
    )
    return endpoint_result


@pytest.mark.endpoint_identity_group
def test_patch_endpoint_group_id_default(api, validator):
    try:
        assert is_valid_patch_endpoint_group_id(
            validator,
            patch_endpoint_group_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
