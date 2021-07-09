# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI identity_group API fixtures and tests.

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


def is_valid_get_all_identity_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9d904c521059563490c4a93871b33d51_v3_0_0').validate(obj.response)
    return True


def get_all_identity_groups(api):
    endpoint_result = api.identity_group.get_all_identity_groups(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_get_all_identity_groups(api, validator):
    try:
        assert is_valid_get_all_identity_groups(
            validator,
            get_all_identity_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_identity_groups_default(api):
    endpoint_result = api.identity_group.get_all_identity_groups(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.identity_group
def test_get_all_identity_groups_default(api, validator):
    try:
        assert is_valid_get_all_identity_groups(
            validator,
            get_all_identity_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_identity_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_592250bf19f653f9a5c48d1fb1890409_v3_0_0').validate(obj.response)
    return True


def create_identity_group(api):
    endpoint_result = api.identity_group.create_identity_group(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        parent='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_create_identity_group(api, validator):
    try:
        assert is_valid_create_identity_group(
            validator,
            create_identity_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_identity_group_default(api):
    endpoint_result = api.identity_group.create_identity_group(
        active_validation=False,
        description=None,
        id=None,
        name=None,
        payload=None,
        parent=None
    )
    return endpoint_result


@pytest.mark.identity_group
def test_create_identity_group_default(api, validator):
    try:
        assert is_valid_create_identity_group(
            validator,
            create_identity_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_identity_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_ca3df31c13b857e6b5dbc8357a8ab010_v3_0_0').validate(obj.response)
    return True


def get_identity_group_by_id(api):
    endpoint_result = api.identity_group.get_identity_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_get_identity_group_by_id(api, validator):
    try:
        assert is_valid_get_identity_group_by_id(
            validator,
            get_identity_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_identity_group_by_id_default(api):
    endpoint_result = api.identity_group.get_identity_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_get_identity_group_by_id_default(api, validator):
    try:
        assert is_valid_get_identity_group_by_id(
            validator,
            get_identity_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_identity_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1c0689e940ba5526946ad15976cc3365_v3_0_0').validate(obj.response)
    return True


def update_identity_group_by_id(api):
    endpoint_result = api.identity_group.update_identity_group_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        payload=None,
        parent='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_update_identity_group_by_id(api, validator):
    try:
        assert is_valid_update_identity_group_by_id(
            validator,
            update_identity_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_identity_group_by_id_default(api):
    endpoint_result = api.identity_group.update_identity_group_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        payload=None,
        parent=None
    )
    return endpoint_result


@pytest.mark.identity_group
def test_update_identity_group_by_id_default(api, validator):
    try:
        assert is_valid_update_identity_group_by_id(
            validator,
            update_identity_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_identity_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_20a6bb2c6d4551c69919aa599df53832_v3_0_0').validate(obj.response)
    return True


def delete_identity_group_by_id(api):
    endpoint_result = api.identity_group.delete_identity_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_delete_identity_group_by_id(api, validator):
    try:
        assert is_valid_delete_identity_group_by_id(
            validator,
            delete_identity_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_identity_group_by_id_default(api):
    endpoint_result = api.identity_group.delete_identity_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_delete_identity_group_by_id_default(api, validator):
    try:
        assert is_valid_delete_identity_group_by_id(
            validator,
            delete_identity_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_identity_group_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1f18bdd1938755409bf6db6b29e85d3a_v3_0_0').validate(obj.response)
    return True


def get_identity_group_by_name(api):
    endpoint_result = api.identity_group.get_identity_group_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_get_identity_group_by_name(api, validator):
    try:
        assert is_valid_get_identity_group_by_name(
            validator,
            get_identity_group_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_identity_group_by_name_default(api):
    endpoint_result = api.identity_group.get_identity_group_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.identity_group
def test_get_identity_group_by_name_default(api, validator):
    try:
        assert is_valid_get_identity_group_by_name(
            validator,
            get_identity_group_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
