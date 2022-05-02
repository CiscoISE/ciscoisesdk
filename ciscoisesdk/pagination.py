# -*- coding: utf-8 -*-
"""Functions that deal with ISE pagination.

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

from future import standard_library

standard_library.install_aliases()
native_str = str
import urllib.parse

from .exceptions import ApiError


def get_next_page_number(page_param):
    next_page_number = 0
    if isinstance(page_param, list):
        if len(page_param) > 0:
            page_param = page_param[0]
    if isinstance(page_param, str):
        try:
            next_page_number = int(page_param)
        except ValueError:
            next_page_number = 0
    elif isinstance(page_param, int):
        next_page_number = page_param
    next_page_number = (next_page_number or 1) + 1
    return next_page_number


def get_next_page(function, params, access_next_list=["SearchResult", "nextPage", "href"],
                  access_resource_list=["SearchResult", "resources"],
                  has_been_found=None, prev_result=None):
    """
    Args:
        function(function): The API function to call
        params(dict): The parameters of the function
        access_next_list(list): List of strings. Allows to access the URL for the next page using the previous response object
        access_resource_list(list): List of strings. Allows to access the response object

    Yields:
        Generator: A generator object containing the RestResponse objects for all pages.

    """
    response = function(**params)
    if response.response:
        result = response.response
        value = response.response
        items_found = 0
        for access_next in access_next_list:
            if isinstance(value, dict) and value.get(access_next) is not None:
                value = value.get(access_next)
                items_found = items_found + 1
            else:
                items_found = 0
                break
        found = isinstance(value, str) and len(access_next_list) == items_found
        if has_been_found is None:
            has_been_found = found

        for access_resource in access_resource_list:
            if isinstance(result, dict) and result.get(access_resource) is not None:
                result = result.get(access_resource)

        if prev_result != result:
            prev_result = result
            if not found:
                if isinstance(result, list) and not has_been_found:
                    if len(result) == 0:
                        yield response
                    else:
                        yield response
                        _params = dict(params)
                        if 'page' in params and 'size' in params:
                            _params['page'] = get_next_page_number(params['page'])
                        try:
                            yield from get_next_page(
                                function, {**_params},
                                access_next_list=access_next_list, access_resource_list=access_resource_list,
                                has_been_found=has_been_found, prev_result=prev_result)
                        except ApiError as e:
                            expected_status_codes = [400, 404, 500]
                            # If is not a 400 Bad Request and is not a 404 Not Found status code
                            if e.status_code not in expected_status_codes:
                                raise e
                else:
                    yield response
            else:
                yield response
                url = value
                _query_params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
                yield from get_next_page(
                    function, {**params, **_query_params},
                    access_next_list=access_next_list, access_resource_list=access_resource_list,
                    has_been_found=has_been_found, prev_result=prev_result)
