# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI internal_user API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_internal_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7f403dda9440503191536993f569cc6f_v3_1_0').validate(obj.response)
    return True


def get_internal_user_by_name(api):
    endpoint_result = api.internal_user.get_internal_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_get_internal_user_by_name(api, validator):
    try:
        assert is_valid_get_internal_user_by_name(
            validator,
            get_internal_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_internal_user_by_name_default(api):
    endpoint_result = api.internal_user.get_internal_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_get_internal_user_by_name_default(api, validator):
    try:
        assert is_valid_get_internal_user_by_name(
            validator,
            get_internal_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_internal_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4758008519d9509db339e3b27dc56b37_v3_1_0').validate(obj.response)
    return True


def update_internal_user_by_name(api):
    endpoint_result = api.internal_user.update_internal_user_by_name(
        active_validation=False,
        change_password=True,
        custom_attributes={},
        description='string',
        email='string',
        enable_password='string',
        enabled=True,
        expiry_date='string',
        expiry_date_enabled=True,
        first_name='string',
        id='string',
        identity_groups='string',
        last_name='string',
        name='string',
        password='string',
        password_idstore='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.internal_user
def test_update_internal_user_by_name(api, validator):
    try:
        assert is_valid_update_internal_user_by_name(
            validator,
            update_internal_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_internal_user_by_name_default(api):
    endpoint_result = api.internal_user.update_internal_user_by_name(
        active_validation=False,
        name='string',
        change_password=None,
        custom_attributes=None,
        description=None,
        email=None,
        enable_password=None,
        enabled=None,
        expiry_date=None,
        expiry_date_enabled=None,
        first_name=None,
        id=None,
        identity_groups=None,
        last_name=None,
        password=None,
        password_idstore=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.internal_user
def test_update_internal_user_by_name_default(api, validator):
    try:
        assert is_valid_update_internal_user_by_name(
            validator,
            update_internal_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_internal_user_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2447b4e2fc3e595aa1be86d6589614b9_v3_1_0').validate(obj.response)
    return True


def delete_internal_user_by_name(api):
    endpoint_result = api.internal_user.delete_internal_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_delete_internal_user_by_name(api, validator):
    try:
        assert is_valid_delete_internal_user_by_name(
            validator,
            delete_internal_user_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_internal_user_by_name_default(api):
    endpoint_result = api.internal_user.delete_internal_user_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_delete_internal_user_by_name_default(api, validator):
    try:
        assert is_valid_delete_internal_user_by_name(
            validator,
            delete_internal_user_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_internal_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bacf1abfc35e509183c9a7f055cbbfec_v3_1_0').validate(obj.response)
    return True


def get_internal_user_by_id(api):
    endpoint_result = api.internal_user.get_internal_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_get_internal_user_by_id(api, validator):
    try:
        assert is_valid_get_internal_user_by_id(
            validator,
            get_internal_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_internal_user_by_id_default(api):
    endpoint_result = api.internal_user.get_internal_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_get_internal_user_by_id_default(api, validator):
    try:
        assert is_valid_get_internal_user_by_id(
            validator,
            get_internal_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_internal_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f7227b280b745b94bb801369b168a529_v3_1_0').validate(obj.response)
    return True


def update_internal_user_by_id(api):
    endpoint_result = api.internal_user.update_internal_user_by_id(
        active_validation=False,
        change_password=True,
        custom_attributes={},
        description='string',
        email='string',
        enable_password='string',
        enabled=True,
        expiry_date='string',
        expiry_date_enabled=True,
        first_name='string',
        id='string',
        identity_groups='string',
        last_name='string',
        name='string',
        password='string',
        password_idstore='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.internal_user
def test_update_internal_user_by_id(api, validator):
    try:
        assert is_valid_update_internal_user_by_id(
            validator,
            update_internal_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_internal_user_by_id_default(api):
    endpoint_result = api.internal_user.update_internal_user_by_id(
        active_validation=False,
        id='string',
        change_password=None,
        custom_attributes=None,
        description=None,
        email=None,
        enable_password=None,
        enabled=None,
        expiry_date=None,
        expiry_date_enabled=None,
        first_name=None,
        identity_groups=None,
        last_name=None,
        name=None,
        password=None,
        password_idstore=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.internal_user
def test_update_internal_user_by_id_default(api, validator):
    try:
        assert is_valid_update_internal_user_by_id(
            validator,
            update_internal_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_internal_user_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_dcf28db5184e51139b15f9ffccd10b67_v3_1_0').validate(obj.response)
    return True


def delete_internal_user_by_id(api):
    endpoint_result = api.internal_user.delete_internal_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_delete_internal_user_by_id(api, validator):
    try:
        assert is_valid_delete_internal_user_by_id(
            validator,
            delete_internal_user_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_internal_user_by_id_default(api):
    endpoint_result = api.internal_user.delete_internal_user_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_delete_internal_user_by_id_default(api, validator):
    try:
        assert is_valid_delete_internal_user_by_id(
            validator,
            delete_internal_user_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_internal_user(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3ccba98a61555ae495f6a05284e3b5ae_v3_1_0').validate(obj.response)
    return True


def get_internal_user(api):
    endpoint_result = api.internal_user.get_internal_user(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.internal_user
def test_get_internal_user(api, validator):
    try:
        assert is_valid_get_internal_user(
            validator,
            get_internal_user(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_internal_user_default(api):
    endpoint_result = api.internal_user.get_internal_user(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.internal_user
def test_get_internal_user_default(api, validator):
    try:
        assert is_valid_get_internal_user(
            validator,
            get_internal_user_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_internal_user(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bf175c04fcb051b9a6fd70a2252903fa_v3_1_0').validate(obj.response)
    return True


def create_internal_user(api):
    endpoint_result = api.internal_user.create_internal_user(
        active_validation=False,
        change_password=True,
        custom_attributes={},
        description='string',
        email='string',
        enable_password='string',
        enabled=True,
        expiry_date='string',
        expiry_date_enabled=True,
        first_name='string',
        identity_groups='string',
        last_name='string',
        name='string',
        password='string',
        password_idstore='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.internal_user
def test_create_internal_user(api, validator):
    try:
        assert is_valid_create_internal_user(
            validator,
            create_internal_user(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_internal_user_default(api):
    endpoint_result = api.internal_user.create_internal_user(
        active_validation=False,
        change_password=None,
        custom_attributes=None,
        description=None,
        email=None,
        enable_password=None,
        enabled=None,
        expiry_date=None,
        expiry_date_enabled=None,
        first_name=None,
        identity_groups=None,
        last_name=None,
        name=None,
        password=None,
        password_idstore=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.internal_user
def test_create_internal_user_default(api, validator):
    try:
        assert is_valid_create_internal_user(
            validator,
            create_internal_user_default(api)
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
    json_schema_validate('jsd_2af99828533e58a2b84996b85bacc9ff_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.internal_user.get_version(

    )
    return endpoint_result


@pytest.mark.internal_user
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
    endpoint_result = api.internal_user.get_version(

    )
    return endpoint_result


@pytest.mark.internal_user
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
