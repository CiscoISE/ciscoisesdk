# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine DownloadableACL API wrapper.

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


class DownloadableAcl(object):
    """Identity Services Engine DownloadableACL API (version: 3.1.1).

    Wraps the Identity Services Engine DownloadableACL
    API and exposes the API as native Python
    methods that return native Python objects.

    | Downloadable ACL API allows the client to add, delete, update, search and perform actions on downloadable ACL.

    **Revision History**

    +------------+--------------------+-------------------+-----------------------------------------+-----------------------+-----------------------------------+
    | Revision # | Resource   Version | Cisco ISE Version | Description                             | Revision Modification | Revision Modification             |
    +------------+--------------------+-------------------+-----------------------------------------+-----------------------+-----------------------------------+
    |            |                    |                   |                                         | Attribute             | Description                       |
    +------------+--------------------+-------------------+-----------------------------------------+-----------------------+-----------------------------------+
    | 0          | 1.0                | 2.3               | Initial Cisco ISE Version               |                       |                                   |
    +------------+--------------------+-------------------+-----------------------------------------+-----------------------+-----------------------------------+
    | 1          | 1.1                | 2.6               | Support new attribute IP version in 2.6 | daclType              | Added Enum   Attribute 'daclType' |
    +------------+--------------------+-------------------+-----------------------------------------+-----------------------+-----------------------------------+

    |

    **Resource Definition**

    +---------------+-----------+--------------+---------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | **Attribute** | **Type**  | **Required** | **Description**                                                                       | **Default Values** | **Example Values**                   |
    +---------------+-----------+--------------+---------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | name          | String    | Yes          | Resource Name. Name may contain alphanumeric or any of the following characters [_.-] |                    | multiline_acl                        |
    +---------------+-----------+--------------+---------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | id            | String    | Yes          | Resource UUID                                                                         |                    | c1e0e9e0-717f-11eb-9fb2-b6cb23d38630 |
    +---------------+-----------+--------------+---------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | description   | String    | No           | Use the string \\n for a newline                                                       |                    | description                          |
    +---------------+-----------+--------------+---------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | dacl          | String    | Yes          | The DACL Content. Use the string \\n for a newline                                     |                    | permit ip any any                    |
    +---------------+-----------+--------------+---------------------------------------------------------------------------------------+--------------------+--------------------------------------+
    | daclType      | Enum      | No           | Allowed values: IPV4, IPV6, IP_AGNOSTIC                                               | IPV4               |                                      |
    +---------------+-----------+--------------+---------------------------------------------------------------------------------------+--------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DownloadableAcl
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DownloadableAcl, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_downloadable_acl_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to get a downloadable ACL by ID.

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
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
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

        e_url = ('/ers/config/downloadableacl/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dfa8f48210e85715beebb44e62fac408_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_downloadable_acl_by_id <#ciscoisesdk.
        api.v3_1_1.downloadable_acl.
        DownloadableAcl.get_downloadable_acl_by_id>`_
        """
        return self.get_downloadable_acl_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_downloadable_acl_by_id(self,
                                      id,
                                      dacl=None,
                                      dacl_type=None,
                                      description=None,
                                      name=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """This API allows the client to update a downloadable ACL.

        Args:
            dacl(string): The DACL Content. Use the string \\n for a
                newline, property of the request body.
            dacl_type(string): Allowed values: IPV4, IPV6,
                IP_AGNOSTIC, property of the request
                body.
            description(string): Use the string \\n for a newline,
                property of the request body.
            id(string): id, property of the request body.
            name(string): Resource Name. Name may contain
                alphanumeric or any of the following
                characters [_.-], property of the
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
                'name':
                    name,
                'description':
                    description,
                'dacl':
                    dacl,
                'daclType':
                    dacl_type,
            }
            _payload = {
                'DownloadableAcl': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d8c7ba0cb8f56d99135e16d2d973d11_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/downloadableacl/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d8c7ba0cb8f56d99135e16d2d973d11_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     dacl=None,
                     dacl_type=None,
                     description=None,
                     name=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_downloadable_acl_by_id <#ciscoisesdk.
        api.v3_1_1.downloadable_acl.
        DownloadableAcl.update_downloadable_acl_by_id>`_
        """
        return self.update_downloadable_acl_by_id(
            id=id,
            dacl=dacl,
            dacl_type=dacl_type,
            description=description,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_downloadable_acl_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """This API deletes a downloadable ACL.

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
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
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

        e_url = ('/ers/config/downloadableacl/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b3db444eaa50678218c29f88de60e8_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_downloadable_acl_by_id <#ciscoisesdk.
        api.v3_1_1.downloadable_acl.
        DownloadableAcl.delete_downloadable_acl_by_id>`_
        """
        return self.delete_downloadable_acl_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_downloadable_acl(self,
                             page=None,
                             size=None,
                             headers=None,
                             **query_parameters):
        """This API allows the client to get all downloadable ACLs.

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

        e_url = ('/ers/config/downloadableacl')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bc200af85d598885a990ff9bcbf8_v3_1_1', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_downloadable_acl <#ciscoisesdk.
        api.v3_1_1.downloadable_acl.
        DownloadableAcl.get_downloadable_acl>`_
        """
        return self.get_downloadable_acl(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_downloadable_acl_generator(self,
                                       page=None,
                                       size=None,
                                       headers=None,
                                       **query_parameters):
        """This API allows the client to get all downloadable ACLs.

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
            self.get_downloadable_acl, dict(
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
        """Alias for `get_downloadable_acl_generator <#ciscoisesdk.
        api.v3_1_1.downloadable_acl.
        DownloadableAcl.get_downloadable_acl_generator>`_
        """
        yield from get_next_page(
            self.get_downloadable_acl, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_downloadable_acl(self,
                                dacl=None,
                                dacl_type=None,
                                description=None,
                                name=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """This API creates a downloadable ACL.

        Args:
            dacl(string): The DACL Content. Use the string \\n for a
                newline, property of the request body.
            dacl_type(string): Allowed values: IPV4, IPV6,
                IP_AGNOSTIC, property of the request
                body.
            description(string): Use the string \\n for a newline,
                property of the request body.
            name(string): Resource Name. Name may contain
                alphanumeric or any of the following
                characters [_.-], property of the
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
                'dacl':
                    dacl,
                'daclType':
                    dacl_type,
            }
            _payload = {
                'DownloadableAcl': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_adcf947c42fe5588b7b82d9c43a3bbf0_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/downloadableacl')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_adcf947c42fe5588b7b82d9c43a3bbf0_v3_1_1', _api_response)

    def create(self,
               dacl=None,
               dacl_type=None,
               description=None,
               name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_downloadable_acl <#ciscoisesdk.
        api.v3_1_1.downloadable_acl.
        DownloadableAcl.create_downloadable_acl>`_
        """
        return self.create_downloadable_acl(
            dacl=dacl,
            dacl_type=dacl_type,
            description=description,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the downloadable ACL.

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

        e_url = ('/ers/config/downloadableacl/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d10b7914625e5da0861cbeab4cf6440e_v3_1_1', _api_response)
