# -*- coding: utf-8 -*-
"""Identity Services Engine cancelBackup data model.

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


class JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902(object):
    """cancelBackup request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "action": {
                "enum": [
                "BACKUP",
                "RESTORE",
                "CANCEL"
                ],
                "type": "string"
                },
                "details": {
                "type": "string"
                },
                "error": {
                "type": "string"
                },
                "hostName": {
                "type": "string"
                },
                "initiatedFrom": {
                "enum": [
                "CLI",
                "ADMIN_GUI",
                "OPEN_API"
                ],
                "type": "string"
                },
                "justComplete": {
                "type": "string"
                },
                "message": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "percentComplete": {
                "type": "string"
                },
                "repository": {
                "type": "string"
                },
                "scheduled": {
                "type": "string"
                },
                "startDate": {
                "type": "string"
                },
                "status": {
                "enum": [
                "IN_PROGRESS",
                "COMPLETED",
                "ERROR"
                ],
                "type": "string"
                },
                "type": {
                "enum": [
                "OPERATIONAL_DB",
                "CONFIGURATION_DB"
                ],
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
