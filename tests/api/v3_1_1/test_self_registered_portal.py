# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI self_registered_portal API fixtures and tests.

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


def is_valid_get_self_registered_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_f9c9a5e917af53dbbb91733e82e72ebe_v3_1_1').validate(obj.response)
    return True


def get_self_registered_portal_by_id(api):
    endpoint_result = api.self_registered_portal.get_self_registered_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_get_self_registered_portal_by_id(api, validator):
    try:
        assert is_valid_get_self_registered_portal_by_id(
            validator,
            get_self_registered_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_self_registered_portal_by_id_default(api):
    endpoint_result = api.self_registered_portal.get_self_registered_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_get_self_registered_portal_by_id_default(api, validator):
    try:
        assert is_valid_get_self_registered_portal_by_id(
            validator,
            get_self_registered_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_self_registered_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_400c4fada6c558d9aba09cc373d5b266_v3_1_1').validate(obj.response)
    return True


def update_self_registered_portal_by_id(api):
    endpoint_result = api.self_registered_portal.update_self_registered_portal_by_id(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        id='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'authenticationMethod': 'string', 'assignedGuestTypeForEmployee': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'accessCode': 'string', 'allowGuestToCreateAccounts': True, 'allowForgotPassword': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'alternateGuestPortal': 'string', 'allowGuestToUseSocialAccounts': True, 'allowShowGuestForm': True, 'socialConfigs': [{'socialMediaType': 'string', 'socialMediaValue': 'string'}]}, 'selfRegPageSettings': {'assignGuestsToGuestType': 'string', 'accountValidityDuration': 0, 'accountValidityTimeUnits': 'string', 'requireRegistrationCode': True, 'registrationCode': 'string', 'fieldUserName': {'include': True, 'require': True}, 'fieldFirstName': {'include': True, 'require': True}, 'fieldLastName': {'include': True, 'require': True}, 'fieldEmailAddr': {'include': True, 'require': True}, 'fieldPhoneNo': {'include': True, 'require': True}, 'fieldCompany': {'include': True, 'require': True}, 'fieldLocation': {'include': True, 'require': True}, 'selectableLocations': ['string'], 'fieldSmsProvider': {'include': True, 'require': True}, 'selectableSmsProviders': ['string'], 'fieldPersonBeingVisited': {'include': True, 'require': True}, 'fieldReasonForVisit': {'include': True, 'require': True}, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'enableGuestEmailWhitelist': True, 'guestEmailWhitelistDomains': ['string'], 'enableGuestEmailBlacklist': True, 'guestEmailBlacklistDomains': ['string'], 'requireGuestApproval': True, 'autoLoginSelfWait': True, 'autoLoginTimePeriod': 0, 'allowGraceAccess': True, 'graceAccessExpireInterval': 0, 'graceAccessSendAccountExpiration': True, 'sendApprovalRequestTo': 'string', 'approvalEmailAddresses': 'string', 'postRegistrationRedirect': 'string', 'postRegistrationRedirectUrl': 'string', 'credentialNotificationUsingEmail': True, 'credentialNotificationUsingSms': True, 'approveDenyLinksValidFor': 0, 'approveDenyLinksTimeUnits': 'string', 'requireApproverToAuthenticate': True, 'authenticateSponsorsUsingPortalList': True, 'sponsorPortalList': []}, 'selfRegSuccessSettings': {'includeUserName': True, 'includePassword': True, 'includeFirstName': True, 'includeLastName': True, 'includeEmailAddr': True, 'includePhoneNo': True, 'includeCompany': True, 'includeLocation': True, 'includeSmsProvider': True, 'includePersonBeingVisited': True, 'includeReasonForVisit': True, 'allowGuestSendSelfUsingPrint': True, 'allowGuestSendSelfUsingEmail': True, 'allowGuestSendSelfUsingSms': True, 'includeAup': True, 'aupOnPage': True, 'requireAupAcceptance': True, 'requireAupScrolling': True, 'allowGuestLoginFromSelfregSuccessPage': True}, 'aupSettings': {'includeAup': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'requireScrolling': True, 'requireAupScrolling': True, 'displayFrequency': 'string', 'displayFrequencyIntervalDays': 0}, 'guestChangePasswordSettings': {'allowChangePasswdAtFirstLogin': True}, 'guestDeviceRegistrationSettings': {'autoRegisterGuestDevices': True, 'allowGuestsToRegisterDevices': True}, 'byodSettings': {'byodWelcomeSettings': {'enableBYOD': True, 'enableGuestAccess': True, 'requireMDM': True, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True}, 'byodRegistrationSettings': {'showDeviceID': True, 'endPointIdentityGroupId': 'string'}, 'byodRegistrationSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_update_self_registered_portal_by_id(api, validator):
    try:
        assert is_valid_update_self_registered_portal_by_id(
            validator,
            update_self_registered_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_self_registered_portal_by_id_default(api):
    endpoint_result = api.self_registered_portal.update_self_registered_portal_by_id(
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


@pytest.mark.self_registered_portal
def test_update_self_registered_portal_by_id_default(api, validator):
    try:
        assert is_valid_update_self_registered_portal_by_id(
            validator,
            update_self_registered_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_self_registered_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_673f9ada2e275fa2934fdb4825266a2c_v3_1_1').validate(obj.response)
    return True


def delete_self_registered_portal_by_id(api):
    endpoint_result = api.self_registered_portal.delete_self_registered_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_delete_self_registered_portal_by_id(api, validator):
    try:
        assert is_valid_delete_self_registered_portal_by_id(
            validator,
            delete_self_registered_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_self_registered_portal_by_id_default(api):
    endpoint_result = api.self_registered_portal.delete_self_registered_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_delete_self_registered_portal_by_id_default(api, validator):
    try:
        assert is_valid_delete_self_registered_portal_by_id(
            validator,
            delete_self_registered_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_self_registered_portals(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bb165bd00a6653ac9da440f23ee62ecc_v3_1_1').validate(obj.response)
    return True


def get_self_registered_portals(api):
    endpoint_result = api.self_registered_portal.get_self_registered_portals(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_get_self_registered_portals(api, validator):
    try:
        assert is_valid_get_self_registered_portals(
            validator,
            get_self_registered_portals(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_self_registered_portals_default(api):
    endpoint_result = api.self_registered_portal.get_self_registered_portals(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_get_self_registered_portals_default(api, validator):
    try:
        assert is_valid_get_self_registered_portals(
            validator,
            get_self_registered_portals_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_self_registered_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_d524614e122d53d68324daf1681eb753_v3_1_1').validate(obj.response)
    return True


def create_self_registered_portal(api):
    endpoint_result = api.self_registered_portal.create_self_registered_portal(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'backgroundImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        name='string',
        payload=None,
        portal_test_url='string',
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'authenticationMethod': 'string', 'assignedGuestTypeForEmployee': 'string', 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string'}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'accessCode': 'string', 'allowGuestToCreateAccounts': True, 'allowForgotPassword': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'alternateGuestPortal': 'string', 'allowGuestToUseSocialAccounts': True, 'allowShowGuestForm': True, 'socialConfigs': [{'socialMediaType': 'string', 'socialMediaValue': 'string'}]}, 'selfRegPageSettings': {'assignGuestsToGuestType': 'string', 'accountValidityDuration': 0, 'accountValidityTimeUnits': 'string', 'requireRegistrationCode': True, 'registrationCode': 'string', 'fieldUserName': {'include': True, 'require': True}, 'fieldFirstName': {'include': True, 'require': True}, 'fieldLastName': {'include': True, 'require': True}, 'fieldEmailAddr': {'include': True, 'require': True}, 'fieldPhoneNo': {'include': True, 'require': True}, 'fieldCompany': {'include': True, 'require': True}, 'fieldLocation': {'include': True, 'require': True}, 'selectableLocations': ['string'], 'fieldSmsProvider': {'include': True, 'require': True}, 'selectableSmsProviders': ['string'], 'fieldPersonBeingVisited': {'include': True, 'require': True}, 'fieldReasonForVisit': {'include': True, 'require': True}, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'enableGuestEmailWhitelist': True, 'guestEmailWhitelistDomains': ['string'], 'enableGuestEmailBlacklist': True, 'guestEmailBlacklistDomains': ['string'], 'requireGuestApproval': True, 'autoLoginSelfWait': True, 'autoLoginTimePeriod': 0, 'allowGraceAccess': True, 'graceAccessExpireInterval': 0, 'graceAccessSendAccountExpiration': True, 'sendApprovalRequestTo': 'string', 'approvalEmailAddresses': 'string', 'postRegistrationRedirect': 'string', 'postRegistrationRedirectUrl': 'string', 'credentialNotificationUsingEmail': True, 'credentialNotificationUsingSms': True, 'approveDenyLinksValidFor': 0, 'approveDenyLinksTimeUnits': 'string', 'requireApproverToAuthenticate': True, 'authenticateSponsorsUsingPortalList': True, 'sponsorPortalList': []}, 'selfRegSuccessSettings': {'includeUserName': True, 'includePassword': True, 'includeFirstName': True, 'includeLastName': True, 'includeEmailAddr': True, 'includePhoneNo': True, 'includeCompany': True, 'includeLocation': True, 'includeSmsProvider': True, 'includePersonBeingVisited': True, 'includeReasonForVisit': True, 'allowGuestSendSelfUsingPrint': True, 'allowGuestSendSelfUsingEmail': True, 'allowGuestSendSelfUsingSms': True, 'includeAup': True, 'aupOnPage': True, 'requireAupAcceptance': True, 'requireAupScrolling': True, 'allowGuestLoginFromSelfregSuccessPage': True}, 'aupSettings': {'includeAup': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'requireScrolling': True, 'requireAupScrolling': True, 'displayFrequency': 'string', 'displayFrequencyIntervalDays': 0}, 'guestChangePasswordSettings': {'allowChangePasswdAtFirstLogin': True}, 'guestDeviceRegistrationSettings': {'autoRegisterGuestDevices': True, 'allowGuestsToRegisterDevices': True}, 'byodSettings': {'byodWelcomeSettings': {'enableBYOD': True, 'enableGuestAccess': True, 'requireMDM': True, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireScrolling': True}, 'byodRegistrationSettings': {'showDeviceID': True, 'endPointIdentityGroupId': 'string'}, 'byodRegistrationSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'postAccessBannerSettings': {'includePostAccessBanner': True}, 'authSuccessSettings': {'successRedirect': 'string', 'redirectUrl': 'string'}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string', 'defaultEmptyFieldValue': 'string'}}
    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_create_self_registered_portal(api, validator):
    try:
        assert is_valid_create_self_registered_portal(
            validator,
            create_self_registered_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def create_self_registered_portal_default(api):
    endpoint_result = api.self_registered_portal.create_self_registered_portal(
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


@pytest.mark.self_registered_portal
def test_create_self_registered_portal_default(api, validator):
    try:
        assert is_valid_create_self_registered_portal(
            validator,
            create_self_registered_portal_default(api)
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
    json_schema_validate('jsd_3d8cc0e6962558c58d263f53b857cff0_v3_1_1').validate(obj.response)
    return True


def get_version(api):
    endpoint_result = api.self_registered_portal.get_version(

    )
    return endpoint_result


@pytest.mark.self_registered_portal
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
    endpoint_result = api.self_registered_portal.get_version(

    )
    return endpoint_result


@pytest.mark.self_registered_portal
def test_get_version_default(api, validator):
    try:
        assert is_valid_get_version(
            validator,
            get_version_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
