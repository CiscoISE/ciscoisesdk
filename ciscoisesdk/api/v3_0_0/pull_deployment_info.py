# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine PullDeploymentInfo API wrapper.

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

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)
from ...pagination import get_next_page


class PullDeploymentInfo(object):
    """Identity Services Engine PullDeploymentInfo API (version: 3.0.0).

    Wraps the Identity Services Engine PullDeploymentInfo
    API and exposes the API as native Python
    methods that return native Python objects.

    Pull Deployment Info API allows clients to get the complete information about a Cisco ISE deployment. The information includes details about the deployment, network zccess, NADs, MDMs, licenses, posture and profiler.

    Revision History
    ----------------

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.7                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    Resource Definition
    -------------------

    **Attribute**

    **Type**

    **Required**

    **Description**

    **Example Values**

    name

    String

    Yes

    Resource Name

    id

    String

    No

    Resource UUID, mandatory for update

    description

    String

    No

    networkAccessInfo

    List

    No

    networkAccessInfo Details

    - deploymentID

    String

    Yes

    Deployment ID

    8f0d1566-6e6c-48ad-abe0-ef2d813a2a11

    - isCsnEnabled

    Boolean

    Yes

    false

    - nodeList

    List

    Yes

    Node list

      - nodeAndScope

    List

    No

    | Includes 'content' which is an array of dictionaries describing various attributes with the properties:
    | - name (String),
    | - declaredType (String),
    | - scope (String),
    | - value (Varies),
    | - nil (Boolean),
    | - globalScope (Boolean),
    | - typeSubstituted (Boolean)

    | ["deployment",
    | "content": {
    |   "name": "{http://www.cisco.com/NetworkAccessInfo}AuthorizationInfo",
    |   "declaredType": "com.cisco.cpm.infrastructure.telemetry.jaxbgen.NetworkAccessInfo$NodeList$Node$AuthorizationInfo",
    |   "scope": "com.cisco.cpm.infrastructure.telemetry.jaxbgen.NetworkAccessInfo$NodeList$Node",
    |   "value": {
    |     "policyLineCount": 0,
    |     "activeVLANCount": 0,
    |     "activedACLCount": 4
    |   },
    |   "nil": false,
    |   "globalScope": false,
    |   "typeSubstituted": false
    | }
    | ]

    - sdaVNs

    List

    No

    - trustSecControl

    String

    No

    ISE

    - radius3RdParty

    List

    No

    profilerInfo

    List

    No

    profilerInfo Details

    - deploymentID

    String

    Yes

    Deployment ID

    8f0d1566-6e6c-48ad-abe0-ef2d813a2a11

    - nodeList

    List

    Yes

    Node list

      - node

    List

    No

    | Includes 'profiles' which is an array of dictionaries describing various attributes with the properties:
    | - profile (List),
    | - customProfilesCount (Integer),
    | - endpointTypes (String),
    | - totalProfilesCount (Integer),
    | - uniqueEndpointsCount (Integer),
    | - unknownEndpointsCount (Integer),
    | - totalEndpointsCount (Integer),
    | - unknownEndpointsPercentage (Integer)

    | [
    | {
    |   "profiles": {
    |     "profile": [],
    |     "customProfilesCount": 0,
    |     "endpointTypes": "",
    |     "totalProfilesCount": 676,
    |     "uniqueEndpointsCount": 0,
    |     "unknownEndpointsCount": 0,
    |     "totalEndpointsCount": 0,
    |    "unknownEndpointsPercentage": 0
    |   },
    |   "onlineSubscriptionEnabled": true,
    |   "lastAppliedFeedDateTime": "2021-03-30T01:06:01.621+00:00",
    |   "scope": "deployment"
    | }
    | ]

    deploymentInfo

    List

    No

    deploymentInfo Details

    - deploymentID

    String

    Yes

    Deployment ID

    8f0d1566-6e6c-48ad-abe0-ef2d813a2a11

    - versionHistoryInfo

    List

    No

    | Array of dictionaries describing various attributes with the properties:
    | - opType (String),
    | - mainVersion (String),
    | - epochTime (Integer)

    | [
    | {
    |   "opType": "Application Install",
    |   "mainVersion": "3.1.0.280",
    |   "epochTime": 1614847786000
    | }
    | ]

    - nodeList

    List

    Yes

    Node list

      - nodeAndNodeCountAndCountInfo

    List

    No

    | Includes 'content' which is an array of dictionaries describing various attributes with the properties:
    | - name (String),
    | - declaredType (String),
    | - scope (String),
    | - value (Varies),
    | - nil (Boolean),
    | - globalScope (Boolean),
    | - typeSubstituted (Boolean)

    | [
    | {
    |   "name": "{http://www.cisco.com/DeploymentInfo}NodeTypes",
    |   "declaredType": "java.lang.String",
    |   "scope": "com.cisco.cpm.infrastructure.telemetry.jaxbgen.DeploymentInfo$NodeList$Node",
    |   "value": "PAP,MNT,PDP,PXG",
    |   "nil": false,
    |   "globalScope": false,
    |   "typeSubstituted": false
    | }
    | ]

    - fipsstatus

    String

    No

    Disabled

    nadInfo

    List

    No

    nadInfo Details

    - deploymentID

    String

    Yes

    Deployment ID

    8f0d1566-6e6c-48ad-abe0-ef2d813a2a11

    - nodeList

    List

    Yes

    Node list

      - nodeAndScope

    List

    No

    | Includes 'content' which is an array of dictionaries describing various attributes with the properties:
    | - name (String),
    | - declaredType (String),
    | - scope (String),
    | - value (List),
    | - nil (Boolean),
    | - globalScope (Boolean),
    | - typeSubstituted (Boolean)

    | ["deployment",
    | "content": [
    |  {
    |     "name": "{http://www.cisco.com/NADInfo}NADProfileInfo",
    |     "declaredType": "com.cisco.cpm.infrastructure.telemetry.jaxbgen.NADInfo$NodeList$Node$NADProfileInfo",
    |     "scope": "com.cisco.cpm.infrastructure.telemetry.jaxbgen.NADInfo$NodeList$Node",
    |     "value": {
    |       "name": "Cisco",
    |       "isCiscoProvided": true,
    |       "isDefProfile": true, "isTacacsSupported": true,
    |       "isRadiusSupported": true,
    |       "isTrustSecSupported": true,
    |       "activeNADCount": 0,
    |       "totalNADCount": 0
    |     },
    |     "nil": false,
    |     "globalScope": false,
    |     "typeSubstituted": false
    |   }
    |   ]
    | }
    | ]

    - nadcountInfo

    List

    No

      - totalActiveNADCount

    Integer

    No

    0

    mdmInfo

    List

    No

    mdmInfo Details

    - activeMdmServersCount

    Integer

    Yes

    0

    - activeDesktopMdmServersCount

    Integer

    Yes

    0

    - activeMobileMdmServersCount

    Integer

    Yes

    0

    - deploymentID

    String

    Yes

    Deployment ID

    8f0d1566-6e6c-48ad-abe0-ef2d813a2a11

    - nodeList

    List

    Yes

    Node list

      - nodeAndScope

    List

    No

    | Includes 'content' which is an array of dictionaries describing various attributes with the properties:
    | - name (String),
    | - declaredType (String),
    | - scope (String),
    | - value (Varies),
    | - nil (Boolean),
    | - globalScope (Boolean),
    | - typeSubstituted (Boolean)

    | [
    | "deployment",
    |   {
    |     "content": []
    |   }
    | ]

    licensesInfo

    List

    No

    licensesInfo Details

    - deploymentID

    String

    Yes

    Deployment ID

    8f0d1566-6e6c-48ad-abe0-ef2d813a2a11

    - nodeList

    List

    Yes

    Node list

      - nodeAndScope

    List

    No

    | Includes 'content' which is an array of dictionaries describing various attributes with the properties:
    | - name (String),
    | - declaredType (String),
    | - scope (String),
    | - value (Varies),
    | - nil (Boolean),
    | - globalScope (Boolean),
    | - typeSubstituted (Boolean)

    | [
    | {
    |   "content": [
    |     {
    |     "name": "{http://www.cisco.com/LicenseInfo}SmartAccountName",
    |     "declaredType": "java.lang.String",
    |     "scope": "com.cisco.cpm.infrastructure.telemetry.jaxbgen.LicensesInfo$NodeList$Node",
    |     "value": "",
    |     "nil": false,
    |     "globalScope": false,
    |     "typeSubstituted": false
    |     }
    |   ]
    | }
    | ]

    postureInfo

    List

    No

    postureInfo Details

    - content

    List

    Yes

    | Array of dictionaries describing various attributes with the properties:
    | - name (String),
    | - declaredType (String),
    | - scope (String),
    | - value (Varies),
    | - nil (Boolean),
    | - globalScope (Boolean),
    | - typeSubstituted (Boolean)

    | [
    | {
    |   "name": "{http://www.cisco.com/PostureInfo}ActivePoliciesCount",
    |   "declaredType": "java.lang.Integer",
    |   "scope": "com.cisco.cpm.infrastructure.telemetry.jaxbgen.PostureInfo",
    |   "value": 0,
    |   "nil": false,
    |   "globalScope": false,
    |   "typeSubstituted": false
    | }
    | ]

    kongInfo

    List

    No

    kongInfo Details

    - deploymentID

    String

    Yes

    Deployment ID

    8f0d1566-6e6c-48ad-abe0-ef2d813a2a11

    - nodeList

    List

    Yes

    Node list

      - node

    List

    No

    | Array of dictionaries describing various attributes with the properties:
    | - sn (String),
    | - service (List)

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PullDeploymentInfo
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PullDeploymentInfo, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_deployment_info(self,
                            timeout=None,
                            headers=None,
                            **query_parameters):
        """This API allows the client to pull the deployment information.

        Args:
            timeout(float, tuple): How long to wait for the server to send
                data before giving up.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/deploymentinfo/getAllInfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              timeout=timeout or self._session.single_request_timeout)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              timeout=timeout or self._session.single_request_timeout)

        return self._object_factory('bpm_f9159c9f9a1951568daee7080e1dda47_v3_0_0', _api_response)

    def get_all(self,
                timeout=None,
                headers=None,
                **query_parameters):
        """Alias for `get_deployment_info <#ciscoisesdk.
        api.v3_0_0.pull_deployment_info.
        PullDeploymentInfo.get_deployment_info>`_
        """
        return self.get_deployment_info(
            timeout=timeout,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the pull deployment info.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/deploymentinfo/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cc09209259dcbde7c851b5a6eda6_v3_0_0', _api_response)
