# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI aci_bindings API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_aci_bindings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3d1448851f0154d0b6e9c856ec6cc6f0_v3_1_0').validate(obj.response)
    return True


def get_aci_bindings(api):
    endpoint_result = api.aci_bindings.get_aci_bindings(
        filter_by='value1,value2',
        filter_value='value1,value2',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.aci_bindings
def test_get_aci_bindings(api, validator):
    try:
        assert is_valid_get_aci_bindings(
            validator,
            get_aci_bindings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_aci_bindings_default(api):
    endpoint_result = api.aci_bindings.get_aci_bindings(
        filter_by=None,
        filter_value=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.aci_bindings
def test_get_aci_bindings_default(api, validator):
    try:
        assert is_valid_get_aci_bindings(
            validator,
            get_aci_bindings_default(api)
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
    json_schema_validate('jsd_d74b5214bad656c98f21e4968661c3c0_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.aci_bindings.get_version(

    )
    return endpoint_result


@pytest.mark.aci_bindings
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
    endpoint_result = api.aci_bindings.get_version(

    )
    return endpoint_result


@pytest.mark.aci_bindings
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
