# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI node_services API fixtures and tests.

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


def is_valid_get_interfaces(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f6f429e124ea58ba85f0b34296d61300_v3_1_patch_1').validate(obj.response)
    return True


def get_interfaces(api):
    endpoint_result = api.node_services.get_interfaces(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_services
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
    endpoint_result = api.node_services.get_interfaces(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_services
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
    json_schema_validate('jsd_86620252ba4b550caf3845b4cbe1074d_v3_1_patch_1').validate(obj.response)
    return True


def get_sxp_interface(api):
    endpoint_result = api.node_services.get_sxp_interface(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_services
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
    endpoint_result = api.node_services.get_sxp_interface(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_services
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
    json_schema_validate('jsd_6c6d188a13915253869849c4b0be7759_v3_1_patch_1').validate(obj.response)
    return True


def set_sxp_interface(api):
    endpoint_result = api.node_services.set_sxp_interface(
        active_validation=False,
        hostname='string',
        interface='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.node_services
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
    endpoint_result = api.node_services.set_sxp_interface(
        active_validation=False,
        hostname='string',
        interface=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_services
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
    json_schema_validate('jsd_94bfa308ed7b5fb6acde734f6267b4e3_v3_1_patch_1').validate(obj.response)
    return True


def get_profiler_probe_config(api):
    endpoint_result = api.node_services.get_profiler_probe_config(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_services
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
    endpoint_result = api.node_services.get_profiler_probe_config(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_services
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
    json_schema_validate('jsd_bba25b96ab6c5a99a7e7933a1ef71977_v3_1_patch_1').validate(obj.response)
    return True


def set_profiler_probe_config(api):
    endpoint_result = api.node_services.set_profiler_probe_config(
        active_directory={'daysBeforeRescan': 0},
        active_validation=False,
        dhcp={'interfaces': [{'interface': 'string'}], 'port': 0},
        dhcp_span={'interfaces': [{'interface': 'string'}]},
        dns={'timeout': 0},
        hostname='string',
        http={'interfaces': [{'interface': 'string'}]},
        netflow={'interfaces': [{'interface': 'string'}], 'port': 0},
        nmap=[{}],
        payload=None,
        pxgrid=[{}],
        radius=[{}],
        snmp_query={'eventTimeout': 0, 'retries': 0, 'timeout': 0},
        snmp_trap={'interfaces': [{'interface': 'string'}], 'linkTrapQuery': True, 'macTrapQuery': True, 'port': 0}
    )
    return endpoint_result


@pytest.mark.node_services
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
    endpoint_result = api.node_services.set_profiler_probe_config(
        active_validation=False,
        hostname='string',
        active_directory=None,
        dhcp=None,
        dhcp_span=None,
        dns=None,
        http=None,
        netflow=None,
        nmap=None,
        payload=None,
        pxgrid=None,
        radius=None,
        snmp_query=None,
        snmp_trap=None
    )
    return endpoint_result


@pytest.mark.node_services
def test_set_profiler_probe_config_default(api, validator):
    try:
        assert is_valid_set_profiler_probe_config(
            validator,
            set_profiler_probe_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
