# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI guest_smtp_notification_configuration API fixtures and tests.

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


def is_valid_get_guest_smtp_notification_settings_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ca28129793d1569bb50de9f43b0d0ee8_v3_3_patch_1').validate(obj.response)
    return True


def get_guest_smtp_notification_settings_by_id(api):
    endpoint_result = api.guest_smtp_notification_configuration.get_guest_smtp_notification_settings_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_get_guest_smtp_notification_settings_by_id(api, validator):
    try:
        assert is_valid_get_guest_smtp_notification_settings_by_id(
            validator,
            get_guest_smtp_notification_settings_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_guest_smtp_notification_settings_by_id_default(api):
    endpoint_result = api.guest_smtp_notification_configuration.get_guest_smtp_notification_settings_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_get_guest_smtp_notification_settings_by_id_default(api, validator):
    try:
        assert is_valid_get_guest_smtp_notification_settings_by_id(
            validator,
            get_guest_smtp_notification_settings_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_smtp_notification_settings_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_a7500f6e473a50e19452683e303dd021_v3_3_patch_1').validate(obj.response)
    return True


def update_guest_smtp_notification_settings_by_id(api):
    endpoint_result = api.guest_smtp_notification_configuration.update_guest_smtp_notification_settings_by_id(
        active_validation=False,
        connection_timeout='string',
        default_from_address='string',
        id='string',
        notification_enabled=True,
        password='string',
        payload=None,
        smtp_port='string',
        smtp_server='string',
        use_default_from_address=True,
        use_password_authentication=True,
        use_tlsor_ssl_encryption=True,
        user_name='string'
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_update_guest_smtp_notification_settings_by_id(api, validator):
    try:
        assert is_valid_update_guest_smtp_notification_settings_by_id(
            validator,
            update_guest_smtp_notification_settings_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_guest_smtp_notification_settings_by_id_default(api):
    endpoint_result = api.guest_smtp_notification_configuration.update_guest_smtp_notification_settings_by_id(
        active_validation=False,
        id='string',
        connection_timeout=None,
        default_from_address=None,
        notification_enabled=None,
        password=None,
        payload=None,
        smtp_port=None,
        smtp_server=None,
        use_default_from_address=None,
        use_password_authentication=None,
        use_tlsor_ssl_encryption=None,
        user_name=None
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_update_guest_smtp_notification_settings_by_id_default(api, validator):
    try:
        assert is_valid_update_guest_smtp_notification_settings_by_id(
            validator,
            update_guest_smtp_notification_settings_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_guest_smtp_notification_settings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_51e4c74e9b4e559e95c73e81183a6c7a_v3_3_patch_1').validate(obj.response)
    return True


def get_guest_smtp_notification_settings(api):
    endpoint_result = api.guest_smtp_notification_configuration.get_guest_smtp_notification_settings(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_get_guest_smtp_notification_settings(api, validator):
    try:
        assert is_valid_get_guest_smtp_notification_settings(
            validator,
            get_guest_smtp_notification_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_guest_smtp_notification_settings_default(api):
    endpoint_result = api.guest_smtp_notification_configuration.get_guest_smtp_notification_settings(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_get_guest_smtp_notification_settings_default(api, validator):
    try:
        assert is_valid_get_guest_smtp_notification_settings(
            validator,
            get_guest_smtp_notification_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_guest_smtp_notification_settings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_01643de7c6f75f68b0d7df00dc72808d_v3_3_patch_1').validate(obj.response)
    return True


def create_guest_smtp_notification_settings(api):
    endpoint_result = api.guest_smtp_notification_configuration.create_guest_smtp_notification_settings(
        active_validation=False,
        connection_timeout='string',
        default_from_address='string',
        notification_enabled=True,
        password='string',
        payload=None,
        smtp_port='string',
        smtp_server='string',
        use_default_from_address=True,
        use_password_authentication=True,
        use_tlsor_ssl_encryption=True,
        user_name='string'
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_create_guest_smtp_notification_settings(api, validator):
    try:
        assert is_valid_create_guest_smtp_notification_settings(
            validator,
            create_guest_smtp_notification_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_guest_smtp_notification_settings_default(api):
    endpoint_result = api.guest_smtp_notification_configuration.create_guest_smtp_notification_settings(
        active_validation=False,
        connection_timeout=None,
        default_from_address=None,
        notification_enabled=None,
        password=None,
        payload=None,
        smtp_port=None,
        smtp_server=None,
        use_default_from_address=None,
        use_password_authentication=None,
        use_tlsor_ssl_encryption=None,
        user_name=None
    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_create_guest_smtp_notification_settings_default(api, validator):
    try:
        assert is_valid_create_guest_smtp_notification_settings(
            validator,
            create_guest_smtp_notification_settings_default(api)
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
    json_schema_validate('jsd_0a0c0e67aead55a2b4db67e9d068351a_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.guest_smtp_notification_configuration.get_version(

    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
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
    endpoint_result = api.guest_smtp_notification_configuration.get_version(

    )
    return endpoint_result


@pytest.mark.guest_smtp_notification_configuration
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
