# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI anc_policy API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.1', reason='version does not match')


def is_valid_get_anc_policy_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_983a095b061f564ebba331f66505b0e3_v3_1_1').validate(obj.response)
    return True


def get_anc_policy_by_name(api):
    endpoint_result = api.anc_policy.get_anc_policy_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_get_anc_policy_by_name(api, validator):
    try:
        assert is_valid_get_anc_policy_by_name(
            validator,
            get_anc_policy_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_anc_policy_by_name_default(api):
    endpoint_result = api.anc_policy.get_anc_policy_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_get_anc_policy_by_name_default(api, validator):
    try:
        assert is_valid_get_anc_policy_by_name(
            validator,
            get_anc_policy_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anc_policy_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f41f77362663580d8cc3e6e88623889d_v3_1_1').validate(obj.response)
    return True


def get_anc_policy_by_id(api):
    endpoint_result = api.anc_policy.get_anc_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_get_anc_policy_by_id(api, validator):
    try:
        assert is_valid_get_anc_policy_by_id(
            validator,
            get_anc_policy_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_anc_policy_by_id_default(api):
    endpoint_result = api.anc_policy.get_anc_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_get_anc_policy_by_id_default(api, validator):
    try:
        assert is_valid_get_anc_policy_by_id(
            validator,
            get_anc_policy_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_anc_policy_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1d79b507bda155c180d42f0a67ef64d5_v3_1_1').validate(obj.response)
    return True


def update_anc_policy_by_id(api):
    endpoint_result = api.anc_policy.update_anc_policy_by_id(
        actions=['string'],
        active_validation=False,
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_update_anc_policy_by_id(api, validator):
    try:
        assert is_valid_update_anc_policy_by_id(
            validator,
            update_anc_policy_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_anc_policy_by_id_default(api):
    endpoint_result = api.anc_policy.update_anc_policy_by_id(
        active_validation=False,
        id='string',
        actions=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_update_anc_policy_by_id_default(api, validator):
    try:
        assert is_valid_update_anc_policy_by_id(
            validator,
            update_anc_policy_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_anc_policy_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7c6b8dd764e052699d4d7a0d8ba43640_v3_1_1').validate(obj.response)
    return True


def delete_anc_policy_by_id(api):
    endpoint_result = api.anc_policy.delete_anc_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_delete_anc_policy_by_id(api, validator):
    try:
        assert is_valid_delete_anc_policy_by_id(
            validator,
            delete_anc_policy_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_anc_policy_by_id_default(api):
    endpoint_result = api.anc_policy.delete_anc_policy_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_delete_anc_policy_by_id_default(api, validator):
    try:
        assert is_valid_delete_anc_policy_by_id(
            validator,
            delete_anc_policy_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_anc_policy(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_440813c9722c56108cac8ca50bf8f01c_v3_1_1').validate(obj.response)
    return True


def get_anc_policy(api):
    endpoint_result = api.anc_policy.get_anc_policy(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_get_anc_policy(api, validator):
    try:
        assert is_valid_get_anc_policy(
            validator,
            get_anc_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_anc_policy_default(api):
    endpoint_result = api.anc_policy.get_anc_policy(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_get_anc_policy_default(api, validator):
    try:
        assert is_valid_get_anc_policy(
            validator,
            get_anc_policy_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_anc_policy(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2acfdb4060de5a1895b383238c205986_v3_1_1').validate(obj.response)
    return True


def create_anc_policy(api):
    endpoint_result = api.anc_policy.create_anc_policy(
        actions=['string'],
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_create_anc_policy(api, validator):
    try:
        assert is_valid_create_anc_policy(
            validator,
            create_anc_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_anc_policy_default(api):
    endpoint_result = api.anc_policy.create_anc_policy(
        active_validation=False,
        actions=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_create_anc_policy_default(api, validator):
    try:
        assert is_valid_create_anc_policy(
            validator,
            create_anc_policy_default(api)
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
    json_schema_validate('jsd_b01a12e2b55e582084fab915465bf962_v3_1_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.anc_policy.get_version(

    )
    return endpoint_result


@pytest.mark.anc_policy
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
    endpoint_result = api.anc_policy.get_version(

    )
    return endpoint_result


@pytest.mark.anc_policy
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_anc_policy(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4d67f9f6fba65dcbbcf64ca3e31b39a6_v3_1_1').validate(obj.response)
    return True


def bulk_request_for_anc_policy(api):
    endpoint_result = api.anc_policy.bulk_request_for_anc_policy(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_bulk_request_for_anc_policy(api, validator):
    try:
        assert is_valid_bulk_request_for_anc_policy(
            validator,
            bulk_request_for_anc_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_request_for_anc_policy_default(api):
    endpoint_result = api.anc_policy.bulk_request_for_anc_policy(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_bulk_request_for_anc_policy_default(api, validator):
    try:
        assert is_valid_bulk_request_for_anc_policy(
            validator,
            bulk_request_for_anc_policy_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_anc_policy(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_10023cdff02b5185b9b54c9e58762704_v3_1_1').validate(obj.response)
    return True


def monitor_bulk_status_anc_policy(api):
    endpoint_result = api.anc_policy.monitor_bulk_status_anc_policy(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_monitor_bulk_status_anc_policy(api, validator):
    try:
        assert is_valid_monitor_bulk_status_anc_policy(
            validator,
            monitor_bulk_status_anc_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def monitor_bulk_status_anc_policy_default(api):
    endpoint_result = api.anc_policy.monitor_bulk_status_anc_policy(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.anc_policy
def test_monitor_bulk_status_anc_policy_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_anc_policy(
            validator,
            monitor_bulk_status_anc_policy_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
