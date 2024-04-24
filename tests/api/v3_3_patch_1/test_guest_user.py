# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI guest_user API fixtures and tests.

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


def is_valid_approve_guest_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c67b4dcffba052ae8ece775bc61a1c21_v3_3_patch_1').validate(obj.response)
    return True


def approve_guest_user_by_id(api):
    endpoint_result = api.guest_user.approve_guest_user_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_approve_guest_user_by_id(api, validator):
    try:
        assert is_valid_approve_guest_user_by_id(
            validator,
            approve_guest_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def approve_guest_user_by_id_default(api):
    endpoint_result = api.guest_user.approve_guest_user_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_approve_guest_user_by_id_default(api, validator):
    try:
        assert is_valid_approve_guest_user_by_id(
            validator,
            approve_guest_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_change_sponsor_password(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2eb3472c4de150828b2dae61e2285313_v3_3_patch_1').validate(obj.response)
    return True


def change_sponsor_password(api):
    endpoint_result = api.guest_user.change_sponsor_password(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        payload=None,
        portal_id='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_change_sponsor_password(api, validator):
    try:
        assert is_valid_change_sponsor_password(
            validator,
            change_sponsor_password(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def change_sponsor_password_default(api):
    endpoint_result = api.guest_user.change_sponsor_password(
        active_validation=False,
        portal_id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_change_sponsor_password_default(api, validator):
    try:
        assert is_valid_change_sponsor_password(
            validator,
            change_sponsor_password_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_suspend_guest_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_83983afcc8fe53b4824ae744a2ff3848_v3_3_patch_1').validate(obj.response)
    return True


def suspend_guest_user_by_name(api):
    endpoint_result = api.guest_user.suspend_guest_user_by_name(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_suspend_guest_user_by_name(api, validator):
    try:
        assert is_valid_suspend_guest_user_by_name(
            validator,
            suspend_guest_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def suspend_guest_user_by_name_default(api):
    endpoint_result = api.guest_user.suspend_guest_user_by_name(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_suspend_guest_user_by_name_default(api, validator):
    try:
        assert is_valid_suspend_guest_user_by_name(
            validator,
            suspend_guest_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reinstate_guest_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_18b21045846d5097a82cd61cb3c7eaf1_v3_3_patch_1').validate(obj.response)
    return True


def reinstate_guest_user_by_name(api):
    endpoint_result = api.guest_user.reinstate_guest_user_by_name(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_reinstate_guest_user_by_name(api, validator):
    try:
        assert is_valid_reinstate_guest_user_by_name(
            validator,
            reinstate_guest_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reinstate_guest_user_by_name_default(api):
    endpoint_result = api.guest_user.reinstate_guest_user_by_name(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_reinstate_guest_user_by_name_default(api, validator):
    try:
        assert is_valid_reinstate_guest_user_by_name(
            validator,
            reinstate_guest_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_guest_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bcb7ec29968e5d5899df4a90d94ed659_v3_3_patch_1').validate(obj.response)
    return True


def get_guest_user_by_name(api):
    endpoint_result = api.guest_user.get_guest_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_get_guest_user_by_name(api, validator):
    try:
        assert is_valid_get_guest_user_by_name(
            validator,
            get_guest_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_guest_user_by_name_default(api):
    endpoint_result = api.guest_user.get_guest_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_get_guest_user_by_name_default(api, validator):
    try:
        assert is_valid_get_guest_user_by_name(
            validator,
            get_guest_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f24049df29d059c48eef86d381ffad5d_v3_3_patch_1').validate(obj.response)
    return True


def update_guest_user_by_name(api):
    endpoint_result = api.guest_user.update_guest_user_by_name(
        active_validation=False,
        custom_fields={},
        description='string',
        guest_access_info={'validDays': 0, 'fromDate': 'string', 'toDate': 'string', 'location': 'string', 'ssid': 'string', 'groupTag': 'string'},
        guest_info={'firstName': 'string', 'lastName': 'string', 'company': 'string', 'creationTime': 'string', 'notificationLanguage': 'string', 'userName': 'string', 'emailAddress': 'string', 'phoneNumber': 'string', 'password': 'string', 'enabled': True, 'smsServiceProvider': 'string'},
        guest_type='string',
        id='string',
        name='string',
        payload=None,
        portal_id='string',
        reason_for_visit='string',
        sponsor_user_id='string',
        sponsor_user_name='string',
        status='string',
        status_reason='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_by_name(api, validator):
    try:
        assert is_valid_update_guest_user_by_name(
            validator,
            update_guest_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_guest_user_by_name_default(api):
    endpoint_result = api.guest_user.update_guest_user_by_name(
        active_validation=False,
        name='string',
        custom_fields=None,
        description=None,
        guest_access_info=None,
        guest_info=None,
        guest_type=None,
        id=None,
        payload=None,
        portal_id=None,
        reason_for_visit=None,
        sponsor_user_id=None,
        sponsor_user_name=None,
        status=None,
        status_reason=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_by_name_default(api, validator):
    try:
        assert is_valid_update_guest_user_by_name(
            validator,
            update_guest_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_guest_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_76ef15d7c6b259f5859ee9675c38887c_v3_3_patch_1').validate(obj.response)
    return True


def delete_guest_user_by_name(api):
    endpoint_result = api.guest_user.delete_guest_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_delete_guest_user_by_name(api, validator):
    try:
        assert is_valid_delete_guest_user_by_name(
            validator,
            delete_guest_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_guest_user_by_name_default(api):
    endpoint_result = api.guest_user.delete_guest_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_delete_guest_user_by_name_default(api, validator):
    try:
        assert is_valid_delete_guest_user_by_name(
            validator,
            delete_guest_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_guest_user_password_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7ea6ea4e41d85f83b6f6c10ce38bb9ed_v3_3_patch_1').validate(obj.response)
    return True


def reset_guest_user_password_by_id(api):
    endpoint_result = api.guest_user.reset_guest_user_password_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_reset_guest_user_password_by_id(api, validator):
    try:
        assert is_valid_reset_guest_user_password_by_id(
            validator,
            reset_guest_user_password_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reset_guest_user_password_by_id_default(api):
    endpoint_result = api.guest_user.reset_guest_user_password_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_reset_guest_user_password_by_id_default(api, validator):
    try:
        assert is_valid_reset_guest_user_password_by_id(
            validator,
            reset_guest_user_password_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reinstate_guest_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4dfcba4a0f685c168bdf2b5b2be317ac_v3_3_patch_1').validate(obj.response)
    return True


def reinstate_guest_user_by_id(api):
    endpoint_result = api.guest_user.reinstate_guest_user_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_reinstate_guest_user_by_id(api, validator):
    try:
        assert is_valid_reinstate_guest_user_by_id(
            validator,
            reinstate_guest_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reinstate_guest_user_by_id_default(api):
    endpoint_result = api.guest_user.reinstate_guest_user_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_reinstate_guest_user_by_id_default(api, validator):
    try:
        assert is_valid_reinstate_guest_user_by_id(
            validator,
            reinstate_guest_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_user_email(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9a9fa9cbccbe50fcb1cd6a63fed47578_v3_3_patch_1').validate(obj.response)
    return True


def update_guest_user_email(api):
    endpoint_result = api.guest_user.update_guest_user_email(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None,
        portal_id='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_email(api, validator):
    try:
        assert is_valid_update_guest_user_email(
            validator,
            update_guest_user_email(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_guest_user_email_default(api):
    endpoint_result = api.guest_user.update_guest_user_email(
        active_validation=False,
        id='string',
        portal_id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_email_default(api, validator):
    try:
        assert is_valid_update_guest_user_email(
            validator,
            update_guest_user_email_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_user_sms(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_290601ba14b751f98206ca2e19cff3fe_v3_3_patch_1').validate(obj.response)
    return True


def update_guest_user_sms(api):
    endpoint_result = api.guest_user.update_guest_user_sms(
        active_validation=False,
        id='string',
        payload=None,
        portal_id='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_sms(api, validator):
    try:
        assert is_valid_update_guest_user_sms(
            validator,
            update_guest_user_sms(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_guest_user_sms_default(api):
    endpoint_result = api.guest_user.update_guest_user_sms(
        active_validation=False,
        id='string',
        portal_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_sms_default(api, validator):
    try:
        assert is_valid_update_guest_user_sms(
            validator,
            update_guest_user_sms_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deny_guest_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3c1e5e2a187652018c59b10155ac973d_v3_3_patch_1').validate(obj.response)
    return True


def deny_guest_user_by_id(api):
    endpoint_result = api.guest_user.deny_guest_user_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_deny_guest_user_by_id(api, validator):
    try:
        assert is_valid_deny_guest_user_by_id(
            validator,
            deny_guest_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def deny_guest_user_by_id_default(api):
    endpoint_result = api.guest_user.deny_guest_user_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_deny_guest_user_by_id_default(api, validator):
    try:
        assert is_valid_deny_guest_user_by_id(
            validator,
            deny_guest_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_guest_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2645275c3c7d5a3a83d9f7441972d399_v3_3_patch_1').validate(obj.response)
    return True


def get_guest_user_by_id(api):
    endpoint_result = api.guest_user.get_guest_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_get_guest_user_by_id(api, validator):
    try:
        assert is_valid_get_guest_user_by_id(
            validator,
            get_guest_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_guest_user_by_id_default(api):
    endpoint_result = api.guest_user.get_guest_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_get_guest_user_by_id_default(api, validator):
    try:
        assert is_valid_get_guest_user_by_id(
            validator,
            get_guest_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_guest_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8754551b9c7c5847b17684c49399ff95_v3_3_patch_1').validate(obj.response)
    return True


def update_guest_user_by_id(api):
    endpoint_result = api.guest_user.update_guest_user_by_id(
        active_validation=False,
        custom_fields={},
        description='string',
        guest_access_info={'validDays': 0, 'fromDate': 'string', 'toDate': 'string', 'location': 'string', 'ssid': 'string', 'groupTag': 'string'},
        guest_info={'firstName': 'string', 'lastName': 'string', 'company': 'string', 'creationTime': 'string', 'notificationLanguage': 'string', 'userName': 'string', 'emailAddress': 'string', 'phoneNumber': 'string', 'password': 'string', 'enabled': True, 'smsServiceProvider': 'string'},
        guest_type='string',
        id='string',
        name='string',
        payload=None,
        portal_id='string',
        reason_for_visit='string',
        sponsor_user_id='string',
        sponsor_user_name='string',
        status='string',
        status_reason='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_by_id(api, validator):
    try:
        assert is_valid_update_guest_user_by_id(
            validator,
            update_guest_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_guest_user_by_id_default(api):
    endpoint_result = api.guest_user.update_guest_user_by_id(
        active_validation=False,
        id='string',
        custom_fields=None,
        description=None,
        guest_access_info=None,
        guest_info=None,
        guest_type=None,
        name=None,
        payload=None,
        portal_id=None,
        reason_for_visit=None,
        sponsor_user_id=None,
        sponsor_user_name=None,
        status=None,
        status_reason=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_update_guest_user_by_id_default(api, validator):
    try:
        assert is_valid_update_guest_user_by_id(
            validator,
            update_guest_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_guest_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1030e251b39f55d3ac2570a963a3ee9c_v3_3_patch_1').validate(obj.response)
    return True


def delete_guest_user_by_id(api):
    endpoint_result = api.guest_user.delete_guest_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_delete_guest_user_by_id(api, validator):
    try:
        assert is_valid_delete_guest_user_by_id(
            validator,
            delete_guest_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_guest_user_by_id_default(api):
    endpoint_result = api.guest_user.delete_guest_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_delete_guest_user_by_id_default(api, validator):
    try:
        assert is_valid_delete_guest_user_by_id(
            validator,
            delete_guest_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_guest_users(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1a5abd33eeaa52e39e926472751ef79e_v3_3_patch_1').validate(obj.response)
    return True


def get_guest_users(api):
    endpoint_result = api.guest_user.get_guest_users(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_get_guest_users(api, validator):
    try:
        assert is_valid_get_guest_users(
            validator,
            get_guest_users(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_guest_users_default(api):
    endpoint_result = api.guest_user.get_guest_users(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_get_guest_users_default(api, validator):
    try:
        assert is_valid_get_guest_users(
            validator,
            get_guest_users_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_guest_user(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_89f7cf06a1655d6da606ace9b0950bcf_v3_3_patch_1').validate(obj.response)
    return True


def create_guest_user(api):
    endpoint_result = api.guest_user.create_guest_user(
        active_validation=False,
        custom_fields={},
        description='string',
        guest_access_info={'validDays': 0, 'fromDate': 'string', 'toDate': 'string', 'location': 'string', 'ssid': 'string', 'groupTag': 'string'},
        guest_info={'firstName': 'string', 'lastName': 'string', 'company': 'string', 'creationTime': 'string', 'notificationLanguage': 'string', 'userName': 'string', 'emailAddress': 'string', 'phoneNumber': 'string', 'password': 'string', 'enabled': True, 'smsServiceProvider': 'string'},
        guest_type='string',
        name='string',
        payload=None,
        portal_id='string',
        reason_for_visit='string',
        sponsor_user_id='string',
        sponsor_user_name='string',
        status='string',
        status_reason='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_create_guest_user(api, validator):
    try:
        assert is_valid_create_guest_user(
            validator,
            create_guest_user(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_guest_user_default(api):
    endpoint_result = api.guest_user.create_guest_user(
        active_validation=False,
        custom_fields=None,
        description=None,
        guest_access_info=None,
        guest_info=None,
        guest_type=None,
        name=None,
        payload=None,
        portal_id=None,
        reason_for_visit=None,
        sponsor_user_id=None,
        sponsor_user_name=None,
        status=None,
        status_reason=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_create_guest_user_default(api, validator):
    try:
        assert is_valid_create_guest_user(
            validator,
            create_guest_user_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_suspend_guest_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_08be5b1e320e55f4a181370417471d9e_v3_3_patch_1').validate(obj.response)
    return True


def suspend_guest_user_by_id(api):
    endpoint_result = api.guest_user.suspend_guest_user_by_id(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_suspend_guest_user_by_id(api, validator):
    try:
        assert is_valid_suspend_guest_user_by_id(
            validator,
            suspend_guest_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def suspend_guest_user_by_id_default(api):
    endpoint_result = api.guest_user.suspend_guest_user_by_id(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_suspend_guest_user_by_id_default(api, validator):
    try:
        assert is_valid_suspend_guest_user_by_id(
            validator,
            suspend_guest_user_by_id_default(api)
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
    json_schema_validate('jsd_76abe22ea0c45f619731bd568c9f57f4_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.guest_user.get_version(

    )
    return endpoint_result


@pytest.mark.guest_user
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
    endpoint_result = api.guest_user.get_version(

    )
    return endpoint_result


@pytest.mark.guest_user
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_guest_user(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_37edfca30e8e514d9bab840c3c2d4c0f_v3_3_patch_1').validate(obj.response)
    return True


def bulk_request_for_guest_user(api):
    endpoint_result = api.guest_user.bulk_request_for_guest_user(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_bulk_request_for_guest_user(api, validator):
    try:
        assert is_valid_bulk_request_for_guest_user(
            validator,
            bulk_request_for_guest_user(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_request_for_guest_user_default(api):
    endpoint_result = api.guest_user.bulk_request_for_guest_user(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.guest_user
def test_bulk_request_for_guest_user_default(api, validator):
    try:
        assert is_valid_bulk_request_for_guest_user(
            validator,
            bulk_request_for_guest_user_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_guest_user(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e38a1af3ad835636a11375363528fa2e_v3_3_patch_1').validate(obj.response)
    return True


def monitor_bulk_status_guest_user(api):
    endpoint_result = api.guest_user.monitor_bulk_status_guest_user(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_monitor_bulk_status_guest_user(api, validator):
    try:
        assert is_valid_monitor_bulk_status_guest_user(
            validator,
            monitor_bulk_status_guest_user(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def monitor_bulk_status_guest_user_default(api):
    endpoint_result = api.guest_user.monitor_bulk_status_guest_user(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.guest_user
def test_monitor_bulk_status_guest_user_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_guest_user(
            validator,
            monitor_bulk_status_guest_user_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
