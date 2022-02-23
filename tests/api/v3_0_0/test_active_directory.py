# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI active_directory API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_active_directory_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7c6be021c4ca59e48c97afe218219bb1_v3_0_0').validate(obj.response)
    return True


def get_active_directory_by_name(api):
    endpoint_result = api.active_directory.get_active_directory_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_active_directory_by_name(api, validator):
    try:
        assert is_valid_get_active_directory_by_name(
            validator,
            get_active_directory_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_directory_by_name_default(api):
    endpoint_result = api.active_directory.get_active_directory_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_active_directory_by_name_default(api, validator):
    try:
        assert is_valid_get_active_directory_by_name(
            validator,
            get_active_directory_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_user_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b839d4dee9b958e48ccef056603e253f_v3_0_0').validate(obj.response)
    return True


def get_user_groups(api):
    endpoint_result = api.active_directory.get_user_groups(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_user_groups(api, validator):
    try:
        assert is_valid_get_user_groups(
            validator,
            get_user_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_user_groups_default(api):
    endpoint_result = api.active_directory.get_user_groups(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_user_groups_default(api, validator):
    try:
        assert is_valid_get_user_groups(
            validator,
            get_user_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_load_groups_from_domain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_14104b05e80058df96e685baa727d578_v3_0_0').validate(obj.response)
    return True


def load_groups_from_domain(api):
    endpoint_result = api.active_directory.load_groups_from_domain(
        active_validation=False,
        ad_attributes={'attributes': [{'name': 'string', 'type': 'string', 'internalName': 'string', 'defaultValue': 'string'}]},
        ad_scopes_names='string',
        adgroups={'groups': [{'name': 'string', 'sid': 'string', 'type': 'string'}]},
        advanced_settings={'enablePassChange': True, 'enableMachineAuth': True, 'enableMachineAccess': True, 'agingTime': 0, 'enableDialinPermissionCheck': True, 'enableCallbackForDialinClient': True, 'plaintextAuth': True, 'enableFailedAuthProtection': True, 'authProtectionType': 'string', 'failedAuthThreshold': 0, 'identityNotInAdBehaviour': 'string', 'unreachableDomainsBehaviour': 'string', 'enableRewrites': True, 'rewriteRules': [{'rowId': 0, 'rewriteMatch': 'string', 'rewriteResult': 'string'}], 'firstName': 'string', 'department': 'string', 'lastName': 'string', 'organizationalUnit': 'string', 'jobTitle': 'string', 'locality': 'string', 'email': 'string', 'stateOrProvince': 'string', 'telephone': 'string', 'country': 'string', 'streetAddress': 'string', 'schema': 'string'},
        description='string',
        domain='string',
        enable_domain_white_list=True,
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_load_groups_from_domain(api, validator):
    try:
        assert is_valid_load_groups_from_domain(
            validator,
            load_groups_from_domain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def load_groups_from_domain_default(api):
    endpoint_result = api.active_directory.load_groups_from_domain(
        active_validation=False,
        id='string',
        ad_attributes=None,
        ad_scopes_names=None,
        adgroups=None,
        advanced_settings=None,
        description=None,
        domain=None,
        enable_domain_white_list=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_load_groups_from_domain_default(api, validator):
    try:
        assert is_valid_load_groups_from_domain(
            validator,
            load_groups_from_domain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_leave_domain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_8091e84541805d1da1fa3d4d581102a9_v3_0_0').validate(obj.response)
    return True


def leave_domain(api):
    endpoint_result = api.active_directory.leave_domain(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_leave_domain(api, validator):
    try:
        assert is_valid_leave_domain(
            validator,
            leave_domain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def leave_domain_default(api):
    endpoint_result = api.active_directory.leave_domain(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_leave_domain_default(api, validator):
    try:
        assert is_valid_leave_domain(
            validator,
            leave_domain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_is_user_member_of_groups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_eae60ece5110590e97ddd910e8144ed2_v3_0_0').validate(obj.response)
    return True


def is_user_member_of_groups(api):
    endpoint_result = api.active_directory.is_user_member_of_groups(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_is_user_member_of_groups(api, validator):
    try:
        assert is_valid_is_user_member_of_groups(
            validator,
            is_user_member_of_groups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def is_user_member_of_groups_default(api):
    endpoint_result = api.active_directory.is_user_member_of_groups(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_is_user_member_of_groups_default(api, validator):
    try:
        assert is_valid_is_user_member_of_groups(
            validator,
            is_user_member_of_groups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trusted_domains(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_7d0ed84901325292ad4e2a91a174f6b2_v3_0_0').validate(obj.response)
    return True


def get_trusted_domains(api):
    endpoint_result = api.active_directory.get_trusted_domains(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_trusted_domains(api, validator):
    try:
        assert is_valid_get_trusted_domains(
            validator,
            get_trusted_domains(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_trusted_domains_default(api):
    endpoint_result = api.active_directory.get_trusted_domains(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_trusted_domains_default(api, validator):
    try:
        assert is_valid_get_trusted_domains(
            validator,
            get_trusted_domains_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_join_domain_with_all_nodes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e84705b918955b53afe61fc37911eb8b_v3_0_0').validate(obj.response)
    return True


def join_domain_with_all_nodes(api):
    endpoint_result = api.active_directory.join_domain_with_all_nodes(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_join_domain_with_all_nodes(api, validator):
    try:
        assert is_valid_join_domain_with_all_nodes(
            validator,
            join_domain_with_all_nodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def join_domain_with_all_nodes_default(api):
    endpoint_result = api.active_directory.join_domain_with_all_nodes(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_join_domain_with_all_nodes_default(api, validator):
    try:
        assert is_valid_join_domain_with_all_nodes(
            validator,
            join_domain_with_all_nodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_leave_domain_with_all_nodes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d011417d18d055ccb864c1dc2ae0456d_v3_0_0').validate(obj.response)
    return True


def leave_domain_with_all_nodes(api):
    endpoint_result = api.active_directory.leave_domain_with_all_nodes(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_leave_domain_with_all_nodes(api, validator):
    try:
        assert is_valid_leave_domain_with_all_nodes(
            validator,
            leave_domain_with_all_nodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def leave_domain_with_all_nodes_default(api):
    endpoint_result = api.active_directory.leave_domain_with_all_nodes(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_leave_domain_with_all_nodes_default(api, validator):
    try:
        assert is_valid_leave_domain_with_all_nodes(
            validator,
            leave_domain_with_all_nodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_groups_by_domain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_48fd729f50e65695966359b589a1606b_v3_0_0').validate(obj.response)
    return True


def get_groups_by_domain(api):
    endpoint_result = api.active_directory.get_groups_by_domain(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_groups_by_domain(api, validator):
    try:
        assert is_valid_get_groups_by_domain(
            validator,
            get_groups_by_domain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_groups_by_domain_default(api):
    endpoint_result = api.active_directory.get_groups_by_domain(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_groups_by_domain_default(api, validator):
    try:
        assert is_valid_get_groups_by_domain(
            validator,
            get_groups_by_domain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_active_directory_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_15236cfcc7615d0492e2dd1b04dd03a9_v3_0_0').validate(obj.response)
    return True


def get_active_directory_by_id(api):
    endpoint_result = api.active_directory.get_active_directory_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_active_directory_by_id(api, validator):
    try:
        assert is_valid_get_active_directory_by_id(
            validator,
            get_active_directory_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_directory_by_id_default(api):
    endpoint_result = api.active_directory.get_active_directory_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_active_directory_by_id_default(api, validator):
    try:
        assert is_valid_get_active_directory_by_id(
            validator,
            get_active_directory_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_active_directory_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_786febbe79ed5bb780d97a98f292b606_v3_0_0').validate(obj.response)
    return True


def delete_active_directory_by_id(api):
    endpoint_result = api.active_directory.delete_active_directory_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.active_directory
def test_delete_active_directory_by_id(api, validator):
    try:
        assert is_valid_delete_active_directory_by_id(
            validator,
            delete_active_directory_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_active_directory_by_id_default(api):
    endpoint_result = api.active_directory.delete_active_directory_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.active_directory
def test_delete_active_directory_by_id_default(api, validator):
    try:
        assert is_valid_delete_active_directory_by_id(
            validator,
            delete_active_directory_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_join_domain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b3284240745e5b929c51495fe80bc1c4_v3_0_0').validate(obj.response)
    return True


def join_domain(api):
    endpoint_result = api.active_directory.join_domain(
        active_validation=False,
        additional_data=[{'value': 'string', 'name': 'string'}],
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_join_domain(api, validator):
    try:
        assert is_valid_join_domain(
            validator,
            join_domain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def join_domain_default(api):
    endpoint_result = api.active_directory.join_domain(
        active_validation=False,
        id='string',
        additional_data=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_join_domain_default(api, validator):
    try:
        assert is_valid_join_domain(
            validator,
            join_domain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_active_directory(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c8dbec9679d453f78cb47d894c507a7b_v3_0_0').validate(obj.response)
    return True


def get_active_directory(api):
    endpoint_result = api.active_directory.get_active_directory(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_active_directory(api, validator):
    try:
        assert is_valid_get_active_directory(
            validator,
            get_active_directory(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_active_directory_default(api):
    endpoint_result = api.active_directory.get_active_directory(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_active_directory_default(api, validator):
    try:
        assert is_valid_get_active_directory(
            validator,
            get_active_directory_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_active_directory(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_64e9318040a456978757d7abfa3e66b1_v3_0_0').validate(obj.response)
    return True


def create_active_directory(api):
    endpoint_result = api.active_directory.create_active_directory(
        active_validation=False,
        ad_attributes={'attributes': [{'name': 'string', 'type': 'string', 'internalName': 'string', 'defaultValue': 'string'}]},
        ad_scopes_names='string',
        adgroups={'groups': [{'name': 'string', 'sid': 'string', 'type': 'string'}]},
        advanced_settings={'enablePassChange': True, 'enableMachineAuth': True, 'enableMachineAccess': True, 'agingTime': 0, 'enableDialinPermissionCheck': True, 'enableCallbackForDialinClient': True, 'plaintextAuth': True, 'enableFailedAuthProtection': True, 'authProtectionType': 'string', 'failedAuthThreshold': 0, 'identityNotInAdBehaviour': 'string', 'unreachableDomainsBehaviour': 'string', 'enableRewrites': True, 'rewriteRules': [{'rowId': 0, 'rewriteMatch': 'string', 'rewriteResult': 'string'}], 'firstName': 'string', 'department': 'string', 'lastName': 'string', 'organizationalUnit': 'string', 'jobTitle': 'string', 'locality': 'string', 'email': 'string', 'stateOrProvince': 'string', 'telephone': 'string', 'country': 'string', 'streetAddress': 'string', 'schema': 'string'},
        description='string',
        domain='string',
        enable_domain_white_list=True,
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_create_active_directory(api, validator):
    try:
        assert is_valid_create_active_directory(
            validator,
            create_active_directory(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_active_directory_default(api):
    endpoint_result = api.active_directory.create_active_directory(
        active_validation=False,
        ad_attributes=None,
        ad_scopes_names=None,
        adgroups=None,
        advanced_settings=None,
        description=None,
        domain=None,
        enable_domain_white_list=None,
        id=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.active_directory
def test_create_active_directory_default(api, validator):
    try:
        assert is_valid_create_active_directory(
            validator,
            create_active_directory_default(api)
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
    json_schema_validate('jsd_c2d0923990e35be1882e4dee000254a9_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.active_directory.get_version(

    )
    return endpoint_result


@pytest.mark.active_directory
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
    endpoint_result = api.active_directory.get_version(

    )
    return endpoint_result


@pytest.mark.active_directory
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
