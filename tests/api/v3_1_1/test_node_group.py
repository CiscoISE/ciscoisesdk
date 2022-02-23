# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI node_group API fixtures and tests.

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


def is_valid_get_node_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_a0824f9a589c58cd8df522524cb550ad_v3_1_1').validate(obj.response)
    return True


def get_node_groups(api):
    endpoint_result = api.node_group.get_node_groups(

    )
    return endpoint_result


@pytest.mark.node_group
def test_get_node_groups(api, validator):
    try:
        assert is_valid_get_node_groups(
            validator,
            get_node_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_node_groups_default(api):
    endpoint_result = api.node_group.get_node_groups(

    )
    return endpoint_result


@pytest.mark.node_group
def test_get_node_groups_default(api, validator):
    try:
        assert is_valid_get_node_groups(
            validator,
            get_node_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_node_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1d5efe180ef459b1a1d9f651e7c1eb92_v3_1_1').validate(obj.response)
    return True


def create_node_group(api):
    endpoint_result = api.node_group.create_node_group(
        active_validation=False,
        description='string',
        mar_cache={'query-attempts': 0, 'query-timeout': 0, 'replication-attempts': 0, 'replication-timeout': 0},
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_create_node_group(api, validator):
    try:
        assert is_valid_create_node_group(
            validator,
            create_node_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_node_group_default(api):
    endpoint_result = api.node_group.create_node_group(
        active_validation=False,
        description=None,
        mar_cache=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_create_node_group_default(api, validator):
    try:
        assert is_valid_create_node_group(
            validator,
            create_node_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_node_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c9d1b776015057a59e659c8327ea91a1_v3_1_1').validate(obj.response)
    return True


def get_node_group(api):
    endpoint_result = api.node_group.get_node_group(
        node_group_name='string'
    )
    return endpoint_result


@pytest.mark.node_group
def test_get_node_group(api, validator):
    try:
        assert is_valid_get_node_group(
            validator,
            get_node_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_node_group_default(api):
    endpoint_result = api.node_group.get_node_group(
        node_group_name='string'
    )
    return endpoint_result


@pytest.mark.node_group
def test_get_node_group_default(api, validator):
    try:
        assert is_valid_get_node_group(
            validator,
            get_node_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_node_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_fbd772420b8851349aa58fb4a9b006b8_v3_1_1').validate(obj.response)
    return True


def update_node_group(api):
    endpoint_result = api.node_group.update_node_group(
        active_validation=False,
        description='string',
        mar_cache={'query-attempts': 0, 'query-timeout': 0, 'replication-attempts': 0, 'replication-timeout': 0},
        name='string',
        node_group_name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_update_node_group(api, validator):
    try:
        assert is_valid_update_node_group(
            validator,
            update_node_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_node_group_default(api):
    endpoint_result = api.node_group.update_node_group(
        active_validation=False,
        node_group_name='string',
        description=None,
        mar_cache=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_update_node_group_default(api, validator):
    try:
        assert is_valid_update_node_group(
            validator,
            update_node_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_node_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b2eacaba249e5762874a801f71631ae8_v3_1_1').validate(obj.response)
    return True


def delete_node_group(api):
    endpoint_result = api.node_group.delete_node_group(
        force_delete=True,
        node_group_name='string'
    )
    return endpoint_result


@pytest.mark.node_group
def test_delete_node_group(api, validator):
    try:
        assert is_valid_delete_node_group(
            validator,
            delete_node_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_node_group_default(api):
    endpoint_result = api.node_group.delete_node_group(
        node_group_name='string',
        force_delete=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_delete_node_group_default(api, validator):
    try:
        assert is_valid_delete_node_group(
            validator,
            delete_node_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_fc44ec6afaf95ea9b51dd404abf46e4e_v3_1_1').validate(obj.response)
    return True


def add_node(api):
    endpoint_result = api.node_group.add_node(
        active_validation=False,
        hostname='string',
        node_group_name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_add_node(api, validator):
    try:
        assert is_valid_add_node(
            validator,
            add_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def add_node_default(api):
    endpoint_result = api.node_group.add_node(
        active_validation=False,
        node_group_name='string',
        hostname=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_add_node_default(api, validator):
    try:
        assert is_valid_add_node(
            validator,
            add_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_nodes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8fe420544d425d3d873632dbb6c1b8c2_v3_1_1').validate(obj.response)
    return True


def get_nodes(api):
    endpoint_result = api.node_group.get_nodes(
        node_group_name='string'
    )
    return endpoint_result


@pytest.mark.node_group
def test_get_nodes(api, validator):
    try:
        assert is_valid_get_nodes(
            validator,
            get_nodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_nodes_default(api):
    endpoint_result = api.node_group.get_nodes(
        node_group_name='string'
    )
    return endpoint_result


@pytest.mark.node_group
def test_get_nodes_default(api, validator):
    try:
        assert is_valid_get_nodes(
            validator,
            get_nodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_19b1a343c45952a79d0bbfbadb02002b_v3_1_1').validate(obj.response)
    return True


def remove_node(api):
    endpoint_result = api.node_group.remove_node(
        active_validation=False,
        hostname='string',
        node_group_name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_remove_node(api, validator):
    try:
        assert is_valid_remove_node(
            validator,
            remove_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def remove_node_default(api):
    endpoint_result = api.node_group.remove_node(
        active_validation=False,
        node_group_name='string',
        hostname=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_group
def test_remove_node_default(api, validator):
    try:
        assert is_valid_remove_node(
            validator,
            remove_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
