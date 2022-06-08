# -*- coding: utf-8 -*-
"""Identity Services Engine createNetworkAccessAuthorizationRule data model.

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


class JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B(object):
    """createNetworkAccessAuthorizationRule request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "link": {
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
                "required": [
                "href"
                ],
                "type": "object"
                },
                "profile": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "rule": {
                "properties": {
                "condition": {
                "properties": {
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
                "ConditionAndBlock",
                "ConditionAttributes",
                "ConditionOrBlock",
                "ConditionReference",
                "LibraryConditionAndBlock",
                "LibraryConditionAttributes",
                "LibraryConditionOrBlock",
                "TimeAndDateCondition"
                ],
                "type": "string"
                },
                "isNegate": {
                "type": "boolean"
                },
                "link": {
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
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "conditionType": {
                "enum": [
                "ConditionAndBlock",
                "ConditionAttributes",
                "ConditionOrBlock",
                "ConditionReference",
                "LibraryConditionAndBlock",
                "LibraryConditionAttributes",
                "LibraryConditionOrBlock",
                "TimeAndDateCondition"
                ],
                "type": "string"
                },
                "datesRange": {
                "properties": {
                "endDate": {
                "type": "string"
                },
                "startDate": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "datesRangeException": {
                "properties": {
                "endDate": {
                "type": "string"
                },
                "startDate": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "description":
                 {
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
                "type": "boolean"
                },
                "link": {
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
                "name": {
                "type": "string"
                },
                "operator": {
                "enum": [
                "contains",
                "endsWith",
                "equals",
                "greaterOrEquals",
                "greaterThan",
                "in",
                "ipEquals",
                "ipGreaterThan",
                "ipLessThan",
                "ipNotEquals",
                "lessOrEquals",
                "lessThan",
                "matches",
                "notContains",
                "notEndsWith",
                "notEquals",
                "notIn",
                "notStartsWith",
                "startsWith"
                ],
                "type": "string"
                },
                "weekDays": {
                "items": {
                "enum": [
                "Friday",
                "Monday",
                "Saturday",
                "Sunday",
                "Thursday",
                "Tuesday",
                "Wednesday"
                ],
                "type": "string"
                },
                "type": "array"
                },
                "weekDaysException": {
                "items": {
                "enum": [
                "Friday",
                "Monday",
                "Saturday",
                "Sunday",
                "Thursday",
                "Tuesday",
                "Wednesday"
                ],
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "default": {
                "type": "boolean"
                },
                "hitCounts": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "rank": {
                "type": "integer"
                },
                "state": {
                "enum": [
                "disabled",
                "enabled",
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
