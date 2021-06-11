# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI guest_type API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_all_guest_type(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0f41a1e47105581fabf212f259626903_v3_0_0').validate(obj.response)
    return True


def get_all_guest_type(api):
    endpoint_result = api.guest_type.get_all_guest_type(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.guest_type
def test_get_all_guest_type(api, validator):
    try:
        assert is_valid_get_all_guest_type(
            validator,
            get_all_guest_type(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_guest_type_default(api):
    endpoint_result = api.guest_type.get_all_guest_type(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.guest_type
def test_get_all_guest_type_default(api, validator):
    try:
        assert is_valid_get_all_guest_type(
            validator,
            get_all_guest_type_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_guest_type(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f46c01449d585b088490c4db530c56d5_v3_0_0').validate(obj.response)
    return True


def create_guest_type(api):
    endpoint_result = api.guest_type.create_guest_type(
        access_time={'fromFirstLogin': True, 'maxAccountDuration': 0, 'durationTimeUnit': 'string', 'defaultDuration': 0, 'allowAccessOnSpecificDaysTimes': True, 'dayTimeLimits': [{'startTime': 'string', 'endTime': 'string', 'days': ['string']}]},
        active_validation=False,
        description='string',
        expiration_notification={'enableNotification': True, 'advanceNotificationDuration': 0, 'advanceNotificationUnits': 'string', 'sendEmailNotification': True, 'emailText': 'string', 'sendSmsNotification': True, 'smsText': 'string'},
        id='string',
        login_options={'limitSimultaneousLogins': True, 'maxSimultaneousLogins': 0, 'failureAction': 'string', 'maxRegisteredDevices': 0, 'identityGroupId': 'string', 'allowGuestPortalBypass': True},
        name='string',
        payload=None,
        sponsor_groups=['string']
    )
    return endpoint_result


@pytest.mark.guest_type
def test_create_guest_type(api, validator):
    try:
        assert is_valid_create_guest_type(
            validator,
            create_guest_type(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_guest_type_default(api):
    endpoint_result = api.guest_type.create_guest_type(
        active_validation=False,
        access_time=None,
        description=None,
        expiration_notification=None,
        id=None,
        login_options=None,
        name=None,
        payload=None,
        sponsor_groups=None
    )
    return endpoint_result


@pytest.mark.guest_type
def test_create_guest_type_default(api, validator):
    try:
        assert is_valid_create_guest_type(
            validator,
            create_guest_type_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_guest_type_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4acb5a41fe395b158a3fe1cda996b0cf_v3_0_0').validate(obj.response)
    return True


def get_guest_type_by_id(api):
    endpoint_result = api.guest_type.get_guest_type_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_type
def test_get_guest_type_by_id(api, validator):
    try:
        assert is_valid_get_guest_type_by_id(
            validator,
            get_guest_type_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_guest_type_by_id_default(api):
    endpoint_result = api.guest_type.get_guest_type_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_type
def test_get_guest_type_by_id_default(api, validator):
    try:
        assert is_valid_get_guest_type_by_id(
            validator,
            get_guest_type_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guesttype_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bac6d4d95ac45a0a8933b8712dcbe70d_v3_0_0').validate(obj.response)
    return True


def update_guesttype_by_id(api):
    endpoint_result = api.guest_type.update_guesttype_by_id(
        access_time={'fromFirstLogin': True, 'maxAccountDuration': 0, 'durationTimeUnit': 'string', 'defaultDuration': 0, 'allowAccessOnSpecificDaysTimes': True, 'dayTimeLimits': [{'startTime': 'string', 'endTime': 'string', 'days': ['string']}]},
        active_validation=False,
        description='string',
        expiration_notification={'enableNotification': True, 'advanceNotificationDuration': 0, 'advanceNotificationUnits': 'string', 'sendEmailNotification': True, 'emailText': 'string', 'sendSmsNotification': True, 'smsText': 'string'},
        id='string',
        login_options={'limitSimultaneousLogins': True, 'maxSimultaneousLogins': 0, 'failureAction': 'string', 'maxRegisteredDevices': 0, 'identityGroupId': 'string', 'allowGuestPortalBypass': True},
        name='string',
        payload=None,
        sponsor_groups=['string']
    )
    return endpoint_result


@pytest.mark.guest_type
def test_update_guesttype_by_id(api, validator):
    try:
        assert is_valid_update_guesttype_by_id(
            validator,
            update_guesttype_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_guesttype_by_id_default(api):
    endpoint_result = api.guest_type.update_guesttype_by_id(
        active_validation=False,
        id='string',
        access_time=None,
        description=None,
        expiration_notification=None,
        login_options=None,
        name=None,
        payload=None,
        sponsor_groups=None
    )
    return endpoint_result


@pytest.mark.guest_type
def test_update_guesttype_by_id_default(api, validator):
    try:
        assert is_valid_update_guesttype_by_id(
            validator,
            update_guesttype_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_guest_type_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6faa7211d68e5b329034e17c82b78694_v3_0_0').validate(obj.response)
    return True


def delete_guest_type_by_id(api):
    endpoint_result = api.guest_type.delete_guest_type_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_type
def test_delete_guest_type_by_id(api, validator):
    try:
        assert is_valid_delete_guest_type_by_id(
            validator,
            delete_guest_type_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_guest_type_by_id_default(api):
    endpoint_result = api.guest_type.delete_guest_type_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_type
def test_delete_guest_type_by_id_default(api, validator):
    try:
        assert is_valid_delete_guest_type_by_id(
            validator,
            delete_guest_type_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_type_sms(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0493eb42e79d5cc38bd1a6eef20613d6_v3_0_0').validate(obj.response)
    return True


def update_guest_type_sms(api):
    endpoint_result = api.guest_type.update_guest_type_sms(
        active_validation=False,
        additional_data=[{'name': 'string', 'value': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_type
def test_update_guest_type_sms(api, validator):
    try:
        assert is_valid_update_guest_type_sms(
            validator,
            update_guest_type_sms(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_guest_type_sms_default(api):
    endpoint_result = api.guest_type.update_guest_type_sms(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_type
def test_update_guest_type_sms_default(api, validator):
    try:
        assert is_valid_update_guest_type_sms(
            validator,
            update_guest_type_sms_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_type_email(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_cf310e621a395bb7bac7b90d7d4c8603_v3_0_0').validate(obj.response)
    return True


def update_guest_type_email(api):
    endpoint_result = api.guest_type.update_guest_type_email(
        active_validation=False,
        additional_data=[{'name': 'string', 'value': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_type
def test_update_guest_type_email(api, validator):
    try:
        assert is_valid_update_guest_type_email(
            validator,
            update_guest_type_email(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_guest_type_email_default(api):
    endpoint_result = api.guest_type.update_guest_type_email(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_type
def test_update_guest_type_email_default(api, validator):
    try:
        assert is_valid_update_guest_type_email(
            validator,
            update_guest_type_email_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
