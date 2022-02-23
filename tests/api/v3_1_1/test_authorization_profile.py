# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI authorization_profile API fixtures and tests.

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


def is_valid_get_authorization_profile_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_acf0372068885036baee3c4524638f31_v3_1_1').validate(obj.response)
    return True


def get_authorization_profile_by_name(api):
    endpoint_result = api.authorization_profile.get_authorization_profile_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_get_authorization_profile_by_name(api, validator):
    try:
        assert is_valid_get_authorization_profile_by_name(
            validator,
            get_authorization_profile_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_authorization_profile_by_name_default(api):
    endpoint_result = api.authorization_profile.get_authorization_profile_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_get_authorization_profile_by_name_default(api, validator):
    try:
        assert is_valid_get_authorization_profile_by_name(
            validator,
            get_authorization_profile_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_authorization_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_a69c7f1ad54e5e9cae1f871e19eed61b_v3_1_1').validate(obj.response)
    return True


def get_authorization_profile_by_id(api):
    endpoint_result = api.authorization_profile.get_authorization_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_get_authorization_profile_by_id(api, validator):
    try:
        assert is_valid_get_authorization_profile_by_id(
            validator,
            get_authorization_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_authorization_profile_by_id_default(api):
    endpoint_result = api.authorization_profile.get_authorization_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_get_authorization_profile_by_id_default(api, validator):
    try:
        assert is_valid_get_authorization_profile_by_id(
            validator,
            get_authorization_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_authorization_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9cb9f26e93655e7d89995b172f6fd97f_v3_1_1').validate(obj.response)
    return True


def update_authorization_profile_by_id(api):
    endpoint_result = api.authorization_profile.update_authorization_profile_by_id(
        access_type='string',
        acl='string',
        active_validation=False,
        advanced_attributes=[{'leftHandSideDictionaryAttribue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}, 'rightHandSideAttribueValue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}}],
        agentless_posture=True,
        airespace_acl='string',
        airespace_ipv6_acl='string',
        asa_vpn='string',
        authz_profile_type='string',
        auto_smart_port='string',
        avc_profile='string',
        dacl_name='string',
        description='string',
        easywired_session_candidate=True,
        id='string',
        interface_template='string',
        ipv6_acl_filter='string',
        ipv6_dacl_name='string',
        mac_sec_policy='string',
        name='string',
        neat=True,
        payload=None,
        profile_name='string',
        reauth={'timer': 0, 'connectivity': 'string'},
        service_template=True,
        track_movement=True,
        vlan={'nameID': 'string', 'tagID': 0},
        voice_domain_permission=True,
        web_auth=True,
        web_redirection={'WebRedirectionType': 'string', 'acl': 'string', 'portalName': 'string', 'staticIPHostNameFQDN': 'string', 'displayCertificatesRenewalMessages': True}
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_update_authorization_profile_by_id(api, validator):
    try:
        assert is_valid_update_authorization_profile_by_id(
            validator,
            update_authorization_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_authorization_profile_by_id_default(api):
    endpoint_result = api.authorization_profile.update_authorization_profile_by_id(
        active_validation=False,
        id='string',
        access_type=None,
        acl=None,
        advanced_attributes=None,
        agentless_posture=None,
        airespace_acl=None,
        airespace_ipv6_acl=None,
        asa_vpn=None,
        authz_profile_type=None,
        auto_smart_port=None,
        avc_profile=None,
        dacl_name=None,
        description=None,
        easywired_session_candidate=None,
        interface_template=None,
        ipv6_acl_filter=None,
        ipv6_dacl_name=None,
        mac_sec_policy=None,
        name=None,
        neat=None,
        payload=None,
        profile_name=None,
        reauth=None,
        service_template=None,
        track_movement=None,
        vlan=None,
        voice_domain_permission=None,
        web_auth=None,
        web_redirection=None
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_update_authorization_profile_by_id_default(api, validator):
    try:
        assert is_valid_update_authorization_profile_by_id(
            validator,
            update_authorization_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_authorization_profile_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c3913dfbda305f678ede16f782762ad3_v3_1_1').validate(obj.response)
    return True


def delete_authorization_profile_by_id(api):
    endpoint_result = api.authorization_profile.delete_authorization_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_delete_authorization_profile_by_id(api, validator):
    try:
        assert is_valid_delete_authorization_profile_by_id(
            validator,
            delete_authorization_profile_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_authorization_profile_by_id_default(api):
    endpoint_result = api.authorization_profile.delete_authorization_profile_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_delete_authorization_profile_by_id_default(api, validator):
    try:
        assert is_valid_delete_authorization_profile_by_id(
            validator,
            delete_authorization_profile_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_authorization_profiles(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2e232c5666ab5ed783588f413c3bc644_v3_1_1').validate(obj.response)
    return True


def get_authorization_profiles(api):
    endpoint_result = api.authorization_profile.get_authorization_profiles(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_get_authorization_profiles(api, validator):
    try:
        assert is_valid_get_authorization_profiles(
            validator,
            get_authorization_profiles(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_authorization_profiles_default(api):
    endpoint_result = api.authorization_profile.get_authorization_profiles(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_get_authorization_profiles_default(api, validator):
    try:
        assert is_valid_get_authorization_profiles(
            validator,
            get_authorization_profiles_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_authorization_profile(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9c43118f80d4556a8ec759a8c41e2097_v3_1_1').validate(obj.response)
    return True


def create_authorization_profile(api):
    endpoint_result = api.authorization_profile.create_authorization_profile(
        access_type='string',
        acl='string',
        active_validation=False,
        advanced_attributes=[{'leftHandSideDictionaryAttribue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}, 'rightHandSideAttribueValue': {'AdvancedAttributeValueType': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'value': 'string'}}],
        agentless_posture=True,
        airespace_acl='string',
        airespace_ipv6_acl='string',
        asa_vpn='string',
        authz_profile_type='string',
        auto_smart_port='string',
        avc_profile='string',
        dacl_name='string',
        description='string',
        easywired_session_candidate=True,
        id='string',
        interface_template='string',
        ipv6_acl_filter='string',
        ipv6_dacl_name='string',
        mac_sec_policy='string',
        name='string',
        neat=True,
        payload=None,
        profile_name='string',
        reauth={'timer': 0, 'connectivity': 'string'},
        service_template=True,
        track_movement=True,
        vlan={'nameID': 'string', 'tagID': 0},
        voice_domain_permission=True,
        web_auth=True,
        web_redirection={'WebRedirectionType': 'string', 'acl': 'string', 'portalName': 'string', 'staticIPHostNameFQDN': 'string', 'displayCertificatesRenewalMessages': True}
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_create_authorization_profile(api, validator):
    try:
        assert is_valid_create_authorization_profile(
            validator,
            create_authorization_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_authorization_profile_default(api):
    endpoint_result = api.authorization_profile.create_authorization_profile(
        active_validation=False,
        access_type=None,
        acl=None,
        advanced_attributes=None,
        agentless_posture=None,
        airespace_acl=None,
        airespace_ipv6_acl=None,
        asa_vpn=None,
        authz_profile_type=None,
        auto_smart_port=None,
        avc_profile=None,
        dacl_name=None,
        description=None,
        easywired_session_candidate=None,
        id=None,
        interface_template=None,
        ipv6_acl_filter=None,
        ipv6_dacl_name=None,
        mac_sec_policy=None,
        name=None,
        neat=None,
        payload=None,
        profile_name=None,
        reauth=None,
        service_template=None,
        track_movement=None,
        vlan=None,
        voice_domain_permission=None,
        web_auth=None,
        web_redirection=None
    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_create_authorization_profile_default(api, validator):
    try:
        assert is_valid_create_authorization_profile(
            validator,
            create_authorization_profile_default(api)
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
    json_schema_validate('jsd_3bee8aa3a03a57a3a5eb1418fe1250b6_v3_1_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.authorization_profile.get_version(

    )
    return endpoint_result


@pytest.mark.authorization_profile
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
    endpoint_result = api.authorization_profile.get_version(

    )
    return endpoint_result


@pytest.mark.authorization_profile
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
