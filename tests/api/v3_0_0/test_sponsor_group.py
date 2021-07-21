# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sponsor_group API fixtures and tests.

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


def is_valid_get_sponsor_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_eaa0d7c339d152b688876c2e10f51fe7_v3_0_0').validate(obj.response)
    return True


def get_sponsor_group_by_id(api):
    endpoint_result = api.sponsor_group.get_sponsor_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_get_sponsor_group_by_id(api, validator):
    try:
        assert is_valid_get_sponsor_group_by_id(
            validator,
            get_sponsor_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sponsor_group_by_id_default(api):
    endpoint_result = api.sponsor_group.get_sponsor_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_get_sponsor_group_by_id_default(api, validator):
    try:
        assert is_valid_get_sponsor_group_by_id(
            validator,
            get_sponsor_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sponsor_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_dfc44f7f24d153d789efa48e904b3832_v3_0_0').validate(obj.response)
    return True


def update_sponsor_group_by_id(api):
    endpoint_result = api.sponsor_group.update_sponsor_group_by_id(
        active_validation=False,
        auto_notification=True,
        create_permissions={'canImportMultipleAccounts': True, 'importBatchSizeLimit': 0, 'canCreateRandomAccounts': True, 'randomBatchSizeLimit': 0, 'defaultUsernamePrefix': 'string', 'canSpecifyUsernamePrefix': True, 'canSetFutureStartDate': True, 'startDateFutureLimitDays': 0},
        description='string',
        guest_types=['string'],
        id='string',
        is_default_group=True,
        is_enabled=True,
        locations=['string'],
        manage_permission='string',
        member_groups=['string'],
        name='string',
        other_permissions={'canUpdateGuestContactInfo': True, 'canViewGuestPasswords': True, 'canSendSmsNotifications': True, 'canResetGuestPasswords': True, 'canExtendGuestAccounts': True, 'canDeleteGuestAccounts': True, 'canSuspendGuestAccounts': True, 'requireSuspensionReason': True, 'canReinstateSuspendedAccounts': True, 'canApproveSelfregGuests': True, 'limitApprovalToSponsorsGuests': True, 'canAccessViaRest': True},
        payload=None
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_update_sponsor_group_by_id(api, validator):
    try:
        assert is_valid_update_sponsor_group_by_id(
            validator,
            update_sponsor_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_sponsor_group_by_id_default(api):
    endpoint_result = api.sponsor_group.update_sponsor_group_by_id(
        active_validation=False,
        id='string',
        auto_notification=None,
        create_permissions=None,
        description=None,
        guest_types=None,
        is_default_group=None,
        is_enabled=None,
        locations=None,
        manage_permission=None,
        member_groups=None,
        name=None,
        other_permissions=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_update_sponsor_group_by_id_default(api, validator):
    try:
        assert is_valid_update_sponsor_group_by_id(
            validator,
            update_sponsor_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sponsor_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_61c28a45acf05fec98879d8d2ac51129_v3_0_0').validate(obj.response)
    return True


def delete_sponsor_group_by_id(api):
    endpoint_result = api.sponsor_group.delete_sponsor_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_delete_sponsor_group_by_id(api, validator):
    try:
        assert is_valid_delete_sponsor_group_by_id(
            validator,
            delete_sponsor_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_sponsor_group_by_id_default(api):
    endpoint_result = api.sponsor_group.delete_sponsor_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_delete_sponsor_group_by_id_default(api, validator):
    try:
        assert is_valid_delete_sponsor_group_by_id(
            validator,
            delete_sponsor_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sponsor_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f1196f1f6fde5978b0522f096926d443_v3_0_0').validate(obj.response)
    return True


def get_sponsor_group(api):
    endpoint_result = api.sponsor_group.get_sponsor_group(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_get_sponsor_group(api, validator):
    try:
        assert is_valid_get_sponsor_group(
            validator,
            get_sponsor_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_sponsor_group_default(api):
    endpoint_result = api.sponsor_group.get_sponsor_group(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_get_sponsor_group_default(api, validator):
    try:
        assert is_valid_get_sponsor_group(
            validator,
            get_sponsor_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sponsor_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_56311acd30d35ee2ae16ff23757de7d8_v3_0_0').validate(obj.response)
    return True


def create_sponsor_group(api):
    endpoint_result = api.sponsor_group.create_sponsor_group(
        active_validation=False,
        auto_notification=True,
        create_permissions={'canImportMultipleAccounts': True, 'importBatchSizeLimit': 0, 'canCreateRandomAccounts': True, 'randomBatchSizeLimit': 0, 'defaultUsernamePrefix': 'string', 'canSpecifyUsernamePrefix': True, 'canSetFutureStartDate': True, 'startDateFutureLimitDays': 0},
        description='string',
        guest_types=['string'],
        is_default_group=True,
        is_enabled=True,
        locations=['string'],
        manage_permission='string',
        member_groups=['string'],
        name='string',
        other_permissions={'canUpdateGuestContactInfo': True, 'canViewGuestPasswords': True, 'canSendSmsNotifications': True, 'canResetGuestPasswords': True, 'canExtendGuestAccounts': True, 'canDeleteGuestAccounts': True, 'canSuspendGuestAccounts': True, 'requireSuspensionReason': True, 'canReinstateSuspendedAccounts': True, 'canApproveSelfregGuests': True, 'limitApprovalToSponsorsGuests': True, 'canAccessViaRest': True},
        payload=None
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_create_sponsor_group(api, validator):
    try:
        assert is_valid_create_sponsor_group(
            validator,
            create_sponsor_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_sponsor_group_default(api):
    endpoint_result = api.sponsor_group.create_sponsor_group(
        active_validation=False,
        auto_notification=None,
        create_permissions=None,
        description=None,
        guest_types=None,
        is_default_group=None,
        is_enabled=None,
        locations=None,
        manage_permission=None,
        member_groups=None,
        name=None,
        other_permissions=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_create_sponsor_group_default(api, validator):
    try:
        assert is_valid_create_sponsor_group(
            validator,
            create_sponsor_group_default(api)
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
    json_schema_validate('jsd_e8d4001b740751e08cfc19e1fdc5fddf_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.sponsor_group.get_version(

    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_get_version(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_version_default(api):
    endpoint_result = api.sponsor_group.get_version(

    )
    return endpoint_result


@pytest.mark.sponsor_group
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
