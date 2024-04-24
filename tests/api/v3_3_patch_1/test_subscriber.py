# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI subscriber API fixtures and tests.

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


def is_valid_get_all_subscribers(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bb725fc737535a23b2459a255a4b9725_v3_3_patch_1').validate(obj.response)
    return True


def get_all_subscribers(api):
    endpoint_result = api.subscriber.get_all_subscribers(
        filter='string',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_get_all_subscribers(api, validator):
    try:
        assert is_valid_get_all_subscribers(
            validator,
            get_all_subscribers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_all_subscribers_default(api):
    endpoint_result = api.subscriber.get_all_subscribers(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.subscriber
def test_get_all_subscribers_default(api, validator):
    try:
        assert is_valid_get_all_subscribers(
            validator,
            get_all_subscribers_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_subscriber(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3083c9ea8f91504d9aa46ebd90dd1ab4_v3_3_patch_1').validate(obj.response)
    return True


def create_subscriber(api):
    endpoint_result = api.subscriber.create_subscriber(
        active_validation=False,
        enabled=True,
        friendly_name='string',
        identity_groups='string',
        imeis='string',
        imsi='string',
        ki='string',
        opc='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.subscriber
def test_create_subscriber(api, validator):
    try:
        assert is_valid_create_subscriber(
            validator,
            create_subscriber(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_subscriber_default(api):
    endpoint_result = api.subscriber.create_subscriber(
        active_validation=False,
        enabled=None,
        friendly_name=None,
        identity_groups=None,
        imeis=None,
        imsi=None,
        ki=None,
        opc=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.subscriber
def test_create_subscriber_default(api, validator):
    try:
        assert is_valid_create_subscriber(
            validator,
            create_subscriber_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_subscriber_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2bf1dfb9226e534cb039880148e47e95_v3_3_patch_1').validate(obj.response)
    return True


def get_subscriber_by_id(api):
    endpoint_result = api.subscriber.get_subscriber_by_id(
        subscriber_id='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_get_subscriber_by_id(api, validator):
    try:
        assert is_valid_get_subscriber_by_id(
            validator,
            get_subscriber_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_subscriber_by_id_default(api):
    endpoint_result = api.subscriber.get_subscriber_by_id(
        subscriber_id='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_get_subscriber_by_id_default(api, validator):
    try:
        assert is_valid_get_subscriber_by_id(
            validator,
            get_subscriber_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_subscriber(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_cfc8b401a45650b386d0ae88c2ac3ef4_v3_3_patch_1').validate(obj.response)
    return True


def update_subscriber(api):
    endpoint_result = api.subscriber.update_subscriber(
        active_validation=False,
        enabled=True,
        friendly_name='string',
        identity_groups='string',
        imeis='string',
        ki='string',
        opc='string',
        payload=None,
        subscriber_id='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_update_subscriber(api, validator):
    try:
        assert is_valid_update_subscriber(
            validator,
            update_subscriber(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_subscriber_default(api):
    endpoint_result = api.subscriber.update_subscriber(
        active_validation=False,
        subscriber_id='string',
        enabled=None,
        friendly_name=None,
        identity_groups=None,
        imeis=None,
        ki=None,
        opc=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.subscriber
def test_update_subscriber_default(api, validator):
    try:
        assert is_valid_update_subscriber(
            validator,
            update_subscriber_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_subscriber(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ce70db8b014a599d8b6d623c4713b176_v3_3_patch_1').validate(obj.response)
    return True


def delete_subscriber(api):
    endpoint_result = api.subscriber.delete_subscriber(
        subscriber_id='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_delete_subscriber(api, validator):
    try:
        assert is_valid_delete_subscriber(
            validator,
            delete_subscriber(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_subscriber_default(api):
    endpoint_result = api.subscriber.delete_subscriber(
        subscriber_id='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_delete_subscriber_default(api, validator):
    try:
        assert is_valid_delete_subscriber(
            validator,
            delete_subscriber_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_subscriber_by_i_m_s_i(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_a1b71359fd0351f3a7f824ce8c4df14a_v3_3_patch_1').validate(obj.response)
    return True


def get_subscriber_by_i_m_s_i(api):
    endpoint_result = api.subscriber.get_subscriber_by_i_m_s_i(
        imsi='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_get_subscriber_by_i_m_s_i(api, validator):
    try:
        assert is_valid_get_subscriber_by_i_m_s_i(
            validator,
            get_subscriber_by_i_m_s_i(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_subscriber_by_i_m_s_i_default(api):
    endpoint_result = api.subscriber.get_subscriber_by_i_m_s_i(
        imsi='string'
    )
    return endpoint_result


@pytest.mark.subscriber
def test_get_subscriber_by_i_m_s_i_default(api, validator):
    try:
        assert is_valid_get_subscriber_by_i_m_s_i(
            validator,
            get_subscriber_by_i_m_s_i_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_subscriber_operation(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ee509b9ea4465d33bcb6552b30ec32b6_v3_3_patch_1').validate(obj.response)
    return True


def bulk_subscriber_operation(api):
    endpoint_result = api.subscriber.bulk_subscriber_operation(
        active_validation=False,
        item_list=[{'id': 'string', 'imsi': 'string', 'enabled': True, 'friendlyName': 'string', 'identityGroups': 'string', 'imeis': 'string', 'opc': 'string', 'ki': 'string'}],
        operation='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.subscriber
def test_bulk_subscriber_operation(api, validator):
    try:
        assert is_valid_bulk_subscriber_operation(
            validator,
            bulk_subscriber_operation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bulk_subscriber_operation_default(api):
    endpoint_result = api.subscriber.bulk_subscriber_operation(
        active_validation=False,
        item_list=None,
        operation=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.subscriber
def test_bulk_subscriber_operation_default(api, validator):
    try:
        assert is_valid_bulk_subscriber_operation(
            validator,
            bulk_subscriber_operation_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
