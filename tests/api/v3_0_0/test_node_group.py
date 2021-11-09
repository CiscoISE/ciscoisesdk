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
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_node_groups(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_a0824f9a589c58cd8df522524cb550ad_v3_0_0').validate(obj.response)
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
            print(original_e)
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


def is_valid_get_node_group(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_64a0aadd33595645bf671efc4912f89a_v3_0_0').validate(obj.response)
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
            print(original_e)
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


def is_valid_create_node_group(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_f41d844dbee15f7680920652004f69b6_v3_0_0').validate(obj.response)
    return True


def create_node_group(api):
    endpoint_result = api.node_group.create_node_group(
        active_validation=False,
        description='string',
        mar_cache={'enabled': True, 'replication-timeout': 0, 'replication-attempts': 0, 'query-timeout': 0, 'query-attempts': 0},
        node_group_name='string',
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
            print(original_e)
            raise original_e


def create_node_group_default(api):
    endpoint_result = api.node_group.create_node_group(
        active_validation=False,
        node_group_name='string',
        description=None,
        mar_cache=None,
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


def is_valid_update_node_group(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_2875a99695fd5ee0b00efce79a5761ff_v3_0_0').validate(obj.response)
    return True


def update_node_group(api):
    endpoint_result = api.node_group.update_node_group(
        active_validation=False,
        description='string',
        mar_cache={'enabled': True, 'replication-timeout': 0, 'replication-attempts': 0, 'query-timeout': 0, 'query-attempts': 0},
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
            print(original_e)
            raise original_e


def update_node_group_default(api):
    endpoint_result = api.node_group.update_node_group(
        active_validation=False,
        node_group_name='string',
        description=None,
        mar_cache=None,
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

    json_schema_validate('jsd_2c5c37c343c050e0af67b2223e64faf3_v3_0_0').validate(obj.response)
    return True


def delete_node_group(api):
    endpoint_result = api.node_group.delete_node_group(
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
            print(original_e)
            raise original_e


def delete_node_group_default(api):
    endpoint_result = api.node_group.delete_node_group(
        node_group_name='string'
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
