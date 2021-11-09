# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sxp_vpns API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_sxp_vpn_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_cd59f40aa9305587b69944a9c819f7a9_v3_1_0').validate(obj.response)
    return True


def get_sxp_vpn_by_id(api):
    endpoint_result = api.sxp_vpns.get_sxp_vpn_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_get_sxp_vpn_by_id(api, validator):
    try:
        assert is_valid_get_sxp_vpn_by_id(
            validator,
            get_sxp_vpn_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sxp_vpn_by_id_default(api):
    endpoint_result = api.sxp_vpns.get_sxp_vpn_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_get_sxp_vpn_by_id_default(api, validator):
    try:
        assert is_valid_get_sxp_vpn_by_id(
            validator,
            get_sxp_vpn_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sxp_vpn_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_8a0501930cc9517ea1cb4103db6e0af7_v3_1_0').validate(obj.response)
    return True


def delete_sxp_vpn_by_id(api):
    endpoint_result = api.sxp_vpns.delete_sxp_vpn_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_delete_sxp_vpn_by_id(api, validator):
    try:
        assert is_valid_delete_sxp_vpn_by_id(
            validator,
            delete_sxp_vpn_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sxp_vpn_by_id_default(api):
    endpoint_result = api.sxp_vpns.delete_sxp_vpn_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_delete_sxp_vpn_by_id_default(api, validator):
    try:
        assert is_valid_delete_sxp_vpn_by_id(
            validator,
            delete_sxp_vpn_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sxp_vpns(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_2a93d058764b51dc922e41bbe4ff7cd6_v3_1_0').validate(obj.response)
    return True


def get_sxp_vpns(api):
    endpoint_result = api.sxp_vpns.get_sxp_vpns(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_get_sxp_vpns(api, validator):
    try:
        assert is_valid_get_sxp_vpns(
            validator,
            get_sxp_vpns(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sxp_vpns_default(api):
    endpoint_result = api.sxp_vpns.get_sxp_vpns(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_get_sxp_vpns_default(api, validator):
    try:
        assert is_valid_get_sxp_vpns(
            validator,
            get_sxp_vpns_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sxp_vpn(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_1a693347bdd15bb19d69a75f088498ce_v3_1_0').validate(obj.response)
    return True


def create_sxp_vpn(api):
    endpoint_result = api.sxp_vpns.create_sxp_vpn(
        active_validation=False,
        payload=None,
        sxp_vpn_name='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_create_sxp_vpn(api, validator):
    try:
        assert is_valid_create_sxp_vpn(
            validator,
            create_sxp_vpn(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sxp_vpn_default(api):
    endpoint_result = api.sxp_vpns.create_sxp_vpn(
        active_validation=False,
        payload=None,
        sxp_vpn_name=None
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_create_sxp_vpn_default(api, validator):
    try:
        assert is_valid_create_sxp_vpn(
            validator,
            create_sxp_vpn_default(api)
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

    json_schema_validate('jsd_36ca67bf525555b086ecee4cb93e9aee_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.sxp_vpns.get_version(

    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_get_version(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_version_default(api):
    endpoint_result = api.sxp_vpns.get_version(

    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_sxp_vpns(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_2549a746755c588c928d15a59f8a693d_v3_1_0').validate(obj.response)
    return True


def bulk_request_for_sxp_vpns(api):
    endpoint_result = api.sxp_vpns.bulk_request_for_sxp_vpns(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_bulk_request_for_sxp_vpns(api, validator):
    try:
        assert is_valid_bulk_request_for_sxp_vpns(
            validator,
            bulk_request_for_sxp_vpns(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_request_for_sxp_vpns_default(api):
    endpoint_result = api.sxp_vpns.bulk_request_for_sxp_vpns(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_bulk_request_for_sxp_vpns_default(api, validator):
    try:
        assert is_valid_bulk_request_for_sxp_vpns(
            validator,
            bulk_request_for_sxp_vpns_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_sxp_vpns(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_ba771c958ccc5f499c3a819fb2c67f57_v3_1_0').validate(obj.response)
    return True


def monitor_bulk_status_sxp_vpns(api):
    endpoint_result = api.sxp_vpns.monitor_bulk_status_sxp_vpns(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_monitor_bulk_status_sxp_vpns(api, validator):
    try:
        assert is_valid_monitor_bulk_status_sxp_vpns(
            validator,
            monitor_bulk_status_sxp_vpns(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def monitor_bulk_status_sxp_vpns_default(api):
    endpoint_result = api.sxp_vpns.monitor_bulk_status_sxp_vpns(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.sxp_vpns
def test_monitor_bulk_status_sxp_vpns_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_sxp_vpns(
            validator,
            monitor_bulk_status_sxp_vpns_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
