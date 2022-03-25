# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine CertificateProfile API wrapper.

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


class CertificateProfile(object):
    """Identity Services Engine CertificateProfile API (version: 3.1.0).

    Wraps the Identity Services Engine CertificateProfile
    API and exposes the API as native Python
    methods that return native Python objects.

    | The certificate profile API allows the client to add, search and perform actions on the certificate profiles.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+---+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |   |
    +----------------+----------------------+-----------------------+---------------------------+---+
    | 0              | 1.0                  | 2.4                   | Initial Cisco ISE Version |   |
    +----------------+----------------------+-----------------------+---------------------------+---+

    |

    **Resource Definition**

    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | **Attribute**             | **Type**  | **Required** | **Description**                                                                                                   | **Default Values**  | **Example Values**                   |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | name                      | String    | Yes          | Resource Name                                                                                                     |                     | Certificate_Profile                  |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | id                        | String    | No           | Resource UUID                                                                                                     |                     | f9269682-dcaf-11e3-ad0a-5bdcd2d9fd69 |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | description               | String    | No           |                                                                                                                   |                     |                                      |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | allowedAsUserName         | Boolean   | No           | To be set true or false                                                                                           | false               |                                      |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | externalIdentityStoreName | String    | No           | Referred IDStore name for the Certificate Profile or [not applicable] in case no identity store is chosen         | [not applicable]    | [not applicable]                     |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | certificateAttributeName  | ENUM      | No           | Attribute name of the Certificate Profile - used only when CERTIFICATE is chosen in usernameFrom. Allowed values: | SUBJECT_COMMON_NAME |                                      |
    |                           |           |              | - SUBJECT_COMMON_NAME                                                                                             |                     |                                      |
    |                           |           |              | - SUBJECT_ALTERNATIVE_NAME                                                                                        |                     |                                      |
    |                           |           |              | - SUBJECT_SERIAL_NUMBER                                                                                           |                     |                                      |
    |                           |           |              | - SUBJECT                                                                                                         |                     |                                      |
    |                           |           |              | - SUBJECT_ALTERNATIVE_NAME_OTHER_NAME                                                                             |                     |                                      |
    |                           |           |              | - SUBJECT_ALTERNATIVE_NAME_EMAIL                                                                                  |                     |                                      |
    |                           |           |              | - SUBJECT_ALTERNATIVE_NAME_DNS.                                                                                   |                     |                                      |
    |                           |           |              | - Additional internal value ALL_SUBJECT_AND_ALTERNATIVE_NAMES is used automatically when usernameFrom=UPN         |                     |                                      |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | matchMode                 | ENUM      | No           | Match mode of the Certificate Profile. Allowed values: NEVER, RESOLVE_IDENTITY_AMBIGUITY,  BINARY_COMPARISON      | NEVER               |                                      |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+
    | usernameFrom              | ENUM      | No           | The attribute in the certificate where the user name should be taken from.                                        | CERTIFICATE         |                                      |
    +---------------------------+-----------+--------------+-------------------------------------------------------------------------------------------------------------------+---------------------+--------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new CertificateProfile
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(CertificateProfile, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_certificate_profile_by_name(self,
                                        name,
                                        headers=None,
                                        **query_parameters):
        """This API allows the client to get a certificate profile by name.

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

        e_url = ('/ers/config/certificateprofile/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e7884eb9c548698cdc54e033f35f4_v3_1_0', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_certificate_profile_by_name <#ciscoisesdk.
        api.v3_1_0.certificate_profile.
        CertificateProfile.get_certificate_profile_by_name>`_
        """
        return self.get_certificate_profile_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_certificate_profile_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """This API allows the client to get a certificate profile by ID.

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

        e_url = ('/ers/config/certificateprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d24a3f485ff758d099b1e4713f18f1c1_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_certificate_profile_by_id <#ciscoisesdk.
        api.v3_1_0.certificate_profile.
        CertificateProfile.get_certificate_profile_by_id>`_
        """
        return self.get_certificate_profile_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_certificate_profile_by_id(self,
                                         id,
                                         allowed_as_user_name=None,
                                         certificate_attribute_name=None,
                                         description=None,
                                         external_identity_store_name=None,
                                         match_mode=None,
                                         name=None,
                                         username_from=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **query_parameters):
        """This API allows the client to update a certificate profile.

        Args:
            allowed_as_user_name(boolean): allowedAsUserName,
                property of the request body.
            certificate_attribute_name(string): Attribute name of
                the Certificate Profile used only when
                CERTIFICATE is chosen in usernameFrom.
                Allowed values: SUBJECT_COMMON_NAME
                SUBJECT_ALTERNATIVE_NAME
                SUBJECT_SERIAL_NUMBER SUBJECT
                SUBJECT_ALTERNATIVE_NAME_OTHER_NAME
                SUBJECT_ALTERNATIVE_NAME_EMAIL
                SUBJECT_ALTERNATIVE_NAME_DNS. Additional
                internal value
                ALL_SUBJECT_AND_ALTERNATIVE_NAMES is
                used automatically when
                usernameFrom=UPN, property of the
                request body.
            description(string): description, property of the
                request body.
            external_identity_store_name(string): Referred IDStore
                name for the Certificate Profile or [not
                applicable] in case no identity store is
                chosen, property of the request body.
            id(string): id, property of the request body.
            match_mode(string): Match mode of the Certificate
                Profile. Allowed values: NEVER
                RESOLVE_IDENTITY_AMBIGUITY
                BINARY_COMPARISON, property of the
                request body.
            name(string): name, property of the request body.
            username_from(string): The attribute in the certificate
                where the user name should be taken
                from. Allowed values: CERTIFICATE (for a
                specific attribute as defined in
                certificateAttributeName) UPN (for using
                any Subject or Alternative Name
                Attributes in the Certificate an option
                only in AD), property of the request
                body.
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
                'externalIdentityStoreName':
                    external_identity_store_name,
                'certificateAttributeName':
                    certificate_attribute_name,
                'allowedAsUserName':
                    allowed_as_user_name,
                'matchMode':
                    match_mode,
                'usernameFrom':
                    username_from,
            }
            _payload = {
                'CertificateProfile': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e09287aba99c56a6a9171b7e3a635a43_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/certificateprofile/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e09287aba99c56a6a9171b7e3a635a43_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     allowed_as_user_name=None,
                     certificate_attribute_name=None,
                     description=None,
                     external_identity_store_name=None,
                     match_mode=None,
                     name=None,
                     username_from=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_certificate_profile_by_id <#ciscoisesdk.
        api.v3_1_0.certificate_profile.
        CertificateProfile.update_certificate_profile_by_id>`_
        """
        return self.update_certificate_profile_by_id(
            id=id,
            allowed_as_user_name=allowed_as_user_name,
            certificate_attribute_name=certificate_attribute_name,
            description=description,
            external_identity_store_name=external_identity_store_name,
            match_mode=match_mode,
            name=name,
            username_from=username_from,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_certificate_profile(self,
                                page=None,
                                size=None,
                                headers=None,
                                **query_parameters):
        """This API allows the client to get all the certificate profiles.

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

        e_url = ('/ers/config/certificateprofile')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_be38700993b5f70acfdc8e44f5558d8_v3_1_0', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_certificate_profile <#ciscoisesdk.
        api.v3_1_0.certificate_profile.
        CertificateProfile.get_certificate_profile>`_
        """
        return self.get_certificate_profile(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_certificate_profile_generator(self,
                                          page=None,
                                          size=None,
                                          headers=None,
                                          **query_parameters):
        """This API allows the client to get all the certificate profiles.

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
            self.get_certificate_profile, dict(
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
        """Alias for `get_certificate_profile_generator <#ciscoisesdk.
        api.v3_1_0.certificate_profile.
        CertificateProfile.get_certificate_profile_generator>`_
        """
        yield from get_next_page(
            self.get_certificate_profile, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_certificate_profile(self,
                                   allowed_as_user_name=None,
                                   certificate_attribute_name=None,
                                   description=None,
                                   external_identity_store_name=None,
                                   id=None,
                                   match_mode=None,
                                   name=None,
                                   username_from=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """This API allows the client to create a certificate profile.

        Args:
            allowed_as_user_name(boolean): allowedAsUserName,
                property of the request body.
            certificate_attribute_name(string): Attribute name of
                the Certificate Profile used only when
                CERTIFICATE is chosen in usernameFrom.
                Allowed values: SUBJECT_COMMON_NAME
                SUBJECT_ALTERNATIVE_NAME
                SUBJECT_SERIAL_NUMBER SUBJECT
                SUBJECT_ALTERNATIVE_NAME_OTHER_NAME
                SUBJECT_ALTERNATIVE_NAME_EMAIL
                SUBJECT_ALTERNATIVE_NAME_DNS. Additional
                internal value
                ALL_SUBJECT_AND_ALTERNATIVE_NAMES is
                used automatically when
                usernameFrom=UPN, property of the
                request body.
            description(string): description, property of the
                request body.
            external_identity_store_name(string): Referred IDStore
                name for the Certificate Profile or [not
                applicable] in case no identity store is
                chosen, property of the request body.
            id(string): id, property of the request body.
            match_mode(string): Match mode of the Certificate
                Profile. Allowed values: NEVER
                RESOLVE_IDENTITY_AMBIGUITY
                BINARY_COMPARISON, property of the
                request body.
            name(string): name, property of the request body.
            username_from(string): The attribute in the certificate
                where the user name should be taken
                from. Allowed values: CERTIFICATE (for a
                specific attribute as defined in
                certificateAttributeName) UPN (for using
                any Subject or Alternative Name
                Attributes in the Certificate an option
                only in AD), property of the request
                body.
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
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'externalIdentityStoreName':
                    external_identity_store_name,
                'certificateAttributeName':
                    certificate_attribute_name,
                'allowedAsUserName':
                    allowed_as_user_name,
                'matchMode':
                    match_mode,
                'usernameFrom':
                    username_from,
            }
            _payload = {
                'CertificateProfile': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_9f955525b0b38a57a3bed311_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/certificateprofile')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_9f955525b0b38a57a3bed311_v3_1_0', _api_response)

    def create(self,
               allowed_as_user_name=None,
               certificate_attribute_name=None,
               description=None,
               external_identity_store_name=None,
               id=None,
               match_mode=None,
               name=None,
               username_from=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_certificate_profile <#ciscoisesdk.
        api.v3_1_0.certificate_profile.
        CertificateProfile.create_certificate_profile>`_
        """
        return self.create_certificate_profile(
            allowed_as_user_name=allowed_as_user_name,
            certificate_attribute_name=certificate_attribute_name,
            description=description,
            external_identity_store_name=external_identity_store_name,
            id=id,
            match_mode=match_mode,
            name=name,
            username_from=username_from,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the certificate profile.

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

        e_url = ('/ers/config/certificateprofile/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e00be3b97b85829bef60c09eaa922ac_v3_1_0', _api_response)
