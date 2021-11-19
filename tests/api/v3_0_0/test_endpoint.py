# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI endpoint API fixtures and tests.

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


def is_valid_release_rejected_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_258969f4f97557daacb3dadaced526cc_v3_0_0').validate(obj.response)
    return True


def release_rejected_endpoint(api):
    endpoint_result = api.endpoint.release_rejected_endpoint(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_release_rejected_endpoint(api, validator):
    try:
        assert is_valid_release_rejected_endpoint(
            validator,
            release_rejected_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def release_rejected_endpoint_default(api):
    endpoint_result = api.endpoint.release_rejected_endpoint(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_release_rejected_endpoint_default(api, validator):
    try:
        assert is_valid_release_rejected_endpoint(
            validator,
            release_rejected_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deregister_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_ed121b2686e85bd5b28c068c3c0de220_v3_0_0').validate(obj.response)
    return True


def deregister_endpoint(api):
    endpoint_result = api.endpoint.deregister_endpoint(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_deregister_endpoint(api, validator):
    try:
        assert is_valid_deregister_endpoint(
            validator,
            deregister_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def deregister_endpoint_default(api):
    endpoint_result = api.endpoint.deregister_endpoint(
        active_validation=False,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_deregister_endpoint_default(api, validator):
    try:
        assert is_valid_deregister_endpoint(
            validator,
            deregister_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_rejected_endpoints(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f8a2f0834e625822bed1cb4cf34fde5e_v3_0_0').validate(obj.response)
    return True


def get_rejected_endpoints(api):
    endpoint_result = api.endpoint.get_rejected_endpoints(

    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_rejected_endpoints(api, validator):
    try:
        assert is_valid_get_rejected_endpoints(
            validator,
            get_rejected_endpoints(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_rejected_endpoints_default(api):
    endpoint_result = api.endpoint.get_rejected_endpoints(

    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_rejected_endpoints_default(api, validator):
    try:
        assert is_valid_get_rejected_endpoints(
            validator,
            get_rejected_endpoints_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoint_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7d53842e83f0538cab91e097aa6800ce_v3_0_0').validate(obj.response)
    return True


def get_endpoint_by_name(api):
    endpoint_result = api.endpoint.get_endpoint_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_endpoint_by_name(api, validator):
    try:
        assert is_valid_get_endpoint_by_name(
            validator,
            get_endpoint_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_endpoint_by_name_default(api):
    endpoint_result = api.endpoint.get_endpoint_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_endpoint_by_name_default(api, validator):
    try:
        assert is_valid_get_endpoint_by_name(
            validator,
            get_endpoint_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoint_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_eb8e0ce63376573995a49178435f7747_v3_0_0').validate(obj.response)
    return True


def get_endpoint_by_id(api):
    endpoint_result = api.endpoint.get_endpoint_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_endpoint_by_id(api, validator):
    try:
        assert is_valid_get_endpoint_by_id(
            validator,
            get_endpoint_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_endpoint_by_id_default(api):
    endpoint_result = api.endpoint.get_endpoint_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_endpoint_by_id_default(api, validator):
    try:
        assert is_valid_get_endpoint_by_id(
            validator,
            get_endpoint_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_endpoint_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c8b30af4b84b5a90be2fc152cf26ad42_v3_0_0').validate(obj.response)
    return True


def update_endpoint_by_id(api):
    endpoint_result = api.endpoint.update_endpoint_by_id(
        active_validation=False,
        custom_attributes={'customAttributes': {}},
        description='string',
        group_id='string',
        id='string',
        identity_store='string',
        identity_store_id='string',
        mac='string',
        mdm_attributes={'mdmServerName': 'string', 'mdmReachable': True, 'mdmEnrolled': True, 'mdmComplianceStatus': True, 'mdmOS': 'string', 'mdmManufacturer': 'string', 'mdmModel': 'string', 'mdmSerial': 'string', 'mdmEncrypted': True, 'mdmPinlock': True, 'mdmJailBroken': True, 'mdmIMEI': 'string', 'mdmPhoneNumber': 'string'},
        name='string',
        payload=None,
        portal_user='string',
        profile_id='string',
        static_group_assignment=True,
        static_profile_assignment=True
    )
    return endpoint_result


@pytest.mark.endpoint
def test_update_endpoint_by_id(api, validator):
    try:
        assert is_valid_update_endpoint_by_id(
            validator,
            update_endpoint_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_endpoint_by_id_default(api):
    endpoint_result = api.endpoint.update_endpoint_by_id(
        active_validation=False,
        id='string',
        custom_attributes=None,
        description=None,
        group_id=None,
        identity_store=None,
        identity_store_id=None,
        mac=None,
        mdm_attributes=None,
        name=None,
        payload=None,
        portal_user=None,
        profile_id=None,
        static_group_assignment=None,
        static_profile_assignment=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_update_endpoint_by_id_default(api, validator):
    try:
        assert is_valid_update_endpoint_by_id(
            validator,
            update_endpoint_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_endpoint_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_36658f1cac5f578ab6509196266ad8e3_v3_0_0').validate(obj.response)
    return True


def delete_endpoint_by_id(api):
    endpoint_result = api.endpoint.delete_endpoint_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_delete_endpoint_by_id(api, validator):
    try:
        assert is_valid_delete_endpoint_by_id(
            validator,
            delete_endpoint_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_endpoint_by_id_default(api):
    endpoint_result = api.endpoint.delete_endpoint_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_delete_endpoint_by_id_default(api, validator):
    try:
        assert is_valid_delete_endpoint_by_id(
            validator,
            delete_endpoint_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_register_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_dfaeea899c185169ae2a3b70b5491008_v3_0_0').validate(obj.response)
    return True


def register_endpoint(api):
    endpoint_result = api.endpoint.register_endpoint(
        active_validation=False,
        custom_attributes={'customAttributes': {}},
        description='string',
        group_id='string',
        id='string',
        identity_store='string',
        identity_store_id='string',
        mac='string',
        mdm_attributes={'mdmServerName': 'string', 'mdmReachable': True, 'mdmEnrolled': True, 'mdmComplianceStatus': True, 'mdmOS': 'string', 'mdmManufacturer': 'string', 'mdmModel': 'string', 'mdmSerial': 'string', 'mdmEncrypted': True, 'mdmPinlock': True, 'mdmJailBroken': True, 'mdmIMEI': 'string', 'mdmPhoneNumber': 'string'},
        name='string',
        payload=None,
        portal_user='string',
        profile_id='string',
        static_group_assignment=True,
        static_profile_assignment=True
    )
    return endpoint_result


@pytest.mark.endpoint
def test_register_endpoint(api, validator):
    try:
        assert is_valid_register_endpoint(
            validator,
            register_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def register_endpoint_default(api):
    endpoint_result = api.endpoint.register_endpoint(
        active_validation=False,
        custom_attributes=None,
        description=None,
        group_id=None,
        id=None,
        identity_store=None,
        identity_store_id=None,
        mac=None,
        mdm_attributes=None,
        name=None,
        payload=None,
        portal_user=None,
        profile_id=None,
        static_group_assignment=None,
        static_profile_assignment=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_register_endpoint_default(api, validator):
    try:
        assert is_valid_register_endpoint(
            validator,
            register_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_endpoints(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_719765b7f7285d71be4645db91b0fc74_v3_0_0').validate(obj.response)
    return True


def get_endpoints(api):
    endpoint_result = api.endpoint.get_endpoints(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_endpoints(api, validator):
    try:
        assert is_valid_get_endpoints(
            validator,
            get_endpoints(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_endpoints_default(api):
    endpoint_result = api.endpoint.get_endpoints(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_endpoints_default(api, validator):
    try:
        assert is_valid_get_endpoints(
            validator,
            get_endpoints_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_845787ab88be5092bf4ba9f522e8e26f_v3_0_0').validate(obj.response)
    return True


def create_endpoint(api):
    endpoint_result = api.endpoint.create_endpoint(
        active_validation=False,
        custom_attributes={'customAttributes': {}},
        description='string',
        group_id='string',
        identity_store='string',
        identity_store_id='string',
        mac='string',
        mdm_attributes={'mdmServerName': 'string', 'mdmReachable': True, 'mdmEnrolled': True, 'mdmComplianceStatus': True, 'mdmOS': 'string', 'mdmManufacturer': 'string', 'mdmModel': 'string', 'mdmSerial': 'string', 'mdmEncrypted': True, 'mdmPinlock': True, 'mdmJailBroken': True, 'mdmIMEI': 'string', 'mdmPhoneNumber': 'string'},
        name='string',
        payload=None,
        portal_user='string',
        profile_id='string',
        static_group_assignment=True,
        static_profile_assignment=True
    )
    return endpoint_result


@pytest.mark.endpoint
def test_create_endpoint(api, validator):
    try:
        assert is_valid_create_endpoint(
            validator,
            create_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_endpoint_default(api):
    endpoint_result = api.endpoint.create_endpoint(
        active_validation=False,
        custom_attributes=None,
        description=None,
        group_id=None,
        identity_store=None,
        identity_store_id=None,
        mac=None,
        mdm_attributes=None,
        name=None,
        payload=None,
        portal_user=None,
        profile_id=None,
        static_group_assignment=None,
        static_profile_assignment=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_create_endpoint_default(api, validator):
    try:
        assert is_valid_create_endpoint(
            validator,
            create_endpoint_default(api)
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
    json_schema_validate('jsd_85adcb1d998d54838add3b4d644242af_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.endpoint.get_version(

    )
    return endpoint_result


@pytest.mark.endpoint
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
    endpoint_result = api.endpoint.get_version(

    )
    return endpoint_result


@pytest.mark.endpoint
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_request_for_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c03505504e8e5af8a715e27c40f16eab_v3_0_0').validate(obj.response)
    return True


def bulk_request_for_endpoint(api):
    endpoint_result = api.endpoint.bulk_request_for_endpoint(
        active_validation=False,
        operation_type='string',
        payload=None,
        resource_media_type='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_bulk_request_for_endpoint(api, validator):
    try:
        assert is_valid_bulk_request_for_endpoint(
            validator,
            bulk_request_for_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_request_for_endpoint_default(api):
    endpoint_result = api.endpoint.bulk_request_for_endpoint(
        active_validation=False,
        operation_type=None,
        payload=None,
        resource_media_type=None
    )
    return endpoint_result


@pytest.mark.endpoint
def test_bulk_request_for_endpoint_default(api, validator):
    try:
        assert is_valid_bulk_request_for_endpoint(
            validator,
            bulk_request_for_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_monitor_bulk_status_endpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_5b054a43ba875f0da3da5a7d863f3ef7_v3_0_0').validate(obj.response)
    return True


def monitor_bulk_status_endpoint(api):
    endpoint_result = api.endpoint.monitor_bulk_status_endpoint(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_monitor_bulk_status_endpoint(api, validator):
    try:
        assert is_valid_monitor_bulk_status_endpoint(
            validator,
            monitor_bulk_status_endpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def monitor_bulk_status_endpoint_default(api):
    endpoint_result = api.endpoint.monitor_bulk_status_endpoint(
        bulkid='string'
    )
    return endpoint_result


@pytest.mark.endpoint
def test_monitor_bulk_status_endpoint_default(api, validator):
    try:
        assert is_valid_monitor_bulk_status_endpoint(
            validator,
            monitor_bulk_status_endpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
