# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine acisettings API wrapper.

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


class Acisettings(object):
    """Identity Services Engine acisettings API (version: 3.5.0).

    Wraps the Identity Services Engine acisettings
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Acisettings
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Acisettings, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_acisettings(self,
                        headers=None,
                        **query_parameters):
        """GetAciSettings.

        Args:
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/acisettings/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d05636b97b452e59dfbdb4d6e7bb075_v3_5_0', _api_response)

    def update_acisettings_testaciconnectivity(self,
                                               headers=None,
                                               **query_parameters):
        """TestACIConnection.

        Args:
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

        return self._object_factory('bpm_b155c91eec153338302d492db1afb80_v3_5_0', _api_response)

    def update_acisettings_by_id(self,
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
                                 description=None,
                                 enable_aci=None,
                                 enable_data_plane=None,
                                 enable_elements_limit=None,
                                 ip_address_host_name=None,
                                 l3_route_network=None,
                                 max_num_iepg_from_aci=None,
                                 max_num_sgt_to_aci=None,
                                 name=None,
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
        """Update.

        Args:
            aci50(boolean): Enable Policy Plane/API integration.,
                property of the request body.
            aci51(boolean): Enable Data Plane/Hardware integration
                (ACI 5.1 onwards)., property of the
                request body.
            aciipaddress(string): ACI Domain manager Ip Address.,
                property of the request body.
            acipassword(string): ACI Domain manager Password.,
                property of the request body.
            aciuser_name(string): ACI Domain manager Username.,
                property of the request body.
            admin_name(string): ACI Cluster Admin name., property of
                the request body.
            admin_password(string): ACI Cluster Admin password.,
                property of the request body.
            all_sxp_domain(boolean): SXP Propagation to all the SXP
                domains., property of the request body.
            default_sgt_name(string): Default SGT name., property of
                the request body.
            description(string): Description, property of the
                request body.
            enable_aci(boolean): Enable ACI Integration., property
                of the request body.
            enable_data_plane(boolean): Enable data plane., property
                of the request body.
            enable_elements_limit(boolean): Enable Elements Limit.,
                property of the request body.
            id(string): Id, property of the request body.
            ip_address_host_name(string): ACI Cluster IP Address /
                Host name., property of the request
                body.
            l3_route_network(string): ACI Cluster L3 Route network
                name., property of the request body.
            max_num_iepg_from_aci(object): Max number of IEPGs.,
                property of the request body.
            max_num_sgt_to_aci(object): Max number of SGTs.,
                property of the request body.
            name(string): name, property of the request body.
            specific_sxp_domain(boolean): SXP Propagation to
                specific SXP domains., property of the
                request body.
            specifix_sxp_domain_list(list): Specific SXP domains
                list., property of the request body
                (list of strings).
            suffix_to_epg(string): Name Conversion EPG suffix.,
                property of the request body.
            suffix_to_sgt(string): Name Conversion SGT suffix.,
                property of the request body.
            tenant_name(string): ACI Cluster Tenant name., property
                of the request body.
            untagged_packet_iepg_name(string): Untagged IEPG packets
                name., property of the request body.
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
                'enableAci':
                    enable_aci,
                'aci50':
                    aci50,
                'ipAddressHostName':
                    ip_address_host_name,
                'adminName':
                    admin_name,
                'adminPassword':
                    admin_password,
                'tenantName':
                    tenant_name,
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
                'aci51':
                    aci51,
                'aciipaddress':
                    aciipaddress,
                'aciuserName':
                    aciuser_name,
                'acipassword':
                    acipassword,
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
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'AciSettings': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cea2e785ee57908a9ee3b118e49cfa_v3_5_0')\
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

        return self._object_factory('bpm_cea2e785ee57908a9ee3b118e49cfa_v3_5_0', _api_response)
