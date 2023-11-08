# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI patching API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.2_beta', reason='version does not match')


def is_valid_list_installed_hotpatches(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_20505f21b6f9513bb973027ba49f7c0d_v3_2_beta').validate(obj.response)
    return True


def list_installed_hotpatches(api):
    endpoint_result = api.patching.list_installed_hotpatches(

    )
    return endpoint_result


@pytest.mark.patching
def test_list_installed_hotpatches(api, validator):
    try:
        assert is_valid_list_installed_hotpatches(
            validator,
            list_installed_hotpatches(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def list_installed_hotpatches_default(api):
    endpoint_result = api.patching.list_installed_hotpatches(

    )
    return endpoint_result


@pytest.mark.patching
def test_list_installed_hotpatches_default(api, validator):
    try:
        assert is_valid_list_installed_hotpatches(
            validator,
            list_installed_hotpatches_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_install_hotpatch(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_a59ee76eaca6561888e738155395eaeb_v3_2_beta').validate(obj.response)
    return True


def install_hotpatch(api):
    endpoint_result = api.patching.install_hotpatch(
        active_validation=False,
        hotpatch_name='string',
        payload=None,
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.patching
def test_install_hotpatch(api, validator):
    try:
        assert is_valid_install_hotpatch(
            validator,
            install_hotpatch(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def install_hotpatch_default(api):
    endpoint_result = api.patching.install_hotpatch(
        active_validation=False,
        hotpatch_name=None,
        payload=None,
        repository_name=None
    )
    return endpoint_result


@pytest.mark.patching
def test_install_hotpatch_default(api, validator):
    try:
        assert is_valid_install_hotpatch(
            validator,
            install_hotpatch_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_rollback_hotpatch(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f65b1178749c5f2399a9d2395591dade_v3_2_beta').validate(obj.response)
    return True


def rollback_hotpatch(api):
    endpoint_result = api.patching.rollback_hotpatch(
        active_validation=False,
        hotpatch_name='string',
        payload=None,
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.patching
def test_rollback_hotpatch(api, validator):
    try:
        assert is_valid_rollback_hotpatch(
            validator,
            rollback_hotpatch(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def rollback_hotpatch_default(api):
    endpoint_result = api.patching.rollback_hotpatch(
        active_validation=False,
        hotpatch_name=None,
        payload=None,
        repository_name=None
    )
    return endpoint_result


@pytest.mark.patching
def test_rollback_hotpatch_default(api, validator):
    try:
        assert is_valid_rollback_hotpatch(
            validator,
            rollback_hotpatch_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_list_installed_patches(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_df2031d0bbb75aa0898d8b2ee2635fae_v3_2_beta').validate(obj.response)
    return True


def list_installed_patches(api):
    endpoint_result = api.patching.list_installed_patches(

    )
    return endpoint_result


@pytest.mark.patching
def test_list_installed_patches(api, validator):
    try:
        assert is_valid_list_installed_patches(
            validator,
            list_installed_patches(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def list_installed_patches_default(api):
    endpoint_result = api.patching.list_installed_patches(

    )
    return endpoint_result


@pytest.mark.patching
def test_list_installed_patches_default(api, validator):
    try:
        assert is_valid_list_installed_patches(
            validator,
            list_installed_patches_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_install_patch(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c6c3a7326c6a542899be49cb9289e1ae_v3_2_beta').validate(obj.response)
    return True


def install_patch(api):
    endpoint_result = api.patching.install_patch(
        active_validation=False,
        patch_name='string',
        payload=None,
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.patching
def test_install_patch(api, validator):
    try:
        assert is_valid_install_patch(
            validator,
            install_patch(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def install_patch_default(api):
    endpoint_result = api.patching.install_patch(
        active_validation=False,
        patch_name=None,
        payload=None,
        repository_name=None
    )
    return endpoint_result


@pytest.mark.patching
def test_install_patch_default(api, validator):
    try:
        assert is_valid_install_patch(
            validator,
            install_patch_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_rollback_patch(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_207bbf4f0a09516dbb4d0c7d7416fb20_v3_2_beta').validate(obj.response)
    return True


def rollback_patch(api):
    endpoint_result = api.patching.rollback_patch(
        active_validation=False,
        patch_number=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.patching
def test_rollback_patch(api, validator):
    try:
        assert is_valid_rollback_patch(
            validator,
            rollback_patch(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def rollback_patch_default(api):
    endpoint_result = api.patching.rollback_patch(
        active_validation=False,
        patch_number=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.patching
def test_rollback_patch_default(api, validator):
    try:
        assert is_valid_rollback_patch(
            validator,
            rollback_patch_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
