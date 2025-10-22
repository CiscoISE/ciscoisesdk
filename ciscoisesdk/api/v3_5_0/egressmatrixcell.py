# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine egressmatrixcell API wrapper.

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


class Egressmatrixcell(object):
    """Identity Services Engine egressmatrixcell API (version: 3.5.0).

    Wraps the Identity Services Engine egressmatrixcell
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Egressmatrixcell
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Egressmatrixcell, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_egressmatrixcell(self,
                             filter=None,
                             page=None,
                             size=None,
                             sortasc=None,
                             sortdsc=None,
                             headers=None,
                             **query_parameters):
        """Get-All.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[sgtSrcValue, matrixStatus,
                description, matrixId, sgtSrcName,
                sgtDstName, sgtDstValue].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[description, sgtSrcName,
                sgtDstName, sgtDstValue].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[description, sgtSrcName,
                sgtDstName, sgtDstValue].
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
        check_type(filter, str)
        check_type(page, (int, str, list))
        check_type(size, (int, str, list))
        check_type(sortdsc, str)
        check_type(sortasc, str)

        _params = {
            'filter':
                filter,
            'page':
                page,
            'size':
                size,
            'sortdsc':
                sortdsc,
            'sortasc':
                sortasc,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/egressmatrixcell/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ee335fbe810c5a7b95d569e72218e548_v3_5_0', _api_response)

    def get_egressmatrixcell_generator(self,
                                       filter=None,
                                       page=None,
                                       size=None,
                                       sortasc=None,
                                       sortdsc=None,
                                       headers=None,
                                       **query_parameters):
        """Get-All.

        Args:
            filter(str): filter query parameter. Filter Supported
                Fields:[sgtSrcValue, matrixStatus,
                description, matrixId, sgtSrcName,
                sgtDstName, sgtDstValue].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[description, sgtSrcName,
                sgtDstName, sgtDstValue].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[description, sgtSrcName,
                sgtDstName, sgtDstValue].
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.

              + RestResponse: REST response with following properties:

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

        yield from get_next_page(
            self.get_egressmatrixcell, dict(
                filter=filter,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_egressmatrixcell(self,
                                default_rule=None,
                                description=None,
                                destination_sgt_id=None,
                                id=None,
                                matrix_cell_status=None,
                                matrix_id=None,
                                name=None,
                                sgacls=None,
                                source_sgt_id=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Create.

        Args:
            default_rule(string): allowed
                values:NONE,DENY_IP,PERMIT_IP, property
                of the request body.
            description(string): Description, property of the
                request body.
            destination_sgt_id(string): destinationSgtId, property
                of the request body.
            id(string): Id, property of the request body.
            matrix_cell_status(string): Allowed
                values:DISABLED,ENABLED,MONITOR,
                property of the request body.
            matrix_id(string): Default value is Production Matrix
                Id, when no value is provided during
                creation. To use it as filter, the
                values should be an UUID of a Matrix.
                The values are case sensitive. For
                example, '[ERSObjectURL]?filter=matrixId
                .eq.ccf9a6ea-153b-4056-b8f4-
                0dc17eca4d30', property of the request
                body.
            name(string): name, property of the request body.
            sgacls(list): sgacls, property of the request body (list
                of any objects).
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
            _tmp_payload = {
                'defaultRule':
                    default_rule,
                'destinationSgtId':
                    destination_sgt_id,
                'matrixCellStatus':
                    matrix_cell_status,
                'sgacls':
                    sgacls,
                'sourceSgtId':
                    source_sgt_id,
                'matrixId':
                    matrix_id,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'EgressMatrixCell': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_a99601dbf5354bf841073fef22468d8_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/egressmatrixcell/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_a99601dbf5354bf841073fef22468d8_v3_5_0', _api_response)

    def update_egressmatrixcell_status(self,
                                       status,
                                       headers=None,
                                       **query_parameters):
        """Set All Cells Status.

        Args:
            status(str): status path parameter.
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
        check_type(status, str,
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

        return self._object_factory('bpm_f47f525dbd71ef49710ef578_v3_5_0', _api_response)

    def update_egressmatrixcell_clonecell_srcsgt_dstsgt_by_id(self,
                                                              dst_sgt_id,
                                                              id,
                                                              src_sgt_id,
                                                              headers=None,
                                                              **query_parameters):
        """Clone Cell.

        Args:
            id(str): id path parameter.
            src_sgt_id(str): srcSgtId path parameter.
            dst_sgt_id(str): dstSgtId path parameter.
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
        check_type(id, str,
                   may_be_none=False)
        check_type(src_sgt_id, str,
                   may_be_none=False)
        check_type(dst_sgt_id, str,
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

        return self._object_factory('bpm_a1e6c05d05e67906b3b59bbe6d274_v3_5_0', _api_response)

    def update_egressmatrixcell_clearallmatrixcells(self,
                                                    headers=None,
                                                    **query_parameters):
        """Clear All Matrix Cells.

        Args:
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

        return self._object_factory('bpm_f503ab54e2921d713ed88f51c9_v3_5_0', _api_response)

    def get_egressmatrixcell_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """Get-By-Id.

        Args:
            id(str): id path parameter.
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
        check_type(id, str,
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

        return self._object_factory('bpm_cdc971b23285b87945021bd5983d1cd_v3_5_0', _api_response)

    def update_egressmatrixcell_by_id(self,
                                      id,
                                      default_rule=None,
                                      description=None,
                                      destination_sgt_id=None,
                                      matrix_cell_status=None,
                                      matrix_id=None,
                                      name=None,
                                      sgacls=None,
                                      source_sgt_id=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """Update.

        Args:
            default_rule(string): allowed
                values:NONE,DENY_IP,PERMIT_IP, property
                of the request body.
            description(string): Description, property of the
                request body.
            destination_sgt_id(string): destinationSgtId, property
                of the request body.
            id(string): Id, property of the request body.
            matrix_cell_status(string): Allowed
                values:DISABLED,ENABLED,MONITOR,
                property of the request body.
            matrix_id(string): Default value is Production Matrix
                Id, when no value is provided during
                creation. To use it as filter, the
                values should be an UUID of a Matrix.
                The values are case sensitive. For
                example, '[ERSObjectURL]?filter=matrixId
                .eq.ccf9a6ea-153b-4056-b8f4-
                0dc17eca4d30', property of the request
                body.
            name(string): name, property of the request body.
            sgacls(list): sgacls, property of the request body (list
                of any objects).
            source_sgt_id(string): sourceSgtId, property of the
                request body.
            id(str): id path parameter.
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
            check_type(payload, str)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, str,
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
                'defaultRule':
                    default_rule,
                'destinationSgtId':
                    destination_sgt_id,
                'matrixCellStatus':
                    matrix_cell_status,
                'sgacls':
                    sgacls,
                'sourceSgtId':
                    source_sgt_id,
                'matrixId':
                    matrix_id,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'EgressMatrixCell': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ce83fba942c25938bae0c7012df68317_v3_5_0')\
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

        return self._object_factory('bpm_ce83fba942c25938bae0c7012df68317_v3_5_0', _api_response)

    def delete_egressmatrixcell_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """Delete.

        Args:
            id(str): id path parameter.
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
        check_type(id, str,
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

        return self._object_factory('bpm_e4393915121d5bcc94dfde6c8f6f7f1c_v3_5_0', _api_response)
