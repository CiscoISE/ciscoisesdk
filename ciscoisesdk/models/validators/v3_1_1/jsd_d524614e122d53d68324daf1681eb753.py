# -*- coding: utf-8 -*-
"""Identity Services Engine createSelfRegisteredPortal data model.

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


from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema
from ciscoisesdk.exceptions import MalformedRequest


class JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753(object):
    """createSelfRegisteredPortal request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "SelfRegPortal": {
                "properties": {
                "customizations": {
                "properties": {
                "globalCustomizations": {
                "properties": {
                "backgroundImage": {
                "properties": {
                "data": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "bannerImage": {
                "properties": {
                "data": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "bannerTitle": {
                "type": "string"
                },
                "contactText": {
                "type": "string"
                },
                "desktopLogoImage": {
                "properties": {
                "data": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "footerElement": {
                "type": "string"
                },
                "mobileLogoImage": {
                "properties": {
                "data": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "language": {
                "properties": {
                "viewLanguage": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "pageCustomizations": {
                "properties": {
                "data": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "portalTheme": {
                "properties": {
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "themeData": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "portalTweakSettings": {
                "properties": {
                "bannerColor": {
                "type": "string"
                },
                "bannerTextColor": {
                "type": "string"
                },
                "pageBackgroundColor": {
                "type": "string"
                },
                "pageLabelAndTextColor": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "portalTestUrl": {
                "type": "string"
                },
                "portalType": {
                "type": "string"
                },
                "settings": {
                "properties": {
                "aupSettings": {
                "properties": {
                "displayFrequency": {
                "type": "string"
                },
                "displayFrequencyIntervalDays": {
                "type": "integer"
                },
                "includeAup": {
                "type": "boolean"
                },
                "requireAupScrolling": {
                "type": "boolean"
                },
                "requireScrolling": {
                "type": "boolean"
                },
                "skipAupForEmployees": {
                "type": "boolean"
                },
                "useDiffAupForEmployees": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "authSuccessSettings": {
                "properties": {
                "redirectUrl": {
                "type": "string"
                },
                "successRedirect": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "byodSettings": {
                "properties": {
                "byodRegistrationSettings": {
                "properties": {
                "endPointIdentityGroupId": {
                "type": "string"
                },
                "showDeviceID": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "byodRegistrationSuccessSettings": {
                "properties": {
                "redirectUrl": {
                "type": "string"
                },
                "successRedirect": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "byodWelcomeSettings": {
                "properties": {
                "aupDisplay": {
                "type": "string"
                },
                "enableBYOD": {
                "type": "boolean"
                },
                "enableGuestAccess": {
                "type": "boolean"
                },
                "includeAup": {
                "type": "boolean"
                },
                "requireAupAcceptance": {
                "type": "boolean"
                },
                "requireMDM": {
                "type": "boolean"
                },
                "requireScrolling": {
                "type": "boolean"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "guestChangePasswordSettings": {
                "properties": {
                "allowChangePasswdAtFirstLogin": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "guestDeviceRegistrationSettings": {
                "properties": {
                "allowGuestsToRegisterDevices": {
                "type": "boolean"
                },
                "autoRegisterGuestDevices": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "loginPageSettings": {
                "properties": {
                "accessCode": {
                "type": "string"
                },
                "allowAlternateGuestPortal": {
                "type": "boolean"
                },
                "allowForgotPassword": {
                "type": "boolean"
                },
                "allowGuestToChangePassword": {
                "type": "boolean"
                },
                "allowGuestToCreateAccounts": {
                "type": "boolean"
                },
                "allowGuestToUseSocialAccounts": {
                "type": "boolean"
                },
                "allowShowGuestForm": {
                "type": "boolean"
                },
                "alternateGuestPortal": {
                "type": "string"
                },
                "aupDisplay": {
                "type": "string"
                },
                "includeAup": {
                "type": "boolean"
                },
                "maxFailedAttemptsBeforeRateLimit": {
                "type": "integer"
                },
                "requireAccessCode": {
                "type": "boolean"
                },
                "requireAupAcceptance": {
                "type": "boolean"
                },
                "socialConfigs": {
                "items": {
                "properties": {
                "socialMediaType": {
                "type": "string"
                },
                "socialMediaValue": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "timeBetweenLoginsDuringRateLimit": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "portalSettings": {
                "properties": {
                "allowedInterfaces": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "alwaysUsedLanguage": {
                "type": "string"
                },
                "assignedGuestTypeForEmployee": {
                "type": "string"
                },
                "authenticationMethod": {
                "type": "string"
                },
                "certificateGroupTag": {
                "type": "string"
                },
                "displayLang": {
                "type": "string"
                },
                "fallbackLanguage": {
                "type": "string"
                },
                "httpsPort": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "postAccessBannerSettings": {
                "properties": {
                "includePostAccessBanner": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "postLoginBannerSettings": {
                "properties": {
                "includePostAccessBanner": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "selfRegPageSettings": {
                "properties": {
                "accountValidityDuration": {
                "type": "integer"
                },
                "accountValidityTimeUnits": {
                "type": "string"
                },
                "allowGraceAccess": {
                "type": "boolean"
                },
                "approvalEmailAddresses": {
                "type": "string"
                },
                "approveDenyLinksTimeUnits": {
                "type": "string"
                },
                "approveDenyLinksValidFor": {
                "type": "integer"
                },
                "assignGuestsToGuestType": {
                "type": "string"
                },
                "aupDisplay": {
                "type": "string"
                },
                "authenticateSponsorsUsingPortalList": {
                "type": "boolean"
                },
                "autoLoginSelfWait": {
                "type": "boolean"
                },
                "autoLoginTimePeriod": {
                "type": "integer"
                },
                "credentialNotificationUsingEmail": {
                "type": "boolean"
                },
                "credentialNotificationUsingSms": {
                "type": "boolean"
                },
                "enableGuestEmailBlacklist": {
                "type": "boolean"
                },
                "enableGuestEmailWhitelist": {
                "type": "boolean"
                },
                "fieldCompany": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldEmailAddr": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldFirstName": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldLastName": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldLocation": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldPersonBeingVisited": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldPhoneNo": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldReasonForVisit": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldSmsProvider": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "fieldUserName": {
                "properties": {
                "include": {
                "type": "boolean"
                },
                "require": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "graceAccessExpireInterval": {
                "type": "integer"
                },
                "graceAccessSendAccountExpiration": {
                "type": "boolean"
                },
                "guestEmailBlacklistDomains": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "guestEmailWhitelistDomains": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "includeAup": {
                "type": "boolean"
                },
                "postRegistrationRedirect": {
                "enum": [
                "SELFREGISTRATIONSUCCESS",
                "LOGINPAGEWITHINSTRUCTIONS",
                "URL"
                ],
                "type": "string"
                },
                "postRegistrationRedirectUrl": {
                "type": "string"
                },
                "registrationCode": {
                "type": "string"
                },
                "requireApproverToAuthenticate": {
                "type": "boolean"
                },
                "requireAupAcceptance": {
                "type": "boolean"
                },
                "requireGuestApproval": {
                "type": "boolean"
                },
                "requireRegistrationCode": {
                "type": "boolean"
                },
                "selectableLocations": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "selectableSmsProviders": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sendApprovalRequestTo": {
                "type": "string"
                },
                "sponsorPortalList": {
                "items": {},
                "type": "array"
                }
                },
                "type": "object"
                },
                "selfRegSuccessSettings": {
                "properties": {
                "allowGuestLoginFromSelfregSuccessPage": {
                "type": "boolean"
                },
                "allowGuestSendSelfUsingEmail": {
                "type": "boolean"
                },
                "allowGuestSendSelfUsingPrint": {
                "type": "boolean"
                },
                "allowGuestSendSelfUsingSms": {
                "type": "boolean"
                },
                "aupOnPage": {
                "type": "boolean"
                },
                "includeAup": {
                "type": "boolean"
                },
                "includeCompany": {
                "type": "boolean"
                },
                "includeEmailAddr": {
                "type": "boolean"
                },
                "includeFirstName": {
                "type": "boolean"
                },
                "includeLastName": {
                "type": "boolean"
                },
                "includeLocation": {
                "type": "boolean"
                },
                "includePassword": {
                "type": "boolean"
                },
                "includePersonBeingVisited": {
                "type": "boolean"
                },
                "includePhoneNo": {
                "type": "boolean"
                },
                "includeReasonForVisit": {
                "type": "boolean"
                },
                "includeSmsProvider": {
                "type": "boolean"
                },
                "includeUserName": {
                "type": "boolean"
                },
                "requireAupAcceptance": {
                "type": "boolean"
                },
                "requireAupScrolling": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "supportInfoSettings": {
                "properties": {
                "defaultEmptyFieldValue": {
                "type": "string"
                },
                "emptyFieldDisplay": {
                "type": "string"
                },
                "includeBrowserUserAgent": {
                "type": "boolean"
                },
                "includeFailureCode": {
                "type": "boolean"
                },
                "includeIpAddress": {
                "type": "boolean"
                },
                "includeMacAddr": {
                "type": "boolean"
                },
                "includePolicyServer": {
                "type": "boolean"
                },
                "includeSupportInfoPage": {
                "type": "boolean"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
