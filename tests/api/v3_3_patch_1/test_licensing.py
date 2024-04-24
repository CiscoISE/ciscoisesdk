# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI licensing API fixtures and tests.

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


def is_valid_get_smart_state(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_53c3b7a2b80553559ed00849b25715c5_v3_3_patch_1').validate(obj.response)
    return True


def get_smart_state(api):
    endpoint_result = api.licensing.get_smart_state(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_smart_state(api, validator):
    try:
        assert is_valid_get_smart_state(
            validator,
            get_smart_state(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_smart_state_default(api):
    endpoint_result = api.licensing.get_smart_state(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_smart_state_default(api, validator):
    try:
        assert is_valid_get_smart_state(
            validator,
            get_smart_state_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_configure_smart_state(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_82bb02a9d24c5cda91845fec33541553_v3_3_patch_1').validate(obj.response)
    return True


def configure_smart_state(api):
    endpoint_result = api.licensing.configure_smart_state(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.licensing
def test_configure_smart_state(api, validator):
    try:
        assert is_valid_configure_smart_state(
            validator,
            configure_smart_state(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def configure_smart_state_default(api):
    endpoint_result = api.licensing.configure_smart_state(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.licensing
def test_configure_smart_state_default(api, validator):
    try:
        assert is_valid_configure_smart_state(
            validator,
            configure_smart_state_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_registration_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_fb4dcfcdb3e3528380bcc644fa9656b5_v3_3_patch_1').validate(obj.response)
    return True


def get_registration_info(api):
    endpoint_result = api.licensing.get_registration_info(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_registration_info(api, validator):
    try:
        assert is_valid_get_registration_info(
            validator,
            get_registration_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_registration_info_default(api):
    endpoint_result = api.licensing.get_registration_info(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_registration_info_default(api, validator):
    try:
        assert is_valid_get_registration_info(
            validator,
            get_registration_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_registration_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8ef3dd04312255cc9b5605141bf8fd03_v3_3_patch_1').validate(obj.response)
    return True


def create_registration_info(api):
    endpoint_result = api.licensing.create_registration_info(
        active_validation=False,
        connection_type='string',
        payload=None,
        registration_type='string',
        ssm_on_prem_server='string',
        tier=['string'],
        token='string'
    )
    return endpoint_result


@pytest.mark.licensing
def test_create_registration_info(api, validator):
    try:
        assert is_valid_create_registration_info(
            validator,
            create_registration_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_registration_info_default(api):
    endpoint_result = api.licensing.create_registration_info(
        active_validation=False,
        connection_type=None,
        payload=None,
        registration_type=None,
        ssm_on_prem_server=None,
        tier=None,
        token=None
    )
    return endpoint_result


@pytest.mark.licensing
def test_create_registration_info_default(api, validator):
    try:
        assert is_valid_create_registration_info(
            validator,
            create_registration_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tier_state_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3249312d398d5702ab68df0bbca8520f_v3_3_patch_1').validate(obj.response)
    return True


def get_tier_state_info(api):
    endpoint_result = api.licensing.get_tier_state_info(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_tier_state_info(api, validator):
    try:
        assert is_valid_get_tier_state_info(
            validator,
            get_tier_state_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_tier_state_info_default(api):
    endpoint_result = api.licensing.get_tier_state_info(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_tier_state_info_default(api, validator):
    try:
        assert is_valid_get_tier_state_info(
            validator,
            get_tier_state_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_tier_state_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_98d89f61af725550ba6291585d77463b_v3_3_patch_1').validate(obj.response)
    return True


def update_tier_state_info(api):
    endpoint_result = api.licensing.update_tier_state_info(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.licensing
def test_update_tier_state_info(api, validator):
    try:
        assert is_valid_update_tier_state_info(
            validator,
            update_tier_state_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_tier_state_info_default(api):
    endpoint_result = api.licensing.update_tier_state_info(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.licensing
def test_update_tier_state_info_default(api, validator):
    try:
        assert is_valid_update_tier_state_info(
            validator,
            update_tier_state_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_eval_license_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d7f0e3aa9642540cb8c9c31f95f6c317_v3_3_patch_1').validate(obj.response)
    return True


def get_eval_license_info(api):
    endpoint_result = api.licensing.get_eval_license_info(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_eval_license_info(api, validator):
    try:
        assert is_valid_get_eval_license_info(
            validator,
            get_eval_license_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_eval_license_info_default(api):
    endpoint_result = api.licensing.get_eval_license_info(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_eval_license_info_default(api, validator):
    try:
        assert is_valid_get_eval_license_info(
            validator,
            get_eval_license_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_connection_type(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_10deae9edd2c53f39c64695de70e8120_v3_3_patch_1').validate(obj.response)
    return True


def get_connection_type(api):
    endpoint_result = api.licensing.get_connection_type(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_connection_type(api, validator):
    try:
        assert is_valid_get_connection_type(
            validator,
            get_connection_type(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_connection_type_default(api):
    endpoint_result = api.licensing.get_connection_type(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_connection_type_default(api, validator):
    try:
        assert is_valid_get_connection_type(
            validator,
            get_connection_type_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_feature_to_tier_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d73e6ed50d6d5f10b75c773a1df2fcfd_v3_3_patch_1').validate(obj.response)
    return True


def get_feature_to_tier_mapping(api):
    endpoint_result = api.licensing.get_feature_to_tier_mapping(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_feature_to_tier_mapping(api, validator):
    try:
        assert is_valid_get_feature_to_tier_mapping(
            validator,
            get_feature_to_tier_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_feature_to_tier_mapping_default(api):
    endpoint_result = api.licensing.get_feature_to_tier_mapping(

    )
    return endpoint_result


@pytest.mark.licensing
def test_get_feature_to_tier_mapping_default(api, validator):
    try:
        assert is_valid_get_feature_to_tier_mapping(
            validator,
            get_feature_to_tier_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
