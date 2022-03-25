# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SecurityGroupToVirtualNetwork API wrapper.

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


class SecurityGroupToVirtualNetwork(object):
    """Identity Services Engine SecurityGroupToVirtualNetwork API (version: 3.1.1).

    Wraps the Identity Services Engine SecurityGroupToVirtualNetwork
    API and exposes the API as native Python
    methods that return native Python objects.

    | SGT mapping to virtual networks are mapped to referenced vlan. These constructs come from out side of Cisco ISE and are not CRUDable inside Cisco ISE.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | 0              | 1.0                  | 2.3                   | Initial Cisco ISE Version |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+

    |

    **Resource Definition**

    +--------------------+-------------+--------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------+
    | **Attribute**      | **Type**    | **Required** | **Description**                                                                                       | **Example Values**                                   |
    +--------------------+-------------+--------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------+
    | name               | String      | Yes          | Resource Name                                                                                         | name                                                 |
    +--------------------+-------------+--------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------+
    | id                 | String      | No           | Resource UUID, mandatory for update                                                                   | 1af3d6e2-cc3b-4603-b80f-6827768335ab                 |
    +--------------------+-------------+--------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------+
    | description        | String      | No           |                                                                                                       | description                                          |
    +--------------------+-------------+--------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------+
    | sgtId              | String      | No           |                                                                                                       | sgt_id                                               |
    +--------------------+-------------+--------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------+
    | virtualnetworklist | List        | No           | Includes 'vlans' which is an array of dictionaries describing various attributes with the properties: | [                                                    |
    |                    |             |              | - id (String),                                                                                        | {                                                    |
    |                    |             |              | - name (String),                                                                                      |   "id" : "1af3d6e2-cc3b-4603-b80f-6827768335ab",     |
    |                    |             |              | - description (String),                                                                               |   "name" : "virtual1",                               |
    |                    |             |              | - defaultVlan (Boolean),                                                                              |   "description" : "description",                     |
    |                    |             |              | - maxValue (Integer),                                                                                 |   "defaultVirtualNetwork" : false,                   |
    |                    |             |              | - data (Boolean)                                                                                      |   "vlans" : [                                        |
    |                    |             |              |                                                                                                       |     {                                                |
    |                    |             |              |                                                                                                       |       "id" : "1af3d6e2-cc3b-4603-b80f-6827768335ab", |
    |                    |             |              |                                                                                                       |       "name" : "vlan1",                              |
    |                    |             |              |                                                                                                       |       "description" : "description1",                |
    |                    |             |              |                                                                                                       |       "defaultVlan" : true,                          |
    |                    |             |              |                                                                                                       |       "maxValue" : 1882725260,                       |
    |                    |             |              |                                                                                                       |       "data" : true                                  |
    |                    |             |              |                                                                                                       |    }                                                 |
    |                    |             |              |                                                                                                       |  ]                                                   |
    |                    |             |              |                                                                                                       | }                                                    |
    |                    |             |              |                                                                                                       | ]                                                    |
    +--------------------+-------------+--------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SecurityGroupToVirtualNetwork
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SecurityGroupToVirtualNetwork, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_security_groups_to_vn_to_vlan_by_id(self,
                                                id,
                                                headers=None,
                                                **query_parameters):
        """This API allows the client to get a security group to virtual
        network by ID.

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

        e_url = ('/ers/config/sgtvnvlan/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea0a65da3ae0346b912a9efac_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_security_groups_to_vn_to_vlan_by_id <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.get_security_groups_to_vn_to_vlan_by_id>`_
        """
        return self.get_security_groups_to_vn_to_vlan_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_security_groups_to_vn_to_vlan_by_id(self,
                                                   id,
                                                   description=None,
                                                   name=None,
                                                   sgt_id=None,
                                                   virtualnetworklist=None,
                                                   headers=None,
                                                   payload=None,
                                                   active_validation=True,
                                                   **query_parameters):
        """This API allows the client to update a security group to virtual
        network.

        Args:
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            name(string): name, property of the request body.
            sgt_id(string): sgtId, property of the request body.
            virtualnetworklist(list): virtualnetworklist, property
                of the request body (list of objects).
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
                'sgtId':
                    sgt_id,
                'virtualnetworklist':
                    virtualnetworklist,
            }
            _payload = {
                'SgtVNVlanContainer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eae98db0c24b5ecca77cce8279e20785_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgtvnvlan/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_eae98db0c24b5ecca77cce8279e20785_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     description=None,
                     name=None,
                     sgt_id=None,
                     virtualnetworklist=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_security_groups_to_vn_to_vlan_by_id <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.update_security_groups_to_vn_to_vlan_by_id>`_
        """
        return self.update_security_groups_to_vn_to_vlan_by_id(
            id=id,
            description=description,
            name=name,
            sgt_id=sgt_id,
            virtualnetworklist=virtualnetworklist,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_security_groups_to_vn_to_vlan_by_id(self,
                                                   id,
                                                   headers=None,
                                                   **query_parameters):
        """This API deletes a security group ACL to virtual network.

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

        e_url = ('/ers/config/sgtvnvlan/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_97c852dbb953860bef3326e0_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_security_groups_to_vn_to_vlan_by_id <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.delete_security_groups_to_vn_to_vlan_by_id>`_
        """
        return self.delete_security_groups_to_vn_to_vlan_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_security_groups_to_vn_to_vlan(self,
                                          filter=None,
                                          filter_type=None,
                                          page=None,
                                          size=None,
                                          headers=None,
                                          **query_parameters):
        """This API allows the client to get all the security group ACL to
        virtual networks.   Filter:   [sgtId]   To search guest
        users by using  toDate  column,follow the format:   DD-
        MON-YY (Example:13-SEP-18)     Day or Year:GET
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

        e_url = ('/ers/config/sgtvnvlan')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e51b6e745cdb5bdda4de26a27b8d92bb_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_security_groups_to_vn_to_vlan <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.get_security_groups_to_vn_to_vlan>`_
        """
        return self.get_security_groups_to_vn_to_vlan(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_security_groups_to_vn_to_vlan_generator(self,
                                                    filter=None,
                                                    filter_type=None,
                                                    page=None,
                                                    size=None,
                                                    headers=None,
                                                    **query_parameters):
        """This API allows the client to get all the security group ACL to
        virtual networks.   Filter:   [sgtId]   To search guest
        users by using  toDate  column,follow the format:   DD-
        MON-YY (Example:13-SEP-18)     Day or Year:GET
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
            self.get_security_groups_to_vn_to_vlan, dict(
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
        """Alias for `get_security_groups_to_vn_to_vlan_generator <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.get_security_groups_to_vn_to_vlan_generator>`_
        """
        yield from get_next_page(
            self.get_security_groups_to_vn_to_vlan, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_security_groups_to_vn_to_vlan(self,
                                             description=None,
                                             id=None,
                                             name=None,
                                             sgt_id=None,
                                             virtualnetworklist=None,
                                             headers=None,
                                             payload=None,
                                             active_validation=True,
                                             **query_parameters):
        """This API creates a security group to virtual network.

        Args:
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            name(string): name, property of the request body.
            sgt_id(string): sgtId, property of the request body.
            virtualnetworklist(list): virtualnetworklist, property
                of the request body (list of objects).
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
                'sgtId':
                    sgt_id,
                'virtualnetworklist':
                    virtualnetworklist,
            }
            _payload = {
                'SgtVNVlanContainer': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a0710ba581da4d3fd00e84d59e3_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgtvnvlan')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a0710ba581da4d3fd00e84d59e3_v3_1_1', _api_response)

    def create(self,
               description=None,
               id=None,
               name=None,
               sgt_id=None,
               virtualnetworklist=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_security_groups_to_vn_to_vlan <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.create_security_groups_to_vn_to_vlan>`_
        """
        return self.create_security_groups_to_vn_to_vlan(
            description=description,
            id=id,
            name=name,
            sgt_id=sgt_id,
            virtualnetworklist=virtualnetworklist,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the security group to virtual network.

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

        e_url = ('/ers/config/sgtvnvlan/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b2811387f4e55c8839c94ea241a3236_v3_1_1', _api_response)

    def bulk_request_for_security_groups_to_vn_to_vlan(self,
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
                'SgtVNVlanContainerBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_bd1af169fa52c59cbc87b010c36f9e_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgtvnvlan/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_bd1af169fa52c59cbc87b010c36f9e_v3_1_1', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_security_groups_to_vn_to_vlan <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.bulk_request_for_security_groups_to_vn_to_vlan>`_
        """
        return self.bulk_request_for_security_groups_to_vn_to_vlan(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_security_groups_to_vn_to_vlan(self,
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

        e_url = ('/ers/config/sgtvnvlan/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea793a0b1b5ac498f7bc74a0aba257_v3_1_1', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_security_groups_to_vn_to_vlan <#ciscoisesdk.
        api.v3_1_1.security_group_to_virtual_network.
        SecurityGroupToVirtualNetwork.monitor_bulk_status_security_groups_to_vn_to_vlan>`_
        """
        return self.monitor_bulk_status_security_groups_to_vn_to_vlan(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )
