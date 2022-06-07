# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine RADIUSServerSequence API wrapper.

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


class RadiusServerSequence(object):
    """Identity Services Engine RADIUSServerSequence API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine RADIUSServerSequence
    API and exposes the API as native Python
    methods that return native Python objects.

    | RADIUS Server Sequence API allows the client to add, delete, update, search and perform actions on RADIUS server sequence.

    **Revision History**

    +----------------+----------------------+-----------------------+---------------------------+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**           |
    +----------------+----------------------+-----------------------+---------------------------+
    | 0              | 1.0                  | 2.3                   | Initial Cisco ISE Version |
    +----------------+----------------------+-----------------------+---------------------------+

    |

    **Resource Definition**

    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | **Attribute**                | **Type**  | **Required** | **Description**                                                                                                                               | **Default Values** | **Example Values**                                   |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | name                         | String    | Yes          | Resource Name                                                                                                                                 |                    | name                                                 |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | id                           | String    | No           | Resource UUID, mandatory for update                                                                                                           |                    | ab6deded-fcc2-47ff-8577-0014737c8fcf                 |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | description                  | String    | No           |                                                                                                                                               |                    | description                                          |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | stripPrefix                  | Boolean   | No           |                                                                                                                                               | false              |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | stripSuffix                  | Boolean   | No           |                                                                                                                                               | false              |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | prefixSeparator              | String    | No           | The prefixSeparator is required only if stripPrefix is true. The maximum length is 1 character                                                | \\                  |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | suffixSeparator              | String    | No           | The suffixSeparator is required only if stripSuffix is true. The maximum length is 1 character                                                | @                  |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | remoteAccounting             | Boolean   | No           |                                                                                                                                               | true               |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | localAccounting              | Boolean   | No           |                                                                                                                                               | false              |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | useAttrSetOnRequest          | Boolean   | No           |                                                                                                                                               | false              |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | useAttrSetBeforeAcc          | Boolean   | No           |                                                                                                                                               | false              |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | continueAuthorzPolicy        | Boolean   | No           |                                                                                                                                               | false              |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | radiusServers                | List      | Yes          | List with names of external radius server. The order of the names in the list is the order of servers that will be used during authentication |                    | [ "externalRadiusServer1", "externalRadiusServer2" ] |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | onRequestAttrManipulators    | List      | No           | The onRequestAttrManipulators is required only if useAttrSetOnRequest is true                                                                 |                    |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | - AttributeManipulator       | List      | No           |                                                                                                                                               |                    |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - action                   | Enum      | Yes          | Allowed Values: ADD, UPDATE, REMOVE, REMOVEANY                                                                                                |                    | ADD                                                  |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - dictionaryName           | String    | Yes          |                                                                                                                                               |                    | Cisco                                                |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - attributeName            | String    | Yes          |                                                                                                                                               |                    | cisco-prev-hop-ip                                    |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - value                    | String    | Yes          |                                                                                                                                               |                    | test1                                                |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - changedVal               | String    | No           | The changedVal is required only if the action equals to 'UPDATE'                                                                              |                    | test2                                                |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | beforeAcceptAttrManipulators | List      | No           | The beforeAcceptAttrManipulators is required only if useAttrSetBeforeAcc is true                                                              |                    |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    | - AttributeManipulator       | List      | No           |                                                                                                                                               |                    |                                                      |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - action                   | Enum      | Yes          | Allowed Values: ADD, UPDATE, REMOVE, REMOVEANY                                                                                                |                    | ADD                                                  |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - dictionaryName           | String    | Yes          |                                                                                                                                               |                    | Cisco                                                |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - attributeName            | String    | Yes          |                                                                                                                                               |                    | cisco-prev-hop-ip                                    |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - value                    | String    | Yes          |                                                                                                                                               |                    | test1                                                |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+
    |   - changedVal               | String    | No           | The changedVal is required only if the action equals to 'UPDATE'                                                                              |                    | test2                                                |
    +------------------------------+-----------+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+------------------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new RadiusServerSequence
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(RadiusServerSequence, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_radius_server_sequence_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """This API allows the client to get a RADIUS server sequence by
        ID.

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

        e_url = ('/ers/config/radiusserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d1df0e230765104863b8d63d5beb68e_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_radius_server_sequence_by_id <#ciscoisesdk.
        api.v3_1_patch_1.radius_server_sequence.
        RadiusServerSequence.get_radius_server_sequence_by_id>`_
        """
        return self.get_radius_server_sequence_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_radius_server_sequence_by_id(self,
                                            id,
                                            before_accept_attr_manipulators_list=None,
                                            continue_authorz_policy=None,
                                            description=None,
                                            local_accounting=None,
                                            name=None,
                                            on_request_attr_manipulator_list=None,
                                            prefix_separator=None,
                                            radius_server_list=None,
                                            remote_accounting=None,
                                            strip_prefix=None,
                                            strip_suffix=None,
                                            suffix_separator=None,
                                            use_attr_set_before_acc=None,
                                            use_attr_set_on_request=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """This API allows the client to update a RADIUS server sequence.

        Args:
            before_accept_attr_manipulators_list(list): The
                beforeAcceptAttrManipulators is required
                only if useAttrSetBeforeAcc is true,
                property of the request body (list of
                objects).
            on_request_attr_manipulator_list(list): The
                onRequestAttrManipulators is required
                only if useAttrSetOnRequest is true,
                property of the request body (list of
                objects).
            radius_server_list(list): RadiusServerList, property of
                the request body (list of strings).
            continue_authorz_policy(boolean): continueAuthorzPolicy,
                property of the request body.
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            local_accounting(boolean): localAccounting, property of
                the request body.
            name(string): name, property of the request body.
            prefix_separator(string): The prefixSeparator is
                required only if stripPrefix is true.
                The maximum length is 1 character,
                property of the request body.
            remote_accounting(boolean): remoteAccounting, property
                of the request body.
            strip_prefix(boolean): stripPrefix, property of the
                request body.
            strip_suffix(boolean): stripSuffix, property of the
                request body.
            suffix_separator(string): The suffixSeparator is
                required only if stripSuffix is true.
                The maximum length is 1 character,
                property of the request body.
            use_attr_set_before_acc(boolean): useAttrSetBeforeAcc,
                property of the request body.
            use_attr_set_on_request(boolean): useAttrSetOnRequest,
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
                'description':
                    description,
                'stripPrefix':
                    strip_prefix,
                'stripSuffix':
                    strip_suffix,
                'prefixSeparator':
                    prefix_separator,
                'suffixSeparator':
                    suffix_separator,
                'remoteAccounting':
                    remote_accounting,
                'localAccounting':
                    local_accounting,
                'useAttrSetOnRequest':
                    use_attr_set_on_request,
                'useAttrSetBeforeAcc':
                    use_attr_set_before_acc,
                'continueAuthorzPolicy':
                    continue_authorz_policy,
                'RadiusServerList':
                    radius_server_list,
                'OnRequestAttrManipulatorList':
                    on_request_attr_manipulator_list,
                'BeforeAcceptAttrManipulatorsList':
                    before_accept_attr_manipulators_list,
            }
            _payload = {
                'RadiusServerSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_df9ab8ff636353279d5c787585dcb6af_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/radiusserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_df9ab8ff636353279d5c787585dcb6af_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
                     before_accept_attr_manipulators_list=None,
                     continue_authorz_policy=None,
                     description=None,
                     local_accounting=None,
                     name=None,
                     on_request_attr_manipulator_list=None,
                     prefix_separator=None,
                     radius_server_list=None,
                     remote_accounting=None,
                     strip_prefix=None,
                     strip_suffix=None,
                     suffix_separator=None,
                     use_attr_set_before_acc=None,
                     use_attr_set_on_request=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_radius_server_sequence_by_id <#ciscoisesdk.
        api.v3_1_patch_1.radius_server_sequence.
        RadiusServerSequence.update_radius_server_sequence_by_id>`_
        """
        return self.update_radius_server_sequence_by_id(
            id=id,
            before_accept_attr_manipulators_list=before_accept_attr_manipulators_list,
            continue_authorz_policy=continue_authorz_policy,
            description=description,
            local_accounting=local_accounting,
            name=name,
            on_request_attr_manipulator_list=on_request_attr_manipulator_list,
            prefix_separator=prefix_separator,
            radius_server_list=radius_server_list,
            remote_accounting=remote_accounting,
            strip_prefix=strip_prefix,
            strip_suffix=strip_suffix,
            suffix_separator=suffix_separator,
            use_attr_set_before_acc=use_attr_set_before_acc,
            use_attr_set_on_request=use_attr_set_on_request,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_radius_server_sequence_by_id(self,
                                            id,
                                            headers=None,
                                            **query_parameters):
        """This API deletes a RADIUS server sequence.

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

        e_url = ('/ers/config/radiusserversequence/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b13838fa75d6e8d970f6eeb6a4510_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_radius_server_sequence_by_id <#ciscoisesdk.
        api.v3_1_patch_1.radius_server_sequence.
        RadiusServerSequence.delete_radius_server_sequence_by_id>`_
        """
        return self.delete_radius_server_sequence_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_radius_server_sequence(self,
                                   page=None,
                                   size=None,
                                   headers=None,
                                   **query_parameters):
        """This API allows the client to get all the RADIUS server
        sequences.

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

        e_url = ('/ers/config/radiusserversequence')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c6c330dace185a548f70f4e5d67776ea_v3_1_patch_1', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_radius_server_sequence <#ciscoisesdk.
        api.v3_1_patch_1.radius_server_sequence.
        RadiusServerSequence.get_radius_server_sequence>`_
        """
        return self.get_radius_server_sequence(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_radius_server_sequence_generator(self,
                                             page=None,
                                             size=None,
                                             headers=None,
                                             **query_parameters):
        """This API allows the client to get all the RADIUS server
        sequences.

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
            self.get_radius_server_sequence, dict(
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
        """Alias for `get_radius_server_sequence_generator <#ciscoisesdk.
        api.v3_1_patch_1.radius_server_sequence.
        RadiusServerSequence.get_radius_server_sequence_generator>`_
        """
        yield from get_next_page(
            self.get_radius_server_sequence, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_radius_server_sequence(self,
                                      before_accept_attr_manipulators_list=None,
                                      continue_authorz_policy=None,
                                      description=None,
                                      local_accounting=None,
                                      name=None,
                                      on_request_attr_manipulator_list=None,
                                      prefix_separator=None,
                                      radius_server_list=None,
                                      remote_accounting=None,
                                      strip_prefix=None,
                                      strip_suffix=None,
                                      suffix_separator=None,
                                      use_attr_set_before_acc=None,
                                      use_attr_set_on_request=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """This API creates a RADIUS server sequence.

        Args:
            before_accept_attr_manipulators_list(list): The
                beforeAcceptAttrManipulators is required
                only if useAttrSetBeforeAcc is true,
                property of the request body (list of
                objects).
            on_request_attr_manipulator_list(list): The
                onRequestAttrManipulators is required
                only if useAttrSetOnRequest is true,
                property of the request body (list of
                objects).
            radius_server_list(list): RadiusServerList, property of
                the request body (list of strings).
            continue_authorz_policy(boolean): continueAuthorzPolicy,
                property of the request body.
            description(string): description, property of the
                request body.
            local_accounting(boolean): localAccounting, property of
                the request body.
            name(string): name, property of the request body.
            prefix_separator(string): The prefixSeparator is
                required only if stripPrefix is true.
                The maximum length is 1 character,
                property of the request body.
            remote_accounting(boolean): remoteAccounting, property
                of the request body.
            strip_prefix(boolean): stripPrefix, property of the
                request body.
            strip_suffix(boolean): stripSuffix, property of the
                request body.
            suffix_separator(string): The suffixSeparator is
                required only if stripSuffix is true.
                The maximum length is 1 character,
                property of the request body.
            use_attr_set_before_acc(boolean): useAttrSetBeforeAcc,
                property of the request body.
            use_attr_set_on_request(boolean): useAttrSetOnRequest,
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
                'description':
                    description,
                'stripPrefix':
                    strip_prefix,
                'stripSuffix':
                    strip_suffix,
                'prefixSeparator':
                    prefix_separator,
                'suffixSeparator':
                    suffix_separator,
                'remoteAccounting':
                    remote_accounting,
                'localAccounting':
                    local_accounting,
                'useAttrSetOnRequest':
                    use_attr_set_on_request,
                'useAttrSetBeforeAcc':
                    use_attr_set_before_acc,
                'continueAuthorzPolicy':
                    continue_authorz_policy,
                'RadiusServerList':
                    radius_server_list,
                'OnRequestAttrManipulatorList':
                    on_request_attr_manipulator_list,
                'BeforeAcceptAttrManipulatorsList':
                    before_accept_attr_manipulators_list,
            }
            _payload = {
                'RadiusServerSequence': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ad6ca0642c5750af6ca9905721a9d7_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/radiusserversequence')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ad6ca0642c5750af6ca9905721a9d7_v3_1_patch_1', _api_response)

    def create(self,
               before_accept_attr_manipulators_list=None,
               continue_authorz_policy=None,
               description=None,
               local_accounting=None,
               name=None,
               on_request_attr_manipulator_list=None,
               prefix_separator=None,
               radius_server_list=None,
               remote_accounting=None,
               strip_prefix=None,
               strip_suffix=None,
               suffix_separator=None,
               use_attr_set_before_acc=None,
               use_attr_set_on_request=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_radius_server_sequence <#ciscoisesdk.
        api.v3_1_patch_1.radius_server_sequence.
        RadiusServerSequence.create_radius_server_sequence>`_
        """
        return self.create_radius_server_sequence(
            before_accept_attr_manipulators_list=before_accept_attr_manipulators_list,
            continue_authorz_policy=continue_authorz_policy,
            description=description,
            local_accounting=local_accounting,
            name=name,
            on_request_attr_manipulator_list=on_request_attr_manipulator_list,
            prefix_separator=prefix_separator,
            radius_server_list=radius_server_list,
            remote_accounting=remote_accounting,
            strip_prefix=strip_prefix,
            strip_suffix=strip_suffix,
            suffix_separator=suffix_separator,
            use_attr_set_before_acc=use_attr_set_before_acc,
            use_attr_set_on_request=use_attr_set_on_request,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the RADIUS server sequence.

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

        e_url = ('/ers/config/radiusserversequence/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fb1a72ded19590fa0aa85fc59ea8cfc_v3_1_patch_1', _api_response)
