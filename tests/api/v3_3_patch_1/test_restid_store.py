# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI restid_store API fixtures and tests.

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


def is_valid_get_rest_id_store_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_48c47e28f13659658b3e6af9409a1177_v3_3_patch_1').validate(obj.response)
    return True


def get_rest_id_store_by_name(api):
    endpoint_result = api.restid_store.get_rest_id_store_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_get_rest_id_store_by_name(api, validator):
    try:
        assert is_valid_get_rest_id_store_by_name(
            validator,
            get_rest_id_store_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_rest_id_store_by_name_default(api):
    endpoint_result = api.restid_store.get_rest_id_store_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_get_rest_id_store_by_name_default(api, validator):
    try:
        assert is_valid_get_rest_id_store_by_name(
            validator,
            get_rest_id_store_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_rest_id_store_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d0e432f52e2a5863858c7dc0c3eda277_v3_3_patch_1').validate(obj.response)
    return True


def update_rest_id_store_by_name(api):
    endpoint_result = api.restid_store.update_rest_id_store_by_name(
        active_validation=False,
        description='string',
        ers_rest_idstore_attributes={'usernameSuffix': 'string', 'rootUrl': 'string', 'predefined': 'string', 'headers': [{'key': 'string', 'value': 'string'}]},
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_update_rest_id_store_by_name(api, validator):
    try:
        assert is_valid_update_rest_id_store_by_name(
            validator,
            update_rest_id_store_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_rest_id_store_by_name_default(api):
    endpoint_result = api.restid_store.update_rest_id_store_by_name(
        active_validation=False,
        name='string',
        description=None,
        ers_rest_idstore_attributes=None,
        id=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_update_rest_id_store_by_name_default(api, validator):
    try:
        assert is_valid_update_rest_id_store_by_name(
            validator,
            update_rest_id_store_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_rest_id_store_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_fe53fb8359725e40ac431d41e1487626_v3_3_patch_1').validate(obj.response)
    return True


def delete_rest_id_store_by_name(api):
    endpoint_result = api.restid_store.delete_rest_id_store_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_delete_rest_id_store_by_name(api, validator):
    try:
        assert is_valid_delete_rest_id_store_by_name(
            validator,
            delete_rest_id_store_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_rest_id_store_by_name_default(api):
    endpoint_result = api.restid_store.delete_rest_id_store_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_delete_rest_id_store_by_name_default(api, validator):
    try:
        assert is_valid_delete_rest_id_store_by_name(
            validator,
            delete_rest_id_store_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rest_id_store_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_788cba3f7ace597da668acfbe00364be_v3_3_patch_1').validate(obj.response)
    return True


def get_rest_id_store_by_id(api):
    endpoint_result = api.restid_store.get_rest_id_store_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_get_rest_id_store_by_id(api, validator):
    try:
        assert is_valid_get_rest_id_store_by_id(
            validator,
            get_rest_id_store_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_rest_id_store_by_id_default(api):
    endpoint_result = api.restid_store.get_rest_id_store_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_get_rest_id_store_by_id_default(api, validator):
    try:
        assert is_valid_get_rest_id_store_by_id(
            validator,
            get_rest_id_store_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_rest_id_store_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ded7f8573c255c318bb1f04bfdbf01e1_v3_3_patch_1').validate(obj.response)
    return True


def update_rest_id_store_by_id(api):
    endpoint_result = api.restid_store.update_rest_id_store_by_id(
        active_validation=False,
        description='string',
        ers_rest_idstore_attributes={'usernameSuffix': 'string', 'rootUrl': 'string', 'predefined': 'string', 'headers': [{'key': 'string', 'value': 'string'}]},
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_update_rest_id_store_by_id(api, validator):
    try:
        assert is_valid_update_rest_id_store_by_id(
            validator,
            update_rest_id_store_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_rest_id_store_by_id_default(api):
    endpoint_result = api.restid_store.update_rest_id_store_by_id(
        active_validation=False,
        id='string',
        description=None,
        ers_rest_idstore_attributes=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_update_rest_id_store_by_id_default(api, validator):
    try:
        assert is_valid_update_rest_id_store_by_id(
            validator,
            update_rest_id_store_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_rest_id_store_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2e77a1dd4aa75dcebbc3ee4e94a162b4_v3_3_patch_1').validate(obj.response)
    return True


def delete_rest_id_store_by_id(api):
    endpoint_result = api.restid_store.delete_rest_id_store_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_delete_rest_id_store_by_id(api, validator):
    try:
        assert is_valid_delete_rest_id_store_by_id(
            validator,
            delete_rest_id_store_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_rest_id_store_by_id_default(api):
    endpoint_result = api.restid_store.delete_rest_id_store_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_delete_rest_id_store_by_id_default(api, validator):
    try:
        assert is_valid_delete_rest_id_store_by_id(
            validator,
            delete_rest_id_store_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rest_id_store(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d810359e31e453ac8145981b7d5bb7e4_v3_3_patch_1').validate(obj.response)
    return True


def get_rest_id_store(api):
    endpoint_result = api.restid_store.get_rest_id_store(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.restid_store
def test_get_rest_id_store(api, validator):
    try:
        assert is_valid_get_rest_id_store(
            validator,
            get_rest_id_store(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_rest_id_store_default(api):
    endpoint_result = api.restid_store.get_rest_id_store(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_get_rest_id_store_default(api, validator):
    try:
        assert is_valid_get_rest_id_store(
            validator,
            get_rest_id_store_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_rest_id_store(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1073c23243c950f29b51f502c03d7058_v3_3_patch_1').validate(obj.response)
    return True


def create_rest_id_store(api):
    endpoint_result = api.restid_store.create_rest_id_store(
        active_validation=False,
        description='string',
        ers_rest_idstore_attributes={'usernameSuffix': 'string', 'rootUrl': 'string', 'predefined': 'string', 'headers': [{'key': 'string', 'value': 'string'}]},
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_create_rest_id_store(api, validator):
    try:
        assert is_valid_create_rest_id_store(
            validator,
            create_rest_id_store(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_rest_id_store_default(api):
    endpoint_result = api.restid_store.create_rest_id_store(
        active_validation=False,
        description=None,
        ers_rest_idstore_attributes=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_create_rest_id_store_default(api, validator):
    try:
        assert is_valid_create_rest_id_store(
            validator,
            create_rest_id_store_default(api)
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
    json_schema_validate('jsd_1b8c3846fcf751e4b008eb0a011dea4d_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.restid_store.get_version(

    )
    return endpoint_result


@pytest.mark.restid_store
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
    endpoint_result = api.restid_store.get_version(

    )
    return endpoint_result


@pytest.mark.restid_store
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_restid_store_name_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_fced674832255f00b1d01cd38d378bf1_v3_3_patch_1').validate(obj.response)
    return True


def patch_restid_store_name_name(api):
    endpoint_result = api.restid_store.patch_restid_store_name_name(
        active_validation=False,
        description='string',
        ers_rest_idstore_advance_settings={'deviceQuerySetting': {}, 'identifyDeviceCertificate': {}, 'subjectNameFormat': 'string', 'sanAttribute': {}, 'sanAttributeValue': 'string'},
        ers_rest_idstore_attributes={'usernameSuffix': 'string', 'rootUrl': 'string', 'predefined': {}, 'headers': [{'key': 'string', 'value': 'string'}]},
        ers_rest_idstore_device_attributes={'name': 'string'},
        ers_rest_idstore_user_attributes={'name': 'string'},
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_patch_restid_store_name_name(api, validator):
    try:
        assert is_valid_patch_restid_store_name_name(
            validator,
            patch_restid_store_name_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_restid_store_name_name_default(api):
    endpoint_result = api.restid_store.patch_restid_store_name_name(
        active_validation=False,
        name='string',
        description=None,
        ers_rest_idstore_advance_settings=None,
        ers_rest_idstore_attributes=None,
        ers_rest_idstore_device_attributes=None,
        ers_rest_idstore_user_attributes=None,
        id=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_patch_restid_store_name_name_default(api, validator):
    try:
        assert is_valid_patch_restid_store_name_name(
            validator,
            patch_restid_store_name_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_restid_store_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9043fe2adcd154a1862a3400b89a52b7_v3_3_patch_1').validate(obj.response)
    return True


def patch_restid_store_id(api):
    endpoint_result = api.restid_store.patch_restid_store_id(
        active_validation=False,
        description='string',
        ers_rest_idstore_advance_settings={'deviceQuerySetting': {}, 'identifyDeviceCertificate': {}, 'subjectNameFormat': 'string', 'sanAttribute': {}, 'sanAttributeValue': 'string'},
        ers_rest_idstore_attributes={'usernameSuffix': 'string', 'rootUrl': 'string', 'predefined': {}, 'headers': [{'key': 'string', 'value': 'string'}]},
        ers_rest_idstore_device_attributes={'name': 'string'},
        ers_rest_idstore_user_attributes={'name': 'string'},
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_patch_restid_store_id(api, validator):
    try:
        assert is_valid_patch_restid_store_id(
            validator,
            patch_restid_store_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_restid_store_id_default(api):
    endpoint_result = api.restid_store.patch_restid_store_id(
        active_validation=False,
        id='string',
        description=None,
        ers_rest_idstore_advance_settings=None,
        ers_rest_idstore_attributes=None,
        ers_rest_idstore_device_attributes=None,
        ers_rest_idstore_user_attributes=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.restid_store
def test_patch_restid_store_id_default(api, validator):
    try:
        assert is_valid_patch_restid_store_id(
            validator,
            patch_restid_store_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
