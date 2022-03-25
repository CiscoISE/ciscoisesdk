# -*- coding: utf-8 -*-
"""Identity Services Engine ImportSystemCertificate data model.

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


class JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953(object):
    """ImportSystemCertificate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "admin": {
                "type": "boolean"
                },
                "allowExtendedValidity": {
                "type": "boolean"
                },
                "allowOutOfDateCert": {
                "type": "boolean"
                },
                "allowReplacementOfCertificates": {
                "type": "boolean"
                },
                "allowReplacementOfPortalGroupTag": {
                "type": "boolean"
                },
                "allowSHA1Certificates": {
                "type": "boolean"
                },
                "allowWildCardCertificates": {
                "type": "boolean"
                },
                "data": {
                "type": "string"
                },
                "eap": {
                "type": "boolean"
                },
                "ims": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "portal": {
                "type": "boolean"
                },
                "portalGroupTag": {
                "type": "string"
                },
                "portalTagTransferForSameSubject": {
                "type": "boolean"
                },
                "privateKeyData": {
                "type": "string"
                },
                "pxgrid": {
                "type": "boolean"
                },
                "radius": {
                "type": "boolean"
                },
                "roleTransferForSameSubject": {
                "type": "boolean"
                },
                "saml": {
                "type": "boolean"
                },
                "validateCertificateExtensions": {
                "type": "boolean"
                }
                },
                "required": [
                "allowExtendedValidity",
                "allowOutOfDateCert",
                "allowReplacementOfCertificates",
                "allowReplacementOfPortalGroupTag",
                "allowSHA1Certificates",
                "data",
                "privateKeyData"
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
