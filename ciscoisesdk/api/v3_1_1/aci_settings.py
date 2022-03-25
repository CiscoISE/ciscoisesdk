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


class AciSettings(object):
    """Identity Services Engine ACISettings API (version: 3.1.1).

    Wraps the Identity Services Engine ACISettings
    API and exposes the API as native Python
    methods that return native Python objects.

    | ACI Settings API allows the client to get and update the ACI Settings. In addition, testing the ACI Domain Manager connection is also possible using the TestACIConnection.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 3.0                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | **Attribute**          | **Type** | **Required** | **Description**                         | **Default Values** | **Example Values**                   |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | name                   | String   | Yes          | Resource Name                           |                    | AciSettings                          |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | id                     | String   | No           | Resource UUID value                     |                    | 29fb45ab-6a8e-4658-8a28-02521c258178 |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | description            | String   | No           |                                         |                    | Aci Settings                         |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | enableAci              | Boolean  | Yes          | Enable ACI Integration                  | false              |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | isAci50                | Boolean  | Yes          | Enable 5.0 ACI Version                  | false              |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | ipAddressHostName      | String   | No           | ACI Cluster IP Address / Host name      |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | adminName              | String   | No           | ACI Cluster Admin name                  |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | adminPassword          | String   | No           | ACI Cluster Admin password              |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | tenantName             | String   | No           | ACI Cluster Tenant name                 | ISE                |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | l3RouteNetwork         | String   | No           | ACI Cluster L3 Route network name       | L3_ROUTE           |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | suffixToEpg            | String   | No           | Name Conversion - EPG suffix            | SGT                |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | suffixToSgt            | String   | No           | Name Conversion - SGT suffix            | EPG                |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | allSxpDomain           | Boolean  | No           | SXP Propagation to all the SXP domains  | false              |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | specificSxpDomain      | Boolean  | No           | SXP Propagation to specific SXP domains | true               |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | specifixSxpDomainList  | List     | No           | Specific SXP domains list               | [default]          |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | isAci51                | Boolean  | Yes          | Enable 5.1 ACI Version                  | false              |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | aciipaddress           | String   | No           | ACI Domain manager Ip Address           |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | aciuserName            | String   | No           | ACI Domain manager Username             |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | acipassword            | String   | No           | ACI Domain manager Password             |                    |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | enableDataPlane        | Boolean  | No           | Enable data plane                       | false              |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | untaggedPacketIepgName | String   | No           | Untagged IEPG packets name              | untagged           |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | defaultSgtName         | String   | No           | Default SGT name                        | Unknown            |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | enableElementsLimit    | Boolean  | No           | Enable Elements Limit                   | false              |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | maxNumIepgFromAci      | Integer  | No           | Max number of IEPGs                     | 1000               |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+
    | maxNumSgtToAci         | Integer  | No           | Max number of SGTs                      | 500                |                                      |
    +------------------------+----------+--------------+-----------------------------------------+--------------------+--------------------------------------+

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

    def get_aci_settings(self,
                         headers=None,
                         **query_parameters):
        """This API allows the client to get ACI Settings.

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

        return self._object_factory('bpm_ea5c865993b56f48f7f43475294a20c_v3_1_1', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_aci_settings <#ciscoisesdk.
        api.v3_1_1.aci_settings.
        AciSettings.get_aci_settings>`_
        """
        return self.get_aci_settings(
            headers=headers,
            **query_parameters
        )

    def test_aci_connectivity(self,
                              headers=None,
                              **query_parameters):
        """This API allows the client to test ACI Domain Manager
        connection.

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

        return self._object_factory('bpm_b155c91eec153338302d492db1afb80_v3_1_1', _api_response)

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
        """This API allows the client to update ACI settings.

        Args:
            aci50(boolean): Enable 5.0 ACI Version, property of the
                request body.
            aci51(boolean): Enable 5.1 ACI Version, property of the
                request body.
            aciipaddress(string): ACI Domain manager Ip Address.,
                property of the request body.
            acipassword(string): ACI Domain manager Password.,
                property of the request body.
            aciuser_name(string): ACI Domain manager Username.,
                property of the request body.
            admin_name(string): ACI Cluster Admin name, property of
                the request body.
            admin_password(string): ACI Cluster Admin password,
                property of the request body.
            all_sxp_domain(boolean): allSxpDomain, property of the
                request body.
            default_sgt_name(string): defaultSgtName, property of
                the request body.
            enable_aci(boolean): Enable ACI Integration, property of
                the request body.
            enable_data_plane(boolean): enableDataPlane, property of
                the request body.
            enable_elements_limit(boolean): enableElementsLimit,
                property of the request body.
            id(string): Resource UUID value, property of the request
                body.
            ip_address_host_name(string): ACI Cluster IP Address /
                Host name, property of the request body.
            l3_route_network(string): l3RouteNetwork, property of
                the request body.
            max_num_iepg_from_aci(integer): maxNumIepgFromAci,
                property of the request body.
            max_num_sgt_to_aci(integer): maxNumSgtToAci, property of
                the request body.
            specific_sxp_domain(boolean): specificSxpDomain,
                property of the request body.
            specifix_sxp_domain_list(list): specifixSxpDomainList,
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
                'enableAci':
                    enable_aci,
                'ipAddressHostName':
                    ip_address_host_name,
                'adminName':
                    admin_name,
                'adminPassword':
                    admin_password,
                'aciipaddress':
                    aciipaddress,
                'aciuserName':
                    aciuser_name,
                'acipassword':
                    acipassword,
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
            self._request_validator('jsd_cea2e785ee57908a9ee3b118e49cfa_v3_1_1')\
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

        return self._object_factory('bpm_cea2e785ee57908a9ee3b118e49cfa_v3_1_1', _api_response)

    def update_by_id(self,
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
        """Alias for `update_aci_settings_by_id <#ciscoisesdk.
        api.v3_1_1.aci_settings.
        AciSettings.update_aci_settings_by_id>`_
        """
        return self.update_aci_settings_by_id(
            id=id,
            aci50=aci50,
            aci51=aci51,
            aciipaddress=aciipaddress,
            acipassword=acipassword,
            aciuser_name=aciuser_name,
            admin_name=admin_name,
            admin_password=admin_password,
            all_sxp_domain=all_sxp_domain,
            default_sgt_name=default_sgt_name,
            enable_aci=enable_aci,
            enable_data_plane=enable_data_plane,
            enable_elements_limit=enable_elements_limit,
            ip_address_host_name=ip_address_host_name,
            l3_route_network=l3_route_network,
            max_num_iepg_from_aci=max_num_iepg_from_aci,
            max_num_sgt_to_aci=max_num_sgt_to_aci,
            specific_sxp_domain=specific_sxp_domain,
            specifix_sxp_domain_list=specifix_sxp_domain_list,
            suffix_to_epg=suffix_to_epg,
            suffix_to_sgt=suffix_to_sgt,
            tenant_name=tenant_name,
            untagged_packet_iepg_name=untagged_packet_iepg_name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the Cisco ACI settings.

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

        e_url = ('/ers/config/acisettings/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea47f65521bcf0ab949b5d72b5_v3_1_1', _api_response)
