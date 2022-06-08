# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI tacacs_external_servers API fixtures and tests.

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


def is_valid_get_tacacs_external_servers_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_afe1108b1a59539ebe3de3e5652c9653_v3_1_patch_1').validate(obj.response)
    return True


def get_tacacs_external_servers_by_name(api):
    endpoint_result = api.tacacs_external_servers.get_tacacs_external_servers_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_get_tacacs_external_servers_by_name(api, validator):
    try:
        assert is_valid_get_tacacs_external_servers_by_name(
            validator,
            get_tacacs_external_servers_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_tacacs_external_servers_by_name_default(api):
    endpoint_result = api.tacacs_external_servers.get_tacacs_external_servers_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_get_tacacs_external_servers_by_name_default(api, validator):
    try:
        assert is_valid_get_tacacs_external_servers_by_name(
            validator,
            get_tacacs_external_servers_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tacacs_external_servers_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8b9eb9547216547cab8b9e686eee674b_v3_1_patch_1').validate(obj.response)
    return True


def get_tacacs_external_servers_by_id(api):
    endpoint_result = api.tacacs_external_servers.get_tacacs_external_servers_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_get_tacacs_external_servers_by_id(api, validator):
    try:
        assert is_valid_get_tacacs_external_servers_by_id(
            validator,
            get_tacacs_external_servers_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_tacacs_external_servers_by_id_default(api):
    endpoint_result = api.tacacs_external_servers.get_tacacs_external_servers_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_get_tacacs_external_servers_by_id_default(api, validator):
    try:
        assert is_valid_get_tacacs_external_servers_by_id(
            validator,
            get_tacacs_external_servers_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_tacacs_external_servers_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7a7cffe3bfae55aa81b7b4447519e4cd_v3_1_patch_1').validate(obj.response)
    return True


def update_tacacs_external_servers_by_id(api):
    endpoint_result = api.tacacs_external_servers.update_tacacs_external_servers_by_id(
        active_validation=False,
        connection_port=0,
        description='string',
        host_ip='string',
        id='string',
        name='string',
        payload=None,
        shared_secret='string',
        single_connect=True,
        timeout=0
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_update_tacacs_external_servers_by_id(api, validator):
    try:
        assert is_valid_update_tacacs_external_servers_by_id(
            validator,
            update_tacacs_external_servers_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_tacacs_external_servers_by_id_default(api):
    endpoint_result = api.tacacs_external_servers.update_tacacs_external_servers_by_id(
        active_validation=False,
        id='string',
        connection_port=None,
        description=None,
        host_ip=None,
        name=None,
        payload=None,
        shared_secret=None,
        single_connect=None,
        timeout=None
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_update_tacacs_external_servers_by_id_default(api, validator):
    try:
        assert is_valid_update_tacacs_external_servers_by_id(
            validator,
            update_tacacs_external_servers_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_tacacs_external_servers_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_896816622564523798353b885b115048_v3_1_patch_1').validate(obj.response)
    return True


def delete_tacacs_external_servers_by_id(api):
    endpoint_result = api.tacacs_external_servers.delete_tacacs_external_servers_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_delete_tacacs_external_servers_by_id(api, validator):
    try:
        assert is_valid_delete_tacacs_external_servers_by_id(
            validator,
            delete_tacacs_external_servers_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_tacacs_external_servers_by_id_default(api):
    endpoint_result = api.tacacs_external_servers.delete_tacacs_external_servers_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_delete_tacacs_external_servers_by_id_default(api, validator):
    try:
        assert is_valid_delete_tacacs_external_servers_by_id(
            validator,
            delete_tacacs_external_servers_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tacacs_external_servers(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8c6c2a4908ee5f48b7e9cae7572f6a94_v3_1_patch_1').validate(obj.response)
    return True


def get_tacacs_external_servers(api):
    endpoint_result = api.tacacs_external_servers.get_tacacs_external_servers(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_get_tacacs_external_servers(api, validator):
    try:
        assert is_valid_get_tacacs_external_servers(
            validator,
            get_tacacs_external_servers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_tacacs_external_servers_default(api):
    endpoint_result = api.tacacs_external_servers.get_tacacs_external_servers(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_get_tacacs_external_servers_default(api, validator):
    try:
        assert is_valid_get_tacacs_external_servers(
            validator,
            get_tacacs_external_servers_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_tacacs_external_servers(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b5097e4db7505ba390914b50b1c2046b_v3_1_patch_1').validate(obj.response)
    return True


def create_tacacs_external_servers(api):
    endpoint_result = api.tacacs_external_servers.create_tacacs_external_servers(
        active_validation=False,
        connection_port=0,
        description='string',
        host_ip='string',
        name='string',
        payload=None,
        shared_secret='string',
        single_connect=True,
        timeout=0
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_create_tacacs_external_servers(api, validator):
    try:
        assert is_valid_create_tacacs_external_servers(
            validator,
            create_tacacs_external_servers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_tacacs_external_servers_default(api):
    endpoint_result = api.tacacs_external_servers.create_tacacs_external_servers(
        active_validation=False,
        connection_port=None,
        description=None,
        host_ip=None,
        name=None,
        payload=None,
        shared_secret=None,
        single_connect=None,
        timeout=None
    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_create_tacacs_external_servers_default(api, validator):
    try:
        assert is_valid_create_tacacs_external_servers(
            validator,
            create_tacacs_external_servers_default(api)
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
    json_schema_validate('jsd_d3e106d187b35547bf1f0463e4fc832f_v3_1_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.tacacs_external_servers.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
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
    endpoint_result = api.tacacs_external_servers.get_version(

    )
    return endpoint_result


@pytest.mark.tacacs_external_servers
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
