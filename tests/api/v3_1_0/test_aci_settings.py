# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI aci_settings API fixtures and tests.

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


def is_valid_get_aci_settings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2ea5c865993b56f48f7f43475294a20c_v3_1_0').validate(obj.response)
    return True


def get_aci_settings(api):
    endpoint_result = api.aci_settings.get_aci_settings(

    )
    return endpoint_result


@pytest.mark.aci_settings
def test_get_aci_settings(api, validator):
    try:
        assert is_valid_get_aci_settings(
            validator,
            get_aci_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_aci_settings_default(api):
    endpoint_result = api.aci_settings.get_aci_settings(

    )
    return endpoint_result


@pytest.mark.aci_settings
def test_get_aci_settings_default(api, validator):
    try:
        assert is_valid_get_aci_settings(
            validator,
            get_aci_settings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_test_aci_connectivity(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1b155c91eec153338302d492db1afb80_v3_1_0').validate(obj.response)
    return True


def test_aci_connectivity(api):
    endpoint_result = api.aci_settings.test_aci_connectivity(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.aci_settings
def test_test_aci_connectivity(api, validator):
    try:
        assert is_valid_test_aci_connectivity(
            validator,
            test_aci_connectivity(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def test_aci_connectivity_default(api):
    endpoint_result = api.aci_settings.test_aci_connectivity(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.aci_settings
def test_test_aci_connectivity_default(api, validator):
    try:
        assert is_valid_test_aci_connectivity(
            validator,
            test_aci_connectivity_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_aci_settings_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_56cea2e785ee57908a9ee3b118e49cfa_v3_1_0').validate(obj.response)
    return True


def update_aci_settings_by_id(api):
    endpoint_result = api.aci_settings.update_aci_settings_by_id(
        aci50=True,
        aci51=True,
        aciipaddress='string',
        acipassword='string',
        aciuser_name='string',
        active_validation=False,
        admin_name='string',
        admin_password='string',
        all_sxp_domain=True,
        default_sgt_name='string',
        enable_aci=True,
        enable_data_plane=True,
        enable_elements_limit=True,
        id='string',
        ip_address_host_name='string',
        l3_route_network='string',
        max_num_iepg_from_aci=0,
        max_num_sgt_to_aci=0,
        payload=None,
        specific_sxp_domain=True,
        specifix_sxp_domain_list=['string'],
        suffix_to_epg='string',
        suffix_to_sgt='string',
        tenant_name='string',
        untagged_packet_iepg_name='string'
    )
    return endpoint_result


@pytest.mark.aci_settings
def test_update_aci_settings_by_id(api, validator):
    try:
        assert is_valid_update_aci_settings_by_id(
            validator,
            update_aci_settings_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_aci_settings_by_id_default(api):
    endpoint_result = api.aci_settings.update_aci_settings_by_id(
        active_validation=False,
        id='string',
        aci50=None,
        aci51=None,
        aciipaddress=None,
        acipassword=None,
        aciuser_name=None,
        admin_name=None,
        admin_password=None,
        all_sxp_domain=None,
        default_sgt_name=None,
        enable_aci=None,
        enable_data_plane=None,
        enable_elements_limit=None,
        ip_address_host_name=None,
        l3_route_network=None,
        max_num_iepg_from_aci=None,
        max_num_sgt_to_aci=None,
        payload=None,
        specific_sxp_domain=None,
        specifix_sxp_domain_list=None,
        suffix_to_epg=None,
        suffix_to_sgt=None,
        tenant_name=None,
        untagged_packet_iepg_name=None
    )
    return endpoint_result


@pytest.mark.aci_settings
def test_update_aci_settings_by_id_default(api, validator):
    try:
        assert is_valid_update_aci_settings_by_id(
            validator,
            update_aci_settings_by_id_default(api)
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
    json_schema_validate('jsd_462410ea47f65521bcf0ab949b5d72b5_v3_1_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.aci_settings.get_version(

    )
    return endpoint_result


@pytest.mark.aci_settings
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
    endpoint_result = api.aci_settings.get_version(

    )
    return endpoint_result


@pytest.mark.aci_settings
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
