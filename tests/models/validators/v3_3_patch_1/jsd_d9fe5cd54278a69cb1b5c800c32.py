# -*- coding: utf-8 -*-
"""Identity Services Engine getIpsecEnabledNodes data model.

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


import json
from builtins import *

import fastjsonschema
from ciscoisesdk.exceptions import MalformedRequest


class JSONSchemaValidatorD9FE5Cd54278A69Cb1B5C800C32(object):
    """getIpsecEnabledNodes request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD9FE5Cd54278A69Cb1B5C800C32, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "nextPage": {
                "properties": {
                "href": {
                "type": "string"
                },
                "rel": {
                "enum": [
                "next",
                "previous",
                "self",
                "status"
                ],
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "previousPage": {
                "properties": {
                "href": {
                "type": "string"
                },
                "rel": {
                "enum": [
                "next",
                "previous",
                "self",
                "status"
                ],
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "response": {
                "items": {
                "properties": {
                "authType": {
                "enum": [
                "psk",
                "x509"
                ],
                "type": "string"
                },
                "certId": {
                "type": "string"
                },
                "configureVti": {
                "type": "boolean"
                },
                "createTime": {
                "type": "string"
                },
                "espAhProtocol": {
                "enum": [
                "ah",
                "esp"
                ],
                "type": "string"
                },
                "hostName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "iface": {
                "type": "string"
                },
                "ikeReAuthTime": {
                "type": "integer"
                },
                "ikeVersion": {
                "enum": [
                "1",
                "2"
                ],
                "type": "string"
                },
                "localInternalIp": {
                "type": "string"
                },
                "modeOption": {
                "enum": [
                "transport",
                "tunnel"
                ],
                "type": "string"
                },
                "nadIp": {
                "type": "string"
                },
                "phaseOneDHGroup": {
                "enum": [
                "GROUP1",
                "GROUP14",
                "GROUP15",
                "GROUP16",
                "GROUP19",
                "GROUP2",
                "GROUP20",
                "GROUP21",
                "GROUP24",
                "GROUP5"
                ],
                "type": "string"
                },
                "phaseOneEncryptionAlgo": {
                "enum": [
                "3des",
                "aes",
                "aes128",
                "aes192",
                "aes256",
                "des"
                ],
                "type": "string"
                },
                "phaseOneHashAlgo": {
                "enum": [
                "sha",
                "sha256",
                "sha384",
                "sha512"
                ],
                "type": "string"
                },
                "phaseOneLifeTime": {
                "type": "integer"
                },
                "phaseTwoDHGroup": {
                "enum": [
                "GROUP1",
                "GROUP14",
                "GROUP15",
                "GROUP16",
                "GROUP19",
                "GROUP2",
                "GROUP20",
                "GROUP21",
                "GROUP24",
                "GROUP5",
                "NONE"
                ],
                "type": "string"
                },
                "phaseTwoEncryptionAlgo": {
                "enum": [
                "3des",
                "aes",
                "aes128",
                "aes192",
                "aes256",
                "des",
                "gcm",
                "gmac"
                ],
                "type": "string"
                },
                "phaseTwoHashAlgo": {
                "enum": [
                "sha",
                "sha256",
                "sha384",
                "sha512"
                ],
                "type": "string"
                },
                "phaseTwoLifeTime": {
                "type": "integer"
                },
                "psk": {
                "type": "string"
                },
                "remotePeerInternalIp": {
                "type": "string"
                },
                "status": {
                "enum": [
                "ESTABLISHED",
                "IN_PROGRESS",
                "NOT_ESTABLISHED"
                ],
                "type": "string"
                },
                "updateTime": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
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
