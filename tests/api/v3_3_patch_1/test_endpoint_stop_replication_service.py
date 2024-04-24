# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI endpoint_stop_replication_service API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.3_patch_1', reason='version does not match')


def is_valid_get_stop_replication_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c99b06123cb958fb91d7581457e28ca1_v3_3_patch_1').validate(obj.response)
    return True


def get_stop_replication_status(api):
    endpoint_result = api.endpoint_stop_replication_service.get_stop_replication_status(

    )
    return endpoint_result


@pytest.mark.endpoint_stop_replication_service
def test_get_stop_replication_status(api, validator):
    try:
        assert is_valid_get_stop_replication_status(
            validator,
            get_stop_replication_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_stop_replication_status_default(api):
    endpoint_result = api.endpoint_stop_replication_service.get_stop_replication_status(

    )
    return endpoint_result


@pytest.mark.endpoint_stop_replication_service
def test_get_stop_replication_status_default(api, validator):
    try:
        assert is_valid_get_stop_replication_status(
            validator,
            get_stop_replication_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_stop_replication_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bdc839ed309b593d8e7b8a90ef5930c5_v3_3_patch_1').validate(obj.response)
    return True


def set_stop_replication_service(api):
    endpoint_result = api.endpoint_stop_replication_service.set_stop_replication_service(
        active_validation=False,
        is_enabled=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint_stop_replication_service
def test_set_stop_replication_service(api, validator):
    try:
        assert is_valid_set_stop_replication_service(
            validator,
            set_stop_replication_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def set_stop_replication_service_default(api):
    endpoint_result = api.endpoint_stop_replication_service.set_stop_replication_service(
        active_validation=False,
        is_enabled=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint_stop_replication_service
def test_set_stop_replication_service_default(api, validator):
    try:
        assert is_valid_set_stop_replication_service(
            validator,
            set_stop_replication_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
