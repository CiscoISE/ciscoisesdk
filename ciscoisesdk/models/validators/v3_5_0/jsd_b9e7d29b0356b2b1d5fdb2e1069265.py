# -*- coding: utf-8 -*-
"""Identity Services Engine putDeviceAdminTimeConditionByConditionId data model.

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


class JSONSchemaValidatorB9E7D29B0356B2B1D5Fdb2E1069265(object):
    """putDeviceAdminTimeConditionByConditionId request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorB9E7D29B0356B2B1D5Fdb2E1069265, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
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
                "datesRange": {
                "properties": {
                "endDate": {
                "type": "string"
                },
                "startDate": {
                "type": "string"
                }
                },
                "required": [
                "endDate",
                "startDate"
                ],
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
                "required": [
                "endDate",
                "startDate"
                ],
                "type": "object"
                },
                "description":
                 {
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
                "endTime",
                "startTime"
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
                "endTime",
                "startTime"
                ],
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
                "required": [
                "href"
                ],
                "type": "object"
                },
                "name": {
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
                "required": [
                "conditionType",
                "name"
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
