# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_device API fixtures and tests.

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


def is_valid_get_network_device_by_name(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_54d8610d4a355b63aaaa364447d5fa00_v3_1_0').validate(obj.response)
    return True


def get_network_device_by_name(api):
    endpoint_result = api.network_device.get_network_device_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_get_network_device_by_name(api, validator):
    try:
        assert is_valid_get_network_device_by_name(
            validator,
            get_network_device_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_name_default(api):
    endpoint_result = api.network_device.get_network_device_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_get_network_device_by_name_default(api, validator):
    try:
        assert is_valid_get_network_device_by_name(
            validator,
            get_network_device_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_device_by_name(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_2ea2c4586b845888b2a9375126f70de2_v3_1_0').validate(obj.response)
    return True


def update_network_device_by_name(api):
    endpoint_result = api.network_device.update_network_device_by_name(
        active_validation=False,
        authentication_settings={'networkProtocol': 'string', 'secondRadiusSharedSecret': 'string', 'radiusSharedSecret': 'string', 'enableKeyWrap': True, 'enabled': True, 'dtlsRequired': True, 'enableMultiSecret': 'string', 'keyEncryptionKey': 'string', 'messageAuthenticatorCodeKey': 'string', 'keyInputFormat': 'string'},
        coa_port=0,
        description='string',
        dtls_dns_name='string',
        id='string',
        model_name='string',
        name='string',
        network_device_group_list=['string'],
        network_device_iplist=[{'ipaddress': 'string', 'mask': 0, 'getIpaddressExclude': 'string'}],
        payload=None,
        profile_name='string',
        snmpsettings={'version': 'string', 'roCommunity': 'string', 'pollingInterval': 0, 'linkTrapQuery': True, 'macTrapQuery': True, 'originatingPolicyServicesNode': 'string'},
        software_version='string',
        tacacs_settings={'sharedSecret': 'string', 'connectModeOptions': 'string'},
        trustsecsettings={'deviceAuthenticationSettings': {'sgaDeviceId': 'string', 'sgaDevicePassword': 'string'}, 'sgaNotificationAndUpdates': {'downlaodEnvironmentDataEveryXSeconds': 0, 'downlaodPeerAuthorizationPolicyEveryXSeconds': 0, 'reAuthenticationEveryXSeconds': 0, 'downloadSGACLListsEveryXSeconds': 0, 'otherSGADevicesToTrustThisDevice': True, 'sendConfigurationToDevice': True, 'sendConfigurationToDeviceUsing': 'string', 'coaSourceHost': 'string'}, 'deviceConfigurationDeployment': {'includeWhenDeployingSGTUpdates': True, 'enableModePassword': 'string', 'execModePassword': 'string', 'execModeUsername': 'string'}, 'pushIdSupport': True}
    )
    return endpoint_result


@pytest.mark.network_device
def test_update_network_device_by_name(api, validator):
    try:
        assert is_valid_update_network_device_by_name(
            validator,
            update_network_device_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_device_by_name_default(api):
    endpoint_result = api.network_device.update_network_device_by_name(
        active_validation=False,
        name='string',
        authentication_settings=None,
        coa_port=None,
        description=None,
        dtls_dns_name=None,
        id=None,
        model_name=None,
        network_device_group_list=None,
        network_device_iplist=None,
        payload=None,
        profile_name=None,
        snmpsettings=None,
        software_version=None,
        tacacs_settings=None,
        trustsecsettings=None
    )
    return endpoint_result


@pytest.mark.network_device
def test_update_network_device_by_name_default(api, validator):
    try:
        assert is_valid_update_network_device_by_name(
            validator,
            update_network_device_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_device_by_name(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_116eafaf2e785c6898fb982dbe4462e7_v3_1_0').validate(obj.response)
    return True


def delete_network_device_by_name(api):
    endpoint_result = api.network_device.delete_network_device_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_delete_network_device_by_name(api, validator):
    try:
        assert is_valid_delete_network_device_by_name(
            validator,
            delete_network_device_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_device_by_name_default(api):
    endpoint_result = api.network_device.delete_network_device_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_delete_network_device_by_name_default(api, validator):
    try:
        assert is_valid_delete_network_device_by_name(
            validator,
            delete_network_device_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_a4ab683ce53052e089626a096abaf451_v3_1_0').validate(obj.response)
    return True


def get_network_device_by_id(api):
    endpoint_result = api.network_device.get_network_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_get_network_device_by_id(api, validator):
    try:
        assert is_valid_get_network_device_by_id(
            validator,
            get_network_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_by_id_default(api):
    endpoint_result = api.network_device.get_network_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_get_network_device_by_id_default(api, validator):
    try:
        assert is_valid_get_network_device_by_id(
            validator,
            get_network_device_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_device_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_b1edfeb182025176bb250633937177ae_v3_1_0').validate(obj.response)
    return True


def update_network_device_by_id(api):
    endpoint_result = api.network_device.update_network_device_by_id(
        active_validation=False,
        authentication_settings={'networkProtocol': 'string', 'secondRadiusSharedSecret': 'string', 'radiusSharedSecret': 'string', 'enableKeyWrap': True, 'enabled': True, 'dtlsRequired': True, 'enableMultiSecret': 'string', 'keyEncryptionKey': 'string', 'messageAuthenticatorCodeKey': 'string', 'keyInputFormat': 'string'},
        coa_port=0,
        description='string',
        dtls_dns_name='string',
        id='string',
        model_name='string',
        name='string',
        network_device_group_list=['string'],
        network_device_iplist=[{'ipaddress': 'string', 'mask': 0, 'getIpaddressExclude': 'string'}],
        payload=None,
        profile_name='string',
        snmpsettings={'version': 'string', 'roCommunity': 'string', 'pollingInterval': 0, 'linkTrapQuery': True, 'macTrapQuery': True, 'originatingPolicyServicesNode': 'string'},
        software_version='string',
        tacacs_settings={'sharedSecret': 'string', 'connectModeOptions': 'string'},
        trustsecsettings={'deviceAuthenticationSettings': {'sgaDeviceId': 'string', 'sgaDevicePassword': 'string'}, 'sgaNotificationAndUpdates': {'downlaodEnvironmentDataEveryXSeconds': 0, 'downlaodPeerAuthorizationPolicyEveryXSeconds': 0, 'reAuthenticationEveryXSeconds': 0, 'downloadSGACLListsEveryXSeconds': 0, 'otherSGADevicesToTrustThisDevice': True, 'sendConfigurationToDevice': True, 'sendConfigurationToDeviceUsing': 'string', 'coaSourceHost': 'string'}, 'deviceConfigurationDeployment': {'includeWhenDeployingSGTUpdates': True, 'enableModePassword': 'string', 'execModePassword': 'string', 'execModeUsername': 'string'}, 'pushIdSupport': True}
    )
    return endpoint_result


@pytest.mark.network_device
def test_update_network_device_by_id(api, validator):
    try:
        assert is_valid_update_network_device_by_id(
            validator,
            update_network_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_device_by_id_default(api):
    endpoint_result = api.network_device.update_network_device_by_id(
        active_validation=False,
        id='string',
        authentication_settings=None,
        coa_port=None,
        description=None,
        dtls_dns_name=None,
        model_name=None,
        name=None,
        network_device_group_list=None,
        network_device_iplist=None,
        payload=None,
        profile_name=None,
        snmpsettings=None,
        software_version=None,
        tacacs_settings=None,
        trustsecsettings=None
    )
    return endpoint_result


@pytest.mark.network_device
def test_update_network_device_by_id_default(api, validator):
    try:
        assert is_valid_update_network_device_by_id(
            validator,
            update_network_device_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_device_by_id(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_9f2fd3c6324b581ca0f3f9eadede1cdc_v3_1_0').validate(obj.response)
    return True


def delete_network_device_by_id(api):
    endpoint_result = api.network_device.delete_network_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_delete_network_device_by_id(api, validator):
    try:
        assert is_valid_delete_network_device_by_id(
            validator,
            delete_network_device_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_device_by_id_default(api):
    endpoint_result = api.network_device.delete_network_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_delete_network_device_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_device_by_id(
            validator,
            delete_network_device_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_48b986fa0f0d54ef98eb135eeb88808a_v3_1_0').validate(obj.response)
    return True


def get_network_device(api):
    endpoint_result = api.network_device.get_network_device(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_get_network_device(api, validator):
    try:
        assert is_valid_get_network_device(
            validator,
            get_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_device_default(api):
    endpoint_result = api.network_device.get_network_device(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.network_device
def test_get_network_device_default(api, validator):
    try:
        assert is_valid_get_network_device(
            validator,
            get_network_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_device(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_574ca6ab8ec556c3bc9531dc380b230a_v3_1_0').validate(obj.response)
    return True


def create_network_device(api):
    endpoint_result = api.network_device.create_network_device(
        active_validation=False,
        authentication_settings={'networkProtocol': 'string', 'secondRadiusSharedSecret': 'string', 'radiusSharedSecret': 'string', 'enableKeyWrap': True, 'enabled': True, 'dtlsRequired': True, 'enableMultiSecret': 'string', 'keyEncryptionKey': 'string', 'messageAuthenticatorCodeKey': 'string', 'keyInputFormat': 'string'},
        coa_port=0,
        description='string',
        dtls_dns_name='string',
        model_name='string',
        name='string',
        network_device_group_list=['string'],
        network_device_iplist=[{'ipaddress': 'string', 'mask': 0, 'getIpaddressExclude': 'string'}],
        payload=None,
        profile_name='string',
        snmpsettings={'version': 'string', 'roCommunity': 'string', 'pollingInterval': 0, 'linkTrapQuery': True, 'macTrapQuery': True, 'originatingPolicyServicesNode': 'string'},
        software_version='string',
        tacacs_settings={'sharedSecret': 'string', 'connectModeOptions': 'string'},
        trustsecsettings={'deviceAuthenticationSettings': {'sgaDeviceId': 'string', 'sgaDevicePassword': 'string'}, 'sgaNotificationAndUpdates': {'downlaodEnvironmentDataEveryXSeconds': 0, 'downlaodPeerAuthorizationPolicyEveryXSeconds': 0, 'reAuthenticationEveryXSeconds': 0, 'downloadSGACLListsEveryXSeconds': 0, 'otherSGADevicesToTrustThisDevice': True, 'sendConfigurationToDevice': True, 'sendConfigurationToDeviceUsing': 'string', 'coaSourceHost': 'string'}, 'deviceConfigurationDeployment': {'includeWhenDeployingSGTUpdates': True, 'enableModePassword': 'string', 'execModePassword': 'string', 'execModeUsername': 'string'}, 'pushIdSupport': True}
    )
    return endpoint_result


@pytest.mark.network_device
def test_create_network_device(api, validator):
    try:
        assert is_valid_create_network_device(
            validator,
            create_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_device_default(api):
    endpoint_result = api.network_device.create_network_device(
        active_validation=False,
        authentication_settings=None,
        coa_port=None,
        description=None,
        dtls_dns_name=None,
        model_name=None,
        name=None,
        network_device_group_list=None,
        network_device_iplist=None,
        payload=None,
        profile_name=None,
        snmpsettings=None,
        software_version=None,
        tacacs_settings=None,
        trustsecsettings=None
    )
    return endpoint_result


@pytest.mark.network_device
def test_create_network_device_default(api, validator):
    try:
        assert is_valid_create_network_device(
            validator,
            create_network_device_default(api)
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

    json_schema_validate('jsd_682601e571185718b6ef6e78bfbfdf68_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.network_device.get_version(

    )
    return endpoint_result


@pytest.mark.network_device
def test_get_version(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_version_default(api):
    endpoint_result = api.network_device.get_version(

    )
    return endpoint_result


@pytest.mark.network_device
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_network_device(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_63b2eebd5c245e58a503aa53115eec53_v3_1_0').validate(obj.response)
    return True


def bulk_request_for_network_device(api):
    endpoint_result = api.network_device.bulk_request_for_network_device(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_bulk_request_for_network_device(api, validator):
    try:
        assert is_valid_bulk_request_for_network_device(
            validator,
            bulk_request_for_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_request_for_network_device_default(api):
    endpoint_result = api.network_device.bulk_request_for_network_device(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.network_device
def test_bulk_request_for_network_device_default(api, validator):
    try:
        assert is_valid_bulk_request_for_network_device(
            validator,
            bulk_request_for_network_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_network_device(json_schema_validate, obj):
    if not obj:
        return False

    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')

    json_schema_validate('jsd_1bf96800cc265b5e9e1566ec7088619c_v3_1_0').validate(obj.response)
    return True


def monitor_bulk_status_network_device(api):
    endpoint_result = api.network_device.monitor_bulk_status_network_device(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_monitor_bulk_status_network_device(api, validator):
    try:
        assert is_valid_monitor_bulk_status_network_device(
            validator,
            monitor_bulk_status_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def monitor_bulk_status_network_device_default(api):
    endpoint_result = api.network_device.monitor_bulk_status_network_device(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.network_device
def test_monitor_bulk_status_network_device_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_network_device(
            validator,
            monitor_bulk_status_network_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
