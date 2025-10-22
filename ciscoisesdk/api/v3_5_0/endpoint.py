# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine endpoint API wrapper.

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


class Endpoint(object):
    """Identity Services Engine endpoint API (version: 3.5.0).

    Wraps the Identity Services Engine endpoint
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Endpoint
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Endpoint, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_endpoint(self,
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
                Fields:[logicalProfileName, portalUser,
                staticProfileAssignment, profileId,
                profile, groupId, staticGroupAssignment,
                mac].
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

        e_url = ('/ers/config/endpoint/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d8b3fff70235400905c32ae03298dcf_v3_5_0', _api_response)

    def get_endpoint_generator(self,
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
                Fields:[logicalProfileName, portalUser,
                staticProfileAssignment, profileId,
                profile, groupId, staticGroupAssignment,
                mac].
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
            self.get_endpoint, dict(
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

    def create_endpoint(self,
                        custom_attributes=None,
                        description=None,
                        group_id=None,
                        id=None,
                        identity_store=None,
                        identity_store_id=None,
                        mac=None,
                        mdm_attributes=None,
                        name=None,
                        portal_user=None,
                        profile_id=None,
                        static_group_assignment=None,
                        static_group_assignment_defined=None,
                        static_profile_assignment=None,
                        static_profile_assignment_defined=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **query_parameters):
        """Create.

        Args:
            custom_attributes(object): Key value map, property of
                the request body.
            description(string): Description, property of the
                request body.
            group_id(string): groupId, property of the request body.
            id(string): Id, property of the request body.
            identity_store(string): This field is for read only,
                property of the request body.
            identity_store_id(string): This field is for read only,
                property of the request body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): MDM Attributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_group_assignment_defined(boolean):
                staticGroupAssignmentDefined, property
                of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            static_profile_assignment_defined(boolean):
                staticProfileAssignmentDefined, property
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
                'customAttributes':
                    custom_attributes,
                'groupId':
                    group_id,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'mac':
                    mac,
                'portalUser':
                    portal_user,
                'profileId':
                    profile_id,
                'staticGroupAssignment':
                    static_group_assignment,
                'staticGroupAssignmentDefined':
                    static_group_assignment_defined,
                'staticProfileAssignment':
                    static_profile_assignment,
                'staticProfileAssignmentDefined':
                    static_profile_assignment_defined,
                'mdmAttributes':
                    mdm_attributes,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSEndPoint': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_af7decaa9bf5e799adb5d8bdff495e2_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_af7decaa9bf5e799adb5d8bdff495e2_v3_5_0', _api_response)

    def update_endpoint_deregister_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """DeRegister.

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

        e_url = ('/ers/config/endpoint/{id}/deregister')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed121b2686e85bd5b28c068c3c0de220_v3_5_0', _api_response)

    def update_endpoint_releaserejectedendpoint_by_id(self,
                                                      id,
                                                      headers=None,
                                                      **query_parameters):
        """ReleaseRejectedEndpoint.

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

        e_url = ('/ers/config/endpoint/{id}/releaserejectedendpoint')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f4f97557daacb3dadaced526cc_v3_5_0', _api_response)

    def get_endpoint_getrejectedendpoints(self,
                                          filter=None,
                                          page=None,
                                          size=None,
                                          sortasc=None,
                                          sortdsc=None,
                                          headers=None,
                                          **query_parameters):
        """GetRejectedEndpoints.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[logicalProfileName, portalUser,
                staticProfileAssignment, profileId,
                profile, groupId, staticGroupAssignment,
                mac].
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

        e_url = ('/ers/config/endpoint/getrejectedendpoints')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f8a2f0834e625822bed1cb4cf34fde5e_v3_5_0', _api_response)

    def get_endpoint_getrejectedendpoints_generator(self,
                                                    filter=None,
                                                    page=None,
                                                    size=None,
                                                    sortasc=None,
                                                    sortdsc=None,
                                                    headers=None,
                                                    **query_parameters):
        """GetRejectedEndpoints.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[logicalProfileName, portalUser,
                staticProfileAssignment, profileId,
                profile, groupId, staticGroupAssignment,
                mac].
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
            self.get_endpoint_getrejectedendpoints, dict(
                filter=filter,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def get_endpoint_name_by_name(self,
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

        e_url = ('/ers/config/endpoint/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d53842e83f0538cab91e097aa6800ce_v3_5_0', _api_response)

    def get_endpoint_by_id(self,
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

        e_url = ('/ers/config/endpoint/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eb8e0ce63376573995a49178435f7747_v3_5_0', _api_response)

    def update_endpoint_by_id(self,
                              id,
                              custom_attributes=None,
                              description=None,
                              group_id=None,
                              identity_store=None,
                              identity_store_id=None,
                              mac=None,
                              mdm_attributes=None,
                              name=None,
                              portal_user=None,
                              profile_id=None,
                              static_group_assignment=None,
                              static_group_assignment_defined=None,
                              static_profile_assignment=None,
                              static_profile_assignment_defined=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Update.

        Args:
            custom_attributes(object): Key value map, property of
                the request body.
            description(string): Description, property of the
                request body.
            group_id(string): groupId, property of the request body.
            id(string): Id, property of the request body.
            identity_store(string): This field is for read only,
                property of the request body.
            identity_store_id(string): This field is for read only,
                property of the request body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): MDM Attributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_group_assignment_defined(boolean):
                staticGroupAssignmentDefined, property
                of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            static_profile_assignment_defined(boolean):
                staticProfileAssignmentDefined, property
                of the request body.
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
                'customAttributes':
                    custom_attributes,
                'groupId':
                    group_id,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'mac':
                    mac,
                'portalUser':
                    portal_user,
                'profileId':
                    profile_id,
                'staticGroupAssignment':
                    static_group_assignment,
                'staticGroupAssignmentDefined':
                    static_group_assignment_defined,
                'staticProfileAssignment':
                    static_profile_assignment,
                'staticProfileAssignmentDefined':
                    static_profile_assignment_defined,
                'mdmAttributes':
                    mdm_attributes,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSEndPoint': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c8b30af4b84b5a90be2fc152cf26ad42_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c8b30af4b84b5a90be2fc152cf26ad42_v3_5_0', _api_response)

    def delete_endpoint_by_id(self,
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

        e_url = ('/ers/config/endpoint/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f1cac5f578ab6509196266ad8e3_v3_5_0', _api_response)

    def patch_endpoint_by_id(self,
                             id,
                             custom_attributes=None,
                             description=None,
                             group_id=None,
                             identity_store=None,
                             identity_store_id=None,
                             mac=None,
                             mdm_attributes=None,
                             name=None,
                             portal_user=None,
                             profile_id=None,
                             static_group_assignment=None,
                             static_group_assignment_defined=None,
                             static_profile_assignment=None,
                             static_profile_assignment_defined=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            custom_attributes(object): Key value map, property of
                the request body.
            description(string): Description, property of the
                request body.
            group_id(string): groupId, property of the request body.
            id(string): Id, property of the request body.
            identity_store(string): This field is for read only,
                property of the request body.
            identity_store_id(string): This field is for read only,
                property of the request body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): MDM Attributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_group_assignment_defined(boolean):
                staticGroupAssignmentDefined, property
                of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            static_profile_assignment_defined(boolean):
                staticProfileAssignmentDefined, property
                of the request body.
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
                'customAttributes':
                    custom_attributes,
                'groupId':
                    group_id,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'mac':
                    mac,
                'portalUser':
                    portal_user,
                'profileId':
                    profile_id,
                'staticGroupAssignment':
                    static_group_assignment,
                'staticGroupAssignmentDefined':
                    static_group_assignment_defined,
                'staticProfileAssignment':
                    static_profile_assignment,
                'staticProfileAssignmentDefined':
                    static_profile_assignment_defined,
                'mdmAttributes':
                    mdm_attributes,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSEndPoint': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a107646bee520ba8247b06bf23311c_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_a107646bee520ba8247b06bf23311c_v3_5_0', _api_response)

    def update_endpoint_register(self,
                                 custom_attributes=None,
                                 description=None,
                                 group_id=None,
                                 id=None,
                                 identity_store=None,
                                 identity_store_id=None,
                                 mac=None,
                                 mdm_attributes=None,
                                 name=None,
                                 portal_user=None,
                                 profile_id=None,
                                 static_group_assignment=None,
                                 static_group_assignment_defined=None,
                                 static_profile_assignment=None,
                                 static_profile_assignment_defined=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **query_parameters):
        """Register.

        Args:
            custom_attributes(object): Key value map, property of
                the request body.
            description(string): Description, property of the
                request body.
            group_id(string): groupId, property of the request body.
            id(string): Id, property of the request body.
            identity_store(string): This field is for read only,
                property of the request body.
            identity_store_id(string): This field is for read only,
                property of the request body.
            mac(string): mac, property of the request body.
            mdm_attributes(object): MDM Attributes, property of the
                request body.
            name(string): name, property of the request body.
            portal_user(string): portalUser, property of the request
                body.
            profile_id(string): profileId, property of the request
                body.
            static_group_assignment(boolean): staticGroupAssignment,
                property of the request body.
            static_group_assignment_defined(boolean):
                staticGroupAssignmentDefined, property
                of the request body.
            static_profile_assignment(boolean):
                staticProfileAssignment, property of the
                request body.
            static_profile_assignment_defined(boolean):
                staticProfileAssignmentDefined, property
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
                'customAttributes':
                    custom_attributes,
                'groupId':
                    group_id,
                'identityStore':
                    identity_store,
                'identityStoreId':
                    identity_store_id,
                'mac':
                    mac,
                'portalUser':
                    portal_user,
                'profileId':
                    profile_id,
                'staticGroupAssignment':
                    static_group_assignment,
                'staticGroupAssignmentDefined':
                    static_group_assignment_defined,
                'staticProfileAssignment':
                    static_profile_assignment,
                'staticProfileAssignmentDefined':
                    static_profile_assignment_defined,
                'mdmAttributes':
                    mdm_attributes,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSEndPoint': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dfaeea899c185169ae2a3b70b5491008_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/endpoint/register')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_dfaeea899c185169ae2a3b70b5491008_v3_5_0', _api_response)
