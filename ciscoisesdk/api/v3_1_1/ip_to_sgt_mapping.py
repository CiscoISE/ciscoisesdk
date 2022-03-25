# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine IPToSGTMapping API wrapper.

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


class IpToSgtMapping(object):
    """Identity Services Engine IPToSGTMapping API (version: 3.1.1).

    Wraps the Identity Services Engine IPToSGTMapping
    API and exposes the API as native Python
    methods that return native Python objects.

    | IP To SGT Mapping API allows the client to add, delete, update, search and deploy IP to SGT mapping.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.0                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | **Attribute** | **Type**    | **Required**                                                  | **Description**                     | **Example Values** |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | name          | String      | Yes                                                           | Resource Name                       | server1.cisco.com  |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | id            | String      | No                                                            | Resource UUID, mandatory for update |                    |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | description   | String      | No                                                            |                                     |                    |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | deployTo      | String      | Mandatory unless mappingGroup is set or unless deployType=ALL |                                     | network_device_id  |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | deployType    | Enum        | Yes                                                           | Allowed values: ALL, ND, NDG        | ND                 |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | hostName      | String      | Mandatory if hostIp is empty                                  |                                     | server1.cisco.com  |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | sgt           | String      | Mandatory unless mappingGroup is set                          |                                     | sgt_id             |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | hostIp        | String      | Mandatory if hostName is empty -- valid IPL                   |                                     |                    |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+
    | mappingGroup  | String      | Mandatory unless sgt and deployTo and deployType are set      |                                     |                    |
    +---------------+-------------+---------------------------------------------------------------+-------------------------------------+--------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new IpToSgtMapping
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(IpToSgtMapping, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def deploy_ip_to_sgt_mapping_by_id(self,
                                       id,
                                       headers=None,
                                       **query_parameters):
        """This API allows the client to deploy an IP to SGT mapping by ID.
        Only one Deploy process can run at any given time.

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

        e_url = ('/ers/config/sgmapping/{id}/deploy')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b5711af534e557749661afb5b6c90cee_v3_1_1', _api_response)

    def deploy_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `deploy_ip_to_sgt_mapping_by_id <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.deploy_ip_to_sgt_mapping_by_id>`_
        """
        return self.deploy_ip_to_sgt_mapping_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def deploy_all_ip_to_sgt_mapping(self,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to deploy all the IP to SGT mappings.
        Only one Deploy process can run at any given time.

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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/sgmapping/deployall')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_df7a50feb38d8729b99553e9_v3_1_1', _api_response)

    def deploy_all(self,
                   headers=None,
                   **query_parameters):
        """Alias for `deploy_all_ip_to_sgt_mapping <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.deploy_all_ip_to_sgt_mapping>`_
        """
        return self.deploy_all_ip_to_sgt_mapping(
            headers=headers,
            **query_parameters
        )

    def get_deploy_status_ip_to_sgt_mapping(self,
                                            headers=None,
                                            **query_parameters):
        """This API allows the client to get the IP to SGT mapping
        deployment status. Deploy Status will show last Deploy
        command output. The information will be saved until the
        next Deploy command.

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

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/sgmapping/deploy/status')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dcd55e1e57d25e65b625526a1d341afd_v3_1_1', _api_response)

    def get_deploy_status(self,
                          headers=None,
                          **query_parameters):
        """Alias for `get_deploy_status_ip_to_sgt_mapping <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.get_deploy_status_ip_to_sgt_mapping>`_
        """
        return self.get_deploy_status_ip_to_sgt_mapping(
            headers=headers,
            **query_parameters
        )

    def get_ip_to_sgt_mapping_by_id(self,
                                    id,
                                    headers=None,
                                    **query_parameters):
        """This API allows the client to get an IP to SGT mapping by ID.

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

        e_url = ('/ers/config/sgmapping/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ddc6729af25f8b8c060b20d09f0057_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_ip_to_sgt_mapping_by_id <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.get_ip_to_sgt_mapping_by_id>`_
        """
        return self.get_ip_to_sgt_mapping_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_ip_to_sgt_mapping_by_id(self,
                                       id,
                                       deploy_to=None,
                                       deploy_type=None,
                                       host_ip=None,
                                       host_name=None,
                                       mapping_group=None,
                                       name=None,
                                       sgt=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """This API allows the client to update an IP to SGT mapping by ID.

        Args:
            deploy_to(string): Mandatory unless mappingGroup is set
                or unless deployType=ALL, property of
                the request body.
            deploy_type(string): Allowed values: ALL, ND, NDG,
                property of the request body.
            host_ip(string): Mandatory if hostName is empty -valid
                IP, property of the request body.
            host_name(string): Mandatory if hostIp is empty,
                property of the request body.
            id(string): id, property of the request body.
            mapping_group(string): Mapping Group Id. Mandatory
                unless sgt and deployTo and deployType
                are set, property of the request body.
            name(string): name, property of the request body.
            sgt(string): Mandatory unless mappingGroup is set,
                property of the request body.
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
                'sgt':
                    sgt,
                'deployTo':
                    deploy_to,
                'deployType':
                    deploy_type,
                'hostName':
                    host_name,
                'hostIp':
                    host_ip,
                'mappingGroup':
                    mapping_group,
            }
            _payload = {
                'SGMapping': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_de3cecd62e5153881245a8613fbeea_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgmapping/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_de3cecd62e5153881245a8613fbeea_v3_1_1', _api_response)

    def update_by_id(self,
                     id,
                     deploy_to=None,
                     deploy_type=None,
                     host_ip=None,
                     host_name=None,
                     mapping_group=None,
                     name=None,
                     sgt=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_ip_to_sgt_mapping_by_id <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.update_ip_to_sgt_mapping_by_id>`_
        """
        return self.update_ip_to_sgt_mapping_by_id(
            id=id,
            deploy_to=deploy_to,
            deploy_type=deploy_type,
            host_ip=host_ip,
            host_name=host_name,
            mapping_group=mapping_group,
            name=name,
            sgt=sgt,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_ip_to_sgt_mapping_by_id(self,
                                       id,
                                       headers=None,
                                       **query_parameters):
        """This API deletes an IP to SGT mapping.

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

        e_url = ('/ers/config/sgmapping/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f0cb1e55c9baee89c136c8ec47_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_ip_to_sgt_mapping_by_id <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.delete_ip_to_sgt_mapping_by_id>`_
        """
        return self.delete_ip_to_sgt_mapping_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_ip_to_sgt_mapping(self,
                              filter=None,
                              filter_type=None,
                              page=None,
                              size=None,
                              sortasc=None,
                              sortdsc=None,
                              headers=None,
                              **query_parameters):
        """This API allows the client to get all the IP to SGT mappings.
        Filter:   [hostName, groupName, ip, sgtName]   To search
        guest users by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [hostName, groupName, ip, sgtName].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
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
        check_type(sortasc, basestring)
        check_type(sortdsc, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sortasc':
                sortasc,
            'sortdsc':
                sortdsc,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/sgmapping')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cd9e91565f5c74b9f32ff0e5be6f17_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_ip_to_sgt_mapping <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.get_ip_to_sgt_mapping>`_
        """
        return self.get_ip_to_sgt_mapping(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_ip_to_sgt_mapping_generator(self,
                                        filter=None,
                                        filter_type=None,
                                        page=None,
                                        size=None,
                                        sortasc=None,
                                        sortdsc=None,
                                        headers=None,
                                        **query_parameters):
        """This API allows the client to get all the IP to SGT mappings.
        Filter:   [hostName, groupName, ip, sgtName]   To search
        guest users by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [hostName, groupName, ip, sgtName].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
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

        yield from get_next_page(
            self.get_ip_to_sgt_mapping, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sortasc=None,
                          sortdsc=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_ip_to_sgt_mapping_generator <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.get_ip_to_sgt_mapping_generator>`_
        """
        yield from get_next_page(
            self.get_ip_to_sgt_mapping, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_ip_to_sgt_mapping(self,
                                 deploy_to=None,
                                 deploy_type=None,
                                 host_ip=None,
                                 host_name=None,
                                 mapping_group=None,
                                 name=None,
                                 sgt=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **query_parameters):
        """This API creates an IP to SGT mapping.

        Args:
            deploy_to(string): Mandatory unless mappingGroup is set
                or unless deployType=ALL, property of
                the request body.
            deploy_type(string): Allowed values: ALL, ND, NDG,
                property of the request body.
            host_ip(string): Mandatory if hostName is empty -valid
                IP, property of the request body.
            host_name(string): Mandatory if hostIp is empty,
                property of the request body.
            mapping_group(string): Mapping Group Id. Mandatory
                unless sgt and deployTo and deployType
                are set, property of the request body.
            name(string): name, property of the request body.
            sgt(string): Mandatory unless mappingGroup is set,
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
                'name':
                    name,
                'sgt':
                    sgt,
                'deployTo':
                    deploy_to,
                'deployType':
                    deploy_type,
                'hostName':
                    host_name,
                'hostIp':
                    host_ip,
                'mappingGroup':
                    mapping_group,
            }
            _payload = {
                'SGMapping': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_dd838b268f5dd298a123ac58448ea9_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgmapping')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_dd838b268f5dd298a123ac58448ea9_v3_1_1', _api_response)

    def create(self,
               deploy_to=None,
               deploy_type=None,
               host_ip=None,
               host_name=None,
               mapping_group=None,
               name=None,
               sgt=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_ip_to_sgt_mapping <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.create_ip_to_sgt_mapping>`_
        """
        return self.create_ip_to_sgt_mapping(
            deploy_to=deploy_to,
            deploy_type=deploy_type,
            host_ip=host_ip,
            host_name=host_name,
            mapping_group=mapping_group,
            name=name,
            sgt=sgt,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to IP
        to SGT mapping.

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

        e_url = ('/ers/config/sgmapping/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af0b5041b56b12c5c08cc53e_v3_1_1', _api_response)

    def bulk_request_for_ip_to_sgt_mapping(self,
                                           operation_type=None,
                                           resource_media_type=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **query_parameters):
        """This API allows the client to submit the bulk request.

        Args:
            operation_type(string): operationType, property of the
                request body.
            resource_media_type(string): resourceMediaType, property
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
                'operationType':
                    operation_type,
                'resourceMediaType':
                    resource_media_type,
            }
            _payload = {
                'SGMappingBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ab203a1dd0015924bf2005a84ae85477_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sgmapping/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_ab203a1dd0015924bf2005a84ae85477_v3_1_1', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_ip_to_sgt_mapping <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.bulk_request_for_ip_to_sgt_mapping>`_
        """
        return self.bulk_request_for_ip_to_sgt_mapping(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_ip_to_sgt_mapping(self,
                                              bulkid,
                                              headers=None,
                                              **query_parameters):
        """This API allows the client to monitor the bulk request.

        Args:
            bulkid(basestring): bulkid path parameter.
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
        check_type(bulkid, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'bulkid': bulkid,
        }

        e_url = ('/ers/config/sgmapping/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f36d3f43a6157978ec529318ce506e0_v3_1_1', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_ip_to_sgt_mapping <#ciscoisesdk.
        api.v3_1_1.ip_to_sgt_mapping.
        IpToSgtMapping.monitor_bulk_status_ip_to_sgt_mapping>`_
        """
        return self.monitor_bulk_status_ip_to_sgt_mapping(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )
