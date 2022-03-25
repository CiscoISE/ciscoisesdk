# -*- coding: utf-8 -*-
"""Identity Services Engine updateAuthorizationProfileById data model.

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


class JSONSchemaValidatorCb9F26E93655E7D89995B172F6Fd97F(object):
    """updateAuthorizationProfileById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorCb9F26E93655E7D89995B172F6Fd97F, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "AuthorizationProfile": {
                "properties": {
                "accessType": {
                "type": "string"
                },
                "acl": {
                "type": "string"
                },
                "advancedAttributes": {
                "items": {
                "properties": {
                "leftHandSideDictionaryAttribue": {
                "properties": {
                "AdvancedAttributeValueType": {
                "enum": [
                "AttributeValue",
                "AdvancedDictionaryAttribute"
                ],
                "type": "string"
                },
                "attributeName": {
                "type": "string"
                },
                "dictionaryName": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "rightHandSideAttribueValue": {
                "properties": {
                "AdvancedAttributeValueType": {
                "enum": [
                "AttributeValue",
                "AdvancedDictionaryAttribute"
                ],
                "type": "string"
                },
                "attributeName": {
                "type": "string"
                },
                "dictionaryName": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "agentlessPosture": {
                "type": "boolean"
                },
                "airespaceACL": {
                "type": "string"
                },
                "airespaceIPv6ACL": {
                "type": "string"
                },
                "asaVpn": {
                "type": "string"
                },
                "authzProfileType": {
                "type": "string"
                },
                "autoSmartPort": {
                "type": "string"
                },
                "avcProfile": {
                "type": "string"
                },
                "daclName": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "easywiredSessionCandidate": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "interfaceTemplate": {
                "type": "string"
                },
                "ipv6ACLFilter": {
                "type": "string"
                },
                "ipv6DaclName": {
                "type": "string"
                },
                "macSecPolicy": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "neat": {
                "type": "boolean"
                },
                "profileName": {
                "type": "string"
                },
                "reauth": {
                "properties": {
                "connectivity": {
                "type": "string"
                },
                "timer": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "serviceTemplate": {
                "type": "boolean"
                },
                "trackMovement": {
                "type": "boolean"
                },
                "vlan": {
                "properties": {
                "nameID": {
                "type": "string"
                },
                "tagID": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "voiceDomainPermission": {
                "type": "boolean"
                },
                "webAuth": {
                "type": "boolean"
                },
                "webRedirection": {
                "properties": {
                "WebRedirectionType": {
                "type": "string"
                },
                "acl": {
                "type": "string"
                },
                "displayCertificatesRenewalMessages": {
                "type": "boolean"
                },
                "portalName": {
                "type": "string"
                },
                "staticIPHostNameFQDN": {
                "type": "string"
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
