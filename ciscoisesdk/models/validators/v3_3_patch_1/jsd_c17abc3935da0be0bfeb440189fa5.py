# -*- coding: utf-8 -*-
"""Identity Services Engine patchSelfregportalPortalid data model.

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


class JSONSchemaValidatorC17AbC3935Da0Be0BFeb440189Fa5(object):
    """patchSelfregportalPortalid request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC17AbC3935Da0Be0BFeb440189Fa5, self).__init__()
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
                }
                },
                "bannerImage": {
                "properties": {
                "data": {
                "type": "string"
                }
                }
                },
                "bannerTitle": {
                "type": "string"
                },
                "contactText": {
                "type": "string"
                },
                "footerElement": {
                "type": "string"
                },
                "mobileLogoImage": {
                "properties": {
                "data": {
                "type": "string"
                }
                }
                }
                }
                },
                "language": {
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
                }
                },
                "type": "array"
                }
                }
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
                }
                },
                "portalTweakSettings": {
                "properties": {
                "banneColor": {
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
                }
                }
                }
                },
                "description":
                 {
                "type": "string"
                },
                "id": {
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
                "type": "number"
                },
                "includeAup": {
                "type": "boolean"
                },
                "requireAupScrolling": {
                "type": "boolean"
                },
                "skipAupForEmployees": {
                "type": "boolean"
                },
                "useDiffAupForEmployees": {
                "type": "boolean"
                }
                }
                },
                "authSuccessSettings": {
                "properties": {
                "redirectUrl": {
                "type": "string"
                },
                "successRedirect": {
                "type": "string"
                }
                }
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
                }
                },
                "byodRegistrationSuccessSettings": {
                "properties": {
                "redirectUrl": {
                "type": "string"
                },
                "successRedirect": {
                "type": "string"
                }
                }
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
                }
                }
                }
                },
                "guestChangePasswordSettings": {
                "properties": {
                "allowChangePasswdAtFirstLogin": {
                "type": "boolean"
                }
                }
                },
                "guestDeviceRegistrationSettings": {
                "properties": {
                "allowGuestsToRegisterDevices": {
                "type": "boolean"
                },
                "autoRegisterGuestDevices": {
                "type": "boolean"
                }
                }
                },
                "loginPageSettings": {
                "properties": {
                "accessCode": {
                "type": "string"
                },
                "allowAlternateGuestPortal": {
                "type": "boolean"
                },
                "allowGuestToChangePassword": {
                "type": "boolean"
                },
                "allowGuestToCreateAccounts": {
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
                "type": "number"
                },
                "requireAccessCode": {
                "type": "boolean"
                },
                "requireAupAcceptance": {
                "type": "boolean"
                },
                "timeBetweenLoginsDuringRateLimit": {
                "type": "number"
                }
                }
                },
                "portalSettings": {
                "properties": {
                "allowedInterfaces": {
                "type": "string"
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
                "type": "number"
                }
                }
                },
                "postLoginBannerSettings": {
                "properties": {
                "includePostAccessBanner": {
                "type": "boolean"
                }
                }
                },
                "selfRegPageSettings": {
                "properties": {
                "accountValidityDuration": {
                "type": "number"
                },
                "accountValidityTimeUnits": {
                "type": "string"
                },
                "approvalEmailAddresses": {
                "type": "string"
                },
                "approveDenyLinksTimeUnits": {
                "type": "string"
                },
                "approveDenyLinksValidFor": {
                "type": "number"
                },
                "assignGuestsToGuestType": {
                "type": "string"
                },
                "aupDisplay": {
                "type": "string"
                },
                "autoLoginSelfWait": {
                "type": "boolean"
                },
                "autoLoginTimePeriod": {
                "type": "object"
                },
                "credentialNotificationUsingEmail": {
                "type": "boolean"
                },
                "credentialNotificationUsingSms": {
                "type": "boolean"
                },
                "enableGuestEmailAllowlist": {
                "type": "boolean"
                },
                "enableGuestEmailBlocklist": {
                "type": "boolean"
                },
                "fieldCompany": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldEmailAddr": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldFirstName": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldLastName": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldLocation": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldPersonBeingVisited": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldPhoneNo": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldReasonForVisit": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldSmsProvider": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "fieldUserName": {
                "properties": {
                "displayFrequency": {
                "type": "boolean"
                },
                "include": {
                "type": "boolean"
                }
                }
                },
                "guestEmailAllowlistDomains": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "guestEmailBlocklistDomains": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "includeAup": {
                "type": "boolean"
                },
                "postRegistrationRedirect": {
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
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                }
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
                }
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
                }
                }
                }
                }
                }
                }
                },
                "required": [
                "SelfRegPortal"
                ],
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
