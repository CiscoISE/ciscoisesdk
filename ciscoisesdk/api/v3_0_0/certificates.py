# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Certificates API wrapper.

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
    get_next_page,
)
import urllib.parse


class Certificates(object):
    """Identity Services Engine Certificates API (version: 3.0.0).

    Wraps the Identity Services Engine Certificates
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Certificates
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Certificates, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def import_trusted_certificate(self,
                                   allow_basic_constraint_cafalse=None,
                                   allow_out_of_date_cert=None,
                                   allow_sha1_certificates=None,
                                   data=None,
                                   description=None,
                                   name=None,
                                   trust_for_certificate_based_admin_auth=None,
                                   trust_for_cisco_services_auth=None,
                                   trust_for_client_auth=None,
                                   trust_for_ise_auth=None,
                                   validate_certificate_extensions=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Purpose of the API is to add root certificate to the ISE
        truststore.

        Args:
            allow_basic_constraint_cafalse(boolean): Allow
                Certificates with Basic Constraints CA
                Field as False (required), property of
                the request body.
            allow_out_of_date_cert(boolean): Allow out of date
                certificates (required), property of the
                request body.
            allow_sha1_certificates(boolean): Allow SHA1 based
                certificates (required), property of the
                request body.
            data(string): Certificate content (required), property
                of the request body.
            description(string): Description of the certificate,
                property of the request body.
            name(string): Name of the certificate, property of the
                request body.
            trust_for_certificate_based_admin_auth(boolean): Trust
                for Certificate based Admin
                authentication, property of the request
                body.
            trust_for_cisco_services_auth(boolean): Trust for
                authentication of Cisco Services,
                property of the request body.
            trust_for_client_auth(boolean): Trust for client
                authentication and Syslog, property of
                the request body.
            trust_for_ise_auth(boolean): Trust for authentication
                within ISE, property of the request
                body.
            validate_certificate_extensions(boolean): Validate trust
                certificate extension, property of the
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'name':
                    name,
                'data':
                    data,
                'description':
                    description,
                'validateCertificateExtensions':
                    validate_certificate_extensions,
                'allowSHA1Certificates':
                    allow_sha1_certificates,
                'allowOutOfDateCert':
                    allow_out_of_date_cert,
                'allowBasicConstraintCAFalse':
                    allow_basic_constraint_cafalse,
                'trustForIseAuth':
                    trust_for_ise_auth,
                'trustForClientAuth':
                    trust_for_client_auth,
                'trustForCiscoServicesAuth':
                    trust_for_cisco_services_auth,
                'trustForCertificateBasedAdminAuth':
                    trust_for_certificate_based_admin_auth,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c8cd2f618b655d988ce626e579486596_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/trusted-certificate/import')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c8cd2f618b655d988ce626e579486596_v3_0_0', _api_response)

    def import_system_certificate(self,
                                  admin=None,
                                  allow_extended_validity=None,
                                  allow_out_of_date_cert=None,
                                  allow_replacement_of_certificates=None,
                                  allow_replacement_of_portal_group_tag=None,
                                  allow_sha1_certificates=None,
                                  allow_wild_card_certificates=None,
                                  data=None,
                                  eap=None,
                                  ims=None,
                                  name=None,
                                  password=None,
                                  portal=None,
                                  portal_group_tag=None,
                                  private_key_data=None,
                                  pxgrid=None,
                                  radius=None,
                                  saml=None,
                                  validate_certificate_extensions=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Purpose of the API is to import system certificate into ISE.

        Args:
            admin(boolean): Use certificate to authenticate the ISE
                Admin Portal, property of the request
                body.
            allow_extended_validity(boolean): Allow import of
                certificates with validity greater than
                398 days, property of the request body.
            allow_out_of_date_cert(boolean): Allow out of date
                certificates (required), property of the
                request body.
            allow_replacement_of_certificates(boolean): Allow
                Replacement of certificates (required),
                property of the request body.
            allow_replacement_of_portal_group_tag(boolean): Allow
                Replacement of Portal Group Tag
                (required), property of the request
                body.
            allow_sha1_certificates(boolean): Allow SHA1 based
                certificates (required), property of the
                request body.
            allow_wild_card_certificates(boolean): Allow Wildcard
                Certificates, property of the request
                body.
            data(string): Certificate Content (required), property
                of the request body.
            eap(boolean): Use certificate for EAP protocols that use
                SSL/TLS tunneling, property of the
                request body.
            ims(boolean): Use certificate for the ISE Messaging
                Service, property of the request body.
            name(string): Name of the certificate, property of the
                request body.
            password(string): Certificate Password (required).,
                property of the request body.
            portal(boolean): Use for portal, property of the request
                body.
            portal_group_tag(string): Set Group tag, property of the
                request body.
            private_key_data(string): Private Key data (required),
                property of the request body.
            pxgrid(boolean): Use certificate for the pxGrid
                Controller, property of the request
                body.
            radius(boolean): Use certificate for the RADSec server,
                property of the request body.
            saml(boolean): Use certificate for SAML Signing,
                property of the request body.
            validate_certificate_extensions(boolean): Validate
                Certificate Extensions, property of the
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'name':
                    name,
                'password':
                    password,
                'data':
                    data,
                'privateKeyData':
                    private_key_data,
                'portalGroupTag':
                    portal_group_tag,
                'admin':
                    admin,
                'eap':
                    eap,
                'radius':
                    radius,
                'pxgrid':
                    pxgrid,
                'saml':
                    saml,
                'portal':
                    portal,
                'ims':
                    ims,
                'allowWildCardCertificates':
                    allow_wild_card_certificates,
                'validateCertificateExtensions':
                    validate_certificate_extensions,
                'allowSHA1Certificates':
                    allow_sha1_certificates,
                'allowOutOfDateCert':
                    allow_out_of_date_cert,
                'allowReplacementOfCertificates':
                    allow_replacement_of_certificates,
                'allowReplacementOfPortalGroupTag':
                    allow_replacement_of_portal_group_tag,
                'allowExtendedValidity':
                    allow_extended_validity,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e6c7251a8508597f1b7ae61cbf953_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/system-certificate/import')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e6c7251a8508597f1b7ae61cbf953_v3_0_0', _api_response)

    def bind_csr(self,
                 admin=None,
                 allow_extended_validity=None,
                 allow_out_of_date_cert=None,
                 allow_replacement_of_certificates=None,
                 allow_replacement_of_portal_group_tag=None,
                 data=None,
                 eap=None,
                 host_name=None,
                 id=None,
                 ims=None,
                 name=None,
                 portal=None,
                 portal_group_tag=None,
                 pxgrid=None,
                 radius=None,
                 saml=None,
                 validate_certificate_extensions=None,
                 headers=None,
                 payload=None,
                 active_validation=True,
                 **query_parameters):
        """Purpose of the API is to Bind CA Signed Certificate.

        Args:
            admin(boolean): Use certificate to authenticate the ISE
                Admin Portal, property of the request
                body.
            allow_extended_validity(boolean): Allow import of
                certificates with validity greater than
                398 days, property of the request body.
            allow_out_of_date_cert(boolean): Allow out of date
                certificates (required), property of the
                request body.
            allow_replacement_of_certificates(boolean): Allow
                Replacement of certificates (required),
                property of the request body.
            allow_replacement_of_portal_group_tag(boolean): Allow
                Replacement of Portal Group Tag
                (required), property of the request
                body.
            data(string): Signed Certificate in escaped format,
                property of the request body.
            eap(boolean): Use certificate for EAP protocols that use
                SSL/TLS tunneling, property of the
                request body.
            host_name(string): Name of Host whose CSR ID has been
                provided, property of the request body.
            id(string): ID of the generated CSR, property of the
                request body.
            ims(boolean): Use certificate for the ISE Messaging
                Service, property of the request body.
            name(string): Friendly Name of the certificate, property
                of the request body.
            portal(boolean): Use for portal, property of the request
                body.
            portal_group_tag(string): Set Group tag, property of the
                request body.
            pxgrid(boolean): Use certificate for the pxGrid
                Controller, property of the request
                body.
            radius(boolean): Use certificate for the RADSec server,
                property of the request body.
            saml(boolean): Use certificate for SAML Signing,
                property of the request body.
            validate_certificate_extensions(boolean): Validate
                Certificate Extensions, property of the
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'id':
                    id,
                'name':
                    name,
                'hostName':
                    host_name,
                'data':
                    data,
                'admin':
                    admin,
                'eap':
                    eap,
                'radius':
                    radius,
                'pxgrid':
                    pxgrid,
                'ims':
                    ims,
                'portal':
                    portal,
                'saml':
                    saml,
                'portalGroupTag':
                    portal_group_tag,
                'validateCertificateExtensions':
                    validate_certificate_extensions,
                'allowOutOfDateCert':
                    allow_out_of_date_cert,
                'allowReplacementOfCertificates':
                    allow_replacement_of_certificates,
                'allowReplacementOfPortalGroupTag':
                    allow_replacement_of_portal_group_tag,
                'allowExtendedValidity':
                    allow_extended_validity,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b94d7d3f0ed5d0b938151ae2cae9fa4_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/signed-certificate/bind')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_b94d7d3f0ed5d0b938151ae2cae9fa4_v3_0_0', _api_response)

    def export_system_cert(self,
                           certificate_id=None,
                           export=None,
                           id=None,
                           password=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """Purpose of the API is to export a system certificate given a
        certificate id.

        Args:
            certificate_id(string): certificateID, property of the
                request body.
            export(string): export, property of the request body.
                Available values are 'CERTIFICATE' and
                'CERTIFICATE_WITH_PRIVATE_KEY'.
            id(string): id, property of the request body.
            password(string): password, property of the request
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
            _payload = {
                'id':
                    id,
                'certificateID':
                    certificate_id,
                'password':
                    password,
                'export':
                    export,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dbe47028859573988880de76fec0936_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/system-certificate/export')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_dbe47028859573988880de76fec0936_v3_0_0', _api_response)

    def get_all_trusted_certificates(self,
                                     filter=None,
                                     filter_type=None,
                                     page=None,
                                     size=None,
                                     sort=None,
                                     sort_by=None,
                                     headers=None,
                                     **query_parameters):
        """ This API supports Filtering, Sorting and Pagination.
        Filtering and Sorting supported on below mentioned
        attributes:      friendlyName   subject   issuedTo
        issuedBy   validFrom     Supported Date Format: yyyy-MM-
        dd HH:mm:ss   Supported Operators: EQ, NEQ, GT and LT
        expirationDate     Supported Date Format: yyyy-MM-dd
        HH:mm:ss   Supported Operators: EQ, NEQ, GT and LT
        status     Allowed values: enabled, disabled   Supported
        Operators: EQ, NEQ      .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type - asc
                or desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sort, basestring)
        check_type(sort_by, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sort':
                sort,
            'sortBy':
                sort_by,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/certs/trusted-certificate')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c654a18faf1b5571ac5ba61145d298c4_v3_0_0', _api_response)

    def get_all_trusted_certificates_generator(self,
                                               filter=None,
                                               filter_type=None,
                                               page=None,
                                               size=None,
                                               sort=None,
                                               sort_by=None,
                                               headers=None,
                                               **query_parameters):
        """ This API supports Filtering, Sorting and Pagination.
        Filtering and Sorting supported on below mentioned
        attributes:      friendlyName   subject   issuedTo
        issuedBy   validFrom     Supported Date Format: yyyy-MM-
        dd HH:mm:ss   Supported Operators: EQ, NEQ, GT and LT
        expirationDate     Supported Date Format: yyyy-MM-dd
        HH:mm:ss   Supported Operators: EQ, NEQ, GT and LT
        status     Allowed values: enabled, disabled   Supported
        Operators: EQ, NEQ      .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type - asc
                or desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
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

        yield from get_next_page(self.get_all_trusted_certificates, dict(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sort=sort,
            sort_by=sort_by,
            **query_parameters
        ), access_next_list=["nextPage", "href"])

    def get_trusted_certificate_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """Purpose of this API is to get Trust Certificate By Id.

        Args:
            id(basestring): id path parameter. The id of the trust
                certificate.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/api/v1/certs/trusted-certificate/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f8f4956d29b821fa9bbf23266_v3_0_0', _api_response)

    def update_trusted_certificate(self,
                                   id,
                                   authenticate_before_crl_received=None,
                                   automatic_crl_update=None,
                                   automatic_crl_update_period=None,
                                   automatic_crl_update_units=None,
                                   crl_distribution_url=None,
                                   crl_download_failure_retries=None,
                                   crl_download_failure_retries_units=None,
                                   description=None,
                                   download_crl=None,
                                   enable_ocs_p_validation=None,
                                   enable_server_identity_check=None,
                                   ignore_crl_expiration=None,
                                   name=None,
                                   non_automatic_crl_update_period=None,
                                   non_automatic_crl_update_units=None,
                                   reject_if_no_status_from_ocs_p=None,
                                   reject_if_unreachable_from_ocs_p=None,
                                   selected_ocs_p_service=None,
                                   status=None,
                                   trust_for_certificate_based_admin_auth=None,
                                   trust_for_cisco_services_auth=None,
                                   trust_for_client_auth=None,
                                   trust_for_ise_auth=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """Purpose of the API is to update trust certificate already
        present in ISE trust store.

        Args:
            authenticate_before_crl_received(boolean): Switch to
                enable/disable CRL Verification if CRL
                is not Received, property of the request
                body.
            automatic_crl_update(boolean): Switch to enable/disable
                automatic CRL update, property of the
                request body.
            automatic_crl_update_period(integer): Automatic CRL
                update period, property of the request
                body.
            automatic_crl_update_units(string): Unit of time for
                automatic CRL update, property of the
                request body. Available values are
                'Minutes', 'Hours', 'Days' and 'Weeks'.
            crl_distribution_url(string): CRL Distribution URL,
                property of the request body.
            crl_download_failure_retries(integer): If CRL download
                fails, wait time before retry, property
                of the request body.
            crl_download_failure_retries_units(string): Unit of time
                before retry if CRL download fails,
                property of the request body. Available
                values are 'Minutes', 'Hours', 'Days'
                and 'Weeks'.
            description(string): Description for trust certificate,
                property of the request body.
            download_crl(boolean): Switch to enable/disable download
                of CRL, property of the request body.
            enable_ocs_p_validation(boolean): Switch to
                enable/disable OCSP Validation, property
                of the request body.
            enable_server_identity_check(boolean): Switch to
                enable/disable verification if HTTPS or
                LDAP server certificate name fits the
                configured server URL, property of the
                request body.
            ignore_crl_expiration(boolean): Switch to enable/disable
                ignore CRL Expiration, property of the
                request body.
            name(string): Friendly name of the certificate, property
                of the request body.
            non_automatic_crl_update_period(integer): Non automatic
                CRL update period, property of the
                request body.
            non_automatic_crl_update_units(string): Unit of time of
                non automatic CRL update, property of
                the request body. Available values are
                'Minutes', 'Hours', 'Days' and 'Weeks'.
            reject_if_no_status_from_ocs_p(boolean): Switch to
                reject certificate if there is no status
                from OCSP, property of the request body.
            reject_if_unreachable_from_ocs_p(boolean): Switch to
                reject certificate if unreachable from
                OCSP, property of the request body.
            selected_ocs_p_service(string): Name of selected OCSP
                Service, property of the request body.
            status(string): status, property of the request body.
                Available values are 'Enabled' and
                'Disabled'.
            trust_for_certificate_based_admin_auth(boolean): Trust
                for Certificate based Admin
                authentication, property of the request
                body.
            trust_for_cisco_services_auth(boolean): Trust for
                authentication of Cisco Services,
                property of the request body.
            trust_for_client_auth(boolean): Trust for client
                authentication and Syslog, property of
                the request body.
            trust_for_ise_auth(boolean): Trust for authentication
                within ISE, property of the request
                body.
            id(basestring): id path parameter. The id of the trust
                certificate.
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
            _payload = {
                'name':
                    name,
                'status':
                    status,
                'description':
                    description,
                'enableOCSPValidation':
                    enable_ocs_p_validation,
                'selectedOCSPService':
                    selected_ocs_p_service,
                'rejectIfNoStatusFromOCSP':
                    reject_if_no_status_from_ocs_p,
                'rejectIfUnreachableFromOCSP':
                    reject_if_unreachable_from_ocs_p,
                'downloadCRL':
                    download_crl,
                'crlDistributionUrl':
                    crl_distribution_url,
                'automaticCRLUpdate':
                    automatic_crl_update,
                'automaticCRLUpdatePeriod':
                    automatic_crl_update_period,
                'automaticCRLUpdateUnits':
                    automatic_crl_update_units,
                'nonAutomaticCRLUpdatePeriod':
                    non_automatic_crl_update_period,
                'nonAutomaticCRLUpdateUnits':
                    non_automatic_crl_update_units,
                'crlDownloadFailureRetries':
                    crl_download_failure_retries,
                'crlDownloadFailureRetriesUnits':
                    crl_download_failure_retries_units,
                'enableServerIdentityCheck':
                    enable_server_identity_check,
                'authenticateBeforeCRLReceived':
                    authenticate_before_crl_received,
                'ignoreCRLExpiration':
                    ignore_crl_expiration,
                'trustForIseAuth':
                    trust_for_ise_auth,
                'trustForClientAuth':
                    trust_for_client_auth,
                'trustForCiscoServicesAuth':
                    trust_for_cisco_services_auth,
                'trustForCertificateBasedAdminAuth':
                    trust_for_certificate_based_admin_auth,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cb625d5ad0ad76b93282f5818a_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/trusted-certificate/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_cb625d5ad0ad76b93282f5818a_v3_0_0', _api_response)

    def delete_trusted_certificate_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """Purpose of the API is to delete Trusted Certificate by ID.

        Args:
            id(basestring): id path parameter. The ID of the Trusted
                Certificate to be deleted.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/api/v1/certs/trusted-certificate/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c578ef80918b5d038024d126cd6e3b8d_v3_0_0', _api_response)

    def get_all_system_certificates(self,
                                    host_name,
                                    filter=None,
                                    filter_type=None,
                                    page=None,
                                    size=None,
                                    sort=None,
                                    sort_by=None,
                                    headers=None,
                                    **query_parameters):
        """ This API supports Filtering, Sorting and Pagination.
        Filtering and Sorting supported on below mentioned
        attributes:      friendlyName   issuedTo   issuedBy
        validFrom     Supported Date Format: yyyy-MM-dd HH:mm:ss
        Supported Operators: EQ, NEQ, GT and LT
        expirationDate     Supported Date Format: yyyy-MM-dd
        HH:mm:ss   Supported Operators: EQ, NEQ, GT and LT
        .

        Args:
            host_name(basestring): hostName path parameter. Name of
                the host of which system certificates
                should be returned.
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type - asc
                or desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sort, basestring)
        check_type(sort_by, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)
        check_type(host_name, basestring,
                   may_be_none=False)

        _params = {
            'page':
                page,
            'size':
                size,
            'sort':
                sort,
            'sortBy':
                sort_by,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
        }

        e_url = ('/api/v1/certs/system-certificate/{hostName}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a56f5c5f739a83e8806da16be5_v3_0_0', _api_response)

    def get_all_system_certificates_generator(self,
                                              host_name,
                                              filter=None,
                                              filter_type=None,
                                              page=None,
                                              size=None,
                                              sort=None,
                                              sort_by=None,
                                              headers=None,
                                              **query_parameters):
        """ This API supports Filtering, Sorting and Pagination.
        Filtering and Sorting supported on below mentioned
        attributes:      friendlyName   issuedTo   issuedBy
        validFrom     Supported Date Format: yyyy-MM-dd HH:mm:ss
        Supported Operators: EQ, NEQ, GT and LT
        expirationDate     Supported Date Format: yyyy-MM-dd
        HH:mm:ss   Supported Operators: EQ, NEQ, GT and LT
        .

        Args:
            host_name(basestring): hostName path parameter. Name of
                the host of which system certificates
                should be returned.
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type - asc
                or desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
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

        yield from get_next_page(self.get_all_system_certificates, dict(
            host_name=host_name,
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sort=sort,
            sort_by=sort_by,
            **query_parameters
        ), access_next_list=["nextPage", "href"])

    def get_system_certificate_by_id(self,
                                     host_name,
                                     id,
                                     headers=None,
                                     **query_parameters):
        """Purpose of this API is to get system certificate of a particular
        node by Id.

        Args:
            host_name(basestring): hostName path parameter. Name of
                the host of which system certificates
                should be returned.
            id(basestring): id path parameter. The id of the system
                certificate.
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
        check_type(host_name, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'id': id,
        }

        e_url = ('/api/v1/certs/system-certificate/{hostName}/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f36e90115b05416a71506061fed7e5c_v3_0_0', _api_response)

    def delete_system_certificate_by_id(self,
                                        host_name,
                                        id,
                                        headers=None,
                                        **query_parameters):
        """Purpose of the API is to delete System Certificate by ID and
        hostname.

        Args:
            host_name(basestring): hostName path parameter. Name of
                the host from which the System
                Certificate needs to be deleted.
            id(basestring): id path parameter. The ID of the System
                Certificate to be deleted.
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
        check_type(host_name, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'id': id,
        }

        e_url = ('/api/v1/certs/system-certificate/{hostName}/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dc2eec65ad680a3c5de47cd87c8_v3_0_0', _api_response)

    def update_system_certificate(self,
                                  host_name,
                                  id,
                                  admin=None,
                                  allow_replacement_of_portal_group_tag=None,
                                  description=None,
                                  eap=None,
                                  expiration_ttl_period=None,
                                  expiration_ttl_units=None,
                                  ims=None,
                                  name=None,
                                  portal=None,
                                  portal_group_tag=None,
                                  pxgrid=None,
                                  radius=None,
                                  renew_self_signed_certificate=None,
                                  saml=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """Purpose of the API is to update data for existing system
        certificate.

        Args:
            admin(boolean): Use certificate to authenticate the ISE
                Admin Portal, property of the request
                body.
            allow_replacement_of_portal_group_tag(boolean): Allow
                Replacement of Portal Group Tag
                (required), property of the request
                body.
            description(string): Description of System Certificate,
                property of the request body.
            eap(boolean): Use certificate for EAP protocols that use
                SSL/TLS tunneling, property of the
                request body.
            expiration_ttl_period(integer): expirationTTLPeriod,
                property of the request body.
            expiration_ttl_units(string): expirationTTLUnits,
                property of the request body. Available
                values are 'days', 'weeks', 'months' and
                'years'.
            ims(boolean): Use certificate for the ISE Messaging
                Service, property of the request body.
            name(string): Name of the certificate, property of the
                request body.
            portal(boolean): Use for portal, property of the request
                body.
            portal_group_tag(string): Set Group tag, property of the
                request body.
            pxgrid(boolean): Use certificate for the pxGrid
                Controller, property of the request
                body.
            radius(boolean): Use certificate for the RADSec server,
                property of the request body.
            renew_self_signed_certificate(boolean): Renew Self
                Signed Certificate, property of the
                request body.
            saml(boolean): Use certificate for SAML Signing,
                property of the request body.
            id(basestring): id path parameter. The ID of the System
                Certificate to be updated.
            host_name(basestring): hostName path parameter. Name of
                Host whose certificate needs to be
                updated.
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
        check_type(id, basestring,
                   may_be_none=False)
        check_type(host_name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
            'hostName': host_name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'name':
                    name,
                'description':
                    description,
                'admin':
                    admin,
                'eap':
                    eap,
                'radius':
                    radius,
                'pxgrid':
                    pxgrid,
                'saml':
                    saml,
                'portal':
                    portal,
                'ims':
                    ims,
                'portalGroupTag':
                    portal_group_tag,
                'allowReplacementOfPortalGroupTag':
                    allow_replacement_of_portal_group_tag,
                'renewSelfSignedCertificate':
                    renew_self_signed_certificate,
                'expirationTTLPeriod':
                    expiration_ttl_period,
                'expirationTTLUnits':
                    expiration_ttl_units,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fb9c22ad9a5eddb590c85abdab460b_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/system-certificate/{hostName}/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_fb9c22ad9a5eddb590c85abdab460b_v3_0_0', _api_response)

    def get_csr(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sort=None,
                sort_by=None,
                headers=None,
                **query_parameters):
        """ This API supports Filtering, Sorting and Pagination.
        Filtering and Sorting supported on below mentioned
        attributes:      friendlyName   subject   timeStamp
        Supported Date Format: yyyy-MM-dd HH:mm:ss.SSS
        Supported Operators: EQ, NEQ, GT and LT      .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type - asc
                or desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
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
            pass

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sort, basestring)
        check_type(sort_by, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sort':
                sort,
            'sortBy':
                sort_by,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/certs/certificate-signing-request')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eeef18d70b159f788b717e301dd3643_v3_0_0', _api_response)

    def get_csr_generator(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sort=None,
                          sort_by=None,
                          headers=None,
                          **query_parameters):
        """ This API supports Filtering, Sorting and Pagination.
        Filtering and Sorting supported on below mentioned
        attributes:      friendlyName   subject   timeStamp
        Supported Date Format: yyyy-MM-dd HH:mm:ss.SSS
        Supported Operators: EQ, NEQ, GT and LT      .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sort(basestring): sort query parameter. sort type - asc
                or desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
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

        yield from get_next_page(self.get_csr, dict(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sort=sort,
            sort_by=sort_by,
            **query_parameters
        ), access_next_list=["nextPage", "href"])

    def generate_csr(self,
                     allow_wild_card_cert=None,
                     certificate_policies=None,
                     digest_type=None,
                     hostnames=None,
                     key_length=None,
                     key_type=None,
                     portal_group_tag=None,
                     san_dir=None,
                     san_dns=None,
                     san_ip=None,
                     san_uri=None,
                     subject_city=None,
                     subject_common_name=None,
                     subject_country=None,
                     subject_org=None,
                     subject_org_unit=None,
                     subject_state=None,
                     used_for=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Purpose of this API is to generate a Certificate Signing Request
        (CSR).

        Args:
            allow_wild_card_cert(boolean): allowWildCardCert,
                property of the request body.
            certificate_policies(string): certificatePolicies,
                property of the request body.
            digest_type(string): digestType, property of the request
                body. Available values are 'SHA-256',
                'SHA-384' and 'SHA-512'.
            hostnames(list): hostnames, property of the request body
                (list of strings).
            key_length(string): keyLength, property of the request
                body. Available values are '512',
                '1024', '2048' and '4096'.
            key_type(string): keyType, property of the request body.
                Available values are 'RSA' and 'ECDSA'.
            portal_group_tag(string): portalGroupTag, property of
                the request body.
            sanDNS(list): sanDNS, property of the request body (list
                of strings).
            sanDir(list): sanDir, property of the request body (list
                of strings).
            sanIP(list): sanIP, property of the request body (list
                of strings).
            sanURI(list): sanURI, property of the request body (list
                of strings).
            subject_city(string): subjectCity, property of the
                request body.
            subject_common_name(string): subjectCommonName, property
                of the request body.
            subject_country(string): subjectCountry, property of the
                request body.
            subject_org(string): subjectOrg, property of the request
                body.
            subject_org_unit(string): subjectOrgUnit, property of
                the request body.
            subject_state(string): subjectState, property of the
                request body.
            used_for(string): usedFor, property of the request body.
                Available values are 'MULTI-USE',
                'ADMIN', 'EAP-AUTH', 'DTLS-AUTH',
                'PORTAL', 'PXGRID', 'SAML' and 'IMS'.
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'hostnames':
                    hostnames,
                'allowWildCardCert':
                    allow_wild_card_cert,
                'subjectCommonName':
                    subject_common_name,
                'subjectOrgUnit':
                    subject_org_unit,
                'subjectOrg':
                    subject_org,
                'subjectCity':
                    subject_city,
                'subjectState':
                    subject_state,
                'subjectCountry':
                    subject_country,
                'sanDNS':
                    san_dns,
                'sanIP':
                    san_ip,
                'sanURI':
                    san_uri,
                'sanDir':
                    san_dir,
                'keyLength':
                    key_length,
                'keyType':
                    key_type,
                'digestType':
                    digest_type,
                'usedFor':
                    used_for,
                'certificatePolicies':
                    certificate_policies,
                'portalGroupTag':
                    portal_group_tag,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e39868ea7aec5efcaaf55009699eda5d_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/certificate-signing-request')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e39868ea7aec5efcaaf55009699eda5d_v3_0_0', _api_response)

    def get_csr_by_id(self,
                      host_name,
                      id,
                      headers=None,
                      **query_parameters):
        """Purpose of the API is to get Certificate Signing Request(CSR) by
        ID.

        Args:
            host_name(basestring): hostName path parameter. Name of
                the host of which CSR's should be
                returned.
            id(basestring): id path parameter. The ID of the
                Certificate Signing Request returned.
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
        check_type(host_name, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'id': id,
        }

        e_url = ('/api/v1/certs/certificate-signing-'
                 + 'request/{hostName}/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b8104a50fc565ae9a756d6d0152e0e5b_v3_0_0', _api_response)

    def delete_csr_by_id(self,
                         host_name,
                         id,
                         headers=None,
                         **query_parameters):
        """Purpose of the API is to delete Certificate Signing Request(CSR)
        by ID.

        Args:
            host_name(basestring): hostName path parameter. Name of
                the host of which CSR's should be
                deleted.
            id(basestring): id path parameter. The ID of the
                Certificate Signing Request to be
                deleted.
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
        check_type(host_name, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'id': id,
        }

        e_url = ('/api/v1/certs/certificate-signing-'
                 + 'request/{hostName}/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bf792ec664fa5202beb776556908b0c1_v3_0_0', _api_response)

    def generate_intermediate_ca_csr(self,
                                     headers=None,
                                     **query_parameters):
        """Purpose of this API is to generate a intermediate CA Certificate
        Signing Request (CSR).

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
            pass

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

        e_url = ('/api/v1/certs/certificate-signing-request/intermediate-'
                 + 'ca')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bf95f099207a5b6599e04c47c22789c0_v3_0_0', _api_response)

    def export_csr(self,
                   hostname,
                   id,
                   headers=None,
                   **query_parameters):
        """The response of this API carries a CSR corresponding to the
        requested ID.

        Args:
            hostname(basestring): hostname path parameter. The
                hostname to which the CSR belongs.
            id(basestring): id path parameter. The ID of the CSR to
                be exported.
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
        check_type(hostname, basestring,
                   may_be_none=False)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostname': hostname,
            'id': id,
        }

        e_url = ('/api/v1/certs/certificate-signing-'
                 + 'request/export/{hostname}/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ec26ec11d92356a594a6efa55ccb9be7_v3_0_0', _api_response)

    def regenerate_ise_root_ca(self,
                               remove_existing_ise_intermediate_csr=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """This API will initiate regeneration of ISE root CA certificate
        chain. Response contains id which can be used to track
        the status.

        Args:
            remove_existing_ise_intermediate_csr(boolean): Setting
                this attribute to true will remove
                existing ISE Intermediate CSR, property
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'removeExistingISEIntermediateCSR':
                    remove_existing_ise_intermediate_csr,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e6d1b224e058288a8c4d70be72c9a6_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/ise-root-ca/regenerate')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e6d1b224e058288a8c4d70be72c9a6_v3_0_0', _api_response)

    def renew_certificate(self,
                          cert_type=None,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **query_parameters):
        """This API will initiate regeneration of certificates. Response
        contains id which can be used to track the status.

        Args:
            cert_type(string): certType, property of the request
                body. Available values are 'OCSP' and
                'IMS'.
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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'certType':
                    cert_type,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c288192f954309b4b35aa612ff226_v3_0_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/renew-certificate')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c288192f954309b4b35aa612ff226_v3_0_0', _api_response)

    def export_trusted_certificate(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """The response of this API carries a trusted certificate file
        mapped to the requested id.

        Args:
            id(basestring): id path parameter. The ID of the Trusted
                Certificate to be exported.
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
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/api/v1/certs/trusted-certificate/export/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b62a711ce705542b5d1d92b7d3ca431_v3_0_0', _api_response)
