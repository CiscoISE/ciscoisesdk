# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SystemCertificate API wrapper.

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


class SystemCertificate(object):
    """Identity Services Engine SystemCertificate API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine SystemCertificate
    API and exposes the API as native Python
    methods that return native Python objects.

    | System Certificate API provides the ability to create certificates like SAML, pxGrid.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+
    | 0              | 1.0                  | 3.0                   | Initial Cisco ISE Version |   |   |
    +----------------+----------------------+-----------------------+---------------------------+---+---+

    |

    **Resource Definition**

    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | **Attribute**               | **Type** | **Required** | **Description**                     | **Example Values**               |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | name                        | String   | Yes          | Resource Name                       |                                  |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | id                          | String   | No           | Resource UUID, mandatory for update |                                  |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | description                 | String   | No           |                                     | Support Bundle Status api        |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | nodeId                      | String   | Yes          | NodeId of Cisco ISE application     | ISE-01                           |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | localCertStub               | List     | Yes          | Inputs for certificate creation     |                                  |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - subjectStub               | List     | No           | Subject data of certificate         |                                  |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    |   - commonName              | String   | No           | Common Name                         | $FQDN$                           |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    |   - organizationalUnitName  | String   | No           | Organizational Unit Name            | Cisco-SAMLCert                   |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    |   - organizationName        | String   | No           | Organizational Name                 | Cisco                            |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    |   - localityName            | String   | No           | Locality Name                       | City                             |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    |   - stateOrProvinceName     | String   | No           | State or Province Name              | State                            |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    |   - countryName             | String   | No           | Country Name                        | Country                          |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - keyType                   | String   | Yes          | Key Type                            | RSA OR ECDSA                     |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - keyLength                 | String   | Yes          | Key Length                          | 512 OR 1024 OR 2048 OR 4096      |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - digest                    | String   | Yes          | Digest                              | SHA-256 OR SHA-384 OR SHA-512    |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - expirationTTL             | Integer  | Yes          | Expiration Time to Live (TTL)       | 2                                |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - selectedExpirationTTLUnit | String   | Yes          | Selected Expiration TTL Unit        | days OR weeks OR months OR years |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - groupTagDD                | String   | No           | Group Tag DD                        | add-group-tag                    |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - samlCertificate           | String   | No           | SAML Certificate                    | on OR off                        |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - xgridCertificate          | String   | No           | XGrid Certificate                   | on OR off                        |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - friendlyName              | String   | No           | Friendly Name                       | Cisco                            |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - allowWildcardCerts        | String   | No           | Allow Wildcard Certificates         | on OR off                        |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - certificateSanDns         | String   | No           | Certificate SAN DNS                 | cisco.com                        |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - certificateSanIp          | String   | No           | Certificate SAN IP                  | IP-ADDRESS                       |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - certificateSanUri         | String   | No           | Certificate SAN URI                 | URI                              |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+
    | - certificatePolicies       | String   | No           | Certificate Profiles                | certificate policies             |
    +-----------------------------+----------+--------------+-------------------------------------+----------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SystemCertificate
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SystemCertificate, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_system_certificate(self,
                                  ers_local_cert_stub=None,
                                  node_id=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """This API allows the client to create a system certificate.

        Args:
            ers_local_cert_stub(object): Inputs for certificate
                creation, property of the request body.
            node_id(string): NodeId of Cisco ISE application,
                property of the request body.
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
                'nodeId':
                    node_id,
                'ersLocalCertStub':
                    ers_local_cert_stub,
            }
            _payload = {
                'ERSSystemCertificate': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dd469dcee9445c72a3861ef94fb3b096_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/systemcertificate')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_dd469dcee9445c72a3861ef94fb3b096_v3_1_patch_1', _api_response)

    def create(self,
               ers_local_cert_stub=None,
               node_id=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_system_certificate <#ciscoisesdk.
        api.v3_1_patch_1.system_certificate.
        SystemCertificate.create_system_certificate>`_
        """
        return self.create_system_certificate(
            ers_local_cert_stub=ers_local_cert_stub,
            node_id=node_id,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the system certificate.

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

        e_url = ('/ers/config/systemcertificate/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a19fb8fe5fe9b069aa19d2dd74d5_v3_1_patch_1', _api_response)
