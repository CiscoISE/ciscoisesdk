# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_dictionary API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_network_access_dictionaries(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_1eb2cef3895d5bc68b7a28eca42ef630_v3_0_0').validate(obj.response)
    return True


def get_network_access_dictionaries(api):
    endpoint_result = api.network_access_dictionary.get_network_access_dictionaries(

    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_get_network_access_dictionaries(api, validator):
    try:
        assert is_valid_get_network_access_dictionaries(
            validator,
            get_network_access_dictionaries(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_dictionaries_default(api):
    endpoint_result = api.network_access_dictionary.get_network_access_dictionaries(

    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_get_network_access_dictionaries_default(api, validator):
    try:
        assert is_valid_get_network_access_dictionaries(
            validator,
            get_network_access_dictionaries_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_post_network_access_dictionaries(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_7205be755dae5251bd2d8348eeebfdde_v3_0_0').validate(obj.response)
    return True


def post_network_access_dictionaries(api):
    endpoint_result = api.network_access_dictionary.post_network_access_dictionaries(
        active_validation=False,
        description='string',
        dictionary_attr_type='string',
        id='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        payload=None,
        version='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_post_network_access_dictionaries(api, validator):
    try:
        assert is_valid_post_network_access_dictionaries(
            validator,
            post_network_access_dictionaries(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def post_network_access_dictionaries_default(api):
    endpoint_result = api.network_access_dictionary.post_network_access_dictionaries(
        active_validation=False,
        description=None,
        dictionary_attr_type=None,
        id=None,
        link=None,
        name=None,
        payload=None,
        version=None
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_post_network_access_dictionaries_default(api, validator):
    try:
        assert is_valid_post_network_access_dictionaries(
            validator,
            post_network_access_dictionaries_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_dictionary(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e60234354578568697b6740d08170678_v3_0_0').validate(obj.response)
    return True


def get_network_access_dictionary(api):
    endpoint_result = api.network_access_dictionary.get_network_access_dictionary(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_get_network_access_dictionary(api, validator):
    try:
        assert is_valid_get_network_access_dictionary(
            validator,
            get_network_access_dictionary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_dictionary_default(api):
    endpoint_result = api.network_access_dictionary.get_network_access_dictionary(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_get_network_access_dictionary_default(api, validator):
    try:
        assert is_valid_get_network_access_dictionary(
            validator,
            get_network_access_dictionary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_put_network_access_dictionaries_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e4f1e31aca1558f782a2cdb43853aaf2_v3_0_0').validate(obj.response)
    return True


def put_network_access_dictionaries_by_name(api):
    endpoint_result = api.network_access_dictionary.put_network_access_dictionaries_by_name(
        active_validation=False,
        description='string',
        dictionary_attr_type='string',
        id='string',
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        name='string',
        payload=None,
        version='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_put_network_access_dictionaries_by_name(api, validator):
    try:
        assert is_valid_put_network_access_dictionaries_by_name(
            validator,
            put_network_access_dictionaries_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_network_access_dictionaries_by_name_default(api):
    endpoint_result = api.network_access_dictionary.put_network_access_dictionaries_by_name(
        active_validation=False,
        name='string',
        description=None,
        dictionary_attr_type=None,
        id=None,
        link=None,
        payload=None,
        version=None
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_put_network_access_dictionaries_by_name_default(api, validator):
    try:
        assert is_valid_put_network_access_dictionaries_by_name(
            validator,
            put_network_access_dictionaries_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_dictionaries_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2b80087f14af51d186a7bfa89f5a494b_v3_0_0').validate(obj.response)
    return True


def delete_network_access_dictionaries_by_name(api):
    endpoint_result = api.network_access_dictionary.delete_network_access_dictionaries_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_delete_network_access_dictionaries_by_name(api, validator):
    try:
        assert is_valid_delete_network_access_dictionaries_by_name(
            validator,
            delete_network_access_dictionaries_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_dictionaries_by_name_default(api):
    endpoint_result = api.network_access_dictionary.delete_network_access_dictionaries_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_delete_network_access_dictionaries_by_name_default(api, validator):
    try:
        assert is_valid_delete_network_access_dictionaries_by_name(
            validator,
            delete_network_access_dictionaries_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
