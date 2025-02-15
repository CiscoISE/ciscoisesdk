# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI external_radius_server API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.3_patch_1', reason='version does not match')


def is_valid_get_external_radius_server_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9afa6d7527045ebc928ee7e30ad3092a_v3_3_patch_1').validate(obj.response)
    return True


def get_external_radius_server_by_name(api):
    endpoint_result = api.external_radius_server.get_external_radius_server_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_get_external_radius_server_by_name(api, validator):
    try:
        assert is_valid_get_external_radius_server_by_name(
            validator,
            get_external_radius_server_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_external_radius_server_by_name_default(api):
    endpoint_result = api.external_radius_server.get_external_radius_server_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_get_external_radius_server_by_name_default(api, validator):
    try:
        assert is_valid_get_external_radius_server_by_name(
            validator,
            get_external_radius_server_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_external_radius_server_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_af14464cc6a05f6f87bbe7c174b6d5f6_v3_3_patch_1').validate(obj.response)
    return True


def get_external_radius_server_by_id(api):
    endpoint_result = api.external_radius_server.get_external_radius_server_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_get_external_radius_server_by_id(api, validator):
    try:
        assert is_valid_get_external_radius_server_by_id(
            validator,
            get_external_radius_server_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_external_radius_server_by_id_default(api):
    endpoint_result = api.external_radius_server.get_external_radius_server_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_get_external_radius_server_by_id_default(api, validator):
    try:
        assert is_valid_get_external_radius_server_by_id(
            validator,
            get_external_radius_server_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_external_radius_server_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_59c6536d17325c84a54189f46d4bbad2_v3_3_patch_1').validate(obj.response)
    return True


def update_external_radius_server_by_id(api):
    endpoint_result = api.external_radius_server.update_external_radius_server_by_id(
        accounting_port=0,
        active_validation=False,
        authentication_port=0,
        authenticator_key='string',
        description='string',
        enable_key_wrap=True,
        encryption_key='string',
        host_ip='string',
        id='string',
        key_input_format='string',
        name='string',
        payload=None,
        proxy_timeout=0,
        retries=0,
        shared_secret='string',
        timeout=0
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_update_external_radius_server_by_id(api, validator):
    try:
        assert is_valid_update_external_radius_server_by_id(
            validator,
            update_external_radius_server_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_external_radius_server_by_id_default(api):
    endpoint_result = api.external_radius_server.update_external_radius_server_by_id(
        active_validation=False,
        id='string',
        accounting_port=None,
        authentication_port=None,
        authenticator_key=None,
        description=None,
        enable_key_wrap=None,
        encryption_key=None,
        host_ip=None,
        key_input_format=None,
        name=None,
        payload=None,
        proxy_timeout=None,
        retries=None,
        shared_secret=None,
        timeout=None
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_update_external_radius_server_by_id_default(api, validator):
    try:
        assert is_valid_update_external_radius_server_by_id(
            validator,
            update_external_radius_server_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_external_radius_server_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d86e3201f9b0561db13a9eb1b1d59bd5_v3_3_patch_1').validate(obj.response)
    return True


def delete_external_radius_server_by_id(api):
    endpoint_result = api.external_radius_server.delete_external_radius_server_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_delete_external_radius_server_by_id(api, validator):
    try:
        assert is_valid_delete_external_radius_server_by_id(
            validator,
            delete_external_radius_server_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_external_radius_server_by_id_default(api):
    endpoint_result = api.external_radius_server.delete_external_radius_server_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_delete_external_radius_server_by_id_default(api, validator):
    try:
        assert is_valid_delete_external_radius_server_by_id(
            validator,
            delete_external_radius_server_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_external_radius_server(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9b641825a9555ecba105cabbdf50fc78_v3_3_patch_1').validate(obj.response)
    return True


def get_external_radius_server(api):
    endpoint_result = api.external_radius_server.get_external_radius_server(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_get_external_radius_server(api, validator):
    try:
        assert is_valid_get_external_radius_server(
            validator,
            get_external_radius_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_external_radius_server_default(api):
    endpoint_result = api.external_radius_server.get_external_radius_server(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_get_external_radius_server_default(api, validator):
    try:
        assert is_valid_get_external_radius_server(
            validator,
            get_external_radius_server_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_external_radius_server(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1fc1c74b35ae5050b4f7fd702570ad5b_v3_3_patch_1').validate(obj.response)
    return True


def create_external_radius_server(api):
    endpoint_result = api.external_radius_server.create_external_radius_server(
        accounting_port=0,
        active_validation=False,
        authentication_port=0,
        authenticator_key='string',
        description='string',
        enable_key_wrap=True,
        encryption_key='string',
        host_ip='string',
        key_input_format='string',
        name='string',
        payload=None,
        proxy_timeout=0,
        retries=0,
        shared_secret='string',
        timeout=0
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_create_external_radius_server(api, validator):
    try:
        assert is_valid_create_external_radius_server(
            validator,
            create_external_radius_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_external_radius_server_default(api):
    endpoint_result = api.external_radius_server.create_external_radius_server(
        active_validation=False,
        accounting_port=None,
        authentication_port=None,
        authenticator_key=None,
        description=None,
        enable_key_wrap=None,
        encryption_key=None,
        host_ip=None,
        key_input_format=None,
        name=None,
        payload=None,
        proxy_timeout=None,
        retries=None,
        shared_secret=None,
        timeout=None
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_create_external_radius_server_default(api, validator):
    try:
        assert is_valid_create_external_radius_server(
            validator,
            create_external_radius_server_default(api)
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
    json_schema_validate('jsd_a6c3ffe72746500b88be3a5418ead4ba_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.external_radius_server.get_version(

    )
    return endpoint_result


@pytest.mark.external_radius_server
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
    endpoint_result = api.external_radius_server.get_version(

    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_external_radius_server_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0d7468254be85e97a56521bff13da212_v3_3_patch_1').validate(obj.response)
    return True


def patch_external_radius_server_id(api):
    endpoint_result = api.external_radius_server.patch_external_radius_server_id(
        accounting_port={},
        active_validation=False,
        authentication_port={},
        authenticator_key='string',
        description='string',
        enable_key_wrap=True,
        encryption_key='string',
        host_ip='string',
        id='string',
        key_input_format='string',
        name='string',
        payload=None,
        proxy_timeout={},
        retries={},
        shared_secret='string',
        timeout={}
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_patch_external_radius_server_id(api, validator):
    try:
        assert is_valid_patch_external_radius_server_id(
            validator,
            patch_external_radius_server_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_external_radius_server_id_default(api):
    endpoint_result = api.externalradiusserver.patch_external_radius_server_id(
        active_validation=False,
        id='string',
        accounting_port=None,
        authentication_port=None,
        authenticator_key=None,
        description=None,
        enable_key_wrap=None,
        encryption_key=None,
        host_ip=None,
        key_input_format=None,
        name=None,
        payload=None,
        proxy_timeout=None,
        retries=None,
        shared_secret=None,
        timeout=None
    )
    return endpoint_result


@pytest.mark.external_radius_server
def test_patch_external_radius_server_id_default(api, validator):
    try:
        assert is_valid_patch_external_radius_server_id(
            validator,
            patch_external_radius_server_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
