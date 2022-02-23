# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sg_vn_mapping API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.1', reason='version does not match')


def is_valid_get_sg_vn_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e69e3338166d5c1887e5fa82efb72a11_v3_1_1').validate(obj.response)
    return True


def get_sg_vn_mappings(api):
    endpoint_result = api.sg_vn_mapping.get_sg_vn_mappings(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_get_sg_vn_mappings(api, validator):
    try:
        assert is_valid_get_sg_vn_mappings(
            validator,
            get_sg_vn_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sg_vn_mappings_default(api):
    endpoint_result = api.sg_vn_mapping.get_sg_vn_mappings(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_get_sg_vn_mappings_default(api, validator):
    try:
        assert is_valid_get_sg_vn_mappings(
            validator,
            get_sg_vn_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sg_vn_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_018b050fff6a5302ace3e16674c8b19a_v3_1_1').validate(obj.response)
    return True


def create_sg_vn_mapping(api):
    endpoint_result = api.sg_vn_mapping.create_sg_vn_mapping(
        active_validation=False,
        id='string',
        last_update='string',
        payload=None,
        sg_name='string',
        sgt_id='string',
        vn_id='string',
        vn_name='string'
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_create_sg_vn_mapping(api, validator):
    try:
        assert is_valid_create_sg_vn_mapping(
            validator,
            create_sg_vn_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_sg_vn_mapping_default(api):
    endpoint_result = api.sg_vn_mapping.create_sg_vn_mapping(
        active_validation=False,
        id=None,
        last_update=None,
        payload=None,
        sg_name=None,
        sgt_id=None,
        vn_id=None,
        vn_name=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_create_sg_vn_mapping_default(api, validator):
    try:
        assert is_valid_create_sg_vn_mapping(
            validator,
            create_sg_vn_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_create_sg_vn_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3e81b5f00f35577dbad11186f70f25be_v3_1_1').validate(obj.response)
    return True


def bulk_create_sg_vn_mappings(api):
    endpoint_result = api.sg_vn_mapping.bulk_create_sg_vn_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_bulk_create_sg_vn_mappings(api, validator):
    try:
        assert is_valid_bulk_create_sg_vn_mappings(
            validator,
            bulk_create_sg_vn_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_create_sg_vn_mappings_default(api):
    endpoint_result = api.sg_vn_mapping.bulk_create_sg_vn_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_bulk_create_sg_vn_mappings_default(api, validator):
    try:
        assert is_valid_bulk_create_sg_vn_mappings(
            validator,
            bulk_create_sg_vn_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_delete_sg_vn_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3c5cad090a875d9d8bd87e59654c9d75_v3_1_1').validate(obj.response)
    return True


def bulk_delete_sg_vn_mappings(api):
    endpoint_result = api.sg_vn_mapping.bulk_delete_sg_vn_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_bulk_delete_sg_vn_mappings(api, validator):
    try:
        assert is_valid_bulk_delete_sg_vn_mappings(
            validator,
            bulk_delete_sg_vn_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_delete_sg_vn_mappings_default(api):
    endpoint_result = api.sg_vn_mapping.bulk_delete_sg_vn_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_bulk_delete_sg_vn_mappings_default(api, validator):
    try:
        assert is_valid_bulk_delete_sg_vn_mappings(
            validator,
            bulk_delete_sg_vn_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_update_sg_vn_mappings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_80c9c798a8ce58b88b3231575f5b8c98_v3_1_1').validate(obj.response)
    return True


def bulk_update_sg_vn_mappings(api):
    endpoint_result = api.sg_vn_mapping.bulk_update_sg_vn_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_bulk_update_sg_vn_mappings(api, validator):
    try:
        assert is_valid_bulk_update_sg_vn_mappings(
            validator,
            bulk_update_sg_vn_mappings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_update_sg_vn_mappings_default(api):
    endpoint_result = api.sg_vn_mapping.bulk_update_sg_vn_mappings(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_bulk_update_sg_vn_mappings_default(api, validator):
    try:
        assert is_valid_bulk_update_sg_vn_mappings(
            validator,
            bulk_update_sg_vn_mappings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sg_vn_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8fceb2944abb59e2a748b970ee79fbb7_v3_1_1').validate(obj.response)
    return True


def get_sg_vn_mapping_by_id(api):
    endpoint_result = api.sg_vn_mapping.get_sg_vn_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_get_sg_vn_mapping_by_id(api, validator):
    try:
        assert is_valid_get_sg_vn_mapping_by_id(
            validator,
            get_sg_vn_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sg_vn_mapping_by_id_default(api):
    endpoint_result = api.sg_vn_mapping.get_sg_vn_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_get_sg_vn_mapping_by_id_default(api, validator):
    try:
        assert is_valid_get_sg_vn_mapping_by_id(
            validator,
            get_sg_vn_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sg_vn_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_147075a66f9651fca28e85b97cf1b968_v3_1_1').validate(obj.response)
    return True


def update_sg_vn_mapping_by_id(api):
    endpoint_result = api.sg_vn_mapping.update_sg_vn_mapping_by_id(
        active_validation=False,
        id='string',
        last_update='string',
        payload=None,
        sg_name='string',
        sgt_id='string',
        vn_id='string',
        vn_name='string'
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_update_sg_vn_mapping_by_id(api, validator):
    try:
        assert is_valid_update_sg_vn_mapping_by_id(
            validator,
            update_sg_vn_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_sg_vn_mapping_by_id_default(api):
    endpoint_result = api.sg_vn_mapping.update_sg_vn_mapping_by_id(
        active_validation=False,
        id='string',
        last_update=None,
        payload=None,
        sg_name=None,
        sgt_id=None,
        vn_id=None,
        vn_name=None
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_update_sg_vn_mapping_by_id_default(api, validator):
    try:
        assert is_valid_update_sg_vn_mapping_by_id(
            validator,
            update_sg_vn_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sg_vn_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0718cb6b83a55dfb8f3536b43cfaf081_v3_1_1').validate(obj.response)
    return True


def delete_sg_vn_mapping_by_id(api):
    endpoint_result = api.sg_vn_mapping.delete_sg_vn_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_delete_sg_vn_mapping_by_id(api, validator):
    try:
        assert is_valid_delete_sg_vn_mapping_by_id(
            validator,
            delete_sg_vn_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_sg_vn_mapping_by_id_default(api):
    endpoint_result = api.sg_vn_mapping.delete_sg_vn_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sg_vn_mapping
def test_delete_sg_vn_mapping_by_id_default(api, validator):
    try:
        assert is_valid_delete_sg_vn_mapping_by_id(
            validator,
            delete_sg_vn_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
