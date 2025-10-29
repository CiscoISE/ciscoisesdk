# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Native IPsec API wrapper.

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


class NativeIpsec(object):
    """Identity Services Engine Native IPsec API (version: 3.5.0).

    Wraps the Identity Services Engine Native IPsec
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NativeIpsec
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NativeIpsec, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_ipsec_enabled_nodes(self,
                                filter=None,
                                filter_type=None,
                                page=None,
                                size=None,
                                sort=None,
                                sort_by=None,
                                headers=None,
                                **query_parameters):
        """ Returns all the IPsec enabled nodes with configuration details.
        This API supports filtering, sorting and pagination.
        The attributes that are suppported for filtering are:
        hostName   nadIp   status   authType     The attribute
        that is suppported for sorting is:      hostName    .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            filter(str): filter query parameter.        Simple
                filtering  should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or"  query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.           OPERATOR
                DESCRIPTION   APPLICABLE ON FIELDS
                EQ   Equals   authType       NEQ   Not
                Equals   authType       EQ   Equals
                hostName       NEQ   Not Equals
                hostName       EQ   Equals   nadIp
                NEQ   Not Equals   nadIp       EQ
                Equals   status       NEQ   Not Equals
                status         .
            filter_type(str): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
            sort(str): sort query parameter. sort type asc or desc.
            sort_by(str): sortBy query parameter. Sort column  The
                IPsec enabled nodes are sorted based on
                the columns. This is applicable for the
                field hostName.
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
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))
        check_type(filter, str)
        check_type(filter_type, str)
        check_type(sort, str)
        check_type(sort_by, str)

        _params = {
            'page':
                page,
            'size':
                size,
            'filter':
                filter,
            'filterType':
                filter_type,
            'sort':
                sort,
            'sortBy':
                sort_by,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/api/v1/ipsec')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d9fe5cd54278a69cb1b5c800c32_v3_5_0', _api_response)

    def get_ipsec_enabled_nodes_generator(self,
                                          filter=None,
                                          filter_type=None,
                                          page=None,
                                          size=None,
                                          sort=None,
                                          sort_by=None,
                                          headers=None,
                                          **query_parameters):
        """ Returns all the IPsec enabled nodes with configuration details.
        This API supports filtering, sorting and pagination.
        The attributes that are suppported for filtering are:
        hostName   nadIp   status   authType     The attribute
        that is suppported for sorting is:      hostName    .

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            filter(str): filter query parameter.        Simple
                filtering  should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or"  query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.           OPERATOR
                DESCRIPTION   APPLICABLE ON FIELDS
                EQ   Equals   authType       NEQ   Not
                Equals   authType       EQ   Equals
                hostName       NEQ   Not Equals
                hostName       EQ   Equals   nadIp
                NEQ   Not Equals   nadIp       EQ
                Equals   status       NEQ   Not Equals
                status         .
            filter_type(str): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
            sort(str): sort query parameter. sort type asc or desc.
            sort_by(str): sortBy query parameter. Sort column  The
                IPsec enabled nodes are sorted based on
                the columns. This is applicable for the
                field hostName.
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
            self.get_ipsec_enabled_nodes, dict(
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

    def update_ipsec_connection_config(self,
                                       auth_type=None,
                                       cert_id=None,
                                       configure_vti=None,
                                       esp_ah_protocol=None,
                                       host_name=None,
                                       iface=None,
                                       ike_re_auth_time=None,
                                       ike_version=None,
                                       local_internal_ip=None,
                                       mode_option=None,
                                       nad_ip=None,
                                       phase_one_dhgroup=None,
                                       phase_one_encryption_algo=None,
                                       phase_one_hash_algo=None,
                                       phase_one_life_time=None,
                                       phase_two_dhgroup=None,
                                       phase_two_encryption_algo=None,
                                       phase_two_hash_algo=None,
                                       phase_two_life_time=None,
                                       psk=None,
                                       remote_peer_internal_ip=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """  Updates the configuration of existing IPsec connection.  The
        following parameters are present in the PUT request
        body:         PARAMETER   DESCRIPTION   EXAMPLE
        id *required   ID of the existing IPsec configuration.
        "id": "7c9484cf-0ebc-47ad-a9ef-bc12729ed73b"       iface
        *required   Ethernet port used for establishing
        connection   "iface": "0"       psk *required   Pre-
        shared key used for establishing connection.   "psk":
        "psk12345"       authType *required   Pre-shared key
        used for establishing connection.   "authType": "psk"
        configureVti   Used For VTI Configurations
        "configureVti": "false"       remotePeerInternalIp   VTI
        Internal IP of the NAD   "remotePeerInternalIp":
        "1.2.3.1"       localInternalIp   IP address assigned to
        the VTI interface so this would be the internal ip
        "localInternalIp": "1.1.3.1"       certId *required   ID
        of the certificate for establishing connection.
        "certId": "21323243545433"       phaseOneEncryptionAlgo
        *required   Phase-one encryption algorithm used for
        establishing connection.   "phaseOneEncryptionAlgo":
        "aes"       phaseTwoEncryptionAlgo *required   Phase-two
        encryption algorithm used for establishing connection.
        "phaseTwoEncryptionAlgo": "aes"       espAhProtocol
        *required   Encryption protocol used for establishing
        connection.   "espAhProtocol": "ah"
        phaseOneHashAlgo *required   Phase-one hashing algorithm
        used for establishing connection.   "phaseOneHashAlgo":
        "sha"       phaseTwoHashAlgo *required   Phase-two
        hashing algorithm used for establishing connection.
        "phaseTwoHashAlgo": "sha"       phaseOneDHGroup
        *required   Phase-one DH group used for establishing
        connection.   "phaseOneDHGroup": "GROUP1"
        phaseTwoDHGroup   Phase-two DH group used for
        establishing connection.   "phaseTwoDHGroup": "GROUP1"
        phaseOneLifeTime   DH Phase-one connection lifetime.
        "phaseOneLifeTime": 14400       phaseTwoLifeTime   DH
        Phase-two connection lifetime.   "phaseTwoLifeTime":
        14400       ikeVersion *required   IKE version.
        "ikeVersion": "1"       ikeReAuthTime   IKE re-
        authentication time.   "ikeReAuthTime": 86400
        nadIp *required   NAD IP for establishing connection.
        "nadIp": "1.1.1.1"       modeOption *required   The Mode
        type used for establishing the connection.
        "modeOption": "tunnel"         NOTE:    psk  field is
        mandatory if authType=psk   certId  field is mandatory
        if authType=x509    If FIPS mode is on.:      Cannot
        choose DES or 3DES for Phase-one and Phase-two
        Encryption algorithms.   PSK length must be 14
        characters or more.   DH Groups 1, 2, and 5 cannot be
        chosen for Phase-one and Phase-two fields.      .

        Args:
            auth_type(string): Authentication type for establishing
                connection, property of the request
                body. Available values are 'psk' and
                'x509'.
            cert_id(string): ID of the certificate for establishing
                connection, property of the request
                body.
            configure_vti(boolean): Authentication type for
                establishing connection, property of the
                request body.
            esp_ah_protocol(string): Encryption protocol used for
                establishing connection, property of the
                request body. Available values are 'ah'
                and 'esp'.
            host_name(string): Hostname of the node, property of the
                request body.
            iface(string): Ethernet port of the node, property of
                the request body.
            ike_re_auth_time(integer): IKE re-authentication time,
                property of the request body.
            ike_version(string): IKE version, property of the
                request body. Available values are '1'
                and '2'.
            local_internal_ip(string): Local Tunnel IP address,
                property of the request body.
            mode_option(string): The Mode type used for establishing
                the connection, property of the request
                body. Available values are 'transport'
                and 'tunnel'.
            nad_ip(string): NAD IP address for establishing
                connection, property of the request
                body.
            phase_one_dhgroup(string): Phase-one DH group used for
                establishing connection, property of the
                request body. Available values are
                'GROUP1', 'GROUP14', 'GROUP15',
                'GROUP16', 'GROUP19', 'GROUP2',
                'GROUP20', 'GROUP21', 'GROUP24' and
                'GROUP5'.
            phase_one_encryption_algo(string): Phase-one encryption
                algorithm used for establishing
                connection, property of the request
                body. Available values are '3des',
                'aes', 'aes128', 'aes192', 'aes256' and
                'des'.
            phase_one_hash_algo(string): Phase-one hashing algorithm
                used for establishing connection,
                property of the request body. Available
                values are 'sha', 'sha256', 'sha384' and
                'sha512'.
            phase_one_life_time(integer): Phase-one connection
                lifetime, property of the request body.
            phase_two_dhgroup(string): Phase-two DH group used for
                establishing connection, property of the
                request body. Available values are
                'GROUP1', 'GROUP14', 'GROUP15',
                'GROUP16', 'GROUP19', 'GROUP2',
                'GROUP20', 'GROUP21', 'GROUP24',
                'GROUP5' and 'NONE'.
            phase_two_encryption_algo(string): Phase-two encryption
                algorithm used for establishing
                connection, property of the request
                body. Available values are '3des',
                'aes', 'aes128', 'aes192', 'aes256',
                'des', 'gcm' and 'gmac'.
            phase_two_hash_algo(string): Phase-two hashing algorithm
                used for establishing connection,
                property of the request body. Available
                values are 'sha', 'sha256', 'sha384' and
                'sha512'.
            phase_two_life_time(integer): Phase-two connection
                lifetime, property of the request body.
            psk(string): Pre-shared key used for establishing
                connection, property of the request
                body.
            remote_peer_internal_ip(string): Remote Tunnel IP
                address, property of the request body.
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
            _payload = {
                'authType':
                    auth_type,
                'certId':
                    cert_id,
                'configureVti':
                    configure_vti,
                'espAhProtocol':
                    esp_ah_protocol,
                'hostName':
                    host_name,
                'iface':
                    iface,
                'ikeReAuthTime':
                    ike_re_auth_time,
                'ikeVersion':
                    ike_version,
                'localInternalIp':
                    local_internal_ip,
                'modeOption':
                    mode_option,
                'nadIp':
                    nad_ip,
                'phaseOneDHGroup':
                    phase_one_dhgroup,
                'phaseOneEncryptionAlgo':
                    phase_one_encryption_algo,
                'phaseOneHashAlgo':
                    phase_one_hash_algo,
                'phaseOneLifeTime':
                    phase_one_life_time,
                'phaseTwoDHGroup':
                    phase_two_dhgroup,
                'phaseTwoEncryptionAlgo':
                    phase_two_encryption_algo,
                'phaseTwoHashAlgo':
                    phase_two_hash_algo,
                'phaseTwoLifeTime':
                    phase_two_life_time,
                'psk':
                    psk,
                'remotePeerInternalIp':
                    remote_peer_internal_ip,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d4fb0706d0f5226b8691538a2bc7309_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/ipsec')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d4fb0706d0f5226b8691538a2bc7309_v3_5_0', _api_response)

    def create_ipsec_connection(self,
                                auth_type=None,
                                cert_id=None,
                                configure_vti=None,
                                esp_ah_protocol=None,
                                host_name=None,
                                iface=None,
                                ike_re_auth_time=None,
                                ike_version=None,
                                local_internal_ip=None,
                                mode_option=None,
                                nad_ip=None,
                                phase_one_dhgroup=None,
                                phase_one_encryption_algo=None,
                                phase_one_hash_algo=None,
                                phase_one_life_time=None,
                                phase_two_dhgroup=None,
                                phase_two_encryption_algo=None,
                                phase_two_hash_algo=None,
                                phase_two_life_time=None,
                                psk=None,
                                remote_peer_internal_ip=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """  Creates an IPsec connection.  The following parameters are
        present in the POST request body:         PARAMETER
        DESCRIPTION   EXAMPLE           hostName *required
        Hostname of the node for which IPsec should be enabled
        "hostName": "ise-host1"       iface *required   Ethernet
        port used for establishing connection   "iface": "0"
        psk *required   Pre-shared key used for establishing
        connection.   "psk": "psk12345"       authType *required
        Pre-shared key used for establishing connection.
        "authType": "psk"       configureVti   Used For VTI
        Configurations   "configureVti": "false"
        remotePeerInternalIp   VTI Internal IP of the NAD
        "remotePeerInternalIp": "1.2.3.1"       localInternalIp
        IP address assigned to the VTI interface so this would
        be the internal ip   "localInternalIp": "1.1.3.1"
        certId *required   ID of the certificate for
        establishing connection.   "certId": "21323243545433"
        phaseOneEncryptionAlgo *required   Phase-one encryption
        algorithm used for establishing connection.
        "phaseOneEncryptionAlgo": "aes"
        phaseTwoEncryptionAlgo *required   Phase-two encryption
        algorithm used for establishing connection.
        "phaseTwoEncryptionAlgo": "aes"       espAhProtocol
        *required   Encryption protocol used for establishing
        connection.   "espAhProtocol": "ah"
        phaseOneHashAlgo *required   Phase-one hashing algorithm
        used for establishing connection.   "phaseOneHashAlgo":
        "sha"       phaseTwoHashAlgo *required   Phase-two
        hashing algorithm used for establishing connection.
        "phaseTwoHashAlgo": "sha"       phaseOneDHGroup
        *required   Phase-one DH group used for establishing
        connection.   "phaseOneDHGroup": "GROUP1"
        phaseTwoDHGroup   Phase-two DH group used for
        establishing connection.   "phaseTwoDHGroup": "GROUP1"
        phaseOneLifeTime   DH Phase-one connection lifetime.
        "phaseOneLifeTime": 14400       phaseTwoLifeTime   DH
        Phase-two connection lifetime.   "phaseTwoLifeTime":
        14400       ikeVersion *required   IKE version.
        "ikeVersion": "1"       ikeReAuthTime   IKE re-
        authentication time.   "ikeReAuthTime": 86400
        nadIp *required   NAD IP for establishing the
        connection.   "nadIp": "1.1.1.1"       modeOption
        *required   The Mode type used for establishing the
        connection.   "modeOption": "tunnel"         NOTE:
        psk  field is mandatory if authType=psk   certId  field
        is mandatory if authType=x509    If FIPS mode is on.:
        Cannot choose DES or 3DES for Phase-one and Phase-two
        Encryption algorithms.   PSK length must be 14
        characters or more.   DH Groups 1, 2, and 5 cannot be
        chosen for Phase-one and Phase-two fields.      .

        Args:
            auth_type(string): Authentication type for establishing
                connection, property of the request
                body. Available values are 'psk' and
                'x509'.
            cert_id(string): ID of the certificate for establishing
                connection, property of the request
                body.
            configure_vti(boolean): Authentication type for
                establishing connection, property of the
                request body.
            esp_ah_protocol(string): Encryption protocol used for
                establishing connection, property of the
                request body. Available values are 'ah'
                and 'esp'.
            host_name(string): Hostname of the node, property of the
                request body.
            iface(string): Ethernet port of the node, property of
                the request body.
            ike_re_auth_time(integer): IKE re-authentication time,
                property of the request body.
            ike_version(string): IKE version, property of the
                request body. Available values are '1'
                and '2'.
            local_internal_ip(string): Local Tunnel IP address,
                property of the request body.
            mode_option(string): The Mode type used for establishing
                the connection, property of the request
                body. Available values are 'transport'
                and 'tunnel'.
            nad_ip(string): NAD IP address for establishing
                connection, property of the request
                body.
            phase_one_dhgroup(string): Phase-one DH group used for
                establishing connection, property of the
                request body. Available values are
                'GROUP1', 'GROUP14', 'GROUP15',
                'GROUP16', 'GROUP19', 'GROUP2',
                'GROUP20', 'GROUP21', 'GROUP24' and
                'GROUP5'.
            phase_one_encryption_algo(string): Phase-one encryption
                algorithm used for establishing
                connection, property of the request
                body. Available values are '3des',
                'aes', 'aes128', 'aes192', 'aes256' and
                'des'.
            phase_one_hash_algo(string): Phase-one hashing algorithm
                used for establishing connection,
                property of the request body. Available
                values are 'sha', 'sha256', 'sha384' and
                'sha512'.
            phase_one_life_time(integer): Phase-one connection
                lifetime, property of the request body.
            phase_two_dhgroup(string): Phase-two DH group used for
                establishing connection, property of the
                request body. Available values are
                'GROUP1', 'GROUP14', 'GROUP15',
                'GROUP16', 'GROUP19', 'GROUP2',
                'GROUP20', 'GROUP21', 'GROUP24',
                'GROUP5' and 'NONE'.
            phase_two_encryption_algo(string): Phase-two encryption
                algorithm used for establishing
                connection, property of the request
                body. Available values are '3des',
                'aes', 'aes128', 'aes192', 'aes256',
                'des', 'gcm' and 'gmac'.
            phase_two_hash_algo(string): Phase-two hashing algorithm
                used for establishing connection,
                property of the request body. Available
                values are 'sha', 'sha256', 'sha384' and
                'sha512'.
            phase_two_life_time(integer): Phase-two connection
                lifetime, property of the request body.
            psk(string): Pre-shared key used for establishing
                connection, property of the request
                body.
            remote_peer_internal_ip(string): Remote Tunnel IP
                address, property of the request body.
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
            _payload = {
                'authType':
                    auth_type,
                'certId':
                    cert_id,
                'configureVti':
                    configure_vti,
                'espAhProtocol':
                    esp_ah_protocol,
                'hostName':
                    host_name,
                'iface':
                    iface,
                'ikeReAuthTime':
                    ike_re_auth_time,
                'ikeVersion':
                    ike_version,
                'localInternalIp':
                    local_internal_ip,
                'modeOption':
                    mode_option,
                'nadIp':
                    nad_ip,
                'phaseOneDHGroup':
                    phase_one_dhgroup,
                'phaseOneEncryptionAlgo':
                    phase_one_encryption_algo,
                'phaseOneHashAlgo':
                    phase_one_hash_algo,
                'phaseOneLifeTime':
                    phase_one_life_time,
                'phaseTwoDHGroup':
                    phase_two_dhgroup,
                'phaseTwoEncryptionAlgo':
                    phase_two_encryption_algo,
                'phaseTwoHashAlgo':
                    phase_two_hash_algo,
                'phaseTwoLifeTime':
                    phase_two_life_time,
                'psk':
                    psk,
                'remotePeerInternalIp':
                    remote_peer_internal_ip,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ef20d5d63551dbe25878007747598_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/ipsec')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ef20d5d63551dbe25878007747598_v3_5_0', _api_response)

    def bulk_ip_sec_operation(self,
                              item_list=None,
                              operation=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **query_parameters):
        """Create, update, disable, enable and remove IPsec connections in
        bulk.

        Args:
            item_list(list): ItemList, property of the request body
                (list of objects).
            operation(string): operation, property of the request
                body. Available values are 'Create',
                'Delete', 'Disable', 'Enable' and
                'Update'.
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
            _payload = {
                'ItemList':
                    item_list,
                'operation':
                    operation,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eca8a69196d555a1b7e71cf190bd2641_v3_5_0')\
                .validate(_payload)

        e_url = ('/api/v1/ipsec/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_eca8a69196d555a1b7e71cf190bd2641_v3_5_0', _api_response)

    def get_ip_sec_certificates(self,
                                headers=None,
                                **query_parameters):
        """ Returns all the certificates for IPsec role.   .

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

        e_url = ('/api/v1/ipsec/certificates')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a5e87f906e357bcb972c60ee082d89b_v3_5_0', _api_response)

    def disable_ipsec_connection(self,
                                 host_name,
                                 nad_ip,
                                 headers=None,
                                 **query_parameters):
        """Disables an enabled IPsec node connection.

        Args:
            host_name(str): hostName path parameter. Hostname of the
                deployed node.
            nad_ip(str): nadIp path parameter. IP address of the
                NAD.
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
        check_type(host_name, str,
                   may_be_none=False)
        check_type(nad_ip, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'nadIp': nad_ip,
        }

        e_url = ('/api/v1/ipsec/disable/{hostName}/{nadIp}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f159a76b6aa52c2b0d0a2fe31dcae91_v3_5_0', _api_response)

    def enable_ipsec_connection(self,
                                host_name,
                                nad_ip,
                                headers=None,
                                **query_parameters):
        """Enables an disabled IPsec node connection.

        Args:
            host_name(str): hostName path parameter. Hostname of the
                deployed node.
            nad_ip(str): nadIp path parameter. IP address of the
                NAD.
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
        check_type(host_name, str,
                   may_be_none=False)
        check_type(nad_ip, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'nadIp': nad_ip,
        }

        e_url = ('/api/v1/ipsec/enable/{hostName}/{nadIp}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b57a1b126cb53ed8533eb22db13719d_v3_5_0', _api_response)

    def get_ipsec_node(self,
                       host_name,
                       nad_ip,
                       headers=None,
                       **query_parameters):
        """Returns the IPsec configuration details of a given node with the
        hostname and the NAD IP.

        Args:
            host_name(str): hostName path parameter. Hostname of the
                deployed node.
            nad_ip(str): nadIp path parameter. IP address of the
                NAD.
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
        check_type(host_name, str,
                   may_be_none=False)
        check_type(nad_ip, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'nadIp': nad_ip,
        }

        e_url = ('/api/v1/ipsec/{hostName}/{nadIp}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a5dd6bd055c73bc02c8a389fd353f_v3_5_0', _api_response)

    def remove_ipsec_connection(self,
                                host_name,
                                nad_ip,
                                headers=None,
                                **query_parameters):
        """Removes an enabled IPsec node connection.

        Args:
            host_name(str): hostName path parameter. Hostname of the
                deployed node.
            nad_ip(str): nadIp path parameter. IP address of the
                NAD.
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
        check_type(host_name, str,
                   may_be_none=False)
        check_type(nad_ip, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'hostName': host_name,
            'nadIp': nad_ip,
        }

        e_url = ('/api/v1/ipsec/{hostName}/{nadIp}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f2a9c1f22035982beaa10f027814d01_v3_5_0', _api_response)
