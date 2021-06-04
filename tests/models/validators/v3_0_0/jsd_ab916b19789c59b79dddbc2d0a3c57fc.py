# -*- coding: utf-8 -*-
"""Identity Services Engine getAllNetworkAccessTimeConditions data model.

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


class JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc(object):
    """getAllNetworkAccessTimeConditions request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "items": {
                "allOf": [
                {
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
                {
                "properties": {
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
                "required": [
                "startDate",
                "endDate"
                ],
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
                "required": [
                "startDate",
                "endDate"
                ],
                "type": "object"
                },
                "description":
                 {
                "default": "",
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
                "required": [
                "startTime",
                "endTime"
                ],
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
                "required": [
                "startTime",
                "endTime"
                ],
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "name": {
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
                "required": [
                "name"
                ]
                }
                ]
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
