# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI support_bundle API fixtures and tests.

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


def is_valid_download_support_bundle(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_737531846d125b968b9d362a3458621d_v3_0_0').validate(obj.response)
    return True


def download_support_bundle(api):
    endpoint_result = api.support_bundle.download_support_bundle(
        dirpath=None,
        save_file=None,
        active_validation=False,
        file_name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.support_bundle
def test_download_support_bundle(api, validator):
    try:
        assert is_valid_download_support_bundle(
            validator,
            download_support_bundle(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def download_support_bundle_default(api):
    endpoint_result = api.support_bundle.download_support_bundle(
        dirpath=None,
        save_file=None,
        active_validation=False,
        file_name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.support_bundle
def test_download_support_bundle_default(api, validator):
    try:
        assert is_valid_download_support_bundle(
            validator,
            download_support_bundle_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_support_bundle_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_505300e162f051d58c6ae9d5e3851780_v3_0_0').validate(obj.response)
    return True


def get_all_support_bundle_status(api):
    endpoint_result = api.support_bundle.get_all_support_bundle_status(

    )
    return endpoint_result


@pytest.mark.support_bundle
def test_get_all_support_bundle_status(api, validator):
    try:
        assert is_valid_get_all_support_bundle_status(
            validator,
            get_all_support_bundle_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_support_bundle_status_default(api):
    endpoint_result = api.support_bundle.get_all_support_bundle_status(

    )
    return endpoint_result


@pytest.mark.support_bundle
def test_get_all_support_bundle_status_default(api, validator):
    try:
        assert is_valid_get_all_support_bundle_status(
            validator,
            get_all_support_bundle_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_support_bundle_status_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_cec7dc317e875ff0a315a7c0556f9c51_v3_0_0').validate(obj.response)
    return True


def get_support_bundle_status_by_id(api):
    endpoint_result = api.support_bundle.get_support_bundle_status_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.support_bundle
def test_get_support_bundle_status_by_id(api, validator):
    try:
        assert is_valid_get_support_bundle_status_by_id(
            validator,
            get_support_bundle_status_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_support_bundle_status_by_id_default(api):
    endpoint_result = api.support_bundle.get_support_bundle_status_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.support_bundle
def test_get_support_bundle_status_by_id_default(api, validator):
    try:
        assert is_valid_get_support_bundle_status_by_id(
            validator,
            get_support_bundle_status_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_support_bundle(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_492171fac48e5c63abfe2feec6fd1903_v3_0_0').validate(obj.response)
    return True


def create_support_bundle(api):
    endpoint_result = api.support_bundle.create_support_bundle(
        active_validation=False,
        description='string',
        host_name='string',
        name='string',
        payload=None,
        support_bundle_include_options={'includeConfigDB': True, 'includeDebugLogs': True, 'includeLocalLogs': True, 'includeCoreFiles': True, 'mntLogs': True, 'includeSystemLogs': True, 'policyXml': True, 'fromDate': 'string', 'toDate': 'string'}
    )
    return endpoint_result


@pytest.mark.support_bundle
def test_create_support_bundle(api, validator):
    try:
        assert is_valid_create_support_bundle(
            validator,
            create_support_bundle(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_support_bundle_default(api):
    endpoint_result = api.support_bundle.create_support_bundle(
        active_validation=False,
        description=None,
        host_name=None,
        name=None,
        payload=None,
        support_bundle_include_options=None
    )
    return endpoint_result


@pytest.mark.support_bundle
def test_create_support_bundle_default(api, validator):
    try:
        assert is_valid_create_support_bundle(
            validator,
            create_support_bundle_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
