# -*- coding: utf-8 -*-
"""Identity Services Engine createInternaluser data model.

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


class JSONSchemaValidatorD70F5BcF7885Af7B2Df100E10B4C88E(object):
    """createInternaluser request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD70F5BcF7885Af7B2Df100E10B4C88E, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "InternalUser": {
                "properties": {
                "accountNameAlias": {
                "type": "string"
                },
                "changePassword": {
                "type": "boolean"
                },
                "customAttributes": {
                "type": "string"
                },
                "dateCreated": {
                "type": "string"
                },
                "dateModified": {
                "type": "string"
                },
                "daysForPasswordExpiration": {
                "type": "number"
                },
                "description":
                 {
                "type": "string"
                },
                "email": {
                "type": "string"
                },
                "enablePassword": {
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "expiryDate": {
                "type": "string"
                },
                "expiryDateEnabled": {
                "type": "boolean"
                },
                "firstName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "identityGroups": {
                "type": "string"
                },
                "lastName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "passwordIDStore": {
                "type": "string"
                },
                "passwordNeverExpires": {
                "type": "boolean"
                }
                },
                "required": [
                "enabled",
                "name"
                ]
                }
                },
                "required": [
                "InternalUser"
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
