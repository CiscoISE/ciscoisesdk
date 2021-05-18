# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine AuthorizationProfile API wrapper.

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
import urllib.parse


class AuthorizationProfile(object):
    """Identity Services Engine AuthorizationProfile API (version: 3.0.0).

    Wraps the Identity Services Engine AuthorizationProfile
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new AuthorizationProfile
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(AuthorizationProfile, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_all_authorization_profiles(self,
                                       page=None,
                                       size=None,
                                       headers=None,
                                       **query_parameters):
        """Get all AuthorizationProfile.

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
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))

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

        e_url = ('/ers/config/authorizationprofile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e232c5666ab5ed783588f413c3bc644_v3_0_0', _api_response)

    def get_all_authorization_profiles_generator(self,
                                                 page=None,
                                                 size=None,
                                                 headers=None,
                                                 **query_parameters):
        """Get all AuthorizationProfile.

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
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))

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

        e_url = ('/ers/config/authorizationprofile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        yield self._object_factory('bpm_e232c5666ab5ed783588f413c3bc644_v3_0_0', _api_response)
        if _api_response.response and _api_response.response.get("SearchResult", {}).get("nextPage", {}).get("href", ""):
            url = _api_response.response.get("SearchResult", {}).get("nextPage", {}).get("href", "")
            _query_params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            _size = _query_params.get('size')
            _page = _query_params.get('page')
            yield from self.get_all_authorization_profiles_generator(headers=headers,
                                                                     page=_page,
                                                                     size=_size,
                                                                     **query_parameters)

    def create_authorization_profile(self,
                                     access_type=None,
                                     acl=None,
                                     advanced_attributes=None,
                                     airespace_acl=None,
                                     airespace_i_pv6_acl=None,
                                     asa_vpn=None,
                                     authz_profile_type=None,
                                     auto_smart_port=None,
                                     avc_profile=None,
                                     dacl_name=None,
                                     description=None,
                                     easywired_session_candidate=None,
                                     id=None,
                                     interface_template=None,
                                     ipv6_acl_filter=None,
                                     ipv6_dacl_name=None,
                                     mac_sec_policy=None,
                                     name=None,
                                     neat=None,
                                     profile_name=None,
                                     reauth=None,
                                     service_template=None,
                                     track_movement=None,
                                     vlan=None,
                                     voice_domain_permission=None,
                                     web_auth=None,
                                     web_redirection=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **query_parameters):
        """Create AuthorizationProfile.

        Args:
            access_type(string): accessType, property of the request
                body.
            acl(string): acl, property of the request body.
            advancedAttributes(list): advancedAttributes, property
                of the request body (list of objects).
            airespace_acl(string): airespaceACL, property of the
                request body.
            airespace_i_pv6_acl(string): airespaceIPv6ACL, property
                of the request body.
            asa_vpn(string): asaVpn, property of the request body.
            authz_profile_type(string): authzProfileType, property
                of the request body.
            auto_smart_port(string): autoSmartPort, property of the
                request body.
            avc_profile(string): avcProfile, property of the request
                body.
            dacl_name(string): daclName, property of the request
                body.
            description(string): description, property of the
                request body.
            easywired_session_candidate(boolean):
                easywiredSessionCandidate, property of
                the request body.
            id(string): id, property of the request body.
            interface_template(string): interfaceTemplate, property
                of the request body.
            ipv6_acl_filter(string): ipv6ACLFilter, property of the
                request body.
            ipv6_dacl_name(string): ipv6DaclName, property of the
                request body.
            mac_sec_policy(string): macSecPolicy, property of the
                request body.
            name(string): name, property of the request body.
            neat(boolean): neat, property of the request body.
            profile_name(string): profileName, property of the
                request body.
            reauth(object): reauth, property of the request body.
            service_template(boolean): serviceTemplate, property of
                the request body.
            track_movement(boolean): trackMovement, property of the
                request body.
            vlan(object): vlan, property of the request body.
            voice_domain_permission(boolean): voiceDomainPermission,
                property of the request body.
            web_auth(boolean): webAuth, property of the request
                body.
            web_redirection(object): webRedirection, property of the
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
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'advancedAttributes':
                    advanced_attributes,
                'accessType':
                    access_type,
                'authzProfileType':
                    authz_profile_type,
                'vlan':
                    vlan,
                'reauth':
                    reauth,
                'airespaceACL':
                    airespace_acl,
                'airespaceIPv6ACL':
                    airespace_i_pv6_acl,
                'webRedirection':
                    web_redirection,
                'acl':
                    acl,
                'trackMovement':
                    track_movement,
                'serviceTemplate':
                    service_template,
                'easywiredSessionCandidate':
                    easywired_session_candidate,
                'daclName':
                    dacl_name,
                'voiceDomainPermission':
                    voice_domain_permission,
                'neat':
                    neat,
                'webAuth':
                    web_auth,
                'autoSmartPort':
                    auto_smart_port,
                'interfaceTemplate':
                    interface_template,
                'ipv6ACLFilter':
                    ipv6_acl_filter,
                'avcProfile':
                    avc_profile,
                'macSecPolicy':
                    mac_sec_policy,
                'asaVpn':
                    asa_vpn,
                'profileName':
                    profile_name,
                'ipv6DaclName':
                    ipv6_dacl_name,
            }
            _payload = {
                'AuthorizationProfile': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c43118f80d4556a8ec759a8c41e2097_v3_0_0')\
                .validate(_payload)

        e_url = ('/ers/config/authorizationprofile')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c43118f80d4556a8ec759a8c41e2097_v3_0_0', _api_response)

    def get_authorization_profile_by_id(self,
                                        id,
                                        headers=None,
                                        **query_parameters):
        """Get AuthorizationProfile by Id.

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

        e_url = ('/ers/config/authorizationprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a69c7f1ad54e5e9cae1f871e19eed61b_v3_0_0', _api_response)

    def update_authorization_profile_by_id(self,
                                           id,
                                           access_type=None,
                                           acl=None,
                                           advanced_attributes=None,
                                           airespace_acl=None,
                                           airespace_i_pv6_acl=None,
                                           asa_vpn=None,
                                           authz_profile_type=None,
                                           auto_smart_port=None,
                                           avc_profile=None,
                                           dacl_name=None,
                                           description=None,
                                           easywired_session_candidate=None,
                                           interface_template=None,
                                           ipv6_acl_filter=None,
                                           ipv6_dacl_name=None,
                                           mac_sec_policy=None,
                                           name=None,
                                           neat=None,
                                           profile_name=None,
                                           reauth=None,
                                           service_template=None,
                                           track_movement=None,
                                           vlan=None,
                                           voice_domain_permission=None,
                                           web_auth=None,
                                           web_redirection=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **query_parameters):
        """Update AuthorizationProfile.

        Args:
            access_type(string): accessType, property of the request
                body.
            acl(string): acl, property of the request body.
            advancedAttributes(list): advancedAttributes, property
                of the request body (list of objects).
            airespace_acl(string): airespaceACL, property of the
                request body.
            airespace_i_pv6_acl(string): airespaceIPv6ACL, property
                of the request body.
            asa_vpn(string): asaVpn, property of the request body.
            authz_profile_type(string): authzProfileType, property
                of the request body.
            auto_smart_port(string): autoSmartPort, property of the
                request body.
            avc_profile(string): avcProfile, property of the request
                body.
            dacl_name(string): daclName, property of the request
                body.
            description(string): description, property of the
                request body.
            easywired_session_candidate(boolean):
                easywiredSessionCandidate, property of
                the request body.
            id(string): id, property of the request body.
            interface_template(string): interfaceTemplate, property
                of the request body.
            ipv6_acl_filter(string): ipv6ACLFilter, property of the
                request body.
            ipv6_dacl_name(string): ipv6DaclName, property of the
                request body.
            mac_sec_policy(string): macSecPolicy, property of the
                request body.
            name(string): name, property of the request body.
            neat(boolean): neat, property of the request body.
            profile_name(string): profileName, property of the
                request body.
            reauth(object): reauth, property of the request body.
            service_template(boolean): serviceTemplate, property of
                the request body.
            track_movement(boolean): trackMovement, property of the
                request body.
            vlan(object): vlan, property of the request body.
            voice_domain_permission(boolean): voiceDomainPermission,
                property of the request body.
            web_auth(boolean): webAuth, property of the request
                body.
            web_redirection(object): webRedirection, property of the
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
                'name':
                    name,
                'description':
                    description,
                'advancedAttributes':
                    advanced_attributes,
                'accessType':
                    access_type,
                'authzProfileType':
                    authz_profile_type,
                'vlan':
                    vlan,
                'reauth':
                    reauth,
                'airespaceACL':
                    airespace_acl,
                'airespaceIPv6ACL':
                    airespace_i_pv6_acl,
                'webRedirection':
                    web_redirection,
                'acl':
                    acl,
                'trackMovement':
                    track_movement,
                'serviceTemplate':
                    service_template,
                'easywiredSessionCandidate':
                    easywired_session_candidate,
                'daclName':
                    dacl_name,
                'voiceDomainPermission':
                    voice_domain_permission,
                'neat':
                    neat,
                'webAuth':
                    web_auth,
                'autoSmartPort':
                    auto_smart_port,
                'interfaceTemplate':
                    interface_template,
                'ipv6ACLFilter':
                    ipv6_acl_filter,
                'avcProfile':
                    avc_profile,
                'macSecPolicy':
                    mac_sec_policy,
                'asaVpn':
                    asa_vpn,
                'profileName':
                    profile_name,
                'ipv6DaclName':
                    ipv6_dacl_name,
            }
            _payload = {
                'AuthorizationProfile': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cb9f26e93655e7d89995b172f6fd97f_v3_0_0')\
                .validate(_payload)

        e_url = ('/ers/config/authorizationprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_cb9f26e93655e7d89995b172f6fd97f_v3_0_0', _api_response)

    def delete_authorization_profile_by_id(self,
                                           id,
                                           headers=None,
                                           **query_parameters):
        """Delete AuthorizationProfile.

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

        e_url = ('/ers/config/authorizationprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c3913dfbda305f678ede16f782762ad3_v3_0_0', _api_response)

    def get_authorization_profile_by_name(self,
                                          name,
                                          headers=None,
                                          **query_parameters):
        """Get AuthorizationProfile by name.

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

        e_url = ('/ers/config/authorizationprofile/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_acf0372068885036baee3c4524638f31_v3_0_0', _api_response)
