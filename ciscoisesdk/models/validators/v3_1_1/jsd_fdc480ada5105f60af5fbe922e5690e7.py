# -*- coding: utf-8 -*-
"""Identity Services Engine generateSelfSignedCertificate data model.

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


class JSONSchemaValidatorFdc480AdA5105F60Af5FBe922E5690E7(object):
    """generateSelfSignedCertificate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFdc480AdA5105F60Af5FBe922E5690E7, self).__init__()
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
                "allowPortalTagTransferForSameSubject": {
                "type": "boolean"
                },
                "allowReplacementOfCertificates": {
                "type": "boolean"
                },
                "allowReplacementOfPortalGroupTag": {
                "type": "boolean"
                },
                "allowRoleTransferForSameSubject": {
                "type": "boolean"
                },
                "allowSanDnsBadName": {
                "type": "boolean"
                },
                "allowSanDnsNonResolvable": {
                "type": "boolean"
                },
                "allowWildCardCertificates": {
                "type": "boolean"
                },
                "certificatePolicies": {
                "type": "string"
                },
                "digestType": {
                "enum": [
                "SHA-256",
                "SHA-384",
                "SHA-512"
                ],
                "type": "string"
                },
                "eap": {
                "type": "boolean"
                },
                "expirationTTL": {
                "type": "integer"
                },
                "expirationTTLUnit": {
                "enum": [
                "days",
                "months",
                "weeks",
                "years"
                ],
                "type": "string"
                },
                "hostName": {
                "type": "string"
                },
                "keyLength": {
                "enum": [
                "1024",
                "2048",
                "4096",
                "512"
                ],
                "type": "string"
                },
                "keyType": {
                "enum": [
                "ECDSA",
                "RSA"
                ],
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "portal": {
                "type": "boolean"
                },
                "portalGroupTag": {
                "type": "string"
                },
                "pxgrid": {
                "type": "boolean"
                },
                "radius": {
                "type": "boolean"
                },
                "saml": {
                "type": "boolean"
                },
                "sanDNS": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sanIP": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sanURI": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "subjectCity": {
                "type": "string"
                },
                "subjectCommonName": {
                "type": "string"
                },
                "subjectCountry": {
                "type": "string"
                },
                "subjectOrg": {
                "type": "string"
                },
                "subjectOrgUnit": {
                "type": "string"
                },
                "subjectState": {
                "type": "string"
                }
                },
                "required": [
                "allowExtendedValidity",
                "allowPortalTagTransferForSameSubject",
                "allowReplacementOfCertificates",
                "allowReplacementOfPortalGroupTag",
                "allowRoleTransferForSameSubject",
                "allowSanDnsBadName",
                "allowSanDnsNonResolvable",
                "digestType",
                "expirationTTL",
                "expirationTTLUnit",
                "hostName",
                "keyLength",
                "keyType"
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
