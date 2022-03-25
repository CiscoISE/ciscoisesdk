# -*- coding: utf-8 -*-
"""Identity Services Engine updateGuestTypeById data model.

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


class JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D(object):
    """updateGuestTypeById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "GuestType": {
                "properties": {
                "accessTime": {
                "properties": {
                "allowAccessOnSpecificDaysTimes": {
                "type": "boolean"
                },
                "dayTimeLimits": {
                "items": {
                "properties": {
                "days": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "endTime": {
                "type": "string"
                },
                "startTime": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "defaultDuration": {
                "type": "integer"
                },
                "durationTimeUnit": {
                "type": "string"
                },
                "fromFirstLogin": {
                "type": "boolean"
                },
                "maxAccountDuration": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "expirationNotification": {
                "properties": {
                "advanceNotificationDuration": {
                "type": "integer"
                },
                "advanceNotificationUnits": {
                "type": "string"
                },
                "emailText": {
                "type": "string"
                },
                "enableNotification": {
                "type": "boolean"
                },
                "sendEmailNotification": {
                "type": "boolean"
                },
                "sendSmsNotification": {
                "type": "boolean"
                },
                "smsText": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "isDefaultType": {
                "type": "boolean"
                },
                "loginOptions": {
                "properties": {
                "allowGuestPortalBypass": {
                "type": "boolean"
                },
                "failureAction": {
                "type": "string"
                },
                "identityGroupId": {
                "type": "string"
                },
                "limitSimultaneousLogins": {
                "type": "boolean"
                },
                "maxRegisteredDevices": {
                "type": "integer"
                },
                "maxSimultaneousLogins": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "sponsorGroups": {
                "items": {
                "type": "string"
                },
                "type": "array"
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
