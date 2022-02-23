# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI identity_sequence API fixtures and tests.

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


def is_valid_get_identity_sequence_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_db686413cf4558188ea60ccc05c3e920_v3_1_0').validate(obj.response)
    return True


def get_identity_sequence_by_name(api):
    endpoint_result = api.identity_sequence.get_identity_sequence_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_get_identity_sequence_by_name(api, validator):
    try:
        assert is_valid_get_identity_sequence_by_name(
            validator,
            get_identity_sequence_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_identity_sequence_by_name_default(api):
    endpoint_result = api.identity_sequence.get_identity_sequence_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_get_identity_sequence_by_name_default(api, validator):
    try:
        assert is_valid_get_identity_sequence_by_name(
            validator,
            get_identity_sequence_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_identity_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_45cb9345e58f5433ae80f5d8f855978b_v3_1_0').validate(obj.response)
    return True


def get_identity_sequence_by_id(api):
    endpoint_result = api.identity_sequence.get_identity_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_get_identity_sequence_by_id(api, validator):
    try:
        assert is_valid_get_identity_sequence_by_id(
            validator,
            get_identity_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_identity_sequence_by_id_default(api):
    endpoint_result = api.identity_sequence.get_identity_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_get_identity_sequence_by_id_default(api, validator):
    try:
        assert is_valid_get_identity_sequence_by_id(
            validator,
            get_identity_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_identity_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9c316d5e2fdd51bdab039ea9e2a417bd_v3_1_0').validate(obj.response)
    return True


def update_identity_sequence_by_id(api):
    endpoint_result = api.identity_sequence.update_identity_sequence_by_id(
        active_validation=False,
        break_on_store_fail=True,
        certificate_authentication_profile='string',
        description='string',
        id='string',
        id_seq_item=[{'idstore': 'string', 'order': 0}],
        name='string',
        parent='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_update_identity_sequence_by_id(api, validator):
    try:
        assert is_valid_update_identity_sequence_by_id(
            validator,
            update_identity_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_identity_sequence_by_id_default(api):
    endpoint_result = api.identity_sequence.update_identity_sequence_by_id(
        active_validation=False,
        id='string',
        break_on_store_fail=None,
        certificate_authentication_profile=None,
        description=None,
        id_seq_item=None,
        name=None,
        parent=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_update_identity_sequence_by_id_default(api, validator):
    try:
        assert is_valid_update_identity_sequence_by_id(
            validator,
            update_identity_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_identity_sequence_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2b8258803668534d87781e995c73c23a_v3_1_0').validate(obj.response)
    return True


def delete_identity_sequence_by_id(api):
    endpoint_result = api.identity_sequence.delete_identity_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_delete_identity_sequence_by_id(api, validator):
    try:
        assert is_valid_delete_identity_sequence_by_id(
            validator,
            delete_identity_sequence_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_identity_sequence_by_id_default(api):
    endpoint_result = api.identity_sequence.delete_identity_sequence_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_delete_identity_sequence_by_id_default(api, validator):
    try:
        assert is_valid_delete_identity_sequence_by_id(
            validator,
            delete_identity_sequence_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_identity_sequence(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_feb30ca768795eed82c118d009d7bcd4_v3_1_0').validate(obj.response)
    return True


def get_identity_sequence(api):
    endpoint_result = api.identity_sequence.get_identity_sequence(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_get_identity_sequence(api, validator):
    try:
        assert is_valid_get_identity_sequence(
            validator,
            get_identity_sequence(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_identity_sequence_default(api):
    endpoint_result = api.identity_sequence.get_identity_sequence(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_get_identity_sequence_default(api, validator):
    try:
        assert is_valid_get_identity_sequence(
            validator,
            get_identity_sequence_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_identity_sequence(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6cc0a87094bf5d96af61403dfc3747db_v3_1_0').validate(obj.response)
    return True


def create_identity_sequence(api):
    endpoint_result = api.identity_sequence.create_identity_sequence(
        active_validation=False,
        break_on_store_fail=True,
        certificate_authentication_profile='string',
        description='string',
        id_seq_item=[{'idstore': 'string', 'order': 0}],
        name='string',
        parent='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_create_identity_sequence(api, validator):
    try:
        assert is_valid_create_identity_sequence(
            validator,
            create_identity_sequence(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_identity_sequence_default(api):
    endpoint_result = api.identity_sequence.create_identity_sequence(
        active_validation=False,
        break_on_store_fail=None,
        certificate_authentication_profile=None,
        description=None,
        id_seq_item=None,
        name=None,
        parent=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_create_identity_sequence_default(api, validator):
    try:
        assert is_valid_create_identity_sequence(
            validator,
            create_identity_sequence_default(api)
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
    json_schema_validate('jsd_dc4c840ad93e53d591ca3a39184e6dde_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.identity_sequence.get_version(

    )
    return endpoint_result


@pytest.mark.identity_sequence
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
    endpoint_result = api.identity_sequence.get_version(

    )
    return endpoint_result


@pytest.mark.identity_sequence
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
