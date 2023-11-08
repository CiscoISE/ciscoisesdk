# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI security_groups API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.2_beta', reason='version does not match')


def is_valid_get_security_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ea658190e73c5ce1b27e7def4aea28e3_v3_2_beta').validate(obj.response)
    return True


def get_security_group_by_id(api):
    endpoint_result = api.security_groups.get_security_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_get_security_group_by_id(api, validator):
    try:
        assert is_valid_get_security_group_by_id(
            validator,
            get_security_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_security_group_by_id_default(api):
    endpoint_result = api.security_groups.get_security_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_get_security_group_by_id_default(api, validator):
    try:
        assert is_valid_get_security_group_by_id(
            validator,
            get_security_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_security_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_42ce666e64a958229cfd8da70945935e_v3_2_beta').validate(obj.response)
    return True


def update_security_group_by_id(api):
    endpoint_result = api.security_groups.update_security_group_by_id(
        active_validation=False,
        default_sgacls=[{}],
        description='string',
        generation_id='string',
        id='string',
        is_read_only=True,
        name='string',
        payload=None,
        propogate_to_apic=True,
        value=0
    )
    return endpoint_result


@pytest.mark.security_groups
def test_update_security_group_by_id(api, validator):
    try:
        assert is_valid_update_security_group_by_id(
            validator,
            update_security_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_security_group_by_id_default(api):
    endpoint_result = api.security_groups.update_security_group_by_id(
        active_validation=False,
        id='string',
        default_sgacls=None,
        description=None,
        generation_id=None,
        is_read_only=None,
        name=None,
        payload=None,
        propogate_to_apic=None,
        value=None
    )
    return endpoint_result


@pytest.mark.security_groups
def test_update_security_group_by_id_default(api, validator):
    try:
        assert is_valid_update_security_group_by_id(
            validator,
            update_security_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_security_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ed2c0f81f4ea5299840089761bfd4f62_v3_2_beta').validate(obj.response)
    return True


def delete_security_group_by_id(api):
    endpoint_result = api.security_groups.delete_security_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_delete_security_group_by_id(api, validator):
    try:
        assert is_valid_delete_security_group_by_id(
            validator,
            delete_security_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_security_group_by_id_default(api):
    endpoint_result = api.security_groups.delete_security_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_delete_security_group_by_id_default(api, validator):
    try:
        assert is_valid_delete_security_group_by_id(
            validator,
            delete_security_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b3c356cfc48a5da4b13b8ecbae5748b7_v3_2_beta').validate(obj.response)
    return True


def get_security_groups(api):
    endpoint_result = api.security_groups.get_security_groups(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_get_security_groups(api, validator):
    try:
        assert is_valid_get_security_groups(
            validator,
            get_security_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_security_groups_default(api):
    endpoint_result = api.security_groups.get_security_groups(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.security_groups
def test_get_security_groups_default(api, validator):
    try:
        assert is_valid_get_security_groups(
            validator,
            get_security_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_security_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1d0290eb241f5bd79221afc8d6cb32da_v3_2_beta').validate(obj.response)
    return True


def create_security_group(api):
    endpoint_result = api.security_groups.create_security_group(
        active_validation=False,
        default_sgacls=[{}],
        description='string',
        generation_id='string',
        is_read_only=True,
        name='string',
        payload=None,
        propogate_to_apic=True,
        value=0
    )
    return endpoint_result


@pytest.mark.security_groups
def test_create_security_group(api, validator):
    try:
        assert is_valid_create_security_group(
            validator,
            create_security_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_security_group_default(api):
    endpoint_result = api.security_groups.create_security_group(
        active_validation=False,
        default_sgacls=None,
        description=None,
        generation_id=None,
        is_read_only=None,
        name=None,
        payload=None,
        propogate_to_apic=None,
        value=None
    )
    return endpoint_result


@pytest.mark.security_groups
def test_create_security_group_default(api, validator):
    try:
        assert is_valid_create_security_group(
            validator,
            create_security_group_default(api)
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
    json_schema_validate('jsd_ad87f41ef4845f19a19bfadac0928ae6_v3_2_beta').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.security_groups.get_version(

    )
    return endpoint_result


@pytest.mark.security_groups
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
    endpoint_result = api.security_groups.get_version(

    )
    return endpoint_result


@pytest.mark.security_groups
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_security_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_742f7bd03a835c95b7a759b39ce7f680_v3_2_beta').validate(obj.response)
    return True


def bulk_request_for_security_group(api):
    endpoint_result = api.security_groups.bulk_request_for_security_group(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_bulk_request_for_security_group(api, validator):
    try:
        assert is_valid_bulk_request_for_security_group(
            validator,
            bulk_request_for_security_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_request_for_security_group_default(api):
    endpoint_result = api.security_groups.bulk_request_for_security_group(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.security_groups
def test_bulk_request_for_security_group_default(api, validator):
    try:
        assert is_valid_bulk_request_for_security_group(
            validator,
            bulk_request_for_security_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_security_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_a3148b789a935070b99caed1e99592cf_v3_2_beta').validate(obj.response)
    return True


def monitor_bulk_status_security_group(api):
    endpoint_result = api.security_groups.monitor_bulk_status_security_group(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_monitor_bulk_status_security_group(api, validator):
    try:
        assert is_valid_monitor_bulk_status_security_group(
            validator,
            monitor_bulk_status_security_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def monitor_bulk_status_security_group_default(api):
    endpoint_result = api.security_groups.monitor_bulk_status_security_group(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.security_groups
def test_monitor_bulk_status_security_group_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_security_group(
            validator,
            monitor_bulk_status_security_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
