# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI acisettings API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.5.0', reason='version does not match')


def is_valid_get_aci_settings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_aci_settings(api):
    endpoint_result = api.acisettings.get_aci_settings(
    )
    return endpoint_result


@pytest.mark.acisettings
def test_get_aci_settings(api, validator):
    try:
        assert is_valid_get_aci_settings(
            validator,
            get_aci_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_aci_settings_default(api):
    endpoint_result = api.acisettings.get_aci_settings(
    )
    return endpoint_result


@pytest.mark.acisettings
def test_get_aci_settings_default(api, validator):
    try:
        assert is_valid_get_aci_settings(
            validator,
            get_aci_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_test_aci_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def test_aci_connection(api):
    endpoint_result = api.acisettings.test_aci_connection(
    )
    return endpoint_result


@pytest.mark.acisettings
def test_test_aci_connection(api, validator):
    try:
        assert is_valid_test_aci_connection(
            validator,
            test_aci_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def test_aci_connection_default(api):
    endpoint_result = api.acisettings.test_aci_connection(
    )
    return endpoint_result


@pytest.mark.acisettings
def test_test_aci_connection_default(api, validator):
    try:
        assert is_valid_test_aci_connection(
            validator,
            test_aci_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def update(api):
    endpoint_result = api.acisettings.update(
    )
    return endpoint_result


@pytest.mark.acisettings
def test_update(api, validator):
    try:
        assert is_valid_update(
            validator,
            update(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_default(api):
    endpoint_result = api.acisettings.update(
    )
    return endpoint_result


@pytest.mark.acisettings
def test_update_default(api, validator):
    try:
        assert is_valid_update(
            validator,
            update_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


