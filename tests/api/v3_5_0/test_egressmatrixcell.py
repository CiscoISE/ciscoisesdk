# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI egressmatrixcell API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.5.0', reason='version does not match')


def is_valid_get_all(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_all(api):
    endpoint_result = api.egressmatrixcell.get_all(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_get_all(api, validator):
    try:
        assert is_valid_get_all(
            validator,
            get_all(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_all_default(api):
    endpoint_result = api.egressmatrixcell.get_all(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_get_all_default(api, validator):
    try:
        assert is_valid_get_all(
            validator,
            get_all_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_generator(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_all_generator(api):
    endpoint_result = api.egressmatrixcell.get_all_generator(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_get_all_generator(api, validator):
    try:
        assert is_valid_get_all_generator(
            validator,
            get_all_generator(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_all_generator_default(api):
    endpoint_result = api.egressmatrixcell.get_all_generator(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_get_all_generator_default(api, validator):
    try:
        assert is_valid_get_all_generator(
            validator,
            get_all_generator_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def create(api):
    endpoint_result = api.egressmatrixcell.create(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_create(api, validator):
    try:
        assert is_valid_create(
            validator,
            create(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_default(api):
    endpoint_result = api.egressmatrixcell.create(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_create_default(api, validator):
    try:
        assert is_valid_create(
            validator,
            create_default(api)
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
    assert hasattr(obj, 'status_code')
    return True


def set_all_cells_status(api):
    endpoint_result = api.egressmatrixcell.set_all_cells_status(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_set_all_cells_status(api, validator):
    try:
        assert is_valid_set_all_cells_status(
            validator,
            set_all_cells_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def set_all_cells_status_default(api):
    endpoint_result = api.egressmatrixcell.set_all_cells_status(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_set_all_cells_status_default(api, validator):
    try:
        assert is_valid_set_all_cells_status(
            validator,
            set_all_cells_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_clone_cell(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def clone_cell(api):
    endpoint_result = api.egressmatrixcell.clone_cell(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_clone_cell(api, validator):
    try:
        assert is_valid_clone_cell(
            validator,
            clone_cell(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def clone_cell_default(api):
    endpoint_result = api.egressmatrixcell.clone_cell(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_clone_cell_default(api, validator):
    try:
        assert is_valid_clone_cell(
            validator,
            clone_cell_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_clear_all_matrix_cells(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def clear_all_matrix_cells(api):
    endpoint_result = api.egressmatrixcell.clear_all_matrix_cells(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_clear_all_matrix_cells(api, validator):
    try:
        assert is_valid_clear_all_matrix_cells(
            validator,
            clear_all_matrix_cells(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def clear_all_matrix_cells_default(api):
    endpoint_result = api.egressmatrixcell.clear_all_matrix_cells(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_clear_all_matrix_cells_default(api, validator):
    try:
        assert is_valid_clear_all_matrix_cells(
            validator,
            clear_all_matrix_cells_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_by_id(api):
    endpoint_result = api.egressmatrixcell.get_by_id(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_get_by_id(api, validator):
    try:
        assert is_valid_get_by_id(
            validator,
            get_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_by_id_default(api):
    endpoint_result = api.egressmatrixcell.get_by_id(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_get_by_id_default(api, validator):
    try:
        assert is_valid_get_by_id(
            validator,
            get_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def update(api):
    endpoint_result = api.egressmatrixcell.update(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_update(api, validator):
    try:
        assert is_valid_update(
            validator,
            update(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_default(api):
    endpoint_result = api.egressmatrixcell.update(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_update_default(api, validator):
    try:
        assert is_valid_update(
            validator,
            update_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def delete(api):
    endpoint_result = api.egressmatrixcell.delete(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_delete(api, validator):
    try:
        assert is_valid_delete(
            validator,
            delete(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_default(api):
    endpoint_result = api.egressmatrixcell.delete(
    )
    return endpoint_result


@pytest.mark.egressmatrixcell
def test_delete_default(api, validator):
    try:
        assert is_valid_delete(
            validator,
            delete_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


