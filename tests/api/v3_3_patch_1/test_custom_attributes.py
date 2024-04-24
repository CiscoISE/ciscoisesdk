# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI custom_attributes API fixtures and tests.

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


def is_valid_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_70a02a1af2b156c8b040d628e59f86e9_v3_3_patch_1').validate(obj.response)
    return True


def list(api):
    endpoint_result = api.custom_attributes.list(

    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_list(api, validator):
    try:
        assert is_valid_list(
            validator,
            list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def list_default(api):
    endpoint_result = api.custom_attributes.list(

    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_list_default(api, validator):
    try:
        assert is_valid_list(
            validator,
            list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_custom_attribute(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_da31003b02f4519eaa18073aa1b85cee_v3_3_patch_1').validate(obj.response)
    return True


def create_custom_attribute(api):
    endpoint_result = api.custom_attributes.create_custom_attribute(
        active_validation=False,
        attribute_name='string',
        attribute_type='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_create_custom_attribute(api, validator):
    try:
        assert is_valid_create_custom_attribute(
            validator,
            create_custom_attribute(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_custom_attribute_default(api):
    endpoint_result = api.custom_attributes.create_custom_attribute(
        active_validation=False,
        attribute_name=None,
        attribute_type=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_create_custom_attribute_default(api, validator):
    try:
        assert is_valid_create_custom_attribute(
            validator,
            create_custom_attribute_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_rename(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_019ebd4481045cdb92a3d380f1c0237e_v3_3_patch_1').validate(obj.response)
    return True


def rename(api):
    endpoint_result = api.custom_attributes.rename(
        active_validation=False,
        current_name='string',
        new_name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_rename(api, validator):
    try:
        assert is_valid_rename(
            validator,
            rename(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def rename_default(api):
    endpoint_result = api.custom_attributes.rename(
        active_validation=False,
        current_name=None,
        new_name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_rename_default(api, validator):
    try:
        assert is_valid_rename(
            validator,
            rename_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bef8c77f8d035a44a5c250db397dd59a_v3_3_patch_1').validate(obj.response)
    return True


def get(api):
    endpoint_result = api.custom_attributes.get(
        name='string'
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_get(api, validator):
    try:
        assert is_valid_get(
            validator,
            get(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_default(api):
    endpoint_result = api.custom_attributes.get(
        name='string'
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_get_default(api, validator):
    try:
        assert is_valid_get(
            validator,
            get_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bd6f3a50e58459b1b7f735dce452c9b2_v3_3_patch_1').validate(obj.response)
    return True


def delete(api):
    endpoint_result = api.custom_attributes.delete(
        name='string'
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_delete(api, validator):
    try:
        assert is_valid_delete(
            validator,
            delete(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_default(api):
    endpoint_result = api.custom_attributes.delete(
        name='string'
    )
    return endpoint_result


@pytest.mark.custom_attributes
def test_delete_default(api, validator):
    try:
        assert is_valid_delete(
            validator,
            delete_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
