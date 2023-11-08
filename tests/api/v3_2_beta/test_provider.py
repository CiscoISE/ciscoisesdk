# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI provider API fixtures and tests.

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


def is_valid_register_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_61c9daa26d4b5b80a41d4b7ff9359380_v3_2_beta').validate(obj.response)
    return True


def register_service(api):
    endpoint_result = api.provider.register_service(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_register_service(api, validator):
    try:
        assert is_valid_register_service(
            validator,
            register_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def register_service_default(api):
    endpoint_result = api.provider.register_service(
        active_validation=False,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_register_service_default(api, validator):
    try:
        assert is_valid_register_service(
            validator,
            register_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_unregister_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b480aaa729e75e3d872d0b30a3f8b804_v3_2_beta').validate(obj.response)
    return True


def unregister_service(api):
    endpoint_result = api.provider.unregister_service(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_unregister_service(api, validator):
    try:
        assert is_valid_unregister_service(
            validator,
            unregister_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def unregister_service_default(api):
    endpoint_result = api.provider.unregister_service(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_unregister_service_default(api, validator):
    try:
        assert is_valid_unregister_service(
            validator,
            unregister_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reregister_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ed4d852c55cd54c480986bec7fd9a8bb_v3_2_beta').validate(obj.response)
    return True


def reregister_service(api):
    endpoint_result = api.provider.reregister_service(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_reregister_service(api, validator):
    try:
        assert is_valid_reregister_service(
            validator,
            reregister_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reregister_service_default(api):
    endpoint_result = api.provider.reregister_service(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_reregister_service_default(api, validator):
    try:
        assert is_valid_reregister_service(
            validator,
            reregister_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_authorization(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c9088df384b458c3991fed7f718971d5_v3_2_beta').validate(obj.response)
    return True


def authorization(api):
    endpoint_result = api.provider.authorization(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_authorization(api, validator):
    try:
        assert is_valid_authorization(
            validator,
            authorization(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def authorization_default(api):
    endpoint_result = api.provider.authorization(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.provider
def test_authorization_default(api, validator):
    try:
        assert is_valid_authorization(
            validator,
            authorization_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
