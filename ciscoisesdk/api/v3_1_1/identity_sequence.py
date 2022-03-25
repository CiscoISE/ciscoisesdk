# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine IdentitySequence API wrapper.

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


class IdentitySequence(object):
    """Identity Services Engine IdentitySequence API (version: 3.1.1).

    Wraps the Identity Services Engine IdentitySequence
    API and exposes the API as native Python
    methods that return native Python objects.

    | Identity Sequence API allows the client to add, delete, update and search Identity sequences.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.2                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+
    | 1              | 1.1                  | 2.4                   | Added GetByName operation |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
    | **Attribute**                    | **Type**    | **Required** | **Description**                                                                                               | **Example Values**                                               |
    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
    | name                             | String      | Yes          | Resource Name                                                                                                 | All_User_ID_Stores                                               |
    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
    | id                               | String      | No           | Resource UUID, mandatory for update                                                                           | 93246270-8c01-11e6-996c-525400b48521                             |
    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
    | description                      | String      | No           |                                                                                                               | A built-in Identity Sequence to include all User Identity Stores |
    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
    | breakOnStoreFail                 | Boolean     | Yes          | Do not access other stores in the sequence If a selected identity store cannot be accessed for authentication | false                                                            |
    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
    | certificateAuthenticationProfile | String      | Yes          | Certificate Authentication Profile, empty if doesn't exist                                                    | Preloaded_Certificate_Profile                                    |
    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
    | idSeqItem                        | List        | Yes          | List of id stores comprised of id store name and order                                                        | [ { "idstore": "Internal Users", "order": 1 },                   |
    |                                  |             |              |                                                                                                               | { "idstore": "All_AD_Join_Points", "order": 2 },                 |
    |                                  |             |              |                                                                                                               | { "idstore": "Guest Users", "order": 3 } ]                       |
    +----------------------------------+-------------+--------------+---------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new IdentitySequence
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(IdentitySequence, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_identity_sequence_by_name(self,
                                      name,
                                      headers=None,
                                      **query_parameters):
        """This API allows the client to get an identity sequence by name.

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
            if 'X-CSRF-Token' in headers:
                check_type(headers.get('X-CSRF-Token'),
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

        e_url = ('/ers/config/idstoresequence/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_db686413cf4558188ea60ccc05c3e920_v3_1_1', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_identity_sequence_by_name <#ciscoisesdk.
        api.v3_1_1.identity_sequence.
        IdentitySequence.get_identity_sequence_by_name>`_
        """
        return self.get_identity_sequence_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_identity_sequence_by_id(self,
                                    id,
                                    headers=None,
                                    **query_parameters):
        """This API allows the client to get an identity sequence by ID.

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

        e_url = ('/ers/config/idstoresequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cb9345e58f5433ae80f5d8f855978b_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_identity_sequence_by_id <#ciscoisesdk.
        api.v3_1_1.identity_sequence.
        IdentitySequence.get_identity_sequence_by_id>`_
        """
        return self.get_identity_sequence_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_identity_sequence_by_id(self,
                                       id,
                                       break_on_store_fail=None,
                                       certificate_authentication_profile=None,
                                       description=None,
                                       id_seq_item=None,
                                       name=None,
                                       parent=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """This API allows the client to update an identity sequence.
        Partial update is not supported.

        Args:
            break_on_store_fail(boolean): breakOnStoreFail, property
                of the request body.
            certificate_authentication_profile(string):
                certificateAuthenticationProfile,
                property of the request body.
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            id_seq_item(list): idSeqItem, property of the request
                body (list of objects).
            name(string): name, property of the request body.
            parent(string): parent, property of the request body.
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
                'parent':
                    parent,
                'idSeqItem':
                    id_seq_item,
                'certificateAuthenticationProfile':
                    certificate_authentication_profile,
                'breakOnStoreFail':
                    break_on_store_fail,
            }
            _payload = {
                'IdStoreSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c316d5e2fdd51bdab039ea9e2a417bd_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/idstoresequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c316d5e2fdd51bdab039ea9e2a417bd_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     break_on_store_fail=None,
                     certificate_authentication_profile=None,
                     description=None,
                     id_seq_item=None,
                     name=None,
                     parent=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_identity_sequence_by_id <#ciscoisesdk.
        api.v3_1_1.identity_sequence.
        IdentitySequence.update_identity_sequence_by_id>`_
        """
        return self.update_identity_sequence_by_id(
            id=id,
            break_on_store_fail=break_on_store_fail,
            certificate_authentication_profile=certificate_authentication_profile,
            description=description,
            id_seq_item=id_seq_item,
            name=name,
            parent=parent,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_identity_sequence_by_id(self,
                                       id,
                                       headers=None,
                                       **query_parameters):
        """This API deletes an identity sequence.

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

        e_url = ('/ers/config/idstoresequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b8258803668534d87781e995c73c23a_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_identity_sequence_by_id <#ciscoisesdk.
        api.v3_1_1.identity_sequence.
        IdentitySequence.delete_identity_sequence_by_id>`_
        """
        return self.delete_identity_sequence_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_identity_sequence(self,
                              page=None,
                              size=None,
                              headers=None,
                              **query_parameters):
        """This API allows the client to get all the identity sequences.

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

        e_url = ('/ers/config/idstoresequence')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_feb30ca768795eed82c118d009d7bcd4_v3_1_1', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_identity_sequence <#ciscoisesdk.
        api.v3_1_1.identity_sequence.
        IdentitySequence.get_identity_sequence>`_
        """
        return self.get_identity_sequence(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_identity_sequence_generator(self,
                                        page=None,
                                        size=None,
                                        headers=None,
                                        **query_parameters):
        """This API allows the client to get all the identity sequences.

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
            self.get_identity_sequence, dict(
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
        """Alias for `get_identity_sequence_generator <#ciscoisesdk.
        api.v3_1_1.identity_sequence.
        IdentitySequence.get_identity_sequence_generator>`_
        """
        yield from get_next_page(
            self.get_identity_sequence, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_identity_sequence(self,
                                 break_on_store_fail=None,
                                 certificate_authentication_profile=None,
                                 description=None,
                                 id_seq_item=None,
                                 name=None,
                                 parent=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **query_parameters):
        """This API creates an identity sequence.

        Args:
            break_on_store_fail(boolean): breakOnStoreFail, property
                of the request body.
            certificate_authentication_profile(string):
                certificateAuthenticationProfile,
                property of the request body.
            description(string): description, property of the
                request body.
            id_seq_item(list): idSeqItem, property of the request
                body (list of objects).
            name(string): name, property of the request body.
            parent(string): parent, property of the request body.
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
                'parent':
                    parent,
                'idSeqItem':
                    id_seq_item,
                'certificateAuthenticationProfile':
                    certificate_authentication_profile,
                'breakOnStoreFail':
                    break_on_store_fail,
            }
            _payload = {
                'IdStoreSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cc0a87094bf5d96af61403dfc3747db_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/idstoresequence')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_cc0a87094bf5d96af61403dfc3747db_v3_1_1', _api_response)

    def create(self,
               break_on_store_fail=None,
               certificate_authentication_profile=None,
               description=None,
               id_seq_item=None,
               name=None,
               parent=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_identity_sequence <#ciscoisesdk.
        api.v3_1_1.identity_sequence.
        IdentitySequence.create_identity_sequence>`_
        """
        return self.create_identity_sequence(
            break_on_store_fail=break_on_store_fail,
            certificate_authentication_profile=certificate_authentication_profile,
            description=description,
            id_seq_item=id_seq_item,
            name=name,
            parent=parent,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the identity sequence.

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

        e_url = ('/ers/config/idstoresequence/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dc4c840ad93e53d591ca3a39184e6dde_v3_1_1', _api_response)
