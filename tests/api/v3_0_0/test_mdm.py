# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI mdm API fixtures and tests.

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


def is_valid_get_endpoints(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_3f66874f1141550da6104eff5428d37a_v3_0_0').validate(obj.response)
    return True


def get_endpoints(api):
    endpoint_result = api.mdm.get_endpoints(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoints(api, validator):
    try:
        assert is_valid_get_endpoints(
            validator,
            get_endpoints(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_endpoints_default(api):
    endpoint_result = api.mdm.get_endpoints(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoints_default(api, validator):
    try:
        assert is_valid_get_endpoints(
            validator,
            get_endpoints_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoint_by_mac_address(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_6419150c239256209b64afc9e5522e11_v3_0_0').validate(obj.response)
    return True


def get_endpoint_by_mac_address(api):
    endpoint_result = api.mdm.get_endpoint_by_mac_address(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoint_by_mac_address(api, validator):
    try:
        assert is_valid_get_endpoint_by_mac_address(
            validator,
            get_endpoint_by_mac_address(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_endpoint_by_mac_address_default(api):
    endpoint_result = api.mdm.get_endpoint_by_mac_address(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoint_by_mac_address_default(api, validator):
    try:
        assert is_valid_get_endpoint_by_mac_address(
            validator,
            get_endpoint_by_mac_address_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoints_by_type(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_0239282311e55709895e677699dfc3f7_v3_0_0').validate(obj.response)
    return True


def get_endpoints_by_type(api):
    endpoint_result = api.mdm.get_endpoints_by_type(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoints_by_type(api, validator):
    try:
        assert is_valid_get_endpoints_by_type(
            validator,
            get_endpoints_by_type(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_endpoints_by_type_default(api):
    endpoint_result = api.mdm.get_endpoints_by_type(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoints_by_type_default(api, validator):
    try:
        assert is_valid_get_endpoints_by_type(
            validator,
            get_endpoints_by_type_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoints_by_os_type(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_339bf2a72bc05f5aabd3a79a5188d86a_v3_0_0').validate(obj.response)
    return True


def get_endpoints_by_os_type(api):
    endpoint_result = api.mdm.get_endpoints_by_os_type(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoints_by_os_type(api, validator):
    try:
        assert is_valid_get_endpoints_by_os_type(
            validator,
            get_endpoints_by_os_type(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_endpoints_by_os_type_default(api):
    endpoint_result = api.mdm.get_endpoints_by_os_type(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.mdm
def test_get_endpoints_by_os_type_default(api, validator):
    try:
        assert is_valid_get_endpoints_by_os_type(
            validator,
            get_endpoints_by_os_type_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
