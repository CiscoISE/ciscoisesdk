# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI allowed_protocols API fixtures and tests.

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


def is_valid_get_allowed_protocol_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_010ac8c8cb9b5007a1e1a6434a20a881_v3_0_0').validate(obj.response)
    return True


def get_allowed_protocol_by_name(api):
    endpoint_result = api.allowed_protocols.get_allowed_protocol_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_get_allowed_protocol_by_name(api, validator):
    try:
        assert is_valid_get_allowed_protocol_by_name(
            validator,
            get_allowed_protocol_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_allowed_protocol_by_name_default(api):
    endpoint_result = api.allowed_protocols.get_allowed_protocol_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_get_allowed_protocol_by_name_default(api, validator):
    try:
        assert is_valid_get_allowed_protocol_by_name(
            validator,
            get_allowed_protocol_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_allowed_protocol_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_696e3ddfddd45e299f14ed194926f8de_v3_0_0').validate(obj.response)
    return True


def get_allowed_protocol_by_id(api):
    endpoint_result = api.allowed_protocols.get_allowed_protocol_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_get_allowed_protocol_by_id(api, validator):
    try:
        assert is_valid_get_allowed_protocol_by_id(
            validator,
            get_allowed_protocol_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_allowed_protocol_by_id_default(api):
    endpoint_result = api.allowed_protocols.get_allowed_protocol_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_get_allowed_protocol_by_id_default(api, validator):
    try:
        assert is_valid_get_allowed_protocol_by_id(
            validator,
            get_allowed_protocol_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_allowed_protocol_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_61a0b312f70257b1bfa90d0260f0c971_v3_0_0').validate(obj.response)
    return True


def update_allowed_protocol_by_id(api):
    endpoint_result = api.allowed_protocols.update_allowed_protocol_by_id(
        active_validation=False,
        allow_chap=True,
        allow_eap_fast=True,
        allow_eap_md5=True,
        allow_eap_tls=True,
        allow_eap_ttls=True,
        allow_leap=True,
        allow_ms_chap_v1=True,
        allow_ms_chap_v2=True,
        allow_pap_ascii=True,
        allow_peap=True,
        allow_preferred_eap_protocol=True,
        allow_teap=True,
        allow_weak_ciphers_for_eap=True,
        description='string',
        eap_fast={'allowEapFastEapMsChapV2': True, 'allowEapFastEapMsChapV2PwdChange': True, 'allowEapFastEapMsChapV2PwdChangeRetries': 0, 'allowEapFastEapGtc': True, 'allowEapFastEapGtcPwdChange': True, 'allowEapFastEapGtcPwdChangeRetries': 0, 'allowEapFastEapTls': True, 'allowEapFastEapTlsAuthOfExpiredCerts': True, 'eapFastUsePacs': True, 'eapFastUsePacsTunnelPacTtl': 0, 'eapFastUsePacsTunnelPacTtlUnits': 'string', 'eapFastUsePacsUseProactivePacUpdatePrecentage': 0, 'eapFastUsePacsAllowAnonymProvisioning': True, 'eapFastUsePacsAllowAuthenProvisioning': True, 'eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning': True, 'eapFastUsePacsAcceptClientCert': True, 'eapFastUsePacsMachinePacTtl': 0, 'eapFastUsePacsMachinePacTtlUnits': 'string', 'eapFastUsePacsAllowMachineAuthentication': True, 'eapFastUsePacsStatelessSessionResume': True, 'eapFastUsePacsAuthorizationPacTtl': 0, 'eapFastUsePacsAuthorizationPacTtlUnits': 'string', 'eapFastDontUsePacsAcceptClientCert': True, 'eapFastDontUsePacsAllowMachineAuthentication': True, 'eapFastEnableEAPChaining': True},
        eap_tls={'allowEapTlsAuthOfExpiredCerts': True, 'eapTlsEnableStatelessSessionResume': True, 'eapTlsSessionTicketTtl': 0, 'eapTlsSessionTicketTtlUnits': 'string', 'eapTlsSessionTicketPrecentage': 0},
        eap_tls_l_bit=True,
        eap_ttls={'eapTtlsPapAscii': True, 'eapTtlsChap': True, 'eapTtlsMsChapV1': True, 'eapTtlsMsChapV2': True, 'eapTtlsEapMd5': True, 'eapTtlsEapMsChapV2': True, 'eapTtlsEapMsChapV2PwdChange': True, 'eapTtlsEapMsChapV2PwdChangeRetries': 0},
        id='string',
        name='string',
        payload=None,
        peap={'allowPeapEapMsChapV2': True, 'allowPeapEapMsChapV2PwdChange': True, 'allowPeapEapMsChapV2PwdChangeRetries': 0, 'allowPeapEapGtc': True, 'allowPeapEapGtcPwdChange': True, 'allowPeapEapGtcPwdChangeRetries': 0, 'allowPeapEapTls': True, 'allowPeapEapTlsAuthOfExpiredCerts': True, 'requireCryptobinding': True, 'allowPeapV0': True},
        preferred_eap_protocol='string',
        process_host_lookup=True,
        require_message_auth=True,
        teap={'allowTeapEapMsChapV2': True, 'allowTeapEapMsChapV2PwdChange': True, 'allowTeapEapMsChapV2PwdChangeRetries': 0, 'allowTeapEapTls': True, 'allowTeapEapTlsAuthOfExpiredCerts': True, 'acceptClientCertDuringTunnelEst': True, 'enableEapChaining': True, 'allowDowngradeMsk': True}
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_update_allowed_protocol_by_id(api, validator):
    try:
        assert is_valid_update_allowed_protocol_by_id(
            validator,
            update_allowed_protocol_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_allowed_protocol_by_id_default(api):
    endpoint_result = api.allowed_protocols.update_allowed_protocol_by_id(
        active_validation=False,
        id='string',
        allow_chap=None,
        allow_eap_fast=None,
        allow_eap_md5=None,
        allow_eap_tls=None,
        allow_eap_ttls=None,
        allow_leap=None,
        allow_ms_chap_v1=None,
        allow_ms_chap_v2=None,
        allow_pap_ascii=None,
        allow_peap=None,
        allow_preferred_eap_protocol=None,
        allow_teap=None,
        allow_weak_ciphers_for_eap=None,
        description=None,
        eap_fast=None,
        eap_tls=None,
        eap_tls_l_bit=None,
        eap_ttls=None,
        name=None,
        payload=None,
        peap=None,
        preferred_eap_protocol=None,
        process_host_lookup=None,
        require_message_auth=None,
        teap=None
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_update_allowed_protocol_by_id_default(api, validator):
    try:
        assert is_valid_update_allowed_protocol_by_id(
            validator,
            update_allowed_protocol_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_allowed_protocol_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a6cbd2c420785cfcbdecc3495bca8af4_v3_0_0').validate(obj.response)
    return True


def delete_allowed_protocol_by_id(api):
    endpoint_result = api.allowed_protocols.delete_allowed_protocol_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_delete_allowed_protocol_by_id(api, validator):
    try:
        assert is_valid_delete_allowed_protocol_by_id(
            validator,
            delete_allowed_protocol_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_allowed_protocol_by_id_default(api):
    endpoint_result = api.allowed_protocols.delete_allowed_protocol_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_delete_allowed_protocol_by_id_default(api, validator):
    try:
        assert is_valid_delete_allowed_protocol_by_id(
            validator,
            delete_allowed_protocol_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_allowed_protocols(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d82fe0f9e4635b74af809beaaf98bd07_v3_0_0').validate(obj.response)
    return True


def get_allowed_protocols(api):
    endpoint_result = api.allowed_protocols.get_allowed_protocols(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_get_allowed_protocols(api, validator):
    try:
        assert is_valid_get_allowed_protocols(
            validator,
            get_allowed_protocols(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_allowed_protocols_default(api):
    endpoint_result = api.allowed_protocols.get_allowed_protocols(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_get_allowed_protocols_default(api, validator):
    try:
        assert is_valid_get_allowed_protocols(
            validator,
            get_allowed_protocols_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_allowed_protocol(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1b40ad23ab0a5a7b8adade320c8912e7_v3_0_0').validate(obj.response)
    return True


def create_allowed_protocol(api):
    endpoint_result = api.allowed_protocols.create_allowed_protocol(
        active_validation=False,
        allow_chap=True,
        allow_eap_fast=True,
        allow_eap_md5=True,
        allow_eap_tls=True,
        allow_eap_ttls=True,
        allow_leap=True,
        allow_ms_chap_v1=True,
        allow_ms_chap_v2=True,
        allow_pap_ascii=True,
        allow_peap=True,
        allow_preferred_eap_protocol=True,
        allow_teap=True,
        allow_weak_ciphers_for_eap=True,
        description='string',
        eap_fast={'allowEapFastEapMsChapV2': True, 'allowEapFastEapMsChapV2PwdChange': True, 'allowEapFastEapMsChapV2PwdChangeRetries': 0, 'allowEapFastEapGtc': True, 'allowEapFastEapGtcPwdChange': True, 'allowEapFastEapGtcPwdChangeRetries': 0, 'allowEapFastEapTls': True, 'allowEapFastEapTlsAuthOfExpiredCerts': True, 'eapFastUsePacs': True, 'eapFastUsePacsTunnelPacTtl': 0, 'eapFastUsePacsTunnelPacTtlUnits': 'string', 'eapFastUsePacsUseProactivePacUpdatePrecentage': 0, 'eapFastUsePacsAllowAnonymProvisioning': True, 'eapFastUsePacsAllowAuthenProvisioning': True, 'eapFastUsePacsReturnAccessAcceptAfterAuthenticatedProvisioning': True, 'eapFastUsePacsAcceptClientCert': True, 'eapFastUsePacsMachinePacTtl': 0, 'eapFastUsePacsMachinePacTtlUnits': 'string', 'eapFastUsePacsAllowMachineAuthentication': True, 'eapFastUsePacsStatelessSessionResume': True, 'eapFastUsePacsAuthorizationPacTtl': 0, 'eapFastUsePacsAuthorizationPacTtlUnits': 'string', 'eapFastDontUsePacsAcceptClientCert': True, 'eapFastDontUsePacsAllowMachineAuthentication': True, 'eapFastEnableEAPChaining': True},
        eap_tls={'allowEapTlsAuthOfExpiredCerts': True, 'eapTlsEnableStatelessSessionResume': True, 'eapTlsSessionTicketTtl': 0, 'eapTlsSessionTicketTtlUnits': 'string', 'eapTlsSessionTicketPrecentage': 0},
        eap_tls_l_bit=True,
        eap_ttls={'eapTtlsPapAscii': True, 'eapTtlsChap': True, 'eapTtlsMsChapV1': True, 'eapTtlsMsChapV2': True, 'eapTtlsEapMd5': True, 'eapTtlsEapMsChapV2': True, 'eapTtlsEapMsChapV2PwdChange': True, 'eapTtlsEapMsChapV2PwdChangeRetries': 0},
        name='string',
        payload=None,
        peap={'allowPeapEapMsChapV2': True, 'allowPeapEapMsChapV2PwdChange': True, 'allowPeapEapMsChapV2PwdChangeRetries': 0, 'allowPeapEapGtc': True, 'allowPeapEapGtcPwdChange': True, 'allowPeapEapGtcPwdChangeRetries': 0, 'allowPeapEapTls': True, 'allowPeapEapTlsAuthOfExpiredCerts': True, 'requireCryptobinding': True, 'allowPeapV0': True},
        preferred_eap_protocol='string',
        process_host_lookup=True,
        require_message_auth=True,
        teap={'allowTeapEapMsChapV2': True, 'allowTeapEapMsChapV2PwdChange': True, 'allowTeapEapMsChapV2PwdChangeRetries': 0, 'allowTeapEapTls': True, 'allowTeapEapTlsAuthOfExpiredCerts': True, 'acceptClientCertDuringTunnelEst': True, 'enableEapChaining': True, 'allowDowngradeMsk': True}
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_create_allowed_protocol(api, validator):
    try:
        assert is_valid_create_allowed_protocol(
            validator,
            create_allowed_protocol(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_allowed_protocol_default(api):
    endpoint_result = api.allowed_protocols.create_allowed_protocol(
        active_validation=False,
        allow_chap=None,
        allow_eap_fast=None,
        allow_eap_md5=None,
        allow_eap_tls=None,
        allow_eap_ttls=None,
        allow_leap=None,
        allow_ms_chap_v1=None,
        allow_ms_chap_v2=None,
        allow_pap_ascii=None,
        allow_peap=None,
        allow_preferred_eap_protocol=None,
        allow_teap=None,
        allow_weak_ciphers_for_eap=None,
        description=None,
        eap_fast=None,
        eap_tls=None,
        eap_tls_l_bit=None,
        eap_ttls=None,
        name=None,
        payload=None,
        peap=None,
        preferred_eap_protocol=None,
        process_host_lookup=None,
        require_message_auth=None,
        teap=None
    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_create_allowed_protocol_default(api, validator):
    try:
        assert is_valid_create_allowed_protocol(
            validator,
            create_allowed_protocol_default(api)
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
    json_schema_validate('jsd_c0f61393474f5744ab0a263a232d3b96_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.allowed_protocols.get_version(

    )
    return endpoint_result


@pytest.mark.allowed_protocols
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
    endpoint_result = api.allowed_protocols.get_version(

    )
    return endpoint_result


@pytest.mark.allowed_protocols
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
