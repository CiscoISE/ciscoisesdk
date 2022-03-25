# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Node Deployment API wrapper.

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


class NodeDeployment(object):
    """Identity Services Engine Node Deployment API (version: 3.1.1).

    Wraps the Identity Services Engine Node Deployment
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NodeDeployment
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NodeDeployment, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_nodes(self,
                  filter=None,
                  filter_type=None,
                  headers=None,
                  **query_parameters):
        """The API lists all the nodes that are deployed in the cluster.
        Returns basic information about each of the deployed
        nodes in the cluster like hostname, status, roles, and
        services.   Supports filtering on FQDN, hostname, IP
        address, roles, services and node status. .

        Args:
            filter(basestring, list, set, tuple): filter query
                parameter.        Simple filtering  is
                available through the filter query
                string parameter. The structure of a
                filter is a triplet of field operator
                and value, separated by dots. More than
                one filter can be sent. The logical
                operator common to all filter criteria
                is AND by default, and can be changed by
                using the  "filterType=or"  query string
                parameter. Each resource Data model
                description should specify if an
                attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
                .
            filter_type(basestring): filterType query parameter. The
                logical operator common to all filter
                criteria is AND by default, and can be
                changed by using this parameter.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/deployment/node')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b95cb82a8954c5a785140a9a8f3156_v3_1_1', _api_response)

    def register_node(self,
                      allow_cert_import=None,
                      fqdn=None,
                      password=None,
                      roles=None,
                      services=None,
                      user_name=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **query_parameters):
        """This API registers a Cisco ISE node to form a multi-node
        deployment.   Approximate execution time 300 seconds. .

        Args:
            allow_cert_import(boolean): Consent to import the self-
                signed certificate of the registering
                node. , property of the request body.
            fqdn(string): fqdn, property of the request body.
            password(string): password, property of the request
                body.
            roles(list): Roles can be empty or have many values for
                a node. , property of the request body
                (list of strings. Available values are
                'PrimaryAdmin',
                'PrimaryDedicatedMonitoring',
                'PrimaryMonitoring', 'SecondaryAdmin',
                'SecondaryDedicatedMonitoring',
                'SecondaryMonitoring' and 'Standalone').
            services(list): Services can be empty or have many
                values for a node. , property of the
                request body (list of strings. Available
                values are 'DeviceAdmin',
                'PassiveIdentity', 'Profiler', 'SXP',
                'Session', 'TC-NAC', 'pxGrid' and
                'pxGridCloud').
            user_name(string): userName, property of the request
                body.
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
            pass

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
            _payload = {
                'allowCertImport':
                    allow_cert_import,
                'fqdn':
                    fqdn,
                'password':
                    password,
                'roles':
                    roles,
                'services':
                    services,
                'userName':
                    user_name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d0ee193cc65780af11ed96b1758755_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/deployment/node')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d0ee193cc65780af11ed96b1758755_v3_1_1', _api_response)

    def get_node_details(self,
                         hostname,
                         headers=None,
                         **query_parameters):
        """This API retrieves detailed information of the deployed node. .

        Args:
            hostname(basestring): hostname path parameter. Hostname
                of the deployed node.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }

        e_url = ('/api/v1/deployment/node/{hostname}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ae8d7c8f33bb52ceb04880845f2f45ba_v3_1_1', _api_response)

    def get_all(self,
                hostname,
                headers=None,
                **query_parameters):
        """Alias for `get_node_details <#ciscoisesdk.
        api.v3_1_1.node_deployment.
        NodeDeployment.get_node_details>`_
        """
        return self.get_node_details(
            hostname=hostname,
            headers=headers,
            **query_parameters
        )

    def update_node(self,
                    hostname,
                    roles=None,
                    services=None,
                    headers=None,
                    payload=None,
                    active_validation=True,
                    **query_parameters):
        """This API updates the configuration of the Cisco ISE node with
        the configuration provided.   Approximate execution time
        300 seconds. .

        Args:
            roles(list): Roles can be empty or have many values for
                a node. , property of the request body
                (list of strings. Available values are
                'PrimaryAdmin',
                'PrimaryDedicatedMonitoring',
                'PrimaryMonitoring', 'SecondaryAdmin',
                'SecondaryDedicatedMonitoring',
                'SecondaryMonitoring' and 'Standalone').
            services(list): Services can be empty or have many
                values for a node. , property of the
                request body (list of strings. Available
                values are 'DeviceAdmin',
                'PassiveIdentity', 'Profiler', 'SXP',
                'Session', 'TC-NAC', 'pxGrid' and
                'pxGridCloud').
            hostname(basestring): hostname path parameter. Hostname
                of the deployed node.
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
            pass

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
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'roles':
                    roles,
                'services':
                    services,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c1fa3bf115c77be99b602aca1493b_v3_1_1')\
                .validate(_payload)

        e_url = ('/api/v1/deployment/node/{hostname}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c1fa3bf115c77be99b602aca1493b_v3_1_1', _api_response)

    def delete_node(self,
                    hostname,
                    headers=None,
                    **query_parameters):
        """The deregistered node becomes a standalone Cisco ISE node.  It
        retains the last configuration that it received from the
        primary PAN and assumes the default roles and services
        of a standalone node.   Approximate execution time 300
        seconds. .

        Args:
            hostname(basestring): hostname path parameter. The
                hostname of the node in the deployment
                to be deregistered.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }

        e_url = ('/api/v1/deployment/node/{hostname}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d26670a205a78800cb50673027a6e_v3_1_1', _api_response)

    def make_primary(self,
                     headers=None,
                     **query_parameters):
        """This API promotes the standalone node on which the API is
        invoked to the primary Policy Administration node (PAN).
        .

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
            pass

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

        e_url = ('/api/v1/deployment/primary')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d2e0f05045c5459824d9f24f2827608_v3_1_1', _api_response)

    def promote_node(self,
                     headers=None,
                     **query_parameters):
        """Execute this API in the secondary PAN in the cluster to promote
        the node to primary PAN.  Ensure that the API Gateway
        setting is enabled in the secondary PAN.   Approximate
        execution time 300 seconds. .

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
            pass

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

        e_url = ('/api/v1/deployment/promote')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f27497451e4aac524c2d7fc4bf0_v3_1_1', _api_response)

    def make_standalone(self,
                        headers=None,
                        **query_parameters):
        """This API changes the primary PAN in a single node cluster on
        which the API is invoked, to a standalone node. .

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
            pass

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

        e_url = ('/api/v1/deployment/standalone')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c63819cf4d3b5854bcbbadbc383236a0_v3_1_1', _api_response)

    def sync_node(self,
                  hostname,
                  headers=None,
                  **query_parameters):
        """Performing a manual synchronization involves a reload of the
        target node, but not the primary PAN.   Approximate
        execution time 300 seconds.

        Args:
            hostname(basestring): hostname path parameter. Hostname
                of the node.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }

        e_url = ('/api/v1/deployment/sync-node/{hostname}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eb4709af3a7528e947ad10d2f2141a8_v3_1_1', _api_response)
