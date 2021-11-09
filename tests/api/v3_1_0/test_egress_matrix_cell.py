# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI egress_matrix_cell API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_clear_all_matrix_cells(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_247716f503ab54e2921d713ed88f51c9_v3_1_0').validate(obj.response)
    return True


def clear_all_matrix_cells(api):
    endpoint_result = api.egress_matrix_cell.clear_all_matrix_cells(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_clear_all_matrix_cells(api, validator):
    try:
        assert is_valid_clear_all_matrix_cells(
            validator,
            clear_all_matrix_cells(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def clear_all_matrix_cells_default(api):
    endpoint_result = api.egress_matrix_cell.clear_all_matrix_cells(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_clear_all_matrix_cells_default(api, validator):
    try:
        assert is_valid_clear_all_matrix_cells(
            validator,
            clear_all_matrix_cells_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_all_cells_status(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_90540642f47f525dbd71ef49710ef578_v3_1_0').validate(obj.response)
    return True


def set_all_cells_status(api):
    endpoint_result = api.egress_matrix_cell.set_all_cells_status(
        active_validation=False,
        payload=None,
        status='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_set_all_cells_status(api, validator):
    try:
        assert is_valid_set_all_cells_status(
            validator,
            set_all_cells_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_all_cells_status_default(api):
    endpoint_result = api.egress_matrix_cell.set_all_cells_status(
        active_validation=False,
        status='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_set_all_cells_status_default(api, validator):
    try:
        assert is_valid_set_all_cells_status(
            validator,
            set_all_cells_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_clone_matrix_cell(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_892a1e6c05d05e67906b3b59bbe6d274_v3_1_0').validate(obj.response)
    return True


def clone_matrix_cell(api):
    endpoint_result = api.egress_matrix_cell.clone_matrix_cell(
        active_validation=False,
        dst_sgt_id='string',
        id='string',
        payload=None,
        src_sgt_id='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_clone_matrix_cell(api, validator):
    try:
        assert is_valid_clone_matrix_cell(
            validator,
            clone_matrix_cell(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def clone_matrix_cell_default(api):
    endpoint_result = api.egress_matrix_cell.clone_matrix_cell(
        active_validation=False,
        dst_sgt_id='string',
        id='string',
        src_sgt_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_clone_matrix_cell_default(api, validator):
    try:
        assert is_valid_clone_matrix_cell(
            validator,
            clone_matrix_cell_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_egress_matrix_cell_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_0cdc971b23285b87945021bd5983d1cd_v3_1_0').validate(obj.response)
    return True


def get_egress_matrix_cell_by_id(api):
    endpoint_result = api.egress_matrix_cell.get_egress_matrix_cell_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_get_egress_matrix_cell_by_id(api, validator):
    try:
        assert is_valid_get_egress_matrix_cell_by_id(
            validator,
            get_egress_matrix_cell_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_egress_matrix_cell_by_id_default(api):
    endpoint_result = api.egress_matrix_cell.get_egress_matrix_cell_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_get_egress_matrix_cell_by_id_default(api, validator):
    try:
        assert is_valid_get_egress_matrix_cell_by_id(
            validator,
            get_egress_matrix_cell_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_egress_matrix_cell_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_ce83fba942c25938bae0c7012df68317_v3_1_0').validate(obj.response)
    return True


def update_egress_matrix_cell_by_id(api):
    endpoint_result = api.egress_matrix_cell.update_egress_matrix_cell_by_id(
        active_validation=False,
        default_rule='string',
        description='string',
        destination_sgt_id='string',
        id='string',
        matrix_cell_status='string',
        name='string',
        payload=None,
        sgacls=['string'],
        source_sgt_id='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_update_egress_matrix_cell_by_id(api, validator):
    try:
        assert is_valid_update_egress_matrix_cell_by_id(
            validator,
            update_egress_matrix_cell_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_egress_matrix_cell_by_id_default(api):
    endpoint_result = api.egress_matrix_cell.update_egress_matrix_cell_by_id(
        active_validation=False,
        id='string',
        default_rule=None,
        description=None,
        destination_sgt_id=None,
        matrix_cell_status=None,
        name=None,
        payload=None,
        sgacls=None,
        source_sgt_id=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_update_egress_matrix_cell_by_id_default(api, validator):
    try:
        assert is_valid_update_egress_matrix_cell_by_id(
            validator,
            update_egress_matrix_cell_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_egress_matrix_cell_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_e4393915121d5bcc94dfde6c8f6f7f1c_v3_1_0').validate(obj.response)
    return True


def delete_egress_matrix_cell_by_id(api):
    endpoint_result = api.egress_matrix_cell.delete_egress_matrix_cell_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_delete_egress_matrix_cell_by_id(api, validator):
    try:
        assert is_valid_delete_egress_matrix_cell_by_id(
            validator,
            delete_egress_matrix_cell_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_egress_matrix_cell_by_id_default(api):
    endpoint_result = api.egress_matrix_cell.delete_egress_matrix_cell_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_delete_egress_matrix_cell_by_id_default(api, validator):
    try:
        assert is_valid_delete_egress_matrix_cell_by_id(
            validator,
            delete_egress_matrix_cell_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_egress_matrix_cell(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_c5e52706e7095a81b8d32f3024e01cf6_v3_1_0').validate(obj.response)
    return True


def get_egress_matrix_cell(api):
    endpoint_result = api.egress_matrix_cell.get_egress_matrix_cell(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_get_egress_matrix_cell(api, validator):
    try:
        assert is_valid_get_egress_matrix_cell(
            validator,
            get_egress_matrix_cell(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_egress_matrix_cell_default(api):
    endpoint_result = api.egress_matrix_cell.get_egress_matrix_cell(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_get_egress_matrix_cell_default(api, validator):
    try:
        assert is_valid_get_egress_matrix_cell(
            validator,
            get_egress_matrix_cell_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_egress_matrix_cell(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_64c560004d8b5f64a10f2cc070368c12_v3_1_0').validate(obj.response)
    return True


def create_egress_matrix_cell(api):
    endpoint_result = api.egress_matrix_cell.create_egress_matrix_cell(
        active_validation=False,
        default_rule='string',
        description='string',
        destination_sgt_id='string',
        matrix_cell_status='string',
        name='string',
        payload=None,
        sgacls=['string'],
        source_sgt_id='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_create_egress_matrix_cell(api, validator):
    try:
        assert is_valid_create_egress_matrix_cell(
            validator,
            create_egress_matrix_cell(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_egress_matrix_cell_default(api):
    endpoint_result = api.egress_matrix_cell.create_egress_matrix_cell(
        active_validation=False,
        default_rule=None,
        description=None,
        destination_sgt_id=None,
        matrix_cell_status=None,
        name=None,
        payload=None,
        sgacls=None,
        source_sgt_id=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_create_egress_matrix_cell_default(api, validator):
    try:
        assert is_valid_create_egress_matrix_cell(
            validator,
            create_egress_matrix_cell_default(api)
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

    json_schema_validate('jsd_703c9da5c04b59358ac8bb1034340df4_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.egress_matrix_cell.get_version(

    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
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
    endpoint_result = api.egress_matrix_cell.get_version(

    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_egress_matrix_cell(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_aa333658bf83576eb36a025283516518_v3_1_0').validate(obj.response)
    return True


def bulk_request_for_egress_matrix_cell(api):
    endpoint_result = api.egress_matrix_cell.bulk_request_for_egress_matrix_cell(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_bulk_request_for_egress_matrix_cell(api, validator):
    try:
        assert is_valid_bulk_request_for_egress_matrix_cell(
            validator,
            bulk_request_for_egress_matrix_cell(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_request_for_egress_matrix_cell_default(api):
    endpoint_result = api.egress_matrix_cell.bulk_request_for_egress_matrix_cell(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_bulk_request_for_egress_matrix_cell_default(api, validator):
    try:
        assert is_valid_bulk_request_for_egress_matrix_cell(
            validator,
            bulk_request_for_egress_matrix_cell_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_egress_matrix_cell(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_72048face30e52b28c76c1b2574de858_v3_1_0').validate(obj.response)
    return True


def monitor_bulk_status_egress_matrix_cell(api):
    endpoint_result = api.egress_matrix_cell.monitor_bulk_status_egress_matrix_cell(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_monitor_bulk_status_egress_matrix_cell(api, validator):
    try:
        assert is_valid_monitor_bulk_status_egress_matrix_cell(
            validator,
            monitor_bulk_status_egress_matrix_cell(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def monitor_bulk_status_egress_matrix_cell_default(api):
    endpoint_result = api.egress_matrix_cell.monitor_bulk_status_egress_matrix_cell(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.egress_matrix_cell
def test_monitor_bulk_status_egress_matrix_cell_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_egress_matrix_cell(
            validator,
            monitor_bulk_status_egress_matrix_cell_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
