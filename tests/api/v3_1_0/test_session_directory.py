# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI session_directory API fixtures and tests.

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


def is_valid_get_sessions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9a86b36d56165904911f133e10d4f955_v3_0_0').validate(obj.response)
    return True


def get_sessions(api):
    endpoint_result = api.session_directory.get_sessions(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_sessions(api, validator):
    try:
        assert is_valid_get_sessions(
            validator,
            get_sessions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sessions_default(api):
    endpoint_result = api.session_directory.get_sessions(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_sessions_default(api, validator):
    try:
        assert is_valid_get_sessions(
            validator,
            get_sessions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sessions_for_recovery(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_12d6da2024445b2cb8a146fe19889e71_v3_0_0').validate(obj.response)
    return True


def get_sessions_for_recovery(api):
    endpoint_result = api.session_directory.get_sessions_for_recovery(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_sessions_for_recovery(api, validator):
    try:
        assert is_valid_get_sessions_for_recovery(
            validator,
            get_sessions_for_recovery(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sessions_for_recovery_default(api):
    endpoint_result = api.session_directory.get_sessions_for_recovery(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_sessions_for_recovery_default(api, validator):
    try:
        assert is_valid_get_sessions_for_recovery(
            validator,
            get_sessions_for_recovery_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_session_by_ip_address(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2515a470322e5500949321c2cbc1b9c9_v3_0_0').validate(obj.response)
    return True


def get_session_by_ip_address(api):
    endpoint_result = api.session_directory.get_session_by_ip_address(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_session_by_ip_address(api, validator):
    try:
        assert is_valid_get_session_by_ip_address(
            validator,
            get_session_by_ip_address(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_session_by_ip_address_default(api):
    endpoint_result = api.session_directory.get_session_by_ip_address(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_session_by_ip_address_default(api, validator):
    try:
        assert is_valid_get_session_by_ip_address(
            validator,
            get_session_by_ip_address_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_session_by_mac_address(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e564f3d00647543db29d1ca6865bc8d0_v3_0_0').validate(obj.response)
    return True


def get_session_by_mac_address(api):
    endpoint_result = api.session_directory.get_session_by_mac_address(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_session_by_mac_address(api, validator):
    try:
        assert is_valid_get_session_by_mac_address(
            validator,
            get_session_by_mac_address(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_session_by_mac_address_default(api):
    endpoint_result = api.session_directory.get_session_by_mac_address(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_session_by_mac_address_default(api, validator):
    try:
        assert is_valid_get_session_by_mac_address(
            validator,
            get_session_by_mac_address_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_user_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f8021c1d176c5de9b8b41dcde0f0268e_v3_0_0').validate(obj.response)
    return True


def get_user_groups(api):
    endpoint_result = api.session_directory.get_user_groups(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_user_groups(api, validator):
    try:
        assert is_valid_get_user_groups(
            validator,
            get_user_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_user_groups_default(api):
    endpoint_result = api.session_directory.get_user_groups(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_user_groups_default(api, validator):
    try:
        assert is_valid_get_user_groups(
            validator,
            get_user_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_user_group_by_user_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1f674031faf65cac8e2f5581bdef4788_v3_0_0').validate(obj.response)
    return True


def get_user_group_by_user_name(api):
    endpoint_result = api.session_directory.get_user_group_by_user_name(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_user_group_by_user_name(api, validator):
    try:
        assert is_valid_get_user_group_by_user_name(
            validator,
            get_user_group_by_user_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_user_group_by_user_name_default(api):
    endpoint_result = api.session_directory.get_user_group_by_user_name(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.session_directory
def test_get_user_group_by_user_name_default(api, validator):
    try:
        assert is_valid_get_user_group_by_user_name(
            validator,
            get_user_group_by_user_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e