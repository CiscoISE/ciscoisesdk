# -*- coding: utf-8 -*-
"""Identity Services Engine getDeploymentInfo data model.

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


class JSONSchemaValidatorF9159C9F9A1951568DaeE7080E1Dda47(object):
    """getDeploymentInfo request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF9159C9F9A1951568DaeE7080E1Dda47, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ERSDeploymentInfo": {
                "properties": {
                "deploymentInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "fipsstatus": {
                "type": "string"
                },
                "nodeList": {
                "properties": {
                "nodeAndNodeCountAndCountInfo": {
                "items": {
                "properties": {
                "declaredType": {
                "type": "string"
                },
                "globalScope": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "nil": {
                "type": "boolean"
                },
                "scope": {
                "type": "string"
                },
                "typeSubstituted": {
                "type": "boolean"
                },
                "value": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "versionHistoryInfo": {
                "items": {
                "properties": {
                "epochTime": {
                "type": "integer"
                },
                "mainVersion": {
                "type": "string"
                },
                "opType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "kongInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "nodeList": {
                "properties": {
                "node": {
                "items": {
                "properties": {
                "service": {
                "items": {
                "properties": {
                "route": {
                "items": {
                "properties": {
                "httpCount": {
                "type": "object"
                },
                "latencyCount": {
                "type": "object"
                },
                "latencySum": {
                "type": "object"
                },
                "routeName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "serviceName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "sn": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "licensesInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "nodeList": {
                "properties": {
                "node": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "mdmInfo": {
                "properties": {
                "activeDesktopMdmServersCount": {
                "type": "string"
                },
                "activeMdmServersCount": {
                "type": "string"
                },
                "activeMobileMdmServersCount": {
                "type": "string"
                },
                "deploymentID": {
                "type": "string"
                },
                "nodeList": {
                "properties": {
                "nodeAndScope": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "nadInfo": {
                "properties": {
                "nadcountInfo": {
                "properties": {
                "totalActiveNADCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "nodeList": {
                "properties": {
                "nodeAndScope": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "networkAccessInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "isCsnEnabled": {
                "type": "boolean"
                },
                "nodeList": {
                "properties": {
                "nodeAndScope": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "radius3RdParty": {
                "items": {},
                "type": "array"
                },
                "sdaVNs": {
                "items": {},
                "type": "array"
                },
                "trustSecControl": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "postureInfo": {
                "properties": {
                "content": {
                "items": {
                "properties": {
                "declaredType": {
                "type": "string"
                },
                "globalScope": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "nil": {
                "type": "boolean"
                },
                "scope": {
                "type": "string"
                },
                "typeSubstituted": {
                "type": "boolean"
                },
                "value": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "profilerInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "nodeList": {
                "properties": {
                "node": {
                "items": {
                "properties": {
                "lastAppliedFeedDateTime": {
                "type": "string"
                },
                "onlineSubscriptionEnabled": {
                "type": "boolean"
                },
                "profiles": {
                "items": {
                "properties": {
                "customProfilesCount": {
                "type": "integer"
                },
                "endpointTypes": {
                "type": "string"
                },
                "profile": {
                "items": {},
                "type": "array"
                },
                "totalEndpointsCount": {
                "type": "integer"
                },
                "totalProfilesCount": {
                "type": "integer"
                },
                "uniqueEndpointsCount": {
                "type": "integer"
                },
                "unknownEndpointsCount": {
                "type": "integer"
                },
                "unknownEndpointsPercentage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "object"
                },
                "scope": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
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
