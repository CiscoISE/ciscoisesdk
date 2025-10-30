# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine sxplocalbindings API wrapper.

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



from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class Sxplocalbindings(object):
    """Identity Services Engine sxplocalbindings API (version: 3.5.0).

    Wraps the Identity Services Engine sxplocalbindings
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sxplocalbindings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sxplocalbindings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_sxplocalbindings(self,
                             filter=None,
                             page=None,
                             size=None,
                             sortasc=None,
                             sortdsc=None,
                             headers=None,
                             **query_parameters):
        """Get-All.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[sgt, vpn, vns, ipOrHost].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[sgt, vpn, ip, vns, ipOrHost].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[sgt, vpn, ip, vns, ipOrHost].
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
        check_type(filter, str)
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))
        check_type(sortdsc, str)
        check_type(sortasc, str)

        _params = {
            'filter':
                filter,
            'page':
                page,
            'size':
                size,
            'sortdsc':
                sortdsc,
            'sortasc':
                sortasc,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/sxplocalbindings/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ce403a1cd2f75dd8afe3370c7c18044c_v3_5_0', _api_response)

    def get_sxplocalbindings_generator(self,
                                       filter=None,
                                       page=None,
                                       size=None,
                                       sortasc=None,
                                       sortdsc=None,
                                       headers=None,
                                       **query_parameters):
        """Get-All.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[sgt, vpn, vns, ipOrHost].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[sgt, vpn, ip, vns, ipOrHost].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[sgt, vpn, ip, vns, ipOrHost].
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.

              + RestResponse: REST response with following properties:

                  - headers(MyDict): response headers.
                  - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
                    or the bracket notation.
                  - content(bytes): representation of the request's response
                  - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """

        yield from get_next_page(
            self.get_sxplocalbindings, dict(
                filter=filter,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_sxplocalbindings(self,
                                binding_name=None,
                                description=None,
                                id=None,
                                ip_address_or_host=None,
                                name=None,
                                sgt=None,
                                sxp_vpn=None,
                                vns=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Create.

        Args:
            binding_name(string): This field is depricated from ISE
                3.0, property of the request body.
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            ip_address_or_host(string): IP address for static
                mapping (hostname is not supported),
                property of the request body.
            name(string): name, property of the request body.
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
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
            check_type(payload, str)
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
                'bindingName':
                    binding_name,
                'ipAddressOrHost':
                    ip_address_or_host,
                'sgt':
                    sgt,
                'sxpVpn':
                    sxp_vpn,
                'vns':
                    vns,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSSxpLocalBindings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b8ba9774e5b6baef02818fe49ced6_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/sxplocalbindings/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b8ba9774e5b6baef02818fe49ced6_v3_5_0', _api_response)

    def get_sxplocalbindings_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """Get-By-Id.

        Args:
            id(str): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
        check_type(id, str,
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

        return self._object_factory('bpm_e56bea5248a25f799b02fcb6098a7b10_v3_5_0', _api_response)

    def update_sxplocalbindings_by_id(self,
                                      id,
                                      binding_name=None,
                                      description=None,
                                      ip_address_or_host=None,
                                      name=None,
                                      sgt=None,
                                      sxp_vpn=None,
                                      vns=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Update.

        Args:
            binding_name(string): This field is depricated from ISE
                3.0, property of the request body.
            description(string): Description, property of the
                request body.
            id(string): Id, property of the request body.
            ip_address_or_host(string): IP address for static
                mapping (hostname is not supported),
                property of the request body.
            name(string): name, property of the request body.
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
            id(str): id path parameter.
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
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
            check_type(payload, str)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, str,
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
                'bindingName':
                    binding_name,
                'ipAddressOrHost':
                    ip_address_or_host,
                'sgt':
                    sgt,
                'sxpVpn':
                    sxp_vpn,
                'vns':
                    vns,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSSxpLocalBindings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e07cb8ea65820863cce345c67926b_v3_5_0')\
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

        return self._object_factory('bpm_e07cb8ea65820863cce345c67926b_v3_5_0', _api_response)

    def delete_sxplocalbindings_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """Delete.

        Args:
            id(str): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(list): A list of MyDict objects. Access the object's properties by using the dot notation
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
        check_type(id, str,
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

        return self._object_factory('bpm_db04edfe595fbba5b49eb71dcb65bd_v3_5_0', _api_response)
