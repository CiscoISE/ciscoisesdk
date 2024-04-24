# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sgt_range_reservation API fixtures and tests.

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


def is_valid_get_sgt_reserved_ranges(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ab239b1cb373585dab8b3d2a1755096a_v3_3_patch_1').validate(obj.response)
    return True


def get_sgt_reserved_ranges(api):
    endpoint_result = api.sgt_range_reservation.get_sgt_reserved_ranges(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_get_sgt_reserved_ranges(api, validator):
    try:
        assert is_valid_get_sgt_reserved_ranges(
            validator,
            get_sgt_reserved_ranges(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sgt_reserved_ranges_default(api):
    endpoint_result = api.sgt_range_reservation.get_sgt_reserved_ranges(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_get_sgt_reserved_ranges_default(api, validator):
    try:
        assert is_valid_get_sgt_reserved_ranges(
            validator,
            get_sgt_reserved_ranges_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reserve_sgt_range(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3c565815d18a5b2bbc5f64f935d322f1_v3_3_patch_1').validate(obj.response)
    return True


def reserve_sgt_range(api):
    endpoint_result = api.sgt_range_reservation.reserve_sgt_range(
        active_validation=False,
        client_name='string',
        number_of_tags=0,
        payload=None
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_reserve_sgt_range(api, validator):
    try:
        assert is_valid_reserve_sgt_range(
            validator,
            reserve_sgt_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def reserve_sgt_range_default(api):
    endpoint_result = api.sgt_range_reservation.reserve_sgt_range(
        active_validation=False,
        client_name=None,
        number_of_tags=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_reserve_sgt_range_default(api, validator):
    try:
        assert is_valid_reserve_sgt_range(
            validator,
            reserve_sgt_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sgt_reserved_range(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8955cf7b3b15569893114af795c1e8e2_v3_3_patch_1').validate(obj.response)
    return True


def get_sgt_reserved_range(api):
    endpoint_result = api.sgt_range_reservation.get_sgt_reserved_range(
        client_id='string'
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_get_sgt_reserved_range(api, validator):
    try:
        assert is_valid_get_sgt_reserved_range(
            validator,
            get_sgt_reserved_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sgt_reserved_range_default(api):
    endpoint_result = api.sgt_range_reservation.get_sgt_reserved_range(
        client_id='string'
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_get_sgt_reserved_range_default(api, validator):
    try:
        assert is_valid_get_sgt_reserved_range(
            validator,
            get_sgt_reserved_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_reserved_range(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_90c8c7bb726f53e7be3a2023aa3dda80_v3_3_patch_1').validate(obj.response)
    return True


def update_reserved_range(api):
    endpoint_result = api.sgt_range_reservation.update_reserved_range(
        active_validation=False,
        client_id='string',
        end_index=0,
        payload=None,
        start_index=0
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_update_reserved_range(api, validator):
    try:
        assert is_valid_update_reserved_range(
            validator,
            update_reserved_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_reserved_range_default(api):
    endpoint_result = api.sgt_range_reservation.update_reserved_range(
        active_validation=False,
        client_id='string',
        end_index=None,
        payload=None,
        start_index=None
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_update_reserved_range_default(api, validator):
    try:
        assert is_valid_update_reserved_range(
            validator,
            update_reserved_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sgt_reserve_range(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_086ca7d6274e5090be92eccb6facea16_v3_3_patch_1').validate(obj.response)
    return True


def delete_sgt_reserve_range(api):
    endpoint_result = api.sgt_range_reservation.delete_sgt_reserve_range(
        client_id='string'
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_delete_sgt_reserve_range(api, validator):
    try:
        assert is_valid_delete_sgt_reserve_range(
            validator,
            delete_sgt_reserve_range(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_sgt_reserve_range_default(api):
    endpoint_result = api.sgt_range_reservation.delete_sgt_reserve_range(
        client_id='string'
    )
    return endpoint_result


@pytest.mark.sgt_range_reservation
def test_delete_sgt_reserve_range_default(api, validator):
    try:
        assert is_valid_delete_sgt_reserve_range(
            validator,
            delete_sgt_reserve_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
