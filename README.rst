=============
ciscoisesdk
=============

**ciscoisesdk** is a *community developed* Python library for working with the Identity Services Engine APIs. 
Our goal is to make working with Cisco Identity Services Engine in Python a *native* and *natural* experience!

.. code-block:: python

    from ciscoisesdk import IdentityServicesEngineAPI
    from ciscoisesdk.exceptions import ApiError

    # Create a IdentityServicesEngineAPI connection object;
    # it uses ISE custom URL, username, and password, with ISE API version 3.1_Patch_1
    # and its API Gateway enabled,
    # verify=True to verify the server's TLS certificate
    # with debug logs disabled
    # and without using the CSRF token
    api = IdentityServicesEngineAPI(username='admin',
                                    password='C1sco12345',
                                    uses_api_gateway=True,
                                    base_url='https://198.18.133.27',
                                    version='3.1_Patch_1',
                                    verify=True,
                                    debug=False,
                                    uses_csrf_token=False)
    # NOTE: This collection assumes that the ERS APIs and OpenAPIs are enabled.

    # Get allowed protocols (first page)
    search_result = api.allowed_protocols.get_all().response.SearchResult
    if search_result and search_result.resources:
      for resource in search_result.resources:
        resource_detail = api.allowed_protocols.get_by_id(
                            resource.id
                          ).response.AllowedProtocols
        print("Id {}\nName {}\nallowChap {}\n".format(resource_detail.id,
                                                      resource_detail.name,
                                                      resource_detail.allowChap))
    print("----------")

    # Handle pagination with a generator
    allowed_protols_gen = api.allowed_protocols.get_all_generator()
    for allowed_protocols_page_resp in allowed_protols_gen:
      allowed_protols_result = allowed_protocols_page_resp.response.SearchResult
      for resource in allowed_protols_result.resources:
        resource_detail = api.allowed_protocols.get_by_id(
                            resource.id
                          ).response.AllowedProtocols
        print("Id {}\nName {}\nallowChap {}\n".format(resource_detail.id,
                                                      resource_detail.name,
                                                      resource_detail.allowChap))

    # Create network device
    try:
        network_device_response = api.network_device.create(
                                    name='ISE_EST_Local_Host_19',
                                    network_device_iplist=[{"ipaddress": "127.35.0.1", "mask": 32}])
        print("Created, new Location {}".format(network_device_response.headers.Location))
    except ApiError as e:
        print(e)

    # Filter network device
    device_list_response = api.network_device.get_all(filter='name.EQ.ISE_EST_Local_Host_19')
    device_responses = device_list_response.response.SearchResult.resources
    if len(device_responses) > 0:
        device_response = device_responses[0]

        # Get network device detail
        device_response_detail = api.network_device.get_by_id(device_response.id).response.NetworkDevice

    # Advance usage example using Custom Caller functions
    ## Define a Custom caller named function
    ## Call them with:
    ##    get_created_result(network_device_response.headers.Location)
    def get_created_result(location):
        return api.custom_caller.call_api('GET', location)

    ## Define the get_created_result function
    ## under the custom_caller wrapper.
    ## Call them with:
    ##    api.custom_caller.get_created_result(network_device_response.headers.Location)
    def setup_custom():
        api.custom_caller.add_api('get_created_result',
                                    lambda location:
                                    api.custom_caller.call_api('GET', location)
                                  )

    # Add the custom API calls to the connection object under the custom_caller wrapper
    setup_custom()

    # Call the newly added functions
    created_device_1 = get_created_result(network_device_response.headers.Location)
    created_device_2 = api.custom_caller.get_created_result(network_device_response.headers.Location)
    print(created_device_1.response == created_device_2.response)

    if len(device_responses) > 0:
        device_response = device_responses[0]

        # Delete network device
        delete_device = api.network_device.delete_by_id(device_response.id)



Introduction_


Installation
------------

Installing and upgrading ciscoisesdk is easy:

**Install via PIP**

.. code-block:: bash

    $ pip install ciscoisesdk

**Upgrading to the latest Version**

.. code-block:: bash

    $ pip install ciscoisesdk --upgrade


Documentation
-------------

**Excellent documentation is now available at:**
https://ciscoisesdk.readthedocs.io

Check out the Quickstart_ to dive in and begin using ciscoisesdk.


Release Notes
-------------

Please see the releases_ page for release notes on the incremental functionality and bug fixes incorporated into the published releases.


Questions, Support & Discussion
-------------------------------

ciscoisesdk is a *community developed* and *community supported* project.  If you experience any issues using this package, please report them using the issues_ page.


Contribution
------------

ciscoisesdk_ is a community development projects.  Feedback, thoughts, ideas, and code contributions are welcome!  Please see the `Contributing`_ guide for more information.


Inspiration
------------

This library is inspired by the webexteamssdk_  library

Change log
----------

All notable changes to this project will be documented in the CHANGELOG_ file.

The development team may make additional name changes as the library evolves with the ISE APIs.


*Copyright (c) 2021 Cisco and/or its affiliates.*

.. _Introduction: https://ciscoisesdk.readthedocs.io/en/latest/api/intro.html
.. _ciscoisesdk.readthedocs.io: https://ciscoisesdk.readthedocs.io
.. _Quickstart: https://ciscoisesdk.readthedocs.io/en/latest/api/quickstart.html
.. _ciscoisesdk: https://github.com/CiscoISE/ciscoisesdk
.. _issues: https://github.com/CiscoISE/ciscoisesdk/issues
.. _pull requests: https://github.com/CiscoISE/ciscoisesdk/pulls
.. _releases: https://github.com/CiscoISE/ciscoisesdk/releases
.. _the repository: ciscoisesdk_
.. _pull request: `pull requests`_
.. _Contributing: https://github.com/CiscoISE/ciscoisesdk/blob/master/docs/contributing.rst
.. _webexteamssdk: https://github.com/CiscoDevNet/webexteamssdk
.. _CHANGELOG: https://github.com/CiscoISE/ciscoisesdk/blob/main/CHANGELOG.md
