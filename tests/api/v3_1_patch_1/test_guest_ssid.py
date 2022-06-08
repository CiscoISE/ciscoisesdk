# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI guest_ssid API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1_Patch_1', reason='version does not match')


def is_valid_get_guest_ssid_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d5572c56526151cb8ea42de44b2db52c_v3_1_patch_1').validate(obj.response)
    return True


def get_guest_ssid_by_id(api):
    endpoint_result = api.guest_ssid.get_guest_ssid_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_get_guest_ssid_by_id(api, validator):
    try:
        assert is_valid_get_guest_ssid_by_id(
            validator,
            get_guest_ssid_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_guest_ssid_by_id_default(api):
    endpoint_result = api.guest_ssid.get_guest_ssid_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_get_guest_ssid_by_id_default(api, validator):
    try:
        assert is_valid_get_guest_ssid_by_id(
            validator,
            get_guest_ssid_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_ssid_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_72e6e4b7d022556a80f1948efb3d5c61_v3_1_patch_1').validate(obj.response)
    return True


def update_guest_ssid_by_id(api):
    endpoint_result = api.guest_ssid.update_guest_ssid_by_id(
        active_validation=False,
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_update_guest_ssid_by_id(api, validator):
    try:
        assert is_valid_update_guest_ssid_by_id(
            validator,
            update_guest_ssid_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_guest_ssid_by_id_default(api):
    endpoint_result = api.guest_ssid.update_guest_ssid_by_id(
        active_validation=False,
        id='string',
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_update_guest_ssid_by_id_default(api, validator):
    try:
        assert is_valid_update_guest_ssid_by_id(
            validator,
            update_guest_ssid_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_guest_ssid_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8328407df7345f788230a512d6635c25_v3_1_patch_1').validate(obj.response)
    return True


def delete_guest_ssid_by_id(api):
    endpoint_result = api.guest_ssid.delete_guest_ssid_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_delete_guest_ssid_by_id(api, validator):
    try:
        assert is_valid_delete_guest_ssid_by_id(
            validator,
            delete_guest_ssid_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_guest_ssid_by_id_default(api):
    endpoint_result = api.guest_ssid.delete_guest_ssid_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_delete_guest_ssid_by_id_default(api, validator):
    try:
        assert is_valid_delete_guest_ssid_by_id(
            validator,
            delete_guest_ssid_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_guest_ssid(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c37778a2faa5552894cc60cec13c56c7_v3_1_patch_1').validate(obj.response)
    return True


def get_guest_ssid(api):
    endpoint_result = api.guest_ssid.get_guest_ssid(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_get_guest_ssid(api, validator):
    try:
        assert is_valid_get_guest_ssid(
            validator,
            get_guest_ssid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_guest_ssid_default(api):
    endpoint_result = api.guest_ssid.get_guest_ssid(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_get_guest_ssid_default(api, validator):
    try:
        assert is_valid_get_guest_ssid(
            validator,
            get_guest_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_guest_ssid(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2a31eb33e3535754b3f754a9199e0d25_v3_1_patch_1').validate(obj.response)
    return True


def create_guest_ssid(api):
    endpoint_result = api.guest_ssid.create_guest_ssid(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_create_guest_ssid(api, validator):
    try:
        assert is_valid_create_guest_ssid(
            validator,
            create_guest_ssid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_guest_ssid_default(api):
    endpoint_result = api.guest_ssid.create_guest_ssid(
        active_validation=False,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_create_guest_ssid_default(api, validator):
    try:
        assert is_valid_create_guest_ssid(
            validator,
            create_guest_ssid_default(api)
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
    json_schema_validate('jsd_b400ebaa2d1f51398d3b32e7a6e4ba35_v3_1_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.guest_ssid.get_version(

    )
    return endpoint_result


@pytest.mark.guest_ssid
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
    endpoint_result = api.guest_ssid.get_version(

    )
    return endpoint_result


@pytest.mark.guest_ssid
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
