# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine EgressMatrixCell API wrapper.

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


class EgressMatrixCell(object):
    """Identity Services Engine EgressMatrixCell API (version: 3.1_Patch_1).

    Wraps the Identity Services Engine EgressMatrixCell
    API and exposes the API as native Python
    methods that return native Python objects.

    | Egress Policy Matrix Cell API allows the client to add, update, delete and search egress matrix cells among other operations.

    **Revision History**

    +----------------+----------------------+-----------------------+-----------------------------+---+
    | **Revision #** | **Resource Version** | **Cisco ISE Version** | **Description**             |   |
    +----------------+----------------------+-----------------------+-----------------------------+---+
    | 0              | 1.0                  | 2.0                   | Initial Cisco ISE Version   |   |
    +----------------+----------------------+-----------------------+-----------------------------+---+
    | 1              | 1.1                  | 2.3                   | Introducing bulk operations |   |
    +----------------+----------------------+-----------------------+-----------------------------+---+

    |

    **Resource Definition**

    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | **Attribute**    | **Type**  | **Required** | **Description**                            | **Default Values** | **Example Values**                       |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | name             | String    | Yes          | Resource Name                              |                    | ANY-ANY                                  |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | id               | String    | No           | Resource UUID, mandatory for update        |                    | f92c1a900-8c01-11e6-996c-525400b48521    |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | description      | String    | No           |                                            |                    | Default egress rule                      |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | defaultRule      | Enum      | Yes          | Allowed values: NONE, DENY_IP, PERMIT_IP   | NONE               | PERMIT_IP                                |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | destinationSgtId | String    | Yes          |                                            |                    | 92bb1950-8c01-11e6-996c-525400b48521     |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | matrixCellStatus | Enum      | Yes          | Allowed values: DISABLED, ENABLED, MONITOR | DISABLED           | ENABLED                                  |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | sgACLs           | List      | Yes          |                                            |                    | ["92951ac0-8c01-11e6-996c-525400b48521"] |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+
    | sourceSgtId      | String    | Yes          |                                            |                    | 92bb1950-8c01-11e6-996c-525400b48521     |
    +------------------+-----------+--------------+--------------------------------------------+--------------------+------------------------------------------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new EgressMatrixCell
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(EgressMatrixCell, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def clear_all_matrix_cells(self,
                               headers=None,
                               **query_parameters):
        """This API allows the client to clear all the egress matrix cells.

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

        e_url = ('/ers/config/egressmatrixcell/clearallmatrixcells')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f503ab54e2921d713ed88f51c9_v3_1_patch_1', _api_response)

    def clear(self,
              headers=None,
              **query_parameters):
        """Alias for `clear_all_matrix_cells <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.clear_all_matrix_cells>`_
        """
        return self.clear_all_matrix_cells(
            headers=headers,
            **query_parameters
        )

    def set_all_cells_status(self,
                             status,
                             headers=None,
                             **query_parameters):
        """This API allows the client to set status of all the egress
        matrix cells.

        Args:
            status(basestring): status path parameter.
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
        check_type(status, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'status': status,
        }

        e_url = ('/ers/config/egressmatrixcell/status/{status}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f47f525dbd71ef49710ef578_v3_1_patch_1', _api_response)

    def set_status(self,
                   status,
                   headers=None,
                   **query_parameters):
        """Alias for `set_all_cells_status <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.set_all_cells_status>`_
        """
        return self.set_all_cells_status(
            status=status,
            headers=headers,
            **query_parameters
        )

    def clone_matrix_cell(self,
                          dst_sgt_id,
                          id,
                          src_sgt_id,
                          headers=None,
                          **query_parameters):
        """This API allows the client to clone an egress matrix cell.

        Args:
            id(basestring): id path parameter.
            src_sgt_id(basestring): srcSgtId path parameter.
            dst_sgt_id(basestring): dstSgtId path parameter.
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
        check_type(src_sgt_id, basestring,
                   may_be_none=False)
        check_type(dst_sgt_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
            'srcSgtId': src_sgt_id,
            'dstSgtId': dst_sgt_id,
        }

        e_url = ('/ers/config/egressmatrixcell/clonecell/{id}/srcSgt/{srcS'
                 + 'gtId}/dstSgt/{dstSgtId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1e6c05d05e67906b3b59bbe6d274_v3_1_patch_1', _api_response)

    def clone(self,
              dst_sgt_id,
              id,
              src_sgt_id,
              headers=None,
              **query_parameters):
        """Alias for `clone_matrix_cell <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.clone_matrix_cell>`_
        """
        return self.clone_matrix_cell(
            dst_sgt_id=dst_sgt_id,
            id=id,
            src_sgt_id=src_sgt_id,
            headers=headers,
            **query_parameters
        )

    def get_egress_matrix_cell_by_id(self,
                                     id,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to get an egress matrix cell by ID.

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

        e_url = ('/ers/config/egressmatrixcell/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cdc971b23285b87945021bd5983d1cd_v3_1_patch_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_egress_matrix_cell_by_id <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.get_egress_matrix_cell_by_id>`_
        """
        return self.get_egress_matrix_cell_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_egress_matrix_cell_by_id(self,
                                        id,
                                        default_rule=None,
                                        description=None,
                                        destination_sgt_id=None,
                                        matrix_cell_status=None,
                                        name=None,
                                        sgacls=None,
                                        source_sgt_id=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **query_parameters):
        """This API allows the client to update an egress matrix cell.

        Args:
            default_rule(string): Allowed values: NONE, DENY_IP,
                PERMIT_IP, property of the request body.
            description(string): description, property of the
                request body.
            destination_sgt_id(string): destinationSgtId, property
                of the request body.
            id(string): id, property of the request body.
            matrix_cell_status(string): Allowed values: DISABLED,
                ENABLED, MONITOR, property of the
                request body.
            name(string): name, property of the request body.
            sgacls(list): sgacls, property of the request body (list
                of strings).
            source_sgt_id(string): sourceSgtId, property of the
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
                'sourceSgtId':
                    source_sgt_id,
                'destinationSgtId':
                    destination_sgt_id,
                'matrixCellStatus':
                    matrix_cell_status,
                'defaultRule':
                    default_rule,
                'sgacls':
                    sgacls,
            }
            _payload = {
                'EgressMatrixCell': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ce83fba942c25938bae0c7012df68317_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/egressmatrixcell/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_ce83fba942c25938bae0c7012df68317_v3_1_patch_1', _api_response)

    def update_by_id(self,
                     id,
                     default_rule=None,
                     description=None,
                     destination_sgt_id=None,
                     matrix_cell_status=None,
                     name=None,
                     sgacls=None,
                     source_sgt_id=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_egress_matrix_cell_by_id <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.update_egress_matrix_cell_by_id>`_
        """
        return self.update_egress_matrix_cell_by_id(
            id=id,
            default_rule=default_rule,
            description=description,
            destination_sgt_id=destination_sgt_id,
            matrix_cell_status=matrix_cell_status,
            name=name,
            sgacls=sgacls,
            source_sgt_id=source_sgt_id,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_egress_matrix_cell_by_id(self,
                                        id,
                                        headers=None,
                                        **query_parameters):
        """This API deletes an egress matrix cell.

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

        e_url = ('/ers/config/egressmatrixcell/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e4393915121d5bcc94dfde6c8f6f7f1c_v3_1_patch_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_egress_matrix_cell_by_id <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.delete_egress_matrix_cell_by_id>`_
        """
        return self.delete_egress_matrix_cell_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_egress_matrix_cell(self,
                               filter=None,
                               filter_type=None,
                               page=None,
                               size=None,
                               sortasc=None,
                               sortdsc=None,
                               headers=None,
                               **query_parameters):
        """This API allows the client to get all the egress matrix cell.
        Filter:   [sgtSrcValue, matrixStatus, description,
        sgtSrcName, sgtDstName, sgtDstValue]   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [description, sgtSrcName, sgtDstName,
        sgtDstValue].

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

        e_url = ('/ers/config/egressmatrixcell')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c5e52706e7095a81b8d32f3024e01cf6_v3_1_patch_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_egress_matrix_cell <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.get_egress_matrix_cell>`_
        """
        return self.get_egress_matrix_cell(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_egress_matrix_cell_generator(self,
                                         filter=None,
                                         filter_type=None,
                                         page=None,
                                         size=None,
                                         sortasc=None,
                                         sortdsc=None,
                                         headers=None,
                                         **query_parameters):
        """This API allows the client to get all the egress matrix cell.
        Filter:   [sgtSrcValue, matrixStatus, description,
        sgtSrcName, sgtDstName, sgtDstValue]   To search
        resources by using  toDate  column,follow the format:
        DD-MON-YY (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [description, sgtSrcName, sgtDstName,
        sgtDstValue].

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
            self.get_egress_matrix_cell, dict(
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
        """Alias for `get_egress_matrix_cell_generator <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.get_egress_matrix_cell_generator>`_
        """
        yield from get_next_page(
            self.get_egress_matrix_cell, dict(
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

    def create_egress_matrix_cell(self,
                                  default_rule=None,
                                  description=None,
                                  destination_sgt_id=None,
                                  matrix_cell_status=None,
                                  name=None,
                                  sgacls=None,
                                  source_sgt_id=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **query_parameters):
        """This API creates an egress matrix cell.

        Args:
            default_rule(string): Allowed values: NONE, DENY_IP,
                PERMIT_IP, property of the request body.
            description(string): description, property of the
                request body.
            destination_sgt_id(string): destinationSgtId, property
                of the request body.
            matrix_cell_status(string): Allowed values: DISABLED,
                ENABLED, MONITOR, property of the
                request body.
            name(string): name, property of the request body.
            sgacls(list): sgacls, property of the request body (list
                of strings).
            source_sgt_id(string): sourceSgtId, property of the
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
                'sourceSgtId':
                    source_sgt_id,
                'destinationSgtId':
                    destination_sgt_id,
                'matrixCellStatus':
                    matrix_cell_status,
                'defaultRule':
                    default_rule,
                'sgacls':
                    sgacls,
            }
            _payload = {
                'EgressMatrixCell': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c560004d8b5f64a10f2cc070368c12_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/egressmatrixcell')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_c560004d8b5f64a10f2cc070368c12_v3_1_patch_1', _api_response)

    def create(self,
               default_rule=None,
               description=None,
               destination_sgt_id=None,
               matrix_cell_status=None,
               name=None,
               sgacls=None,
               source_sgt_id=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_egress_matrix_cell <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.create_egress_matrix_cell>`_
        """
        return self.create_egress_matrix_cell(
            default_rule=default_rule,
            description=description,
            destination_sgt_id=destination_sgt_id,
            matrix_cell_status=matrix_cell_status,
            name=name,
            sgacls=sgacls,
            source_sgt_id=source_sgt_id,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the egress matrix cell.

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

        e_url = ('/ers/config/egressmatrixcell/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c9da5c04b59358ac8bb1034340df4_v3_1_patch_1', _api_response)

    def bulk_request_for_egress_matrix_cell(self,
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
                'EgressMatrixCellBulkRequest': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_aa333658bf83576eb36a025283516518_v3_1_patch_1')\
                .validate(_payload)

        e_url = ('/ers/config/egressmatrixcell/bulk/submit')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_aa333658bf83576eb36a025283516518_v3_1_patch_1', _api_response)

    def bulk_request(self,
                     operation_type=None,
                     resource_media_type=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `bulk_request_for_egress_matrix_cell <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.bulk_request_for_egress_matrix_cell>`_
        """
        return self.bulk_request_for_egress_matrix_cell(
            operation_type=operation_type,
            resource_media_type=resource_media_type,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def monitor_bulk_status_egress_matrix_cell(self,
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

        e_url = ('/ers/config/egressmatrixcell/bulk/{bulkid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_face30e52b28c76c1b2574de858_v3_1_patch_1', _api_response)

    def monitor_bulk_status(self,
                            bulkid,
                            headers=None,
                            **query_parameters):
        """Alias for `monitor_bulk_status_egress_matrix_cell <#ciscoisesdk.
        api.v3_1_patch_1.egress_matrix_cell.
        EgressMatrixCell.monitor_bulk_status_egress_matrix_cell>`_
        """
        return self.monitor_bulk_status_egress_matrix_cell(
            bulkid=bulkid,
            headers=headers,
            **query_parameters
        )
