# -*- coding: utf-8 -*-
"""Identity Services Engine createLdap data model.

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


class JSONSchemaValidatorC5614142C07C59EaA3CbC297Cad57E39(object):
    """createLdap request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC5614142C07C59EaA3CbC297Cad57E39, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ERSLdap": {
                "properties": {
                "attributes": {
                "properties": {
                "attributes": {
                "items": {},
                "type": "array"
                }
                },
                "type": "object"
                },
                "connectionSettings": {
                "properties": {
                "alwaysAccessPrimaryFirst": {
                "type": "boolean"
                },
                "failbackRetryDelay": {
                "type": "number"
                },
                "failoverToSecondary": {
                "type": "boolean"
                },
                "ldapNodeData": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "primaryHostname": {
                "type": "string"
                },
                "primaryPort": {
                "type": "number"
                },
                "secondaryHostname": {
                "type": "string"
                },
                "secondaryPort": {
                "type": "number"
                }
                }
                },
                "type": "array"
                },
                "primaryServer": {
                "properties": {
                "adminDN": {
                "type": "string"
                },
                "adminPassword": {
                "type": "string"
                },
                "enableForceReconnect": {
                "type": "boolean"
                },
                "enableSecureConnection": {
                "type": "boolean"
                },
                "enableServerIdentityCheck": {
                "type": "boolean"
                },
                "forceReconnectTime": {
                "type": "number"
                },
                "hostName": {
                "type": "string"
                },
                "issuerCACertificate": {
                "type": "string"
                },
                "maxConnections": {
                "type": "number"
                },
                "port": {
                "type": "number"
                },
                "serverTimeout": {
                "type": "number"
                },
                "trustCertificate": {
                "type": "string"
                },
                "useAdminAccess": {
                "type": "boolean"
                }
                },
                "required": [
                "hostName",
                "port",
                "trustCertificate"
                ],
                "type": "object"
                },
                "secondaryServer": {
                "properties": {
                "adminDN": {
                "type": "string"
                },
                "adminPassword": {
                "type": "string"
                },
                "enableForceReconnect": {
                "type": "boolean"
                },
                "enableSecureConnection": {
                "type": "boolean"
                },
                "enableServerIdentityCheck": {
                "type": "boolean"
                },
                "forceReconnectTime": {
                "type": "number"
                },
                "hostName": {
                "type": "string"
                },
                "issuerCACertificate": {
                "type": "string"
                },
                "maxConnections": {
                "type": "number"
                },
                "port": {
                "type": "number"
                },
                "serverTimeout": {
                "type": "number"
                },
                "trustCertificate": {
                "type": "string"
                },
                "useAdminAccess": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "specifyServerForEachISENode": {
                "type": "boolean"
                }
                },
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "directoryOrganization": {
                "properties": {
                "groupDirectorySubtree": {
                "type": "string"
                },
                "macFormat": {
                "type": "object"
                },
                "prefixSeparator": {
                "type": "string"
                },
                "stripPrefix": {
                "type": "boolean"
                },
                "stripSuffix": {
                "type": "string"
                },
                "suffixSeparator": {
                "type": "string"
                },
                "userDirectorySubtree": {
                "type": "string"
                }
                },
                "required": [
                "groupDirectorySubtree",
                "macFormat",
                "userDirectorySubtree"
                ],
                "type": "object"
                },
                "enablePasswordChangeLDAP": {
                "type": "boolean"
                },
                "generalSettings": {
                "properties": {
                "certificate": {
                "type": "string"
                },
                "groupMapAttributeName": {
                "type": "string"
                },
                "groupMemberReference": {
                "type": "object"
                },
                "groupNameAttribute": {
                "type": "string"
                },
                "groupObjectClass": {
                "type": "string"
                },
                "schema": {
                "type": "object"
                },
                "userInfoAttributes": {
                "properties": {
                "additionalAttribute": {
                "type": "string"
                },
                "country": {
                "type": "string"
                },
                "department": {
                "type": "string"
                },
                "email": {
                "type": "string"
                },
                "firstName": {
                "type": "string"
                },
                "jobTitle": {
                "type": "string"
                },
                "lastName": {
                "type": "string"
                },
                "locality": {
                "type": "string"
                },
                "organizationalUnit": {
                "type": "string"
                },
                "stateOrProvince": {
                "type": "string"
                },
                "streetAddress": {
                "type": "string"
                },
                "telephone": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "userNameAttribute": {
                "type": "string"
                },
                "userObjectClass": {
                "type": "string"
                }
                },
                "required": [
                "schema"
                ],
                "type": "object"
                },
                "groups": {
                "properties": {
                "groupsNames": {
                "items": {},
                "type": "array"
                }
                },
                "type": "object"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "required": [
                "name"
                ]
                }
                },
                "required": [
                "ERSLdap"
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
