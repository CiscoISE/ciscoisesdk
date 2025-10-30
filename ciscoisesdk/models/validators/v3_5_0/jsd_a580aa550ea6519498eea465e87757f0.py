# -*- coding: utf-8 -*-
"""Identity Services Engine updateMydeviceportalById data model.

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


class JSONSchemaValidatorA580Aa550Ea6519498EeA465E87757F0(object):
    """updateMydeviceportalById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA580Aa550Ea6519498EeA465E87757F0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "MyDevicePortal": {
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
                "required": [
                "name"
                ],
                "type": "object"
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
                }
                },
                "type": "object"
                },
                "employeeChangePasswordSettings": {
                "properties": {
                "allowEmployeeToChangePwd": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "loginPageSettings": {
                "properties": {
                "aupDisplay": {
                "type": "string"
                },
                "includeAup": {
                "type": "boolean"
                },
                "maxFailedAttemptsBeforeRateLimit": {
                "type": "number"
                },
                "requireAupAcceptance": {
                "type": "boolean"
                },
                "requireAupScrolling": {
                "type": "boolean"
                },
                "timeBetweenLoginsDuringRateLimit": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "portalSettings": {
                "properties": {
                "allowedInterfaces": {
                "type": "string"
                },
                "alwaysUsedLanguage": {
                "type": "string"
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
                "type": "number"
                }
                },
                "required": [
                "allowedInterfaces",
                "certificateGroupTag",
                "endpointIdentityGroup",
                "httpsPort"
                ],
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
                "required": [
                "name",
                "portalType"
                ]
                }
                },
                "required": [
                "MyDevicePortal"
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
