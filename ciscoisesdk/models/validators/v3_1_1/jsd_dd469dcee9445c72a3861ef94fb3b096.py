# -*- coding: utf-8 -*-
"""Identity Services Engine createSystemCertificate data model.

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


class JSONSchemaValidatorDd469DceE9445C72A3861Ef94Fb3B096(object):
    """createSystemCertificate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDd469DceE9445C72A3861Ef94Fb3B096, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ERSSystemCertificate": {
                "properties": {
                "ersLocalCertStub": {
                "properties": {
                "allowWildcardCerts": {
                "type": "string"
                },
                "certificatePolicies": {
                "type": "string"
                },
                "certificateSanDns": {
                "type": "string"
                },
                "certificateSanIp": {
                "type": "string"
                },
                "certificateSanUri": {
                "type": "string"
                },
                "digest": {
                "type": "string"
                },
                "ersSubjectStub": {
                "properties": {
                "commonName": {
                "type": "string"
                },
                "countryName": {
                "type": "string"
                },
                "localityName": {
                "type": "string"
                },
                "organizationName": {
                "type": "string"
                },
                "organizationalUnitName": {
                "type": "string"
                },
                "stateOrProvinceName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "expirationTTL": {
                "type": "integer"
                },
                "friendlyName": {
                "type": "string"
                },
                "groupTagDD": {
                "type": "string"
                },
                "keyLength": {
                "type": "string"
                },
                "keyType": {
                "type": "string"
                },
                "samlCertificate": {
                "type": "string"
                },
                "selectedExpirationTTLUnit": {
                "type": "string"
                },
                "xgridCertificate": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "nodeId": {
                "type": "string"
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
