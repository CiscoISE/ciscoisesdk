# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SXPLocalBindings API wrapper.

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


class SxpLocalBindings(object):
    """Identity Services Engine SXPLocalBindings API (version: 3.1.0).

    Wraps the Identity Services Engine SXPLocalBindings
    API and exposes the API as native Python
    methods that return native Python objects.

    | SXP Local Bindings API allows clients to add, get, update and delete SGT static mappings.

    **Revision History**

    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+---------------------------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**             | **Revision Modification** | **Revision Modification**                   |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+---------------------------------------------+
    |                |                      |                       |                             | **Attribute**             | **Description**                             |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+---------------------------------------------+
    | 0              | 1.0                  | 2.0                   | Initial Cisco ISE Version   |                           |                                             |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+---------------------------------------------+
    | 1              | 1.1                  | 3.0                   | Cisco ISE 3.0 model changes | vns                       | Added new property for the Virtual Networks |
    +----------------+----------------------+-----------------------+-----------------------------+---------------------------+---------------------------------------------+

    |

    **Resource Definition**

    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | **Attribute**   | **Type** | **Required** | **Description**                                                                                  | **Example Values**                   |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | name            | String   | Yes          | Resource Name                                                                                    |                                      |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | id              | String   | No           | Resource UUID value                                                                              | f9269682-dcaf-11e3-ad0a-5bdcd2d9fd69 |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | description     | String   | No           |                                                                                                  |                                      |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | bindingName     | String   | No           | This field is depricated from Cisco ISE 3.0                                                      |                                      |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | ipAddressOrHost | String   | Yes          | IP address for static mapping (hostname is not supported)                                        | ipAddressOrHost                      |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | sgt             | String   | Yes          | SGT name or ID                                                                                   | sgt_id                               |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | sxpVpn          | String   | Yes          | List of SXP Domains, separated with comma. At least one of: sxpVpn or vns should be defined      | Sxp Vpn Name                         |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+
    | vns             | String   | Yes          | List of Virtual Networks, separated with comma. At least one of: sxpVpn or vns should be defined | virtualNetwork                       |
    +-----------------+----------+--------------+--------------------------------------------------------------------------------------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SxpLocalBindings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SxpLocalBindings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_sxp_local_bindings_by_id(self,
                                     id,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to get a SXP local binding by ID.

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

        e_url = ('/ers/config/sxplocalbindings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e56bea5248a25f799b02fcb6098a7b10_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_sxp_local_bindings_by_id <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.get_sxp_local_bindings_by_id>`_
        """
        return self.get_sxp_local_bindings_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_sxp_local_bindings_by_id(self,
                                        id,
                                        binding_name=None,
                                        description=None,
                                        ip_address_or_host=None,
                                        sgt=None,
                                        sxp_vpn=None,
                                        vns=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **query_parameters):
        """This API allows the client to update a SXP local binding.

        Args:
            binding_name(string): This field is depricated from
                Cisco ISE 3.0, property of the request
                body.
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            ip_address_or_host(string): IP address for static
                mapping (hostname is not supported),
                property of the request body.
            sgt(string): SGT name or ID, property of the request
                body.
            sxp_vpn(string): List of SXP Domains, separated with
                comma. At least one of: sxpVpn or vns
                should be defined, property of the
                request body.
            vns(string): List of Virtual Networks, separated with
                comma. At least one of: sxpVpn or vns
                should be defined, property of the
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
                'description':
                    description,
                'bindingName':
                    binding_name,
                'ipAddressOrHost':
                    ip_address_or_host,
                'sxpVpn':
                    sxp_vpn,
                'sgt':
                    sgt,
                'vns':
                    vns,
            }
            _payload = {
                'ERSSxpLocalBindings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e07cb8ea65820863cce345c67926b_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/sxplocalbindings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e07cb8ea65820863cce345c67926b_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     binding_name=None,
                     description=None,
                     ip_address_or_host=None,
                     sgt=None,
                     sxp_vpn=None,
                     vns=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_sxp_local_bindings_by_id <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.update_sxp_local_bindings_by_id>`_
        """
        return self.update_sxp_local_bindings_by_id(
            id=id,
            binding_name=binding_name,
            description=description,
            ip_address_or_host=ip_address_or_host,
            sgt=sgt,
            sxp_vpn=sxp_vpn,
            vns=vns,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_sxp_local_bindings_by_id(self,
                                        id,
                                        headers=None,
                                        **query_parameters):
        """This API deletes a SXP local binding.

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

        e_url = ('/ers/config/sxplocalbindings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_db04edfe595fbba5b49eb71dcb65bd_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_sxp_local_bindings_by_id <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.delete_sxp_local_bindings_by_id>`_
        """
        return self.delete_sxp_local_bindings_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_sxp_local_bindings(self,
                               filter=None,
                               filter_type=None,
                               page=None,
                               size=None,
                               sortasc=None,
                               sortdsc=None,
                               headers=None,
                               **query_parameters):
        """This API allows the client to get all the SXP local bindings.
        Filter:   [name, description]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [name, description].

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

        e_url = ('/ers/config/sxplocalbindings')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f845bd746a5c00967fe66178c5edbf_v3_1_0', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_sxp_local_bindings <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.get_sxp_local_bindings>`_
        """
        return self.get_sxp_local_bindings(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_sxp_local_bindings_generator(self,
                                         filter=None,
                                         filter_type=None,
                                         page=None,
                                         size=None,
                                         sortasc=None,
                                         sortdsc=None,
                                         headers=None,
                                         **query_parameters):
        """This API allows the client to get all the SXP local bindings.
        Filter:   [name, description]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [name, description].

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
            self.get_sxp_local_bindings, dict(
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
        """Alias for `get_sxp_local_bindings_generator <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.get_sxp_local_bindings_generator>`_
        """
        yield from get_next_page(
            self.get_sxp_local_bindings, dict(
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

    def create_sxp_local_bindings(self,
                                  binding_name=None,
                                  description=None,
                                  id=None,
                                  ip_address_or_host=None,
                                  sgt=None,
                                  sxp_vpn=None,
                                  vns=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """This API creates a SXP local binding.

        Args:
            binding_name(string): This field is depricated from
                Cisco ISE 3.0, property of the request
                body.
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            ip_address_or_host(string): IP address for static
                mapping (hostname is not supported),
                property of the request body.
            sgt(string): SGT name or ID, property of the request
                body.
            sxp_vpn(string): List of SXP Domains, separated with
                comma. At least one of: sxpVpn or vns
                should be defined, property of the
                request body.
            vns(string): List of Virtual Networks, separated with
                comma. At least one of: sxpVpn or vns
                should be defined, property of the
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
                'description':
                    description,
                'bindingName':
                    binding_name,
                'ipAddressOrHost':
                    ip_address_or_host,
                'sxpVpn':
                    sxp_vpn,
                'sgt':
                    sgt,
                'vns':
                    vns,
            }
            _payload = {
                'ERSSxpLocalBindings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cf67e0155eab895b50d1a377f21_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/sxplocalbindings')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_cf67e0155eab895b50d1a377f21_v3_1_0', _api_response)

    def create(self,
               binding_name=None,
               description=None,
               id=None,
               ip_address_or_host=None,
               sgt=None,
               sxp_vpn=None,
               vns=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_sxp_local_bindings <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.create_sxp_local_bindings>`_
        """
        return self.create_sxp_local_bindings(
            binding_name=binding_name,
            description=description,
            id=id,
            ip_address_or_host=ip_address_or_host,
            sgt=sgt,
            sxp_vpn=sxp_vpn,
            vns=vns,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the SXP local bindings.

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

        e_url = ('/ers/config/sxplocalbindings/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ee22235f36835dec897ed6381e3e15fc_v3_1_0', _api_response)

    def bulk_request_for_sxp_local_bindings(self,
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
                'LocalBindingBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c21f51995bff8d6468a1e9c0b2e9_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/sxplocalbindings/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c21f51995bff8d6468a1e9c0b2e9_v3_1_0', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_sxp_local_bindings <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.bulk_request_for_sxp_local_bindings>`_
        """
        return self.bulk_request_for_sxp_local_bindings(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_sxp_local_bindings(self,
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

        e_url = ('/ers/config/sxplocalbindings/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_db866e1125ca0b7cd7cc13ac4bdd4_v3_1_0', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_sxp_local_bindings <#ciscoisesdk.
        api.v3_1_0.sxp_local_bindings.
        SxpLocalBindings.monitor_bulk_status_sxp_local_bindings>`_
        """
        return self.monitor_bulk_status_sxp_local_bindings(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )
