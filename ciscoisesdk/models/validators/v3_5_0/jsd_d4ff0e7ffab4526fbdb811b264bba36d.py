# -*- coding: utf-8 -*-
"""Identity Services Engine testConnector data model.

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


class JSONSchemaValidatorD4Ff0E7FFab4526FBdb811B264Bba36D(object):
    """testConnector request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorD4Ff0E7FFab4526FBdb811B264Bba36D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "authType": {
                "enum": [
                "apikey",
                "basic",
                "oauth2"
                ],
                "type": "string"
                },
                "authValues": {
                "properties": {
                "clientId": {
                "type": "string"
                },
                "clientSecret": {
                "type": "string"
                },
                "flow": {
                "type": "string"
                },
                "headerName": {
                "type": "string"
                },
                "key": {
                "type": "string"
                },
                "keyType": {
                "type": "string"
                },
                "paramName": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "requestBody": {
                "type": "string"
                },
                "scope": {
                "type": "string"
                },
                "tokenIssuingUrl": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "connectorName": {
                "type": "string"
                },
                "flexibleUrl": {
                "properties": {
                "bulk": {
                "properties": {
                "additionalHeaders": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "apiKeyProperties": {
                "properties": {
                "headerName": {
                "type": "string"
                },
                "key": {
                "type": "string"
                },
                "keyType": {
                "enum": [
                "header",
                "json",
                "param"
                ],
                "type": "string"
                },
                "paramName": {
                "type": "string"
                },
                "requestBody": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "authenticationType": {
                "enum": [
                "apikey",
                "basic",
                "oauth2"
                ],
                "type": "string"
                },
                "basicAuthProperties": {
                "properties": {
                "password": {
                "type": "string"
                },
                "requestBody": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "method": {
                "enum": [
                "DELETE",
                "GET",
                "POST",
                "PUT"
                ],
                "type": "string"
                },
                "oauthProperties": {
                "properties": {
                "clientId": {
                "type": "string"
                },
                "clientSecret": {
                "type": "string"
                },
                "flow": {
                "enum": [
                "authorization_code",
                "client_credentials",
                "password"
                ],
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "scope": {
                "type": "string"
                },
                "tokenIssuingUrl": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "url": {
                "type": "string"
                }
                },
                "required": [
                "authenticationType"
                ],
                "type": "object"
                },
                "incremental": {
                "properties": {
                "additionalHeaders": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "apiKeyProperties": {
                "properties": {
                "headerName": {
                "type": "string"
                },
                "key": {
                "type": "string"
                },
                "keyType": {
                "enum": [
                "header",
                "json",
                "param"
                ],
                "type": "string"
                },
                "paramName": {
                "type": "string"
                },
                "requestBody": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "authenticationType": {
                "enum": [
                "apikey",
                "basic",
                "oauth2"
                ],
                "type": "string"
                },
                "basicAuthProperties": {
                "properties": {
                "password": {
                "type": "string"
                },
                "requestBody": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "method": {
                "enum": [
                "DELETE",
                "GET",
                "POST",
                "PUT"
                ],
                "type": "string"
                },
                "oauthProperties": {
                "properties": {
                "clientId": {
                "type": "string"
                },
                "clientSecret": {
                "type": "string"
                },
                "flow": {
                "enum": [
                "authorization_code",
                "client_credentials",
                "password"
                ],
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "scope": {
                "type": "string"
                },
                "tokenIssuingUrl": {
                "type": "string"
                },
                "userName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "url": {
                "type": "string"
                }
                },
                "required": [
                "authenticationType"
                ],
                "type": "object"
                }
                },
                "type": "object"
                },
                "incrementalUrl": {
                "type": "string"
                },
                "responseParsing": {
                "type": "string"
                },
                "skipCertificateValidations": {
                "type": "boolean"
                },
                "uniqueID": {
                "type": "string"
                },
                "url": {
                "type": "string"
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
