# -*- coding: utf-8 -*-
"""Identity Services Engine updateSelfRegisteredPortalById data model.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from ciscoisesdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266(object):
    """updateSelfRegisteredPortalById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266, self).__init__()
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
                "id": {
                "type": "string"
                },
                "name": {
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
                "includeAup": {
                "type": "boolean"
                },
                "requireAccessCode": {
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
                "requireAupScrolling": {
                "type": "boolean"
                },
                "socialConfigs": {
                "items": {},
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
                "availableSsids": {
                "items": {},
                "type": "array"
                },
                "certificateGroupTag": {
                "type": "string"
                },
                "displayLang": {
                "type": "string"
                },
                "endpointIdentityGroup": {
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
                "approveDenyLinksTimeUnits": {
                "type": "string"
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
                "type": "string"
                },
                "registrationCode": {
                "type": "string"
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
                "required": [
                "name",
                "portalType"
                ],
                "type": "object"
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
