# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine restidstore API wrapper.

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


class Restidstore(object):
    """Identity Services Engine restidstore API (version: 3.5.0).

    Wraps the Identity Services Engine restidstore
    API and exposes the API as native Python
    methods that return native Python objects.


    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Restidstore
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Restidstore, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_restidstore(self,
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
                Fields:[name].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name].
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

        e_url = ('/ers/config/restidstore/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ec1cd0e95e96ad1204b5b2dfee1a_v3_5_0', _api_response)

    def get_restidstore_generator(self,
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
                Fields:[name].
            page(int): page query parameter. Page Number (0...N).
            size(int): size query parameter. Items by Page.
            sortdsc(str): sortdsc query parameter. Sorting Supported
                Fields:[name].
            sortasc(str): sortasc query parameter. Sorting Supported
                Fields:[name].
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
            self.get_restidstore, dict(
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

    def create_restidstore(self,
                           description=None,
                           ers_rest_idstore_advance_settings=None,
                           ers_rest_idstore_attributes=None,
                           ers_rest_idstore_device_attributes=None,
                           ers_rest_idstore_user_attributes=None,
                           id=None,
                           name=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **query_parameters):
        """Create.

        Args:
            description(string): Description, property of the
                request body.
            ers_rest_idstore_advance_settings(object):
                ersRestIDStoreAdvanceSettings, property
                of the request body.
            ers_rest_idstore_attributes(object):
                ersRestIDStoreAttributes, property of
                the request body.
            ers_rest_idstore_device_attributes(object):
                ersRestIDStoreDeviceAttributes, property
                of the request body.
            ers_rest_idstore_user_attributes(object):
                ersRestIDStoreUserAttributes, property
                of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'ersRestIDStoreAttributes':
                    ers_rest_idstore_attributes,
                'ersRestIDStoreUserAttributes':
                    ers_rest_idstore_user_attributes,
                'ersRestIDStoreDeviceAttributes':
                    ers_rest_idstore_device_attributes,
                'ersRestIDStoreAdvanceSettings':
                    ers_rest_idstore_advance_settings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSRestIDStore': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ccb1fa524db3f37254b3f67c83_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/restidstore/')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ccb1fa524db3f37254b3f67c83_v3_5_0', _api_response)

    def get_restidstore_name_by_name(self,
                                     name,
                                     headers=None,
                                     **query_parameters):
        """Get-By-Name.

        Args:
            name(str): name path parameter.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/ers/config/restidstore/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c47e28f13659658b3e6af9409a1177_v3_5_0', _api_response)

    def update_restidstore_name_by_name(self,
                                        name,
                                        description=None,
                                        ers_rest_idstore_advance_settings=None,
                                        ers_rest_idstore_attributes=None,
                                        ers_rest_idstore_device_attributes=None,
                                        ers_rest_idstore_user_attributes=None,
                                        id=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **query_parameters):
        """Update-By-Name.

        Args:
            description(string): Description, property of the
                request body.
            ers_rest_idstore_advance_settings(object):
                ersRestIDStoreAdvanceSettings, property
                of the request body.
            ers_rest_idstore_attributes(object):
                ersRestIDStoreAttributes, property of
                the request body.
            ers_rest_idstore_device_attributes(object):
                ersRestIDStoreDeviceAttributes, property
                of the request body.
            ers_rest_idstore_user_attributes(object):
                ersRestIDStoreUserAttributes, property
                of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            name(str): name path parameter.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'ersRestIDStoreAttributes':
                    ers_rest_idstore_attributes,
                'ersRestIDStoreUserAttributes':
                    ers_rest_idstore_user_attributes,
                'ersRestIDStoreDeviceAttributes':
                    ers_rest_idstore_device_attributes,
                'ersRestIDStoreAdvanceSettings':
                    ers_rest_idstore_advance_settings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSRestIDStore': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d0e432f52e2a5863858c7dc0c3eda277_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/restidstore/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d0e432f52e2a5863858c7dc0c3eda277_v3_5_0', _api_response)

    def delete_restidstore_name_by_name(self,
                                        name,
                                        headers=None,
                                        **query_parameters):
        """Delete-By-Name.

        Args:
            name(str): name path parameter.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/ers/config/restidstore/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fe53fb8359725e40ac431d41e1487626_v3_5_0', _api_response)

    def patch_restidstore_name_by_name(self,
                                       name,
                                       description=None,
                                       ers_rest_idstore_advance_settings=None,
                                       ers_rest_idstore_attributes=None,
                                       ers_rest_idstore_device_attributes=None,
                                       ers_rest_idstore_user_attributes=None,
                                       id=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            description(string): Description, property of the
                request body.
            ers_rest_idstore_advance_settings(object):
                ersRestIDStoreAdvanceSettings, property
                of the request body.
            ers_rest_idstore_attributes(object):
                ersRestIDStoreAttributes, property of
                the request body.
            ers_rest_idstore_device_attributes(object):
                ersRestIDStoreDeviceAttributes, property
                of the request body.
            ers_rest_idstore_user_attributes(object):
                ersRestIDStoreUserAttributes, property
                of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
            name(str): name path parameter.
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
        check_type(name, str,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'ersRestIDStoreAttributes':
                    ers_rest_idstore_attributes,
                'ersRestIDStoreUserAttributes':
                    ers_rest_idstore_user_attributes,
                'ersRestIDStoreDeviceAttributes':
                    ers_rest_idstore_device_attributes,
                'ersRestIDStoreAdvanceSettings':
                    ers_rest_idstore_advance_settings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSRestIDStore': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fced674832255f00b1d01cd38d378bf1_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/restidstore/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_fced674832255f00b1d01cd38d378bf1_v3_5_0', _api_response)

    def get_restidstore_by_id(self,
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

        e_url = ('/ers/config/restidstore/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cba3f7ace597da668acfbe00364be_v3_5_0', _api_response)

    def update_restidstore_by_id(self,
                                 id,
                                 description=None,
                                 ers_rest_idstore_advance_settings=None,
                                 ers_rest_idstore_attributes=None,
                                 ers_rest_idstore_device_attributes=None,
                                 ers_rest_idstore_user_attributes=None,
                                 name=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **query_parameters):
        """Update.

        Args:
            description(string): Description, property of the
                request body.
            ers_rest_idstore_advance_settings(object):
                ersRestIDStoreAdvanceSettings, property
                of the request body.
            ers_rest_idstore_attributes(object):
                ersRestIDStoreAttributes, property of
                the request body.
            ers_rest_idstore_device_attributes(object):
                ersRestIDStoreDeviceAttributes, property
                of the request body.
            ers_rest_idstore_user_attributes(object):
                ersRestIDStoreUserAttributes, property
                of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'ersRestIDStoreAttributes':
                    ers_rest_idstore_attributes,
                'ersRestIDStoreUserAttributes':
                    ers_rest_idstore_user_attributes,
                'ersRestIDStoreDeviceAttributes':
                    ers_rest_idstore_device_attributes,
                'ersRestIDStoreAdvanceSettings':
                    ers_rest_idstore_advance_settings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSRestIDStore': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ded7f8573c255c318bb1f04bfdbf01e1_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/restidstore/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_ded7f8573c255c318bb1f04bfdbf01e1_v3_5_0', _api_response)

    def delete_restidstore_by_id(self,
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

        e_url = ('/ers/config/restidstore/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e77a1dd4aa75dcebbc3ee4e94a162b4_v3_5_0', _api_response)

    def patch_restidstore_by_id(self,
                                id,
                                description=None,
                                ers_rest_idstore_advance_settings=None,
                                ers_rest_idstore_attributes=None,
                                ers_rest_idstore_device_attributes=None,
                                ers_rest_idstore_user_attributes=None,
                                name=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """Update any attribute subset. Only attributes that sent will be
        affected.

        Args:
            description(string): Description, property of the
                request body.
            ers_rest_idstore_advance_settings(object):
                ersRestIDStoreAdvanceSettings, property
                of the request body.
            ers_rest_idstore_attributes(object):
                ersRestIDStoreAttributes, property of
                the request body.
            ers_rest_idstore_device_attributes(object):
                ersRestIDStoreDeviceAttributes, property
                of the request body.
            ers_rest_idstore_user_attributes(object):
                ersRestIDStoreUserAttributes, property
                of the request body.
            id(string): Id, property of the request body.
            name(string): name, property of the request body.
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
                'ersRestIDStoreAttributes':
                    ers_rest_idstore_attributes,
                'ersRestIDStoreUserAttributes':
                    ers_rest_idstore_user_attributes,
                'ersRestIDStoreDeviceAttributes':
                    ers_rest_idstore_device_attributes,
                'ersRestIDStoreAdvanceSettings':
                    ers_rest_idstore_advance_settings,
                'name':
                    name,
                'id':
                    id,
                'description':
                    description,
            }
            _payload = {
                'ERSRestIDStore': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fe2adcd154a1862a3400b89a52b7_v3_5_0')\
                .validate(_payload)

        e_url = ('/ers/config/restidstore/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                headers=_headers,
                                                **request_params)
        else:
            _api_response = self._session.patch(endpoint_full_url, params=_params,
                                                **request_params)

        return self._object_factory('bpm_fe2adcd154a1862a3400b89a52b7_v3_5_0', _api_response)
