# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Node Group API wrapper.

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


class NodeGroup(object):
    """Identity Services Engine Node Group API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine Node Group
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NodeGroup
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NodeGroup, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_node_groups(self,
                        headers=None,
                        **query_parameters):
        """This API retrieves the details of all the node groups in the
        cluster.  Each node group retrieved consists of name,
        description and MAR cache details like query-attempts,
        query-timeout, replication-attempts, replication-
        timeout. .

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

        e_url = ('/api/v1/deployment/node-group')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a0824f9a589c58cd8df522524cb550ad_v3_1_patch_1', _api_response)

    def create_node_group(self,
                          description=None,
                          mar_cache=None,
                          name=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """    This API creates a node group in the cluster.  A node group
        is a group of PSNs, where the PSNs maintain a heartbeat
        with each other. It is used primarily to terminate or
        transfer posture-pending sessions when a PSN in a local
        node group fails.  Node group members can communicate
        over TCP/7800.   The following parameters are used in
        the request body of the API:         PARAMETER
        DESCRIPTION   EXAMPLE           name * required   Name
        of the node group( valid-range:  1-100 characters)
        {"name": "site1"}       description   Description of the
        node group ( valid-range:  0-256 characters)   {"name":
        "site2", "description": "sample"}       query-attempts
        The number of times Cisco ISE attempts to perform the
        cache entry query. ( valid-range:  0 5,  default-value:
        1)   {"name": "site3","marCache": {"query-attempts": 1}}
        query-timeout   The time, in seconds, after which a
        cache entry query times out. ( valid-range:  1 10,
        default-value:  2) second(s)   {"name":
        "site4","marCache": {"query-timeout": 2}}
        replication-attempts   The number of times Cisco ISE
        attempts to perform MAR cache entry replication. (
        valid-range:  0 5,  default-value:  2)   {"name":
        "site5","marCache": {"replication-attempts": 2}}
        replication-timeout   The time, in seconds, after which
        the cache entry replication times out. ( valid-range:  1
        10,  default-value:  5) second(s)   {"name":
        "site6","marCache": {"replication-timeout": 5}}
        NOTE 1:  : Node group name and description cannot
        contain any of the following characters: ! % ^ : ; , . ~
        @ # & [ { ( | ) } ] ` > <  / \\ " + = ?  NOTE 2:  :
        Parameter marCache stands for Machine Access Restriction
        (MAR) cache that provides an additional means of
        controlling authorization for Active Directory-
        authentication users. We can enable the marCache for a
        nodegroup by providing key "marCache" in json request.
        Additionally we may also provide any combination of
        parameters query-attempts, query-timeout, replication-
        attempts, replication-timeout in marCache object. If no
        value is specified for a particular parameter its
        default value will be recorded.If no marCache object is
        given, marCache will be considered as disabled.    .

        Args:
            description(string): description, property of the
                request body.
            mar_cache(object): marCache, property of the request
                body.
            name(string): name, property of the request body.
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
                'description':
                    description,
                'marCache':
                    mar_cache,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d5efe180ef459b1a1d9f651e7c1eb92_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/deployment/node-group')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d5efe180ef459b1a1d9f651e7c1eb92_v3_1_patch_1', _api_response)

    def get_node_group(self,
                       node_group_name,
                       headers=None,
                       **query_parameters):
        """This API retrieves the details of a node group in the cluster
        using a node group name.

        Args:
            node_group_name(basestring): nodeGroupName path
                parameter. Name of the existing node
                group.
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
        check_type(node_group_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'nodeGroupName': node_group_name,
        }

        e_url = ('/api/v1/deployment/node-group/{nodeGroupName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c9d1b776015057a59e659c8327ea91a1_v3_1_patch_1', _api_response)

    def update_node_group(self,
                          node_group_name,
                          description=None,
                          mar_cache=None,
                          name=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """    Purpose of this API is to update an existing node group.
        The following parameters are used in the request body of
        the API:         PARAMETER   DESCRIPTION   EXAMPLE
        name * required    Name of the node group existing in
        ISE( valid-range:  1-100 characters)   NOTE :  name of
        an existing node group cannot be modified. "name"
        parameter should be identical to the node group
        name(nodeGroupName) provided in the path     {"name":
        "site1"}       description    Description of the node
        group ( valid-range:  0-256 characters)     {"name":
        "site2", "description": "sample"}       query-attempts
        The number of times Cisco ISE attempts to perform the
        cache entry query. ( valid-range:  0 5,  default-value:
        1)   {"name": "site3","marCache": {"query-attempts": 1}}
        query-timeout   The time, in seconds, after which a
        cache entry query times out. ( valid-range:  1 10,
        default-value:  2) second(s)   {"name":
        "site4","marCache": {"query-timeout": 2}}
        replication-attempts   The number of times Cisco ISE
        attempts to perform MAR cache entry replication. (
        valid-range:  0 5,  default-value:  2)   {"name":
        "site5","marCache": {"replication-attempts": 2}}
        replication-timeout   The time, in seconds, after which
        the cache entry replication times out. ( valid-range:  1
        10,  default-value:  5) second(s)   {"name":
        "site6","marCache": {"replication-timeout": 5}}
        NOTE 1:   Node group name and description cannot contain
        any of the following characters: ! % ^ : ; , . ~ @ # & [
        { ( | ) } ] ` > <  / \\ " + = ?  NOTE 2:   Parameter
        marCache stands for Machine Access Restriction (MAR)
        cache that provides an additional means of controlling
        authorization for Active Directory-authentication users.
        We can enable the marCache for a nodegroup by providing
        key "marCache" in json request. Additionally we may also
        provide any combination of parameters query-attempts,
        query-timeout, replication-attempts, replication-timeout
        in marCache object. If no value is specified for a
        particular parameter its default value will be recorded.
        If no marCache object is given, marCache will be
        disabled.    .

        Args:
            description(string): description, property of the
                request body.
            mar_cache(object): marCache, property of the request
                body.
            name(string): name, property of the request body.
            node_group_name(basestring): nodeGroupName path
                parameter. Name of the existing node
                group.
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
        check_type(node_group_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'nodeGroupName': node_group_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'description':
                    description,
                'marCache':
                    mar_cache,
                'name':
                    name,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fbd772420b8851349aa58fb4a9b006b8_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/deployment/node-group/{nodeGroupName}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_fbd772420b8851349aa58fb4a9b006b8_v3_1_patch_1', _api_response)

    def delete_node_group(self,
                          force_delete,
                          node_group_name,
                          headers=None,
                          **query_parameters):
        """Delete an existing node group in the cluster. Deleting the node
        group does not delete the nodes, but failover is no
        longer carried out among the nodes.

        Args:
            node_group_name(basestring): nodeGroupName path
                parameter. Name of the existing node
                group.
            force_delete(bool): forceDelete query parameter. Force
                delete the group even if the node group
                contains one or more nodes.
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
        check_type(force_delete, bool,
                   may_be_none=False)
        check_type(node_group_name, basestring,
                   may_be_none=False)

        _params = {
            'forceDelete':
                force_delete,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'nodeGroupName': node_group_name,
        }

        e_url = ('/api/v1/deployment/node-group/{nodeGroupName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b2eacaba249e5762874a801f71631ae8_v3_1_patch_1', _api_response)

    def add_node(self,
                 node_group_name,
                 hostname=None,
                 headers=None,
                 payload=None,
                 active_validation=True,
                 **query_parameters):
        """    This API adds a node to the node group in the cluster. When
        a node that belongs to a node group fails, another node
        in the same node group issues a Change of Authorization
        (CoA) for all the URL-redirected sessions on the failed
        node.   The following parameters are used in the request
        body of the API:         PARAMETER   DESCRIPTION
        EXAMPLE           hostname * required   Name of the host
        name    {"hostname": "isenode"}        .

        Args:
            hostname(string): hostname, property of the request
                body.
            node_group_name(basestring): nodeGroupName path
                parameter. Name of the existing node
                group.
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
        check_type(node_group_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'nodeGroupName': node_group_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'hostname':
                    hostname,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fc44ec6afaf95ea9b51dd404abf46e4e_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/deployment/node-group/{nodeGroupName}/add-node')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_fc44ec6afaf95ea9b51dd404abf46e4e_v3_1_patch_1', _api_response)

    def get_nodes(self,
                  node_group_name,
                  headers=None,
                  **query_parameters):
        """This API retrieves the list of nodes associated with a node
        group in the cluster with a given node group name.

        Args:
            node_group_name(basestring): nodeGroupName path
                parameter. Name of the existing node
                group.
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
        check_type(node_group_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'nodeGroupName': node_group_name,
        }

        e_url = ('/api/v1/deployment/node-group/{nodeGroupName}/node')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fe420544d425d3d873632dbb6c1b8c2_v3_1_patch_1', _api_response)

    def remove_node(self,
                    node_group_name,
                    hostname=None,
                    headers=None,
                    payload=None,
                    active_validation=True,
                    **query_parameters):
        """    Purpose of this API is to remove a node from a node group in
        the cluster. Removing node from the node group does not
        delete the node, but failover is no longer carried out
        if the node is not part any node group.   The following
        parameters are used in the request body of the API:
        PARAMETER   DESCRIPTION   EXAMPLE           hostname *
        required   Name of the host name    {"hostname":
        "isenode"}        .

        Args:
            hostname(string): hostname, property of the request
                body.
            node_group_name(basestring): nodeGroupName path
                parameter. Name of the existing node
                group.
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
        check_type(node_group_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'nodeGroupName': node_group_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'hostname':
                    hostname,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b1a343c45952a79d0bbfbadb02002b_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/deployment/node-group/{nodeGroupName}/remove-'
                 + 'node')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b1a343c45952a79d0bbfbadb02002b_v3_1_patch_1', _api_response)
