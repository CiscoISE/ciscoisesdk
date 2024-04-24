# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI native_ipsec API fixtures and tests.

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


def is_valid_get_ipsec_enabled_nodes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_23993d9fe5cd54278a69cb1b5c800c32_v3_3_patch_1').validate(obj.response)
    return True


def get_ipsec_enabled_nodes(api):
    endpoint_result = api.native_ipsec.get_ipsec_enabled_nodes(
        filter='string',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_get_ipsec_enabled_nodes(api, validator):
    try:
        assert is_valid_get_ipsec_enabled_nodes(
            validator,
            get_ipsec_enabled_nodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_ipsec_enabled_nodes_default(api):
    endpoint_result = api.native_ipsec.get_ipsec_enabled_nodes(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_get_ipsec_enabled_nodes_default(api, validator):
    try:
        assert is_valid_get_ipsec_enabled_nodes(
            validator,
            get_ipsec_enabled_nodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_ipsec_connection_config(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5d4fb0706d0f5226b8691538a2bc7309_v3_3_patch_1').validate(obj.response)
    return True


def update_ipsec_connection_config(api):
    endpoint_result = api.native_ipsec.update_ipsec_connection_config(
        active_validation=False,
        auth_type='string',
        cert_id='string',
        configure_vti=True,
        esp_ah_protocol='string',
        host_name='string',
        iface='string',
        ike_re_auth_time=0,
        ike_version='string',
        local_internal_ip='string',
        mode_option='string',
        nad_ip='string',
        payload=None,
        phase_one_dhgroup='string',
        phase_one_encryption_algo='string',
        phase_one_hash_algo='string',
        phase_one_life_time=0,
        phase_two_dhgroup='string',
        phase_two_encryption_algo='string',
        phase_two_hash_algo='string',
        phase_two_life_time=0,
        psk='string',
        remote_peer_internal_ip='string'
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_update_ipsec_connection_config(api, validator):
    try:
        assert is_valid_update_ipsec_connection_config(
            validator,
            update_ipsec_connection_config(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_ipsec_connection_config_default(api):
    endpoint_result = api.native_ipsec.update_ipsec_connection_config(
        active_validation=False,
        auth_type=None,
        cert_id=None,
        configure_vti=None,
        esp_ah_protocol=None,
        host_name=None,
        iface=None,
        ike_re_auth_time=None,
        ike_version=None,
        local_internal_ip=None,
        mode_option=None,
        nad_ip=None,
        payload=None,
        phase_one_dhgroup=None,
        phase_one_encryption_algo=None,
        phase_one_hash_algo=None,
        phase_one_life_time=None,
        phase_two_dhgroup=None,
        phase_two_encryption_algo=None,
        phase_two_hash_algo=None,
        phase_two_life_time=None,
        psk=None,
        remote_peer_internal_ip=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_update_ipsec_connection_config_default(api, validator):
    try:
        assert is_valid_update_ipsec_connection_config(
            validator,
            update_ipsec_connection_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_ipsec_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_289ef20d5d63551dbe25878007747598_v3_3_patch_1').validate(obj.response)
    return True


def create_ipsec_connection(api):
    endpoint_result = api.native_ipsec.create_ipsec_connection(
        active_validation=False,
        auth_type='string',
        cert_id='string',
        configure_vti=True,
        esp_ah_protocol='string',
        host_name='string',
        iface='string',
        ike_re_auth_time=0,
        ike_version='string',
        local_internal_ip='string',
        mode_option='string',
        nad_ip='string',
        payload=None,
        phase_one_dhgroup='string',
        phase_one_encryption_algo='string',
        phase_one_hash_algo='string',
        phase_one_life_time=0,
        phase_two_dhgroup='string',
        phase_two_encryption_algo='string',
        phase_two_hash_algo='string',
        phase_two_life_time=0,
        psk='string',
        remote_peer_internal_ip='string'
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_create_ipsec_connection(api, validator):
    try:
        assert is_valid_create_ipsec_connection(
            validator,
            create_ipsec_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_ipsec_connection_default(api):
    endpoint_result = api.native_ipsec.create_ipsec_connection(
        active_validation=False,
        auth_type=None,
        cert_id=None,
        configure_vti=None,
        esp_ah_protocol=None,
        host_name=None,
        iface=None,
        ike_re_auth_time=None,
        ike_version=None,
        local_internal_ip=None,
        mode_option=None,
        nad_ip=None,
        payload=None,
        phase_one_dhgroup=None,
        phase_one_encryption_algo=None,
        phase_one_hash_algo=None,
        phase_one_life_time=None,
        phase_two_dhgroup=None,
        phase_two_encryption_algo=None,
        phase_two_hash_algo=None,
        phase_two_life_time=None,
        psk=None,
        remote_peer_internal_ip=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_create_ipsec_connection_default(api, validator):
    try:
        assert is_valid_create_ipsec_connection(
            validator,
            create_ipsec_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_ip_sec_operation(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_eca8a69196d555a1b7e71cf190bd2641_v3_3_patch_1').validate(obj.response)
    return True


def bulk_ip_sec_operation(api):
    endpoint_result = api.native_ipsec.bulk_ip_sec_operation(
        active_validation=False,
        item_list=[{'authType': 'string', 'certId': 'string', 'configureVti': True, 'espAhProtocol': 'string', 'hostName': 'string', 'iface': 'string', 'ikeReAuthTime': 0, 'ikeVersion': 'string', 'localInternalIp': 'string', 'modeOption': 'string', 'nadIp': 'string', 'phaseOneDHGroup': 'string', 'phaseOneEncryptionAlgo': 'string', 'phaseOneHashAlgo': 'string', 'phaseOneLifeTime': 0, 'phaseTwoDHGroup': 'string', 'phaseTwoEncryptionAlgo': 'string', 'phaseTwoHashAlgo': 'string', 'phaseTwoLifeTime': 0, 'psk': 'string', 'remotePeerInternalIp': 'string'}],
        operation='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_bulk_ip_sec_operation(api, validator):
    try:
        assert is_valid_bulk_ip_sec_operation(
            validator,
            bulk_ip_sec_operation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_ip_sec_operation_default(api):
    endpoint_result = api.native_ipsec.bulk_ip_sec_operation(
        active_validation=False,
        item_list=None,
        operation=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_bulk_ip_sec_operation_default(api, validator):
    try:
        assert is_valid_bulk_ip_sec_operation(
            validator,
            bulk_ip_sec_operation_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_sec_certificates(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3a5e87f906e357bcb972c60ee082d89b_v3_3_patch_1').validate(obj.response)
    return True


def get_ip_sec_certificates(api):
    endpoint_result = api.native_ipsec.get_ip_sec_certificates(

    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_get_ip_sec_certificates(api, validator):
    try:
        assert is_valid_get_ip_sec_certificates(
            validator,
            get_ip_sec_certificates(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_ip_sec_certificates_default(api):
    endpoint_result = api.native_ipsec.get_ip_sec_certificates(

    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_get_ip_sec_certificates_default(api, validator):
    try:
        assert is_valid_get_ip_sec_certificates(
            validator,
            get_ip_sec_certificates_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disable_ipsec_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_4f159a76b6aa52c2b0d0a2fe31dcae91_v3_3_patch_1').validate(obj.response)
    return True


def disable_ipsec_connection(api):
    endpoint_result = api.native_ipsec.disable_ipsec_connection(
        active_validation=False,
        host_name='string',
        nad_ip='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_disable_ipsec_connection(api, validator):
    try:
        assert is_valid_disable_ipsec_connection(
            validator,
            disable_ipsec_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def disable_ipsec_connection_default(api):
    endpoint_result = api.native_ipsec.disable_ipsec_connection(
        active_validation=False,
        host_name='string',
        nad_ip='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_disable_ipsec_connection_default(api, validator):
    try:
        assert is_valid_disable_ipsec_connection(
            validator,
            disable_ipsec_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_enable_ipsec_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2b57a1b126cb53ed8533eb22db13719d_v3_3_patch_1').validate(obj.response)
    return True


def enable_ipsec_connection(api):
    endpoint_result = api.native_ipsec.enable_ipsec_connection(
        active_validation=False,
        host_name='string',
        nad_ip='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_enable_ipsec_connection(api, validator):
    try:
        assert is_valid_enable_ipsec_connection(
            validator,
            enable_ipsec_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def enable_ipsec_connection_default(api):
    endpoint_result = api.native_ipsec.enable_ipsec_connection(
        active_validation=False,
        host_name='string',
        nad_ip='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_enable_ipsec_connection_default(api, validator):
    try:
        assert is_valid_enable_ipsec_connection(
            validator,
            enable_ipsec_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ipsec_node(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_208a5dd6bd055c73bc02c8a389fd353f_v3_3_patch_1').validate(obj.response)
    return True


def get_ipsec_node(api):
    endpoint_result = api.native_ipsec.get_ipsec_node(
        host_name='string',
        nad_ip='string'
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_get_ipsec_node(api, validator):
    try:
        assert is_valid_get_ipsec_node(
            validator,
            get_ipsec_node(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_ipsec_node_default(api):
    endpoint_result = api.native_ipsec.get_ipsec_node(
        host_name='string',
        nad_ip='string'
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_get_ipsec_node_default(api, validator):
    try:
        assert is_valid_get_ipsec_node(
            validator,
            get_ipsec_node_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_ipsec_connection(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9f2a9c1f22035982beaa10f027814d01_v3_3_patch_1').validate(obj.response)
    return True


def remove_ipsec_connection(api):
    endpoint_result = api.native_ipsec.remove_ipsec_connection(
        host_name='string',
        nad_ip='string'
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_remove_ipsec_connection(api, validator):
    try:
        assert is_valid_remove_ipsec_connection(
            validator,
            remove_ipsec_connection(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def remove_ipsec_connection_default(api):
    endpoint_result = api.native_ipsec.remove_ipsec_connection(
        host_name='string',
        nad_ip='string'
    )
    return endpoint_result


@pytest.mark.native_ipsec
def test_remove_ipsec_connection_default(api, validator):
    try:
        assert is_valid_remove_ipsec_connection(
            validator,
            remove_ipsec_connection_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
