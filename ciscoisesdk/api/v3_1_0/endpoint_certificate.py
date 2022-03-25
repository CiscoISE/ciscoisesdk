# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine EndpointCertificate API wrapper.

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


class EndpointCertificate(object):
    """Identity Services Engine EndpointCertificate API (version: 3.1.0).

    Wraps the Identity Services Engine EndpointCertificate
    API and exposes the API as native Python
    methods that return native Python objects.

    | Endpoint Certificate API allows the client to create endpoint certificates signed by the Cisco ISE Internal CA. This API can takes in certificate request details, create a RSA key pair, create a certificate and return the resulting key pair and certificate as a ZIP file. ZIP files are returned as an octet stream.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.0                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | **Attribute**      | **Type**    | **Required** | **Description**                                                                                                                                                                                                 | **Example Values**        |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | name               | String      | Yes          | Resource Name                                                                                                                                                                                                   |                           |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | id                 | String      | No           | Resource UUID, mandatory for update                                                                                                                                                                             |                           |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | description        | String      | No           |                                                                                                                                                                                                                 |                           |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | certTemplateName   | String      | Yes          | Name of an Internal CA template                                                                                                                                                                                 | Certificate_Template_Name |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | format             | Enum        | Yes          | Allowed values: PKCS12, PKCS12_CHAIN, PKCS8, PKCS8_CHAIN                                                                                                                                                        | PKCS8                     |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | password           | String      | Yes          | Protects the private key. Must have more than 8 characters, less than 15 characters, at least one upper case letter, at least one lower case letter, at least one digit, and can only contain [A-Z][a-z][0-9]_# | Password_123              |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | certificateRequest | Map         | Yes          | Key value map. Must have CN and SAN entries                                                                                                                                                                     |                           |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | - CN               | String      | Yes          | Matches the requester's User Name, unless the Requester is an ERS Admin. ERS Admins are allowed to create requests for any CN                                                                                   | userName [or] machineName |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
    | - SAN              | String      | Yes          | Valid MAC Address, delimited by '-'                                                                                                                                                                             | 11-22-33-44-55-66         |
    +--------------------+-------------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new EndpointCertificate
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(EndpointCertificate, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_endpoint_certificate(self,
                                    cert_template_name=None,
                                    certificate_request=None,
                                    format=None,
                                    password=None,
                                    dirpath=None,
                                    save_file=None,
                                    filename=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """This API allows the client to create an endpoint certificate.

        Args:
            cert_template_name(string): Name of an Internal CA
                template, property of the request body.
            certificate_request(object): Key value map. Must have CN
                and SAN entries, property of the request
                body.
            format(string): Allowed values: PKCS12, PKCS12_CHAIN,
                PKCS8, PKCS8_CHAIN, property of the
                request body.
            password(string): Protects the private key. Must have
                more than 8 characters, less than 15
                characters, at least one upper case
                letter, at least one lower case letter,
                at least one digit, and can only contain
                [A-Z][a-z][0-9]_#, property of the
                request body.
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
                'certTemplateName':
                    cert_template_name,
                'format':
                    format,
                'password':
                    password,
                'certificateRequest':
                    certificate_request,
            }
            _payload = {
                'ERSEndPointCert': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e27d5df9cbe5b29a7e16bb7c877a4ce_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/endpointcert/certRequest')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              stream=True, dirpath=dirpath, save_file=save_file, filename=filename,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              stream=True, dirpath=dirpath, save_file=save_file, filename=filename,
                                              **request_params)

        return self._object_factory('bpm_e27d5df9cbe5b29a7e16bb7c877a4ce_v3_1_0', _api_response)

    def create(self,
               cert_template_name=None,
               certificate_request=None,
               format=None,
               password=None,
               dirpath=None,
               save_file=None,
               filename=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_endpoint_certificate <#ciscoisesdk.
        api.v3_1_0.endpoint_certificate.
        EndpointCertificate.create_endpoint_certificate>`_
        """
        return self.create_endpoint_certificate(
            cert_template_name=cert_template_name,
            certificate_request=certificate_request,
            format=format,
            password=password,
            dirpath=dirpath,
            save_file=save_file,
            filename=filename,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the endpoint certificate.

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

        e_url = ('/ers/config/endpointcert/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c5c84028d8f5c078d8ab37553812d39_v3_1_0', _api_response)
