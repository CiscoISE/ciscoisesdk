# -*- coding: utf-8 -*-
"""Identity Services Engine createSponsoredGuestPortal data model.

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


class JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7(object):
    """createSponsoredGuestPortal request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "SponsoredGuestPortal": {
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
                "name"
                ],
                "type": "object"
                }
                },
                "required": [
                "SponsoredGuestPortal"
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
