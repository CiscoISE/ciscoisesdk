# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_dictionary_attributes_list API fixtures and tests.

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


def is_valid_get_device_admin_dictionaries_authentication(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7f1ff6e8bb2d5c7fbcf39fbadf5da2d5_v3_0_0').validate(obj.response)
    return True


def get_device_admin_dictionaries_authentication(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_authentication(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_authentication(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_authentication(
            validator,
            get_device_admin_dictionaries_authentication(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_dictionaries_authentication_default(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_authentication(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_authentication_default(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_authentication(
            validator,
            get_device_admin_dictionaries_authentication_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_dictionaries_authorization(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6e2f955f29ce511993a189f2d234048d_v3_0_0').validate(obj.response)
    return True


def get_device_admin_dictionaries_authorization(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_authorization(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_authorization(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_authorization(
            validator,
            get_device_admin_dictionaries_authorization(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_dictionaries_authorization_default(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_authorization(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_authorization_default(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_authorization(
            validator,
            get_device_admin_dictionaries_authorization_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_dictionaries_policyset(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_892e064032895c8098927d3a39ef6af2_v3_0_0').validate(obj.response)
    return True


def get_device_admin_dictionaries_policyset(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_policyset(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_policyset(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_policyset(
            validator,
            get_device_admin_dictionaries_policyset(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_dictionaries_policyset_default(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_policyset(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_policyset_default(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_policyset(
            validator,
            get_device_admin_dictionaries_policyset_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
