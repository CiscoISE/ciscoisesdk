# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI ip_to_sgt_mapping API fixtures and tests.

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


def is_valid_deploy_ip_to_sgt_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b5711af534e557749661afb5b6c90cee_v3_1_0').validate(obj.response)
    return True


def deploy_ip_to_sgt_mapping_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping.deploy_ip_to_sgt_mapping_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_deploy_ip_to_sgt_mapping_by_id(api, validator):
    try:
        assert is_valid_deploy_ip_to_sgt_mapping_by_id(
            validator,
            deploy_ip_to_sgt_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def deploy_ip_to_sgt_mapping_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping.deploy_ip_to_sgt_mapping_by_id(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_deploy_ip_to_sgt_mapping_by_id_default(api, validator):
    try:
        assert is_valid_deploy_ip_to_sgt_mapping_by_id(
            validator,
            deploy_ip_to_sgt_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_all_ip_to_sgt_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_83343989df7a50feb38d8729b99553e9_v3_1_0').validate(obj.response)
    return True


def deploy_all_ip_to_sgt_mapping(api):
    endpoint_result = api.ip_to_sgt_mapping.deploy_all_ip_to_sgt_mapping(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_deploy_all_ip_to_sgt_mapping(api, validator):
    try:
        assert is_valid_deploy_all_ip_to_sgt_mapping(
            validator,
            deploy_all_ip_to_sgt_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def deploy_all_ip_to_sgt_mapping_default(api):
    endpoint_result = api.ip_to_sgt_mapping.deploy_all_ip_to_sgt_mapping(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_deploy_all_ip_to_sgt_mapping_default(api, validator):
    try:
        assert is_valid_deploy_all_ip_to_sgt_mapping(
            validator,
            deploy_all_ip_to_sgt_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deploy_status_ip_to_sgt_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_dcd55e1e57d25e65b625526a1d341afd_v3_1_0').validate(obj.response)
    return True


def get_deploy_status_ip_to_sgt_mapping(api):
    endpoint_result = api.ip_to_sgt_mapping.get_deploy_status_ip_to_sgt_mapping(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_get_deploy_status_ip_to_sgt_mapping(api, validator):
    try:
        assert is_valid_get_deploy_status_ip_to_sgt_mapping(
            validator,
            get_deploy_status_ip_to_sgt_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_deploy_status_ip_to_sgt_mapping_default(api):
    endpoint_result = api.ip_to_sgt_mapping.get_deploy_status_ip_to_sgt_mapping(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_get_deploy_status_ip_to_sgt_mapping_default(api, validator):
    try:
        assert is_valid_get_deploy_status_ip_to_sgt_mapping(
            validator,
            get_deploy_status_ip_to_sgt_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_to_sgt_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_17ddc6729af25f8b8c060b20d09f0057_v3_1_0').validate(obj.response)
    return True


def get_ip_to_sgt_mapping_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping.get_ip_to_sgt_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_get_ip_to_sgt_mapping_by_id(api, validator):
    try:
        assert is_valid_get_ip_to_sgt_mapping_by_id(
            validator,
            get_ip_to_sgt_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_ip_to_sgt_mapping_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping.get_ip_to_sgt_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_get_ip_to_sgt_mapping_by_id_default(api, validator):
    try:
        assert is_valid_get_ip_to_sgt_mapping_by_id(
            validator,
            get_ip_to_sgt_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ip_to_sgt_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_94de3cecd62e5153881245a8613fbeea_v3_1_0').validate(obj.response)
    return True


def update_ip_to_sgt_mapping_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping.update_ip_to_sgt_mapping_by_id(
        active_validation=False,
        deploy_to='string',
        deploy_type='string',
        host_ip='string',
        host_name='string',
        id='string',
        mapping_group='string',
        name='string',
        payload=None,
        sgt='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_update_ip_to_sgt_mapping_by_id(api, validator):
    try:
        assert is_valid_update_ip_to_sgt_mapping_by_id(
            validator,
            update_ip_to_sgt_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_ip_to_sgt_mapping_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping.update_ip_to_sgt_mapping_by_id(
        active_validation=False,
        id='string',
        deploy_to=None,
        deploy_type=None,
        host_ip=None,
        host_name=None,
        mapping_group=None,
        name=None,
        payload=None,
        sgt=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_update_ip_to_sgt_mapping_by_id_default(api, validator):
    try:
        assert is_valid_update_ip_to_sgt_mapping_by_id(
            validator,
            update_ip_to_sgt_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ip_to_sgt_mapping_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_582650f0cb1e55c9baee89c136c8ec47_v3_1_0').validate(obj.response)
    return True


def delete_ip_to_sgt_mapping_by_id(api):
    endpoint_result = api.ip_to_sgt_mapping.delete_ip_to_sgt_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_delete_ip_to_sgt_mapping_by_id(api, validator):
    try:
        assert is_valid_delete_ip_to_sgt_mapping_by_id(
            validator,
            delete_ip_to_sgt_mapping_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_ip_to_sgt_mapping_by_id_default(api):
    endpoint_result = api.ip_to_sgt_mapping.delete_ip_to_sgt_mapping_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_delete_ip_to_sgt_mapping_by_id_default(api, validator):
    try:
        assert is_valid_delete_ip_to_sgt_mapping_by_id(
            validator,
            delete_ip_to_sgt_mapping_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_to_sgt_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_10cd9e91565f5c74b9f32ff0e5be6f17_v3_1_0').validate(obj.response)
    return True


def get_ip_to_sgt_mapping(api):
    endpoint_result = api.ip_to_sgt_mapping.get_ip_to_sgt_mapping(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_get_ip_to_sgt_mapping(api, validator):
    try:
        assert is_valid_get_ip_to_sgt_mapping(
            validator,
            get_ip_to_sgt_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_ip_to_sgt_mapping_default(api):
    endpoint_result = api.ip_to_sgt_mapping.get_ip_to_sgt_mapping(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_get_ip_to_sgt_mapping_default(api, validator):
    try:
        assert is_valid_get_ip_to_sgt_mapping(
            validator,
            get_ip_to_sgt_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_ip_to_sgt_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_52dd838b268f5dd298a123ac58448ea9_v3_1_0').validate(obj.response)
    return True


def create_ip_to_sgt_mapping(api):
    endpoint_result = api.ip_to_sgt_mapping.create_ip_to_sgt_mapping(
        active_validation=False,
        deploy_to='string',
        deploy_type='string',
        host_ip='string',
        host_name='string',
        mapping_group='string',
        name='string',
        payload=None,
        sgt='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_create_ip_to_sgt_mapping(api, validator):
    try:
        assert is_valid_create_ip_to_sgt_mapping(
            validator,
            create_ip_to_sgt_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_ip_to_sgt_mapping_default(api):
    endpoint_result = api.ip_to_sgt_mapping.create_ip_to_sgt_mapping(
        active_validation=False,
        deploy_to=None,
        deploy_type=None,
        host_ip=None,
        host_name=None,
        mapping_group=None,
        name=None,
        payload=None,
        sgt=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_create_ip_to_sgt_mapping_default(api, validator):
    try:
        assert is_valid_create_ip_to_sgt_mapping(
            validator,
            create_ip_to_sgt_mapping_default(api)
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
    json_schema_validate('jsd_63042762af0b5041b56b12c5c08cc53e_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.ip_to_sgt_mapping.get_version(

    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
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
    endpoint_result = api.ip_to_sgt_mapping.get_version(

    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_ip_to_sgt_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_ab203a1dd0015924bf2005a84ae85477_v3_1_0').validate(obj.response)
    return True


def bulk_request_for_ip_to_sgt_mapping(api):
    endpoint_result = api.ip_to_sgt_mapping.bulk_request_for_ip_to_sgt_mapping(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_bulk_request_for_ip_to_sgt_mapping(api, validator):
    try:
        assert is_valid_bulk_request_for_ip_to_sgt_mapping(
            validator,
            bulk_request_for_ip_to_sgt_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_request_for_ip_to_sgt_mapping_default(api):
    endpoint_result = api.ip_to_sgt_mapping.bulk_request_for_ip_to_sgt_mapping(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_bulk_request_for_ip_to_sgt_mapping_default(api, validator):
    try:
        assert is_valid_bulk_request_for_ip_to_sgt_mapping(
            validator,
            bulk_request_for_ip_to_sgt_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_ip_to_sgt_mapping(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9f36d3f43a6157978ec529318ce506e0_v3_1_0').validate(obj.response)
    return True


def monitor_bulk_status_ip_to_sgt_mapping(api):
    endpoint_result = api.ip_to_sgt_mapping.monitor_bulk_status_ip_to_sgt_mapping(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_monitor_bulk_status_ip_to_sgt_mapping(api, validator):
    try:
        assert is_valid_monitor_bulk_status_ip_to_sgt_mapping(
            validator,
            monitor_bulk_status_ip_to_sgt_mapping(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def monitor_bulk_status_ip_to_sgt_mapping_default(api):
    endpoint_result = api.ip_to_sgt_mapping.monitor_bulk_status_ip_to_sgt_mapping(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.ip_to_sgt_mapping
def test_monitor_bulk_status_ip_to_sgt_mapping_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_ip_to_sgt_mapping(
            validator,
            monitor_bulk_status_ip_to_sgt_mapping_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
