# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI custom_caller API fixtures and tests.

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

import pytest


@pytest.fixture(scope="session")
def custom_caller(api):
    api.custom_caller.add_api('get_hotspotportal',
                              lambda params: api.custom_caller.call_api(
                                  'GET',
                                  '/ers/config/hotspotportal',
                                  params)
                              )
    api.custom_caller.add_api('create_hotspotportal',
                              lambda hotspotportal: api.custom_caller.call_api(
                                  'POST',
                                  '/ers/config/hotspotportal',
                                  json={
                                      "HotspotPortal": hotspotportal
                                  })
                              )
    api.custom_caller.add_api('delete_hotspotportal_by_id',
                              lambda _id:
                                  api.custom_caller.call_api(
                                      'DELETE',
                                      '/ers/config/hotspotportal/{id}',
                                      path_params={
                                          'id': _id,
                                      })
                              )
    return api.custom_caller


@pytest.mark.custom_caller
def test_custom_caller(custom_caller):
    hotspotportal = custom_caller.get_hotspotportal(params={'filter': 'name.EQ.Hotspot Guest Portal'})
    assert hotspotportal.response is not None
    create_response = custom_caller.create_hotspotportal({
        'name': 'Hotspot Guest Portal (test)',
        'description': 'Hotspot Guest Portal for tests',
    })
    assert create_response.response is not None
    delete_response = custom_caller.delete_hotspotportal_by_id('string')
    assert delete_response is not None
