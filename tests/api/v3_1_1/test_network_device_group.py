# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_device_group API fixtures and tests.

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


def is_valid_get_network_device_group_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e1d938f110e059a5abcb9cc8fb3cbd7c_v3_1_1').validate(obj.response)
    return True


def get_network_device_group_by_name(api):
    endpoint_result = api.network_device_group.get_network_device_group_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_get_network_device_group_by_name(api, validator):
    try:
        assert is_valid_get_network_device_group_by_name(
            validator,
            get_network_device_group_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_device_group_by_name_default(api):
    endpoint_result = api.network_device_group.get_network_device_group_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_get_network_device_group_by_name_default(api, validator):
    try:
        assert is_valid_get_network_device_group_by_name(
            validator,
            get_network_device_group_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a0fdb67d95475cd39382171dec96d6c1_v3_1_1').validate(obj.response)
    return True


def get_network_device_group_by_id(api):
    endpoint_result = api.network_device_group.get_network_device_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_get_network_device_group_by_id(api, validator):
    try:
        assert is_valid_get_network_device_group_by_id(
            validator,
            get_network_device_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_device_group_by_id_default(api):
    endpoint_result = api.network_device_group.get_network_device_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_get_network_device_group_by_id_default(api, validator):
    try:
        assert is_valid_get_network_device_group_by_id(
            validator,
            get_network_device_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_device_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_808461e6734850fabb2097fa969948cb_v3_1_1').validate(obj.response)
    return True


def update_network_device_group_by_id(api):
    endpoint_result = api.network_device_group.update_network_device_group_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        othername='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_update_network_device_group_by_id(api, validator):
    try:
        assert is_valid_update_network_device_group_by_id(
            validator,
            update_network_device_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_network_device_group_by_id_default(api):
    endpoint_result = api.network_device_group.update_network_device_group_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        othername=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_update_network_device_group_by_id_default(api, validator):
    try:
        assert is_valid_update_network_device_group_by_id(
            validator,
            update_network_device_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_device_group_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_9291975ded6653128f502c97e52cf279_v3_1_1').validate(obj.response)
    return True


def delete_network_device_group_by_id(api):
    endpoint_result = api.network_device_group.delete_network_device_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_delete_network_device_group_by_id(api, validator):
    try:
        assert is_valid_delete_network_device_group_by_id(
            validator,
            delete_network_device_group_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_network_device_group_by_id_default(api):
    endpoint_result = api.network_device_group.delete_network_device_group_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_delete_network_device_group_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_device_group_by_id(
            validator,
            delete_network_device_group_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2a1af553d663556ca429a10ed82effda_v3_1_1').validate(obj.response)
    return True


def get_network_device_group(api):
    endpoint_result = api.network_device_group.get_network_device_group(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_get_network_device_group(api, validator):
    try:
        assert is_valid_get_network_device_group(
            validator,
            get_network_device_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_device_group_default(api):
    endpoint_result = api.network_device_group.get_network_device_group(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_get_network_device_group_default(api, validator):
    try:
        assert is_valid_get_network_device_group(
            validator,
            get_network_device_group_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_device_group(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6c38fb2e2dd45f4dab6ec3a19effd15a_v3_1_1').validate(obj.response)
    return True


def create_network_device_group(api):
    endpoint_result = api.network_device_group.create_network_device_group(
        active_validation=False,
        description='string',
        name='string',
        othername='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_create_network_device_group(api, validator):
    try:
        assert is_valid_create_network_device_group(
            validator,
            create_network_device_group(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_network_device_group_default(api):
    endpoint_result = api.network_device_group.create_network_device_group(
        active_validation=False,
        description=None,
        name=None,
        othername=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_device_group
def test_create_network_device_group_default(api, validator):
    try:
        assert is_valid_create_network_device_group(
            validator,
            create_network_device_group_default(api)
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
    json_schema_validate('jsd_163f22d64bd4557d856a66ad6599d2d1_v3_1_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.network_device_group.get_version(

    )
    return endpoint_result


@pytest.mark.network_device_group
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
    endpoint_result = api.network_device_group.get_version(

    )
    return endpoint_result


@pytest.mark.network_device_group
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
