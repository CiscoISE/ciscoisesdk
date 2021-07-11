# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Device Administration - Network Conditions API wrapper.

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


class DeviceAdministrationNetworkConditions(object):
    """Identity Services Engine Device Administration - Network Conditions API (version: 3.0.0).

    Wraps the Identity Services Engine Device Administration - Network Conditions
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceAdministrationNetworkConditions
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceAdministrationNetworkConditions, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_device_admin_network_conditions(self,
                                            headers=None,
                                            **query_parameters):
        """Device Admin Returns a list of network conditions.

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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
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

        e_url = ('/v1/policy/device-admin/network-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bda58fc63575503b80c024dbe02cf547_v3_0_0', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_device_admin_network_conditions <#ciscoisesdk.
        api.v3_0_0.device_administration_network_conditions.
        DeviceAdministrationNetworkConditions.get_device_admin_network_conditions>`_
        """
        return self.get_device_admin_network_conditions(
            headers=headers,
            **query_parameters
        )

    def post_device_admin_network_condition(self,
                                            cli_dnis_list=None,
                                            condition_type=None,
                                            description=None,
                                            device_group_list=None,
                                            device_list=None,
                                            id=None,
                                            ip_addr_list=None,
                                            link=None,
                                            mac_addr_list=None,
                                            name=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """Device AdminCreates network condition.

        Args:
            cliDnisList(list): This field should contain a Caller ID
                (CLI), comma, and Called ID (DNIS).
                Line format  Caller ID (CLI), Called ID
                (DNIS), property of the request body
                (list of strings).
            condition_type(string): This field determines the
                content of the conditions field,
                property of the request body. Available
                values are 'EndstationCondition',
                'DeviceCondition' and
                'DevicePortCondition'.
            description(string): description, property of the
                request body.
            deviceGroupList(list): This field should contain a tuple
                with NDG Root, comma, and an NDG (that
                it under the root).  Line format NDG
                Root Name, NDG, Port, property of the
                request body (list of strings).
            deviceList(list): This field should contain Device-
                Name,port-number. The device name must
                be the same as the name field in a
                Network Device object.  Line format
                Device Name,Port, property of the
                request body (list of strings).
            id(string): id, property of the request body.
            ipAddrList(list): This field should contain IP-address-
                or-subnet,port number  IP address can be
                IPV4 format (n.n.n.n) or IPV6 format
                (n:n:n:n:n:n:n:n).  IP subnet can be
                IPV4 format (n.n.n.n/m) or IPV6 format
                (n:n:n:n:n:n:n:n/m).  Line format IP
                Address or subnet,Port, property of the
                request body (list of strings).
            link(object): link, property of the request body.
            macAddrList(list): This field should contain Endstation
                MAC address, comma, and Destination MAC
                addresses.  Each Max address must
                include twelve hexadecimal digits using
                formats nn:nn:nn:nn:nn:nn or nn-nn-nn-
                nn-nn-nn or nnnn.nnnn.nnnn or
                nnnnnnnnnnnn.  Line format Endstation
                MAC,Destination MAC , property of the
                request body (list of strings).
            name(string): Network Condition name, property of the
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
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
            _payload = {
                'conditionType':
                    condition_type,
                'description':
                    description,
                'id':
                    id,
                'link':
                    link,
                'name':
                    name,
                'cliDnisList':
                    cli_dnis_list,
                'ipAddrList':
                    ip_addr_list,
                'macAddrList':
                    mac_addr_list,
                'deviceGroupList':
                    device_group_list,
                'deviceList':
                    device_list,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ea4e38c44e5b1c90b19af25b88546e_v3_0_0')\
                .validate(_payload)

        e_url = ('/v1/policy/device-admin/network-condition')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ea4e38c44e5b1c90b19af25b88546e_v3_0_0', _api_response)

    def create(self,
               cli_dnis_list=None,
               condition_type=None,
               description=None,
               device_group_list=None,
               device_list=None,
               id=None,
               ip_addr_list=None,
               link=None,
               mac_addr_list=None,
               name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `post_device_admin_network_condition <#ciscoisesdk.
        api.v3_0_0.device_administration_network_conditions.
        DeviceAdministrationNetworkConditions.post_device_admin_network_condition>`_
        """
        return self.post_device_admin_network_condition(
            cli_dnis_list=cli_dnis_list,
            condition_type=condition_type,
            description=description,
            device_group_list=device_group_list,
            device_list=device_list,
            id=id,
            ip_addr_list=ip_addr_list,
            link=link,
            mac_addr_list=mac_addr_list,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_device_admin_network_condition_by_condition_id(self,
                                                           id,
                                                           headers=None,
                                                           **query_parameters):
        """Device Admin Returns a network condition.

        Args:
            id(basestring): id path parameter. Condition id.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
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

        e_url = ('/v1/policy/device-admin/network-condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e81a05d1f5cb5ba7bcc2351c0bfd6_v3_0_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_device_admin_network_condition_by_condition_id <#ciscoisesdk.
        api.v3_0_0.device_administration_network_conditions.
        DeviceAdministrationNetworkConditions.get_device_admin_network_condition_by_condition_id>`_
        """
        return self.get_device_admin_network_condition_by_condition_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def put_device_admin_network_condition_by_condition_id(self,
                                                           id,
                                                           cli_dnis_list=None,
                                                           condition_type=None,
                                                           description=None,
                                                           device_group_list=None,
                                                           device_list=None,
                                                           ip_addr_list=None,
                                                           link=None,
                                                           mac_addr_list=None,
                                                           name=None,
                                                           headers=None,
                                                           payload=None,
                                                           active_validation=True,
                                                           **query_parameters):
        """Device Admin Update network condition.

        Args:
            cliDnisList(list): This field should contain a Caller ID
                (CLI), comma, and Called ID (DNIS).
                Line format  Caller ID (CLI), Called ID
                (DNIS), property of the request body
                (list of strings).
            condition_type(string): This field determines the
                content of the conditions field,
                property of the request body. Available
                values are 'EndstationCondition',
                'DeviceCondition' and
                'DevicePortCondition'.
            description(string): description, property of the
                request body.
            deviceGroupList(list): This field should contain a tuple
                with NDG Root, comma, and an NDG (that
                it under the root).  Line format NDG
                Root Name, NDG, Port, property of the
                request body (list of strings).
            deviceList(list): This field should contain Device-
                Name,port-number. The device name must
                be the same as the name field in a
                Network Device object.  Line format
                Device Name,Port, property of the
                request body (list of strings).
            id(string): id, property of the request body.
            ipAddrList(list): This field should contain IP-address-
                or-subnet,port number  IP address can be
                IPV4 format (n.n.n.n) or IPV6 format
                (n:n:n:n:n:n:n:n).  IP subnet can be
                IPV4 format (n.n.n.n/m) or IPV6 format
                (n:n:n:n:n:n:n:n/m).  Line format IP
                Address or subnet,Port, property of the
                request body (list of strings).
            link(object): link, property of the request body.
            macAddrList(list): This field should contain Endstation
                MAC address, comma, and Destination MAC
                addresses.  Each Max address must
                include twelve hexadecimal digits using
                formats nn:nn:nn:nn:nn:nn or nn-nn-nn-
                nn-nn-nn or nnnn.nnnn.nnnn or
                nnnnnnnnnnnn.  Line format Endstation
                MAC,Destination MAC , property of the
                request body (list of strings).
            name(string): Network Condition name, property of the
                request body.
            id(basestring): id path parameter. Condition id.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
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
            _payload = {
                'conditionType':
                    condition_type,
                'description':
                    description,
                'id':
                    id,
                'link':
                    link,
                'name':
                    name,
                'cliDnisList':
                    cli_dnis_list,
                'ipAddrList':
                    ip_addr_list,
                'macAddrList':
                    mac_addr_list,
                'deviceGroupList':
                    device_group_list,
                'deviceList':
                    device_list,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cd32d094f1815c388d1392bb90f3744d_v3_0_0')\
                .validate(_payload)

        e_url = ('/v1/policy/device-admin/network-condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_cd32d094f1815c388d1392bb90f3744d_v3_0_0', _api_response)

    def update_by_id(self,
                     id,
                     cli_dnis_list=None,
                     condition_type=None,
                     description=None,
                     device_group_list=None,
                     device_list=None,
                     ip_addr_list=None,
                     link=None,
                     mac_addr_list=None,
                     name=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `put_device_admin_network_condition_by_condition_id <#ciscoisesdk.
        api.v3_0_0.device_administration_network_conditions.
        DeviceAdministrationNetworkConditions.put_device_admin_network_condition_by_condition_id>`_
        """
        return self.put_device_admin_network_condition_by_condition_id(
            id=id,
            cli_dnis_list=cli_dnis_list,
            condition_type=condition_type,
            description=description,
            device_group_list=device_group_list,
            device_list=device_list,
            ip_addr_list=ip_addr_list,
            link=link,
            mac_addr_list=mac_addr_list,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_device_admin_network_condition_by_condition_id(self,
                                                              id,
                                                              headers=None,
                                                              **query_parameters):
        """Device Admin Delete network condition.

        Args:
            id(basestring): id path parameter. Condition id.
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
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
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

        e_url = ('/v1/policy/device-admin/network-condition/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ac9ced821bc2503fa0d22badea9834ad_v3_0_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_device_admin_network_condition_by_condition_id <#ciscoisesdk.
        api.v3_0_0.device_administration_network_conditions.
        DeviceAdministrationNetworkConditions.delete_device_admin_network_condition_by_condition_id>`_
        """
        return self.delete_device_admin_network_condition_by_condition_id(
            id=id,
            headers=headers,
            **query_parameters
        )
