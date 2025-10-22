# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine activedirectory API wrapper.

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


class Activedirectory(object):
    """Identity Services Engine activedirectory API (version: 3.5.0).

    Wraps the Identity Services Engine activedirectory
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Activedirectory
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Activedirectory, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_activedirectory(self,
                            filter=None,
                            page=None,
                            size=None,
                            sortasc=None,
                            sortdsc=None,
                            headers=None,
                            **query_parameters):
        """Get all join points.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[name].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name].
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

        e_url = ('/ers/config/activedirectory/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d4b48930a5a5e8558f659f6cc2f77_v3_5_0', _api_response)

    def get_activedirectory_generator(self,
                                      filter=None,
                                      page=None,
                                      size=None,
                                      sortasc=None,
                                      sortdsc=None,
                                      headers=None,
                                      **query_parameters):
        """Get all join points.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[name].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name].
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
            self.get_activedirectory, dict(
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

    def create_activedirectory(self,
                               ad_attributes=None,
                               ad_scopes_names=None,
                               adgroups=None,
                               advanced_settings=None,
                               description=None,
                               domain=None,
                               enable_domain_allowed_list=None,
                               ers_active_directory_domains=None,
                               id=None,
                               name=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """Create join point.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e6326f97d53a58ff0b4a30c1b6423_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e6326f97d53a58ff0b4a30c1b6423_v3_5_0', _api_response)

    def update_activedirectory_passiveidsettings_by_id(self,
                                                       id,
                                                       ad_attributes=None,
                                                       ad_scopes_names=None,
                                                       adgroups=None,
                                                       advanced_settings=None,
                                                       description=None,
                                                       domain=None,
                                                       enable_domain_allowed_list=None,
                                                       ers_active_directory_domains=None,
                                                       name=None,
                                                       headers=None,
                                                       payload=None,
                                                       active_validation=True,
                                                       **query_parameters):
        """Updates passive ID settings.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a4f73d4359bd5ea980569899048dfdff_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/passiveIdSettings')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_a4f73d4359bd5ea980569899048dfdff_v3_5_0', _api_response)

    def update_activedirectory_addgroups_by_id(self,
                                               id,
                                               ad_attributes=None,
                                               ad_scopes_names=None,
                                               adgroups=None,
                                               advanced_settings=None,
                                               description=None,
                                               domain=None,
                                               enable_domain_allowed_list=None,
                                               ers_active_directory_domains=None,
                                               name=None,
                                               headers=None,
                                               payload=None,
                                               active_validation=True,
                                               **query_parameters):
        """Load groups from domain.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b05e80058df96e685baa727d578_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/addGroups')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b05e80058df96e685baa727d578_v3_5_0', _api_response)

    def update_activedirectory_getusergroups_by_id(self,
                                                   id,
                                                   additional_data=None,
                                                   headers=None,
                                                   payload=None,
                                                   active_validation=True,
                                                   **query_parameters):
        """Get user groups.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of any objects).
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
        _payload = payload or {}
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b839d4dee9b958e48ccef056603e253f_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/getUserGroups')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b839d4dee9b958e48ccef056603e253f_v3_5_0', _api_response)

    def get_activedirectory_name_by_name(self,
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

        e_url = ('/ers/config/activedirectory/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c6be021c4ca59e48c97afe218219bb1_v3_5_0', _api_response)

    def update_activedirectory_gettrusteddomains_by_id(self,
                                                       id,
                                                       headers=None,
                                                       **query_parameters):
        """Get trusted domains.

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

        e_url = ('/ers/config/activedirectory/{id}/getTrustedDomains')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d0ed84901325292ad4e2a91a174f6b2_v3_5_0', _api_response)

    def update_activedirectory_leaveallnodes_by_id(self,
                                                   id,
                                                   ad_attributes=None,
                                                   ad_scopes_names=None,
                                                   adgroups=None,
                                                   advanced_settings=None,
                                                   description=None,
                                                   domain=None,
                                                   enable_domain_allowed_list=None,
                                                   ers_active_directory_domains=None,
                                                   name=None,
                                                   headers=None,
                                                   payload=None,
                                                   active_validation=True,
                                                   **query_parameters):
        """Leave a domain with all nodes.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d011417d18d055ccb864c1dc2ae0456d_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/leaveAllNodes')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d011417d18d055ccb864c1dc2ae0456d_v3_5_0', _api_response)

    def update_activedirectory_join_by_id(self,
                                          id,
                                          ad_attributes=None,
                                          ad_scopes_names=None,
                                          adgroups=None,
                                          advanced_settings=None,
                                          description=None,
                                          domain=None,
                                          enable_domain_allowed_list=None,
                                          ers_active_directory_domains=None,
                                          name=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **query_parameters):
        """Join a domain.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b3284240745e5b929c51495fe80bc1c4_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/join')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b3284240745e5b929c51495fe80bc1c4_v3_5_0', _api_response)

    def update_activedirectory_joinallnodes_by_id(self,
                                                  id,
                                                  ad_attributes=None,
                                                  ad_scopes_names=None,
                                                  adgroups=None,
                                                  advanced_settings=None,
                                                  description=None,
                                                  domain=None,
                                                  enable_domain_allowed_list=None,
                                                  ers_active_directory_domains=None,
                                                  name=None,
                                                  headers=None,
                                                  payload=None,
                                                  active_validation=True,
                                                  **query_parameters):
        """Join a domain with all nodes.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e84705b918955b53afe61fc37911eb8b_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/joinAllNodes')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e84705b918955b53afe61fc37911eb8b_v3_5_0', _api_response)

    def update_activedirectory_getdomainusers_by_id(self,
                                                    id,
                                                    ad_attributes=None,
                                                    ad_scopes_names=None,
                                                    adgroups=None,
                                                    advanced_settings=None,
                                                    description=None,
                                                    domain=None,
                                                    enable_domain_allowed_list=None,
                                                    ers_active_directory_domains=None,
                                                    name=None,
                                                    headers=None,
                                                    payload=None,
                                                    active_validation=True,
                                                    **query_parameters):
        """Get domain users.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f7bf995f35dd5bf5a4bece3d60007fee_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/getDomainUsers')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_f7bf995f35dd5bf5a4bece3d60007fee_v3_5_0', _api_response)

    def update_activedirectory_isusermemberof_by_id(self,
                                                    id,
                                                    additional_data=None,
                                                    headers=None,
                                                    payload=None,
                                                    active_validation=True,
                                                    **query_parameters):
        """Is user a member of groups.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of any objects).
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
        _payload = payload or {}
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eae60ece5110590e97ddd910e8144ed2_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/isUserMemberOf')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_eae60ece5110590e97ddd910e8144ed2_v3_5_0', _api_response)

    def update_activedirectory_getgroupsbydomain_by_id(self,
                                                       id,
                                                       additional_data=None,
                                                       headers=None,
                                                       payload=None,
                                                       active_validation=True,
                                                       **query_parameters):
        """Get groups by domain.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of any objects).
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
        _payload = payload or {}
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fd729f50e65695966359b589a1606b_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/getGroupsByDomain')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_fd729f50e65695966359b589a1606b_v3_5_0', _api_response)

    def get_activedirectory_by_id(self,
                                  id,
                                  headers=None,
                                  **query_parameters):
        """Get join point details.

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

        e_url = ('/ers/config/activedirectory/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cfcc7615d0492e2dd1b04dd03a9_v3_5_0', _api_response)

    def delete_activedirectory_by_id(self,
                                     id,
                                     headers=None,
                                     **query_parameters):
        """Delete join point.

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

        e_url = ('/ers/config/activedirectory/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_febbe79ed5bb780d97a98f292b606_v3_5_0', _api_response)

    def update_activedirectory_leave_by_id(self,
                                           id,
                                           ad_attributes=None,
                                           ad_scopes_names=None,
                                           adgroups=None,
                                           advanced_settings=None,
                                           description=None,
                                           domain=None,
                                           enable_domain_allowed_list=None,
                                           ers_active_directory_domains=None,
                                           name=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **query_parameters):
        """Leave a domain.

        Args:
            ers_active_directory_domains(object):
                ERSActiveDirectoryDomains, property of
                the request body.
            ad_attributes(object): adAttributes, property of the
                request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma, property of the request body.
            adgroups(object): adgroups, property of the request
                body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): Description, property of the
                request body.
            domain(string): The AD domain, property of the request
                body.
            enable_domain_allowed_list(boolean):
                enableDomainAllowedList, property of the
                request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'domain':
                    domain,
                'adScopesNames':
                    ad_scopes_names,
                'enableDomainAllowedList':
                    enable_domain_allowed_list,
                'adgroups':
                    adgroups,
                'adAttributes':
                    ad_attributes,
                'advancedSettings':
                    advanced_settings,
                'ERSActiveDirectoryDomains':
                    ers_active_directory_domains,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e84541805d1da1fa3d4d581102a9_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/leave')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e84541805d1da1fa3d4d581102a9_v3_5_0', _api_response)
