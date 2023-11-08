# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI dataconnect_services API fixtures and tests.

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


def is_valid_get_odbc_detail(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d98458307a1c5cea9b11ee96945fcefa_v3_2_beta').validate(obj.response)
    return True


def get_odbc_detail(api):
    endpoint_result = api.dataconnect_services.get_odbc_detail(

    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_get_odbc_detail(api, validator):
    try:
        assert is_valid_get_odbc_detail(
            validator,
            get_odbc_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_odbc_detail_default(api):
    endpoint_result = api.dataconnect_services.get_odbc_detail(

    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_get_odbc_detail_default(api, validator):
    try:
        assert is_valid_get_odbc_detail(
            validator,
            get_odbc_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_dataconnect_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e0455a6b0945530585c7a32f36ae76b0_v3_2_beta').validate(obj.response)
    return True


def get_dataconnect_service(api):
    endpoint_result = api.dataconnect_services.get_dataconnect_service(

    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_get_dataconnect_service(api, validator):
    try:
        assert is_valid_get_dataconnect_service(
            validator,
            get_dataconnect_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_dataconnect_service_default(api):
    endpoint_result = api.dataconnect_services.get_dataconnect_service(

    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_get_dataconnect_service_default(api, validator):
    try:
        assert is_valid_get_dataconnect_service(
            validator,
            get_dataconnect_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_dataconnect_password(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_709687a7458c54ed9f4761c46a3c5e58_v3_2_beta').validate(obj.response)
    return True


def update_dataconnect_password(api):
    endpoint_result = api.dataconnect_services.update_dataconnect_password(
        active_validation=False,
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_update_dataconnect_password(api, validator):
    try:
        assert is_valid_update_dataconnect_password(
            validator,
            update_dataconnect_password(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_dataconnect_password_default(api):
    endpoint_result = api.dataconnect_services.update_dataconnect_password(
        active_validation=False,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_update_dataconnect_password_default(api, validator):
    try:
        assert is_valid_update_dataconnect_password(
            validator,
            update_dataconnect_password_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_dataconnect_password_expiry(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_550974fed9705442857aa0fee26a7a62_v3_2_beta').validate(obj.response)
    return True


def update_dataconnect_password_expiry(api):
    endpoint_result = api.dataconnect_services.update_dataconnect_password_expiry(
        active_validation=False,
        password_expires_in_days=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_update_dataconnect_password_expiry(api, validator):
    try:
        assert is_valid_update_dataconnect_password_expiry(
            validator,
            update_dataconnect_password_expiry(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_dataconnect_password_expiry_default(api):
    endpoint_result = api.dataconnect_services.update_dataconnect_password_expiry(
        active_validation=False,
        password_expires_in_days=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_update_dataconnect_password_expiry_default(api, validator):
    try:
        assert is_valid_update_dataconnect_password_expiry(
            validator,
            update_dataconnect_password_expiry_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_data_connect_service(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b1b4aa6b58875e0cb90805def240b058_v3_2_beta').validate(obj.response)
    return True


def set_data_connect_service(api):
    endpoint_result = api.dataconnect_services.set_data_connect_service(
        active_validation=False,
        is_enabled=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_set_data_connect_service(api, validator):
    try:
        assert is_valid_set_data_connect_service(
            validator,
            set_data_connect_service(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def set_data_connect_service_default(api):
    endpoint_result = api.dataconnect_services.set_data_connect_service(
        active_validation=False,
        is_enabled=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.dataconnect_services
def test_set_data_connect_service_default(api, validator):
    try:
        assert is_valid_set_data_connect_service(
            validator,
            set_data_connect_service_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
