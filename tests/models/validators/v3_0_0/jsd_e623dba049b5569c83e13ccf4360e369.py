# -*- coding: utf-8 -*-
"""Identity Services Engine getAllNetworkAccessAuthorizationRules data model.

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


class JSONSchemaValidatorE623Dba049B5569C83E13Ccf4360E369(object):
    """getAllNetworkAccessAuthorizationRules request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE623Dba049B5569C83E13Ccf4360E369, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "properties": {
                "profile": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "rule": {
                "properties": {
                "condition": {
                "discriminator": {
                "mapping": {
                "ConditionAndBlock": "#/components/schemas/ConditionAndBlock",
                "ConditionAttributes": "#/components/schemas/ConditionAttributes",
                "ConditionOrBlock": "#/components/schemas/ConditionOrBlock",
                "ConditionReference": "#/components/schemas/ConditionReference",
                "LibraryConditionAndBlock": "#/components/schemas/LibraryConditionAndBlock",
                "LibraryConditionAttributes": "#/components/schemas/LibraryConditionAttributes",
                "LibraryConditionOrBlock": "#/components/schemas/LibraryConditionOrBlock",
                "TimeAndDateCondition": "#/components/schemas/TimeAndDateCondition"
                },
                "propertyName": "conditionType"
                },
                "properties": {
                "conditionType": {
                "enum": [
                "ConditionReference",
                "ConditionAttributes",
                "LibraryConditionAttributes",
                "ConditionAndBlock",
                "LibraryConditionAndBlock",
                "ConditionOrBlock",
                "LibraryConditionOrBlock",
                "TimeAndDateCondition"
                ],
                "type": "string"
                },
                "isNegate": {
                "default": false,
                "type": "boolean"
                }
                },
                "required": [
                "conditionType"
                ],
                "type": "object"
                },
                "default": {
                "default": false,
                "type": "boolean"
                },
                "description":
                 {
                "default": "Empty string",
                "type": "string"
                },
                "hitCounts": {
                "default": 0,
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "rank": {
                "default": 0,
                "type": "integer"
                },
                "state": {
                "default": "enabled",
                "enum": [
                "enabled",
                "disabled",
                "monitor"
                ],
                "type": "string"
                }
                },
                "required": [
                "name"
                ],
                "type": "object"
                },
                "securityGroup": {
                "type": "string"
                }
                },
                "required": [
                "rule",
                "profile"
                ],
                "type": "object"
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
