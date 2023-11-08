# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI px_grid_node API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.2_beta', reason='version does not match')


def is_valid_approve_px_grid_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f47d656ed0805859a85e5cc082c78dcf_v3_2_beta').validate(obj.response)
    return True


def approve_px_grid_node(api):
    endpoint_result = api.px_grid_node.approve_px_grid_node(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_approve_px_grid_node(api, validator):
    try:
        assert is_valid_approve_px_grid_node(
            validator,
            approve_px_grid_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def approve_px_grid_node_default(api):
    endpoint_result = api.px_grid_node.approve_px_grid_node(
        active_validation=False,
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_approve_px_grid_node_default(api, validator):
    try:
        assert is_valid_approve_px_grid_node(
            validator,
            approve_px_grid_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_px_grid_node_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_111a9d109aac585a89bdd3fae400064b_v3_2_beta').validate(obj.response)
    return True


def get_px_grid_node_by_name(api):
    endpoint_result = api.px_grid_node.get_px_grid_node_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_get_px_grid_node_by_name(api, validator):
    try:
        assert is_valid_get_px_grid_node_by_name(
            validator,
            get_px_grid_node_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_px_grid_node_by_name_default(api):
    endpoint_result = api.px_grid_node.get_px_grid_node_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_get_px_grid_node_by_name_default(api, validator):
    try:
        assert is_valid_get_px_grid_node_by_name(
            validator,
            get_px_grid_node_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_px_grid_node_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_849e718d5054593b94a2fef39461c24a_v3_2_beta').validate(obj.response)
    return True


def delete_px_grid_node_by_name(api):
    endpoint_result = api.px_grid_node.delete_px_grid_node_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_delete_px_grid_node_by_name(api, validator):
    try:
        assert is_valid_delete_px_grid_node_by_name(
            validator,
            delete_px_grid_node_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_px_grid_node_by_name_default(api):
    endpoint_result = api.px_grid_node.delete_px_grid_node_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_delete_px_grid_node_by_name_default(api, validator):
    try:
        assert is_valid_delete_px_grid_node_by_name(
            validator,
            delete_px_grid_node_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_px_grid_node_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d24ade0b53405fbc898cb0cc1ea57fb8_v3_2_beta').validate(obj.response)
    return True


def get_px_grid_node_by_id(api):
    endpoint_result = api.px_grid_node.get_px_grid_node_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_get_px_grid_node_by_id(api, validator):
    try:
        assert is_valid_get_px_grid_node_by_id(
            validator,
            get_px_grid_node_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_px_grid_node_by_id_default(api):
    endpoint_result = api.px_grid_node.get_px_grid_node_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_get_px_grid_node_by_id_default(api, validator):
    try:
        assert is_valid_get_px_grid_node_by_id(
            validator,
            get_px_grid_node_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_px_grid_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_52661028d97156379640002f79b2007c_v3_2_beta').validate(obj.response)
    return True


def get_px_grid_node(api):
    endpoint_result = api.px_grid_node.get_px_grid_node(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_get_px_grid_node(api, validator):
    try:
        assert is_valid_get_px_grid_node(
            validator,
            get_px_grid_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_px_grid_node_default(api):
    endpoint_result = api.px_grid_node.get_px_grid_node(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_get_px_grid_node_default(api, validator):
    try:
        assert is_valid_get_px_grid_node(
            validator,
            get_px_grid_node_default(api)
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
    json_schema_validate('jsd_73c2962d70ef5964be55cfeae68e5ba6_v3_2_beta').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.px_grid_node.get_version(

    )
    return endpoint_result


@pytest.mark.px_grid_node
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
    endpoint_result = api.px_grid_node.get_version(

    )
    return endpoint_result


@pytest.mark.px_grid_node
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
