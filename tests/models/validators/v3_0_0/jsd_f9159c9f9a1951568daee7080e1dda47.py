# -*- coding: utf-8 -*-
"""Identity Services Engine getAllDeploymentInfo data model.

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


class JSONSchemaValidatorF9159C9F9A1951568DaeE7080E1Dda47(object):
    """getAllDeploymentInfo request schema definition."""
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
                "type": "boolean"
                }
                },
                "required": [
                "name",
                "declaredType",
                "scope",
                "value",
                "nil",
                "globalScope",
                "typeSubstituted"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "fileSystem": {
                "items": {
                "properties": {
                "available": {
                "type": "string"
                },
                "mountPoint": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "percent": {
                "type": "string"
                },
                "total": {
                "type": "string"
                },
                "used": {
                "type": "string"
                }
                },
                "required": [
                "name",
                "total",
                "used",
                "available",
                "percent",
                "mountPoint"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "free": {
                "type": "string"
                },
                "fromDate": {
                "type": "string"
                },
                "loadAvgFifteen": {
                "type": "string"
                },
                "loadAvgFive": {
                "type": "string"
                },
                "loadAvgOne": {
                "type": "string"
                },
                "percent": {
                "type": "string"
                },
                "toDate": {
                "type": "string"
                },
                "total": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "required": [
                "name",
                "declaredType",
                "scope",
                "value",
                "nil",
                "globalScope",
                "typeSubstituted"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "currentGuestUserCount": {
                "type": "integer"
                },
                "currentMDMEndPtCount": {
                "type": "integer"
                },
                "currentPostureEndptCount": {
                "type": "integer"
                },
                "currentPxGridClientCount": {
                "type": "integer"
                },
                "fromDate": {
                "type": "string"
                },
                "toDate": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "required": [
                "name",
                "declaredType",
                "scope",
                "value",
                "nil",
                "globalScope",
                "typeSubstituted"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "nodeAndNodeCountAndCountInfo"
                ],
                "type": "object"
                }
                },
                "required": [
                "deploymentID",
                "nodeList",
                "fipsstatus"
                ],
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
                "type": "string"
                },
                "type": "array"
                }
                },
                "required": [
                "node"
                ],
                "type": "object"
                }
                },
                "required": [
                "deploymentID",
                "nodeList"
                ],
                "type": "object"
                },
                "licensesInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "nodeList": {
                "properties": {
                "nodeAndScope": {
                "items": {
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
                "properties": {
                "count": {
                "type": "integer"
                },
                "fileName": {
                "type": "string"
                },
                "isEvaluation": {
                "type": "boolean"
                },
                "isExpired": {
                "type": "boolean"
                },
                "isWiredEnabled": {
                "type": "boolean"
                },
                "primaryUDI": {
                "type": "string"
                },
                "remainingDays": {
                "type": "integer"
                },
                "secondaryUDI": {
                "type": "string"
                },
                "serviceTypes": {
                "type": "string"
                },
                "term": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "required": [
                "name",
                "declaredType",
                "scope",
                "value",
                "nil",
                "globalScope",
                "typeSubstituted"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "nodeAndScope"
                ],
                "type": "object"
                }
                },
                "required": [
                "deploymentID",
                "nodeList"
                ],
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
                "properties": {
                "content": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "nodeAndScope"
                ],
                "type": "object"
                }
                },
                "required": [
                "activeMdmServersCount",
                "activeDesktopMdmServersCount",
                "activeMobileMdmServersCount",
                "deploymentID",
                "nodeList"
                ],
                "type": "object"
                },
                "nadInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "nadcountInfo": {
                "properties": {
                "totalActiveNADCount": {
                "type": "integer"
                }
                },
                "required": [
                "totalActiveNADCount"
                ],
                "type": "object"
                },
                "nodeList": {
                "properties": {
                "nodeAndScope": {
                "items": {
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
                "properties": {
                "activeNADCount": {
                "type": "integer"
                },
                "isCiscoProvided": {
                "type": "boolean"
                },
                "isDefProfile": {
                "type": "boolean"
                },
                "isRadiusSupported": {
                "type": "boolean"
                },
                "isTacacsSupported": {
                "type": "boolean"
                },
                "isTrustSecSupported": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "totalNADCount": {
                "type": "integer"
                }
                },
                "required": [
                "name",
                "isCiscoProvided",
                "isDefProfile",
                "isTacacsSupported",
                "isRadiusSupported",
                "isTrustSecSupported",
                "activeNADCount",
                "totalNADCount"
                ],
                "type": "object"
                }
                },
                "required": [
                "name",
                "declaredType",
                "scope",
                "value",
                "nil",
                "globalScope",
                "typeSubstituted"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "nodeAndScope"
                ],
                "type": "object"
                }
                },
                "required": [
                "deploymentID",
                "nodeList",
                "nadcountInfo"
                ],
                "type": "object"
                },
                "networkAccessInfo": {
                "properties": {
                "deploymentID": {
                "type": "string"
                },
                "nodeList": {
                "properties": {
                "nodeAndScope": {
                "items": {
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
                "properties": {
                "activeVLANCount": {
                "type": "integer"
                },
                "activedACLCount": {
                "type": "integer"
                },
                "adauthStoreCount": {
                "type": "integer"
                },
                "ldapidstoreCount": {
                "type": "integer"
                },
                "localIdentityNonAdminUserCount": {
                "type": "integer"
                },
                "ndgheierarchyNADMap": {
                "type": "string"
                },
                "ndghierarchyMap": {
                "type": "string"
                },
                "odbcInfo": {
                "items": {
                "properties": {
                "odbccount": {
                "type": "integer"
                },
                "odbctype": {
                "items": {
                "type": "string"
                },
                "type": "array"
                }
                },
                "required": [
                "odbctype",
                "odbccount"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "policyLineCount": {
                "type": "integer"
                },
                "radiusidstoreCount": {
                "type": "integer"
                },
                "restIDInfo": {
                "items": {
                "properties": {
                "restIDType": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "restidcount": {
                "type": "integer"
                }
                },
                "required": [
                "restIDType",
                "restidcount"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "rsaidstoreCount": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "required": [
                "name",
                "declaredType",
                "scope",
                "value",
                "nil",
                "globalScope",
                "typeSubstituted"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "nodeAndScope"
                ],
                "type": "object"
                },
                "radius3RdParty": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "sdaVNs": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "trustSecControl": {
                "type": "string"
                }
                },
                "required": [
                "deploymentID",
                "nodeList",
                "sdaVNs",
                "trustSecControl",
                "radius3RdParty"
                ],
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
                "type": "integer"
                }
                },
                "required": [
                "name",
                "declaredType",
                "scope",
                "value",
                "nil",
                "globalScope",
                "typeSubstituted"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "content"
                ],
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
                "properties": {
                "customProfilesCount": {
                "type": "integer"
                },
                "endpointTypes": {
                "type": "string"
                },
                "profile": {
                "items": {
                "type": "string"
                },
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
                "required": [
                "profile",
                "customProfilesCount",
                "endpointTypes",
                "totalProfilesCount",
                "uniqueEndpointsCount",
                "unknownEndpointsCount",
                "totalEndpointsCount",
                "unknownEndpointsPercentage"
                ],
                "type": "object"
                },
                "scope": {
                "type": "string"
                }
                },
                "required": [
                "profiles",
                "onlineSubscriptionEnabled",
                "lastAppliedFeedDateTime",
                "scope"
                ],
                "type": "object"
                },
                "type": "array"
                }
                },
                "required": [
                "node"
                ],
                "type": "object"
                }
                },
                "required": [
                "deploymentID",
                "nodeList"
                ],
                "type": "object"
                }
                },
                "required": [
                "networkAccessInfo",
                "profilerInfo",
                "deploymentInfo",
                "nadInfo",
                "mdmInfo",
                "licensesInfo",
                "postureInfo",
                "kongInfo"
                ],
                "type": "object"
                }
                },
                "required": [
                "ERSDeploymentInfo"
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
