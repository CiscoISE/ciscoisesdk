# -*- coding: utf-8 -*-
"""Identity Services Engine createNetworkdevice data model.

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


class JSONSchemaValidatorF9Ce55D5Dc7F53DfBcccC12E8Ae6Da63(object):
    """createNetworkdevice request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF9Ce55D5Dc7F53DfBcccC12E8Ae6Da63, self).__init__()
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
                "ipaddressExclude": {
                "type": "string"
                },
                "mask": {
                "type": "object"
                }
                }
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
                "type": "boolean"
                },
                "enabled": {
                "type": "boolean"
                },
                "keyEncryptionKey": {
                "type": "string"
                },
                "keyInputFormat": {
                "type": "object"
                },
                "messageAuthenticatorCodeKey": {
                "type": "string"
                },
                "networkProtocol": {
                "type": "object"
                },
                "radiusSharedSecret": {
                "type": "string"
                },
                "secondRadiusSharedSecret": {
                "type": "string"
                }
                },
                "required": [
                "enableKeyWrap",
                "enabled",
                "keyEncryptionKey",
                "keyInputFormat"
                ],
                "type": "object"
                },
                "coaPort": {
                "type": "number"
                },
                "description":
                 {
                "type": "string"
                },
                "dtlsDnsName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "modelName": {
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
                "authPassword": {
                "type": "string"
                },
                "authProtocol": {
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
                "type": "object"
                },
                "privacyPassword": {
                "type": "string"
                },
                "privacyProtocol": {
                "type": "string"
                },
                "roCommunity": {
                "type": "string"
                },
                "securityLevel": {
                "type": "string"
                },
                "username": {
                "type": "string"
                },
                "version": {
                "type": "string"
                }
                },
                "required": [
                "linkTrapQuery",
                "macTrapQuery",
                "originatingPolicyServicesNode",
                "pollingInterval",
                "version"
                ],
                "type": "object"
                },
                "softwareVersion": {
                "type": "string"
                },
                "tacacsSettings": {
                "properties": {
                "connectModeOptions": {
                "type": "object"
                },
                "previousSharedSecret": {
                "type": "string"
                },
                "previousSharedSecretExpiry": {
                "type": "object"
                },
                "sharedSecret": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "tacacsTlsSettings": {
                "properties": {
                "connectModeOptions": {
                "type": "object"
                },
                "enableSanIpValidation": {
                "type": "boolean"
                },
                "enableTls": {
                "type": "boolean"
                },
                "sanValues": {
                "properties": {
                "directoryNames": {
                "items": {},
                "type": "array"
                },
                "dnsNames": {
                "items": {},
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "required": [
                "enableTls"
                ],
                "type": "object"
                },
                "trustsecsettings": {
                "properties": {
                "deviceAuthenticationSettings": {
                "properties": {
                "restApiPassword": {
                "type": "string"
                },
                "restApiUsername": {
                "type": "string"
                },
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
                "execModeUsername": {
                "type": "string"
                },
                "includeWhenDeployingSGTUpdates": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "sgaNotificationAndUpdates": {
                "properties": {
                "coaSourceHost": {
                "type": "string"
                },
                "downlaodEnvironmentDataEveryXSeconds": {
                "type": "object"
                },
                "downlaodPeerAuthorizationPolicyEveryXSeconds": {
                "type": "object"
                },
                "downloadSGACLListsEveryXSeconds": {
                "type": "object"
                },
                "otherSGADevicesToTrustThisDevice": {
                "type": "object"
                },
                "reAuthenticationEveryXSeconds": {
                "type": "object"
                },
                "sendConfigurationToDevice": {
                "type": "object"
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
                "coaPort",
                "name",
                "profileName"
                ]
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
