# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sponsor_portal API fixtures and tests.

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


def is_valid_get_sponsor_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_cd6793a4a8e7576c8b290bdc88001f6f_v3_0_0').validate(obj.response)
    return True


def get_sponsor_portal_by_id(api):
    endpoint_result = api.sponsor_portal.get_sponsor_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_get_sponsor_portal_by_id(api, validator):
    try:
        assert is_valid_get_sponsor_portal_by_id(
            validator,
            get_sponsor_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sponsor_portal_by_id_default(api):
    endpoint_result = api.sponsor_portal.get_sponsor_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_get_sponsor_portal_by_id_default(api, validator):
    try:
        assert is_valid_get_sponsor_portal_by_id(
            validator,
            get_sponsor_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sponsor_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bd8691c5d9435e48a3c7a08658bda585_v3_0_0').validate(obj.response)
    return True


def update_sponsor_portal_by_id(api):
    endpoint_result = api.sponsor_portal.update_sponsor_portal_by_id(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        id='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'fqdn': 'string', 'authenticationMethod': 'string', 'idleTimeout': 0, 'displayLang': 'string', 'fallbackLanguage': 'string', 'availableSsids': ['string']}, 'loginPageSettings': {'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireAupScrolling': True, 'socialConfigs': []}, 'aupSettings': {'includeAup': True, 'requireScrolling': True, 'displayFrequency': 'string', 'displayFrequencyIntervalDays': 0}, 'sponsorChangePasswordSettings': {'allowSponsorToChangePwd': True}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_update_sponsor_portal_by_id(api, validator):
    try:
        assert is_valid_update_sponsor_portal_by_id(
            validator,
            update_sponsor_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_sponsor_portal_by_id_default(api):
    endpoint_result = api.sponsor_portal.update_sponsor_portal_by_id(
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


@pytest.mark.sponsor_portal
def test_update_sponsor_portal_by_id_default(api, validator):
    try:
        assert is_valid_update_sponsor_portal_by_id(
            validator,
            update_sponsor_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sponsor_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d8d4c7451f7f5e2faae4e8ac530b5f08_v3_0_0').validate(obj.response)
    return True


def delete_sponsor_portal_by_id(api):
    endpoint_result = api.sponsor_portal.delete_sponsor_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_delete_sponsor_portal_by_id(api, validator):
    try:
        assert is_valid_delete_sponsor_portal_by_id(
            validator,
            delete_sponsor_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_sponsor_portal_by_id_default(api):
    endpoint_result = api.sponsor_portal.delete_sponsor_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_delete_sponsor_portal_by_id_default(api, validator):
    try:
        assert is_valid_delete_sponsor_portal_by_id(
            validator,
            delete_sponsor_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sponsor_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_69aa24c1260a568b93c283ecd2c3510e_v3_0_0').validate(obj.response)
    return True


def get_sponsor_portal(api):
    endpoint_result = api.sponsor_portal.get_sponsor_portal(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_get_sponsor_portal(api, validator):
    try:
        assert is_valid_get_sponsor_portal(
            validator,
            get_sponsor_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sponsor_portal_default(api):
    endpoint_result = api.sponsor_portal.get_sponsor_portal(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_get_sponsor_portal_default(api, validator):
    try:
        assert is_valid_get_sponsor_portal(
            validator,
            get_sponsor_portal_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sponsor_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1f15d19b858d59218ab56b7323ca2fae_v3_0_0').validate(obj.response)
    return True


def create_sponsor_portal(api):
    endpoint_result = api.sponsor_portal.create_sponsor_portal(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'fqdn': 'string', 'authenticationMethod': 'string', 'idleTimeout': 0, 'displayLang': 'string', 'fallbackLanguage': 'string', 'availableSsids': ['string']}, 'loginPageSettings': {'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireAupScrolling': True, 'socialConfigs': []}, 'aupSettings': {'includeAup': True, 'requireScrolling': True, 'displayFrequency': 'string', 'displayFrequencyIntervalDays': 0}, 'sponsorChangePasswordSettings': {'allowSponsorToChangePwd': True}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_create_sponsor_portal(api, validator):
    try:
        assert is_valid_create_sponsor_portal(
            validator,
            create_sponsor_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_sponsor_portal_default(api):
    endpoint_result = api.sponsor_portal.create_sponsor_portal(
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


@pytest.mark.sponsor_portal
def test_create_sponsor_portal_default(api, validator):
    try:
        assert is_valid_create_sponsor_portal(
            validator,
            create_sponsor_portal_default(api)
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
    json_schema_validate('jsd_fa39b9cc4834522395edcbe0d6830ae4_v3_0_0').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.sponsor_portal.get_version(

    )
    return endpoint_result


@pytest.mark.sponsor_portal
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
    endpoint_result = api.sponsor_portal.get_version(

    )
    return endpoint_result


@pytest.mark.sponsor_portal
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
