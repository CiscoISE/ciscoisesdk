# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI duo_identity_sync API fixtures and tests.

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


def is_valid_get_identitysync(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1df181ea3dcd56bfbe7f79ff573b5fc2_v3_3_patch_1').validate(obj.response)
    return True


def get_identitysync(api):
    endpoint_result = api.duo_identity_sync.get_identitysync(

    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_get_identitysync(api, validator):
    try:
        assert is_valid_get_identitysync(
            validator,
            get_identitysync(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_identitysync_default(api):
    endpoint_result = api.duo_identity_sync.get_identitysync(

    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_get_identitysync_default(api, validator):
    try:
        assert is_valid_get_identitysync(
            validator,
            get_identitysync_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_identitysync(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_69373c868f315159b4ba2bc7682c7887_v3_3_patch_1').validate(obj.response)
    return True


def create_identitysync(api):
    endpoint_result = api.duo_identity_sync.create_identitysync(
        active_validation=False,
        ad_groups=[{'name': 'string', 'source': 'string'}],
        configurations={'activeDirectories': [{'directoryID': 'string', 'domain': 'string', 'name': 'string'}]},
        last_sync='string',
        payload=None,
        sync_name='string',
        sync_schedule={'interval': 0, 'intervalUnit': 'string', 'schedulerSync': 'string', 'startDate': 'string'},
        sync_status='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_create_identitysync(api, validator):
    try:
        assert is_valid_create_identitysync(
            validator,
            create_identitysync(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_identitysync_default(api):
    endpoint_result = api.duo_identity_sync.create_identitysync(
        active_validation=False,
        ad_groups=None,
        configurations=None,
        last_sync=None,
        payload=None,
        sync_name=None,
        sync_schedule=None,
        sync_status=None
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_create_identitysync_default(api, validator):
    try:
        assert is_valid_create_identitysync(
            validator,
            create_identitysync_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1076d1e5dabd543288df5173b39fb8cf_v3_3_patch_1').validate(obj.response)
    return True


def update_status(api):
    endpoint_result = api.duo_identity_sync.update_status(
        active_validation=False,
        error_list=[{'reason': 'string', 'user': {'directoryname': 'string', 'email': 'string', 'firstname': 'string', 'groupname': 'string', 'lastname': 'string', 'notes': 'string', 'realname': 'string', 'status': 'string', 'username': 'string'}}],
        payload=None,
        status='string',
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_update_status(api, validator):
    try:
        assert is_valid_update_status(
            validator,
            update_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_status_default(api):
    endpoint_result = api.duo_identity_sync.update_status(
        active_validation=False,
        sync_name='string',
        error_list=None,
        payload=None,
        status=None
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_update_status_default(api, validator):
    try:
        assert is_valid_update_status(
            validator,
            update_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_cancel_sync(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_19763764ea97590ebf96ed2ccce5e19c_v3_3_patch_1').validate(obj.response)
    return True


def cancel_sync(api):
    endpoint_result = api.duo_identity_sync.cancel_sync(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_cancel_sync(api, validator):
    try:
        assert is_valid_cancel_sync(
            validator,
            cancel_sync(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def cancel_sync_default(api):
    endpoint_result = api.duo_identity_sync.cancel_sync(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_cancel_sync_default(api, validator):
    try:
        assert is_valid_cancel_sync(
            validator,
            cancel_sync_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e23a28af8006509c85271e07d522a12e_v3_3_patch_1').validate(obj.response)
    return True


def sync(api):
    endpoint_result = api.duo_identity_sync.sync(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_sync(api, validator):
    try:
        assert is_valid_sync(
            validator,
            sync(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def sync_default(api):
    endpoint_result = api.duo_identity_sync.sync(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_sync_default(api, validator):
    try:
        assert is_valid_sync(
            validator,
            sync_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_identitysync_by_sync_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4eceed7a4795587b812ca7d4fb71c1ad_v3_3_patch_1').validate(obj.response)
    return True


def get_identitysync_by_sync_name(api):
    endpoint_result = api.duo_identity_sync.get_identitysync_by_sync_name(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_get_identitysync_by_sync_name(api, validator):
    try:
        assert is_valid_get_identitysync_by_sync_name(
            validator,
            get_identitysync_by_sync_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_identitysync_by_sync_name_default(api):
    endpoint_result = api.duo_identity_sync.get_identitysync_by_sync_name(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_get_identitysync_by_sync_name_default(api, validator):
    try:
        assert is_valid_get_identitysync_by_sync_name(
            validator,
            get_identitysync_by_sync_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_identitysync_by_sync_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_28cd01786a6f5573be19bbd17a7a2561_v3_3_patch_1').validate(obj.response)
    return True


def update_identitysync_by_sync_name(api):
    endpoint_result = api.duo_identity_sync.update_identitysync_by_sync_name(
        active_validation=False,
        ad_groups=[{'name': 'string', 'source': 'string'}],
        configurations={'activeDirectories': [{'directoryID': 'string', 'domain': 'string', 'name': 'string'}]},
        last_sync='string',
        payload=None,
        sync_name='string',
        sync_schedule={'interval': 0, 'intervalUnit': 'string', 'schedulerSync': 'string', 'startDate': 'string'},
        sync_status='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_update_identitysync_by_sync_name(api, validator):
    try:
        assert is_valid_update_identitysync_by_sync_name(
            validator,
            update_identitysync_by_sync_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_identitysync_by_sync_name_default(api):
    endpoint_result = api.duo_identity_sync.update_identitysync_by_sync_name(
        active_validation=False,
        sync_name='string',
        ad_groups=None,
        configurations=None,
        last_sync=None,
        payload=None,
        sync_schedule=None,
        sync_status=None
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_update_identitysync_by_sync_name_default(api, validator):
    try:
        assert is_valid_update_identitysync_by_sync_name(
            validator,
            update_identitysync_by_sync_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_identity_sync_by_sync_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7a957abe42fe5ec4ba32c71309d30c12_v3_3_patch_1').validate(obj.response)
    return True


def delete_identity_sync_by_sync_name(api):
    endpoint_result = api.duo_identity_sync.delete_identity_sync_by_sync_name(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_delete_identity_sync_by_sync_name(api, validator):
    try:
        assert is_valid_delete_identity_sync_by_sync_name(
            validator,
            delete_identity_sync_by_sync_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_identity_sync_by_sync_name_default(api):
    endpoint_result = api.duo_identity_sync.delete_identity_sync_by_sync_name(
        sync_name='string'
    )
    return endpoint_result


@pytest.mark.duo_identity_sync
def test_delete_identity_sync_by_sync_name_default(api, validator):
    try:
        assert is_valid_delete_identity_sync_by_sync_name(
            validator,
            delete_identity_sync_by_sync_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
