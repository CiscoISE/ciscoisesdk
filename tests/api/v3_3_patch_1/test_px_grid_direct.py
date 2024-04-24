# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI px_grid_direct API fixtures and tests.

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


def is_valid_get_connector_config(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_318d1004b4485c06871c0c86358068cb_v3_3_patch_1').validate(obj.response)
    return True


def get_connector_config(api):
    endpoint_result = api.px_grid_direct.get_connector_config(

    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_get_connector_config(api, validator):
    try:
        assert is_valid_get_connector_config(
            validator,
            get_connector_config(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_connector_config_default(api):
    endpoint_result = api.px_grid_direct.get_connector_config(

    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_get_connector_config_default(api, validator):
    try:
        assert is_valid_get_connector_config(
            validator,
            get_connector_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_connector_config(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_af9c8ad00e925e6885c3b3167dbdb4a3_v3_3_patch_1').validate(obj.response)
    return True


def create_connector_config(api):
    endpoint_result = api.px_grid_direct.create_connector_config(
        active_validation=False,
        additional_properties={},
        attributes={'attributeMapping': [{'dictionaryAttribute': 'string', 'includeInDictionary': True, 'jsonAttribute': 'string'}], 'correlationIdentifier': 'string', 'topLevelObject': 'string', 'uniqueIdentifier': 'string', 'versionIdentifier': 'string'},
        connector_name='string',
        connector_type='string',
        deltasync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        description='string',
        enabled=True,
        fullsync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        payload=None,
        protocol='string',
        skip_certificate_validations=True,
        url={'authenticationType': 'string', 'bulkUrl': 'string', 'incrementalUrl': 'string', 'password': 'string', 'userName': 'string'}
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_create_connector_config(api, validator):
    try:
        assert is_valid_create_connector_config(
            validator,
            create_connector_config(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_connector_config_default(api):
    endpoint_result = api.px_grid_direct.create_connector_config(
        active_validation=False,
        additional_properties=None,
        attributes=None,
        connector_name=None,
        connector_type=None,
        deltasync_schedule=None,
        description=None,
        enabled=None,
        fullsync_schedule=None,
        payload=None,
        protocol=None,
        skip_certificate_validations=None,
        url=None
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_create_connector_config_default(api, validator):
    try:
        assert is_valid_create_connector_config(
            validator,
            create_connector_config_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_connector_config_by_connector_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9994d4fedcc553a3966efb225bd927c6_v3_3_patch_1').validate(obj.response)
    return True


def get_connector_config_by_connector_name(api):
    endpoint_result = api.px_grid_direct.get_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_get_connector_config_by_connector_name(api, validator):
    try:
        assert is_valid_get_connector_config_by_connector_name(
            validator,
            get_connector_config_by_connector_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_connector_config_by_connector_name_default(api):
    endpoint_result = api.px_grid_direct.get_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_get_connector_config_by_connector_name_default(api, validator):
    try:
        assert is_valid_get_connector_config_by_connector_name(
            validator,
            get_connector_config_by_connector_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_connector_config_by_connector_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_87dbcbf6ee965b90a47c157c87efef5f_v3_3_patch_1').validate(obj.response)
    return True


def update_connector_config_by_connector_name(api):
    endpoint_result = api.px_grid_direct.update_connector_config_by_connector_name(
        active_validation=False,
        additional_properties={},
        attributes={'attributeMapping': [{'dictionaryAttribute': 'string', 'includeInDictionary': True, 'jsonAttribute': 'string'}], 'correlationIdentifier': 'string', 'topLevelObject': 'string', 'uniqueIdentifier': 'string', 'versionIdentifier': 'string'},
        connector_name='string',
        connector_type='string',
        deltasync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        description='string',
        enabled=True,
        fullsync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        payload=None,
        protocol='string',
        skip_certificate_validations=True,
        url={'authenticationType': 'string', 'bulkUrl': 'string', 'incrementalUrl': 'string', 'password': 'string', 'userName': 'string'}
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_update_connector_config_by_connector_name(api, validator):
    try:
        assert is_valid_update_connector_config_by_connector_name(
            validator,
            update_connector_config_by_connector_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_connector_config_by_connector_name_default(api):
    endpoint_result = api.px_grid_direct.update_connector_config_by_connector_name(
        active_validation=False,
        connector_name='string',
        additional_properties=None,
        attributes=None,
        connector_type=None,
        deltasync_schedule=None,
        description=None,
        enabled=None,
        fullsync_schedule=None,
        payload=None,
        protocol=None,
        skip_certificate_validations=None,
        url=None
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_update_connector_config_by_connector_name_default(api, validator):
    try:
        assert is_valid_update_connector_config_by_connector_name(
            validator,
            update_connector_config_by_connector_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_connector_config_by_connector_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_87dbb36cd7f25770b884da5053decff4_v3_3_patch_1').validate(obj.response)
    return True


def delete_connector_config_by_connector_name(api):
    endpoint_result = api.px_grid_direct.delete_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_delete_connector_config_by_connector_name(api, validator):
    try:
        assert is_valid_delete_connector_config_by_connector_name(
            validator,
            delete_connector_config_by_connector_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_connector_config_by_connector_name_default(api):
    endpoint_result = api.px_grid_direct.delete_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_delete_connector_config_by_connector_name_default(api, validator):
    try:
        assert is_valid_delete_connector_config_by_connector_name(
            validator,
            delete_connector_config_by_connector_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_getpxgrid_direct_dictionary_references(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_851a85e09e275340b9c39f9f0cc77902_v3_3_patch_1').validate(obj.response)
    return True


def getpxgrid_direct_dictionary_references(api):
    endpoint_result = api.px_grid_direct.getpxgrid_direct_dictionary_references(

    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_getpxgrid_direct_dictionary_references(api, validator):
    try:
        assert is_valid_getpxgrid_direct_dictionary_references(
            validator,
            getpxgrid_direct_dictionary_references(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def getpxgrid_direct_dictionary_references_default(api):
    endpoint_result = api.px_grid_direct.getpxgrid_direct_dictionary_references(

    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_getpxgrid_direct_dictionary_references_default(api, validator):
    try:
        assert is_valid_getpxgrid_direct_dictionary_references(
            validator,
            getpxgrid_direct_dictionary_references_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_connector_config_sync_now_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_059f5ea29c9654f99a341aff1c064f9b_v3_3_patch_1').validate(obj.response)
    return True


def get_connector_config_sync_now_status(api):
    endpoint_result = api.px_grid_direct.get_connector_config_sync_now_status(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_get_connector_config_sync_now_status(api, validator):
    try:
        assert is_valid_get_connector_config_sync_now_status(
            validator,
            get_connector_config_sync_now_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_connector_config_sync_now_status_default(api):
    endpoint_result = api.px_grid_direct.get_connector_config_sync_now_status(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_get_connector_config_sync_now_status_default(api, validator):
    try:
        assert is_valid_get_connector_config_sync_now_status(
            validator,
            get_connector_config_sync_now_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_now_connector(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_a83fbc2fed26547b964c13e5771038f7_v3_3_patch_1').validate(obj.response)
    return True


def sync_now_connector(api):
    endpoint_result = api.px_grid_direct.sync_now_connector(
        active_validation=False,
        connector_name='string',
        description='string',
        payload=None,
        sync_type='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_sync_now_connector(api, validator):
    try:
        assert is_valid_sync_now_connector(
            validator,
            sync_now_connector(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def sync_now_connector_default(api):
    endpoint_result = api.px_grid_direct.sync_now_connector(
        active_validation=False,
        connector_name=None,
        description=None,
        payload=None,
        sync_type=None
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_sync_now_connector_default(api, validator):
    try:
        assert is_valid_sync_now_connector(
            validator,
            sync_now_connector_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_test_connector(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d4ff0e7ffab4526fbdb811b264bba36d_v3_3_patch_1').validate(obj.response)
    return True


def test_connector(api):
    endpoint_result = api.px_grid_direct.test_connector(
        active_validation=False,
        auth_type='string',
        auth_values={'password': 'string', 'userName': 'string'},
        connector_name='string',
        payload=None,
        response_parsing='string',
        skip_certificate_validations=True,
        unique_id='string',
        url='string'
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_test_connector(api, validator):
    try:
        assert is_valid_test_connector(
            validator,
            test_connector(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def test_connector_default(api):
    endpoint_result = api.px_grid_direct.test_connector(
        active_validation=False,
        auth_type=None,
        auth_values=None,
        connector_name=None,
        payload=None,
        response_parsing=None,
        skip_certificate_validations=None,
        unique_id=None,
        url=None
    )
    return endpoint_result


@pytest.mark.px_grid_direct
def test_test_connector_default(api, validator):
    try:
        assert is_valid_test_connector(
            validator,
            test_connector_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
