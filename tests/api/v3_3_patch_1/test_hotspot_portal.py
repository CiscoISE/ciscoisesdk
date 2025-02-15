# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI hotspot_portal API fixtures and tests.

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


def is_valid_get_hotspot_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_6cbcecf65a0155fcad602d3ac16531a7_v3_3_patch_1').validate(obj.response)
    return True


def get_hotspot_portal_by_id(api):
    endpoint_result = api.hotspot_portal.get_hotspot_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_get_hotspot_portal_by_id(api, validator):
    try:
        assert is_valid_get_hotspot_portal_by_id(
            validator,
            get_hotspot_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_hotspot_portal_by_id_default(api):
    endpoint_result = api.hotspot_portal.get_hotspot_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_get_hotspot_portal_by_id_default(api, validator):
    try:
        assert is_valid_get_hotspot_portal_by_id(
            validator,
            get_hotspot_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_hotspot_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0ae4af25df565334b20a24c4878b68e4_v3_3_patch_1').validate(obj.response)
    return True


def update_hotspot_portal_by_id(api):
    endpoint_result = api.hotspot_portal.update_hotspot_portal_by_id(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        id='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'coaType': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'aupSettings': {'requireAccessCode': True, 'accessCode': 'string', 'includeAup': True, 'requireScrolling': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_update_hotspot_portal_by_id(api, validator):
    try:
        assert is_valid_update_hotspot_portal_by_id(
            validator,
            update_hotspot_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_hotspot_portal_by_id_default(api):
    endpoint_result = api.hotspot_portal.update_hotspot_portal_by_id(
        active_validation=False,
        id='string',
        customizations=None,
        description=None,
        name=None,
        payload=None,
        portal_test_url=None,
        portal_type=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_update_hotspot_portal_by_id_default(api, validator):
    try:
        assert is_valid_update_hotspot_portal_by_id(
            validator,
            update_hotspot_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_hotspot_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1a344d1c6f535789b7badbaa502e8d3b_v3_3_patch_1').validate(obj.response)
    return True


def delete_hotspot_portal_by_id(api):
    endpoint_result = api.hotspot_portal.delete_hotspot_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_delete_hotspot_portal_by_id(api, validator):
    try:
        assert is_valid_delete_hotspot_portal_by_id(
            validator,
            delete_hotspot_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_hotspot_portal_by_id_default(api):
    endpoint_result = api.hotspot_portal.delete_hotspot_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_delete_hotspot_portal_by_id_default(api, validator):
    try:
        assert is_valid_delete_hotspot_portal_by_id(
            validator,
            delete_hotspot_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_hotspot_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d912b1c21e2b5dca8b56332d3a8ad13d_v3_3_patch_1').validate(obj.response)
    return True


def get_hotspot_portal(api):
    endpoint_result = api.hotspot_portal.get_hotspot_portal(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_get_hotspot_portal(api, validator):
    try:
        assert is_valid_get_hotspot_portal(
            validator,
            get_hotspot_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_hotspot_portal_default(api):
    endpoint_result = api.hotspot_portal.get_hotspot_portal(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_get_hotspot_portal_default(api, validator):
    try:
        assert is_valid_get_hotspot_portal(
            validator,
            get_hotspot_portal_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_hotspot_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0df78c9a3f72584dbd1c7b667b0e312f_v3_3_patch_1').validate(obj.response)
    return True


def create_hotspot_portal(api):
    endpoint_result = api.hotspot_portal.create_hotspot_portal(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'coaType': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'aupSettings': {'requireAccessCode': True, 'accessCode': 'string', 'includeAup': True, 'requireScrolling': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_create_hotspot_portal(api, validator):
    try:
        assert is_valid_create_hotspot_portal(
            validator,
            create_hotspot_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_hotspot_portal_default(api):
    endpoint_result = api.hotspot_portal.create_hotspot_portal(
        active_validation=False,
        customizations=None,
        description=None,
        name=None,
        payload=None,
        portal_test_url=None,
        portal_type=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_create_hotspot_portal_default(api, validator):
    try:
        assert is_valid_create_hotspot_portal(
            validator,
            create_hotspot_portal_default(api)
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
    json_schema_validate('jsd_91257d81be4f5a0486cc085499c19b1c_v3_3_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.hotspot_portal.get_version(

    )
    return endpoint_result


@pytest.mark.hotspot_portal
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
    endpoint_result = api.hotspot_portal.get_version(

    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_patch_hotspot_portal_portal_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_cfa8d603cadc58d59aa71f70fbb8aafd_v3_3_patch_1').validate(obj.response)
    return True


def patch_hotspot_portal_portal_id(api):
    endpoint_result = api.hotspot_portal.patch_hotspot_portal_portal_id(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'banneColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {}, 'globalCustomizations': {'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string', 'mobileLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        id='string',
        name='string',
        payload=None,
        portal_id='string',
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': 'string', 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string', 'coaType': 'string'}, 'aupSettings': {'requireAccessCode': True, 'accessCode': 'string', 'includeAup': True, 'requireAupScrolling': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_patch_hotspot_portal_portal_id(api, validator):
    try:
        assert is_valid_patch_hotspot_portal_portal_id(
            validator,
            patch_hotspot_portal_portal_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def patch_hotspot_portal_portal_id_default(api):
    endpoint_result = api.hotspot_portal.patch_hotspot_portal_portal_id(
        active_validation=False,
        portal_id='string',
        customizations=None,
        description=None,
        id=None,
        name=None,
        payload=None,
        portal_test_url=None,
        portal_type=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.hotspot_portal
def test_patch_hotspot_portal_portal_id_default(api, validator):
    try:
        assert is_valid_patch_hotspot_portal_portal_id(
            validator,
            patch_hotspot_portal_portal_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
