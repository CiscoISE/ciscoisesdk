# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI node_deployment API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1_Patch_1', reason='version does not match')


def is_valid_get_nodes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_51b95cb82a8954c5a785140a9a8f3156_v3_1_patch_1').validate(obj.response)
    return True


def get_nodes(api):
    endpoint_result = api.node_deployment.get_nodes(
        filter='value1,value2',
        filter_type='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
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
    endpoint_result = api.node_deployment.get_nodes(
        filter=None,
        filter_type=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_get_nodes_default(api, validator):
    try:
        assert is_valid_get_nodes(
            validator,
            get_nodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_register_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_58d0ee193cc65780af11ed96b1758755_v3_1_patch_1').validate(obj.response)
    return True


def register_node(api):
    endpoint_result = api.node_deployment.register_node(
        active_validation=False,
        allow_cert_import=True,
        fqdn='string',
        password='string',
        payload=None,
        roles=['string'],
        services=['string'],
        user_name='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_register_node(api, validator):
    try:
        assert is_valid_register_node(
            validator,
            register_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def register_node_default(api):
    endpoint_result = api.node_deployment.register_node(
        active_validation=False,
        allow_cert_import=None,
        fqdn=None,
        password=None,
        payload=None,
        roles=None,
        services=None,
        user_name=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_register_node_default(api, validator):
    try:
        assert is_valid_register_node(
            validator,
            register_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_node_details(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ae8d7c8f33bb52ceb04880845f2f45ba_v3_1_patch_1').validate(obj.response)
    return True


def get_node_details(api):
    endpoint_result = api.node_deployment.get_node_details(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_get_node_details(api, validator):
    try:
        assert is_valid_get_node_details(
            validator,
            get_node_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_node_details_default(api):
    endpoint_result = api.node_deployment.get_node_details(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_get_node_details_default(api, validator):
    try:
        assert is_valid_get_node_details(
            validator,
            get_node_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_682c1fa3bf115c77be99b602aca1493b_v3_1_patch_1').validate(obj.response)
    return True


def update_node(api):
    endpoint_result = api.node_deployment.update_node(
        active_validation=False,
        hostname='string',
        payload=None,
        roles=['string'],
        services=['string']
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_update_node(api, validator):
    try:
        assert is_valid_update_node(
            validator,
            update_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_node_default(api):
    endpoint_result = api.node_deployment.update_node(
        active_validation=False,
        hostname='string',
        payload=None,
        roles=None,
        services=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_update_node_default(api, validator):
    try:
        assert is_valid_update_node(
            validator,
            update_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_161d26670a205a78800cb50673027a6e_v3_1_patch_1').validate(obj.response)
    return True


def delete_node(api):
    endpoint_result = api.node_deployment.delete_node(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_delete_node(api, validator):
    try:
        assert is_valid_delete_node(
            validator,
            delete_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_node_default(api):
    endpoint_result = api.node_deployment.delete_node(
        hostname='string'
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_delete_node_default(api, validator):
    try:
        assert is_valid_delete_node(
            validator,
            delete_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_make_primary(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5d2e0f05045c5459824d9f24f2827608_v3_1_patch_1').validate(obj.response)
    return True


def make_primary(api):
    endpoint_result = api.node_deployment.make_primary(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_make_primary(api, validator):
    try:
        assert is_valid_make_primary(
            validator,
            make_primary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def make_primary_default(api):
    endpoint_result = api.node_deployment.make_primary(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_make_primary_default(api, validator):
    try:
        assert is_valid_make_primary(
            validator,
            make_primary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_promote_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_31351f27497451e4aac524c2d7fc4bf0_v3_1_patch_1').validate(obj.response)
    return True


def promote_node(api):
    endpoint_result = api.node_deployment.promote_node(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_promote_node(api, validator):
    try:
        assert is_valid_promote_node(
            validator,
            promote_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def promote_node_default(api):
    endpoint_result = api.node_deployment.promote_node(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_promote_node_default(api, validator):
    try:
        assert is_valid_promote_node(
            validator,
            promote_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_make_standalone(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c63819cf4d3b5854bcbbadbc383236a0_v3_1_patch_1').validate(obj.response)
    return True


def make_standalone(api):
    endpoint_result = api.node_deployment.make_standalone(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_make_standalone(api, validator):
    try:
        assert is_valid_make_standalone(
            validator,
            make_standalone(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def make_standalone_default(api):
    endpoint_result = api.node_deployment.make_standalone(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_make_standalone_default(api, validator):
    try:
        assert is_valid_make_standalone(
            validator,
            make_standalone_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4eb4709af3a7528e947ad10d2f2141a8_v3_1_patch_1').validate(obj.response)
    return True


def sync_node(api):
    endpoint_result = api.node_deployment.sync_node(
        active_validation=False,
        hostname='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_sync_node(api, validator):
    try:
        assert is_valid_sync_node(
            validator,
            sync_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def sync_node_default(api):
    endpoint_result = api.node_deployment.sync_node(
        active_validation=False,
        hostname='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.node_deployment
def test_sync_node_default(api, validator):
    try:
        assert is_valid_sync_node(
            validator,
            sync_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
