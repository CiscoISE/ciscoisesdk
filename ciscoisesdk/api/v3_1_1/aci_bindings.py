# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine ACIBindings API wrapper.

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


class AciBindings(object):
    """Identity Services Engine ACIBindings API (version: 3.1.1).

    Wraps the Identity Services Engine ACIBindings
    API and exposes the API as native Python
    methods that return native Python objects.

    | The ACI Bindings API allows clients to retrieve bindings that were sent to Cisco ISE by ACI or received on ACI from Cisco ISE. The binding information will be identical to the information on the ACI bindings page in the Cisco ISE UI. Filtering will be based on one attribute only, such as ip, sgt, vn, psn, learnedFrom, or learnedBy with CONTAINS mode of search.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 3.0                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | **Attribute** | **Type**    | **Required** | **Description**                                                                                         | **Example Values**                   |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | name          | String      | Yes          | Resource Name                                                                                           |                                      |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | id            | String      | No           | Resource UUID value                                                                                     | f9269682-dcaf-11e3-ad0a-5bdcd2d9fd69 |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | description   | String      | No           |                                                                                                         |                                      |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | ip            | String      | Yes          | Binding IPv4 address. Each binding will be exclusively identified by its IP address and virtual network | 10.0.0.1                             |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | sgt           | String      | No           | Security Group Tag (SGT) value. The valid range for SGT values is 0-65534                               | 1234                                 |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | vn            | String      | Yes          | Virtual network. Each binding will be exclusively identified by its IP address and virtual network      | vn1234                               |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | psn           | String      | No           | Cisco ISE Policy Service node (PSN) IP address                                                          | 10.86.189.216                        |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | learnedFrom   | String      | Yes          | Binding Source                                                                                          | ISE by ACI                           |
    |               |             |              |                                                                                                         | ACI by ISE                           |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+
    | learnedBy     | String      | Yes          | Binding Type                                                                                            | SXP(SXP, 0)                          |
    |               |             |              |                                                                                                         | STATIC(Static, 1)                    |
    |               |             |              |                                                                                                         | RADIUS(RADIUS, 2)                    |
    |               |             |              |                                                                                                         | ACI(ACI, 3)                          |
    +---------------+-------------+--------------+---------------------------------------------------------------------------------------------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AciBindings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AciBindings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_aci_bindings(self,
                         filter_by=None,
                         filter_value=None,
                         page=None,
                         size=None,
                         sort=None,
                         sort_by=None,
                         headers=None,
                         **query_parameters):
        """This API allows clients to retrieve all the bindings that were
        sent to Cisco ISE by ACI or received on ACI from Cisco
        ISE.The binding information will be identical to the
        information on ACI bindings page in the Cisco ISE UI.
        Filtering will be based on one attribute only, such as
        ip/sgt/vn/psn/learnedFrom/learnedBy with CONTAINS mode
        of search.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter_by(basestring, list, set, tuple): filterBy query
                parameter.
            filter_value(basestring, list, set, tuple): filterValue
                query parameter.
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
        check_type(sort, basestring)
        check_type(sort_by, basestring)
        check_type(filter_by, (basestring, list, set, tuple))
        check_type(filter_value, (basestring, list, set, tuple))

        _params = {
            'page':
                page,
            'size':
                size,
            'sort':
                sort,
            'sortBy':
                sort_by,
            'filterBy':
                filter_by,
            'filterValue':
                filter_value,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/acibindings/getall')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d1448851f0154d0b6e9c856ec6cc6f0_v3_1_1', _api_response)

    def get_all(self,
                filter_by=None,
                filter_value=None,
                page=None,
                size=None,
                sort=None,
                sort_by=None,
                headers=None,
                **query_parameters):
        """Alias for `get_aci_bindings <#ciscoisesdk.
        api.v3_1_1.aci_bindings.
        AciBindings.get_aci_bindings>`_
        """
        return self.get_aci_bindings(
            filter_by=filter_by,
            filter_value=filter_value,
            page=page,
            size=size,
            sort=sort,
            sort_by=sort_by,
            headers=headers,
            **query_parameters
        )

    def get_aci_bindings_generator(self,
                                   filter_by=None,
                                   filter_value=None,
                                   page=None,
                                   size=None,
                                   sort=None,
                                   sort_by=None,
                                   headers=None,
                                   **query_parameters):
        """This API allows clients to retrieve all the bindings that were
        sent to Cisco ISE by ACI or received on ACI from Cisco
        ISE.The binding information will be identical to the
        information on ACI bindings page in the Cisco ISE UI.
        Filtering will be based on one attribute only, such as
        ip/sgt/vn/psn/learnedFrom/learnedBy with CONTAINS mode
        of search.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter_by(basestring, list, set, tuple): filterBy query
                parameter.
            filter_value(basestring, list, set, tuple): filterValue
                query parameter.
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
            self.get_aci_bindings, dict(
                filter_by=filter_by,
                filter_value=filter_value,
                page=page,
                size=size,
                sort=sort,
                sort_by=sort_by,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def get_all_generator(self,
                          filter_by=None,
                          filter_value=None,
                          page=None,
                          size=None,
                          sort=None,
                          sort_by=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_aci_bindings_generator <#ciscoisesdk.
        api.v3_1_1.aci_bindings.
        AciBindings.get_aci_bindings_generator>`_
        """
        yield from get_next_page(
            self.get_aci_bindings, dict(
                filter_by=filter_by,
                filter_value=filter_value,
                page=page,
                size=size,
                sort=sort,
                sort_by=sort_by,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the Cisco ACI bindings.

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

        e_url = ('/ers/config/acibindings/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d74b5214bad656c98f21e4968661c3c0_v3_1_1', _api_response)
