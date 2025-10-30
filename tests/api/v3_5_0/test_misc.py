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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.5.0', reason='version does not match')


def is_valid_get_active_session_count(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_active_session_count(api):
    endpoint_result = api.misc.get_active_session_count(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_session_count(api, validator):
    try:
        assert is_valid_get_active_session_count(
            validator,
            get_active_session_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_session_count_default(api):
    endpoint_result = api.misc.get_active_session_count(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_session_count_default(api, validator):
    try:
        assert is_valid_get_active_session_count(
            validator,
            get_active_session_count_default(api)
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


def is_valid_get_active_session_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_active_session_list(api):
    endpoint_result = api.misc.get_active_session_list(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_session_list(api, validator):
    try:
        assert is_valid_get_active_session_list(
            validator,
            get_active_session_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_session_list_default(api):
    endpoint_result = api.misc.get_active_session_list(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_session_list_default(api, validator):
    try:
        assert is_valid_get_active_session_list(
            validator,
            get_active_session_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_auth_session_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_auth_session_list(api):
    endpoint_result = api.misc.get_auth_session_list(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_auth_session_list(api, validator):
    try:
        assert is_valid_get_auth_session_list(
            validator,
            get_auth_session_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_auth_session_list_default(api):
    endpoint_result = api.misc.get_auth_session_list(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_auth_session_list_default(api, validator):
    try:
        assert is_valid_get_auth_session_list(
            validator,
            get_auth_session_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_full_s_d_mac_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_full_s_d_mac_info(api):
    endpoint_result = api.misc.get_full_s_d_mac_info(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_s_d_mac_info(api, validator):
    try:
        assert is_valid_get_full_s_d_mac_info(
            validator,
            get_full_s_d_mac_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_full_s_d_mac_info_default(api):
    endpoint_result = api.misc.get_full_s_d_mac_info(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_s_d_mac_info_default(api, validator):
    try:
        assert is_valid_get_full_s_d_mac_info(
            validator,
            get_full_s_d_mac_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_full_s_d_username_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_full_s_d_username_info(api):
    endpoint_result = api.misc.get_full_s_d_username_info(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_s_d_username_info(api, validator):
    try:
        assert is_valid_get_full_s_d_username_info(
            validator,
            get_full_s_d_username_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_full_s_d_username_info_default(api):
    endpoint_result = api.misc.get_full_s_d_username_info(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_s_d_username_info_default(api, validator):
    try:
        assert is_valid_get_full_s_d_username_info(
            validator,
            get_full_s_d_username_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_full_s_d_ip_address_info(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_full_s_d_ip_address_info(api):
    endpoint_result = api.misc.get_full_s_d_ip_address_info(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_s_d_ip_address_info(api, validator):
    try:
        assert is_valid_get_full_s_d_ip_address_info(
            validator,
            get_full_s_d_ip_address_info(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_full_s_d_ip_address_info_default(api):
    endpoint_result = api.misc.get_full_s_d_ip_address_info(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_s_d_ip_address_info_default(api, validator):
    try:
        assert is_valid_get_full_s_d_ip_address_info(
            validator,
            get_full_s_d_ip_address_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_active_session_by_session_id_and_output_type(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_active_session_by_session_id_and_output_type(api):
    endpoint_result = api.misc.get_active_session_by_session_id_and_output_type(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_session_by_session_id_and_output_type(api, validator):
    try:
        assert is_valid_get_active_session_by_session_id_and_output_type(
            validator,
            get_active_session_by_session_id_and_output_type(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_session_by_session_id_and_output_type_default(api):
    endpoint_result = api.misc.get_active_session_by_session_id_and_output_type(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_active_session_by_session_id_and_output_type_default(api, validator):
    try:
        assert is_valid_get_active_session_by_session_id_and_output_type(
            validator,
            get_active_session_by_session_id_and_output_type_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_product_version(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_product_version(api):
    endpoint_result = api.misc.get_product_version(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_product_version(api, validator):
    try:
        assert is_valid_get_product_version(
            validator,
            get_product_version(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_product_version_default(api):
    endpoint_result = api.misc.get_product_version(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_product_version_default(api, validator):
    try:
        assert is_valid_get_product_version(
            validator,
            get_product_version_default(api)
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


def is_valid_get_auth_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_auth_status(api):
    endpoint_result = api.misc.get_auth_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_auth_status(api, validator):
    try:
        assert is_valid_get_auth_status(
            validator,
            get_auth_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_auth_status_default(api):
    endpoint_result = api.misc.get_auth_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_auth_status_default(api, validator):
    try:
        assert is_valid_get_auth_status(
            validator,
            get_auth_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_acct_status_t_t(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_acct_status_t_t(api):
    endpoint_result = api.misc.get_acct_status_t_t(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_acct_status_t_t(api, validator):
    try:
        assert is_valid_get_acct_status_t_t(
            validator,
            get_acct_status_t_t(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_acct_status_t_t_default(api):
    endpoint_result = api.misc.get_acct_status_t_t(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_acct_status_t_t_default(api, validator):
    try:
        assert is_valid_get_acct_status_t_t(
            validator,
            get_acct_status_t_t_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_co_a_reauth_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_co_a_reauth_status(api):
    endpoint_result = api.misc.get_co_a_reauth_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_co_a_reauth_status(api, validator):
    try:
        assert is_valid_get_co_a_reauth_status(
            validator,
            get_co_a_reauth_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_co_a_reauth_status_default(api):
    endpoint_result = api.misc.get_co_a_reauth_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_co_a_reauth_status_default(api, validator):
    try:
        assert is_valid_get_co_a_reauth_status(
            validator,
            get_co_a_reauth_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_co_a_disconnect_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_co_a_disconnect_status(api):
    endpoint_result = api.misc.get_co_a_disconnect_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_co_a_disconnect_status(api, validator):
    try:
        assert is_valid_get_co_a_disconnect_status(
            validator,
            get_co_a_disconnect_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_co_a_disconnect_status_default(api):
    endpoint_result = api.misc.get_co_a_disconnect_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_co_a_disconnect_status_default(api, validator):
    try:
        assert is_valid_get_co_a_disconnect_status(
            validator,
            get_co_a_disconnect_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_full_session_details_for_end_point_ip_address(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_full_session_details_for_end_point_ip_address(api):
    endpoint_result = api.misc.get_full_session_details_for_end_point_ip_address(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_session_details_for_end_point_ip_address(api, validator):
    try:
        assert is_valid_get_full_session_details_for_end_point_ip_address(
            validator,
            get_full_session_details_for_end_point_ip_address(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_full_session_details_for_end_point_ip_address_default(api):
    endpoint_result = api.misc.get_full_session_details_for_end_point_ip_address(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_full_session_details_for_end_point_ip_address_default(api, validator):
    try:
        assert is_valid_get_full_session_details_for_end_point_ip_address(
            validator,
            get_full_session_details_for_end_point_ip_address_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_session_record_by_macaddress(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def delete_session_record_by_macaddress(api):
    endpoint_result = api.misc.delete_session_record_by_macaddress(
    )
    return endpoint_result


@pytest.mark.misc
def test_delete_session_record_by_macaddress(api, validator):
    try:
        assert is_valid_delete_session_record_by_macaddress(
            validator,
            delete_session_record_by_macaddress(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_session_record_by_macaddress_default(api):
    endpoint_result = api.misc.delete_session_record_by_macaddress(
    )
    return endpoint_result


@pytest.mark.misc
def test_delete_session_record_by_macaddress_default(api, validator):
    try:
        assert is_valid_delete_session_record_by_macaddress(
            validator,
            delete_session_record_by_macaddress_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_session_record_by_session_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def delete_session_record_by_session_id(api):
    endpoint_result = api.misc.delete_session_record_by_session_id(
    )
    return endpoint_result


@pytest.mark.misc
def test_delete_session_record_by_session_id(api, validator):
    try:
        assert is_valid_delete_session_record_by_session_id(
            validator,
            delete_session_record_by_session_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_session_record_by_session_id_default(api):
    endpoint_result = api.misc.delete_session_record_by_session_id(
    )
    return endpoint_result


@pytest.mark.misc
def test_delete_session_record_by_session_id_default(api, validator):
    try:
        assert is_valid_delete_session_record_by_session_id(
            validator,
            delete_session_record_by_session_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_all_session_records(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def delete_all_session_records(api):
    endpoint_result = api.misc.delete_all_session_records(
    )
    return endpoint_result


@pytest.mark.misc
def test_delete_all_session_records(api, validator):
    try:
        assert is_valid_delete_all_session_records(
            validator,
            delete_all_session_records(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_all_session_records_default(api):
    endpoint_result = api.misc.delete_all_session_records(
    )
    return endpoint_result


@pytest.mark.misc
def test_delete_all_session_records_default(api, validator):
    try:
        assert is_valid_delete_all_session_records(
            validator,
            delete_all_session_records_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_acct_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_acct_status(api):
    endpoint_result = api.misc.get_acct_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_acct_status(api, validator):
    try:
        assert is_valid_get_acct_status(
            validator,
            get_acct_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_acct_status_default(api):
    endpoint_result = api.misc.get_acct_status(
    )
    return endpoint_result


@pytest.mark.misc
def test_get_acct_status_default(api, validator):
    try:
        assert is_valid_get_acct_status(
            validator,
            get_acct_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


