# -*- coding: utf-8 -*-
"""Identity Services Engine UpdateSystemCertificate data model.

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


class JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B(object):
    """UpdateSystemCertificate request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "admin": {
                "type": "boolean"
                },
                "allowReplacementOfPortalGroupTag": {
                "type": "boolean"
                },
                "description":
                 {
                "type": "string"
                },
                "eap": {
                "type": "boolean"
                },
                "expirationTTLPeriod": {
                "type": "integer"
                },
                "expirationTTLUnits": {
                "enum": [
                "days",
                "weeks",
                "months",
                "years"
                ],
                "type": "string"
                },
                "ims": {
                "type": "boolean"
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
                "renewSelfSignedCertificate": {
                "type": "boolean"
                },
                "saml": {
                "type": "boolean"
                }
                },
                "required": [
                "allowReplacementOfPortalGroupTag"
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
