# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI sponsored_guest_portal API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1_Patch_1', reason='version does not match')


def is_valid_get_sponsored_guest_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_56d1132a216d54d091022aec0ad018f8_v3_1_patch_1').validate(obj.response)
    return True


def get_sponsored_guest_portal_by_id(api):
    endpoint_result = api.sponsored_guest_portal.get_sponsored_guest_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_get_sponsored_guest_portal_by_id(api, validator):
    try:
        assert is_valid_get_sponsored_guest_portal_by_id(
            validator,
            get_sponsored_guest_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sponsored_guest_portal_by_id_default(api):
    endpoint_result = api.sponsored_guest_portal.get_sponsored_guest_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_get_sponsored_guest_portal_by_id_default(api, validator):
    try:
        assert is_valid_get_sponsored_guest_portal_by_id(
            validator,
            get_sponsored_guest_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sponsored_guest_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_0d39172f68fd5cbd897f03f1440f98a4_v3_1_patch_1').validate(obj.response)
    return True


def update_sponsored_guest_portal_by_id(api):
    endpoint_result = api.sponsored_guest_portal.update_sponsored_guest_portal_by_id(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        id='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'authenticationMethod': 'string', 'assignedGuestTypeForEmployee': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'accessCode': 'string', 'allowGuestToCreateAccounts': True, 'allowForgotPassword': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'socialConfigs': [{'socialMediaType': 'string', 'socialMediaValue': 'string'}]}, 'aupSettings': {'includeAup': True, 'requireAupScrolling': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'displayFrequencyIntervalDays': 0, 'requireScrolling': True, 'displayFrequency': 'string'}, 'guestChangePasswordSettings': {'allowChangePasswdAtFirstLogin': True}, 'guestDeviceRegistrationSettings': {'autoRegisterGuestDevices': True, 'allowGuestsToRegisterDevices': True}, 'byodSettings': {'byodWelcomeSettings': {'enableBYOD': True, 'enableGuestAccess': True, 'requireMDM': True, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True}, 'byodRegistrationSettings': {'showDeviceID': True, 'endPointIdentityGroupId': 'string'}, 'byodRegistrationSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_update_sponsored_guest_portal_by_id(api, validator):
    try:
        assert is_valid_update_sponsored_guest_portal_by_id(
            validator,
            update_sponsored_guest_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_sponsored_guest_portal_by_id_default(api):
    endpoint_result = api.sponsored_guest_portal.update_sponsored_guest_portal_by_id(
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


@pytest.mark.sponsored_guest_portal
def test_update_sponsored_guest_portal_by_id_default(api, validator):
    try:
        assert is_valid_update_sponsored_guest_portal_by_id(
            validator,
            update_sponsored_guest_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sponsored_guest_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_9218749931f05e2ebc796f080892085f_v3_1_patch_1').validate(obj.response)
    return True


def delete_sponsored_guest_portal_by_id(api):
    endpoint_result = api.sponsored_guest_portal.delete_sponsored_guest_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_delete_sponsored_guest_portal_by_id(api, validator):
    try:
        assert is_valid_delete_sponsored_guest_portal_by_id(
            validator,
            delete_sponsored_guest_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_sponsored_guest_portal_by_id_default(api):
    endpoint_result = api.sponsored_guest_portal.delete_sponsored_guest_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_delete_sponsored_guest_portal_by_id_default(api, validator):
    try:
        assert is_valid_delete_sponsored_guest_portal_by_id(
            validator,
            delete_sponsored_guest_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sponsored_guest_portals(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_97886854bdae59219027b4d40b94fa3d_v3_1_patch_1').validate(obj.response)
    return True


def get_sponsored_guest_portals(api):
    endpoint_result = api.sponsored_guest_portal.get_sponsored_guest_portals(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_get_sponsored_guest_portals(api, validator):
    try:
        assert is_valid_get_sponsored_guest_portals(
            validator,
            get_sponsored_guest_portals(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_sponsored_guest_portals_default(api):
    endpoint_result = api.sponsored_guest_portal.get_sponsored_guest_portals(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_get_sponsored_guest_portals_default(api, validator):
    try:
        assert is_valid_get_sponsored_guest_portals(
            validator,
            get_sponsored_guest_portals_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sponsored_guest_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_ca78559d8a9f559c87f53ea85169a2c7_v3_1_patch_1').validate(obj.response)
    return True


def create_sponsored_guest_portal(api):
    endpoint_result = api.sponsored_guest_portal.create_sponsored_guest_portal(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'authenticationMethod': 'string', 'assignedGuestTypeForEmployee': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'accessCode': 'string', 'allowGuestToCreateAccounts': True, 'allowForgotPassword': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'socialConfigs': [{'socialMediaType': 'string', 'socialMediaValue': 'string'}]}, 'aupSettings': {'includeAup': True, 'requireAupScrolling': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'displayFrequencyIntervalDays': 0, 'requireScrolling': True, 'displayFrequency': 'string'}, 'guestChangePasswordSettings': {'allowChangePasswdAtFirstLogin': True}, 'guestDeviceRegistrationSettings': {'autoRegisterGuestDevices': True, 'allowGuestsToRegisterDevices': True}, 'byodSettings': {'byodWelcomeSettings': {'enableBYOD': True, 'enableGuestAccess': True, 'requireMDM': True, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True}, 'byodRegistrationSettings': {'showDeviceID': True, 'endPointIdentityGroupId': 'string'}, 'byodRegistrationSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_create_sponsored_guest_portal(api, validator):
    try:
        assert is_valid_create_sponsored_guest_portal(
            validator,
            create_sponsored_guest_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_sponsored_guest_portal_default(api):
    endpoint_result = api.sponsored_guest_portal.create_sponsored_guest_portal(
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


@pytest.mark.sponsored_guest_portal
def test_create_sponsored_guest_portal_default(api, validator):
    try:
        assert is_valid_create_sponsored_guest_portal(
            validator,
            create_sponsored_guest_portal_default(api)
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
    json_schema_validate('jsd_2f1aacc5c48654cebbc4d075dc7dde80_v3_1_patch_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.sponsored_guest_portal.get_version(

    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
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
    endpoint_result = api.sponsored_guest_portal.get_version(

    )
    return endpoint_result


@pytest.mark.sponsored_guest_portal
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
