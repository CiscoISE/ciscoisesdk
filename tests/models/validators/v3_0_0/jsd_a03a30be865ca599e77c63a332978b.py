# -*- coding: utf-8 -*-
"""Identity Services Engine createDeviceAdminAuthorizationRule data model.

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


class JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B(object):
    """createDeviceAdminAuthorizationRule request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "minProperties": 2,
                "properties": {
                "commands": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "profile": {
                "type": "string"
                },
                "rule": {
                "properties": {
                "condition": {
                "properties": {
                "attributeId": {
                "type": "string"
                },
                "attributeName": {
                "type": "string"
                },
                "attributeValue": {
                "type": "string"
                },
                "children": {
                "items": {
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
                "type": "object"
                },
                "minItems": 2,
                "type": "array"
                },
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
                "datesRange": {
                "properties": {
                "endDate": {
                "maxLength": 10,
                "minLength": 10,
                "type": "string"
                },
                "startDate": {
                "maxLength": 10,
                "minLength": 10,
                "type": "string"
                }
                },
                "type": "object"
                },
                "datesRangeException": {
                "properties": {
                "endDate": {
                "maxLength": 10,
                "minLength": 10,
                "type": "string"
                },
                "startDate": {
                "maxLength": 10,
                "minLength": 10,
                "type": "string"
                }
                },
                "type": "object"
                },
                "description":
                 {
                "default": "",
                "type": "string"
                },
                "dictionaryName": {
                "type": "string"
                },
                "dictionaryValue": {
                "type": "string"
                },
                "hoursRange": {
                "properties": {
                "endTime": {
                "type": "string"
                },
                "startTime": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "hoursRangeException": {
                "properties": {
                "endTime": {
                "type": "string"
                },
                "startTime": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "isNegate": {
                "default": false,
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "operator": {
                "enum": [
                "equals",
                "notEquals",
                "contains",
                "notContains",
                "matches",
                "in",
                "notIn",
                "startsWith",
                "notStartsWith",
                "endsWith",
                "notEndsWith",
                "greaterThan",
                "lessThan",
                "greaterOrEquals",
                "lessOrEquals",
                "macEquals",
                "macNotEquals",
                "macNotIn",
                "macIn",
                "macStartsWith",
                "macNotStartsWith",
                "macEndsWith",
                "macNotEndsWith",
                "macContains",
                "macNotContains",
                "ipGreaterThan",
                "ipLessThan",
                "ipEquals",
                "ipNotEquals",
                "dateTimeMatches",
                "dateLessThan",
                "dateLessThanOrEquals",
                "dateGreaterThan",
                "dateGreaterThanOrEquals",
                "dateEquals",
                "dateNotEquals"
                ],
                "type": "string"
                },
                "weekDays": {
                "default": [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
                ],
                "items": {
                "enum": [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
                ],
                "type": "string"
                },
                "minItems": 1,
                "type": "array"
                },
                "weekDaysException": {
                "items": {
                "enum": [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
                ],
                "type": "string"
                },
                "type": "array"
                }
                },
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
                }
                },
                "required": [
                "rule"
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
