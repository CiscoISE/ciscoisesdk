# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_dictionary_attribute API fixtures and tests.

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


def is_valid_create_network_access_dictionary_attribute_for_dictionary(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_706f4508bb3352ff920dbdc229e0fc50_v3_0_0').validate(obj.response)
    return True


def create_network_access_dictionary_attribute_for_dictionary(api):
    endpoint_result = api.network_access_dictionary_attribute.create_network_access_dictionary_attribute_for_dictionary(
        active_validation=False,
        allowed_values=[{'key': 'string', 'value': 'string', 'isDefault': True}],
        data_type='string',
        description='string',
        dictionary_name='string',
        direction_type='string',
        id='string',
        internal_name='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_create_network_access_dictionary_attribute_for_dictionary(api, validator):
    try:
        assert is_valid_create_network_access_dictionary_attribute_for_dictionary(
            validator,
            create_network_access_dictionary_attribute_for_dictionary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_access_dictionary_attribute_for_dictionary_default(api):
    endpoint_result = api.network_access_dictionary_attribute.create_network_access_dictionary_attribute_for_dictionary(
        active_validation=False,
        dictionary_name='string',
        allowed_values=None,
        data_type=None,
        description=None,
        direction_type=None,
        id=None,
        internal_name=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_create_network_access_dictionary_attribute_for_dictionary_default(api, validator):
    try:
        assert is_valid_create_network_access_dictionary_attribute_for_dictionary(
            validator,
            create_network_access_dictionary_attribute_for_dictionary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_dictionary_attribute_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0462fbd7ec7052709e5d0e0a46dc7f68_v3_0_0').validate(obj.response)
    return True


def get_network_access_dictionary_attribute_by_name(api):
    endpoint_result = api.network_access_dictionary_attribute.get_network_access_dictionary_attribute_by_name(
        attribute_name='string',
        dictionary_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_get_network_access_dictionary_attribute_by_name(api, validator):
    try:
        assert is_valid_get_network_access_dictionary_attribute_by_name(
            validator,
            get_network_access_dictionary_attribute_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_dictionary_attribute_by_name_default(api):
    endpoint_result = api.network_access_dictionary_attribute.get_network_access_dictionary_attribute_by_name(
        attribute_name='string',
        dictionary_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_get_network_access_dictionary_attribute_by_name_default(api, validator):
    try:
        assert is_valid_get_network_access_dictionary_attribute_by_name(
            validator,
            get_network_access_dictionary_attribute_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_dictionary_attribute_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_fda64cd1ab7d53448962f61de0f76948_v3_0_0').validate(obj.response)
    return True


def update_network_access_dictionary_attribute_by_name(api):
    endpoint_result = api.network_access_dictionary_attribute.update_network_access_dictionary_attribute_by_name(
        active_validation=False,
        allowed_values=[{'key': 'string', 'value': 'string', 'isDefault': True}],
        attribute_name='string',
        data_type='string',
        description='string',
        dictionary_name='string',
        direction_type='string',
        id='string',
        internal_name='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_update_network_access_dictionary_attribute_by_name(api, validator):
    try:
        assert is_valid_update_network_access_dictionary_attribute_by_name(
            validator,
            update_network_access_dictionary_attribute_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_access_dictionary_attribute_by_name_default(api):
    endpoint_result = api.network_access_dictionary_attribute.update_network_access_dictionary_attribute_by_name(
        active_validation=False,
        attribute_name='string',
        dictionary_name='string',
        allowed_values=None,
        data_type=None,
        description=None,
        direction_type=None,
        id=None,
        internal_name=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_update_network_access_dictionary_attribute_by_name_default(api, validator):
    try:
        assert is_valid_update_network_access_dictionary_attribute_by_name(
            validator,
            update_network_access_dictionary_attribute_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_dictionary_attribute_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_15257c813c9b5a73b6d00cac1ca5a41f_v3_0_0').validate(obj.response)
    return True


def delete_network_access_dictionary_attribute_by_name(api):
    endpoint_result = api.network_access_dictionary_attribute.delete_network_access_dictionary_attribute_by_name(
        attribute_name='string',
        dictionary_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_delete_network_access_dictionary_attribute_by_name(api, validator):
    try:
        assert is_valid_delete_network_access_dictionary_attribute_by_name(
            validator,
            delete_network_access_dictionary_attribute_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_dictionary_attribute_by_name_default(api):
    endpoint_result = api.network_access_dictionary_attribute.delete_network_access_dictionary_attribute_by_name(
        attribute_name='string',
        dictionary_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_delete_network_access_dictionary_attribute_by_name_default(api, validator):
    try:
        assert is_valid_delete_network_access_dictionary_attribute_by_name(
            validator,
            delete_network_access_dictionary_attribute_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
