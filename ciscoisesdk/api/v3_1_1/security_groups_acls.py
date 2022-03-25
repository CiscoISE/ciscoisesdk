# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SecurityGroupsACLs API wrapper.

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


class SecurityGroupsAcls(object):
    """Identity Services Engine SecurityGroupsACLs API (version: 3.1.1).

    Wraps the Identity Services Engine SecurityGroupsACLs
    API and exposes the API as native Python
    methods that return native Python objects.

    | Security Groups ACLs API allows the client to search security groups access control lists.

    **Revision History**

    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+--------------------------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**             | **Revision Modification** | **Revision Modification**                  |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+--------------------------------------------+
    |                |                      |                       |                             | **Attribute**             | **Description**                            |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+--------------------------------------------+
    | 0              | 1.0                  | 2.0                   | Initial Cisco ISE Version   |                           |                                            |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+--------------------------------------------+
    | 1              | 1.1                  | 2.3                   | Introducing bulk operations |                           |                                            |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+--------------------------------------------+
    | 2              | 1.2                  | 3.1                   | Cisco ISE 3.1 model changes | modelledContent           | Adding modelled content from Cisco ISE 3.1 |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+--------------------------------------------+

    |

    **Resource Definition**

    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | **Attribute**   | **Type**  | **Required** | **Description**                                                            | **Default Values** | **Example Values**                   |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | name            | String    | Yes          | Resource Name                                                              |                    | Permit IP                            |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | id              | String    | No           | Resource UUID, mandatory for update                                        |                    | 92951ac0-8c01-11e6-996c-525400b48521 |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | description     | String    | No           |                                                                            |                    | Permit IP SGACL                      |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | ACLContent      | String    | No           |                                                                            |                    | permit ip                            |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | ipVersion       | Enum      | Yes          | Allowed values: IPV4, IPV6, IP_AGNOSTIC                                    | IPV4               |                                      |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | isReadOnly      | Boolean   | No           |                                                                            | false              |                                      |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | generationId    | String    | No           | GenerationId is a read only attribute and is being generated by the server |                    | 0                                    |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+
    | modelledContent | List      | No           | Modelled content of contract                                               |                    |                                      |
    +-----------------+-----------+--------------+----------------------------------------------------------------------------+--------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SecurityGroupsAcls
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SecurityGroupsAcls, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_security_groups_acl_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """This API allows the client to get a security group ACL by ID.

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

        e_url = ('/ers/config/sgacl/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a50d1bd34d5f593aadf8eb02083c67b0_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_security_groups_acl_by_id <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.get_security_groups_acl_by_id>`_
        """
        return self.get_security_groups_acl_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_security_groups_acl_by_id(self,
                                         id,
                                         aclcontent=None,
                                         description=None,
                                         generation_id=None,
                                         ip_version=None,
                                         is_read_only=None,
                                         modelled_content=None,
                                         name=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """This API allows the client to update a security group ACL.

        Args:
            aclcontent(string): aclcontent, property of the request
                body.
            description(string): description, property of the
                request body.
            generation_id(string): generationId, property of the
                request body.
            id(string): id, property of the request body.
            ip_version(string): Allowed values: IPV4, IPV6,
                IP_AGNOSTIC, property of the request
                body.
            is_read_only(boolean): isReadOnly, property of the
                request body.
            modelled_content(object): Modelled content of contract,
                property of the request body.
            name(string): name, property of the request body.
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
                'generationId':
                    generation_id,
                'aclcontent':
                    aclcontent,
                'isReadOnly':
                    is_read_only,
                'modelledContent':
                    modelled_content,
                'ipVersion':
                    ip_version,
            }
            _payload = {
                'Sgacl': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_afc81cd1e25c50319f75606b97c23b3d_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgacl/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_afc81cd1e25c50319f75606b97c23b3d_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     aclcontent=None,
                     description=None,
                     generation_id=None,
                     ip_version=None,
                     is_read_only=None,
                     modelled_content=None,
                     name=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_security_groups_acl_by_id <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.update_security_groups_acl_by_id>`_
        """
        return self.update_security_groups_acl_by_id(
            id=id,
            aclcontent=aclcontent,
            description=description,
            generation_id=generation_id,
            ip_version=ip_version,
            is_read_only=is_read_only,
            modelled_content=modelled_content,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_security_groups_acl_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """This API deletes a security group ACL.

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

        e_url = ('/ers/config/sgacl/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b0a2bea8bfec52b68663ef3f7ac6d7a7_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_security_groups_acl_by_id <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.delete_security_groups_acl_by_id>`_
        """
        return self.delete_security_groups_acl_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_security_groups_acl(self,
                                filter=None,
                                filter_type=None,
                                page=None,
                                size=None,
                                sortasc=None,
                                sortdsc=None,
                                headers=None,
                                **query_parameters):
        """This API allows the client to get all the security group ACLs.
        Filter:   [ipVersion, name, description]   To search
        guest users by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [ipVersion, name, description].

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

        e_url = ('/ers/config/sgacl')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b22d6ad9f595ab7e3eee5cf44de8a_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_security_groups_acl <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.get_security_groups_acl>`_
        """
        return self.get_security_groups_acl(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_security_groups_acl_generator(self,
                                          filter=None,
                                          filter_type=None,
                                          page=None,
                                          size=None,
                                          sortasc=None,
                                          sortdsc=None,
                                          headers=None,
                                          **query_parameters):
        """This API allows the client to get all the security group ACLs.
        Filter:   [ipVersion, name, description]   To search
        guest users by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [ipVersion, name, description].

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
            self.get_security_groups_acl, dict(
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
        """Alias for `get_security_groups_acl_generator <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.get_security_groups_acl_generator>`_
        """
        yield from get_next_page(
            self.get_security_groups_acl, dict(
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

    def create_security_groups_acl(self,
                                   aclcontent=None,
                                   description=None,
                                   generation_id=None,
                                   ip_version=None,
                                   is_read_only=None,
                                   modelled_content=None,
                                   name=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """This API creates a security group ACL.

        Args:
            aclcontent(string): aclcontent, property of the request
                body.
            description(string): description, property of the
                request body.
            generation_id(string): generationId, property of the
                request body.
            ip_version(string): Allowed values: IPV4, IPV6,
                IP_AGNOSTIC, property of the request
                body.
            is_read_only(boolean): isReadOnly, property of the
                request body.
            modelled_content(object): Modelled content of contract,
                property of the request body.
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
                'generationId':
                    generation_id,
                'aclcontent':
                    aclcontent,
                'isReadOnly':
                    is_read_only,
                'modelledContent':
                    modelled_content,
                'ipVersion':
                    ip_version,
            }
            _payload = {
                'Sgacl': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ab61f24bdaf508590f7686e1130913f_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgacl')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ab61f24bdaf508590f7686e1130913f_v3_1_1', _api_response)

    def create(self,
               aclcontent=None,
               description=None,
               generation_id=None,
               ip_version=None,
               is_read_only=None,
               modelled_content=None,
               name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_security_groups_acl <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.create_security_groups_acl>`_
        """
        return self.create_security_groups_acl(
            aclcontent=aclcontent,
            description=description,
            generation_id=generation_id,
            ip_version=ip_version,
            is_read_only=is_read_only,
            modelled_content=modelled_content,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the security group ACLs.

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

        e_url = ('/ers/config/sgacl/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e67a1131578aa794d8377da9a1de_v3_1_1', _api_response)

    def bulk_request_for_security_groups_acl(self,
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
                'SgaclBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_da250e23ac05e6a8dcf32a81effcee9_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgacl/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_da250e23ac05e6a8dcf32a81effcee9_v3_1_1', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_security_groups_acl <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.bulk_request_for_security_groups_acl>`_
        """
        return self.bulk_request_for_security_groups_acl(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_security_groups_acl(self,
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

        e_url = ('/ers/config/sgacl/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af5ee576605a5a915d888924c1e804_v3_1_1', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_security_groups_acl <#ciscoisesdk.
        api.v3_1_1.security_groups_acls.
        SecurityGroupsAcls.monitor_bulk_status_security_groups_acl>`_
        """
        return self.monitor_bulk_status_security_groups_acl(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )
