# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI node_deployment API fixtures and tests.

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


def is_valid_get_nodes(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_fa838e78175e51b4bcfb0821c19b81b7_v3_0_0').validate(obj.response)
    return True


def get_nodes(api):
    endpoint_result = api.node_deployment.get_nodes(

    )
    return endpoint_result


@pytest.mark.node_deployment
def test_get_nodes(api, validator):
    try:
        assert is_valid_get_nodes(
            validator,
            get_nodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_nodes_default(api):
    endpoint_result = api.node_deployment.get_nodes(

    )
    return endpoint_result


@pytest.mark.node_deployment
def test_get_nodes_default(api, validator):
    try:
        assert is_valid_get_nodes(
            validator,
            get_nodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_register_node(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_e82e46732de25832a543c4640312588c_v3_0_0').validate(obj.response)
    return True


def register_node(api):
    endpoint_result = api.node_deployment.register_node(
        active_validation=False,
        administration={'isEnabled': True, 'role': 'string'},
        fdqn='string',
        general_settings={'monitoring': {'isEnabled': True, 'role': 'string', 'otherMonitoringNode': 'string', 'isMntDedicated': True, 'policyservice': {'enabled': True, 'sessionService': {'isEnabled': True, 'nodegroup': 'string'}, 'enableProfilingService': True, 'enableNACService': True, 'sxpservice': {'isEnabled': True, 'userInterface': 'string'}, 'enableDeviceAdminService': True, 'enablePassiveIdentityService': True}, 'enablePXGrid': True}},
        password='string',
        payload=None,
        profile_configuration={'netflow': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcp': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcpSpan': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'http': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'radius': {'enabled': True, 'description': 'string'}, 'nmap': {'enabled': True, 'description': 'string'}, 'dns': {'enabled': True, 'description': 'string'}, 'snmpQuery': {'enabled': True, 'description': 'string', 'retries': 0, 'timeout': 0, 'eventTimeout': 0}, 'snmpTrap': {'linkTrapQuery': True, 'macTrapQuery': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'activeDirectory': {'enabled': True, 'daysBeforeRescan': 0, 'description': 'string'}, 'pxgrid': {'enabled': True, 'description': 'string'}},
        user_name='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_register_node(api, validator):
    try:
        assert is_valid_register_node(
            validator,
            register_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def register_node_default(api):
    endpoint_result = api.node_deployment.register_node(
        active_validation=False,
        administration=None,
        fdqn=None,
        general_settings=None,
        password=None,
        payload=None,
        profile_configuration=None,
        user_name=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_register_node_default(api, validator):
    try:
        assert is_valid_register_node(
            validator,
            register_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_promote_node(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_42b11e2f1af656bcb5880a7b33720ec5_v3_0_0').validate(obj.response)
    return True


def promote_node(api):
    endpoint_result = api.node_deployment.promote_node(
        active_validation=False,
        payload=None,
        promotion_type='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_promote_node(api, validator):
    try:
        assert is_valid_promote_node(
            validator,
            promote_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def promote_node_default(api):
    endpoint_result = api.node_deployment.promote_node(
        active_validation=False,
        payload=None,
        promotion_type=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_promote_node_default(api, validator):
    try:
        assert is_valid_promote_node(
            validator,
            promote_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_node_details(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_ae8d7c8f33bb52ceb04880845f2f45ba_v3_0_0').validate(obj.response)
    return True


def get_node_details(api):
    endpoint_result = api.node_deployment.get_node_details(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_get_node_details(api, validator):
    try:
        assert is_valid_get_node_details(
            validator,
            get_node_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_node_details_default(api):
    endpoint_result = api.node_deployment.get_node_details(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_get_node_details_default(api, validator):
    try:
        assert is_valid_get_node_details(
            validator,
            get_node_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_node(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_682c1fa3bf115c77be99b602aca1493b_v3_0_0').validate(obj.response)
    return True


def update_node(api):
    endpoint_result = api.node_deployment.update_node(
        active_validation=False,
        general_settings={'monitoring': {'isEnabled': True, 'role': 'string', 'otherMonitoringNode': 'string', 'isMntDedicated': True, 'policyservice': {'enabled': True, 'sessionService': {'isEnabled': True, 'nodegroup': 'string'}, 'enableProfilingService': True, 'enableNACService': True, 'sxpservice': {'isEnabled': True, 'userInterface': 'string'}, 'enableDeviceAdminService': True, 'enablePassiveIdentityService': True}, 'enablePXGrid': True}},
        hostname='string',
        payload=None,
        profile_configuration={'netflow': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcp': {'enabled': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'dhcpSpan': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'http': {'enabled': True, 'interface': 'string', 'description': 'string'}, 'radius': {'enabled': True, 'description': 'string'}, 'nmap': {'enabled': True, 'description': 'string'}, 'dns': {'enabled': True, 'description': 'string'}, 'snmpQuery': {'enabled': True, 'description': 'string', 'retries': 0, 'timeout': 0, 'eventTimeout': 0}, 'snmpTrap': {'linkTrapQuery': True, 'macTrapQuery': True, 'interface': 'string', 'port': {}, 'description': 'string'}, 'activeDirectory': {'enabled': True, 'daysBeforeRescan': 0, 'description': 'string'}, 'pxgrid': {'enabled': True, 'description': 'string'}}
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_update_node(api, validator):
    try:
        assert is_valid_update_node(
            validator,
            update_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_node_default(api):
    endpoint_result = api.node_deployment.update_node(
        active_validation=False,
        hostname='string',
        general_settings=None,
        payload=None,
        profile_configuration=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_update_node_default(api, validator):
    try:
        assert is_valid_update_node(
            validator,
            update_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_node(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_161d26670a205a78800cb50673027a6e_v3_0_0').validate(obj.response)
    return True


def delete_node(api):
    endpoint_result = api.node_deployment.delete_node(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_delete_node(api, validator):
    try:
        assert is_valid_delete_node(
            validator,
            delete_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_node_default(api):
    endpoint_result = api.node_deployment.delete_node(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_delete_node_default(api, validator):
    try:
        assert is_valid_delete_node(
            validator,
            delete_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
