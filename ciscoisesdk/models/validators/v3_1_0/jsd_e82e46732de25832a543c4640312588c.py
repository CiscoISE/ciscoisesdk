# -*- coding: utf-8 -*-
"""Identity Services Engine registerNode data model.

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


class JSONSchemaValidatorE82E46732De25832A543C4640312588C(object):
    """registerNode request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE82E46732De25832A543C4640312588C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "administration": {
                "properties": {
                "isEnabled": {
                "type": "boolean"
                },
                "role": {
                "enum": [
                "Primary",
                "Secondary",
                "Standalone"
                ],
                "type": "string"
                }
                },
                "type": "object"
                },
                "fdqn": {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "generalSettings": {
                "properties": {
                "monitoring": {
                "properties": {
                "enablePXGrid": {
                "type": "boolean"
                },
                "isEnabled": {
                "type": "boolean"
                },
                "isMntDedicated": {
                "type": "boolean"
                },
                "otherMonitoringNode": {
                "maxLength": 64,
                "minLength": 1,
                "type": "string"
                },
                "policyservice": {
                "properties": {
                "enableDeviceAdminService": {
                "type": "boolean"
                },
                "enableNACService": {
                "type": "boolean"
                },
                "enablePassiveIdentityService": {
                "type": "boolean"
                },
                "enableProfilingService": {
                "type": "boolean"
                },
                "enabled": {
                "type": "boolean"
                },
                "sessionService": {
                "properties": {
                "isEnabled": {
                "type": "boolean"
                },
                "nodegroup": {
                "default": "NONE",
                "type": "string"
                }
                },
                "type": "object"
                },
                "sxpservice": {
                "properties": {
                "isEnabled": {
                "type": "boolean"
                },
                "userInterface": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "role": {
                "enum": [
                "Primary",
                "Secondary",
                "None"
                ],
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "password": {
                "type": "string"
                },
                "profileConfiguration": {
                "properties": {
                "activeDirectory": {
                "properties": {
                "daysBeforeRescan": {
                "type": "integer"
                },
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "dhcp": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "interface": {
                "type": "string"
                },
                "port": {
                "allOf": [
                {
                "maximum": 65535,
                "minimum": 0,
                "type": "integer"
                },
                {
                "default": 67
                }
                ]
                }
                },
                "type": "object"
                },
                "dhcpSpan": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "interface": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "dns": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "http": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "interface": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "netflow": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "interface": {
                "type": "string"
                },
                "port": {
                "allOf": [
                {
                "maximum": 65535,
                "minimum": 0,
                "type": "integer"
                },
                {
                "default": 9996
                }
                ]
                }
                },
                "type": "object"
                },
                "nmap": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "pxgrid": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "radius": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "snmpQuery": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "eventTimeout": {
                "type": "integer"
                },
                "retries": {
                "type": "integer"
                },
                "timeout": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "snmpTrap": {
                "properties": {
                "description":
                 {
                "maxLength": 256,
                "minLength": 1,
                "type": "string"
                },
                "interface": {
                "type": "string"
                },
                "linkTrapQuery": {
                "type": "boolean"
                },
                "macTrapQuery": {
                "type": "boolean"
                },
                "port": {
                "allOf": [
                {
                "maximum": 65535,
                "minimum": 0,
                "type": "integer"
                },
                {
                "default": 162
                }
                ]
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "userName": {
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
