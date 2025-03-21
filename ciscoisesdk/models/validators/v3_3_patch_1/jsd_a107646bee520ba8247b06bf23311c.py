# -*- coding: utf-8 -*-
"""Identity Services Engine patchEndpointId data model.

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


class JSONSchemaValidatorA107646Bee520BA8247B06Bf23311C(object):
    """patchEndpointId request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA107646Bee520BA8247B06Bf23311C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ERSEndPoint": {
                "properties": {
                "customAttributes": {
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
                "staticGroupAssignmentDefined": {
                "type": "boolean"
                },
                "staticProfileAssignment": {
                "type": "boolean"
                },
                "staticProfileAssignmentDefined": {
                "type": "boolean"
                }
                }
                }
                },
                "required": [
                "ERSEndPoint"
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
