# -*- coding: utf-8 -*-
"""Identity Services Engine registerEndpoint data model.

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


class JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008(object):
    """registerEndpoint request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ERSEndPoint": {
                "properties": {
                "customAttributes": {
                "properties": {
                "customAttributes": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "groupId": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "identityStore": {
                "type": "string"
                },
                "identityStoreId": {
                "type": "string"
                },
                "mac": {
                "type": "string"
                },
                "mdmAttributes": {
                "properties": {
                "mdmComplianceStatus": {
                "type": "boolean"
                },
                "mdmEncrypted": {
                "type": "boolean"
                },
                "mdmEnrolled": {
                "type": "boolean"
                },
                "mdmIMEI": {
                "type": "string"
                },
                "mdmJailBroken": {
                "type": "boolean"
                },
                "mdmManufacturer": {
                "type": "string"
                },
                "mdmModel": {
                "type": "string"
                },
                "mdmOS": {
                "type": "string"
                },
                "mdmPhoneNumber": {
                "type": "string"
                },
                "mdmPinlock": {
                "type": "boolean"
                },
                "mdmReachable": {
                "type": "boolean"
                },
                "mdmSerial": {
                "type": "string"
                },
                "mdmServerName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "portalUser": {
                "type": "string"
                },
                "profileId": {
                "type": "string"
                },
                "staticGroupAssignment": {
                "type": "boolean"
                },
                "staticProfileAssignment": {
                "type": "boolean"
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
