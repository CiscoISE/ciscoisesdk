# -*- coding: utf-8 -*-
"""Identity Services Engine updateBulkEndPoints data model.

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


class JSONSchemaValidatorE076428D49535723A07A5Bbcbcbd128D(object):
    """updateBulkEndPoints request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE076428D49535723A07A5Bbcbcbd128D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "connectedLinks": {
                "type": "object",
                "x-exampleSetFlag": true
                },
                "customAttributes": {
                "type": "object",
                "x-exampleSetFlag": true
                },
                "description":
                 {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "deviceType": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "groupId": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "hardwareRevision": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "id": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "identityStore": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "identityStoreId": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "ipAddress": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "mac": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "mdmAttributes": {
                "type": "object",
                "x-exampleSetFlag": true
                },
                "name": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "portalUser": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "productId": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "profileId": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "protocol": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "serialNumber": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "softwareRevision": {
                "type": "string",
                "x-exampleSetFlag": true
                },
                "staticGroupAssignment": {
                "type": "boolean",
                "x-exampleSetFlag": true
                },
                "staticProfileAssignment": {
                "type": "boolean",
                "x-exampleSetFlag": true
                },
                "vendor": {
                "type": "string",
                "x-exampleSetFlag": true
                }
                },
                "required": [
                "mac"
                ],
                "type": "object",
                "x-exampleSetFlag": false
                },
                "type": "array",
                "x-exampleSetFlag": true
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
