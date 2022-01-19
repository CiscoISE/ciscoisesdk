# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine NetworkDevice API wrapper.

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
)
from ...pagination import get_next_page


class NetworkDevice(object):
    """Identity Services Engine NetworkDevice API (version: 3.1.1).

    Wraps the Identity Services Engine NetworkDevice
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkDevice
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkDevice, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_network_device_by_name(self,
                                   name,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to get a network device by name.

        Args:
            name(basestring): name path parameter.
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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/ers/config/networkdevice/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d8610d4a355b63aaaa364447d5fa00_v3_1_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_network_device_by_name <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.get_network_device_by_name>`_
        """
        return self.get_network_device_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def update_network_device_by_name(self,
                                      name,
                                      authentication_settings=None,
                                      coa_port=None,
                                      description=None,
                                      dtls_dns_name=None,
                                      id=None,
                                      model_name=None,
                                      network_device_group_list=None,
                                      network_device_iplist=None,
                                      profile_name=None,
                                      snmpsettings=None,
                                      software_version=None,
                                      tacacs_settings=None,
                                      trustsecsettings=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """This API allows the client to update a network device by name.

        Args:
            network_device_group_list(list): List of Network Device
                Group names for this node, property of
                the request body (list of strings).
            network_device_iplist(list): List of IP Subnets for this
                node, property of the request body (list
                of objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(integer): coaPort, property of the request
                body.
            description(string): description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            id(string): id, property of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): profileName, property of the
                request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            trustsecsettings(object): trustsecsettings, property of
                the request body.
            name(basestring): name path parameter.
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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
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
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
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
                'authenticationSettings':
                    authentication_settings,
                'snmpsettings':
                    snmpsettings,
                'trustsecsettings':
                    trustsecsettings,
                'tacacsSettings':
                    tacacs_settings,
                'profileName':
                    profile_name,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ea2c4586b845888b2a9375126f70de2_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/networkdevice/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_ea2c4586b845888b2a9375126f70de2_v3_1_1', _api_response)

    def update_by_name(self,
                       name,
                       authentication_settings=None,
                       coa_port=None,
                       description=None,
                       dtls_dns_name=None,
                       id=None,
                       model_name=None,
                       network_device_group_list=None,
                       network_device_iplist=None,
                       profile_name=None,
                       snmpsettings=None,
                       software_version=None,
                       tacacs_settings=None,
                       trustsecsettings=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **query_parameters):
        """Alias for `update_network_device_by_name <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.update_network_device_by_name>`_
        """
        return self.update_network_device_by_name(
            name=name,
            authentication_settings=authentication_settings,
            coa_port=coa_port,
            description=description,
            dtls_dns_name=dtls_dns_name,
            id=id,
            model_name=model_name,
            network_device_group_list=network_device_group_list,
            network_device_iplist=network_device_iplist,
            profile_name=profile_name,
            snmpsettings=snmpsettings,
            software_version=software_version,
            tacacs_settings=tacacs_settings,
            trustsecsettings=trustsecsettings,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_network_device_by_name(self,
                                      name,
                                      headers=None,
                                      **query_parameters):
        """This API deletes a network device by name.

        Args:
            name(basestring): name path parameter.
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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/ers/config/networkdevice/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eafaf2e785c6898fb982dbe4462e7_v3_1_1', _api_response)

    def delete_by_name(self,
                       name,
                       headers=None,
                       **query_parameters):
        """Alias for `delete_network_device_by_name <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.delete_network_device_by_name>`_
        """
        return self.delete_network_device_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_network_device_by_id(self,
                                 id,
                                 headers=None,
                                 **query_parameters):
        """This API allows the client to get a network device by ID.

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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
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

        e_url = ('/ers/config/networkdevice/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4ab683ce53052e089626a096abaf451_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_network_device_by_id <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.get_network_device_by_id>`_
        """
        return self.get_network_device_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_network_device_by_id(self,
                                    id,
                                    authentication_settings=None,
                                    coa_port=None,
                                    description=None,
                                    dtls_dns_name=None,
                                    model_name=None,
                                    name=None,
                                    network_device_group_list=None,
                                    network_device_iplist=None,
                                    profile_name=None,
                                    snmpsettings=None,
                                    software_version=None,
                                    tacacs_settings=None,
                                    trustsecsettings=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """This API allows the client to update a network device by ID.

        Args:
            network_device_group_list(list): List of Network Device
                Group names for this node, property of
                the request body (list of strings).
            network_device_iplist(list): List of IP Subnets for this
                node, property of the request body (list
                of objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(integer): coaPort, property of the request
                body.
            description(string): description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            id(string): id, property of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): profileName, property of the
                request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            trustsecsettings(object): trustsecsettings, property of
                the request body.
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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
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
                'authenticationSettings':
                    authentication_settings,
                'snmpsettings':
                    snmpsettings,
                'trustsecsettings':
                    trustsecsettings,
                'tacacsSettings':
                    tacacs_settings,
                'profileName':
                    profile_name,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b1edfeb182025176bb250633937177ae_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/networkdevice/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b1edfeb182025176bb250633937177ae_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     authentication_settings=None,
                     coa_port=None,
                     description=None,
                     dtls_dns_name=None,
                     model_name=None,
                     name=None,
                     network_device_group_list=None,
                     network_device_iplist=None,
                     profile_name=None,
                     snmpsettings=None,
                     software_version=None,
                     tacacs_settings=None,
                     trustsecsettings=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_network_device_by_id <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.update_network_device_by_id>`_
        """
        return self.update_network_device_by_id(
            id=id,
            authentication_settings=authentication_settings,
            coa_port=coa_port,
            description=description,
            dtls_dns_name=dtls_dns_name,
            model_name=model_name,
            name=name,
            network_device_group_list=network_device_group_list,
            network_device_iplist=network_device_iplist,
            profile_name=profile_name,
            snmpsettings=snmpsettings,
            software_version=software_version,
            tacacs_settings=tacacs_settings,
            trustsecsettings=trustsecsettings,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_network_device_by_id(self,
                                    id,
                                    headers=None,
                                    **query_parameters):
        """This API deletes a network device by ID.

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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
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

        e_url = ('/ers/config/networkdevice/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f2fd3c6324b581ca0f3f9eadede1cdc_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_network_device_by_id <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.delete_network_device_by_id>`_
        """
        return self.delete_network_device_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_network_device(self,
                           filter=None,
                           filter_type=None,
                           page=None,
                           size=None,
                           sortasc=None,
                           sortdsc=None,
                           headers=None,
                           **query_parameters):
        """This API allows the client to get all the network devices.
        Filter:   [ipaddress, name, description, location, type]
        To search resources by using  toDate  column,follow the
        format:   DD-MON-YY (Example:13-SEP-18)     Day or
        Year:GET
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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
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

        e_url = ('/ers/config/networkdevice')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b986fa0f0d54ef98eb135eeb88808a_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_network_device <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.get_network_device>`_
        """
        return self.get_network_device(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_network_device_generator(self,
                                     filter=None,
                                     filter_type=None,
                                     page=None,
                                     size=None,
                                     sortasc=None,
                                     sortdsc=None,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to get all the network devices.
        Filter:   [ipaddress, name, description, location, type]
        To search resources by using  toDate  column,follow the
        format:   DD-MON-YY (Example:13-SEP-18)     Day or
        Year:GET
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
            self.get_network_device, dict(
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
        """Alias for `get_network_device_generator <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.get_network_device_generator>`_
        """
        yield from get_next_page(
            self.get_network_device, dict(
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

    def create_network_device(self,
                              authentication_settings=None,
                              coa_port=None,
                              description=None,
                              dtls_dns_name=None,
                              model_name=None,
                              name=None,
                              network_device_group_list=None,
                              network_device_iplist=None,
                              profile_name=None,
                              snmpsettings=None,
                              software_version=None,
                              tacacs_settings=None,
                              trustsecsettings=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """This API creates a network device.

        Args:
            network_device_group_list(list): List of Network Device
                Group names for this node, property of
                the request body (list of strings).
            network_device_iplist(list): List of IP Subnets for this
                node, property of the request body (list
                of objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(integer): coaPort, property of the request
                body.
            description(string): description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): profileName, property of the
                request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            trustsecsettings(object): trustsecsettings, property of
                the request body.
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
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
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
                'authenticationSettings':
                    authentication_settings,
                'snmpsettings':
                    snmpsettings,
                'trustsecsettings':
                    trustsecsettings,
                'tacacsSettings':
                    tacacs_settings,
                'profileName':
                    profile_name,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ca6ab8ec556c3bc9531dc380b230a_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/networkdevice')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ca6ab8ec556c3bc9531dc380b230a_v3_1_1', _api_response)

    def create(self,
               authentication_settings=None,
               coa_port=None,
               description=None,
               dtls_dns_name=None,
               model_name=None,
               name=None,
               network_device_group_list=None,
               network_device_iplist=None,
               profile_name=None,
               snmpsettings=None,
               software_version=None,
               tacacs_settings=None,
               trustsecsettings=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_network_device <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.create_network_device>`_
        """
        return self.create_network_device(
            authentication_settings=authentication_settings,
            coa_port=coa_port,
            description=description,
            dtls_dns_name=dtls_dns_name,
            model_name=model_name,
            name=name,
            network_device_group_list=network_device_group_list,
            network_device_iplist=network_device_iplist,
            profile_name=profile_name,
            snmpsettings=snmpsettings,
            software_version=software_version,
            tacacs_settings=tacacs_settings,
            trustsecsettings=trustsecsettings,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the network device.

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

        e_url = ('/ers/config/networkdevice/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e571185718b6ef6e78bfbfdf68_v3_1_1', _api_response)

    def bulk_request_for_network_device(self,
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
                'NetworkDeviceBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b2eebd5c245e58a503aa53115eec53_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/networkdevice/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b2eebd5c245e58a503aa53115eec53_v3_1_1', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_network_device <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.bulk_request_for_network_device>`_
        """
        return self.bulk_request_for_network_device(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_network_device(self,
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

        e_url = ('/ers/config/networkdevice/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bf96800cc265b5e9e1566ec7088619c_v3_1_1', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_network_device <#ciscoisesdk.
        api.v3_1_1.network_device.
        NetworkDevice.monitor_bulk_status_network_device>`_
        """
        return self.monitor_bulk_status_network_device(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )