# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine endpoint API wrapper.

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

from builtins import *

from past.builtins import basestring

from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class Endpoint(object):
    """Identity Services Engine endpoint API (version: 3.1.1).

    Wraps the Identity Services Engine endpoint
    API and exposes the API as native Python
    methods that return native Python objects.

    | Endpoint API allows the client to add, delete, update, search, register and de-register endpoints. Please note that each API description shows whether the API is supported in bulk operation. The Bulk section is showing only 'create' bulk operation however, all other operation which are bulk supported can be used in same way.

    **Revision History**

    +------------+------------------+---------------------+-------------------------------+-------------------------+-------------------------------------------------------------------------------------------------------+
    | Revision # | Resource Version | Cisco   ISE Version | Description                   | Revision   Modification |                                                                                                       |
    +------------+------------------+---------------------+-------------------------------+-------------------------+-------------------------------------------------------------------------------------------------------+
    |            |                  |                     |                               | Attribute               | Description                                                                                           |
    +------------+------------------+---------------------+-------------------------------+-------------------------+-------------------------------------------------------------------------------------------------------+
    | 0          | 1.0              | 1.3                 | Initial Cisco ISE Version     |                         |                                                                                                       |
    +------------+------------------+---------------------+-------------------------------+-------------------------+-------------------------------------------------------------------------------------------------------+
    | 1          | 1.1              | 2.1                 | Cisco ISE 2.1   model changes | customAttributes        | Added custom attibutes for the   user to include custom attributes when adding endpoints to Cisco ISE |
    +------------+------------------+---------------------+-------------------------------+-------------------------+-------------------------------------------------------------------------------------------------------+
    | 2          | 1.2              | 2.2                 | Cisco ISE 2.2 model changes   | apiAdded                | Added custom   operation to get list of rejected endpoints: '/getrejectedendpoints'                   |
    +------------+------------------+---------------------+-------------------------------+-------------------------+-------------------------------------------------------------------------------------------------------+
    |            |                  |                     |                               | apiAdded                | Added custom   operation to release rejected endpoint: '{id}/releaserejectedendpoint'                 |
    +------------+------------------+---------------------+-------------------------------+-------------------------+-------------------------------------------------------------------------------------------------------+

    |

    **Resource Definition**

    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | **Attribute**           | **Type** | **Required** | **Description**                     | **Example Values**                   |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | name                    | String   | Yes          | Resource Name                       | 11:22:33:44:55:66                    |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | id                      | String   | No           | Resource UUID, mandatory for update | 172f8270-8f4f-11eb-b4a8-9eb04987ed29 |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | description             | String   | No           |                                     | MyEndpoint                           |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | customAttributes        | Map      | No           | Key value map                       | {"key1" : "value1"}                  |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | groupId                 | String   | Yes          |                                     | aa13bb40-8bff-11e6-996c-525400b48521 |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | identityStore           | String   | No           |                                     | identityStore                        |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | identityStoreId         | String   | No           |                                     | identityStoreId                      |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | mac                     | String   | Yes          |                                     | 11:22:33:44:55:66                    |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | portalUser              | String   | No           |                                     | portalUser                           |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | profileId               | String   | No           |                                     | profileId                            |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | staticGroupAssignment   | Boolean  | Yes          |                                     | true                                 |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | staticProfileAssignment | Boolean  | Yes          |                                     | false                                |
    +-------------------------+----------+--------------+-------------------------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Endpoint
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Endpoint, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def release_rejected_endpoint(self,
                                  id,
                                  headers=None,
                                  **query_parameters):
        """This API allows the client to release a rejected endpoint.

        Args:
            id(basestring): id path parameter.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/endpoint/{id}/releaserejectedendpoint')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f4f97557daacb3dadaced526cc_v3_1_1', _api_response)

    def release_rejected(self,
                         id,
                         headers=None,
                         **query_parameters):
        """Alias for `release_rejected_endpoint <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.release_rejected_endpoint>`_
        """
        return self.release_rejected_endpoint(
            id=id,
            headers=headers,
            **query_parameters
        )

    def deregister_endpoint(self,
                            id,
                            headers=None,
                            **query_parameters):
        """This API allows the client to de-register an endpoint.

        Args:
            id(basestring): id path parameter.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/endpoint/{id}/deregister')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed121b2686e85bd5b28c068c3c0de220_v3_1_1', _api_response)

    def deregister(self,
                   id,
                   headers=None,
                   **query_parameters):
        """Alias for `deregister_endpoint <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.deregister_endpoint>`_
        """
        return self.deregister_endpoint(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_rejected_endpoints(self,
                               headers=None,
                               **query_parameters):
        """This API allows the client to get the rejected endpoints.

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

        e_url = ('/ers/config/endpoint/getrejectedendpoints')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f8a2f0834e625822bed1cb4cf34fde5e_v3_1_1', _api_response)

    def get_rejected(self,
                     headers=None,
                     **query_parameters):
        """Alias for `get_rejected_endpoints <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.get_rejected_endpoints>`_
        """
        return self.get_rejected_endpoints(
            headers=headers,
            **query_parameters
        )

    def get_endpoint_by_name(self,
                             name,
                             headers=None,
                             **query_parameters):
        """This API allows the client to get an endpoint by name.

        Args:
            name(basestring): name path parameter.
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
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/ers/config/endpoint/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d53842e83f0538cab91e097aa6800ce_v3_1_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_endpoint_by_name <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.get_endpoint_by_name>`_
        """
        return self.get_endpoint_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_endpoint_by_id(self,
                           id,
                           headers=None,
                           **query_parameters):
        """This API allows the client to get an endpoint by ID.

        Args:
            id(basestring): id path parameter.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/endpoint/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eb8e0ce63376573995a49178435f7747_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_endpoint_by_id <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.get_endpoint_by_id>`_
        """
        return self.get_endpoint_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_endpoint_by_id(self,
                              id,
                              custom_attributes=None,
                              description=None,
                              group_id=None,
                              identity_store=None,
                              identity_store_id=None,
                              mac=None,
                              mdm_attributes=None,
                              name=None,
                              portal_user=None,
                              profile_id=None,
                              static_group_assignment=None,
                              static_profile_assignment=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """This API allows the client to update an endpoint.

        Args:
            custom_attributes(object): customAttributes, property of
                the request body.
            description(string): description, property of the
                request body.
            group_id(string): groupId, property of the request body.
            id(string): id, property of the request body.
            identity_store(string): identityStore, property of the
                request body.
            identity_store_id(string): identityStoreId, property of
                the request body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): mdmAttributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
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
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'mac':
                    mac,
                'profileId':
                    profile_id,
                'staticProfileAssignment':
                    static_profile_assignment,
                'groupId':
                    group_id,
                'staticGroupAssignment':
                    static_group_assignment,
                'portalUser':
                    portal_user,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'mdmAttributes':
                    mdm_attributes,
                'customAttributes':
                    custom_attributes,
            }
            _payload = {
                'ERSEndPoint': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c8b30af4b84b5a90be2fc152cf26ad42_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c8b30af4b84b5a90be2fc152cf26ad42_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     custom_attributes=None,
                     description=None,
                     group_id=None,
                     identity_store=None,
                     identity_store_id=None,
                     mac=None,
                     mdm_attributes=None,
                     name=None,
                     portal_user=None,
                     profile_id=None,
                     static_group_assignment=None,
                     static_profile_assignment=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_endpoint_by_id <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.update_endpoint_by_id>`_
        """
        return self.update_endpoint_by_id(
            id=id,
            custom_attributes=custom_attributes,
            description=description,
            group_id=group_id,
            identity_store=identity_store,
            identity_store_id=identity_store_id,
            mac=mac,
            mdm_attributes=mdm_attributes,
            name=name,
            portal_user=portal_user,
            profile_id=profile_id,
            static_group_assignment=static_group_assignment,
            static_profile_assignment=static_profile_assignment,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_endpoint_by_id(self,
                              id,
                              headers=None,
                              **query_parameters):
        """This API deletes an endpoint.

        Args:
            id(basestring): id path parameter.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/endpoint/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f1cac5f578ab6509196266ad8e3_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_endpoint_by_id <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.delete_endpoint_by_id>`_
        """
        return self.delete_endpoint_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def register_endpoint(self,
                          custom_attributes=None,
                          description=None,
                          group_id=None,
                          id=None,
                          identity_store=None,
                          identity_store_id=None,
                          mac=None,
                          mdm_attributes=None,
                          name=None,
                          portal_user=None,
                          profile_id=None,
                          static_group_assignment=None,
                          static_profile_assignment=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """This API allows the client to register an endpoint.

        Args:
            custom_attributes(object): customAttributes, property of
                the request body.
            description(string): description, property of the
                request body.
            group_id(string): groupId, property of the request body.
            id(string): id, property of the request body.
            identity_store(string): identityStore, property of the
                request body.
            identity_store_id(string): identityStoreId, property of
                the request body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): mdmAttributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
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
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'mac':
                    mac,
                'profileId':
                    profile_id,
                'staticProfileAssignment':
                    static_profile_assignment,
                'groupId':
                    group_id,
                'staticGroupAssignment':
                    static_group_assignment,
                'portalUser':
                    portal_user,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'mdmAttributes':
                    mdm_attributes,
                'customAttributes':
                    custom_attributes,
            }
            _payload = {
                'ERSEndPoint': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dfaeea899c185169ae2a3b70b5491008_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint/register')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_dfaeea899c185169ae2a3b70b5491008_v3_1_1', _api_response)

    def register(self,
                 custom_attributes=None,
                 description=None,
                 group_id=None,
                 id=None,
                 identity_store=None,
                 identity_store_id=None,
                 mac=None,
                 mdm_attributes=None,
                 name=None,
                 portal_user=None,
                 profile_id=None,
                 static_group_assignment=None,
                 static_profile_assignment=None,
                 headers=None,
                 payload=None,
                 active_validation=True,
                 **query_parameters):
        """Alias for `register_endpoint <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.register_endpoint>`_
        """
        return self.register_endpoint(
            custom_attributes=custom_attributes,
            description=description,
            group_id=group_id,
            id=id,
            identity_store=identity_store,
            identity_store_id=identity_store_id,
            mac=mac,
            mdm_attributes=mdm_attributes,
            name=name,
            portal_user=portal_user,
            profile_id=profile_id,
            static_group_assignment=static_group_assignment,
            static_profile_assignment=static_profile_assignment,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_endpoints(self,
                      filter=None,
                      filter_type=None,
                      page=None,
                      size=None,
                      sortasc=None,
                      sortdsc=None,
                      headers=None,
                      **query_parameters):
        """This API allows the client to get all the endpoints.   Filter:
        Filters can be used to filter out Endpoints based on a
        set of attributes. This API currently provides the
        following filters:  [logicalProfileName, portalUser,
        staticProfileAssignment, profileId, profile, groupId,
        staticGroupAssignment, mac]   Example 1:   The
        logicalProfileName  filter can be used to get Enpoints
        that belong  to a specific Logical Profile. The
        supported operator for logicalProfileNamefilter is EQ
        (equal to). The syntax to invoke the API with this
        filter:   /ers/config/endpoint?filter={filter
        name}.{operator}.{logical profile name}   Example:
        https://{ise-ip}:9060/ers/config/endpoint?filter=logical
        ProfileName.EQ.LP_Apple   Example 2:   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting: [name, description].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
            filter(basestring, list, set, tuple): filter query
                parameter.               **Simple
                filtering** should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or" query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.              (Operator:
                Description),
                (EQ: Equals),               (NEQ: Not
                Equals),               (GT: Greater
                Than),               (LT: Less Then),
                (STARTSW: Starts With),
                (NSTARTSW: Not Starts With),
                (ENDSW: Ends With),
                (NENDSW: Not Ends With),
                (CONTAINS: Contains),
                (NCONTAINS: Not Contains),
                .
            filter_type(basestring): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
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
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sortasc, basestring)
        check_type(sortdsc, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sortasc':
                sortasc,
            'sortdsc':
                sortdsc,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/endpoint')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b7f7285d71be4645db91b0fc74_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_endpoints <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.get_endpoints>`_
        """
        return self.get_endpoints(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_endpoints_generator(self,
                                filter=None,
                                filter_type=None,
                                page=None,
                                size=None,
                                sortasc=None,
                                sortdsc=None,
                                headers=None,
                                **query_parameters):
        """This API allows the client to get all the endpoints.   Filter:
        Filters can be used to filter out Endpoints based on a
        set of attributes. This API currently provides the
        following filters:  [logicalProfileName, portalUser,
        staticProfileAssignment, profileId, profile, groupId,
        staticGroupAssignment, mac]   Example 1:   The
        logicalProfileName  filter can be used to get Enpoints
        that belong  to a specific Logical Profile. The
        supported operator for logicalProfileNamefilter is EQ
        (equal to). The syntax to invoke the API with this
        filter:   /ers/config/endpoint?filter={filter
        name}.{operator}.{logical profile name}   Example:
        https://{ise-ip}:9060/ers/config/endpoint?filter=logical
        ProfileName.EQ.LP_Apple   Example 2:   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting: [name, description].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
            filter(basestring, list, set, tuple): filter query
                parameter.               **Simple
                filtering** should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or" query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.              (Operator:
                Description),
                (EQ: Equals),               (NEQ: Not
                Equals),               (GT: Greater
                Than),               (LT: Less Then),
                (STARTSW: Starts With),
                (NSTARTSW: Not Starts With),
                (ENDSW: Ends With),
                (NENDSW: Not Ends With),
                (CONTAINS: Contains),
                (NCONTAINS: Not Contains),
                .
            filter_type(basestring): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.

              + RestResponse: REST response with following properties:

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

        yield from get_next_page(
            self.get_endpoints, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sortasc=None,
                          sortdsc=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_endpoints_generator <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.get_endpoints_generator>`_
        """
        yield from get_next_page(
            self.get_endpoints, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_endpoint(self,
                        custom_attributes=None,
                        description=None,
                        group_id=None,
                        identity_store=None,
                        identity_store_id=None,
                        mac=None,
                        mdm_attributes=None,
                        name=None,
                        portal_user=None,
                        profile_id=None,
                        static_group_assignment=None,
                        static_profile_assignment=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **query_parameters):
        """This API creates an endpoint.

        Args:
            custom_attributes(object): customAttributes, property of
                the request body.
            description(string): description, property of the
                request body.
            group_id(string): groupId, property of the request body.
            identity_store(string): identityStore, property of the
                request body.
            identity_store_id(string): identityStoreId, property of
                the request body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): mdmAttributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
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
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'name':
                    name,
                'description':
                    description,
                'mac':
                    mac,
                'profileId':
                    profile_id,
                'staticProfileAssignment':
                    static_profile_assignment,
                'groupId':
                    group_id,
                'staticGroupAssignment':
                    static_group_assignment,
                'portalUser':
                    portal_user,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'mdmAttributes':
                    mdm_attributes,
                'customAttributes':
                    custom_attributes,
            }
            _payload = {
                'ERSEndPoint': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ab88be5092bf4ba9f522e8e26f_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ab88be5092bf4ba9f522e8e26f_v3_1_1', _api_response)

    def create(self,
               custom_attributes=None,
               description=None,
               group_id=None,
               identity_store=None,
               identity_store_id=None,
               mac=None,
               mdm_attributes=None,
               name=None,
               portal_user=None,
               profile_id=None,
               static_group_assignment=None,
               static_profile_assignment=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_endpoint <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.create_endpoint>`_
        """
        return self.create_endpoint(
            custom_attributes=custom_attributes,
            description=description,
            group_id=group_id,
            identity_store=identity_store,
            identity_store_id=identity_store_id,
            mac=mac,
            mdm_attributes=mdm_attributes,
            name=name,
            portal_user=portal_user,
            profile_id=profile_id,
            static_group_assignment=static_group_assignment,
            static_profile_assignment=static_profile_assignment,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the endpoint.

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

        e_url = ('/ers/config/endpoint/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_adcb1d998d54838add3b4d644242af_v3_1_1', _api_response)

    def bulk_request_for_endpoint(self,
                                  operation_type=None,
                                  resource_media_type=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """This API allows the client to submit the bulk request.

        Args:
            operation_type(string): operationType, property of the
                request body.
            resource_media_type(string): resourceMediaType, property
                of the request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
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
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'operationType':
                    operation_type,
                'resourceMediaType':
                    resource_media_type,
            }
            _payload = {
                'EndpointBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c03505504e8e5af8a715e27c40f16eab_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c03505504e8e5af8a715e27c40f16eab_v3_1_1', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_endpoint <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.bulk_request_for_endpoint>`_
        """
        return self.bulk_request_for_endpoint(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_endpoint(self,
                                     bulkid,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to monitor the bulk request.

        Args:
            bulkid(basestring): bulkid path parameter.
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
        check_type(bulkid, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'bulkid': bulkid,
        }

        e_url = ('/ers/config/endpoint/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b054a43ba875f0da3da5a7d863f3ef7_v3_1_1', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_endpoint <#ciscoisesdk.
        api.v3_1_1.endpoint.
        Endpoint.monitor_bulk_status_endpoint>`_
        """
        return self.monitor_bulk_status_endpoint(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )
