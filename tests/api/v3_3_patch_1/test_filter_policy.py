# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI filter_policy API fixtures and tests.

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


def is_valid_get_filter_policy_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_16555f5d5ab6568d8bf5f9932f7ed7f4_v3_3_patch_1').validate(obj.response)
    return True


def get_filter_policy_by_id(api):
    endpoint_result = api.filter_policy.get_filter_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_get_filter_policy_by_id(api, validator):
    try:
        assert is_valid_get_filter_policy_by_id(
            validator,
            get_filter_policy_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_filter_policy_by_id_default(api):
    endpoint_result = api.filter_policy.get_filter_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_get_filter_policy_by_id_default(api, validator):
    try:
        assert is_valid_get_filter_policy_by_id(
            validator,
            get_filter_policy_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_filter_policy_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_95d0006cc03d53c89a3593526bf8dc0f_v3_3_patch_1').validate(obj.response)
    return True


def update_filter_policy_by_id(api):
    endpoint_result = api.filter_policy.update_filter_policy_by_id(
        active_validation=False,
        domains='string',
        id='string',
        payload=None,
        sgt='string',
        subnet='string',
        vn='string'
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_update_filter_policy_by_id(api, validator):
    try:
        assert is_valid_update_filter_policy_by_id(
            validator,
            update_filter_policy_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_filter_policy_by_id_default(api):
    endpoint_result = api.filter_policy.update_filter_policy_by_id(
        active_validation=False,
        id='string',
        domains=None,
        payload=None,
        sgt=None,
        subnet=None,
        vn=None
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_update_filter_policy_by_id_default(api, validator):
    try:
        assert is_valid_update_filter_policy_by_id(
            validator,
            update_filter_policy_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_filter_policy_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4a83e0d4f56a5c06946f685aa46fa3e3_v3_3_patch_1').validate(obj.response)
    return True


def delete_filter_policy_by_id(api):
    endpoint_result = api.filter_policy.delete_filter_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_delete_filter_policy_by_id(api, validator):
    try:
        assert is_valid_delete_filter_policy_by_id(
            validator,
            delete_filter_policy_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_filter_policy_by_id_default(api):
    endpoint_result = api.filter_policy.delete_filter_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_delete_filter_policy_by_id_default(api, validator):
    try:
        assert is_valid_delete_filter_policy_by_id(
            validator,
            delete_filter_policy_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_filter_policy(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_250a599ae00f5e47b9ece23cd3183d1c_v3_3_patch_1').validate(obj.response)
    return True


def get_filter_policy(api):
    endpoint_result = api.filter_policy.get_filter_policy(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_get_filter_policy(api, validator):
    try:
        assert is_valid_get_filter_policy(
            validator,
            get_filter_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_filter_policy_default(api):
    endpoint_result = api.filter_policy.get_filter_policy(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_get_filter_policy_default(api, validator):
    try:
        assert is_valid_get_filter_policy(
            validator,
            get_filter_policy_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_filter_policy(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_22f8082b07ce528f82545e210b84d7de_v3_3_patch_1').validate(obj.response)
    return True


def create_filter_policy(api):
    endpoint_result = api.filter_policy.create_filter_policy(
        active_validation=False,
        domains='string',
        payload=None,
        sgt='string',
        subnet='string',
        vn='string'
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_create_filter_policy(api, validator):
    try:
        assert is_valid_create_filter_policy(
            validator,
            create_filter_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_filter_policy_default(api):
    endpoint_result = api.filter_policy.create_filter_policy(
        active_validation=False,
        domains=None,
        payload=None,
        sgt=None,
        subnet=None,
        vn=None
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_create_filter_policy_default(api, validator):
    try:
        assert is_valid_create_filter_policy(
            validator,
            create_filter_policy_default(api)
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
    json_schema_validate('jsd_209810ed6cad570d90243b1e0dbbe27b_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.filter_policy.get_version(

    )
    return endpoint_result


@pytest.mark.filter_policy
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
    endpoint_result = api.filter_policy.get_version(

    )
    return endpoint_result


@pytest.mark.filter_policy
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_filter_policy_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1d1f85d51e0255c6bb9e89d0617d3434_v3_3_patch_1').validate(obj.response)
    return True


def patch_filter_policy_id(api):
    endpoint_result = api.filter_policy.patch_filter_policy_id(
        active_validation=False,
        description='string',
        domains='string',
        id='string',
        name='string',
        payload=None,
        sgt='string',
        subnet='string',
        vn='string'
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_patch_filter_policy_id(api, validator):
    try:
        assert is_valid_patch_filter_policy_id(
            validator,
            patch_filter_policy_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_filter_policy_id_default(api):
    endpoint_result = api.filterpolicy.patch_filter_policy_id(
        active_validation=False,
        id='string',
        description=None,
        domains=None,
        name=None,
        payload=None,
        sgt=None,
        subnet=None,
        vn=None
    )
    return endpoint_result


@pytest.mark.filter_policy
def test_patch_filter_policy_id_default(api, validator):
    try:
        assert is_valid_patch_filter_policy_id(
            validator,
            patch_filter_policy_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
