# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI duo_mfa API fixtures and tests.

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


def is_valid_get_mfa(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f1841c8263105468a0e51fc4751ba6dc_v3_3_patch_1').validate(obj.response)
    return True


def get_mfa(api):
    endpoint_result = api.duo_mfa.get_mfa(

    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_get_mfa(api, validator):
    try:
        assert is_valid_get_mfa(
            validator,
            get_mfa(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_mfa_default(api):
    endpoint_result = api.duo_mfa.get_mfa(

    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_get_mfa_default(api, validator):
    try:
        assert is_valid_get_mfa(
            validator,
            get_mfa_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_mfa(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_45dcf17da7955cee9028a267873d055f_v3_3_patch_1').validate(obj.response)
    return True


def create_mfa(api):
    endpoint_result = api.duo_mfa.create_mfa(
        account_configurations={'adminApi': {'ikey': 'string', 'sKey': 'string'}, 'apiHostName': 'string', 'authenticationApi': {'ikey': 'string', 'sKey': 'string'}},
        active_validation=False,
        connection_name='string',
        description='string',
        identity_sync='string',
        payload=None,
        type='string'
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_create_mfa(api, validator):
    try:
        assert is_valid_create_mfa(
            validator,
            create_mfa(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_mfa_default(api):
    endpoint_result = api.duo_mfa.create_mfa(
        active_validation=False,
        account_configurations=None,
        connection_name=None,
        description=None,
        identity_sync=None,
        payload=None,
        type=None
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_create_mfa_default(api, validator):
    try:
        assert is_valid_create_mfa(
            validator,
            create_mfa_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_test_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4fb47bc0b25f53b093b356d41f1c59ab_v3_3_patch_1').validate(obj.response)
    return True


def test_connection(api):
    endpoint_result = api.duo_mfa.test_connection(
        active_validation=False,
        admin_api={'ikey': 'string', 'sKey': 'string'},
        api_host_name='string',
        authentication_api={'ikey': 'string', 'sKey': 'string'},
        connection_name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_test_connection(api, validator):
    try:
        assert is_valid_test_connection(
            validator,
            test_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def test_connection_default(api):
    endpoint_result = api.duo_mfa.test_connection(
        active_validation=False,
        connection_name='string',
        admin_api=None,
        api_host_name=None,
        authentication_api=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_test_connection_default(api, validator):
    try:
        assert is_valid_test_connection(
            validator,
            test_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_mfa_byconnection_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_72fe75e2be3e56c9836c9c0db3a4be20_v3_3_patch_1').validate(obj.response)
    return True


def get_mfa_byconnection_name(api):
    endpoint_result = api.duo_mfa.get_mfa_byconnection_name(
        connection_name='string'
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_get_mfa_byconnection_name(api, validator):
    try:
        assert is_valid_get_mfa_byconnection_name(
            validator,
            get_mfa_byconnection_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_mfa_byconnection_name_default(api):
    endpoint_result = api.duo_mfa.get_mfa_byconnection_name(
        connection_name='string'
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_get_mfa_byconnection_name_default(api, validator):
    try:
        assert is_valid_get_mfa_byconnection_name(
            validator,
            get_mfa_byconnection_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_m_fa_by_connection_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_803320e8eb885d7cb70656383f03864f_v3_3_patch_1').validate(obj.response)
    return True


def update_m_fa_by_connection_name(api):
    endpoint_result = api.duo_mfa.update_m_fa_by_connection_name(
        account_configurations={'adminApi': {'ikey': 'string', 'sKey': 'string'}, 'apiHostName': 'string', 'authenticationApi': {'ikey': 'string', 'sKey': 'string'}},
        active_validation=False,
        connection_name='string',
        description='string',
        identity_sync='string',
        payload=None,
        type='string'
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_update_m_fa_by_connection_name(api, validator):
    try:
        assert is_valid_update_m_fa_by_connection_name(
            validator,
            update_m_fa_by_connection_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_m_fa_by_connection_name_default(api):
    endpoint_result = api.duo_mfa.update_m_fa_by_connection_name(
        active_validation=False,
        connection_name='string',
        account_configurations=None,
        description=None,
        identity_sync=None,
        payload=None,
        type=None
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_update_m_fa_by_connection_name_default(api, validator):
    try:
        assert is_valid_update_m_fa_by_connection_name(
            validator,
            update_m_fa_by_connection_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_mfa_by_connection_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bec78a0adabd51a7bb03a74616b7b501_v3_3_patch_1').validate(obj.response)
    return True


def delete_mfa_by_connection_name(api):
    endpoint_result = api.duo_mfa.delete_mfa_by_connection_name(
        connection_name='string'
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_delete_mfa_by_connection_name(api, validator):
    try:
        assert is_valid_delete_mfa_by_connection_name(
            validator,
            delete_mfa_by_connection_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_mfa_by_connection_name_default(api):
    endpoint_result = api.duo_mfa.delete_mfa_by_connection_name(
        connection_name='string'
    )
    return endpoint_result


@pytest.mark.duo_mfa
def test_delete_mfa_by_connection_name_default(api, validator):
    try:
        assert is_valid_delete_mfa_by_connection_name(
            validator,
            delete_mfa_by_connection_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
