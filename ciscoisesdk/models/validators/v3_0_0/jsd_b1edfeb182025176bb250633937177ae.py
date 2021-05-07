# -*- coding: utf-8 -*-
"""Identity Services Engine updateNetworkDeviceById data model.

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


class JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae(object):
    """updateNetworkDeviceById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "NetworkDevice": {
                "properties": {
                "NetworkDeviceGroupList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "NetworkDeviceIPList": {
                "items": {
                "properties": {
                "ipaddress": {
                "type": "string"
                },
                "mask": {
                "type": "integer"
                }
                },
                "required": [
                "ipaddress",
                "mask"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "authenticationSettings": {
                "properties": {
                "dtlsRequired": {
                "type": "boolean"
                },
                "enableKeyWrap": {
                "type": "boolean"
                },
                "enableMultiSecret": {
                "type": "string"
                },
                "keyEncryptionKey": {
                "type": "string"
                },
                "keyInputFormat": {
                "type": "string"
                },
                "messageAuthenticatorCodeKey": {
                "type": "string"
                },
                "networkProtocol": {
                "type": "string"
                },
                "radiusSharedSecret": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "coaPort": {
                "type": "integer"
                },
                "description":
                 {
                "type": "string"
                },
                "dtlsDnsName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "profileName": {
                "type": "string"
                },
                "snmpsettings": {
                "properties": {
                "authPassowrd": {
                "type": "string"
                },
                "linkTrapQuery": {
                "type": "boolean"
                },
                "macTrapQuery": {
                "type": "boolean"
                },
                "originatingPolicyServicesNode": {
                "type": "string"
                },
                "pollingInterval": {
                "type": "integer"
                },
                "privacyPassowrd": {
                "type": "string"
                },
                "roCommunity": {
                "type": "string"
                },
                "version": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "tacacsSettings": {
                "properties": {
                "connectModeOptions": {
                "type": "string"
                },
                "sharedSecret": {
                "type": "string"
                }
                },
                "required": [
                "sharedSecret",
                "connectModeOptions"
                ],
                "type": "object"
                },
                "trustsecsettings": {
                "properties": {
                "deviceAuthenticationSettings": {
                "properties": {
                "sgaDeviceId": {
                "type": "string"
                },
                "sgaDevicePassword": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "deviceConfigurationDeployment": {
                "properties": {
                "enableModePassword": {
                "type": "string"
                },
                "execModePassword": {
                "type": "string"
                },
                "includeWhenDeployingSGTUpdates": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "pushIdSupport": {
                "type": "string"
                },
                "sgaNotificationAndUpdates": {
                "properties": {
                "coaSourceHost": {
                "type": "string"
                },
                "downlaodEnvironmentDataEveryXSeconds": {
                "type": "integer"
                },
                "downlaodPeerAuthorizationPolicyEveryXSeconds": {
                "type": "integer"
                },
                "downloadSGACLListsEveryXSeconds": {
                "type": "integer"
                },
                "otherSGADevicesToTrustThisDevice": {
                "type": "boolean"
                },
                "reAuthenticationEveryXSeconds": {
                "type": "integer"
                },
                "sendConfigurationToDevice": {
                "type": "boolean"
                },
                "sendConfigurationToDeviceUsing": {
                "type": "string"
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
                "NetworkDeviceIPList"
                ],
                "type": "object"
                }
                },
                "required": [
                "NetworkDevice"
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
