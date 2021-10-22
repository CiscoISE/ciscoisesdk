# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI trust_sec_configuration API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_security_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9b5b0eb1671a51758acf5ec364d80738_v3_0_0').validate(obj.response)
    return True


def get_security_groups(api):
    endpoint_result = api.trust_sec_configuration.get_security_groups(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_security_groups(api, validator):
    try:
        assert is_valid_get_security_groups(
            validator,
            get_security_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_groups_default(api):
    endpoint_result = api.trust_sec_configuration.get_security_groups(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_security_groups_default(api, validator):
    try:
        assert is_valid_get_security_groups(
            validator,
            get_security_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_group_acls(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_02b4aa5797455ee4a27390b77262992d_v3_0_0').validate(obj.response)
    return True


def get_security_group_acls(api):
    endpoint_result = api.trust_sec_configuration.get_security_group_acls(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_security_group_acls(api, validator):
    try:
        assert is_valid_get_security_group_acls(
            validator,
            get_security_group_acls(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_group_acls_default(api):
    endpoint_result = api.trust_sec_configuration.get_security_group_acls(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_security_group_acls_default(api, validator):
    try:
        assert is_valid_get_security_group_acls(
            validator,
            get_security_group_acls_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_egress_policies(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3da8b5be1a475510a5aa1593d625ffbb_v3_0_0').validate(obj.response)
    return True


def get_egress_policies(api):
    endpoint_result = api.trust_sec_configuration.get_egress_policies(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_egress_policies(api, validator):
    try:
        assert is_valid_get_egress_policies(
            validator,
            get_egress_policies(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_egress_policies_default(api):
    endpoint_result = api.trust_sec_configuration.get_egress_policies(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_egress_policies_default(api, validator):
    try:
        assert is_valid_get_egress_policies(
            validator,
            get_egress_policies_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_egress_matrices(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3f9e6e1c33155fdd9a88f48d093f375b_v3_0_0').validate(obj.response)
    return True


def get_egress_matrices(api):
    endpoint_result = api.trust_sec_configuration.get_egress_matrices(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_egress_matrices(api, validator):
    try:
        assert is_valid_get_egress_matrices(
            validator,
            get_egress_matrices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_egress_matrices_default(api):
    endpoint_result = api.trust_sec_configuration.get_egress_matrices(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.trust_sec_configuration
def test_get_egress_matrices_default(api, validator):
    try:
        assert is_valid_get_egress_matrices(
            validator,
            get_egress_matrices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
