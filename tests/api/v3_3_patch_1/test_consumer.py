# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI consumer API fixtures and tests.

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


def is_valid_create_account(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_91101b93b991556cae0fdd562c5e3f63_v3_3_patch_1').validate(obj.response)
    return True


def create_account(api):
    endpoint_result = api.consumer.create_account(
        active_validation=False,
        node_name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.consumer
def test_create_account(api, validator):
    try:
        assert is_valid_create_account(
            validator,
            create_account(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_account_default(api):
    endpoint_result = api.consumer.create_account(
        active_validation=False,
        node_name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.consumer
def test_create_account_default(api, validator):
    try:
        assert is_valid_create_account(
            validator,
            create_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_activate_account(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d1f92a9024975e9dad6114255be546bd_v3_3_patch_1').validate(obj.response)
    return True


def activate_account(api):
    endpoint_result = api.consumer.activate_account(
        active_validation=False,
        description='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.consumer
def test_activate_account(api, validator):
    try:
        assert is_valid_activate_account(
            validator,
            activate_account(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def activate_account_default(api):
    endpoint_result = api.consumer.activate_account(
        active_validation=False,
        description=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.consumer
def test_activate_account_default(api, validator):
    try:
        assert is_valid_activate_account(
            validator,
            activate_account_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_lookup_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_98c8ffe8c6095203a83131f49d4c8bb2_v3_3_patch_1').validate(obj.response)
    return True


def lookup_service(api):
    endpoint_result = api.consumer.lookup_service(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.consumer
def test_lookup_service(api, validator):
    try:
        assert is_valid_lookup_service(
            validator,
            lookup_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def lookup_service_default(api):
    endpoint_result = api.consumer.lookup_service(
        active_validation=False,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.consumer
def test_lookup_service_default(api, validator):
    try:
        assert is_valid_lookup_service(
            validator,
            lookup_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_access_secret(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_eaad68e7996c5562901de57bf5a0420a_v3_3_patch_1').validate(obj.response)
    return True


def access_secret(api):
    endpoint_result = api.consumer.access_secret(
        active_validation=False,
        payload=None,
        peer_node_name='string'
    )
    return endpoint_result


@pytest.mark.consumer
def test_access_secret(api, validator):
    try:
        assert is_valid_access_secret(
            validator,
            access_secret(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def access_secret_default(api):
    endpoint_result = api.consumer.access_secret(
        active_validation=False,
        payload=None,
        peer_node_name=None
    )
    return endpoint_result


@pytest.mark.consumer
def test_access_secret_default(api, validator):
    try:
        assert is_valid_access_secret(
            validator,
            access_secret_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
