# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine NodeDetails API wrapper.

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


class NodeDetails(object):
    """Identity Services Engine NodeDetails API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine NodeDetails
    API and exposes the API as native Python
    methods that return native Python objects.

    | Node Details API allows the client to get deployment node details, get all nodes and filter nodes based on NodeServiceTypes.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**                                   | **Revision Modification** | **Revision Modification**                                                              |
    +----------------+----------------------+-----------------------+---------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------+
    |                |                      |                       |                                                   | **Attribute**             | **Description**                                                                        |
    +----------------+----------------------+-----------------------+---------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------+
    | 0              | 1.0                  | 2.2                   | Initial Cisco ISE Version                         |                           |                                                                                        |
    +----------------+----------------------+-----------------------+---------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------+
    | 1              | 1.1                  | 2.4                   | Support Node Service Types as part of Node Object | NodeServiceTypes          | Added String Field NodeServiceTypes. String represents services configured on the Node |
    +----------------+----------------------+-----------------------+---------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------+
    | 2              | 1.2                  | 2.7                   | Support Node FQDN as part of Node Object          | fqdn                      | Added String Field FQDN. String represents FQDN of the Node                            |
    +----------------+----------------------+-----------------------+---------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------+
    | 3              | 1.3                  | 3.0                   | Support SXP IP Address as part of Node Details    | sxpIpAddress              | Added String Field sxpIpAddress. String represents SXP IP Address of the Node          |
    +----------------+----------------------+-----------------------+---------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------+

    |

    **Resource Definition**

    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | **Attribute**    | **Type** | **Required** | **Description**                     | **Example Values**                   |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | name             | String   | Yes          | Resource Name                       | TestNode                             |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | id               | String   | No           | Resource UUID, mandatory for update | ab6deded-fcc2-47ff-8577-0014737c8fcf |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | description      | String   | No           |                                     |                                      |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | gateWay          | String   | No           |                                     | 10.0.10.11                           |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | displayName      | String   | No           |                                     | TestNode                             |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | inDeployment     | Boolean  | No           |                                     | false                                |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | ipAddresses      | String   | No           |                                     | [ "10.0.0.1", "10.0.0.2" ]           |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | otherPapFqdn     | String   | No           |                                     | OtherTestNode                        |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | ipAddress        | String   | No           |                                     | 10.0.0.3                             |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | sxpIpAddress     | String   | No           |                                     | 10.10.10.1                           |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | nodeServiceTypes | String   | No           |                                     | DEVICE ADMIN                         |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | fqdn             | String   | No           |                                     | test.ers.cisco.com                   |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | primaryPapNode   | Boolean  | No           |                                     | true                                 |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | papNode          | Boolean  | No           |                                     | true                                 |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+
    | pxGridNode       | Boolean  | No           |                                     | true                                 |
    +------------------+----------+--------------+-------------------------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NodeDetails
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NodeDetails, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_node_detail_by_name(self,
                                name,
                                headers=None,
                                **query_parameters):
        """This API allows the client to get node details by name.

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

        e_url = ('/ers/config/node/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab48268c76aa598788a5ebc370226f3a_v3_1_patch_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_node_detail_by_name <#ciscoisesdk.
        api.v3_1_patch_1.node_details.
        NodeDetails.get_node_detail_by_name>`_
        """
        return self.get_node_detail_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_node_detail_by_id(self,
                              id,
                              headers=None,
                              **query_parameters):
        """This API allows the client to get node details by ID.

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

        e_url = ('/ers/config/node/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bb2e9d6651c7bf18c1b60ff7eb14_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_node_detail_by_id <#ciscoisesdk.
        api.v3_1_patch_1.node_details.
        NodeDetails.get_node_detail_by_id>`_
        """
        return self.get_node_detail_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_node_details(self,
                         filter=None,
                         filter_type=None,
                         page=None,
                         size=None,
                         headers=None,
                         **query_parameters):
        """This API allows the client to get all the node details.
        Filter:   [nodeservicetypes]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
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
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/node')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d9b8599f55fc4a1bd9d6ac02619eb_v3_1_patch_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_node_details <#ciscoisesdk.
        api.v3_1_patch_1.node_details.
        NodeDetails.get_node_details>`_
        """
        return self.get_node_details(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_node_details_generator(self,
                                   filter=None,
                                   filter_type=None,
                                   page=None,
                                   size=None,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to get all the node details.
        Filter:   [nodeservicetypes]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
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
            self.get_node_details, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
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
                          headers=None,
                          **query_parameters):
        """Alias for `get_node_details_generator <#ciscoisesdk.
        api.v3_1_patch_1.node_details.
        NodeDetails.get_node_details_generator>`_
        """
        yield from get_next_page(
            self.get_node_details, dict(
                filter=filter,
                filter_type=filter_type,
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
        """This API helps to retrieve the version information realted to
        the node details.

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

        e_url = ('/ers/config/node/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ca9a3d8217d5507aa11020bee82ef228_v3_1_patch_1', _api_response)
