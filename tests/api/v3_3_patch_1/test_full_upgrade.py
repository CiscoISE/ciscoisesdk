# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI full_upgrade API fixtures and tests.

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


def is_valid_get_precheck_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6a8cb91a4f09598bbdfa6c4b146c2763_v3_3_patch_1').validate(obj.response)
    return True


def get_precheck_status(api):
    endpoint_result = api.full_upgrade.get_precheck_status(
        pre_check_id='string',
        pre_check_report_id='string'
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_get_precheck_status(api, validator):
    try:
        assert is_valid_get_precheck_status(
            validator,
            get_precheck_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_precheck_status_default(api):
    endpoint_result = api.full_upgrade.get_precheck_status(
        pre_check_id=None,
        pre_check_report_id=None
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_get_precheck_status_default(api, validator):
    try:
        assert is_valid_get_precheck_status(
            validator,
            get_precheck_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_pre_checks_in_p_p_a_n(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_aa612059ca395d97922d045b42c75fcc_v3_3_patch_1').validate(obj.response)
    return True


def run_pre_checks_in_p_p_a_n(api):
    endpoint_result = api.full_upgrade.run_pre_checks_in_p_p_a_n(
        active_validation=False,
        bundle_name='string',
        hostnames=['string'],
        patch_bundle_name='string',
        payload=None,
        pre_check_report_id='string',
        pre_checks=['string'],
        re_trigger=True,
        repo_name='string',
        upgrade_type='string'
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_run_pre_checks_in_p_p_a_n(api, validator):
    try:
        assert is_valid_run_pre_checks_in_p_p_a_n(
            validator,
            run_pre_checks_in_p_p_a_n(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def run_pre_checks_in_p_p_a_n_default(api):
    endpoint_result = api.full_upgrade.run_pre_checks_in_p_p_a_n(
        active_validation=False,
        bundle_name=None,
        hostnames=None,
        patch_bundle_name=None,
        payload=None,
        pre_check_report_id=None,
        pre_checks=None,
        re_trigger=None,
        repo_name=None,
        upgrade_type=None
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_run_pre_checks_in_p_p_a_n_default(api, validator):
    try:
        assert is_valid_run_pre_checks_in_p_p_a_n(
            validator,
            run_pre_checks_in_p_p_a_n_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_proceed_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_15572010b4b951fa8ed4a6e4da1a5696_v3_3_patch_1').validate(obj.response)
    return True


def proceed_status(api):
    endpoint_result = api.full_upgrade.proceed_status(
        pre_check_report_id='string'
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_proceed_status(api, validator):
    try:
        assert is_valid_proceed_status(
            validator,
            proceed_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def proceed_status_default(api):
    endpoint_result = api.full_upgrade.proceed_status(
        pre_check_report_id=None
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_proceed_status_default(api, validator):
    try:
        assert is_valid_proceed_status(
            validator,
            proceed_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_initiate_upgrade_on_p_p_a_n(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_22d4d90ae0435f3fa638b6b4f206b5a6_v3_3_patch_1').validate(obj.response)
    return True


def initiate_upgrade_on_p_p_a_n(api):
    endpoint_result = api.full_upgrade.initiate_upgrade_on_p_p_a_n(
        active_validation=False,
        hostnames=['string'],
        payload=None,
        pre_check_report_id='string',
        upgrade_type='string'
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_initiate_upgrade_on_p_p_a_n(api, validator):
    try:
        assert is_valid_initiate_upgrade_on_p_p_a_n(
            validator,
            initiate_upgrade_on_p_p_a_n(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def initiate_upgrade_on_p_p_a_n_default(api):
    endpoint_result = api.full_upgrade.initiate_upgrade_on_p_p_a_n(
        active_validation=False,
        hostnames=None,
        payload=None,
        pre_check_report_id=None,
        upgrade_type=None
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_initiate_upgrade_on_p_p_a_n_default(api, validator):
    try:
        assert is_valid_initiate_upgrade_on_p_p_a_n(
            validator,
            initiate_upgrade_on_p_p_a_n_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_cancel_staging_on_p_p_a_n(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1255607ea018583db18166b743662136_v3_3_patch_1').validate(obj.response)
    return True


def cancel_staging_on_p_p_a_n(api):
    endpoint_result = api.full_upgrade.cancel_staging_on_p_p_a_n(
        active_validation=False,
        hostnames=['string'],
        payload=None,
        pre_check_report_id='string',
        upgrade_type='string'
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_cancel_staging_on_p_p_a_n(api, validator):
    try:
        assert is_valid_cancel_staging_on_p_p_a_n(
            validator,
            cancel_staging_on_p_p_a_n(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def cancel_staging_on_p_p_a_n_default(api):
    endpoint_result = api.full_upgrade.cancel_staging_on_p_p_a_n(
        active_validation=False,
        hostnames=None,
        payload=None,
        pre_check_report_id=None,
        upgrade_type=None
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_cancel_staging_on_p_p_a_n_default(api, validator):
    try:
        assert is_valid_cancel_staging_on_p_p_a_n(
            validator,
            cancel_staging_on_p_p_a_n_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_stage_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_de4f26345bf95460b81cfce5395e989c_v3_3_patch_1').validate(obj.response)
    return True


def stage_status(api):
    endpoint_result = api.full_upgrade.stage_status(
        pre_check_report_id='string'
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_stage_status(api, validator):
    try:
        assert is_valid_stage_status(
            validator,
            stage_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def stage_status_default(api):
    endpoint_result = api.full_upgrade.stage_status(
        pre_check_report_id=None
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_stage_status_default(api, validator):
    try:
        assert is_valid_stage_status(
            validator,
            stage_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_initiate_staging_on_p_p_a_n(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0d78612f495d584a8a941677e9194f35_v3_3_patch_1').validate(obj.response)
    return True


def initiate_staging_on_p_p_a_n(api):
    endpoint_result = api.full_upgrade.initiate_staging_on_p_p_a_n(
        active_validation=False,
        hostnames=['string'],
        payload=None,
        pre_check_report_id='string',
        re_trigger=True,
        upgrade_type='string'
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_initiate_staging_on_p_p_a_n(api, validator):
    try:
        assert is_valid_initiate_staging_on_p_p_a_n(
            validator,
            initiate_staging_on_p_p_a_n(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def initiate_staging_on_p_p_a_n_default(api):
    endpoint_result = api.full_upgrade.initiate_staging_on_p_p_a_n(
        active_validation=False,
        hostnames=None,
        payload=None,
        pre_check_report_id=None,
        re_trigger=None,
        upgrade_type=None
    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_initiate_staging_on_p_p_a_n_default(api, validator):
    try:
        assert is_valid_initiate_staging_on_p_p_a_n(
            validator,
            initiate_staging_on_p_p_a_n_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_upgradesummary(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2c8ccef8538b5c3892d8e9211faa051f_v3_3_patch_1').validate(obj.response)
    return True


def upgradesummary(api):
    endpoint_result = api.full_upgrade.upgradesummary(

    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_upgradesummary(api, validator):
    try:
        assert is_valid_upgradesummary(
            validator,
            upgradesummary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def upgradesummary_default(api):
    endpoint_result = api.full_upgrade.upgradesummary(

    )
    return endpoint_result


@pytest.mark.full_upgrade
def test_upgradesummary_default(api, validator):
    try:
        assert is_valid_upgradesummary(
            validator,
            upgradesummary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
