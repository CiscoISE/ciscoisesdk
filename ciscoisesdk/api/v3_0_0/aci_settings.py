# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine ACISettings API wrapper.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
    get_next_page,
)
import urllib.parse


class AciSettings(object):
    """Identity Services Engine ACISettings API (version: 3.0.0).

    Wraps the Identity Services Engine ACISettings
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AciSettings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AciSettings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_aci_settings(self,
                             headers=None,
                             **query_parameters):
        """Get all ACISettings.

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

        e_url = ('/ers/config/acisettings')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea5c865993b56f48f7f43475294a20c_v3_0_0', _api_response)

    def update_aci_settings_by_id(self,
                                  id,
                                  aci50=None,
                                  aci51=None,
                                  aciipaddress=None,
                                  acipassword=None,
                                  aciuser_name=None,
                                  admin_name=None,
                                  admin_password=None,
                                  all_sxp_domain=None,
                                  default_sgt_name=None,
                                  enable_aci=None,
                                  enable_data_plane=None,
                                  enable_elements_limit=None,
                                  ip_address_host_name=None,
                                  l3_route_network=None,
                                  max_num_iepg_from_aci=None,
                                  max_num_sgt_to_aci=None,
                                  specific_sxp_domain=None,
                                  specifix_sxp_domain_list=None,
                                  suffix_to_epg=None,
                                  suffix_to_sgt=None,
                                  tenant_name=None,
                                  untagged_packet_iepg_name=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Update ACISettings by Id.

        Args:
            aci50(boolean): aci50, property of the request body.
            aci51(boolean): aci51, property of the request body.
            aciipaddress(string): aciipaddress, property of the
                request body.
            acipassword(string): acipassword, property of the
                request body.
            aciuser_name(string): aciuserName, property of the
                request body.
            admin_name(string): adminName, property of the request
                body.
            admin_password(string): adminPassword, property of the
                request body.
            all_sxp_domain(boolean): allSxpDomain, property of the
                request body.
            default_sgt_name(string): defaultSgtName, property of
                the request body.
            enable_aci(boolean): enableAci, property of the request
                body.
            enable_data_plane(boolean): enableDataPlane, property of
                the request body.
            enable_elements_limit(boolean): enableElementsLimit,
                property of the request body.
            id(string): id, property of the request body.
            ip_address_host_name(string): ipAddressHostName,
                property of the request body.
            l3_route_network(string): l3RouteNetwork, property of
                the request body.
            max_num_iepg_from_aci(integer): maxNumIepgFromAci,
                property of the request body.
            max_num_sgt_to_aci(integer): maxNumSgtToAci, property of
                the request body.
            specific_sxp_domain(boolean): specificSxpDomain,
                property of the request body.
            specifixSxpDomainList(list): specifixSxpDomainList,
                property of the request body (list of
                strings).
            suffix_to_epg(string): suffixToEpg, property of the
                request body.
            suffix_to_sgt(string): suffixToSgt, property of the
                request body.
            tenant_name(string): tenantName, property of the request
                body.
            untagged_packet_iepg_name(string):
                untaggedPacketIepgName, property of the
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
                'enableAci':
                    enable_aci,
                'ipAddressHostName':
                    ip_address_host_name,
                'adminName':
                    admin_name,
                'tenantName':
                    tenant_name,
                'adminPassword':
                    admin_password,
                'l3RouteNetwork':
                    l3_route_network,
                'suffixToEpg':
                    suffix_to_epg,
                'suffixToSgt':
                    suffix_to_sgt,
                'allSxpDomain':
                    all_sxp_domain,
                'specificSxpDomain':
                    specific_sxp_domain,
                'specifixSxpDomainList':
                    specifix_sxp_domain_list,
                'enableDataPlane':
                    enable_data_plane,
                'untaggedPacketIepgName':
                    untagged_packet_iepg_name,
                'defaultSgtName':
                    default_sgt_name,
                'enableElementsLimit':
                    enable_elements_limit,
                'maxNumIepgFromAci':
                    max_num_iepg_from_aci,
                'maxNumSgtToAci':
                    max_num_sgt_to_aci,
                'aciipaddress':
                    aciipaddress,
                'aciuserName':
                    aciuser_name,
                'acipassword':
                    acipassword,
                'aci50':
                    aci50,
                'aci51':
                    aci51,
            }
            _payload = {
                'AciSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cea2e785ee57908a9ee3b118e49cfa_v3_0_0')\
                .validate(_payload)

        e_url = ('/ers/config/acisettings/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_cea2e785ee57908a9ee3b118e49cfa_v3_0_0', _api_response)

    def test_aci_connectivity(self,
                              headers=None,
                              **query_parameters):
        """Test ACI Connectivity.

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

        e_url = ('/ers/config/acisettings/testACIConnectivity')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b155c91eec153338302d492db1afb80_v3_0_0', _api_response)
