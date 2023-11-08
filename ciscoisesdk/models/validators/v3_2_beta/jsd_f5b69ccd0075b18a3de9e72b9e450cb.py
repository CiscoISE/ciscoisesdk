# -*- coding: utf-8 -*-
"""Identity Services Engine updateConnectorConfigByConnectorName data model.

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


class JSONSchemaValidatorF5B69CcD0075B18A3De9E72B9E450Cb(object):
    """updateConnectorConfigByConnectorName request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF5B69CcD0075B18A3De9E72B9E450Cb, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "connector": {
                "properties": {
                "additionalProperties": {
                "additionalProperties": {
                "type": "string"
                },
                "type": "object"
                },
                "attributes": {
                "properties": {
                "attributeMapping": {
                "items": {
                "properties": {
                "dictionaryAttribute": {
                "type": "string"
                },
                "includeInDictionary": {
                "type": "boolean"
                },
                "jsonAttribute": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "bulkUniqueIdentifier": {
                "type": "string"
                },
                "topLevelObject": {
                "type": "string"
                },
                "uniqueIdentifier": {
                "type": "string"
                },
                "versionIdentifier": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "connectorName": {
                "type": "string"
                },
                "connectorType": {
                "enum": [
                "urlfetcher",
                "vmware"
                ],
                "type": "string"
                },
                "deltasyncSchedule": {
                "properties": {
                "interval": {
                "type": "integer"
                },
                "intervalUnit": {
                "enum": [
                "days",
                "hours",
                "weeks"
                ],
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
                "enabled": {
                "type": "boolean"
                },
                "fullsyncSchedule": {
                "properties": {
                "interval": {
                "type": "integer"
                },
                "intervalUnit": {
                "enum": [
                "days",
                "hours",
                "weeks"
                ],
                "type": "string"
                },
                "startDate": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "protocol": {
                "type": "string"
                },
                "skipCertificateValidations": {
                "type": "boolean"
                },
                "url": {
                "properties": {
                "accessKey": {
                "type": "string"
                },
                "authenticationType": {
                "enum": [
                "apikey",
                "basic"
                ],
                "type": "string"
                },
                "bulkUrl": {
                "type": "string"
                },
                "clientId": {
                "type": "string"
                },
                "clientSecret": {
                "type": "string"
                },
                "incrementalUrl": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "refreshToken": {
                "type": "string"
                },
                "tokenHeader": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
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
