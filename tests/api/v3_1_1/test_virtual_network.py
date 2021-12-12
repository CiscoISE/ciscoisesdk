# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI virtual_network API fixtures and tests.

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


def is_valid_get_virtual_networks(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2199bd42dc595dd68ab56120039f89f1_v3_1_1').validate(obj.response)
    return True


def get_virtual_networks(api):
    endpoint_result = api.virtual_network.get_virtual_networks(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_get_virtual_networks(api, validator):
    try:
        assert is_valid_get_virtual_networks(
            validator,
            get_virtual_networks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_virtual_networks_default(api):
    endpoint_result = api.virtual_network.get_virtual_networks(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_get_virtual_networks_default(api, validator):
    try:
        assert is_valid_get_virtual_networks(
            validator,
            get_virtual_networks_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_virtual_network(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_fe478ea1775758638d714efe1b67eec2_v3_1_1').validate(obj.response)
    return True


def create_virtual_network(api):
    endpoint_result = api.virtual_network.create_virtual_network(
        active_validation=False,
        additional_attributes='string',
        id='string',
        last_update='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_create_virtual_network(api, validator):
    try:
        assert is_valid_create_virtual_network(
            validator,
            create_virtual_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_virtual_network_default(api):
    endpoint_result = api.virtual_network.create_virtual_network(
        active_validation=False,
        additional_attributes=None,
        id=None,
        last_update=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_create_virtual_network_default(api, validator):
    try:
        assert is_valid_create_virtual_network(
            validator,
            create_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_create_virtual_networks(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f7253733d7025c8b8459478b159e84fc_v3_1_1').validate(obj.response)
    return True


def bulk_create_virtual_networks(api):
    endpoint_result = api.virtual_network.bulk_create_virtual_networks(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_bulk_create_virtual_networks(api, validator):
    try:
        assert is_valid_bulk_create_virtual_networks(
            validator,
            bulk_create_virtual_networks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_create_virtual_networks_default(api):
    endpoint_result = api.virtual_network.bulk_create_virtual_networks(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_bulk_create_virtual_networks_default(api, validator):
    try:
        assert is_valid_bulk_create_virtual_networks(
            validator,
            bulk_create_virtual_networks_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_delete_virtual_networks(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b6cdd5dd57b95d8bac87ce9600a84b5d_v3_1_1').validate(obj.response)
    return True


def bulk_delete_virtual_networks(api):
    endpoint_result = api.virtual_network.bulk_delete_virtual_networks(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_bulk_delete_virtual_networks(api, validator):
    try:
        assert is_valid_bulk_delete_virtual_networks(
            validator,
            bulk_delete_virtual_networks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_delete_virtual_networks_default(api):
    endpoint_result = api.virtual_network.bulk_delete_virtual_networks(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_bulk_delete_virtual_networks_default(api, validator):
    try:
        assert is_valid_bulk_delete_virtual_networks(
            validator,
            bulk_delete_virtual_networks_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_update_virtual_networks(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e3c62bba9f9e5344a38479f6437cf8b4_v3_1_1').validate(obj.response)
    return True


def bulk_update_virtual_networks(api):
    endpoint_result = api.virtual_network.bulk_update_virtual_networks(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_bulk_update_virtual_networks(api, validator):
    try:
        assert is_valid_bulk_update_virtual_networks(
            validator,
            bulk_update_virtual_networks(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_update_virtual_networks_default(api):
    endpoint_result = api.virtual_network.bulk_update_virtual_networks(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_bulk_update_virtual_networks_default(api, validator):
    try:
        assert is_valid_bulk_update_virtual_networks(
            validator,
            bulk_update_virtual_networks_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_virtual_network_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d89686dd9cb05c02833cdefc5d3ba9f2_v3_1_1').validate(obj.response)
    return True


def get_virtual_network_by_id(api):
    endpoint_result = api.virtual_network.get_virtual_network_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_get_virtual_network_by_id(api, validator):
    try:
        assert is_valid_get_virtual_network_by_id(
            validator,
            get_virtual_network_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_virtual_network_by_id_default(api):
    endpoint_result = api.virtual_network.get_virtual_network_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_get_virtual_network_by_id_default(api, validator):
    try:
        assert is_valid_get_virtual_network_by_id(
            validator,
            get_virtual_network_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_virtual_network_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6d02f9a7ed46581b8baf07e182f80695_v3_1_1').validate(obj.response)
    return True


def update_virtual_network_by_id(api):
    endpoint_result = api.virtual_network.update_virtual_network_by_id(
        active_validation=False,
        additional_attributes='string',
        id='string',
        last_update='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_update_virtual_network_by_id(api, validator):
    try:
        assert is_valid_update_virtual_network_by_id(
            validator,
            update_virtual_network_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_virtual_network_by_id_default(api):
    endpoint_result = api.virtual_network.update_virtual_network_by_id(
        active_validation=False,
        id='string',
        additional_attributes=None,
        last_update=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_update_virtual_network_by_id_default(api, validator):
    try:
        assert is_valid_update_virtual_network_by_id(
            validator,
            update_virtual_network_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_virtual_network_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_30f7fda88868581085da6ac8c0e04b5c_v3_1_1').validate(obj.response)
    return True


def delete_virtual_network_by_id(api):
    endpoint_result = api.virtual_network.delete_virtual_network_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_delete_virtual_network_by_id(api, validator):
    try:
        assert is_valid_delete_virtual_network_by_id(
            validator,
            delete_virtual_network_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_virtual_network_by_id_default(api):
    endpoint_result = api.virtual_network.delete_virtual_network_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.virtual_network
def test_delete_virtual_network_by_id_default(api, validator):
    try:
        assert is_valid_delete_virtual_network_by_id(
            validator,
            delete_virtual_network_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
