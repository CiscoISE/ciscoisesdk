# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI clear_threats_and_vulnerabilities API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_clear_threats_and_vulnerabilities(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e3110fc63ecb5428a075a8af8497fb35_v3_1_0').validate(obj.response)
    return True


def clear_threats_and_vulnerabilities(api):
    endpoint_result = api.clear_threats_and_vulnerabilities.clear_threats_and_vulnerabilities(
        active_validation=False,
        mac_addresses='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.clear_threats_and_vulnerabilities
def test_clear_threats_and_vulnerabilities(api, validator):
    try:
        assert is_valid_clear_threats_and_vulnerabilities(
            validator,
            clear_threats_and_vulnerabilities(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def clear_threats_and_vulnerabilities_default(api):
    endpoint_result = api.clear_threats_and_vulnerabilities.clear_threats_and_vulnerabilities(
        active_validation=False,
        mac_addresses=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.clear_threats_and_vulnerabilities
def test_clear_threats_and_vulnerabilities_default(api, validator):
    try:
        assert is_valid_clear_threats_and_vulnerabilities(
            validator,
            clear_threats_and_vulnerabilities_default(api)
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
    json_schema_validate('jsd_83379c74d24e5ae9bb90f798a190cca3_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.clear_threats_and_vulnerabilities.get_version(

    )
    return endpoint_result


@pytest.mark.clear_threats_and_vulnerabilities
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
    endpoint_result = api.clear_threats_and_vulnerabilities.get_version(

    )
    return endpoint_result


@pytest.mark.clear_threats_and_vulnerabilities
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
