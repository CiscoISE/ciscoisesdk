# -*- coding: utf-8 -*-
"""Identity Services Engine createHotspotPortal data model.

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


class JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F(object):
    """createHotspotPortal request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "HotspotPortal": {
                "properties": {
                "customizations": {
                "properties": {
                "globalCustomizations": {
                "properties": {
                "bannerTitle": {
                "type": "string"
                },
                "contactText": {
                "type": "string"
                },
                "footerElement": {
                "type": "string"
                }
                },
                "required": [
                "bannerTitle",
                "contactText",
                "footerElement"
                ],
                "type": "object"
                },
                "language": {
                "properties": {
                "viewLanguage": {
                "type": "string"
                }
                },
                "required": [
                "viewLanguage"
                ],
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
                "required": [
                "key",
                "value"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "data"
                ],
                "type": "object"
                },
                "portalTheme": {
                "properties": {
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "required": [
                "id",
                "name"
                ],
                "type": "object"
                }
                },
                "required": [
                "portalTheme",
                "language",
                "globalCustomizations",
                "pageCustomizations"
                ],
                "type": "object"
                },
                "description":
                 {
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
                "includeAup": {
                "type": "boolean"
                },
                "requireScrolling": {
                "type": "boolean"
                }
                },
                "required": [
                "includeAup",
                "requireScrolling"
                ],
                "type": "object"
                },
                "authSuccessSettings": {
                "properties": {
                "successRedirect": {
                "type": "string"
                }
                },
                "required": [
                "successRedirect"
                ],
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
                "certificateGroupTag": {
                "type": "string"
                },
                "coaType": {
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
                "required": [
                "httpsPort",
                "allowedInterfaces",
                "certificateGroupTag",
                "endpointIdentityGroup",
                "coaType",
                "displayLang",
                "fallbackLanguage",
                "alwaysUsedLanguage"
                ],
                "type": "object"
                },
                "postAccessBannerSettings": {
                "properties": {
                "includePostAccessBanner": {
                "type": "boolean"
                }
                },
                "required": [
                "includePostAccessBanner"
                ],
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
                "required": [
                "includeSupportInfoPage",
                "includeMacAddr",
                "includeIpAddress",
                "includeBrowserUserAgent",
                "includePolicyServer",
                "includeFailureCode",
                "emptyFieldDisplay"
                ],
                "type": "object"
                }
                },
                "required": [
                "portalSettings",
                "aupSettings",
                "postAccessBannerSettings",
                "authSuccessSettings",
                "supportInfoSettings"
                ],
                "type": "object"
                }
                },
                "required": [
                "name",
                "description",
                "portalType",
                "settings",
                "customizations"
                ],
                "type": "object"
                }
                },
                "required": [
                "HotspotPortal"
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
