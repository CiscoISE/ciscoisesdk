# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI nbar_app API fixtures and tests.

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


def is_valid_get_nbar_apps(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1e8a476ad8455fdebad0d8973c810495_v3_1_1').validate(obj.response)
    return True


def get_nbar_apps(api):
    endpoint_result = api.nbar_app.get_nbar_apps(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_get_nbar_apps(api, validator):
    try:
        assert is_valid_get_nbar_apps(
            validator,
            get_nbar_apps(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_nbar_apps_default(api):
    endpoint_result = api.nbar_app.get_nbar_apps(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_get_nbar_apps_default(api, validator):
    try:
        assert is_valid_get_nbar_apps(
            validator,
            get_nbar_apps_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_nbar_app(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ccc30178afce5e51a65e96cd95ca1773_v3_1_1').validate(obj.response)
    return True


def create_nbar_app(api):
    endpoint_result = api.nbar_app.create_nbar_app(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        network_identities=[{'ports': 'string', 'protocol': 'string'}],
        payload=None
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_create_nbar_app(api, validator):
    try:
        assert is_valid_create_nbar_app(
            validator,
            create_nbar_app(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_nbar_app_default(api):
    endpoint_result = api.nbar_app.create_nbar_app(
        active_validation=False,
        description=None,
        id=None,
        name=None,
        network_identities=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_create_nbar_app_default(api, validator):
    try:
        assert is_valid_create_nbar_app(
            validator,
            create_nbar_app_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_nbar_app_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_61e99726f3745554a07ee102f74fe3bd_v3_1_1').validate(obj.response)
    return True


def get_nbar_app_by_id(api):
    endpoint_result = api.nbar_app.get_nbar_app_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_get_nbar_app_by_id(api, validator):
    try:
        assert is_valid_get_nbar_app_by_id(
            validator,
            get_nbar_app_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_nbar_app_by_id_default(api):
    endpoint_result = api.nbar_app.get_nbar_app_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_get_nbar_app_by_id_default(api, validator):
    try:
        assert is_valid_get_nbar_app_by_id(
            validator,
            get_nbar_app_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_nbar_app_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b55622f1671359919573b261ba16ea71_v3_1_1').validate(obj.response)
    return True


def update_nbar_app_by_id(api):
    endpoint_result = api.nbar_app.update_nbar_app_by_id(
        active_validation=False,
        description='string',
        id='string',
        name='string',
        network_identities=[{'ports': 'string', 'protocol': 'string'}],
        payload=None
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_update_nbar_app_by_id(api, validator):
    try:
        assert is_valid_update_nbar_app_by_id(
            validator,
            update_nbar_app_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_nbar_app_by_id_default(api):
    endpoint_result = api.nbar_app.update_nbar_app_by_id(
        active_validation=False,
        id='string',
        description=None,
        name=None,
        network_identities=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_update_nbar_app_by_id_default(api, validator):
    try:
        assert is_valid_update_nbar_app_by_id(
            validator,
            update_nbar_app_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_nbar_app_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_44d289d5685350f5b00f130db0a45142_v3_1_1').validate(obj.response)
    return True


def delete_nbar_app_by_id(api):
    endpoint_result = api.nbar_app.delete_nbar_app_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_delete_nbar_app_by_id(api, validator):
    try:
        assert is_valid_delete_nbar_app_by_id(
            validator,
            delete_nbar_app_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_nbar_app_by_id_default(api):
    endpoint_result = api.nbar_app.delete_nbar_app_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.nbar_app
def test_delete_nbar_app_by_id_default(api, validator):
    try:
        assert is_valid_delete_nbar_app_by_id(
            validator,
            delete_nbar_app_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
