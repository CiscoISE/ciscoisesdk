# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI misc API fixtures and tests.

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


def is_valid_get_active_count(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0e629f554fa652d980ff08988c788c57_v3_1_patch_1').validate(obj.response)
    return True


def get_active_count(api):
    endpoint_result = api.misc.get_active_count(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_count(api, validator):
    try:
        assert is_valid_get_active_count(
            validator,
            get_active_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_count_default(api):
    endpoint_result = api.misc.get_active_count(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_count_default(api, validator):
    try:
        assert is_valid_get_active_count(
            validator,
            get_active_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_active_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6a6c71a1e4d2597ea1b5533e9f1b438f_v3_1_patch_1').validate(obj.response)
    return True


def get_active_list(api):
    endpoint_result = api.misc.get_active_list(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_list(api, validator):
    try:
        assert is_valid_get_active_list(
            validator,
            get_active_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_list_default(api):
    endpoint_result = api.misc.get_active_list(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_list_default(api, validator):
    try:
        assert is_valid_get_active_list(
            validator,
            get_active_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_session_auth_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2d91e71e5b84583fb8ea91fcd9fb6751_v3_1_patch_1').validate(obj.response)
    return True


def get_session_auth_list(api):
    endpoint_result = api.misc.get_session_auth_list(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_session_auth_list(api, validator):
    try:
        assert is_valid_get_session_auth_list(
            validator,
            get_session_auth_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_session_auth_list_default(api):
    endpoint_result = api.misc.get_session_auth_list(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_session_auth_list_default(api, validator):
    try:
        assert is_valid_get_session_auth_list(
            validator,
            get_session_auth_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_posture_count(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_83d51ebdbbc75c0f8ed6161ae070a276_v3_1_patch_1').validate(obj.response)
    return True


def get_posture_count(api):
    endpoint_result = api.misc.get_posture_count(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_posture_count(api, validator):
    try:
        assert is_valid_get_posture_count(
            validator,
            get_posture_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_posture_count_default(api):
    endpoint_result = api.misc.get_posture_count(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_posture_count_default(api, validator):
    try:
        assert is_valid_get_posture_count(
            validator,
            get_posture_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_profiler_count(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1bdb77066ba75002bd343de0e9120b86_v3_1_patch_1').validate(obj.response)
    return True


def get_profiler_count(api):
    endpoint_result = api.misc.get_profiler_count(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_profiler_count(api, validator):
    try:
        assert is_valid_get_profiler_count(
            validator,
            get_profiler_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_profiler_count_default(api):
    endpoint_result = api.misc.get_profiler_count(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_profiler_count_default(api, validator):
    try:
        assert is_valid_get_profiler_count(
            validator,
            get_profiler_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sessions_by_mac(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b93e1accc1f35864b9a5b7bc478c7a7c_v3_1_patch_1').validate(obj.response)
    return True


def get_sessions_by_mac(api):
    endpoint_result = api.misc.get_sessions_by_mac(
        mac='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_mac(api, validator):
    try:
        assert is_valid_get_sessions_by_mac(
            validator,
            get_sessions_by_mac(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sessions_by_mac_default(api):
    endpoint_result = api.misc.get_sessions_by_mac(
        mac='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_mac_default(api, validator):
    try:
        assert is_valid_get_sessions_by_mac(
            validator,
            get_sessions_by_mac_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sessions_by_username(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8329e037613954b58692d89d64eba681_v3_1_patch_1').validate(obj.response)
    return True


def get_sessions_by_username(api):
    endpoint_result = api.misc.get_sessions_by_username(
        username='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_username(api, validator):
    try:
        assert is_valid_get_sessions_by_username(
            validator,
            get_sessions_by_username(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sessions_by_username_default(api):
    endpoint_result = api.misc.get_sessions_by_username(
        username='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_username_default(api, validator):
    try:
        assert is_valid_get_sessions_by_username(
            validator,
            get_sessions_by_username_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sessions_by_nas_ip(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_323fb7171efd5df8a0fe319983882265_v3_1_patch_1').validate(obj.response)
    return True


def get_sessions_by_nas_ip(api):
    endpoint_result = api.misc.get_sessions_by_nas_ip(
        nas_ipv4='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_nas_ip(api, validator):
    try:
        assert is_valid_get_sessions_by_nas_ip(
            validator,
            get_sessions_by_nas_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sessions_by_nas_ip_default(api):
    endpoint_result = api.misc.get_sessions_by_nas_ip(
        nas_ipv4='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_nas_ip_default(api, validator):
    try:
        assert is_valid_get_sessions_by_nas_ip(
            validator,
            get_sessions_by_nas_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sessions_by_endpoint_ip(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_123c7f72c6db5ecbb380133c106d0566_v3_1_patch_1').validate(obj.response)
    return True


def get_sessions_by_endpoint_ip(api):
    endpoint_result = api.misc.get_sessions_by_endpoint_ip(
        endpoint_ipv4='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_endpoint_ip(api, validator):
    try:
        assert is_valid_get_sessions_by_endpoint_ip(
            validator,
            get_sessions_by_endpoint_ip(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sessions_by_endpoint_ip_default(api):
    endpoint_result = api.misc.get_sessions_by_endpoint_ip(
        endpoint_ipv4='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_endpoint_ip_default(api, validator):
    try:
        assert is_valid_get_sessions_by_endpoint_ip(
            validator,
            get_sessions_by_endpoint_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sessions_by_session_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4eb415db854f5b12aa326bde54285c59_v3_1_patch_1').validate(obj.response)
    return True


def get_sessions_by_session_id(api):
    endpoint_result = api.misc.get_sessions_by_session_id(
        session_id='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_session_id(api, validator):
    try:
        assert is_valid_get_sessions_by_session_id(
            validator,
            get_sessions_by_session_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sessions_by_session_id_default(api):
    endpoint_result = api.misc.get_sessions_by_session_id(
        session_id='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_sessions_by_session_id_default(api, validator):
    try:
        assert is_valid_get_sessions_by_session_id(
            validator,
            get_sessions_by_session_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_all_sessions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_549bd2a2c3735c6ca7b59c86d428e222_v3_1_patch_1').validate(obj.response)
    return True


def delete_all_sessions(api):
    endpoint_result = api.misc.delete_all_sessions(

    )
    return endpoint_result


@pytest.mark.misc
def test_delete_all_sessions(api, validator):
    try:
        assert is_valid_delete_all_sessions(
            validator,
            delete_all_sessions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_all_sessions_default(api):
    endpoint_result = api.misc.delete_all_sessions(

    )
    return endpoint_result


@pytest.mark.misc
def test_delete_all_sessions_default(api, validator):
    try:
        assert is_valid_delete_all_sessions(
            validator,
            delete_all_sessions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_mnt_version(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_fc354ec4d361514a8e949f628f8e5f89_v3_1_patch_1').validate(obj.response)
    return True


def get_mnt_version(api):
    endpoint_result = api.misc.get_mnt_version(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_mnt_version(api, validator):
    try:
        assert is_valid_get_mnt_version(
            validator,
            get_mnt_version(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_mnt_version_default(api):
    endpoint_result = api.misc.get_mnt_version(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_mnt_version_default(api, validator):
    try:
        assert is_valid_get_mnt_version(
            validator,
            get_mnt_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_failure_reasons(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e346dbd9f9df554da3a3bcc06f4e77d5_v3_1_patch_1').validate(obj.response)
    return True


def get_failure_reasons(api):
    endpoint_result = api.misc.get_failure_reasons(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_failure_reasons(api, validator):
    try:
        assert is_valid_get_failure_reasons(
            validator,
            get_failure_reasons(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_failure_reasons_default(api):
    endpoint_result = api.misc.get_failure_reasons(

    )
    return endpoint_result


@pytest.mark.misc
def test_get_failure_reasons_default(api, validator):
    try:
        assert is_valid_get_failure_reasons(
            validator,
            get_failure_reasons_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_authentication_status_by_mac(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8877b26746235997bc32ace7d67d6987_v3_1_patch_1').validate(obj.response)
    return True


def get_authentication_status_by_mac(api):
    endpoint_result = api.misc.get_authentication_status_by_mac(
        mac='string',
        sseconds='string',
        seconds='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_authentication_status_by_mac(api, validator):
    try:
        assert is_valid_get_authentication_status_by_mac(
            validator,
            get_authentication_status_by_mac(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_authentication_status_by_mac_default(api):
    endpoint_result = api.misc.get_authentication_status_by_mac(
        mac='string',
        sseconds='string',
        seconds='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_authentication_status_by_mac_default(api, validator):
    try:
        assert is_valid_get_authentication_status_by_mac(
            validator,
            get_authentication_status_by_mac_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_session_reauthentication_by_mac(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7f73477346fb5e7097d915c7f0a99659_v3_1_patch_1').validate(obj.response)
    return True


def session_reauthentication_by_mac(api):
    endpoint_result = api.misc.session_reauthentication_by_mac(
        endpoint_mac='string',
        psn_name='string',
        reauth_type='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_session_reauthentication_by_mac(api, validator):
    try:
        assert is_valid_session_reauthentication_by_mac(
            validator,
            session_reauthentication_by_mac(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def session_reauthentication_by_mac_default(api):
    endpoint_result = api.misc.session_reauthentication_by_mac(
        endpoint_mac='string',
        psn_name='string',
        reauth_type='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_session_reauthentication_by_mac_default(api, validator):
    try:
        assert is_valid_session_reauthentication_by_mac(
            validator,
            session_reauthentication_by_mac_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_session_disconnect(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5504a097870d5734861255a347911a24_v3_1_patch_1').validate(obj.response)
    return True


def session_disconnect(api):
    endpoint_result = api.misc.session_disconnect(
        disconnect_type='string',
        endpoint_ip='string',
        mac='string',
        nas_ipv4='string',
        psn_name='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_session_disconnect(api, validator):
    try:
        assert is_valid_session_disconnect(
            validator,
            session_disconnect(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, ciscoisesdkException)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def session_disconnect_default(api):
    endpoint_result = api.misc.session_disconnect(
        disconnect_type='string',
        endpoint_ip='string',
        mac='string',
        nas_ipv4='string',
        psn_name='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_session_disconnect_default(api, validator):
    try:
        assert is_valid_session_disconnect(
            validator,
            session_disconnect_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError, ciscoisesdkException)):
            raise original_e


def is_valid_get_account_status_by_mac(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_644ab0a3ec0359faa72142f074145f6a_v3_1_patch_1').validate(obj.response)
    return True


def get_account_status_by_mac(api):
    endpoint_result = api.misc.get_account_status_by_mac(
        duration='string',
        mac='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_account_status_by_mac(api, validator):
    try:
        assert is_valid_get_account_status_by_mac(
            validator,
            get_account_status_by_mac(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_account_status_by_mac_default(api):
    endpoint_result = api.misc.get_account_status_by_mac(
        duration='string',
        mac='string'
    )
    return endpoint_result


@pytest.mark.misc
def test_get_account_status_by_mac_default(api, validator):
    try:
        assert is_valid_get_account_status_by_mac(
            validator,
            get_account_status_by_mac_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
