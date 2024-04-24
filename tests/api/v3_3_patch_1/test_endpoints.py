# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI endpoints API fixtures and tests.

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


def is_valid_list_1(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_33977733578154648184bcb37d211030_v3_3_patch_1').validate(obj.response)
    return True


def list_1(api):
    endpoint_result = api.endpoints.list_1(
        filter='string',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_list_1(api, validator):
    try:
        assert is_valid_list_1(
            validator,
            list_1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def list_1_default(api):
    endpoint_result = api.endpoints.list_1(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_list_1_default(api, validator):
    try:
        assert is_valid_list_1(
            validator,
            list_1_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_end_point(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5175a51ed0d2536b9df3968e4773abe6_v3_3_patch_1').validate(obj.response)
    return True


def create_end_point(api):
    endpoint_result = api.endpoints.create_end_point(
        active_validation=False,
        connected_links={},
        custom_attributes={},
        description='string',
        device_type='string',
        group_id='string',
        hardware_revision='string',
        id='string',
        identity_store='string',
        identity_store_id='string',
        ip_address='string',
        mac='string',
        mdm_attributes={},
        name='string',
        payload=None,
        portal_user='string',
        product_id='string',
        profile_id='string',
        protocol='string',
        serial_number='string',
        software_revision='string',
        static_group_assignment=True,
        static_profile_assignment=True,
        vendor='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_create_end_point(api, validator):
    try:
        assert is_valid_create_end_point(
            validator,
            create_end_point(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_end_point_default(api):
    endpoint_result = api.endpoints.create_end_point(
        active_validation=False,
        connected_links=None,
        custom_attributes=None,
        description=None,
        device_type=None,
        group_id=None,
        hardware_revision=None,
        id=None,
        identity_store=None,
        identity_store_id=None,
        ip_address=None,
        mac=None,
        mdm_attributes=None,
        name=None,
        payload=None,
        portal_user=None,
        product_id=None,
        profile_id=None,
        protocol=None,
        serial_number=None,
        software_revision=None,
        static_group_assignment=None,
        static_profile_assignment=None,
        vendor=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_create_end_point_default(api, validator):
    try:
        assert is_valid_create_end_point(
            validator,
            create_end_point_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_bulk_end_points(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e076428d49535723a07a5bbcbcbd128d_v3_3_patch_1').validate(obj.response)
    return True


def update_bulk_end_points(api):
    endpoint_result = api.endpoints.update_bulk_end_points(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_update_bulk_end_points(api, validator):
    try:
        assert is_valid_update_bulk_end_points(
            validator,
            update_bulk_end_points(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_bulk_end_points_default(api):
    endpoint_result = api.endpoints.update_bulk_end_points(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_update_bulk_end_points_default(api, validator):
    try:
        assert is_valid_update_bulk_end_points(
            validator,
            update_bulk_end_points_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_bulk_end_points(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_64dcda215550553980db1cd60c7314a7_v3_3_patch_1').validate(obj.response)
    return True


def create_bulk_end_points(api):
    endpoint_result = api.endpoints.create_bulk_end_points(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_create_bulk_end_points(api, validator):
    try:
        assert is_valid_create_bulk_end_points(
            validator,
            create_bulk_end_points(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_bulk_end_points_default(api):
    endpoint_result = api.endpoints.create_bulk_end_points(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_create_bulk_end_points_default(api, validator):
    try:
        assert is_valid_create_bulk_end_points(
            validator,
            create_bulk_end_points_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_bulk_end_points(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0d43c525d23b5c4bba03a0c774d4d411_v3_3_patch_1').validate(obj.response)
    return True


def delete_bulk_end_points(api):
    endpoint_result = api.endpoints.delete_bulk_end_points(

    )
    return endpoint_result


@pytest.mark.endpoints
def test_delete_bulk_end_points(api, validator):
    try:
        assert is_valid_delete_bulk_end_points(
            validator,
            delete_bulk_end_points(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_bulk_end_points_default(api):
    endpoint_result = api.endpoints.delete_bulk_end_points(

    )
    return endpoint_result


@pytest.mark.endpoints
def test_delete_bulk_end_points_default(api, validator):
    try:
        assert is_valid_delete_bulk_end_points(
            validator,
            delete_bulk_end_points_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_type_summary(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_689e06db5cda5ba7b82f14cbd46d262c_v3_3_patch_1').validate(obj.response)
    return True


def get_device_type_summary(api):
    endpoint_result = api.endpoints.get_device_type_summary(

    )
    return endpoint_result


@pytest.mark.endpoints
def test_get_device_type_summary(api, validator):
    try:
        assert is_valid_get_device_type_summary(
            validator,
            get_device_type_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_device_type_summary_default(api):
    endpoint_result = api.endpoints.get_device_type_summary(

    )
    return endpoint_result


@pytest.mark.endpoints
def test_get_device_type_summary_default(api, validator):
    try:
        assert is_valid_get_device_type_summary(
            validator,
            get_device_type_summary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_1(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f190d005d391514e97e04abe777a25f6_v3_3_patch_1').validate(obj.response)
    return True


def get_1(api):
    endpoint_result = api.endpoints.get_1(
        value='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_get_1(api, validator):
    try:
        assert is_valid_get_1(
            validator,
            get_1(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_1_default(api):
    endpoint_result = api.endpoints.get_1(
        value='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_get_1_default(api, validator):
    try:
        assert is_valid_get_1(
            validator,
            get_1_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ced9c2b976d053d898d9867def5eef28_v3_3_patch_1').validate(obj.response)
    return True


def update_endpoint(api):
    endpoint_result = api.endpoints.update_endpoint(
        active_validation=False,
        connected_links={},
        custom_attributes={},
        description='string',
        device_type='string',
        group_id='string',
        hardware_revision='string',
        id='string',
        identity_store='string',
        identity_store_id='string',
        ip_address='string',
        mac='string',
        mdm_attributes={},
        name='string',
        payload=None,
        portal_user='string',
        product_id='string',
        profile_id='string',
        protocol='string',
        serial_number='string',
        software_revision='string',
        static_group_assignment=True,
        static_profile_assignment=True,
        value='string',
        vendor='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_update_endpoint(api, validator):
    try:
        assert is_valid_update_endpoint(
            validator,
            update_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_endpoint_default(api):
    endpoint_result = api.endpoints.update_endpoint(
        active_validation=False,
        value='string',
        connected_links=None,
        custom_attributes=None,
        description=None,
        device_type=None,
        group_id=None,
        hardware_revision=None,
        id=None,
        identity_store=None,
        identity_store_id=None,
        ip_address=None,
        mac=None,
        mdm_attributes=None,
        name=None,
        payload=None,
        portal_user=None,
        product_id=None,
        profile_id=None,
        protocol=None,
        serial_number=None,
        software_revision=None,
        static_group_assignment=None,
        static_profile_assignment=None,
        vendor=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_update_endpoint_default(api, validator):
    try:
        assert is_valid_update_endpoint(
            validator,
            update_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_71de74c081ab537aadfcb4843f33e4c7_v3_3_patch_1').validate(obj.response)
    return True


def delete_endpoint(api):
    endpoint_result = api.endpoints.delete_endpoint(
        value='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_delete_endpoint(api, validator):
    try:
        assert is_valid_delete_endpoint(
            validator,
            delete_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_endpoint_default(api):
    endpoint_result = api.endpoints.delete_endpoint(
        value='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_delete_endpoint_default(api, validator):
    try:
        assert is_valid_delete_endpoint(
            validator,
            delete_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_end_point_task(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_35a7b96eb91052e49e6fc7bfc499ba5f_v3_3_patch_1').validate(obj.response)
    return True


def create_end_point_task(api):
    endpoint_result = api.endpoints.create_end_point_task(
        active_validation=False,
        connected_links={},
        custom_attributes={},
        description='string',
        device_type='string',
        group_id='string',
        hardware_revision='string',
        id='string',
        identity_store='string',
        identity_store_id='string',
        ip_address='string',
        mac='string',
        mdm_attributes={},
        name='string',
        payload=None,
        portal_user='string',
        product_id='string',
        profile_id='string',
        protocol='string',
        serial_number='string',
        software_revision='string',
        static_group_assignment=True,
        static_profile_assignment=True,
        vendor='string'
    )
    return endpoint_result


@pytest.mark.endpoints
def test_create_end_point_task(api, validator):
    try:
        assert is_valid_create_end_point_task(
            validator,
            create_end_point_task(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_end_point_task_default(api):
    endpoint_result = api.endpoints.create_end_point_task(
        active_validation=False,
        connected_links=None,
        custom_attributes=None,
        description=None,
        device_type=None,
        group_id=None,
        hardware_revision=None,
        id=None,
        identity_store=None,
        identity_store_id=None,
        ip_address=None,
        mac=None,
        mdm_attributes=None,
        name=None,
        payload=None,
        portal_user=None,
        product_id=None,
        profile_id=None,
        protocol=None,
        serial_number=None,
        software_revision=None,
        static_group_assignment=None,
        static_profile_assignment=None,
        vendor=None
    )
    return endpoint_result


@pytest.mark.endpoints
def test_create_end_point_task_default(api, validator):
    try:
        assert is_valid_create_end_point_task(
            validator,
            create_end_point_task_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
