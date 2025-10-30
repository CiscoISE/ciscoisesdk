# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI patch API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.5.0', reason='version does not match')


def is_valid_run_patch_pre_checks(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def run_patch_pre_checks(api):
    endpoint_result = api.patch.run_patch_pre_checks(
    )
    return endpoint_result


@pytest.mark.patch
def test_run_patch_pre_checks(api, validator):
    try:
        assert is_valid_run_patch_pre_checks(
            validator,
            run_patch_pre_checks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def run_patch_pre_checks_default(api):
    endpoint_result = api.patch.run_patch_pre_checks(
    )
    return endpoint_result


@pytest.mark.patch
def test_run_patch_pre_checks_default(api, validator):
    try:
        assert is_valid_run_patch_pre_checks(
            validator,
            run_patch_pre_checks_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_patch_precheck_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_patch_precheck_status(api):
    endpoint_result = api.patch.get_patch_precheck_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_get_patch_precheck_status(api, validator):
    try:
        assert is_valid_get_patch_precheck_status(
            validator,
            get_patch_precheck_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_patch_precheck_status_default(api):
    endpoint_result = api.patch.get_patch_precheck_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_get_patch_precheck_status_default(api, validator):
    try:
        assert is_valid_get_patch_precheck_status(
            validator,
            get_patch_precheck_status_default(api)
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
    return True


def install_patch(api):
    endpoint_result = api.patch.install_patch(
    )
    return endpoint_result


@pytest.mark.patch
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
    endpoint_result = api.patch.install_patch(
    )
    return endpoint_result


@pytest.mark.patch
def test_install_patch_default(api, validator):
    try:
        assert is_valid_install_patch(
            validator,
            install_patch_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_install_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def patch_install_status(api):
    endpoint_result = api.patch.patch_install_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_install_status(api, validator):
    try:
        assert is_valid_patch_install_status(
            validator,
            patch_install_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_install_status_default(api):
    endpoint_result = api.patch.patch_install_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_install_status_default(api, validator):
    try:
        assert is_valid_patch_install_status(
            validator,
            patch_install_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_installed_patches(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_installed_patches(api):
    endpoint_result = api.patch.get_installed_patches(
    )
    return endpoint_result


@pytest.mark.patch
def test_get_installed_patches(api, validator):
    try:
        assert is_valid_get_installed_patches(
            validator,
            get_installed_patches(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_installed_patches_default(api):
    endpoint_result = api.patch.get_installed_patches(
    )
    return endpoint_result


@pytest.mark.patch
def test_get_installed_patches_default(api, validator):
    try:
        assert is_valid_get_installed_patches(
            validator,
            get_installed_patches_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_rollback_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def patch_rollback_info(api):
    endpoint_result = api.patch.patch_rollback_info(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_rollback_info(api, validator):
    try:
        assert is_valid_patch_rollback_info(
            validator,
            patch_rollback_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_rollback_info_default(api):
    endpoint_result = api.patch.patch_rollback_info(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_rollback_info_default(api, validator):
    try:
        assert is_valid_patch_rollback_info(
            validator,
            patch_rollback_info_default(api)
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
    return True


def rollback_patch(api):
    endpoint_result = api.patch.rollback_patch(
    )
    return endpoint_result


@pytest.mark.patch
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
    endpoint_result = api.patch.rollback_patch(
    )
    return endpoint_result


@pytest.mark.patch
def test_rollback_patch_default(api, validator):
    try:
        assert is_valid_rollback_patch(
            validator,
            rollback_patch_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_rollback_pre_checks(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def run_rollback_pre_checks(api):
    endpoint_result = api.patch.run_rollback_pre_checks(
    )
    return endpoint_result


@pytest.mark.patch
def test_run_rollback_pre_checks(api, validator):
    try:
        assert is_valid_run_rollback_pre_checks(
            validator,
            run_rollback_pre_checks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def run_rollback_pre_checks_default(api):
    endpoint_result = api.patch.run_rollback_pre_checks(
    )
    return endpoint_result


@pytest.mark.patch
def test_run_rollback_pre_checks_default(api, validator):
    try:
        assert is_valid_run_rollback_pre_checks(
            validator,
            run_rollback_pre_checks_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rollback_precheck_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_rollback_precheck_status(api):
    endpoint_result = api.patch.get_rollback_precheck_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_get_rollback_precheck_status(api, validator):
    try:
        assert is_valid_get_rollback_precheck_status(
            validator,
            get_rollback_precheck_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_rollback_precheck_status_default(api):
    endpoint_result = api.patch.get_rollback_precheck_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_get_rollback_precheck_status_default(api, validator):
    try:
        assert is_valid_get_rollback_precheck_status(
            validator,
            get_rollback_precheck_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_rollback_summary(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def patch_rollback_summary(api):
    endpoint_result = api.patch.patch_rollback_summary(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_rollback_summary(api, validator):
    try:
        assert is_valid_patch_rollback_summary(
            validator,
            patch_rollback_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_rollback_summary_default(api):
    endpoint_result = api.patch.patch_rollback_summary(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_rollback_summary_default(api, validator):
    try:
        assert is_valid_patch_rollback_summary(
            validator,
            patch_rollback_summary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_rollback_proceed_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def patch_rollback_proceed_status(api):
    endpoint_result = api.patch.patch_rollback_proceed_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_rollback_proceed_status(api, validator):
    try:
        assert is_valid_patch_rollback_proceed_status(
            validator,
            patch_rollback_proceed_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_rollback_proceed_status_default(api):
    endpoint_result = api.patch.patch_rollback_proceed_status(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_rollback_proceed_status_default(api, validator):
    try:
        assert is_valid_patch_rollback_proceed_status(
            validator,
            patch_rollback_proceed_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_summary(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def patch_summary(api):
    endpoint_result = api.patch.patch_summary(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_summary(api, validator):
    try:
        assert is_valid_patch_summary(
            validator,
            patch_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_summary_default(api):
    endpoint_result = api.patch.patch_summary(
    )
    return endpoint_result


@pytest.mark.patch
def test_patch_summary_default(api, validator):
    try:
        assert is_valid_patch_summary(
            validator,
            patch_summary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


