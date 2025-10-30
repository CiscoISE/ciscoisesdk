# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI nodeservices API fixtures and tests.

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


def is_valid_get_interfaces(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_interfaces(api):
    endpoint_result = api.nodeservices.get_interfaces(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_get_interfaces(api, validator):
    try:
        assert is_valid_get_interfaces(
            validator,
            get_interfaces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_interfaces_default(api):
    endpoint_result = api.nodeservices.get_interfaces(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_get_interfaces_default(api, validator):
    try:
        assert is_valid_get_interfaces(
            validator,
            get_interfaces_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sxp_interface(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_sxp_interface(api):
    endpoint_result = api.nodeservices.get_sxp_interface(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_get_sxp_interface(api, validator):
    try:
        assert is_valid_get_sxp_interface(
            validator,
            get_sxp_interface(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sxp_interface_default(api):
    endpoint_result = api.nodeservices.get_sxp_interface(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_get_sxp_interface_default(api, validator):
    try:
        assert is_valid_get_sxp_interface(
            validator,
            get_sxp_interface_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_sxp_interface(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def set_sxp_interface(api):
    endpoint_result = api.nodeservices.set_sxp_interface(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_set_sxp_interface(api, validator):
    try:
        assert is_valid_set_sxp_interface(
            validator,
            set_sxp_interface(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def set_sxp_interface_default(api):
    endpoint_result = api.nodeservices.set_sxp_interface(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_set_sxp_interface_default(api, validator):
    try:
        assert is_valid_set_sxp_interface(
            validator,
            set_sxp_interface_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_profiler_probe_config(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_profiler_probe_config(api):
    endpoint_result = api.nodeservices.get_profiler_probe_config(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_get_profiler_probe_config(api, validator):
    try:
        assert is_valid_get_profiler_probe_config(
            validator,
            get_profiler_probe_config(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_profiler_probe_config_default(api):
    endpoint_result = api.nodeservices.get_profiler_probe_config(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_get_profiler_probe_config_default(api, validator):
    try:
        assert is_valid_get_profiler_probe_config(
            validator,
            get_profiler_probe_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_profiler_probe_config(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def set_profiler_probe_config(api):
    endpoint_result = api.nodeservices.set_profiler_probe_config(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_set_profiler_probe_config(api, validator):
    try:
        assert is_valid_set_profiler_probe_config(
            validator,
            set_profiler_probe_config(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def set_profiler_probe_config_default(api):
    endpoint_result = api.nodeservices.set_profiler_probe_config(
    )
    return endpoint_result


@pytest.mark.nodeservices
def test_set_profiler_probe_config_default(api, validator):
    try:
        assert is_valid_set_profiler_probe_config(
            validator,
            set_profiler_probe_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


