# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI certificate_profile API fixtures and tests.

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


def is_valid_get_certificate_profile_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_337e7884eb9c548698cdc54e033f35f4_v3_0_0').validate(obj.response)
    return True


def get_certificate_profile_by_name(api):
    endpoint_result = api.certificate_profile.get_certificate_profile_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_get_certificate_profile_by_name(api, validator):
    try:
        assert is_valid_get_certificate_profile_by_name(
            validator,
            get_certificate_profile_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_certificate_profile_by_name_default(api):
    endpoint_result = api.certificate_profile.get_certificate_profile_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_get_certificate_profile_by_name_default(api, validator):
    try:
        assert is_valid_get_certificate_profile_by_name(
            validator,
            get_certificate_profile_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_certificate_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d24a3f485ff758d099b1e4713f18f1c1_v3_0_0').validate(obj.response)
    return True


def get_certificate_profile_by_id(api):
    endpoint_result = api.certificate_profile.get_certificate_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_get_certificate_profile_by_id(api, validator):
    try:
        assert is_valid_get_certificate_profile_by_id(
            validator,
            get_certificate_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_certificate_profile_by_id_default(api):
    endpoint_result = api.certificate_profile.get_certificate_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_get_certificate_profile_by_id_default(api, validator):
    try:
        assert is_valid_get_certificate_profile_by_id(
            validator,
            get_certificate_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_certificate_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e09287aba99c56a6a9171b7e3a635a43_v3_0_0').validate(obj.response)
    return True


def update_certificate_profile_by_id(api):
    endpoint_result = api.certificate_profile.update_certificate_profile_by_id(
        active_validation=False,
        allowed_as_user_name=True,
        certificate_attribute_name='string',
        external_identity_store_name='string',
        id='string',
        match_mode='string',
        name='string',
        payload=None,
        username_from='string'
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_update_certificate_profile_by_id(api, validator):
    try:
        assert is_valid_update_certificate_profile_by_id(
            validator,
            update_certificate_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_certificate_profile_by_id_default(api):
    endpoint_result = api.certificate_profile.update_certificate_profile_by_id(
        active_validation=False,
        id='string',
        allowed_as_user_name=None,
        certificate_attribute_name=None,
        external_identity_store_name=None,
        match_mode=None,
        name=None,
        payload=None,
        username_from=None
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_update_certificate_profile_by_id_default(api, validator):
    try:
        assert is_valid_update_certificate_profile_by_id(
            validator,
            update_certificate_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_certificate_profile(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3be38700993b5f70acfdc8e44f5558d8_v3_0_0').validate(obj.response)
    return True


def get_all_certificate_profile(api):
    endpoint_result = api.certificate_profile.get_all_certificate_profile(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_get_all_certificate_profile(api, validator):
    try:
        assert is_valid_get_all_certificate_profile(
            validator,
            get_all_certificate_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_certificate_profile_default(api):
    endpoint_result = api.certificate_profile.get_all_certificate_profile(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_get_all_certificate_profile_default(api, validator):
    try:
        assert is_valid_get_all_certificate_profile(
            validator,
            get_all_certificate_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_certificate_profile(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_776141419f955525b0b38a57a3bed311_v3_0_0').validate(obj.response)
    return True


def create_certificate_profile(api):
    endpoint_result = api.certificate_profile.create_certificate_profile(
        active_validation=False,
        allowed_as_user_name=True,
        certificate_attribute_name='string',
        external_identity_store_name='string',
        id='string',
        match_mode='string',
        name='string',
        payload=None,
        username_from='string'
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_create_certificate_profile(api, validator):
    try:
        assert is_valid_create_certificate_profile(
            validator,
            create_certificate_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_certificate_profile_default(api):
    endpoint_result = api.certificate_profile.create_certificate_profile(
        active_validation=False,
        allowed_as_user_name=None,
        certificate_attribute_name=None,
        external_identity_store_name=None,
        id=None,
        match_mode=None,
        name=None,
        payload=None,
        username_from=None
    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_create_certificate_profile_default(api, validator):
    try:
        assert is_valid_create_certificate_profile(
            validator,
            create_certificate_profile_default(api)
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
    json_schema_validate('jsd_8e00be3b97b85829bef60c09eaa922ac_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.certificate_profile.get_version(

    )
    return endpoint_result


@pytest.mark.certificate_profile
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
    endpoint_result = api.certificate_profile.get_version(

    )
    return endpoint_result


@pytest.mark.certificate_profile
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
