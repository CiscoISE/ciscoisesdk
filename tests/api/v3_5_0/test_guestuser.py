# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI guestuser API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.5.0', reason='version does not match')


def is_valid_get_all(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_all(api):
    endpoint_result = api.guestuser.get_all(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_all(api, validator):
    try:
        assert is_valid_get_all(
            validator,
            get_all(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_all_default(api):
    endpoint_result = api.guestuser.get_all(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_all_default(api, validator):
    try:
        assert is_valid_get_all(
            validator,
            get_all_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_generator(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_all_generator(api):
    endpoint_result = api.guestuser.get_all_generator(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_all_generator(api, validator):
    try:
        assert is_valid_get_all_generator(
            validator,
            get_all_generator(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_all_generator_default(api):
    endpoint_result = api.guestuser.get_all_generator(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_all_generator_default(api, validator):
    try:
        assert is_valid_get_all_generator(
            validator,
            get_all_generator_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def create(api):
    endpoint_result = api.guestuser.create(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_create(api, validator):
    try:
        assert is_valid_create(
            validator,
            create(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_default(api):
    endpoint_result = api.guestuser.create(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_create_default(api, validator):
    try:
        assert is_valid_create(
            validator,
            create_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deny(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def deny(api):
    endpoint_result = api.guestuser.deny(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_deny(api, validator):
    try:
        assert is_valid_deny(
            validator,
            deny(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def deny_default(api):
    endpoint_result = api.guestuser.deny(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_deny_default(api, validator):
    try:
        assert is_valid_deny(
            validator,
            deny_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_suspend_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def suspend_by_id(api):
    endpoint_result = api.guestuser.suspend_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_suspend_by_id(api, validator):
    try:
        assert is_valid_suspend_by_id(
            validator,
            suspend_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def suspend_by_id_default(api):
    endpoint_result = api.guestuser.suspend_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_suspend_by_id_default(api, validator):
    try:
        assert is_valid_suspend_by_id(
            validator,
            suspend_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_approve(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def approve(api):
    endpoint_result = api.guestuser.approve(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_approve(api, validator):
    try:
        assert is_valid_approve(
            validator,
            approve(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def approve_default(api):
    endpoint_result = api.guestuser.approve(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_approve_default(api, validator):
    try:
        assert is_valid_approve(
            validator,
            approve_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_by_name(api):
    endpoint_result = api.guestuser.get_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_by_name(api, validator):
    try:
        assert is_valid_get_by_name(
            validator,
            get_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_by_name_default(api):
    endpoint_result = api.guestuser.get_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_by_name_default(api, validator):
    try:
        assert is_valid_get_by_name(
            validator,
            get_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def update_by_name(api):
    endpoint_result = api.guestuser.update_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_update_by_name(api, validator):
    try:
        assert is_valid_update_by_name(
            validator,
            update_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_by_name_default(api):
    endpoint_result = api.guestuser.update_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_update_by_name_default(api, validator):
    try:
        assert is_valid_update_by_name(
            validator,
            update_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def delete_by_name(api):
    endpoint_result = api.guestuser.delete_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_delete_by_name(api, validator):
    try:
        assert is_valid_delete_by_name(
            validator,
            delete_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_by_name_default(api):
    endpoint_result = api.guestuser.delete_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_delete_by_name_default(api, validator):
    try:
        assert is_valid_delete_by_name(
            validator,
            delete_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sms(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def sms(api):
    endpoint_result = api.guestuser.sms(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_sms(api, validator):
    try:
        assert is_valid_sms(
            validator,
            sms(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def sms_default(api):
    endpoint_result = api.guestuser.sms(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_sms_default(api, validator):
    try:
        assert is_valid_sms(
            validator,
            sms_default(api)
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
    return True


def change_sponsor_password(api):
    endpoint_result = api.guestuser.change_sponsor_password(
    )
    return endpoint_result


@pytest.mark.guestuser
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
    endpoint_result = api.guestuser.change_sponsor_password(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_change_sponsor_password_default(api, validator):
    try:
        assert is_valid_change_sponsor_password(
            validator,
            change_sponsor_password_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_resetpassword(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def resetpassword(api):
    endpoint_result = api.guestuser.resetpassword(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_resetpassword(api, validator):
    try:
        assert is_valid_resetpassword(
            validator,
            resetpassword(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def resetpassword_default(api):
    endpoint_result = api.guestuser.resetpassword(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_resetpassword_default(api, validator):
    try:
        assert is_valid_resetpassword(
            validator,
            resetpassword_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_email(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def email(api):
    endpoint_result = api.guestuser.email(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_email(api, validator):
    try:
        assert is_valid_email(
            validator,
            email(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def email_default(api):
    endpoint_result = api.guestuser.email(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_email_default(api, validator):
    try:
        assert is_valid_email(
            validator,
            email_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reinstate_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def reinstate_by_id(api):
    endpoint_result = api.guestuser.reinstate_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_reinstate_by_id(api, validator):
    try:
        assert is_valid_reinstate_by_id(
            validator,
            reinstate_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reinstate_by_id_default(api):
    endpoint_result = api.guestuser.reinstate_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_reinstate_by_id_default(api, validator):
    try:
        assert is_valid_reinstate_by_id(
            validator,
            reinstate_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reinstate_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def reinstate_by_name(api):
    endpoint_result = api.guestuser.reinstate_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_reinstate_by_name(api, validator):
    try:
        assert is_valid_reinstate_by_name(
            validator,
            reinstate_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reinstate_by_name_default(api):
    endpoint_result = api.guestuser.reinstate_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_reinstate_by_name_default(api, validator):
    try:
        assert is_valid_reinstate_by_name(
            validator,
            reinstate_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_suspend_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def suspend_by_name(api):
    endpoint_result = api.guestuser.suspend_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_suspend_by_name(api, validator):
    try:
        assert is_valid_suspend_by_name(
            validator,
            suspend_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def suspend_by_name_default(api):
    endpoint_result = api.guestuser.suspend_by_name(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_suspend_by_name_default(api, validator):
    try:
        assert is_valid_suspend_by_name(
            validator,
            suspend_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_by_id(api):
    endpoint_result = api.guestuser.get_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_by_id(api, validator):
    try:
        assert is_valid_get_by_id(
            validator,
            get_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_by_id_default(api):
    endpoint_result = api.guestuser.get_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_get_by_id_default(api, validator):
    try:
        assert is_valid_get_by_id(
            validator,
            get_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def update_by_id(api):
    endpoint_result = api.guestuser.update_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_update_by_id(api, validator):
    try:
        assert is_valid_update_by_id(
            validator,
            update_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_by_id_default(api):
    endpoint_result = api.guestuser.update_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_update_by_id_default(api, validator):
    try:
        assert is_valid_update_by_id(
            validator,
            update_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def delete_by_id(api):
    endpoint_result = api.guestuser.delete_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_delete_by_id(api, validator):
    try:
        assert is_valid_delete_by_id(
            validator,
            delete_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_by_id_default(api):
    endpoint_result = api.guestuser.delete_by_id(
    )
    return endpoint_result


@pytest.mark.guestuser
def test_delete_by_id_default(api, validator):
    try:
        assert is_valid_delete_by_id(
            validator,
            delete_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


