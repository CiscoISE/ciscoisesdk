# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI native_supplicant_profile API fixtures and tests.

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


def is_valid_get_native_supplicant_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5d1b9755414c5dcbb61987b2dd06839a_v3_2_beta').validate(obj.response)
    return True


def get_native_supplicant_profile_by_id(api):
    endpoint_result = api.native_supplicant_profile.get_native_supplicant_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_get_native_supplicant_profile_by_id(api, validator):
    try:
        assert is_valid_get_native_supplicant_profile_by_id(
            validator,
            get_native_supplicant_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_native_supplicant_profile_by_id_default(api):
    endpoint_result = api.native_supplicant_profile.get_native_supplicant_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_get_native_supplicant_profile_by_id_default(api, validator):
    try:
        assert is_valid_get_native_supplicant_profile_by_id(
            validator,
            get_native_supplicant_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_native_supplicant_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c54a2ad63f46527dbec140a05f1213b7_v3_2_beta').validate(obj.response)
    return True


def update_native_supplicant_profile_by_id(api):
    endpoint_result = api.native_supplicant_profile.update_native_supplicant_profile_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        wireless_profiles=[{'ssid': 'string', 'allowedProtocol': 'string', 'certificateTemplateId': 'string', 'actionType': 'string', 'previousSsid': 'string'}]
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_update_native_supplicant_profile_by_id(api, validator):
    try:
        assert is_valid_update_native_supplicant_profile_by_id(
            validator,
            update_native_supplicant_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_native_supplicant_profile_by_id_default(api):
    endpoint_result = api.native_supplicant_profile.update_native_supplicant_profile_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        payload=None,
        wireless_profiles=None
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_update_native_supplicant_profile_by_id_default(api, validator):
    try:
        assert is_valid_update_native_supplicant_profile_by_id(
            validator,
            update_native_supplicant_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_native_supplicant_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3fff9d421c78597d98a54dd08a9a99f9_v3_2_beta').validate(obj.response)
    return True


def delete_native_supplicant_profile_by_id(api):
    endpoint_result = api.native_supplicant_profile.delete_native_supplicant_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_delete_native_supplicant_profile_by_id(api, validator):
    try:
        assert is_valid_delete_native_supplicant_profile_by_id(
            validator,
            delete_native_supplicant_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_native_supplicant_profile_by_id_default(api):
    endpoint_result = api.native_supplicant_profile.delete_native_supplicant_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_delete_native_supplicant_profile_by_id_default(api, validator):
    try:
        assert is_valid_delete_native_supplicant_profile_by_id(
            validator,
            delete_native_supplicant_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_native_supplicant_profile(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6470fa9802505d7bbdf85b951581db47_v3_2_beta').validate(obj.response)
    return True


def get_native_supplicant_profile(api):
    endpoint_result = api.native_supplicant_profile.get_native_supplicant_profile(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_get_native_supplicant_profile(api, validator):
    try:
        assert is_valid_get_native_supplicant_profile(
            validator,
            get_native_supplicant_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_native_supplicant_profile_default(api):
    endpoint_result = api.native_supplicant_profile.get_native_supplicant_profile(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_get_native_supplicant_profile_default(api, validator):
    try:
        assert is_valid_get_native_supplicant_profile(
            validator,
            get_native_supplicant_profile_default(api)
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
    json_schema_validate('jsd_f577c55d36b05178b0275dd88c71e118_v3_2_beta').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.native_supplicant_profile.get_version(

    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
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
    endpoint_result = api.native_supplicant_profile.get_version(

    )
    return endpoint_result


@pytest.mark.native_supplicant_profile
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
