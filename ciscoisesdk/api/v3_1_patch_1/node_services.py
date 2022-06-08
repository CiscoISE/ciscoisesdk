# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Node Services API wrapper.

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


class NodeServices(object):
    """Identity Services Engine Node Services API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine Node Services
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NodeServices
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NodeServices, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_interfaces(self,
                       hostname,
                       headers=None,
                       **query_parameters):
        """This API retrieves the list of interfaces on a node in a
        cluster. .

        Args:
            hostname(basestring): hostname path parameter. Hostname
                of the node.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }

        e_url = ('/api/v1/node/{hostname}/interface')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f6f429e124ea58ba85f0b34296d61300_v3_1_patch_1', _api_response)

    def get_sxp_interface(self,
                          hostname,
                          headers=None,
                          **query_parameters):
        """This API retrieves the SXP interface. .

        Args:
            hostname(basestring): hostname path parameter. Hostname
                of the node.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }

        e_url = ('/api/v1/node/{hostname}/sxp-interface')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ba4b550caf3845b4cbe1074d_v3_1_patch_1', _api_response)

    def set_sxp_interface(self,
                          hostname,
                          interface=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """This API configures the SXP interface. .

        Args:
            interface(string): interface, property of the request
                body.
            hostname(basestring): hostname path parameter. Hostname
                of the node.
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
            pass

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
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'interface':
                    interface,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c6d188a13915253869849c4b0be7759_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/node/{hostname}/sxp-interface')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c6d188a13915253869849c4b0be7759_v3_1_patch_1', _api_response)

    def get_profiler_probe_config(self,
                                  hostname,
                                  headers=None,
                                  **query_parameters):
        """This API retrieves the profiler probe configuration of a PSN. .

        Args:
            hostname(basestring): hostname path parameter. Hostname
                of the node.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }

        e_url = ('/api/v1/profile/{hostname}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bfa308ed7b5fb6acde734f6267b4e3_v3_1_patch_1', _api_response)

    def set_profiler_probe_config(self,
                                  hostname,
                                  active_directory=None,
                                  dhcp=None,
                                  dhcp_span=None,
                                  dns=None,
                                  http=None,
                                  netflow=None,
                                  nmap=None,
                                  pxgrid=None,
                                  radius=None,
                                  snmp_query=None,
                                  snmp_trap=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """This API updates the profiler probe configuration of a PSN.  Set
        probe value as  null  to disable probe.  Ex: Below
        payload will disable NMAP, PxGrid and SNMPTRAP probes  {
        "activeDirectory": { "daysBeforeRescan": 1 },    "dhcp":
        { "interfaces": "[{"interface":"GigabitEthernet 0"}]",
        "port": 0 },    "dhcpSpan": { "interfaces":
        "[{"interface":"GigabitEthernet 0"}]" },    "dns": {
        "timeout": 2 },    "http": { "interfaces":
        "[{"interface":"GigabitEthernet 0"}]" },    "netflow": {
        "interfaces": "[{"interface":"GigabitEthernet 0"}]",
        "port": 0 },    "nmap":  null ,    "pxgrid":  null ,
        "radius": [],    "snmpQuery": { "eventTimeout": 30,
        "retries": 2, "timeout": 1000 },    "snmpTrap":  null
        }  .

        Args:
            active_directory(object): The Active Directory probe
                queries the Active Directory for Windows
                information., property of the request
                body.
            dhcp(object): The DHCP probe listens for DHCP packets
                from IP helpers., property of the
                request body.
            dhcp_span(object): The DHCP SPAN probe collects DHCP
                packets., property of the request body.
            dns(object): The DNS probe performs a DNS lookup for the
                FQDN., property of the request body.
            http(object): The HTTP probe receives and parses HTTP
                packets., property of the request body.
            netflow(object): The NetFlow probe collects the NetFlow
                packets that are sent to it from
                routers., property of the request body.
            nmap(list): The NMAP probe scans endpoints for open
                ports and OS., property of the request
                body (list of objects).
            pxgrid(list): The pxGrid probe fetches attributes of MAC
                address or IP address as a subscriber
                from the pxGrid queue., property of the
                request body (list of objects).
            radius(list): The RADIUS probe collects RADIUS session
                attributes as well as CDP, LLDP, DHCP,
                HTTP, and MDM attributes from IOS
                Sensors., property of the request body
                (list of objects).
            snmp_query(object): The SNMP query probe collects
                details from network devices such as
                interface, CDP, LLDP, and ARP., property
                of the request body.
            snmp_trap(object): The SNMP trap probe receives linkup,
                linkdown, and MAC notification traps
                from network devices., property of the
                request body.
            hostname(basestring): hostname path parameter. Hostname
                of the node.
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
            pass

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
        check_type(hostname, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'activeDirectory':
                    active_directory,
                'dhcp':
                    dhcp,
                'dhcpSpan':
                    dhcp_span,
                'dns':
                    dns,
                'http':
                    http,
                'netflow':
                    netflow,
                'nmap':
                    nmap,
                'pxgrid':
                    pxgrid,
                'radius':
                    radius,
                'snmpQuery':
                    snmp_query,
                'snmpTrap':
                    snmp_trap,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_bba25b96ab6c5a99a7e7933a1ef71977_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/api/v1/profile/{hostname}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_bba25b96ab6c5a99a7e7933a1ef71977_v3_1_patch_1', _api_response)
