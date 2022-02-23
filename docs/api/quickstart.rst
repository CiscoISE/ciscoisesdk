.. _Quickstart:

.. currentmodule:: ciscoisesdk

==========
Quickstart
==========

*Dive in!*  ...to get started using the ciscoisesdk package:

Make sure that you have:

* ciscoisesdk :ref:`installed <Install>`
* ciscoisesdk :ref:`upgraded to the latest version <Upgrade>`

Pass your Identity Services Engine Access Token
-----------------------------------------------

To interact with the Identity Services Engine APIs, you must have a **Identity Services Engine Access Token**.
A Identity Services Engine Access Token is how the Identity Services Engine APIs validate access and identify the
requesting user.

As a `best practice`__, you can store your Identity Services Engine 'credentials' as
an environment variables in your development or production environment. 

By default, ciscoisesdk will look for the following environment variables to create new connection objects:

    * ``IDENTITY_SERVICES_ENGINE_DEBUG`` - Tells the SDK whether to log request and response information. Useful for debugging and seeing what is going on under the hood. Defaults to False.

    * ``IDENTITY_SERVICES_ENGINE_VERSION`` - Identity Services Engine API version to use. Defaults to '3.1.1'.

    * ``IDENTITY_SERVICES_ENGINE_ENCODED_AUTH`` - It takes priority. It is the `username:password` encoded in base 64.
      For example 'ZGV2bmV0dXNlcjpDaXNjbzEyMyEK' which decoded is 'devnetuser:Cisco123!'

    * ``IDENTITY_SERVICES_ENGINE_USERNAME`` - HTTP Basic Auth username.

    * ``IDENTITY_SERVICES_ENGINE_PASSWORD`` - HTTP Basic Auth password.

    * ``IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY`` - Enables or disables the usage of the API Gateway. Defaults to True.

    * ``IDENTITY_SERVICES_ENGINE_USES_CSRF_TOKEN`` - Enables or disables the usage of X-CSRF-Token. Defaults to False.
    
    * ``IDENTITY_SERVICES_ENGINE_BASE_URL`` - The base URL to be prefixed to the individual API endpoint suffixes. It is used if the IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY is True. Defaults to 'https://dcloud-dna-ise-rtp.cisco.com'.

    * ``IDENTITY_SERVICES_ENGINE_UI_BASE_URL`` - The UI base URL to be prefixed to the individual ISE UI API endpoint suffixes. It is used if the IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY is False.

    * ``IDENTITY_SERVICES_ENGINE_ERS_BASE_URL`` - The ERS base URL to be prefixed to the individual ISE ERS API endpoint suffixes. It is used if the IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY is False.

    * ``IDENTITY_SERVICES_ENGINE_MNT_BASE_URL`` - The MNT base URL to be prefixed to the individual ISE MNT API endpoint suffixes. It is used if the IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY is False.

    * ``IDENTITY_SERVICES_ENGINE_PX_GRID_BASE_URL`` - The PX_GRID base URL to be prefixed to the individual ISE PX_GRID API endpoint suffixes. It is used if the IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY is False.

    * ``IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT`` - Timeout (in seconds) for RESTful HTTP requests. Defaults to 60.

    * ``IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT`` - Enables or disables automatic rate-limit handling. Defaults to True.

    * ``IDENTITY_SERVICES_ENGINE_VERIFY`` - Controls whether to verify the server's TLS certificate or not. Defaults to True.

__ https://12factor.net/config


However, you choose to set it, if you have ``IDENTITY_SERVICES_ENGINE_VERSION``, ``IDENTITY_SERVICES_ENGINE_USERNAME`` and ``IDENTITY_SERVICES_ENGINE_PASSWORD``, or
``IDENTITY_SERVICES_ENGINE_VERSION`` and ``IDENTITY_SERVICES_ENGINE_ENCODED_AUTH`` environment variables, you are good to go.
ciscoisesdk will use them to create your access token when creating new :class:`IdentityServicesEngineAPI` objects.

If you don't want to set your credentials as environment variables, you
can manually provide them as parameters when creating a IdentityServicesEngineAPI object.

.. note::
    The ciscoisesdk assumes that the ERS APIs and OpenAPIs are enabled.
    If uses_api_gateway is True, the ciscoisesdk assumes that your ISE API Gateway is enabled as well.


Set credentials as environment variables
-----------------------------------------

There are many places and diverse ways that you can set an environment
variable, which can include:

    * A setting within your development IDE
    * A setting in your container / PaaS service
    * A statement in a shell script that configures and launches your app

It can be as simple as setting it in your CLI before running your script...

.. code-block:: bash

    $ IDENTITY_SERVICES_ENGINE_USERNAME=your_username_here
    $ IDENTITY_SERVICES_ENGINE_PASSWORD=your_password_here
    $ python myscript.py

...or putting your credentials in a shell script that you ``source`` when your
shell starts up or before your run a script:

.. code-block:: bash

    $ cat mycredentials.sh
    export IDENTITY_SERVICES_ENGINE_ENCODED_AUTH=your_encoded_auth_here
    $ source mycredentials.sh
    $ python myscript.py


Create a IdentityServicesEngineAPI "Connection Object"
------------------------------------------------------

To make interacting with the Identity Services Engine APIs as simple and intuitive as
possible, all of the APIs have 'wrapped' underneath a single interface.  To get
started, import the :class:`IdentityServicesEngineAPI` class and create an API "connection
object".

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> api = IdentityServicesEngineAPI()

As discussed above (`Pass your Identity Services Engine Access Token`_), ciscoisesdk defaults
to pulling from environment variables to generate your access token.
If you do not have those environment variables set and you try to
create a new :class:`IdentityServicesEngineAPI` object without providing them,
a :exc:`AccessTokenError` will be raised (a :exc:`ciscoisesdkException` subclass).

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> api = IdentityServicesEngineAPI()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "ciscoisesdk/api/__init__.py", line 356, in __init__
        raise AccessTokenError(error_message)
    AccessTokenError: You need an access token to interact with the Identity Services Engine
    APIs. Identity Services Engine uses HTTP Basic Auth to create an access
    token. You must provide the username and password or just
    the encoded_auth, either by setting each parameter or its
    environment variable counterpart (IDENTITY_SERVICES_ENGINE_USERNAME,
    IDENTITY_SERVICES_ENGINE_PASSWORD, IDENTITY_SERVICES_ENGINE_ENCODED_AUTH).


If you don't provide a known version and try to create a new :class:`IdentityServicesEngineAPI`, a :exc:`VersionError` will be raised.

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> api = IdentityServicesEngineAPI(username='devnetuser',
                                        password='Cisco123!',
                                        base_url='https://dcloud-dna-ise-rtp.cisco.com',
                                        version='0.1.12')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "ciscoisesdk/api/__init__.py", line 344, in __init__
        raise VersionError(error_message)
    VersionError: Unknown API version, known versions are 3.0.0, 3.1.0 and 3.1.1.


Use the arguments to manually provide enough information for the HTTP Basic Auth process, 
when creating a new :class:`IdentityServicesEngineAPI` connection object.

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> # Create a IdentityServicesEngineAPI connection object;
    >>> # Using encoded_auth, with Identity Services Engine API version 3.1.1
    >>> api = IdentityServicesEngineAPI(encoded_auth='YWRtaW46QzFzY28xMjM0NQo=',
    ...                                 base_url="https://dcloud-dna-ise-rtp.cisco.com",
    ...                                 version='3.1.1',
    ...                                 uses_api_gateway=True,
    ...                                 uses_csrf_token=True)
    >>> # Create a IdentityServicesEngineAPI connection object;
    >>> # Using username, and password, with ISE API version 3.1.1
    >>> api = IdentityServicesEngineAPI(username='admin', password='C1sco12345',
    ...                                 uses_api_gateway=True,
    ...                                 base_url="https://dcloud-dna-ise-rtp.cisco.com",
    ...                                 version='3.1.1',
    ...                                 uses_csrf_token=True)


Use the arguments to provide the URLs required depending on the uses_api_gateway value.

.. note::
    If uses_api_gateway is True, the ciscoisesdk assumes that your ISE API Gateway is enabled.

.. note::
    If uses_csrf_token is True, the ciscoisesdk assumes that your ISE CSRF Check is enabled.
    Furthermore, it assumes you need the ciscoisesdk to manage the CSRF token automatically for you.


.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> # Create a IdentityServicesEngineAPI connection object; 
    >>> # Using API Gateway (since it was enabled on ISE)
    >>> # Using CSRF Token (since the CSRF Check was enabled on ISE)
    >>> api = IdentityServicesEngineAPI(username='admin',
    ...                                 password='C1sco12345',
    ...                                 uses_api_gateway=True,
    ...                                 uses_csrf_token=True,
    ...                                 base_url='https://dcloud-dna-ise-rtp.cisco.com',
    ...                                 version='3.1.1',
    ...                                 verify=True)
    >>> # Not using API Gateway
    >>> # Not using CSRF Token
    >>> api = IdentityServicesEngineAPI(username='devnetuser', password='Cisco123!',
    ...                                 uses_api_gateway=False,
    ...                                 uses_csrf_token=False,
    ...                                 ers_base_url="https://dcloud-dna-ise-rtp.cisco.com:9060",
    ...                                 ui_base_url="https://dcloud-dna-ise-rtp.cisco.com:443",
    ...                                 mnt_base_url="https://dcloud-dna-ise-rtp.cisco.com:443",
    ...                                 px_grid_base_url="https://dcloud-dna-ise-rtp.cisco.com:8910",
    ...                                 version='3.1.1')


Note that this can be very useful if you are reading authentication credentials
from a file or database and/or when you want to create more than one connection object.

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> kingston_auth = 'ZG5hY2VudGVydXNlcjpDaXNjbzEyMyEK'
    >>> london_auth = ('london', 'rcx0cf43!')
    >>> kingston_api = IdentityServicesEngineAPI(encoded_auth=kingston_auth, base_url="https://dcloud-dna-ise-rtp.cisco.com", version='3.1.1')
    >>> london_api = IdentityServicesEngineAPI(*london_auth, base_url="https://128.107.71.199:443",
    ...                                        version='3.1.1', uses_api_gateway=True)  # * Unpacks tuple


CSRF Token Check
----------------

If `uses_csrf_token` is True, the ciscoisesdk assumes that your ISE CSRF Check is enabled.
Furthermore, it presumes you need the ciscoisesdk to manage the CSRF token **automatically** for you.

If `uses_csrf_token` is False, the ciscoisesdk assumes that your ISE CSRF Check is disabled.
Additionally, it supposes you do not need the ciscoisesdk to send CSRF token for POST/PUT/DELETE operations.
In this case, you could still do it manually like in the following code fragment:

.. code-block:: python

    >>> endpoint_id_to_delete = "be46f4f0-932f-11ec-aa4c-8e0da8a23ad8"
    >>> get_request = api.endpoint.get_version(headers={"X-CSRF-Token": "fetch"})
    >>> r2 = api.endpoint.delete_by_id(id=endpoint_id_to_delete,
    ...                                headers={"X-CSRF-Token": get_request.headers["X-CSRF-Token"]})


API Gateway
-----------

If `uses_api_gateway` is True, the ciscoisesdk assumes that the API Gateway is enabled.

If `uses_api_gateway` is True you only need to set your `base_url`.

If `uses_api_gateway` is False you need to set the `ers_base_url`, `ui_base_url`, `mnt_base_url` and `px_grid_base_url`.

.. warning::
    1. Ensure that you have enabled the ERS APIs and OpenAPIs.
    2. Make sure to check the ISE settings for the API Gateway, and set the uses_api_gateway accordingly.


If you don't provide the URLs necessary and try to create a new :class:`IdentityServicesEngineAPI`, a :exc:`TypeError` will be raised.

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> # Create a IdentityServicesEngineAPI connection object;
    >>> # it uses Identity Services Engine username and password, with ISE API version 3.1.1
    >>> # The base_url used by default is `from ciscoisesdk.config import DEFAULT_BASE_URL`
    >>> api = IdentityServicesEngineAPI(username='admin',
    ...                                 password='C1sco12345',
    ...                                 uses_api_gateway=True,
    ...                                 base_url=None,
    ...                                 version='3.1.1',
    ...                                 verify=True)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        api = IdentityServicesEngineAPI(username='admin',
      File "ciscoisesdk/api/__init__.py", line 336, in __init__
      File "ciscoisesdk/utils.py", line 165, in check_type
    TypeError: We were expecting to receive an instance of one of the following types: 
    'basestring'; but instead we received None which is a 'NoneType'.


.. code-block:: python

    >>> # Other way to create IdentityServicesEngineAPI connection object; if it does not use the API Gateway
    >>> api = IdentityServicesEngineAPI(username='devnetuser', password='Cisco123!',
    ...                                 uses_api_gateway=False,
    ...                                 ers_base_url="https://dcloud-dna-ise-rtp.cisco.com:9060",
    ...                                 ui_base_url="https://dcloud-dna-ise-rtp.cisco.com:443",
    ...                                 mnt_base_url="https://dcloud-dna-ise-rtp.cisco.com:443",
    ...                                 # px_grid_base_url="https://dcloud-dna-ise-rtp.cisco.com:8910",
    ...                                 version='3.1.1')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        api = IdentityServicesEngineAPI(username='admin',
      File "ciscoisesdk/api/__init__.py", line 341, in __init__
      File "ciscoisesdk/utils.py", line 165, in check_type
    TypeError: We were expecting to receive an instance of one of the following types: 
    'basestring'; but instead we received None which is a 'NoneType'.


Certificates
------------

Besides username, password, encoded_auth, base_url, and version, there are other parameters when creating the :class:`IdentityServicesEngineAPI`, many of them have a default value (check `Package Constants`_ for more).

When dealing with certificates, the most important one is the ``verify`` parameter.

To avoid getting errors like the following:

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> own_api = IdentityServicesEngineAPI(encoded_auth='dXNlcm5hbWU6cGFzc3dvcmQK',
    ... base_url="https://128.107.71.199:443", version='3.1.1', uses_api_gateway=True)
    requests.exceptions.SLError: HTTPSConnectionPool(host='128.107.71.199', port=443):
    Max retries exceeded with url: /dna/system/api/v1/auth/token (Caused by
    SSLError (SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: self signed certificate in certificate chain (_ssl.c:1076)')))
    >>>

Include the verify parameter and set it to False:

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI
    >>> own_api = IdentityServicesEngineAPI(encoded_auth='dXNlcm5hbWU6cGFzc3dvcmQK', 
    ... base_url="https://128.107.71.199:443", version='1.3.0',
    ... verify=False)
    InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate
     verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
      InsecureRequestWarning)
    >>>


You will see urllib3 warnings instead. If you want to disable them, the easiest way is with:

.. code-block:: python

    >>> import urllib3
    >>> urllib3.disable_warnings()


Package Constants
------------------

The following are the default values pulled ``from ciscoisesdk.config`` and used when creating the connection object.

.. automodule:: ciscoisesdk.config
    :members:
    :no-undoc-members:
    :exclude-members: DEBUG_ENVIRONMENT_VARIABLE, VERSION_ENVIRONMENT_VARIABLE, USERNAME_ENVIRONMENT_VARIABLE, PASSWORD_ENVIRONMENT_VARIABLE, ENCODED_AUTH_ENVIRONMENT_VARIABLE, BASE_URL_ENVIRONMENT_VARIABLE, SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE, WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE, VERIFY_ENVIRONMENT_VARIABLE, VERIFY_STRING_ENVIRONMENT_VARIABLE 


Making API Calls
----------------

Now that you have created a :class:`IdentityServicesEngineAPI` "connection object," you are
ready to start making API calls.

.. code-block:: python

    >>> api.network_device.get_all(page=1,size=3).response.SearchResult.resources
    [{'id': '4969bc30-ad2a-11eb-95af-f263cf05f605',
      'name': 'ISE_EST_Local_Host_19',
      'description': '',
      'link': {'rel': 'self',
      'href': 'https://198.18.133.27/ers/config/networkdevice/4969bc30-ad2a-11eb-95af-f263cf05f605',
      'type': 'application/json'}},
    {'id': 'a56f6360-a9fe-11eb-95af-f263cf05f605',
      'name': 'ISE_EST_Local_Host_92348',
      'description': '',
      'link': {'rel': 'self',
      'href': 'https://198.18.133.27/ers/config/networkdevice/a56f6360-a9fe-11eb-95af-f263cf05f605',
      'type': 'application/json'}},
    {'id': '2ea03580-aa02-11eb-95af-f263cf05f605',
      'name': 'Test_Device_4',
      'description': '',
      'link': {'rel': 'self',
      'href': 'https://198.18.133.27/ers/config/networkdevice/2ea03580-aa02-11eb-95af-f263cf05f605',
      'type': 'application/json'}}]

It really is that easy.

All of the calls have been wrapped and represented as native Python method
calls, like :meth:`IdentityServicesEngineAPI.network_device.get_all() <ciscoisesdk.api.v3_0_0.network_device.NetworkDevice.get_all>` which gets the network devices summaries
for the Cisco ISE ERS - see 
the `Network Device - Get All
<https://developer.cisco.com/docs/identity-services-engine/3.0/#!network-device/get-all>`_ API endpoint
documentation.

As you can see, we have represented the API endpoints using simple terms
that are aligned with the API docs; for example, representing the ``/ers/config/networkdevice``
API endpoint as a ``network_device.get_network_device()`` method available underneath the
:class:`IdentityServicesEngineAPI` connection object.

A full list of the available API methods, with their descriptions and
parameters, is available in the :ref:`User API Doc`. 

A summary of the structure is available for each version supported


+ :ref:`v3.0.0 <v3_0_0 summary>`


+ :ref:`v3.1.0 <v3_1_0 summary>`


+ :ref:`v3.1.1 <v3_1_1 summary>`



You can easily access and call any of these methods directly from your
:class:`IdentityServicesEngineAPI` connection object:

.. code-block:: python

    >>> api.network_access_policy_set.get_all().response.response
    [{'default': False,
      'id': 'f22b6a01-759b-47e2-99ea-2e062abdb6ed',
      'name': 'Test Policy Set 1',
      'description': 'Test Policy Set',
      'hitCounts': 0,
      'rank': 0,
      'state': 'enabled',
      'condition': {'link': None,
      'conditionType': 'ConditionReference',
      'isNegate': False,
      'name': 'My New Condition',
      'id': '92bba708-1df6-4f03-9d40-d28b4cb2d982',
      'description': 'New optional Description'},
      'serviceName': 'Default Network Access',
      'isProxy': False,
      'link': {'rel': 'self',
      'href': 'https://198.18.133.27/api/v1/policy/network-access/policy-set/f22b6a01-759b-47e2-99ea-2e062abdb6ed',
      'type': 'application/json'}}]


Catching Exceptions
-------------------

If something should go wrong with the API call, an exception will be raised.
:exc:`ApiError` exceptions are raised when an error condition is
returned from the Identity Services Engine cloud.  Details will be provided in the error
message.

.. code-block:: python

    >>> from ciscoisesdk import IdentityServicesEngineAPI, ApiError
    >>> api = IdentityServicesEngineAPI(username='devnetuser', password='Cisco123!')
    >>> # The uses_api_gateway is True by default and the base_url used by default is `from ciscoisesdk.config import DEFAULT_BASE_URL`
    >>> network_device_response = api.network_device.create_network_device(name='ISE_EST_Local_Host_19', network_device_iplist=[{"ipaddress": "127.35.0.1", "mask": 32}])
    ---------------------------------------------------------------------------
    ApiError                                  Traceback (most recent call last)
    <ipython-input-71-afadb5c98c43> in <module>
    ----> 1 network_device_response = api.network_device.create_network_device(name='ISE_EST_Local_Host_19', network_device_iplist=[{"ipaddress": "127.35.0.1", "mask": 32}])
          2
    ciscoisesdk/misc.py in check_response_code(response, expected_response_code)
        63         raise RateLimitError(response)
        64     else:
    --> 65         raise ApiError(response)
        66
    ApiError: [400] - The request was invalid or cannot be otherwise served.
    {
      "ERSResponse" : {
        "operation" : "POST-create-networkdevice",
        "messages" : [ {
          "title" : "Network Device Create failed: Device Name Already Exist",
          "type" : "ERROR",
          "code" : "Application resource validation exception"
        } ],
        "link" : {
          "rel" : "related",
          "href" : "https://198.18.133.27/ers/config/networkdevice",
          "type" : "application/xml"
        }
      }
    }
    >>>

You can catch any errors returned by the Identity Services Engine cloud by catching
:exc:`ApiError` exceptions in a try-except block.

.. code-block:: python

    >>> from ciscoisesdk.exceptions import ApiError
    >>> try:
    ...     network_device_response = api.network_device.create_network_device(name='ISE_EST_Local_Host_19', network_device_iplist=[{"ipaddress": "127.35.0.1", "mask": 32}])
    ... except ApiError as e:
    ...     print(e)
    ApiError: [400] - The request was invalid or cannot be otherwise served.
    {
      "ERSResponse" : {
        "operation" : "POST-create-networkdevice",
        "messages" : [ {
          "title" : "Network Device Create failed: Device Name Already Exist",
          "type" : "ERROR",
          "code" : "Application resource validation exception"
        } ],
        "link" : {
          "rel" : "related",
          "href" : "https://198.18.133.27/ers/config/networkdevice",
          "type" : "application/xml"
        }
      }
    }
    >>>

ciscoisesdk will also raise a number of other standard errors
(:exc:`TypeError`, :exc:`ValueError`, etc.); however, these errors are usually
caused by incorrect use of the package or methods and should be sorted while
debugging your app.


Working with Returned Objects
-----------------------------

The Identity Services Engine cloud returns data objects in JSON format, like so:

.. code-block:: json

    [
      {
        "default": false,
        "id": "f22b6a01-759b-47e2-99ea-2e062abdb6ed",
        "name": "Test Policy Set 1",
        "description": "Test Policy Set",
        "hitCounts": 0,
        "rank": 0,
        "state": "enabled",
        "condition": {
          "link": null,
          "conditionType": "ConditionReference",
          "isNegate": false,
          "name": "My New Condition",
          "id": "92bba708-1df6-4f03-9d40-d28b4cb2d982",
          "description": "New optional Description"
        },
        "serviceName": "Default Network Access",
        "isProxy": false,
        "link": {
          "rel": "self",
          "href": "https://198.18.133.27/api/v1/policy/network-access/policy-set/f22b6a01-759b-47e2-99ea-2e062abdb6ed",
          "type": "application/json"
        }
      }
    ]


Sure, JSON data objects can easily be parsed and represented in Python using
dictionaries, but when working with an 'object' wouldn't it be nice to be able
to work with it like an object - using native object syntax (like accessing
attributes using '.' notation)? ciscoisesdk enables you to do just that:

.. code-block:: python

    >>> policy_set = api.network_access_policy_set.get_all().response.response
    >>> policy_set[0].id
    'f22b6a01-759b-47e2-99ea-2e062abdb6ed'
    >>> policy_set[0].condition.conditionType
    'ConditionReference'
    >>> policy_set[0].condition.name
    'My New Condition'

Representing and treating Identity Services Engine data objects as Python data objects, can really
help clean up your code and make coding easier:

    1.  You don't need to create variables to hold all the data attributes, just
        use the attributes available underneath the data object.

        .. code-block:: python

            >>> # Do this
            >>> device_list_response = api.network_device.get_all(filter='name.EQ.ISE_EST_Local_Host_19')
            >>> device_response = device_list_response.response.SearchResult.resources[0]
            >>> device_response_detail = api.network_device.get_by_id(device_response.id).response.NetworkDevice

            >>> # or even this
            >>> filter_query = 'name.EQ.ISE_EST_Local_Host_19'
            >>> device_response_id = api.network_device.get_all(filter=filter_query).response.SearchResult.resources[0].id
            >>> device_response_detail = api.network_device.get_by_id(device_response_id).response.NetworkDevice

    2.  When accessing 'optional' attributes, like ``device_list_response.response.SearchResult.resources[0].id``
        attribute of Identity Services Engine NetworkDevice object, the response object will return ``None`` when
        the attribute is not present and will return the attribute's value when
        it is present.  This avoids some boiler plate code and/or needless
        exception handling, when working with optional attributes.

        .. code-block:: python

            >>> devices_response = api.network_device.get_all().response
            >>> # Instead of doing this
            >>> if hasattr(devices_response, 'SearchResult') and hasattr(devices_response.SearchResult, 'resources'):
            ...     devices = devices_response.SearchResult.resources
            ...     for d in devices:
            ...          if hasattr(d, 'id') and hasattr(d, 'description'):
            ...              # Do something with the configList attribute
            ...              print(d.id, d.description)
            >>> # Or this
            ... try:
            ...     devices = devices_response.SearchResult.resources
            ... except AttributeError as e:
            ...     pass
            ... for d in devices:
            ...      # Do something with the configList attribute
            ...      print(d.id, d.description)
            ... except AttributeError as e:
            ...     pass
            >>> # You can do this, which is cleaner
            >>> if devices_response.SearchResult and devices_response.SearchResult.resources:
            ...      for d in devices_response.SearchResult.resources:
            ...          if d.id and d.description:
            ...              # Do something with the configList attribute
            ...              print(d.id, d.description)


    3.  It just feels more *natural*.  :-)  When iterating through sequences,
        and working with objects in those sequences (see the next section),
        working with objects as objects is definitely more Pythonic.

        The Zen of Python (`PEP 20`_):
            "Beautiful is better than ugly."
            "Simple is better than complex."

The currently modeled :ref:`Identity Services Engine Data Object` with its
functions, is available :ref:`here <Identity Services Engine Data Object>` in the
:ref:`User API Doc`.


**What if Identity Services Engine adds new data attributes?**

Attribute access WILL WORK for the newly added attributes (yes, without a
package update!).  ciscoisesdk is written to automatically take advantage
of new attributes and data as they are returned.


Configuring Logging for ciscoisesdk
-----------------------------------

The main ciscoisesdk logger is ciscoisesdk.

Other loggers are ciscoisesdk.exceptions, ciscoisesdk.restsession and ciscoisesdk.api.custom_caller.

The ciscoisesdk adds only the logging.NullHandler following the `logging recommendations for libraries`_

So you can add your logging handlers according to your needs.

.. code-block:: python

    import logging
    import warnings
    from ciscoisesdk import IdentityServicesEngineAPI

    # Another way to disable warnings caused by (verify=False)
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')

    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)

    ch_ = logging.StreamHandler()
    api = IdentityServicesEngineAPI(verify=False, debug=True)
    logging.getLogger('ciscoisesdk').addHandler(ch_)

    logger.debug('simple message')
    api.network_device.get_all().response


Adding API call definitions
-----------------------------

Custom caller functions help you:

  1. Add support for custom API calls.

  2. Add support for API calls that are/were not documented when the SDK was released.


.. code-block:: python

    from ciscoisesdk import api

    # Create a IdentityServicesEngineAPI connection object;
    # it uses Identity Services Engine sandbox URL, username and password, with Identity Services Engine API version 3.1.1.,
    # and requests to verify the server's TLS certificate with verify=True.
    api_ = api.IdentityServicesEngineAPI(username="devnetuser",
        password="Cisco123!",
        base_url="https://dcloud-dna-ise-rtp.cisco.com",
        version='3.1.1',
        verify=True
    )

    # Add your custom API call to the connection object.
    # Define the get_hotspotportal function.
    # Call it with:
    #     get_hotspotportal(params={'filter': 'name.EQ.Hotspot Guest Portal'})
    def get_hotspotportal(params):
        return api_.custom_caller.call_api('GET', '/ers/config/hotspotportal', params)

    # Add your custom API call to the connection object.
    # Define the delete_hotspotportal_by_id function
    # under the custom_caller wrapper.
    # Call it with:
    #     api_.custom_caller.delete_hotspotportal_by_id('be456g16-14fd-4cac-94b7-ac3b8f9f')
    api_.custom_caller.add_api('delete_hotspotportal_by_id',
                               lambda _id:
                                   api_.custom_caller.call_api(
                                       'DELETE',
                                       '/ers/config/hotspotportal/{id}',
                                       path_params={
                                           'id': _id,
                                       })
                               )

    # Advance usage example using Custom Caller functions.
    def setup_custom():
        """
        Defines the get_hotspotportal_by_id and delete_hotspotportal_by_id functions
        under the custom_caller wrapper, and with help documentation
        in two different ways.

        Check that they have been added with
            'get_hotspotportal_by_id' in dir(api_.custom_caller)
            'delete_hotspotportal_by_id' in dir(api_.custom_caller)

        Quickly check that you indeed have them as functions with
            type(getattr(api_.custom_caller, 'get_hotspotportal_by_id'))
            type(getattr(api_.custom_caller, 'delete_hotspotportal_by_id'))

        Check the documentation with
            help(api_.custom_caller.get_hotspotportal_by_id)
            help(api_.custom_caller.delete_hotspotportal_by_id)

        """

        # Alternative 1: Definition with helper function.
        def _get_hotspotportal_by_id(_id):
            """Custom hostport portal API call, returns response attribute

                Args:
                    _id(str): Hostport portal id.

                Returns: 
                    RestResponse: REST response with following properties:
                      - headers(MyDict): response headers.
                      - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                            or the bracket notation.
                      - content(bytes): representation of the request's response
                      - text(str): representation of the request's response
            """
            return api_.custom_caller.call_api(
                                              'GET',
                                              '/ers/config/hotspotportal/{id}',
                                              path_params={
                                                  'id': _id,
                                              })
        # Finally add the function as an attribute.
        api_.custom_caller.add_api('get_hotspotportal_by_id', _get_hotspotportal_by_id)

        # Alternative 2: Definition with lambda function.
        api_.custom_caller.add_api('delete_hotspotportal_by_id',
                                   lambda _id:
                                       api_.custom_caller.call_api(
                                           'DELETE',
                                           '/ers/config/hotspotportal/{id}',
                                           path_params={
                                               'id': _id,
                                           })
                                   )
        # Finally add the documentation
        api_.custom_caller.delete_hotspotportal_by_id.__doc__ = """
            Custom global credential API call to delete hostport portal

            Args:
                _id(str): Hostport portal id.

            Returns: 
                RestResponse: REST response with following properties:
                  - headers(MyDict): response headers.
                  - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                        or the bracket notation.
                  - content(bytes): representation of the request's response
                  - text(str): representation of the request's response
            """


Check out the `Custom Caller`_ documentation to begin using it.


.. _logging recommendations for libraries: https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
.. _Custom Caller: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#custom-caller


*Copyright (c) 2021 Cisco and/or its affiliates.*

.. _PEP 20: https://www.python.org/dev/peps/pep-0020/