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
from ciscoisesdk.exceptions import ciscoisesdkException
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.1', reason='version does not match')


def is_valid_get_device_admin_dictionaries_authentication(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4f74a3e991b7535e8a810540ef47cfda_v3_1_1').validate(obj.response)
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
            print("ERROR: {error}".format(error=original_e))
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
    json_schema_validate('jsd_ae98c0dfbd8f5c80b62def7cf2fb70e6_v3_1_1').validate(obj.response)
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
            print("ERROR: {error}".format(error=original_e))
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


def is_valid_get_device_admin_dictionaries_policy_set(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1b83a635ff055d7b94d1cce6f0a492ec_v3_1_1').validate(obj.response)
    return True


def get_device_admin_dictionaries_policy_set(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_policy_set(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_policy_set(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_policy_set(
            validator,
            get_device_admin_dictionaries_policy_set(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_admin_dictionaries_policy_set_default(api):
    endpoint_result = api.device_administration_dictionary_attributes_list.get_device_admin_dictionaries_policy_set(

    )
    return endpoint_result


@pytest.mark.device_administration_dictionary_attributes_list
def test_get_device_admin_dictionaries_policy_set_default(api, validator):
    try:
        assert is_valid_get_device_admin_dictionaries_policy_set(
            validator,
            get_device_admin_dictionaries_policy_set_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
