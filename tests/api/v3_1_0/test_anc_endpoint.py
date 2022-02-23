# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI anc_endpoint API fixtures and tests.

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


def is_valid_get_anc_endpoint_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5ffbc09a97795b8d872a943895c00345_v3_1_0').validate(obj.response)
    return True


def get_anc_endpoint_by_id(api):
    endpoint_result = api.anc_endpoint.get_anc_endpoint_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_get_anc_endpoint_by_id(api, validator):
    try:
        assert is_valid_get_anc_endpoint_by_id(
            validator,
            get_anc_endpoint_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_anc_endpoint_by_id_default(api):
    endpoint_result = api.anc_endpoint.get_anc_endpoint_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_get_anc_endpoint_by_id_default(api, validator):
    try:
        assert is_valid_get_anc_endpoint_by_id(
            validator,
            get_anc_endpoint_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_clear_anc_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2131fc6670fd50dfb04b1f6b16981256_v3_1_0').validate(obj.response)
    return True


def clear_anc_endpoint(api):
    endpoint_result = api.anc_endpoint.clear_anc_endpoint(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_clear_anc_endpoint(api, validator):
    try:
        assert is_valid_clear_anc_endpoint(
            validator,
            clear_anc_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def clear_anc_endpoint_default(api):
    endpoint_result = api.anc_endpoint.clear_anc_endpoint(
        active_validation=False,
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_clear_anc_endpoint_default(api, validator):
    try:
        assert is_valid_clear_anc_endpoint(
            validator,
            clear_anc_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anc_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_502e681462295b8b8faea9ce6099ff0c_v3_1_0').validate(obj.response)
    return True


def get_anc_endpoint(api):
    endpoint_result = api.anc_endpoint.get_anc_endpoint(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_get_anc_endpoint(api, validator):
    try:
        assert is_valid_get_anc_endpoint(
            validator,
            get_anc_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_anc_endpoint_default(api):
    endpoint_result = api.anc_endpoint.get_anc_endpoint(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_get_anc_endpoint_default(api, validator):
    try:
        assert is_valid_get_anc_endpoint(
            validator,
            get_anc_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_apply_anc_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_136bc936bcb25464b9f3f227647b0443_v3_1_0').validate(obj.response)
    return True


def apply_anc_endpoint(api):
    endpoint_result = api.anc_endpoint.apply_anc_endpoint(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_apply_anc_endpoint(api, validator):
    try:
        assert is_valid_apply_anc_endpoint(
            validator,
            apply_anc_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def apply_anc_endpoint_default(api):
    endpoint_result = api.anc_endpoint.apply_anc_endpoint(
        active_validation=False,
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_apply_anc_endpoint_default(api, validator):
    try:
        assert is_valid_apply_anc_endpoint(
            validator,
            apply_anc_endpoint_default(api)
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
    json_schema_validate('jsd_d5eb6cea45635ef58f5bc624de004f16_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.anc_endpoint.get_version(

    )
    return endpoint_result


@pytest.mark.anc_endpoint
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
    endpoint_result = api.anc_endpoint.get_version(

    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_anc_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5e6167fc5cb6593b8b48429187a26a67_v3_1_0').validate(obj.response)
    return True


def bulk_request_for_anc_endpoint(api):
    endpoint_result = api.anc_endpoint.bulk_request_for_anc_endpoint(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_bulk_request_for_anc_endpoint(api, validator):
    try:
        assert is_valid_bulk_request_for_anc_endpoint(
            validator,
            bulk_request_for_anc_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_request_for_anc_endpoint_default(api):
    endpoint_result = api.anc_endpoint.bulk_request_for_anc_endpoint(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_bulk_request_for_anc_endpoint_default(api, validator):
    try:
        assert is_valid_bulk_request_for_anc_endpoint(
            validator,
            bulk_request_for_anc_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_anc_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0a1c6b9323e55505830673a1819840f3_v3_1_0').validate(obj.response)
    return True


def monitor_bulk_status_anc_endpoint(api):
    endpoint_result = api.anc_endpoint.monitor_bulk_status_anc_endpoint(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_monitor_bulk_status_anc_endpoint(api, validator):
    try:
        assert is_valid_monitor_bulk_status_anc_endpoint(
            validator,
            monitor_bulk_status_anc_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def monitor_bulk_status_anc_endpoint_default(api):
    endpoint_result = api.anc_endpoint.monitor_bulk_status_anc_endpoint(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.anc_endpoint
def test_monitor_bulk_status_anc_endpoint_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_anc_endpoint(
            validator,
            monitor_bulk_status_anc_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
