# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI endpoint_certificate API fixtures and tests.

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


def is_valid_create_endpoint_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'data')
    return True


def create_endpoint_certificate(api):
    endpoint_result = api.endpoint_certificate.create_endpoint_certificate(
        dirpath=None,
        save_file=None,
        filename=None,
        active_validation=False,
        cert_template_name='string',
        certificate_request={'san': 'string', 'cn': 'string'},
        format='string',
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint_certificate
def test_create_endpoint_certificate(api, validator):
    try:
        assert is_valid_create_endpoint_certificate(
            validator,
            create_endpoint_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_endpoint_certificate_default(api):
    endpoint_result = api.endpoint_certificate.create_endpoint_certificate(
        dirpath=None,
        save_file=None,
        filename=None,
        active_validation=False,
        cert_template_name=None,
        certificate_request=None,
        format=None,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint_certificate
def test_create_endpoint_certificate_default(api, validator):
    try:
        assert is_valid_create_endpoint_certificate(
            validator,
            create_endpoint_certificate_default(api)
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
    json_schema_validate('jsd_4c5c84028d8f5c078d8ab37553812d39_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.endpoint_certificate.get_version(

    )
    return endpoint_result


@pytest.mark.endpoint_certificate
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
    endpoint_result = api.endpoint_certificate.get_version(

    )
    return endpoint_result


@pytest.mark.endpoint_certificate
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
