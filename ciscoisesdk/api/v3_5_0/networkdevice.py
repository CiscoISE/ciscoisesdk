# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine networkdevice API wrapper.

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


class Networkdevice(object):
    """Identity Services Engine networkdevice API (version: 3.5.0).

    Wraps the Identity Services Engine networkdevice
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Networkdevice
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Networkdevice, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_networkdevice(self,
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
                Fields:[ipaddress, name, description,
                location, type].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name, description].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name, description].
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

        e_url = ('/ers/config/networkdevice/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6785492ac651ab88a9ce37ed8e2e36_v3_5_0', _api_response)

    def get_networkdevice_generator(self,
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
                Fields:[ipaddress, name, description,
                location, type].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name, description].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name, description].
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
            self.get_networkdevice, dict(
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

    def create_networkdevice(self,
                             authentication_settings=None,
                             coa_port=None,
                             description=None,
                             dtls_dns_name=None,
                             id=None,
                             model_name=None,
                             name=None,
                             network_device_group_list=None,
                             network_device_iplist=None,
                             profile_name=None,
                             snmpsettings=None,
                             software_version=None,
                             tacacs_settings=None,
                             tacacs_tls_settings=None,
                             trustsecsettings=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """Create.

        Args:
            network_device_group_list(list): List of NDG names for
                this node, property of the request body
                (list of strings).
            network_device_iplist(list): List of IPSubnets for this
                node, property of the request body (list
                of any objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(number): since 2.0 (for 3rd party), property of
                the request body.
            description(string): Description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            id(string): Id, property of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): since 2.0 (for 3rd party),
                property of the request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            tacacs_tls_settings(object): tacacsTlsSettings, property
                of the request body.
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
                'authenticationSettings':
                    authentication_settings,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'profileName':
                    profile_name,
                'snmpsettings':
                    snmpsettings,
                'tacacsSettings':
                    tacacs_settings,
                'tacacsTlsSettings':
                    tacacs_tls_settings,
                'trustsecsettings':
                    trustsecsettings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f9ce55d5dc7f53dfbcccc12e8ae6da63_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/networkdevice/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f9ce55d5dc7f53dfbcccc12e8ae6da63_v3_5_0', _api_response)

    def get_networkdevice_name_by_name(self,
                                       name,
                                       headers=None,
                                       **query_parameters):
        """Get-By-Name.

        Args:
            name(str): name path parameter.
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
        check_type(name, str,
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

        return self._object_factory('bpm_d8610d4a355b63aaaa364447d5fa00_v3_5_0', _api_response)

    def update_networkdevice_name_by_name(self,
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
                                          tacacs_tls_settings=None,
                                          trustsecsettings=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **query_parameters):
        """Update-By-Name.

        Args:
            network_device_group_list(list): List of NDG names for
                this node, property of the request body
                (list of strings).
            network_device_iplist(list): List of IPSubnets for this
                node, property of the request body (list
                of any objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(number): since 2.0 (for 3rd party), property of
                the request body.
            description(string): Description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            id(string): Id, property of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): since 2.0 (for 3rd party),
                property of the request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            tacacs_tls_settings(object): tacacsTlsSettings, property
                of the request body.
            trustsecsettings(object): trustsecsettings, property of
                the request body.
            name(str): name path parameter.
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
        check_type(name, str,
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
                'authenticationSettings':
                    authentication_settings,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'profileName':
                    profile_name,
                'snmpsettings':
                    snmpsettings,
                'tacacsSettings':
                    tacacs_settings,
                'tacacsTlsSettings':
                    tacacs_tls_settings,
                'trustsecsettings':
                    trustsecsettings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ea2c4586b845888b2a9375126f70de2_v3_5_0')\
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

        return self._object_factory('bpm_ea2c4586b845888b2a9375126f70de2_v3_5_0', _api_response)

    def delete_networkdevice_name_by_name(self,
                                          name,
                                          headers=None,
                                          **query_parameters):
        """Delete-By-Name.

        Args:
            name(str): name path parameter.
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
        check_type(name, str,
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

        return self._object_factory('bpm_eafaf2e785c6898fb982dbe4462e7_v3_5_0', _api_response)

    def patch_networkdevice_name_by_name(self,
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
                                         tacacs_tls_settings=None,
                                         trustsecsettings=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            network_device_group_list(list): List of NDG names for
                this node, property of the request body
                (list of strings).
            network_device_iplist(list): List of IPSubnets for this
                node, property of the request body (list
                of any objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(number): since 2.0 (for 3rd party), property of
                the request body.
            description(string): Description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            id(string): Id, property of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): since 2.0 (for 3rd party),
                property of the request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            tacacs_tls_settings(object): tacacsTlsSettings, property
                of the request body.
            trustsecsettings(object): trustsecsettings, property of
                the request body.
            name(str): name path parameter.
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
        check_type(name, str,
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
                'authenticationSettings':
                    authentication_settings,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'profileName':
                    profile_name,
                'snmpsettings':
                    snmpsettings,
                'tacacsSettings':
                    tacacs_settings,
                'tacacsTlsSettings':
                    tacacs_tls_settings,
                'trustsecsettings':
                    trustsecsettings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f3d98c9771c557b881dfc1d45516ea23_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/networkdevice/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_f3d98c9771c557b881dfc1d45516ea23_v3_5_0', _api_response)

    def get_networkdevice_by_id(self,
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

        e_url = ('/ers/config/networkdevice/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4ab683ce53052e089626a096abaf451_v3_5_0', _api_response)

    def update_networkdevice_by_id(self,
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
                                   tacacs_tls_settings=None,
                                   trustsecsettings=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Update.

        Args:
            network_device_group_list(list): List of NDG names for
                this node, property of the request body
                (list of strings).
            network_device_iplist(list): List of IPSubnets for this
                node, property of the request body (list
                of any objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(number): since 2.0 (for 3rd party), property of
                the request body.
            description(string): Description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            id(string): Id, property of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): since 2.0 (for 3rd party),
                property of the request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            tacacs_tls_settings(object): tacacsTlsSettings, property
                of the request body.
            trustsecsettings(object): trustsecsettings, property of
                the request body.
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
                'authenticationSettings':
                    authentication_settings,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'profileName':
                    profile_name,
                'snmpsettings':
                    snmpsettings,
                'tacacsSettings':
                    tacacs_settings,
                'tacacsTlsSettings':
                    tacacs_tls_settings,
                'trustsecsettings':
                    trustsecsettings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b1edfeb182025176bb250633937177ae_v3_5_0')\
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

        return self._object_factory('bpm_b1edfeb182025176bb250633937177ae_v3_5_0', _api_response)

    def delete_networkdevice_by_id(self,
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

        e_url = ('/ers/config/networkdevice/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f2fd3c6324b581ca0f3f9eadede1cdc_v3_5_0', _api_response)

    def patch_networkdevice_by_id(self,
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
                                  tacacs_tls_settings=None,
                                  trustsecsettings=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            network_device_group_list(list): List of NDG names for
                this node, property of the request body
                (list of strings).
            network_device_iplist(list): List of IPSubnets for this
                node, property of the request body (list
                of any objects).
            authentication_settings(object): authenticationSettings,
                property of the request body.
            coa_port(number): since 2.0 (for 3rd party), property of
                the request body.
            description(string): Description, property of the
                request body.
            dtls_dns_name(string): This value is used to verify the
                client identity contained in the X.509
                RADIUS/DTLS client certificate, property
                of the request body.
            id(string): Id, property of the request body.
            model_name(string): modelName, property of the request
                body.
            name(string): name, property of the request body.
            profile_name(string): since 2.0 (for 3rd party),
                property of the request body.
            snmpsettings(object): snmpsettings, property of the
                request body.
            software_version(string): softwareVersion, property of
                the request body.
            tacacs_settings(object): tacacsSettings, property of the
                request body.
            tacacs_tls_settings(object): tacacsTlsSettings, property
                of the request body.
            trustsecsettings(object): trustsecsettings, property of
                the request body.
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
                'authenticationSettings':
                    authentication_settings,
                'coaPort':
                    coa_port,
                'dtlsDnsName':
                    dtls_dns_name,
                'NetworkDeviceIPList':
                    network_device_iplist,
                'NetworkDeviceGroupList':
                    network_device_group_list,
                'modelName':
                    model_name,
                'softwareVersion':
                    software_version,
                'profileName':
                    profile_name,
                'snmpsettings':
                    snmpsettings,
                'tacacsSettings':
                    tacacs_settings,
                'tacacsTlsSettings':
                    tacacs_tls_settings,
                'trustsecsettings':
                    trustsecsettings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'NetworkDevice': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f3ef592da51cbb2ba2e239065d509_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/networkdevice/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_f3ef592da51cbb2ba2e239065d509_v3_5_0', _api_response)
