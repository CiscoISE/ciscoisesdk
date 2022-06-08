# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI tacacs_profile API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1_Patch_1', reason='version does not match')


def is_valid_get_tacacs_profile_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3578b8696d875b12b0a3ab735b397d7a_v3_1_patch_1').validate(obj.response)
    return True


def get_tacacs_profile_by_name(api):
    endpoint_result = api.tacacs_profile.get_tacacs_profile_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_get_tacacs_profile_by_name(api, validator):
    try:
        assert is_valid_get_tacacs_profile_by_name(
            validator,
            get_tacacs_profile_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_tacacs_profile_by_name_default(api):
    endpoint_result = api.tacacs_profile.get_tacacs_profile_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_get_tacacs_profile_by_name_default(api, validator):
    try:
        assert is_valid_get_tacacs_profile_by_name(
            validator,
            get_tacacs_profile_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tacacs_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bdea52558473565c9963ec14c65727b8_v3_1_patch_1').validate(obj.response)
    return True


def get_tacacs_profile_by_id(api):
    endpoint_result = api.tacacs_profile.get_tacacs_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_get_tacacs_profile_by_id(api, validator):
    try:
        assert is_valid_get_tacacs_profile_by_id(
            validator,
            get_tacacs_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_tacacs_profile_by_id_default(api):
    endpoint_result = api.tacacs_profile.get_tacacs_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_get_tacacs_profile_by_id_default(api, validator):
    try:
        assert is_valid_get_tacacs_profile_by_id(
            validator,
            get_tacacs_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_tacacs_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4a0db9ec45c05879a6f016a1edf54793_v3_1_patch_1').validate(obj.response)
    return True


def update_tacacs_profile_by_id(api):
    endpoint_result = api.tacacs_profile.update_tacacs_profile_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        session_attributes={'sessionAttributeList': [{'type': 'string', 'name': 'string', 'value': 'string'}]}
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_update_tacacs_profile_by_id(api, validator):
    try:
        assert is_valid_update_tacacs_profile_by_id(
            validator,
            update_tacacs_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_tacacs_profile_by_id_default(api):
    endpoint_result = api.tacacs_profile.update_tacacs_profile_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        payload=None,
        session_attributes=None
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_update_tacacs_profile_by_id_default(api, validator):
    try:
        assert is_valid_update_tacacs_profile_by_id(
            validator,
            update_tacacs_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_tacacs_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9fd38182c505549fbc0d8c1122c1f685_v3_1_patch_1').validate(obj.response)
    return True


def delete_tacacs_profile_by_id(api):
    endpoint_result = api.tacacs_profile.delete_tacacs_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_delete_tacacs_profile_by_id(api, validator):
    try:
        assert is_valid_delete_tacacs_profile_by_id(
            validator,
            delete_tacacs_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_tacacs_profile_by_id_default(api):
    endpoint_result = api.tacacs_profile.delete_tacacs_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_delete_tacacs_profile_by_id_default(api, validator):
    try:
        assert is_valid_delete_tacacs_profile_by_id(
            validator,
            delete_tacacs_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tacacs_profile(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ffff1c792bf559ebb39b789421be6966_v3_1_patch_1').validate(obj.response)
    return True


def get_tacacs_profile(api):
    endpoint_result = api.tacacs_profile.get_tacacs_profile(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_get_tacacs_profile(api, validator):
    try:
        assert is_valid_get_tacacs_profile(
            validator,
            get_tacacs_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_tacacs_profile_default(api):
    endpoint_result = api.tacacs_profile.get_tacacs_profile(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_get_tacacs_profile_default(api, validator):
    try:
        assert is_valid_get_tacacs_profile(
            validator,
            get_tacacs_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_tacacs_profile(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c094086382485201ad36d4641fc6822e_v3_1_patch_1').validate(obj.response)
    return True


def create_tacacs_profile(api):
    endpoint_result = api.tacacs_profile.create_tacacs_profile(
        active_validation=False,
        description='string',
        name='string',
        payload=None,
        session_attributes={'sessionAttributeList': [{'type': 'string', 'name': 'string', 'value': 'string'}]}
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_create_tacacs_profile(api, validator):
    try:
        assert is_valid_create_tacacs_profile(
            validator,
            create_tacacs_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_tacacs_profile_default(api):
    endpoint_result = api.tacacs_profile.create_tacacs_profile(
        active_validation=False,
        description=None,
        name=None,
        payload=None,
        session_attributes=None
    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_create_tacacs_profile_default(api, validator):
    try:
        assert is_valid_create_tacacs_profile(
            validator,
            create_tacacs_profile_default(api)
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
    json_schema_validate('jsd_17b22259a4415709a97bd2b7646f734f_v3_1_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.tacacs_profile.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_profile
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
    endpoint_result = api.tacacs_profile.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_profile
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
