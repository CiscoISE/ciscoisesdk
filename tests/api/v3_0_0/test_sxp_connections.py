# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sxp_connections API fixtures and tests.

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


def is_valid_get_sxp_connections_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_86a5b160a5675039b7ddf3dc960c7968_v3_0_0').validate(obj.response)
    return True


def get_sxp_connections_by_id(api):
    endpoint_result = api.sxp_connections.get_sxp_connections_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_get_sxp_connections_by_id(api, validator):
    try:
        assert is_valid_get_sxp_connections_by_id(
            validator,
            get_sxp_connections_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sxp_connections_by_id_default(api):
    endpoint_result = api.sxp_connections.get_sxp_connections_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_get_sxp_connections_by_id_default(api, validator):
    try:
        assert is_valid_get_sxp_connections_by_id(
            validator,
            get_sxp_connections_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sxp_connections_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1cab8440e21553c3a807d23d05e5e1aa_v3_0_0').validate(obj.response)
    return True


def update_sxp_connections_by_id(api):
    endpoint_result = api.sxp_connections.update_sxp_connections_by_id(
        active_validation=False,
        description='string',
        enabled=True,
        id='string',
        ip_address='string',
        payload=None,
        sxp_mode='string',
        sxp_node='string',
        sxp_peer='string',
        sxp_version='string',
        sxp_vpn='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_update_sxp_connections_by_id(api, validator):
    try:
        assert is_valid_update_sxp_connections_by_id(
            validator,
            update_sxp_connections_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_sxp_connections_by_id_default(api):
    endpoint_result = api.sxp_connections.update_sxp_connections_by_id(
        active_validation=False,
        id='string',
        description=None,
        enabled=None,
        ip_address=None,
        payload=None,
        sxp_mode=None,
        sxp_node=None,
        sxp_peer=None,
        sxp_version=None,
        sxp_vpn=None
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_update_sxp_connections_by_id_default(api, validator):
    try:
        assert is_valid_update_sxp_connections_by_id(
            validator,
            update_sxp_connections_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sxp_connections_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_65954377fb665776b98ba815b52515a6_v3_0_0').validate(obj.response)
    return True


def delete_sxp_connections_by_id(api):
    endpoint_result = api.sxp_connections.delete_sxp_connections_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_delete_sxp_connections_by_id(api, validator):
    try:
        assert is_valid_delete_sxp_connections_by_id(
            validator,
            delete_sxp_connections_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_sxp_connections_by_id_default(api):
    endpoint_result = api.sxp_connections.delete_sxp_connections_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_delete_sxp_connections_by_id_default(api, validator):
    try:
        assert is_valid_delete_sxp_connections_by_id(
            validator,
            delete_sxp_connections_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sxp_connections(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7c56dfcff6285f9b882c884873d5d6c1_v3_0_0').validate(obj.response)
    return True


def get_sxp_connections(api):
    endpoint_result = api.sxp_connections.get_sxp_connections(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_get_sxp_connections(api, validator):
    try:
        assert is_valid_get_sxp_connections(
            validator,
            get_sxp_connections(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sxp_connections_default(api):
    endpoint_result = api.sxp_connections.get_sxp_connections(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_get_sxp_connections_default(api, validator):
    try:
        assert is_valid_get_sxp_connections(
            validator,
            get_sxp_connections_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sxp_connections(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_789c371214c759f791c0a522b9eaf5b5_v3_0_0').validate(obj.response)
    return True


def create_sxp_connections(api):
    endpoint_result = api.sxp_connections.create_sxp_connections(
        active_validation=False,
        description='string',
        enabled=True,
        ip_address='string',
        payload=None,
        sxp_mode='string',
        sxp_node='string',
        sxp_peer='string',
        sxp_version='string',
        sxp_vpn='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_create_sxp_connections(api, validator):
    try:
        assert is_valid_create_sxp_connections(
            validator,
            create_sxp_connections(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_sxp_connections_default(api):
    endpoint_result = api.sxp_connections.create_sxp_connections(
        active_validation=False,
        description=None,
        enabled=None,
        ip_address=None,
        payload=None,
        sxp_mode=None,
        sxp_node=None,
        sxp_peer=None,
        sxp_version=None,
        sxp_vpn=None
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_create_sxp_connections_default(api, validator):
    try:
        assert is_valid_create_sxp_connections(
            validator,
            create_sxp_connections_default(api)
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
    json_schema_validate('jsd_c1ceea62877152f6a4cf7ce709f4d0f8_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.sxp_connections.get_version(

    )
    return endpoint_result


@pytest.mark.sxp_connections
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
    endpoint_result = api.sxp_connections.get_version(

    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_sxp_connections(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e390313557e95aa9b8c2453d6f1de1e8_v3_0_0').validate(obj.response)
    return True


def bulk_request_for_sxp_connections(api):
    endpoint_result = api.sxp_connections.bulk_request_for_sxp_connections(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_bulk_request_for_sxp_connections(api, validator):
    try:
        assert is_valid_bulk_request_for_sxp_connections(
            validator,
            bulk_request_for_sxp_connections(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_request_for_sxp_connections_default(api):
    endpoint_result = api.sxp_connections.bulk_request_for_sxp_connections(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_bulk_request_for_sxp_connections_default(api, validator):
    try:
        assert is_valid_bulk_request_for_sxp_connections(
            validator,
            bulk_request_for_sxp_connections_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_sxp_connections(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9462c2fb20ca5eb79facdda896457507_v3_0_0').validate(obj.response)
    return True


def monitor_bulk_status_sxp_connections(api):
    endpoint_result = api.sxp_connections.monitor_bulk_status_sxp_connections(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_monitor_bulk_status_sxp_connections(api, validator):
    try:
        assert is_valid_monitor_bulk_status_sxp_connections(
            validator,
            monitor_bulk_status_sxp_connections(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def monitor_bulk_status_sxp_connections_default(api):
    endpoint_result = api.sxp_connections.monitor_bulk_status_sxp_connections(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.sxp_connections
def test_monitor_bulk_status_sxp_connections_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_sxp_connections(
            validator,
            monitor_bulk_status_sxp_connections_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
