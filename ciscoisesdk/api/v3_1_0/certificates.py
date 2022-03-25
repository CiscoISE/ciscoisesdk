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


class Certificates(object):
    """Identity Services Engine Certificates API (version: 3.1.0).

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

    def get_csrs(self,
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
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring, list, set, tuple): filter query
                parameter.        Simple filtering
                should be available through the filter
                query string parameter. The structure of
                a filter is a triplet of field operator
                and value separated with dots. More than
                one filter can be sent. The logical
                operator common to ALL filter criteria
                will be by default AND, and can be
                changed by using the  "filterType=or"
                query string parameter. Each resource
                Data model description should specify if
                an attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
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

        return self._object_factory('bpm_eeef18d70b159f788b717e301dd3643_v3_1_0', _api_response)

    def get_csrs_generator(self,
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
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring, list, set, tuple): filter query
                parameter.        Simple filtering
                should be available through the filter
                query string parameter. The structure of
                a filter is a triplet of field operator
                and value separated with dots. More than
                one filter can be sent. The logical
                operator common to ALL filter criteria
                will be by default AND, and can be
                changed by using the  "filterType=or"
                query string parameter. Each resource
                Data model description should specify if
                an attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
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
            self.get_csrs, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sort=sort,
                sort_by=sort_by,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

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
        """    Generate a certificate signing request for Multi-Use, Admin,
        EAP Authentication, RADIUS DTLS, PxGrid, SAML, Portal
        and IMS Services.   Following Parameters are present in
        POST request body         PARAMETER   DESCRIPTION
        EXAMPLE           hostnames   List of ise node hostnames
        for which CSRs should be generated   [ise-host1, ise-
        host2]       allowWildCardCert   Allow use of WildCards
        in certificates   false       keyLength   Length of the
        Key used for CSR generation (required)   512
        keyType   Type of key used for CSR generation either RSA
        or ECDSA(required)   RSA       digestType   Hash
        algorithm used for signing CSR(required)   SHA-256
        usedFor   Certificate Usage(required)   MULTI-USE
        subjectCommonName   Certificate common
        name(CN)(required)   $FQDN$       subjectOrgUnit
        Certificate organizational unit(OU)   Engineering
        subjectOrg   Certificate organization (O)   Cisco
        subjectCity   Certificate city or locality (L)   San
        Jose     subjectState   Certificate state (ST)
        California     subjectCountry   Certificate country ( C)
        US       sanDNS   Array of SAN(Subject Alternative Name)
        DNS entries(optional)   [ise.example.com]     sanIP
        Array of SAN IP entries(optional)   [1.1.1.1]     sanURI
        Array of SAN URI entries(optional)   [https://1.1.1.1]
        sanDir   Array of SAN DIR entries(optional)
        [CN=AAA,DC=COM,C=IL]       portalGroupTag   Portal Group
        Tag when using certificate for PORTAL service   Default
        Portal Certificate Group         NOTE:  For
        allowWildCardCert to be false, the below mentioned
        parameter is mandatory:  hostnames    When Certificate
        is selected to be used for Portal Service, the below
        mentioned parameter is mandatory:  portalGroupTag    .

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
                body. Available values are '1024',
                '2048', '4096' and '512'.
            key_type(string): keyType, property of the request body.
                Available values are 'ECDSA' and 'RSA'.
            portal_group_tag(string): portalGroupTag, property of
                the request body.
            san_dns(list): sanDNS, property of the request body
                (list of strings).
            san_dir(list): sanDir, property of the request body
                (list of strings).
            san_ip(list): sanIP, property of the request body (list
                of strings).
            san_uri(list): sanURI, property of the request body
                (list of strings).
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
                Available values are 'ADMIN', 'DTLS-
                AUTH', 'EAP-AUTH', 'IMS', 'MULTI-USE',
                'PORTAL', 'PXGRID' and 'SAML'.
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
                'allowWildCardCert':
                    allow_wild_card_cert,
                'certificatePolicies':
                    certificate_policies,
                'digestType':
                    digest_type,
                'hostnames':
                    hostnames,
                'keyLength':
                    key_length,
                'keyType':
                    key_type,
                'portalGroupTag':
                    portal_group_tag,
                'sanDNS':
                    san_dns,
                'sanDir':
                    san_dir,
                'sanIP':
                    san_ip,
                'sanURI':
                    san_uri,
                'subjectCity':
                    subject_city,
                'subjectCommonName':
                    subject_common_name,
                'subjectCountry':
                    subject_country,
                'subjectOrg':
                    subject_org,
                'subjectOrgUnit':
                    subject_org_unit,
                'subjectState':
                    subject_state,
                'usedFor':
                    used_for,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e39868ea7aec5efcaaf55009699eda5d_v3_1_0')\
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

        return self._object_factory('bpm_e39868ea7aec5efcaaf55009699eda5d_v3_1_0', _api_response)

    def export_csr(self,
                   hostname,
                   id,
                   dirpath=None,
                   save_file=None,
                   filename=None,
                   headers=None,
                   **query_parameters):
        """The response of this API carries a CSR corresponding to the
        requested ID.

        Args:
            hostname(basestring): hostname path parameter. The
                hostname to which the CSR belongs.
            id(basestring): id path parameter. The ID of the CSR to
                be exported.
            dirpath(basestring): Directory absolute path. Defaults to
                os.getcwd().
            save_file(bool): Enable or disable automatic file creation of
                raw response.
            filename(basestring): The filename used to save the download
                file.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            DownloadResponse: The DownloadResponse wrapper. Wraps the urllib3.response.HTTPResponse. For more
            information check the `urlib3 documentation <https://urllib3.readthedocs.io/en/latest/reference/urllib3.response.html>`_

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
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
                                              headers=_headers,
                                              stream=True, dirpath=dirpath, save_file=save_file, filename=filename)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              stream=True, dirpath=dirpath, save_file=save_file, filename=filename)

        return self._object_factory('bpm_ec26ec11d92356a594a6efa55ccb9be7_v3_1_0', _api_response)

    def generate_intermediate_ca_csr(self,
                                     headers=None,
                                     **query_parameters):
        """CSR Generation for Intermediate Certificates.

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

        return self._object_factory('bpm_bf95f099207a5b6599e04c47c22789c0_v3_1_0', _api_response)

    def get_csr_by_id(self,
                      host_name,
                      id,
                      headers=None,
                      **query_parameters):
        """This API displays details of a Certificate Signing Request of a
        particular node based on a given HostName and ID.

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

        return self._object_factory('bpm_b8104a50fc565ae9a756d6d0152e0e5b_v3_1_0', _api_response)

    def delete_csr_by_id(self,
                         host_name,
                         id,
                         headers=None,
                         **query_parameters):
        """This API deletes a Certificate Signing Request of a particular
        node based on a given HostName and ID.

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

        return self._object_factory('bpm_bf792ec664fa5202beb776556908b0c1_v3_1_0', _api_response)

    def regenerate_ise_root_ca(self,
                               remove_existing_ise_intermediate_csr=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **query_parameters):
        """This API will initiate regeneration of ISE root CA certificate
        chain. Response contains id which can be used to track
        the status.    Setting
        "removeExistingISEIntermediateCSR" to true will remove
        existing ISE Intermediate CSR.

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
            self._request_validator('jsd_e6d1b224e058288a8c4d70be72c9a6_v3_1_0')\
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

        return self._object_factory('bpm_e6d1b224e058288a8c4d70be72c9a6_v3_1_0', _api_response)

    def renew_certificates(self,
                           cert_type=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """This API will initiate regeneration of certificates. Response
        contains id which can be used to track the status.

        Args:
            cert_type(string): certType, property of the request
                body. Available values are 'IMS' and
                'OCSP'.
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
            self._request_validator('jsd_c288192f954309b4b35aa612ff226_v3_1_0')\
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

        return self._object_factory('bpm_c288192f954309b4b35aa612ff226_v3_1_0', _api_response)

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
        """    Bind CA Signed Certificate.   NOTE:  This API requires an
        existing Certificate Signing Request, and the root
        certificate must already be trusted.   NOTE:  The
        certificate may have a validity period longer than 398
        days. It may be untrusted by many browsers.   NOTE:
        Request Parameters accepting True and False as input can
        be replaced by 1 and 0 respectively.    Following
        Parameters are used in POST body         PARAMETER
        DESCRIPTION   EXAMPLE           name   Friendly name of
        the certificate.   Signed Certificate       data
        Plain-text contents of the certificate file. Every space
        needs to be replaced with newline escape sequence (\n)
        (required).   awk 'NF {sub(/\r/, ""); printf
        "%s\\n",$0;}' <<your .pem file>>
        allowExtendedValidity   Allow the certificates greater
        than validity of 398 days (required)   false
        allowOutOfDateCert   Allow out of date certificates
        (required)   false       allowReplacementOfCertificates
        Allow Replacement of certificates (required)   false
        allowReplacementOfPortalGroupTag   Allow Replacement of
        Portal Group Tag (required)   false     admin   Use
        certificate to authenticate the ISE Admin Portal   false
        eap   Use certificate for EAP protocols that use SSL/TLS
        tunneling   false       radius   Use certificate for
        RADSec server   false       pxgrid   Use certificate for
        the pxGrid Controller   false       ims   Use
        certificate for the ISE Messaging Service   false
        saml   Use certificate for SAML Signing   false
        portal   Use certificate for portal   false
        portalGroupTag   Portal Group Tag for using certificate
        with portal role   Default Portal Certificate Group
        validateCertificateExtensions   Validate Certificate
        Extensions   false           Following Roles can be used
        in any combinations         ROLE   DEFAULT   WARNING
        Admin   False   Enabling Admin role for this certificate
        will cause an application server restart on the selected
        node. Note:  Make sure required Certificate Chain is
        imported under Trusted Certificates       EAP
        Authentication   False   Only one system certificate can
        be used for EAP. Assigning EAP to this certificate will
        remove the assignment from another certificate. Note:
        Make sure required Certificate Chain is imported under
        Trusted Certificates       RADIUS DTLS   False   Only
        one system certificate can be used for DTLS. Assigning
        DTLS to this certificate will remove the assignment from
        another certificate. Note:  Make sure required
        Certificate Chain is imported under Trusted Certificates
        SAML   False   SAML cannot be used with other Usage.
        Enabling SAML will uncheck all other Usage. Note:  Make
        sure required Certificate Chain is imported under
        Trusted Certificates        .

        Args:
            admin(boolean): Use certificate to authenticate the ISE
                Admin Portal, property of the request
                body.
            allow_extended_validity(boolean): Allow import of
                certificates with validity greater than
                398 days (required), property of the
                request body.
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
            data(string): Signed Certificate data (required),
                property of the request body.
            eap(boolean): Use certificate for EAP protocols that use
                SSL/TLS tunneling, property of the
                request body.
            host_name(string): Name of Host whose CSR ID has been
                provided (required), property of the
                request body.
            id(string): ID of the generated CSR (required), property
                of the request body.
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
                'admin':
                    admin,
                'allowExtendedValidity':
                    allow_extended_validity,
                'allowOutOfDateCert':
                    allow_out_of_date_cert,
                'allowReplacementOfCertificates':
                    allow_replacement_of_certificates,
                'allowReplacementOfPortalGroupTag':
                    allow_replacement_of_portal_group_tag,
                'data':
                    data,
                'eap':
                    eap,
                'hostName':
                    host_name,
                'id':
                    id,
                'ims':
                    ims,
                'name':
                    name,
                'portal':
                    portal,
                'portalGroupTag':
                    portal_group_tag,
                'pxgrid':
                    pxgrid,
                'radius':
                    radius,
                'saml':
                    saml,
                'validateCertificateExtensions':
                    validate_certificate_extensions,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b94d7d3f0ed5d0b938151ae2cae9fa4_v3_1_0')\
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

        return self._object_factory('bpm_b94d7d3f0ed5d0b938151ae2cae9fa4_v3_1_0', _api_response)

    def export_system_certificate(self,
                                  export=None,
                                  id=None,
                                  password=None,
                                  dirpath=None,
                                  save_file=None,
                                  filename=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """    Export System Certificate.   Following Parameters are used
        in POST body         PARAMETER   DESCRIPTION   EXAMPLE
        id   ID of a System Certificate(required)   <
        SYSTEM_CERT_ID >       export    One of the below option
        is required    "CERTIFICATE" : Export only Certificate
        without Private Key   "CERTIFICATE_WITH_PRIVATE_KEY" :
        Export both Certificate and Private Key(
        "certificatePassword"  is required)
        CERTIFICATE_WITH_PRIVATE_KEY       password
        Certificate Password (required if  "export" :
        CERTIFICATE_WITH_PRIVATE_KEY )  Password Constraints:
        Alphanumeric   Minimum of 8 Characters   Maximum of 100
        Characters       Passw***           NOTE:  The response
        of this API carries a ZIP file containing the
        certificate and private key if  "export" :
        "CERTIFICATE_WITH_PRIVATE_KEY"  in the request. If
        "export" : "CERTIFICATE"  in request body, the response
        carries a ZIP file containing only the certificate.
        WARNING:  Exporting a private key is not a secure
        operation. It could lead to possible exposure of the
        private key.     .

        Args:
            export(string): export, property of the request body.
                Available values are 'CERTIFICATE' and
                'CERTIFICATE_WITH_PRIVATE_KEY'.
            id(string): id, property of the request body.
            password(string): password, property of the request
                body.
            dirpath(basestring): Directory absolute path. Defaults to
                os.getcwd().
            save_file(bool): Enable or disable automatic file creation of
                raw response.
            filename(basestring): The filename used to save the download
                file.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            DownloadResponse: The DownloadResponse wrapper. Wraps the urllib3.response.HTTPResponse. For more
            information check the `urlib3 documentation <https://urllib3.readthedocs.io/en/latest/reference/urllib3.response.html>`_

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
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
                'export':
                    export,
                'id':
                    id,
                'password':
                    password,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dbe47028859573988880de76fec0936_v3_1_0')\
                .validate(_payload)

        e_url = ('/api/v1/certs/system-certificate/export')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               stream=True, dirpath=dirpath, save_file=save_file, filename=filename,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               stream=True, dirpath=dirpath, save_file=save_file, filename=filename,
                                               **request_params)

        return self._object_factory('bpm_dbe47028859573988880de76fec0936_v3_1_0', _api_response)

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
                                  portal_tag_transfer_for_same_subject=None,
                                  private_key_data=None,
                                  pxgrid=None,
                                  radius=None,
                                  role_transfer_for_same_subject=None,
                                  saml=None,
                                  validate_certificate_extensions=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """    Import an X509 certificate as a system certificate.   NOTE:
        The certificate may have a validity period longer than
        398 days. It may be untrusted by many browsers.   NOTE:
        Request Parameters accepting True and False as input can
        be replaced by 1 and 0 respectively.    Following
        Parameters are used in POST body         PARAMETER
        DESCRIPTION   EXAMPLE           name   Friendly name of
        the certificate.   System Certificate       password
        Password of the certificate to be imported (required).
        Passw***       data   Plain-text contents of the
        certificate file. Every space needs to be replaced with
        newline escape sequence (\n) (required).   awk 'NF
        {sub(/\r/, ""); printf "%s\\n",$0;}' <<your .pem file>>
        privateKeyData   Plain-text contents of the private key
        file. Every space needs to be replaced with newline
        escape sequence (\n) (required).   awk 'NF {sub(/\r/,
        ""); printf "%s\\n",$0;}' <<your .pem file>>
        allowOutOfDateCert   Allow out of date certificates
        (required)   false       allowSHA1Certificates   Allow
        SHA1 based certificates (required)   false
        allowExtendedValidity   Allow the certificates greater
        than validity of 398 days (required)   false
        roleTransferForSameSubject   Allow the transfer of roles
        to certificates with same subject   false
        portalTagTransferForSameSubject   Acquire the group tag
        of the matching certificate   false       admin   Use
        certificate to authenticate the ISE Admin Portal   false
        eap   Use certificate for EAP protocols that use SSL/TLS
        tunneling   false       radius   Use certificate for
        RADSec server   false       pxgrid   Use certificate for
        the pxGrid Controller   false       ims   Use
        certificate for the ISE Messaging Service   false
        saml   Use certificate for SAML Signing   false
        portal   Use certificate for portal   false
        portalGroupTag   Portal Group Tag for using certificate
        with portal role   Default Portal Certificate Group
        allowReplacementOfPortalGroupTag   Allow Replacement of
        Portal Group Tag (required)   false
        allowWildCardCertificates   Allow use of WildCards in
        certificates   false       validateCertificateExtensions
        Validate Certificate Extensions   false
        Following Roles can be used in any combinations
        ROLE   DEFAULT   WARNING           Admin   False
        Enabling Admin role for this certificate will cause an
        application server restart on the selected node. Note:
        Make sure required Certificate Chain is imported under
        Trusted Certificates       EAP Authentication   False
        Only one system certificate can be used for EAP.
        Assigning EAP to this certificate will remove the
        assignment from another certificate. Note:  Make sure
        required Certificate Chain is imported under Trusted
        Certificates       RADIUS DTLS   False   Only one system
        certificate can be used for DTLS. Assigning DTLS to this
        certificate will remove the assignment from another
        certificate. Note:  Make sure required Certificate Chain
        is imported under Trusted Certificates       SAML
        False   SAML cannot be used with other Usage. Enabling
        SAML will uncheck all other Usage. Note:  Make sure
        required Certificate Chain is imported under Trusted
        Certificates        .

        Args:
            admin(boolean): Use certificate to authenticate the ISE
                Admin Portal, property of the request
                body.
            allow_extended_validity(boolean): Allow import of
                certificates with validity greater than
                398 days (required), property of the
                request body.
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
            portal_tag_transfer_for_same_subject(boolean): Allow
                overwriting the portal tag from matching
                certificate of same subject, property of
                the request body.
            private_key_data(string): Private Key data (required),
                property of the request body.
            pxgrid(boolean): Use certificate for the pxGrid
                Controller, property of the request
                body.
            radius(boolean): Use certificate for the RADSec server,
                property of the request body.
            role_transfer_for_same_subject(boolean): Allow transfer
                of roles for certificate with matching
                subject , property of the request body.
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
                'admin':
                    admin,
                'allowExtendedValidity':
                    allow_extended_validity,
                'allowOutOfDateCert':
                    allow_out_of_date_cert,
                'allowReplacementOfCertificates':
                    allow_replacement_of_certificates,
                'allowReplacementOfPortalGroupTag':
                    allow_replacement_of_portal_group_tag,
                'allowSHA1Certificates':
                    allow_sha1_certificates,
                'allowWildCardCertificates':
                    allow_wild_card_certificates,
                'data':
                    data,
                'eap':
                    eap,
                'ims':
                    ims,
                'name':
                    name,
                'password':
                    password,
                'portal':
                    portal,
                'portalGroupTag':
                    portal_group_tag,
                'portalTagTransferForSameSubject':
                    portal_tag_transfer_for_same_subject,
                'privateKeyData':
                    private_key_data,
                'pxgrid':
                    pxgrid,
                'radius':
                    radius,
                'roleTransferForSameSubject':
                    role_transfer_for_same_subject,
                'saml':
                    saml,
                'validateCertificateExtensions':
                    validate_certificate_extensions,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e6c7251a8508597f1b7ae61cbf953_v3_1_0')\
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

        return self._object_factory('bpm_e6c7251a8508597f1b7ae61cbf953_v3_1_0', _api_response)

    def get_system_certificates(self,
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
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring, list, set, tuple): filter query
                parameter.        Simple filtering
                should be available through the filter
                query string parameter. The structure of
                a filter is a triplet of field operator
                and value separated with dots. More than
                one filter can be sent. The logical
                operator common to ALL filter criteria
                will be by default AND, and can be
                changed by using the  "filterType=or"
                query string parameter. Each resource
                Data model description should specify if
                an attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
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

        return self._object_factory('bpm_a56f5c5f739a83e8806da16be5_v3_1_0', _api_response)

    def get_system_certificates_generator(self,
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
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring, list, set, tuple): filter query
                parameter.        Simple filtering
                should be available through the filter
                query string parameter. The structure of
                a filter is a triplet of field operator
                and value separated with dots. More than
                one filter can be sent. The logical
                operator common to ALL filter criteria
                will be by default AND, and can be
                changed by using the  "filterType=or"
                query string parameter. Each resource
                Data model description should specify if
                an attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
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
            self.get_system_certificates, dict(
                host_name=host_name,
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sort=sort,
                sort_by=sort_by,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def get_system_certificate_by_id(self,
                                     host_name,
                                     id,
                                     headers=None,
                                     **query_parameters):
        """This API displays details of a System Certificate of a
        particular node based on a given HostName and ID.

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

        return self._object_factory('bpm_f36e90115b05416a71506061fed7e5c_v3_1_0', _api_response)

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
                                  portal_tag_transfer_for_same_subject=None,
                                  pxgrid=None,
                                  radius=None,
                                  renew_self_signed_certificate=None,
                                  role_transfer_for_same_subject=None,
                                  saml=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """    Update a System Certificate.   NOTE:  Renewing a certificate
        will cause an application server restart on the selected
        node.    NOTE:  Request Parameters accepting True and
        False as input can be replaced by 1 and 0 respectively.
        Following Parameters are used in POST body
        PARAMETER   DESCRIPTION   EXAMPLE           name
        Friendly name of the certificate.   System Certificate
        description  Description of the Certificate  Default
        Description      admin   Use certificate to authenticate
        the ISE Admin Portal   false       eap   Use certificate
        for EAP protocols that use SSL/TLS tunneling   false
        radius   Use certificate for RADSec server   false
        pxgrid   Use certificate for the pxGrid Controller
        false       ims   Use certificate for the ISE Messaging
        Service   false       saml   Use certificate for SAML
        Signing   false       portal   Use certificate for
        portal   false       portalGroupTag   Portal Group Tag
        for using certificate with portal role   Default Portal
        Certificate Group       allowReplacementOfPortalGroupTag
        Allow Replacement of Portal Group Tag (required)   false
        roleTransferForSameSubject   Allow the transfer of roles
        to certificates with same subject   false
        portalTagTransferForSameSubject   Acquire the group tag
        of the matching certificate   false
        renewSelfSignedCertificate   Renew Self Signed
        Certificate   false       expirationTTLPeriod
        Expiration Period   365       expirationTTLUnits
        Expiration Units in one of the below formats    days /
        weeks / months / years       days           Following
        Roles can be used in any combinations         ROLE
        DEFAULT   WARNING           Admin   False   Enabling
        Admin role for this certificate will cause an
        application server restart on the selected node. Note:
        Make sure required Certificate Chain is imported under
        Trusted Certificates       EAP Authentication   False
        Only one system certificate can be used for EAP.
        Assigning EAP to this certificate will remove the
        assignment from another certificate. Note:  Make sure
        required Certificate Chain is imported under Trusted
        Certificates       RADIUS DTLS   False   Only one system
        certificate can be used for DTLS. Assigning DTLS to this
        certificate will remove the assignment from another
        certificate. Note:  Make sure required Certificate Chain
        is imported under Trusted Certificates       SAML
        False   SAML cannot be used with other Usage. Enabling
        SAML will uncheck all other Usage. Note:  Make sure
        required Certificate Chain is imported under Trusted
        Certificates        .

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
                values are 'days', 'months', 'weeks' and
                'years'.
            ims(boolean): Use certificate for the ISE Messaging
                Service, property of the request body.
            name(string): Name of the certificate, property of the
                request body.
            portal(boolean): Use for portal, property of the request
                body.
            portal_group_tag(string): Set Group tag, property of the
                request body.
            portal_tag_transfer_for_same_subject(boolean): Allow
                overwriting the portal tag from matching
                certificate of same subject, property of
                the request body.
            pxgrid(boolean): Use certificate for the pxGrid
                Controller, property of the request
                body.
            radius(boolean): Use certificate for the RADSec server,
                property of the request body.
            renew_self_signed_certificate(boolean): Renew Self
                Signed Certificate, property of the
                request body.
            role_transfer_for_same_subject(boolean): Allow transfer
                of roles for certificate with matching
                subject , property of the request body.
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
                'admin':
                    admin,
                'allowReplacementOfPortalGroupTag':
                    allow_replacement_of_portal_group_tag,
                'description':
                    description,
                'eap':
                    eap,
                'expirationTTLPeriod':
                    expiration_ttl_period,
                'expirationTTLUnits':
                    expiration_ttl_units,
                'ims':
                    ims,
                'name':
                    name,
                'portal':
                    portal,
                'portalGroupTag':
                    portal_group_tag,
                'portalTagTransferForSameSubject':
                    portal_tag_transfer_for_same_subject,
                'pxgrid':
                    pxgrid,
                'radius':
                    radius,
                'renewSelfSignedCertificate':
                    renew_self_signed_certificate,
                'roleTransferForSameSubject':
                    role_transfer_for_same_subject,
                'saml':
                    saml,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fb9c22ad9a5eddb590c85abdab460b_v3_1_0')\
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

        return self._object_factory('bpm_fb9c22ad9a5eddb590c85abdab460b_v3_1_0', _api_response)

    def delete_system_certificate_by_id(self,
                                        host_name,
                                        id,
                                        headers=None,
                                        **query_parameters):
        """This API deletes a System Certificate of a particular node based
        on a given HostName and ID.

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

        return self._object_factory('bpm_dc2eec65ad680a3c5de47cd87c8_v3_1_0', _api_response)

    def get_trusted_certificates(self,
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
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring, list, set, tuple): filter query
                parameter.        Simple filtering
                should be available through the filter
                query string parameter. The structure of
                a filter is a triplet of field operator
                and value separated with dots. More than
                one filter can be sent. The logical
                operator common to ALL filter criteria
                will be by default AND, and can be
                changed by using the  "filterType=or"
                query string parameter. Each resource
                Data model description should specify if
                an attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
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

        return self._object_factory('bpm_c654a18faf1b5571ac5ba61145d298c4_v3_1_0', _api_response)

    def get_trusted_certificates_generator(self,
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
            sort(basestring): sort query parameter. sort type asc or
                desc.
            sort_by(basestring): sortBy query parameter. sort column
                by which objects needs to be sorted.
            filter(basestring, list, set, tuple): filter query
                parameter.        Simple filtering
                should be available through the filter
                query string parameter. The structure of
                a filter is a triplet of field operator
                and value separated with dots. More than
                one filter can be sent. The logical
                operator common to ALL filter criteria
                will be by default AND, and can be
                changed by using the  "filterType=or"
                query string parameter. Each resource
                Data model description should specify if
                an attribute is a filtered field.
                OPERATOR   DESCRIPTION           EQ
                Equals       NEQ   Not Equals       GT
                Greater Than       LT   Less Then
                STARTSW   Starts With       NSTARTSW
                Not Starts With       ENDSW   Ends With
                NENDSW   Not Ends With       CONTAINS
                Contains       NCONTAINS   Not Contains
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
            self.get_trusted_certificates, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sort=sort,
                sort_by=sort_by,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["nextPage", "href"],
            access_resource_list=["response"])

    def export_trusted_certificate(self,
                                   id,
                                   dirpath=None,
                                   save_file=None,
                                   filename=None,
                                   headers=None,
                                   **query_parameters):
        """The response of this API carries a trusted certificate file
        mapped to the requested id.

        Args:
            id(basestring): id path parameter. The ID of the Trusted
                Certificate to be exported.
            dirpath(basestring): Directory absolute path. Defaults to
                os.getcwd().
            save_file(bool): Enable or disable automatic file creation of
                raw response.
            filename(basestring): The filename used to save the download
                file.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            DownloadResponse: The DownloadResponse wrapper. Wraps the urllib3.response.HTTPResponse. For more
            information check the `urlib3 documentation <https://urllib3.readthedocs.io/en/latest/reference/urllib3.response.html>`_

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
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
                                              headers=_headers,
                                              stream=True, dirpath=dirpath, save_file=save_file, filename=filename)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              stream=True, dirpath=dirpath, save_file=save_file, filename=filename)

        return self._object_factory('bpm_b62a711ce705542b5d1d92b7d3ca431_v3_1_0', _api_response)

    def import_trust_certificate(self,
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
        """    Import an X509 certificate as a trust certificate.   NOTE:
        Request Parameters accepting True and False as input can
        be replaced by 1 and 0 respectively.    Following
        Parameters are used in POST body         PARAMETER
        DESCRIPTION   EXAMPLE           name   Friendly name of
        the certificate   Trust Certificate       description
        Description of the certificate   Passw***       data
        Plain-text contents of the certificate file. Every space
        needs to be replaced with newline escape sequence (\n)
        (required).   awk 'NF {sub(/\r/, ""); printf
        "%s\\n",$0;}' <<your .pem file>>
        allowOutOfDateCert   Allow out of date certificates
        (required)   false       allowSHA1Certificates   Allow
        SHA1 based certificates (required)   false
        trustForIseAuth   Trust for authentication within ISE
        false       trustForClientAuth   Trust for client
        authentication and Syslog   false
        trustForCertificateBasedAdminAuth   Trust for
        Certificate based Admin authentication   false
        trustForCiscoServicesAuth   Trust for authentication of
        Cisco Services   false
        validateCertificateExtensions   Validate extensions for
        trust certificate   false         NOTE:  If name is not
        set, a default name of the following format will be
        generated:   common-name#issuer#nnnnn       where
        "nnnnn"  is a unique number. You can always change the
        friendly name later by editing the certificate.
        You must choose how this certificate will be trusted in
        ISE. The objective here is to distinguish between
        certificates that are used for trust within an ISE
        deployment and public certificates that are used to
        trust Cisco services. Typically, you will not want to
        use a given certificate for both purposes.
        Trusted For   Usage           Authentication within ISE
        Use  "trustForIseAuth":true  if the certificate is used
        for trust within ISE, such as for secure communication
        between ISE nodes       Client authentication and Syslog
        Use  "trustForClientAuth":true  if the certificate is to
        be used for authentication of endpoints that contact ISE
        over the EAP protocol. Also check this box if
        certificate is used to trust a Syslog server. Make sure
        to have keyCertSign bit asserted under KeyUsage
        extension for this certificate.  Note:  "" can be set
        true only if the "trustForIseAuth" has been set true.
        Certificate based admin authentication   Use
        "trustForCertificateBasedAdminAuth":true  if the
        certificate is used for trust within ISE, such as for
        secure communication between ISE nodes  Note:
        "trustForCertificateBasedAdminAuth" can be set true only
        if "trustForIseAuth" and "trustForClientAuth" are true.
        Authentication of Cisco Services    Use
        "trustForCiscoServicesAuth":true  if the certificate is
        to be used for trusting external Cisco services, such as
        Feed Service.        .

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
                'allowBasicConstraintCAFalse':
                    allow_basic_constraint_cafalse,
                'allowOutOfDateCert':
                    allow_out_of_date_cert,
                'allowSHA1Certificates':
                    allow_sha1_certificates,
                'data':
                    data,
                'description':
                    description,
                'name':
                    name,
                'trustForCertificateBasedAdminAuth':
                    trust_for_certificate_based_admin_auth,
                'trustForCiscoServicesAuth':
                    trust_for_cisco_services_auth,
                'trustForClientAuth':
                    trust_for_client_auth,
                'trustForIseAuth':
                    trust_for_ise_auth,
                'validateCertificateExtensions':
                    validate_certificate_extensions,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c8cd2f618b655d988ce626e579486596_v3_1_0')\
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

        return self._object_factory('bpm_c8cd2f618b655d988ce626e579486596_v3_1_0', _api_response)

    def get_trusted_certificate_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """This API can displays details of a Trust Certificate based on a
        given ID.

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

        return self._object_factory('bpm_f8f4956d29b821fa9bbf23266_v3_1_0', _api_response)

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
                                   enable_ocsp_validation=None,
                                   enable_server_identity_check=None,
                                   ignore_crl_expiration=None,
                                   name=None,
                                   non_automatic_crl_update_period=None,
                                   non_automatic_crl_update_units=None,
                                   reject_if_no_status_from_ocs_p=None,
                                   reject_if_unreachable_from_ocs_p=None,
                                   selected_ocsp_service=None,
                                   status=None,
                                   trust_for_certificate_based_admin_auth=None,
                                   trust_for_cisco_services_auth=None,
                                   trust_for_client_auth=None,
                                   trust_for_ise_auth=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """    Update a trusted certificate present in ISE trust store.
        Following Parameters are used in PUT request body
        PARAMETER   DESCRIPTION   EXAMPLE           name
        Friendly name of the certificate(required)   Trust
        Certificate       status   Status of the certificate
        Enabled       description   Description of the
        certificate   Certificate for secure connection to
        cisco.com       trustForIseAuth   Trust for
        authentication within ISE   false
        trustForClientAuth   Trust for client authentication and
        Syslog   false       trustForCertificateBasedAdminAuth
        Trust for Certificate based Admin authentication   false
        trustForCiscoServicesAuth   Trust for authentication of
        Cisco Services   false       enableOCSPValidation
        Switch to enable/disable OCSP Validation   false
        selectedOCSPService   Name of selected OCSP Service
        INTERNAL_OCSP_SERVICE       rejectIfNoStatusFromOCSP
        Switch to reject certificate if there is no status from
        OCSP   false       rejectIfUnreachableFromOCSP   Switch
        to reject certificate if unreachable from OCSP   false
        downloadCRL   Switch to enable/disable download of CRL
        false       crlDistributionUrl   Certificate Revocation
        List Distribution URL         automaticCRLUpdate
        Switch to enable/disable automatic CRL update   false
        automaticCRLUpdatePeriod   Automatic CRL update period
        5       automaticCRLUpdateUnits   Unit of time for
        automatic CRL update   Minutes
        nonAutomaticCRLUpdatePeriod   Non automatic CRL update
        period   1       nonAutomaticCRLUpdateUnits   Unit of
        time of non automatic CRL update   Hours
        crlDownloadFailureRetries   If CRL download fails, wait
        time before retry   10
        crlDownloadFailureRetriesUnits   Unit of time before
        retry if CRL download fails   Minutes
        enableServerIdentityCheck   Switch to enable/disable
        verification if HTTPS or LDAP server certificate name
        fits the configured server URL   false
        authenticateBeforeCRLReceived   Switch to enable/disable
        CRL Verification if CRL is not Received   false
        ignoreCRLExpiration   Switch to enable/disable ignore
        CRL Expiration   false                 Trusted For
        Usage           Authentication within ISE   Use
        "trustForIseAuth":true  if the certificate is used for
        trust within ISE, such as for secure communication
        between ISE nodes       Client authentication and Syslog
        Use  "trustForClientAuth":true  if the certificate is to
        be used for authentication of endpoints that contact ISE
        over the EAP protocol. Also check this box if
        certificate is used to trust a Syslog server. Make sure
        to have keyCertSign bit asserted under KeyUsage
        extension for this certificate.  Note:
        "trustForClientAuth" can be set true only if the
        "trustForIseAuth" has been set true.       Certificate
        based admin authentication   Use
        "trustForCertificateBasedAdminAuth":true  if the
        certificate is used for trust within ISE, such as for
        secure communication between ISE nodes  Note:
        "trustForCertificateBasedAdminAuth" can be set true only
        if "trustForIseAuth" and "trustForClientAuth" are true.
        Authentication of Cisco Services    Use
        "trustForCiscoServicesAuth":true  if the certificate is
        to be used for trusting external Cisco services, such as
        Feed Service.               OCSP Configuration   Usage
        Validation against OCSP service   Use
        "enableOCSPValidation":true  to validate the certificate
        against OCSP service mentioned in the field
        selectedOCSPService       OCSP Service name   Use
        "selectedOCSPService":"Name of OCSP Service"  Name of
        the OCSP service against which the certificate should be
        validated  Note:  "selectedOCSPService" value will on be
        used if "enableOCSPValidation" has been set true.
        Reject the request if OCSP returns UNKNOWN status   Use
        "rejectIfNoStatusFromOCSP":true  to reject the
        certificate if the OCSP service returns UNKNOWN status
        Note:  "rejectIfNoStatusFromOCSP:true" can be used only
        if "enableOCSPValidation" has been set true.
        Reject the request if OCSP Responder is unreachable
        Use  "rejectIfUnreachableFromOCSP":true  to reject the
        certificate if the OCSP service is unreachable.  Note:
        "rejectIfUnreachableFromOCSP:true" can be used only if
        "enableOCSPValidation" has been set true.
        Certificate Revocation List Configuration   Usage
        Validation against CRL   Use  "downloadCRL":true  to
        validate the certificate against CRL downloaded from URL
        mentioned in the field  crlDistributionUrl       CRL
        distribution url   Use  "crlDistributionUrl"  to specify
        the URL from where the CRL should be downloaded  Note:
        "crlDistributionUrl" value will only be used if
        "downloadCRL" has been set true.       Retrieve CRL time
        Use  "automaticCRLUpdate":true and
        automaticCRLUpdatePeriod, automaticCRLUpdatePeriod  to
        set the time before which CRL is automatically retrieved
        prior to expiration Use  "nonAutomaticCRLUpdatePeriod,
        nonAutomaticCRLUpdateUnits  to set the time period for
        CRL retrieval in loop.   Note:  All the above fields can
        be used only if "downloadCRL" has been set true.
        If download fails   Use  "crlDownloadFailureRetries" and
        "crlDownloadFailureRetriesUnits"  to set retry time
        period if CRL download fails  Note:
        "crlDownloadFailureRetries" and
        "crlDownloadFailureRetriesUnits" can be used only if
        "downloadCRL" has been set true.       Enable Server
        Identity Check   Use  "enableServerIdentityCheck":true
        to verify that HTTPS or LDAPS server certificate name
        fits the configured server URL  Note:
        "enableServerIdentityCheck:true" can be used only if
        "downloadCRL" has been set true.       Bypass CRL
        Verification if CRL is not Received   Use
        "authenticateBeforeCRLReceived":true  to bypass CRL
        Verification if CRL is not Received  Note:
        "authenticateBeforeCRLReceived:true" can be used only if
        "downloadCRL" has been set true.       Ignore that CRL
        is not yet valid or has expired    Use
        "ignoreCRLExpiration":true  to ignore if CRL is not yet
        valid or expired  Note:  "ignoreCRLExpiration:true" can
        be used only if "downloadCRL" has been set true.
        Note:  boolean properties accept integers values as
        well, with 0 considered as false and other values being
        considered as true   .

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
                'Days', 'Hours', 'Minutes' and 'Weeks'.
            crl_distribution_url(string): CRL Distribution URL,
                property of the request body.
            crl_download_failure_retries(integer): If CRL download
                fails, wait time before retry, property
                of the request body.
            crl_download_failure_retries_units(string): Unit of time
                before retry if CRL download fails,
                property of the request body. Available
                values are 'Days', 'Hours', 'Minutes'
                and 'Weeks'.
            description(string): Description for trust certificate,
                property of the request body.
            download_crl(boolean): Switch to enable/disable download
                of CRL, property of the request body.
            enable_ocsp_validation(boolean): Switch to
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
                'Days', 'Hours', 'Minutes' and 'Weeks'.
            reject_if_no_status_from_ocs_p(boolean): Switch to
                reject certificate if there is no status
                from OCSP, property of the request body.
            reject_if_unreachable_from_ocs_p(boolean): Switch to
                reject certificate if unreachable from
                OCSP, property of the request body.
            selected_ocsp_service(string): Name of selected OCSP
                Service, property of the request body.
            status(string): status, property of the request body.
                Available values are 'Disabled' and
                'Enabled'.
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
                'authenticateBeforeCRLReceived':
                    authenticate_before_crl_received,
                'automaticCRLUpdate':
                    automatic_crl_update,
                'automaticCRLUpdatePeriod':
                    automatic_crl_update_period,
                'automaticCRLUpdateUnits':
                    automatic_crl_update_units,
                'crlDistributionUrl':
                    crl_distribution_url,
                'crlDownloadFailureRetries':
                    crl_download_failure_retries,
                'crlDownloadFailureRetriesUnits':
                    crl_download_failure_retries_units,
                'description':
                    description,
                'downloadCRL':
                    download_crl,
                'enableOCSPValidation':
                    enable_ocsp_validation,
                'enableServerIdentityCheck':
                    enable_server_identity_check,
                'ignoreCRLExpiration':
                    ignore_crl_expiration,
                'name':
                    name,
                'nonAutomaticCRLUpdatePeriod':
                    non_automatic_crl_update_period,
                'nonAutomaticCRLUpdateUnits':
                    non_automatic_crl_update_units,
                'rejectIfNoStatusFromOCSP':
                    reject_if_no_status_from_ocs_p,
                'rejectIfUnreachableFromOCSP':
                    reject_if_unreachable_from_ocs_p,
                'selectedOCSPService':
                    selected_ocsp_service,
                'status':
                    status,
                'trustForCertificateBasedAdminAuth':
                    trust_for_certificate_based_admin_auth,
                'trustForCiscoServicesAuth':
                    trust_for_cisco_services_auth,
                'trustForClientAuth':
                    trust_for_client_auth,
                'trustForIseAuth':
                    trust_for_ise_auth,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_cb625d5ad0ad76b93282f5818a_v3_1_0')\
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

        return self._object_factory('bpm_cb625d5ad0ad76b93282f5818a_v3_1_0', _api_response)

    def delete_trusted_certificate_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """This API deletes a Trust Certificate from Trusted Certificate
        Store based on a given ID.

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

        return self._object_factory('bpm_c578ef80918b5d038024d126cd6e3b8d_v3_1_0', _api_response)
