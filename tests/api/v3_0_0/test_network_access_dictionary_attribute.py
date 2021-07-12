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


def is_valid_get_network_access_dictionary_attributes_by_dictionary_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d83302be1f7c528e8211524aeaacd66d_v3_0_0').validate(obj.response)
    return True


def get_network_access_dictionary_attributes_by_dictionary_name(api):
    endpoint_result = api.network_access_dictionary_attribute.get_network_access_dictionary_attributes_by_dictionary_name(
        dictionary_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_get_network_access_dictionary_attributes_by_dictionary_name(api, validator):
    try:
        assert is_valid_get_network_access_dictionary_attributes_by_dictionary_name(
            validator,
            get_network_access_dictionary_attributes_by_dictionary_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_dictionary_attributes_by_dictionary_name_default(api):
    endpoint_result = api.network_access_dictionary_attribute.get_network_access_dictionary_attributes_by_dictionary_name(
        dictionary_name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_get_network_access_dictionary_attributes_by_dictionary_name_default(api, validator):
    try:
        assert is_valid_get_network_access_dictionary_attributes_by_dictionary_name(
            validator,
            get_network_access_dictionary_attributes_by_dictionary_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_post_network_access_dictionaries_by_dictionary_name_attribute(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_706f4508bb3352ff920dbdc229e0fc50_v3_0_0').validate(obj.response)
    return True


def post_network_access_dictionaries_by_dictionary_name_attribute(api):
    endpoint_result = api.network_access_dictionary_attribute.post_network_access_dictionaries_by_dictionary_name_attribute(
        active_validation=False,
        allowed_values=[{'isDefault': True, 'key': 'string', 'value': 'string'}],
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
def test_post_network_access_dictionaries_by_dictionary_name_attribute(api, validator):
    try:
        assert is_valid_post_network_access_dictionaries_by_dictionary_name_attribute(
            validator,
            post_network_access_dictionaries_by_dictionary_name_attribute(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def post_network_access_dictionaries_by_dictionary_name_attribute_default(api):
    endpoint_result = api.network_access_dictionary_attribute.post_network_access_dictionaries_by_dictionary_name_attribute(
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
def test_post_network_access_dictionaries_by_dictionary_name_attribute_default(api, validator):
    try:
        assert is_valid_post_network_access_dictionaries_by_dictionary_name_attribute(
            validator,
            post_network_access_dictionaries_by_dictionary_name_attribute_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c77600d349fc5c259dbd22d65b3ffa1d_v3_0_0').validate(obj.response)
    return True


def get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api):
    endpoint_result = api.network_access_dictionary_attribute.get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
        dictionary_name='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api, validator):
    try:
        assert is_valid_get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
            validator,
            get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api):
    endpoint_result = api.network_access_dictionary_attribute.get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
        dictionary_name='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api, validator):
    try:
        assert is_valid_get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
            validator,
            get_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a60b29bfe2b055299e4360d84380ddd4_v3_0_0').validate(obj.response)
    return True


def put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api):
    endpoint_result = api.network_access_dictionary_attribute.put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
        active_validation=False,
        allowed_values=[{'isDefault': True, 'key': 'string', 'value': 'string'}],
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
def test_put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api, validator):
    try:
        assert is_valid_put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
            validator,
            put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api):
    endpoint_result = api.network_access_dictionary_attribute.put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
        active_validation=False,
        dictionary_name='string',
        name='string',
        allowed_values=None,
        data_type=None,
        description=None,
        direction_type=None,
        id=None,
        internal_name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api, validator):
    try:
        assert is_valid_put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
            validator,
            put_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_dd6c2553ae0053c1bbbdbd46c1df0ef9_v3_0_0').validate(obj.response)
    return True


def delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api):
    endpoint_result = api.network_access_dictionary_attribute.delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
        dictionary_name='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api, validator):
    try:
        assert is_valid_delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
            validator,
            delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api):
    endpoint_result = api.network_access_dictionary_attribute.delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
        dictionary_name='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary_attribute
def test_delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api, validator):
    try:
        assert is_valid_delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name(
            validator,
            delete_network_access_dictionaries_by_dictionary_name_attribute_by_attribute_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
