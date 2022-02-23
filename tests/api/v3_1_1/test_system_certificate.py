# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI system_certificate API fixtures and tests.

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


def is_valid_create_system_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_dd469dcee9445c72a3861ef94fb3b096_v3_1_1').validate(obj.response)
    return True


def create_system_certificate(api):
    endpoint_result = api.system_certificate.create_system_certificate(
        active_validation=False,
        ers_local_cert_stub={'friendlyName': 'string', 'ersSubjectStub': {'commonName': 'string', 'organizationalUnitName': 'string', 'organizationName': 'string', 'localityName': 'string', 'stateOrProvinceName': 'string', 'countryName': 'string'}, 'keyLength': 'string', 'xgridCertificate': 'string', 'groupTagDD': 'string', 'samlCertificate': 'string', 'keyType': 'string', 'digest': 'string', 'certificatePolicies': 'string', 'expirationTTL': 0, 'selectedExpirationTTLUnit': 'string', 'allowWildcardCerts': 'string', 'certificateSanDns': 'string', 'certificateSanIp': 'string', 'certificateSanUri': 'string'},
        node_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.system_certificate
def test_create_system_certificate(api, validator):
    try:
        assert is_valid_create_system_certificate(
            validator,
            create_system_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_system_certificate_default(api):
    endpoint_result = api.system_certificate.create_system_certificate(
        active_validation=False,
        ers_local_cert_stub=None,
        node_id=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.system_certificate
def test_create_system_certificate_default(api, validator):
    try:
        assert is_valid_create_system_certificate(
            validator,
            create_system_certificate_default(api)
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
    json_schema_validate('jsd_3512a19fb8fe5fe9b069aa19d2dd74d5_v3_1_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.system_certificate.get_version(

    )
    return endpoint_result


@pytest.mark.system_certificate
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
    endpoint_result = api.system_certificate.get_version(

    )
    return endpoint_result


@pytest.mark.system_certificate
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
