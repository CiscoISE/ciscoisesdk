# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI ip_to_sgt_mapping_group API fixtures and tests.

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


def is_valid_deploy_ip_to_sgt_mapping_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bd7f3fb27d71596ebafecca578c85bc7_v3_0_0').validate(obj.response)
    return True


def deploy_ip_to_sgt_mapping_group_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping_group.deploy_ip_to_sgt_mapping_group_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_deploy_ip_to_sgt_mapping_group_by_id(api, validator):
    try:
        assert is_valid_deploy_ip_to_sgt_mapping_group_by_id(
            validator,
            deploy_ip_to_sgt_mapping_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_ip_to_sgt_mapping_group_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.deploy_ip_to_sgt_mapping_group_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_deploy_ip_to_sgt_mapping_group_by_id_default(api, validator):
    try:
        assert is_valid_deploy_ip_to_sgt_mapping_group_by_id(
            validator,
            deploy_ip_to_sgt_mapping_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_all_ip_to_sgt_mapping_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0b8ef94d6d5554a4b57d37c52612ad7d_v3_0_0').validate(obj.response)
    return True


def deploy_all_ip_to_sgt_mapping_group(api):
    endpoint_result = api.ip_to_sgt_mapping_group.deploy_all_ip_to_sgt_mapping_group(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_deploy_all_ip_to_sgt_mapping_group(api, validator):
    try:
        assert is_valid_deploy_all_ip_to_sgt_mapping_group(
            validator,
            deploy_all_ip_to_sgt_mapping_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_all_ip_to_sgt_mapping_group_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.deploy_all_ip_to_sgt_mapping_group(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_deploy_all_ip_to_sgt_mapping_group_default(api, validator):
    try:
        assert is_valid_deploy_all_ip_to_sgt_mapping_group(
            validator,
            deploy_all_ip_to_sgt_mapping_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deploy_status_ip_to_sgt_mapping_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d6c25690e3a854c5be7763a4106e379e_v3_0_0').validate(obj.response)
    return True


def get_deploy_status_ip_to_sgt_mapping_group(api):
    endpoint_result = api.ip_to_sgt_mapping_group.get_deploy_status_ip_to_sgt_mapping_group(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_get_deploy_status_ip_to_sgt_mapping_group(api, validator):
    try:
        assert is_valid_get_deploy_status_ip_to_sgt_mapping_group(
            validator,
            get_deploy_status_ip_to_sgt_mapping_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deploy_status_ip_to_sgt_mapping_group_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.get_deploy_status_ip_to_sgt_mapping_group(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_get_deploy_status_ip_to_sgt_mapping_group_default(api, validator):
    try:
        assert is_valid_get_deploy_status_ip_to_sgt_mapping_group(
            validator,
            get_deploy_status_ip_to_sgt_mapping_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_to_sgt_mapping_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e56b94dafa5652228fd71abd2b4d6df3_v3_0_0').validate(obj.response)
    return True


def get_ip_to_sgt_mapping_group_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping_group.get_ip_to_sgt_mapping_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_get_ip_to_sgt_mapping_group_by_id(api, validator):
    try:
        assert is_valid_get_ip_to_sgt_mapping_group_by_id(
            validator,
            get_ip_to_sgt_mapping_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_ip_to_sgt_mapping_group_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.get_ip_to_sgt_mapping_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_get_ip_to_sgt_mapping_group_by_id_default(api, validator):
    try:
        assert is_valid_get_ip_to_sgt_mapping_group_by_id(
            validator,
            get_ip_to_sgt_mapping_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ip_to_sgt_mapping_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_02a5a26c964e53b3be3f9f0c103f304c_v3_0_0').validate(obj.response)
    return True


def update_ip_to_sgt_mapping_group_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping_group.update_ip_to_sgt_mapping_group_by_id(
        active_validation=False,
        deploy_to='string',
        deploy_type='string',
        id='string',
        name='string',
        payload=None,
        sgt='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_update_ip_to_sgt_mapping_group_by_id(api, validator):
    try:
        assert is_valid_update_ip_to_sgt_mapping_group_by_id(
            validator,
            update_ip_to_sgt_mapping_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_ip_to_sgt_mapping_group_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.update_ip_to_sgt_mapping_group_by_id(
        active_validation=False,
        id='string',
        deploy_to=None,
        deploy_type=None,
        name=None,
        payload=None,
        sgt=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_update_ip_to_sgt_mapping_group_by_id_default(api, validator):
    try:
        assert is_valid_update_ip_to_sgt_mapping_group_by_id(
            validator,
            update_ip_to_sgt_mapping_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ip_to_sgt_mapping_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_73ebc15160cf5c0184d3eaff3be14508_v3_0_0').validate(obj.response)
    return True


def delete_ip_to_sgt_mapping_group_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping_group.delete_ip_to_sgt_mapping_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_delete_ip_to_sgt_mapping_group_by_id(api, validator):
    try:
        assert is_valid_delete_ip_to_sgt_mapping_group_by_id(
            validator,
            delete_ip_to_sgt_mapping_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ip_to_sgt_mapping_group_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.delete_ip_to_sgt_mapping_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_delete_ip_to_sgt_mapping_group_by_id_default(api, validator):
    try:
        assert is_valid_delete_ip_to_sgt_mapping_group_by_id(
            validator,
            delete_ip_to_sgt_mapping_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_ip_to_sgt_mapping_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_680a1544a7125003b7803c0ed383f4bf_v3_0_0').validate(obj.response)
    return True


def get_all_ip_to_sgt_mapping_group(api):
    endpoint_result = api.ip_to_sgt_mapping_group.get_all_ip_to_sgt_mapping_group(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_get_all_ip_to_sgt_mapping_group(api, validator):
    try:
        assert is_valid_get_all_ip_to_sgt_mapping_group(
            validator,
            get_all_ip_to_sgt_mapping_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_ip_to_sgt_mapping_group_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.get_all_ip_to_sgt_mapping_group(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_get_all_ip_to_sgt_mapping_group_default(api, validator):
    try:
        assert is_valid_get_all_ip_to_sgt_mapping_group(
            validator,
            get_all_ip_to_sgt_mapping_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_ip_to_sgt_mapping_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_55c2e3af6da356009f6499f00a4115e9_v3_0_0').validate(obj.response)
    return True


def create_ip_to_sgt_mapping_group(api):
    endpoint_result = api.ip_to_sgt_mapping_group.create_ip_to_sgt_mapping_group(
        active_validation=False,
        deploy_to='string',
        deploy_type='string',
        name='string',
        payload=None,
        sgt='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_create_ip_to_sgt_mapping_group(api, validator):
    try:
        assert is_valid_create_ip_to_sgt_mapping_group(
            validator,
            create_ip_to_sgt_mapping_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_ip_to_sgt_mapping_group_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.create_ip_to_sgt_mapping_group(
        active_validation=False,
        deploy_to=None,
        deploy_type=None,
        name=None,
        payload=None,
        sgt=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_create_ip_to_sgt_mapping_group_default(api, validator):
    try:
        assert is_valid_create_ip_to_sgt_mapping_group(
            validator,
            create_ip_to_sgt_mapping_group_default(api)
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
    json_schema_validate('jsd_14c9a2546739540eb2c1cb7c411836cb_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.ip_to_sgt_mapping_group.get_version(

    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
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
    endpoint_result = api.ip_to_sgt_mapping_group.get_version(

    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_ip_to_sgt_mapping_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a39fa17ffcd45736aa221dd27916e843_v3_0_0').validate(obj.response)
    return True


def bulk_request_for_ip_to_sgt_mapping_group(api):
    endpoint_result = api.ip_to_sgt_mapping_group.bulk_request_for_ip_to_sgt_mapping_group(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_bulk_request_for_ip_to_sgt_mapping_group(api, validator):
    try:
        assert is_valid_bulk_request_for_ip_to_sgt_mapping_group(
            validator,
            bulk_request_for_ip_to_sgt_mapping_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_request_for_ip_to_sgt_mapping_group_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.bulk_request_for_ip_to_sgt_mapping_group(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_bulk_request_for_ip_to_sgt_mapping_group_default(api, validator):
    try:
        assert is_valid_bulk_request_for_ip_to_sgt_mapping_group(
            validator,
            bulk_request_for_ip_to_sgt_mapping_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_ip_to_sgt_mapping_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bb5f9095ca7953d3bdb16155e263f25a_v3_0_0').validate(obj.response)
    return True


def monitor_bulk_status_ip_to_sgt_mapping_group(api):
    endpoint_result = api.ip_to_sgt_mapping_group.monitor_bulk_status_ip_to_sgt_mapping_group(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_monitor_bulk_status_ip_to_sgt_mapping_group(api, validator):
    try:
        assert is_valid_monitor_bulk_status_ip_to_sgt_mapping_group(
            validator,
            monitor_bulk_status_ip_to_sgt_mapping_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def monitor_bulk_status_ip_to_sgt_mapping_group_default(api):
    endpoint_result = api.ip_to_sgt_mapping_group.monitor_bulk_status_ip_to_sgt_mapping_group(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping_group
def test_monitor_bulk_status_ip_to_sgt_mapping_group_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_ip_to_sgt_mapping_group(
            validator,
            monitor_bulk_status_ip_to_sgt_mapping_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
