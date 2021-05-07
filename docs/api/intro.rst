.. _Introduction:

============
Introduction
============


Work with the Identity Services Engine APIs in Native Python!
-------------------------------------------------------------

Sure, working with the Identity Services Engine APIs is easy (see
`api_docs`_).  They are RESTful,  naturally structured,
require only a simple Access Token for authentication, and the data is
elegantly represented in intuitive JSON.  What could be easier?

.. code-block:: python

    import requests

    URL = 'https://dcloud-dna-ise-rtp.cisco.com/ers/config/networkdevice' 
    ACCESS_TOKEN = '<your_access_token>'

    filter_query = '<filter_query>'
    headers = {'authorization': ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    params_data = { 'filter': filter_query }
    response = requests.get(URL, params=params_data, headers=headers)
    if response.status_code == 200:
        device_response = response.json
        if device_response.get('SearchResult') and device_response['SearchResult'].get('resources'):
        for device in device_response['SearchResult']['resources']:
            print('{:20s}{}'.format(device['id'], device['name']))
    else:
        # Oops something went wrong...  Better do something about it.
        print(response.status_code, response.text)

Like I said, EASY.  However, in use, the code can become rather repetitive...

- You have to setup the environment every time
- You have to remember URLs, request parameters and JSON formats
  (or reference the docs)
- You have to parse the returned JSON and work with multiple layers of list
  and dictionary indexes


Enter **ciscoisesdk**, a simple API wrapper that wraps all of the Identity Services Engine API
calls and returned JSON objects within native Python objects and methods.

With ciscoisesdk, the above Python code can be consolidated to the following:

.. code-block:: python

    from ciscoisesdk import api

    api_ = api.IdentityServicesEngineAPI(base_url='https://dcloud-dna-ise-rtp.cisco.com', version='3.0.0')
    # Or even just api_ = api.IdentityServicesEngineAPI() as base_url and version have those values.
    try:
        device_response = api_.network_device.networkdevice(filter='name.EQ.Test').response
        if device_response.SearchResult and device_response.SearchResult.resources:
            for device in device_response.SearchResult.resources:
                print('{:20s}{}'.format(device.hostname, device.upTime))
    except ApiError as e:
        print(e)


**ciscoisesdk handles all of this for you:**

+ Reads your Identity Services Engine credentials from environment variables (IDENTITY_SERVICES_ENGINE_ENCODED_AUTH, IDENTITY_SERVICES_ENGINE_USERNAME, IDENTITY_SERVICES_ENGINE_PASSWORD)

+ Reads your Identity Services Engine API version from environment variable IDENTITY_SERVICES_ENGINE_VERSION. Supported versions: 3.0.0. Now with version and base_url, you have more control.

+ Controls whether to verify the server's TLS certificate or not according to the verify parameter.

+ Reads your Identity Services Engine debug from environment variable IDENTITY_SERVICES_ENGINE_DEBUG. Boolean, it controls whether to log information about Identity Services Engine APIs' request and response process.

+ Wraps and represents all Identity Services Engine API calls as a simple hierarchical tree of
  native-Python methods (with default arguments provided everywhere possible!)

+ If your Python IDE supports **auto-completion** (like PyCharm_), you can
  navigate the available methods and object attributes right within your IDE

+ Represents all returned JSON objects as native Python objects - you can
  access all of the object's attributes using native *dot.syntax*

+ **Automatic Rate-Limit Handling**  Sending a lot of requests to Identity Services Engine?
  Don't worry; we have you covered.  Identity Services Engine will respond with a rate-limit
  response, which will automatically be caught and "handled" for you.  Your
  requests and script will automatically be "paused" for the amount of time
  specified by Identity Services Engine, while we wait for the Identity Services Engine rate-limit timer to cool
  down.  After the cool-down, your request will automatically be retried, and
  your script will continue to run as normal.  Handling all of this requires
  zero (0) changes to your code - you're welcome.  😎

  Just know that if you are are sending a lot of requests, your script might
  take longer to run if your requests are getting rate limited.


All of this, combined, lets you do powerful things simply:

.. code-block:: python

    from ciscoisesdk import IdentityServicesEngineAPI
    from ciscoisesdk.exceptions import ApiError

    # Get allowed protocols
    search_result = api_.allowed_protocols.allowedprotocols().response.SearchResult
    if search_result and search_result.resources:
      for resource in search_result.resources:
        resource_detail = api_.allowed_protocols.allowedprotocols_by_id(resource.id).response.AllowedProtocols
        print("Id {}\nName {}\nallowChap {}\n".format(resource_detail.id, resource_detail.name, resource_detail.allowChap))

    # Filter network device
    device_list_response = api_.network_device.networkdevice(filter='name.EQ.ISE_EST_Local_Host_19')
    device_responses = device_list_response.response.SearchResult.resources
    device_response = device_responses[0]

    # Get network device detail
    device_response_detail = api_.network_device.networkdevice_by_id(device_response.id).response.NetworkDevice

    # Delete network device
    delete_device = api_.network_device.delete_networkdevice_by_id(device_response.id)

    # Create network device
    try:
        network_device_response = api_.network_device.create_networkdevice(name='ISE_EST_Local_Host_19', network_device_iplist=[{"ipaddress": "127.35.0.1", "mask": 32}])
        print("Created, new Location {}".format(network_device_response.headers.Location))
    except api_Error as e:
        print(e)

Head over to the :ref:`Quickstart` page to begin working with the
**Identity Services Engine APIs in native Python**!


.. _MITLicense:

MIT License
-----------

ciscoisesdk is currently licensed under the `MIT Open Source License`_, and
distributed as a source distribution (no binaries) via :ref:`PyPI <Install>`,
and the complete :ref:`source code <Source Code>` is available on GitHub.

ciscoisesdk License
-------------------

.. include:: ../../LICENSE


*Copyright (c) 2021 Cisco and/or its affiliates.*


.. _MIT Open Source License: https://opensource.org/licenses/MIT
.. _api_docs: https://developer.cisco.com/docs/identity-services-engine/3.0/#!cisco-ise-api-documentation
.. _PyCharm: https://www.jetbrains.com/pycharm/
