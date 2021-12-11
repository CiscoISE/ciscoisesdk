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
from ciscoisesdk.exceptions import ciscoisesdkException
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.1', reason='version does not match')


def is_valid_get_network_access_dictionaries(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8f0c9b561c6257a5b5fcc4f0eb8d875a_v3_1_1').validate(obj.response)
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
            print("ERROR: {error}".format(error=original_e))
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


def is_valid_create_network_access_dictionaries(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_20c038e43a955a42ad4a6822f525d05e_v3_1_1').validate(obj.response)
    return True


def create_network_access_dictionaries(api):
    endpoint_result = api.network_access_dictionary.create_network_access_dictionaries(
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
def test_create_network_access_dictionaries(api, validator):
    try:
        assert is_valid_create_network_access_dictionaries(
            validator,
            create_network_access_dictionaries(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_network_access_dictionaries_default(api):
    endpoint_result = api.network_access_dictionary.create_network_access_dictionaries(
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
def test_create_network_access_dictionaries_default(api, validator):
    try:
        assert is_valid_create_network_access_dictionaries(
            validator,
            create_network_access_dictionaries_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_dictionary_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d36440a5e1f8560ba7146ce16cc5e9d7_v3_1_1').validate(obj.response)
    return True


def get_network_access_dictionary_by_name(api):
    endpoint_result = api.network_access_dictionary.get_network_access_dictionary_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_get_network_access_dictionary_by_name(api, validator):
    try:
        assert is_valid_get_network_access_dictionary_by_name(
            validator,
            get_network_access_dictionary_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_network_access_dictionary_by_name_default(api):
    endpoint_result = api.network_access_dictionary.get_network_access_dictionary_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_get_network_access_dictionary_by_name_default(api, validator):
    try:
        assert is_valid_get_network_access_dictionary_by_name(
            validator,
            get_network_access_dictionary_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_dictionary_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6005031ca76d5d419ee9d9fb4d6df9d6_v3_1_1').validate(obj.response)
    return True


def update_network_access_dictionary_by_name(api):
    endpoint_result = api.network_access_dictionary.update_network_access_dictionary_by_name(
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
def test_update_network_access_dictionary_by_name(api, validator):
    try:
        assert is_valid_update_network_access_dictionary_by_name(
            validator,
            update_network_access_dictionary_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_network_access_dictionary_by_name_default(api):
    endpoint_result = api.network_access_dictionary.update_network_access_dictionary_by_name(
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
def test_update_network_access_dictionary_by_name_default(api, validator):
    try:
        assert is_valid_update_network_access_dictionary_by_name(
            validator,
            update_network_access_dictionary_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_dictionary_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_37db7520334b5264acb4ee9eea31e543_v3_1_1').validate(obj.response)
    return True


def delete_network_access_dictionary_by_name(api):
    endpoint_result = api.network_access_dictionary.delete_network_access_dictionary_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_delete_network_access_dictionary_by_name(api, validator):
    try:
        assert is_valid_delete_network_access_dictionary_by_name(
            validator,
            delete_network_access_dictionary_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_network_access_dictionary_by_name_default(api):
    endpoint_result = api.network_access_dictionary.delete_network_access_dictionary_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.network_access_dictionary
def test_delete_network_access_dictionary_by_name_default(api, validator):
    try:
        assert is_valid_delete_network_access_dictionary_by_name(
            validator,
            delete_network_access_dictionary_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
