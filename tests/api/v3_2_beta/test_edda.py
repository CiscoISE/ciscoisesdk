# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI edda API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.2_beta', reason='version does not match')


def is_valid_get_connector_config(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3c8f79c0801555878ad94493ade34587_v3_2_beta').validate(obj.response)
    return True


def get_connector_config(api):
    endpoint_result = api.edda.get_connector_config(

    )
    return endpoint_result


@pytest.mark.edda
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
    endpoint_result = api.edda.get_connector_config(

    )
    return endpoint_result


@pytest.mark.edda
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
    json_schema_validate('jsd_92c89285c31159faa2fb8abee25ce4a4_v3_2_beta').validate(obj.response)
    return True


def create_connector_config(api):
    endpoint_result = api.edda.create_connector_config(
        active_validation=False,
        additional_properties={},
        attributes={'attributeMapping': [{'dictionaryAttribute': 'string', 'includeInDictionary': True, 'jsonAttribute': 'string'}], 'bulkUniqueIdentifier': 'string', 'topLevelObject': 'string', 'uniqueIdentifier': 'string', 'versionIdentifier': 'string'},
        connector_name='string',
        connector_type='string',
        deltasync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        description='string',
        enabled=True,
        fullsync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        payload=None,
        protocol='string',
        skip_certificate_validations=True,
        url={'accessKey': 'string', 'authenticationType': 'string', 'bulkUrl': 'string', 'clientId': 'string', 'clientSecret': 'string', 'incrementalUrl': 'string', 'password': 'string', 'refreshToken': 'string', 'tokenHeader': 'string', 'userName': 'string'}
    )
    return endpoint_result


@pytest.mark.edda
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
    endpoint_result = api.edda.create_connector_config(
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


@pytest.mark.edda
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
    json_schema_validate('jsd_a3c21e5b61d95a0b9acf313e3ea03ad7_v3_2_beta').validate(obj.response)
    return True


def get_connector_config_by_connector_name(api):
    endpoint_result = api.edda.get_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.edda
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
    endpoint_result = api.edda.get_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.edda
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
    json_schema_validate('jsd_7f5b69ccd0075b18a3de9e72b9e450cb_v3_2_beta').validate(obj.response)
    return True


def update_connector_config_by_connector_name(api):
    endpoint_result = api.edda.update_connector_config_by_connector_name(
        active_validation=False,
        additional_properties={},
        attributes={'attributeMapping': [{'dictionaryAttribute': 'string', 'includeInDictionary': True, 'jsonAttribute': 'string'}], 'bulkUniqueIdentifier': 'string', 'topLevelObject': 'string', 'uniqueIdentifier': 'string', 'versionIdentifier': 'string'},
        connector_name='string',
        connector_type='string',
        deltasync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        description='string',
        enabled=True,
        fullsync_schedule={'interval': 0, 'intervalUnit': 'string', 'startDate': 'string'},
        payload=None,
        protocol='string',
        skip_certificate_validations=True,
        url={'accessKey': 'string', 'authenticationType': 'string', 'bulkUrl': 'string', 'clientId': 'string', 'clientSecret': 'string', 'incrementalUrl': 'string', 'password': 'string', 'refreshToken': 'string', 'tokenHeader': 'string', 'userName': 'string'}
    )
    return endpoint_result


@pytest.mark.edda
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
    endpoint_result = api.edda.update_connector_config_by_connector_name(
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


@pytest.mark.edda
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
    json_schema_validate('jsd_7011b1f3a77153ee82dca51d2a94f5b9_v3_2_beta').validate(obj.response)
    return True


def delete_connector_config_by_connector_name(api):
    endpoint_result = api.edda.delete_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.edda
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
    endpoint_result = api.edda.delete_connector_config_by_connector_name(
        connector_name='string'
    )
    return endpoint_result


@pytest.mark.edda
def test_delete_connector_config_by_connector_name_default(api, validator):
    try:
        assert is_valid_delete_connector_config_by_connector_name(
            validator,
            delete_connector_config_by_connector_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_edda_dictionary_references(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_5bcc373fcfcd5bf69742d3d63dd6f92a_v3_2_beta').validate(obj.response)
    return True


def get_edda_dictionary_references(api):
    endpoint_result = api.edda.get_edda_dictionary_references(

    )
    return endpoint_result


@pytest.mark.edda
def test_get_edda_dictionary_references(api, validator):
    try:
        assert is_valid_get_edda_dictionary_references(
            validator,
            get_edda_dictionary_references(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_edda_dictionary_references_default(api):
    endpoint_result = api.edda.get_edda_dictionary_references(

    )
    return endpoint_result


@pytest.mark.edda
def test_get_edda_dictionary_references_default(api, validator):
    try:
        assert is_valid_get_edda_dictionary_references(
            validator,
            get_edda_dictionary_references_default(api)
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
    json_schema_validate('jsd_ed122b5ef64b5ecabe3526490589e041_v3_2_beta').validate(obj.response)
    return True


def test_connector(api):
    endpoint_result = api.edda.test_connector(
        active_validation=False,
        auth_type='string',
        auth_values={'password': 'string', 'userName': 'string'},
        connector_name='string',
        payload=None,
        response_parsing='string',
        unique_id='string',
        url='string'
    )
    return endpoint_result


@pytest.mark.edda
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
    endpoint_result = api.edda.test_connector(
        active_validation=False,
        auth_type=None,
        auth_values=None,
        connector_name=None,
        payload=None,
        response_parsing=None,
        unique_id=None,
        url=None
    )
    return endpoint_result


@pytest.mark.edda
def test_test_connector_default(api, validator):
    try:
        assert is_valid_test_connector(
            validator,
            test_connector_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
