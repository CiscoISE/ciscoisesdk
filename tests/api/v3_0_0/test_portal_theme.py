# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI portal_theme API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_portal_theme_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6e58eabefef15feb880ecfe2906d805f_v3_0_0').validate(obj.response)
    return True


def get_portal_theme_by_id(api):
    endpoint_result = api.portal_theme.get_portal_theme_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_get_portal_theme_by_id(api, validator):
    try:
        assert is_valid_get_portal_theme_by_id(
            validator,
            get_portal_theme_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_portal_theme_by_id_default(api):
    endpoint_result = api.portal_theme.get_portal_theme_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_get_portal_theme_by_id_default(api, validator):
    try:
        assert is_valid_get_portal_theme_by_id(
            validator,
            get_portal_theme_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_portal_theme_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c82dcf6f2c3d5d399045050b02208db2_v3_0_0').validate(obj.response)
    return True


def update_portal_theme_by_id(api):
    endpoint_result = api.portal_theme.update_portal_theme_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        theme_data='string'
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_update_portal_theme_by_id(api, validator):
    try:
        assert is_valid_update_portal_theme_by_id(
            validator,
            update_portal_theme_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_portal_theme_by_id_default(api):
    endpoint_result = api.portal_theme.update_portal_theme_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        payload=None,
        theme_data=None
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_update_portal_theme_by_id_default(api, validator):
    try:
        assert is_valid_update_portal_theme_by_id(
            validator,
            update_portal_theme_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_portal_theme_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8567c39e537955888cc23e4f90e6449b_v3_0_0').validate(obj.response)
    return True


def delete_portal_theme_by_id(api):
    endpoint_result = api.portal_theme.delete_portal_theme_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_delete_portal_theme_by_id(api, validator):
    try:
        assert is_valid_delete_portal_theme_by_id(
            validator,
            delete_portal_theme_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_portal_theme_by_id_default(api):
    endpoint_result = api.portal_theme.delete_portal_theme_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_delete_portal_theme_by_id_default(api, validator):
    try:
        assert is_valid_delete_portal_theme_by_id(
            validator,
            delete_portal_theme_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_portal_themes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_5ad233598ed75e0c97ddd3c3f1af50e4_v3_0_0').validate(obj.response)
    return True


def get_portal_themes(api):
    endpoint_result = api.portal_theme.get_portal_themes(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_get_portal_themes(api, validator):
    try:
        assert is_valid_get_portal_themes(
            validator,
            get_portal_themes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_portal_themes_default(api):
    endpoint_result = api.portal_theme.get_portal_themes(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_get_portal_themes_default(api, validator):
    try:
        assert is_valid_get_portal_themes(
            validator,
            get_portal_themes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_portal_theme(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_91eb833980f55025bfacbfcb8de814c8_v3_0_0').validate(obj.response)
    return True


def create_portal_theme(api):
    endpoint_result = api.portal_theme.create_portal_theme(
        active_validation=False,
        description='string',
        name='string',
        payload=None,
        theme_data='string'
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_create_portal_theme(api, validator):
    try:
        assert is_valid_create_portal_theme(
            validator,
            create_portal_theme(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_portal_theme_default(api):
    endpoint_result = api.portal_theme.create_portal_theme(
        active_validation=False,
        description=None,
        name=None,
        payload=None,
        theme_data=None
    )
    return endpoint_result


@pytest.mark.portal_theme
def test_create_portal_theme_default(api, validator):
    try:
        assert is_valid_create_portal_theme(
            validator,
            create_portal_theme_default(api)
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
    json_schema_validate('jsd_b6bf4f02759a5e7f968896a30575e4c6_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.portal_theme.get_version(

    )
    return endpoint_result


@pytest.mark.portal_theme
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
    endpoint_result = api.portal_theme.get_version(

    )
    return endpoint_result


@pytest.mark.portal_theme
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
