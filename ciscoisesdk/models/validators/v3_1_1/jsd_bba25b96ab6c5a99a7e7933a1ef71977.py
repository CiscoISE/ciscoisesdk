# -*- coding: utf-8 -*-
"""Identity Services Engine setProfilerProbeConfig data model.

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


class JSONSchemaValidatorBba25B96Ab6C5A99A7E7933A1Ef71977(object):
    """setProfilerProbeConfig request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorBba25B96Ab6C5A99A7E7933A1Ef71977, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "activeDirectory": {
                "properties": {
                "daysBeforeRescan": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "dhcp": {
                "properties": {
                "interfaces": {
                "items": {
                "properties": {
                "interface": {
                "type": "string"
                }
                },
                "required": [
                "interface"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "port": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "dhcpSpan": {
                "properties": {
                "interfaces": {
                "items": {
                "properties": {
                "interface": {
                "type": "string"
                }
                },
                "required": [
                "interface"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "dns": {
                "properties": {
                "timeout": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "http": {
                "properties": {
                "interfaces": {
                "items": {
                "properties": {
                "interface": {
                "type": "string"
                }
                },
                "required": [
                "interface"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "netflow": {
                "properties": {
                "interfaces": {
                "items": {
                "properties": {
                "interface": {
                "type": "string"
                }
                },
                "required": [
                "interface"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "port": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "nmap": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "pxgrid": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "radius": {
                "items": {
                "type": "object"
                },
                "type": "array"
                },
                "snmpQuery": {
                "properties": {
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
                "interfaces": {
                "items": {
                "properties": {
                "interface": {
                "type": "string"
                }
                },
                "required": [
                "interface"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "linkTrapQuery": {
                "type": "boolean"
                },
                "macTrapQuery": {
                "type": "boolean"
                },
                "port": {
                "type": "integer"
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
