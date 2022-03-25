# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine pxGridNode API wrapper.

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


class PxGridNode(object):
    """Identity Services Engine pxGridNode API (version: 3.1.0).

    Wraps the Identity Services Engine pxGridNode
    API and exposes the API as native Python
    methods that return native Python objects.

    | pxGrid Node API allows the client to retrieve pxGrid information, delete an existing pxGrid node, and approve new pxGrid nodes. **Note:** From Cisco ISE Release 3.1, all pxGrid connections must be based on pxGrid 2.0. pxGrid 1.0-based (XMPP-based) integrations will cease to work on Cisco ISE from Release 3.1 onwards. pxGrid Version 2.0, which is based on WebSockets, was introduced in Cisco ISE Release 2.4. We recommend that you plan and upgrade your other systems to pxGrid 2.0-compliant versions in order to prevent potential disruptions, if any, to integrations.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.4                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +---------------+----------+--------------+-------------------------------------+--------------------------------------+
    | **Attribute** | **Type** | **Required** | **Description**                     | **Example Values**                   |
    +---------------+----------+--------------+-------------------------------------+--------------------------------------+
    | name          | String   | Yes          | Resource Name                       | ers-sample-client                    |
    +---------------+----------+--------------+-------------------------------------+--------------------------------------+
    | id            | String   | No           | Resource UUID, mandatory for update | ab6deded-fcc2-47ff-8577-0014737c8fcf |
    +---------------+----------+--------------+-------------------------------------+--------------------------------------+
    | description   | String   | No           |                                     | ERS sample client                    |
    +---------------+----------+--------------+-------------------------------------+--------------------------------------+
    | status        | String   | No           |                                     | Online (XMPP)                        |
    +---------------+----------+--------------+-------------------------------------+--------------------------------------+
    | authMethod    | String   | No           |                                     | Certificate                          |
    +---------------+----------+--------------+-------------------------------------+--------------------------------------+
    | groups        | String   | No           |                                     |                                      |
    +---------------+----------+--------------+-------------------------------------+--------------------------------------+

    |

    **pxGrid Characterization**

    **Session data Consumption over pxGrid**

    On a 35 node Cisco ISE deployment with a dedicated primary Policy Administration node (PAN), dedicated secondary PAN, dedicated primary Monitoring and Troubleshooting node (MnT node), dedicated secondary MnT, dedicated pxGrid node and 30 heterogeneous Policy Service node (PSN) platforms, there was no delay observed in consuming session data with the following parameters as shown in the table below:

    +----------------------------------------+------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------+
    | **RADIUS Traffic**                     | **Total number of sessions in the deployment** | **Number of pxGrid clients (subscribers to the session topic)** | **pxGrid client’s delay in consuming session data** |
    +----------------------------------------+------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------+
    | Upto 500 transactions per second (TPS) | ~2 million                                     | 50                                                              | No delay                                            |
    +----------------------------------------+------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------+

    **Bulk download time taken**

    On a 35 node Cisco ISE deployment with a dedicated primary PAN, dedicated secondary PAN, dedicated primary MnT, dedicated secondary MnT, dedicated pxGrid node and 30 heterogeneous PSN Platforms, the bulk download time for all the pxGrid clients is shown in the table below:

    +------------------------------------------------+-----------------------------------------------------------------+----------------------------------+
    | **Total number of sessions in the deployment** | **Number of pxGrid clients (subscribers to the session topic)** | **Time taken for bulk download** |
    +------------------------------------------------+-----------------------------------------------------------------+----------------------------------+
    | 2 million                                      | 50                                                              | ~17 minutes                      |
    +------------------------------------------------+-----------------------------------------------------------------+----------------------------------+

    |
    | **Note:** From Cisco ISE Release 3.1, we can use either pxgridnode or pxgridNode in the URL.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PxGridNode
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(PxGridNode, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def approve_px_grid_node(self,
                             name,
                             headers=None,
                             **query_parameters):
        """This API allows the client to approve a pxGrid node. Only
        pending pxGrid nodes can be approved.

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
                           basestring, may_be_none=False)
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

        e_url = ('/ers/config/pxgridnode/name/{name}/approve')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f47d656ed0805859a85e5cc082c78dcf_v3_1_0', _api_response)

    def approve(self,
                name,
                headers=None,
                **query_parameters):
        """Alias for `approve_px_grid_node <#ciscoisesdk.
        api.v3_1_0.px_grid_node.
        PxGridNode.approve_px_grid_node>`_
        """
        return self.approve_px_grid_node(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_px_grid_node_by_name(self,
                                 name,
                                 headers=None,
                                 **query_parameters):
        """This API allows the client to get a pxGrid node by name.

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
                           basestring, may_be_none=False)
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

        e_url = ('/ers/config/pxgridnode/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a9d109aac585a89bdd3fae400064b_v3_1_0', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_px_grid_node_by_name <#ciscoisesdk.
        api.v3_1_0.px_grid_node.
        PxGridNode.get_px_grid_node_by_name>`_
        """
        return self.get_px_grid_node_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def delete_px_grid_node_by_name(self,
                                    name,
                                    headers=None,
                                    **query_parameters):
        """This API deletes a pxGrid node by name.

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
                           basestring, may_be_none=False)
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

        e_url = ('/ers/config/pxgridnode/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e718d5054593b94a2fef39461c24a_v3_1_0', _api_response)

    def delete_by_name(self,
                       name,
                       headers=None,
                       **query_parameters):
        """Alias for `delete_px_grid_node_by_name <#ciscoisesdk.
        api.v3_1_0.px_grid_node.
        PxGridNode.delete_px_grid_node_by_name>`_
        """
        return self.delete_px_grid_node_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_px_grid_node_by_id(self,
                               id,
                               headers=None,
                               **query_parameters):
        """This API allows the client to get a pxGrid node by ID.

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
                           basestring, may_be_none=False)
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

        e_url = ('/ers/config/pxgridnode/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d24ade0b53405fbc898cb0cc1ea57fb8_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_px_grid_node_by_id <#ciscoisesdk.
        api.v3_1_0.px_grid_node.
        PxGridNode.get_px_grid_node_by_id>`_
        """
        return self.get_px_grid_node_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_px_grid_node(self,
                         page=None,
                         size=None,
                         headers=None,
                         **query_parameters):
        """This API allows the client to get all the npxGrid nodes.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
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
                           basestring, may_be_none=False)
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

        _params = {
            'page':
                page,
            'size':
                size,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/pxgridnode')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d97156379640002f79b2007c_v3_1_0', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_px_grid_node <#ciscoisesdk.
        api.v3_1_0.px_grid_node.
        PxGridNode.get_px_grid_node>`_
        """
        return self.get_px_grid_node(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_px_grid_node_generator(self,
                                   page=None,
                                   size=None,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to get all the npxGrid nodes.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
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
            self.get_px_grid_node, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          page=None,
                          size=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_px_grid_node_generator <#ciscoisesdk.
        api.v3_1_0.px_grid_node.
        PxGridNode.get_px_grid_node_generator>`_
        """
        yield from get_next_page(
            self.get_px_grid_node, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the pxGrid node.

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

        e_url = ('/ers/config/pxgridnode/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c2962d70ef5964be55cfeae68e5ba6_v3_1_0', _api_response)
