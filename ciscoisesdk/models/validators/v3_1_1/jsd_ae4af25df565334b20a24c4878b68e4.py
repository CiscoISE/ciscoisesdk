# -*- coding: utf-8 -*-
"""Identity Services Engine updateHotspotPortalById data model.

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


class JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4(object):
    """updateHotspotPortalById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4, self).__init__()
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
                "accessCode": {
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
