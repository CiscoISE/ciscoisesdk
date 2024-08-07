# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine NativeSupplicantProfile API wrapper.

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

from builtins import *
from ...pagination import get_next_page
from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class NativeSupplicantProfile(object):
    """Identity Services Engine NativeSupplicantProfile API (version: 3.1.0).

    Wraps the Identity Services Engine NativeSupplicantProfile
    API and exposes the API as native Python
    methods that return native Python objects.

    | Native supplicant profile API provides the ability to update, delete and search native supplicant profiles.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.2                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | **Attribute**           | **Type**    | **Required** | **Description**                                                                | **Example Values**                                                                                 |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | name                    | String      | Yes          | Resource Name                                                                  | Cisco-ISE-NSP                                                                                      |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | id                      | String      | No           | Resource UUID, mandatory for update                                            | b8ce01e6-b150-4d4e-9698-40e48d5e0197                                                               |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | description             | String      | No           |                                                                                | Pre-configured Native Supplicant Profile. The SSID Will Need To Be Customized For Your Environment |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | wirelessProfiles        | List        | Yes          | List of Wireless profiles                                                      |                                                                                                    |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | - ssid                  | String      | Yes          | SSID for the wireless profile                                                  | ISE                                                                                                |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | - allowedProtocol       | Enum        | Yes          | Allowed protocol for the wireless profile.                                     | TLS                                                                                                |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | - certificateTemplateId | String      | No           | Certificate template ID                                                        | 0ca8f1b6-500d-560b-e053-75189a0ab0d1                                                               |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | - actionType            | Enum        | Yes          | Action type for WifiProfile.                                                   | UPDATE                                                                                             |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
    | - previousSsid          | String      | Yes          | Previous ssid for WifiProfile (required for updating existing WirelessProfile) | ssid1                                                                                              |
    +-------------------------+-------------+--------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NativeSupplicantProfile
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NativeSupplicantProfile, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_native_supplicant_profile_by_id(self,
                                            id,
                                            headers=None,
                                            **query_parameters):
        """This API allows the client to get a native supplicant profile by
        ID.

        Args:
            id(str): id path parameter.
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
                           str, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           str)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
                           str)

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

        e_url = ('/ers/config/nspprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d1b9755414c5dcbb61987b2dd06839a_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_native_supplicant_profile_by_id <#ciscoisesdk.
        api.v3_1_0.native_supplicant_profile.
        NativeSupplicantProfile.get_native_supplicant_profile_by_id>`_
        """
        return self.get_native_supplicant_profile_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_native_supplicant_profile_by_id(self,
                                               id,
                                               description=None,
                                               name=None,
                                               wireless_profiles=None,
                                               headers=None,
                                               payload=None,
                                               active_validation=True,
                                               **query_parameters):
        """This API allows the client to update a native supplicant
        profile.

        Args:
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            name(string): name, property of the request body.
            wireless_profiles(list): wirelessProfiles, property of
                the request body (list of objects).
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
                           str, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           str)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
                           str)

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
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'wirelessProfiles':
                    wireless_profiles,
            }
            _payload = {
                'ERSNSPProfile': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c54a2ad63f46527dbec140a05f1213b7_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/nspprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c54a2ad63f46527dbec140a05f1213b7_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     description=None,
                     name=None,
                     wireless_profiles=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_native_supplicant_profile_by_id <#ciscoisesdk.
        api.v3_1_0.native_supplicant_profile.
        NativeSupplicantProfile.update_native_supplicant_profile_by_id>`_
        """
        return self.update_native_supplicant_profile_by_id(
            id=id,
            description=description,
            name=name,
            wireless_profiles=wireless_profiles,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_native_supplicant_profile_by_id(self,
                                               id,
                                               headers=None,
                                               **query_parameters):
        """This API deletes a native supplicant profile.

        Args:
            id(str): id path parameter.
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
                           str, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           str)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
                           str)

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

        e_url = ('/ers/config/nspprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fff9d421c78597d98a54dd08a9a99f9_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_native_supplicant_profile_by_id <#ciscoisesdk.
        api.v3_1_0.native_supplicant_profile.
        NativeSupplicantProfile.delete_native_supplicant_profile_by_id>`_
        """
        return self.delete_native_supplicant_profile_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_native_supplicant_profile(self,
                                      page=None,
                                      size=None,
                                      headers=None,
                                      **query_parameters):
        """This API allows the client to get all the native supplicant
        profiles.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
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
                           str, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           str)
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
                           str)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))

        _params = {
            'page':
                page,
            'size':
                size,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/nspprofile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fa9802505d7bbdf85b951581db47_v3_1_0', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_native_supplicant_profile <#ciscoisesdk.
        api.v3_1_0.native_supplicant_profile.
        NativeSupplicantProfile.get_native_supplicant_profile>`_
        """
        return self.get_native_supplicant_profile(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_native_supplicant_profile_generator(self,
                                                page=None,
                                                size=None,
                                                headers=None,
                                                **query_parameters):
        """This API allows the client to get all the native supplicant
        profiles.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
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
            self.get_native_supplicant_profile, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          page=None,
                          size=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_native_supplicant_profile_generator <#ciscoisesdk.
        api.v3_1_0.native_supplicant_profile.
        NativeSupplicantProfile.get_native_supplicant_profile_generator>`_
        """
        yield from get_next_page(
            self.get_native_supplicant_profile, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the native supplicant profile.

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
                           str, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str, may_be_none=False)

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

        e_url = ('/ers/config/nspprofile/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f577c55d36b05178b0275dd88c71e118_v3_1_0', _api_response)
