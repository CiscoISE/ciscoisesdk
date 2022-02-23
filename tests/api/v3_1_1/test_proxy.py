# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI proxy API fixtures and tests.

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


def is_valid_get_proxy_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d788d0c12f7956f0b7e37810d21f10f1_v3_1_1').validate(obj.response)
    return True


def get_proxy_connection(api):
    endpoint_result = api.proxy.get_proxy_connection(

    )
    return endpoint_result


@pytest.mark.proxy
def test_get_proxy_connection(api, validator):
    try:
        assert is_valid_get_proxy_connection(
            validator,
            get_proxy_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_proxy_connection_default(api):
    endpoint_result = api.proxy.get_proxy_connection(

    )
    return endpoint_result


@pytest.mark.proxy
def test_get_proxy_connection_default(api, validator):
    try:
        assert is_valid_get_proxy_connection(
            validator,
            get_proxy_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_proxy_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6903ddc568fc56f7b6310160e3fb3b2f_v3_1_1').validate(obj.response)
    return True


def update_proxy_connection(api):
    endpoint_result = api.proxy.update_proxy_connection(
        active_validation=False,
        bypass_hosts='string',
        fqdn='string',
        password='string',
        password_required=True,
        payload=None,
        port=0,
        user_name='string'
    )
    return endpoint_result


@pytest.mark.proxy
def test_update_proxy_connection(api, validator):
    try:
        assert is_valid_update_proxy_connection(
            validator,
            update_proxy_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_proxy_connection_default(api):
    endpoint_result = api.proxy.update_proxy_connection(
        active_validation=False,
        bypass_hosts=None,
        fqdn=None,
        password=None,
        password_required=None,
        payload=None,
        port=None,
        user_name=None
    )
    return endpoint_result


@pytest.mark.proxy
def test_update_proxy_connection_default(api, validator):
    try:
        assert is_valid_update_proxy_connection(
            validator,
            update_proxy_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
