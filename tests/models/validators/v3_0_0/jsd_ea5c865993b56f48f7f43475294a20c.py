# -*- coding: utf-8 -*-
"""Identity Services Engine getAllAciSettings data model.

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


class JSONSchemaValidatorEa5C865993B56F48F7F43475294A20C(object):
    """getAllAciSettings request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEa5C865993B56F48F7F43475294A20C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "AciSettings": {
                "properties": {
                "aci50": {
                "type": "boolean"
                },
                "aci51": {
                "type": "boolean"
                },
                "aciipaddress": {
                "type": "string"
                },
                "acipassword": {
                "type": "string"
                },
                "aciuserName": {
                "type": "string"
                },
                "adminName": {
                "type": "string"
                },
                "adminPassword": {
                "type": "string"
                },
                "allSxpDomain": {
                "type": "boolean"
                },
                "defaultSgtName": {
                "type": "string"
                },
                "enableAci": {
                "type": "boolean"
                },
                "enableDataPlane": {
                "type": "boolean"
                },
                "enableElementsLimit": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "ipAddressHostName": {
                "type": "string"
                },
                "l3RouteNetwork": {
                "type": "string"
                },
                "maxNumIepgFromAci": {
                "type": "integer"
                },
                "maxNumSgtToAci": {
                "type": "integer"
                },
                "specificSxpDomain": {
                "type": "boolean"
                },
                "specifixSxpDomainList": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "suffixToEpg": {
                "type": "string"
                },
                "suffixToSgt": {
                "type": "string"
                },
                "tenantName": {
                "type": "string"
                },
                "untaggedPacketIepgName": {
                "type": "string"
                }
                },
                "required": [
                "enableAci",
                "defaultSgtName",
                "aci50",
                "aci51"
                ],
                "type": "object"
                }
                },
                "required": [
                "AciSettings"
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
