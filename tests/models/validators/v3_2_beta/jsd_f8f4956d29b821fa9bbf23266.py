# -*- coding: utf-8 -*-
"""Identity Services Engine getTrustedCertificateById data model.

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


import json
from builtins import *

import fastjsonschema
from ciscoisesdk.exceptions import MalformedRequest


class JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266(object):
    """getTrustedCertificateById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "authenticateBeforeCRLReceived": {
                "type": "string"
                },
                "automaticCRLUpdate": {
                "type": "string"
                },
                "automaticCRLUpdatePeriod": {
                "type": "string"
                },
                "automaticCRLUpdateUnits": {
                "type": "string"
                },
                "crlDistributionUrl": {
                "type": "string"
                },
                "crlDownloadFailureRetries": {
                "type": "string"
                },
                "crlDownloadFailureRetriesUnits": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "downloadCRL": {
                "type": "string"
                },
                "enableOCSPValidation": {
                "type": "string"
                },
                "enableServerIdentityCheck": {
                "type": "string"
                },
                "expirationDate": {
                "type": "string"
                },
                "friendlyName": {
                "type": "string"
                },
                "id": {
                "type": "string"
                },
                "ignoreCRLExpiration": {
                "type": "string"
                },
                "internalCA": {
                "type": "boolean"
                },
                "isReferredInPolicy": {
                "type": "boolean"
                },
                "issuedBy": {
                "type": "string"
                },
                "issuedTo": {
                "type": "string"
                },
                "keySize": {
                "type": "string"
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
                "nonAutomaticCRLUpdatePeriod": {
                "type": "string"
                },
                "nonAutomaticCRLUpdateUnits": {
                "type": "string"
                },
                "rejectIfNoStatusFromOCSP": {
                "type": "string"
                },
                "rejectIfUnreachableFromOCSP": {
                "type": "string"
                },
                "selectedOCSPService": {
                "type": "string"
                },
                "serialNumberDecimalFormat": {
                "type": "string"
                },
                "sha256Fingerprint": {
                "type": "string"
                },
                "signatureAlgorithm": {
                "type": "string"
                },
                "status": {
                "type": "string"
                },
                "subject": {
                "type": "string"
                },
                "trustedFor": {
                "type": "string"
                },
                "validFrom": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "version": {
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
