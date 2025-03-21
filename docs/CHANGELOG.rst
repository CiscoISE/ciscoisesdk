Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <https://keepachangelog.com/en/1.0.0/>`__, and this project
adheres to `Semantic
Versioning <https://semver.org/spec/v2.0.0.html>`__.

`Unreleased <https://github.com/CiscoISE/ciscoisesdk/compare/v2.3.1...develop>`__
---------------------------------------------------------------------------------

`2.3.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.3.0...v2.3.1>`__ - 2025-03-20
----------------------------------------------------------------------------------------

Added
~~~~~

- ``delete_bulk_end_points`` now supports payload in 3.3 patch 1

.. _section-1:

`2.3.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.2.3...v2.3.0>`__ - 2025-02-14
----------------------------------------------------------------------------------------

.. _added-1:

Added
~~~~~

- The following functions were added for version 3.3 patch 1:

  - ``patch_allowed_protocols_id``
  - ``patch_authorization_profile_id``
  - ``patch_certificate_profile_id``
  - ``patch_downloadable_acl_id``
  - ``patch_endpoint_group_id``
  - ``patch_endpoint_id``
  - ``patch_external_radius_server_id``
  - ``patch_filter_policy_id``
  - ``patch_guest_smtp_notification_settings_id``
  - ``patch_guest_ssid_id``
  - ``patch_hotspot_portal_portal_id``
  - ``patch_identity_group_id``
  - ``patch_id_store_sequence_id``
  - ``patch_internal_user_name_name``
  - ``patch_internal_user_id``
  - ``patch_network_device_group_id``
  - ``patch_network_device_name_name``
  - ``patch_network_device_id``
  - ``patch_portal_theme_id``
  - ``patch_radius_server_sequence_id``
  - ``patch_restid_store_name_name``
  - ``patch_restid_store_id``
  - ``patch_self_reg_portal_portal_id``
  - ``patch_tacacs_command_sets_id``
  - ``patch_tacacs_external_servers_id``
  - ``patch_tacacs_profile_id``
  - ``patch_tacacs_server_sequence_id``

.. _section-2:

`2.2.3 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.2.2...v2.2.3>`__ - 2024-08-05
----------------------------------------------------------------------------------------

- Update ``endpoint.get_endpoints`` in 3.3 patch 1 change ``filterType``
  to ``filtertype`` json request
- Update ``SupportBundleDownload`` API to remove unused parameters
- Update User-Agent header in RestSession
- Update requirements:

  - python = “^3.8”
  - requests = “^2.32.0”
  - readthedocs-sphinx-search = “^0.3.2”

.. _section-3:

`2.2.2 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.2.1...v2.2.2>`__ - 2024-07-16
----------------------------------------------------------------------------------------

Fixed
~~~~~

- Update EndpointIdentityGroup API to include ``parent_id`` parameters
- Update requirements

.. _section-4:

`2.2.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.2.0...v2.2.1>`__ - 2024-05-15
----------------------------------------------------------------------------------------

.. _fixed-1:

Fixed
~~~~~

- Update NetworkDeviceGroup API parameter name from ``ndgtype`` to
  ``othername`` in 3.3 patch 1.

.. _section-5:

`2.2.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.1.2...v2.2.0>`__ - 2024-04-24
----------------------------------------------------------------------------------------

.. _added-2:

Added
~~~~~

- ``ciscoisesdk`` now supports ISE 3.3 patch 1 API services included:
  ``active_directories, ad_groups, custom_attributes, duo_identity_sync, duo_mfa, enable_mfa, endpoint_stop_replication_service, endpoints, full_upgrade, is_mfa_enabled, native_ipsec, px_grid_direct, sgt_range_reservation, user_equipment``

.. _section-6:

`2.1.2 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.1.1...v2.1.2>`__ - 2023-11-10
----------------------------------------------------------------------------------------

.. _fixed-2:

Fixed
~~~~~

- Fix configuration import

.. _section-7:

`2.1.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.1.0...v2.1.1>`__ - 2023-11-09
----------------------------------------------------------------------------------------

.. _fixed-3:

Fixed
~~~~~

- some imports that caused problems were removed

.. _section-8:

`2.1.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.12...v2.1.0>`__ - 2023-11-07
-----------------------------------------------------------------------------------------

.. _added-3:

Added
~~~~~

- ``ciscoisesdk`` now supports ISE 3.2-Beta API services included:
  ``configuration, edda, dataconnect_services, subscriber``

.. _section-9:

`2.0.12 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.11...v2.0.12>`__ - 2023-08-25
-------------------------------------------------------------------------------------------

- Update requirements and readthedocs settings

.. _section-10:

`2.0.11 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.10...v2.0.11>`__ - 2023-08-24
-------------------------------------------------------------------------------------------

Changed
~~~~~~~

- Update requirements

.. _section-11:

`2.0.10 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.9...v2.0.10>`__ - 2023-07-25
------------------------------------------------------------------------------------------

.. _added-4:

Added
~~~~~

- Adding new param ``ersRestIDStoreUserAttributes`` on restid_store
  create function.

.. _section-12:

`2.0.9 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.8...v2.0.9>`__ - 2023-04-19
----------------------------------------------------------------------------------------

.. _changed-1:

Changed
~~~~~~~

- Updating request-toolbelt from 0.9.1 to 0.10.1

.. _section-13:

`2.0.8 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.7...v2.0.8>`__ - 2022-11-07
----------------------------------------------------------------------------------------

.. _fixed-4:

Fixed
~~~~~

- Added a missing parameter allow_wildcard_delete

  - ciscoisesdk.api.v3_1_1.certificates.delete_system_certificate_by_id
  - ciscoisesdk.api.v3_1_patch_1.certificates.delete_system_certificate_by_id

.. _section-14:

`2.0.7 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.6...v2.0.7>`__ - 2022-11-01
----------------------------------------------------------------------------------------

.. _fixed-5:

Fixed
~~~~~

- The following url have been repaired in
  v3_1_0.mics.session_disconnect, v3_1_1.mics.session_disconnect and
  v3_1_patch_1.mics.session_disconnect

  - From
    /admin/API/mnt/CoA/Disconnect/{PSN_NAME}/{MAC}/{DISCONNECT_TYPE}/{NAS_IPV4}/{{ENDPOINT_IP}}
    to
    /admin/API/mnt/CoA/Disconnect/{PSN_NAME}/{MAC}/{DISCONNECT_TYPE}/{NAS_IPV4}/{ENDPOINT_IP}

.. _section-15:

`2.0.6 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.5...v2.0.6>`__ - 2022-10-27
----------------------------------------------------------------------------------------

.. _fixed-6:

Fixed
~~~~~

- The following variable names have been repaired in v3_1_0.mics,
  v3_1_1.mics and v3_1_patch_1.mics

  - The following variable was renamed from rec_ord_s to records
  - The following variable was renamed from sec_ond_s to seconds
  - The following variable was renamed from end_poi_ntm_ac to
    endpoint_mac
  - The following variable was renamed from psn_nam_e to psn_name
  - The following variable was renamed from rea_uth_typ_e to reauth_type
  - The following variable was renamed from dis_con_nec_tty_pe to
    disconnect_type
  - The following variable was renamed from end_poi_nti_p to endpoint_ip

- The following url have been repaired in
  v3_1_0.mics.session_disconnect, v3_1_1.mics.session_disconnect and
  v3_1_patch_1.mics.session_disconnect

  - From
    /admin/API/mnt/CoA/Disconnect>/{PSN_NAME}/{MAC}/{DISCONNECT_TYPE}/{NAS_IPV4}/{{ENDPOINT_IP}}
    to
    /admin/API/mnt/CoA/Disconnect/{PSN_NAME}/{MAC}/{DISCONNECT_TYPE}/{NAS_IPV4}/{{ENDPOINT_IP}}

.. _section-16:

`2.0.5 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.4...v2.0.5>`__ - 2022-10-13
----------------------------------------------------------------------------------------

.. _fixed-7:

Fixed
~~~~~

- Repaired the request body of the
  network_access_network_conditions.create_network_access_network_condition
  request 3.1_patch_1 and 3.1.1
- Repaired the request body of the
  network_access_network_conditions.update_network_access_network_condition_by_id
  request 3.1_patch_1 and 3.1.1

.. _section-17:

`2.0.4 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.3...v2.0.4>`__ - 2022-07-11
----------------------------------------------------------------------------------------

.. _fixed-8:

Fixed
~~~~~

- Update check_type to pass an instance of a list.

.. _section-18:

`2.0.3 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.2...v2.0.3>`__ - 2022-06-07
----------------------------------------------------------------------------------------

.. _changed-2:

Changed
~~~~~~~

- Default ISE DEFAULT_VERSION to 3.1_Patch_1
- Update documentation to use ISE v3.1_Patch_1

.. _section-19:

`2.0.2 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.1...v2.0.2>`__ - 2022-05-02
----------------------------------------------------------------------------------------

.. _fixed-9:

Fixed
~~~~~

- Update pagination to capture and ignore 500 Internal server error when
  they attempt to get_next_page. Previous version only captured and
  ignored 404 Not Found and 400 Bad Request.

.. _section-20:

`2.0.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v2.0.0...v2.0.1>`__ - 2022-03-24
----------------------------------------------------------------------------------------

.. _added-5:

Added
~~~~~

- Add ``DownloadResponse`` class that wraps the
  ``urllib3.response.HTTPResponse``.
- Add ``filename`` optional parameter to the following functions:

  - ciscoisesdk.api.v3_1_0.certificates.Certificates.export_csr
  - ciscoisesdk.api.v3_1_0.certificates.Certificates.export_system_certificate
  - ciscoisesdk.api.v3_1_0.certificates.Certificates.export_trusted_certificate
  - ciscoisesdk.api.v3_1_0.endpoint_certificate.EndpointCertificate.create_endpoint_certificate
  - ciscoisesdk.api.v3_1_0.endpoint_certificate.EndpointCertificate.create
  - ciscoisesdk.api.v3_1_0.support_bundle_download.SupportBundleDownload.download_support_bundle
  - ciscoisesdk.api.v3_1_0.support_bundle_download.SupportBundleDownload.download
  - ciscoisesdk.api.v3_1_1.certificates.Certificates.export_csr
  - ciscoisesdk.api.v3_1_1.certificates.Certificates.export_system_certificate
  - ciscoisesdk.api.v3_1_1.certificates.Certificates.export_trusted_certificate
  - ciscoisesdk.api.v3_1_1.endpoint_certificate.EndpointCertificate.create_endpoint_certificate
  - ciscoisesdk.api.v3_1_1.endpoint_certificate.EndpointCertificate.create
  - ciscoisesdk.api.v3_1_1.support_bundle_download.SupportBundleDownload.download_support_bundle
  - ciscoisesdk.api.v3_1_1.support_bundle_download.SupportBundleDownload.download

.. _changed-3:

Changed
~~~~~~~

- Change the response of the following funtions from
  ``urllib3.response.HTTPResponse`` to a wrapper ``DownloadResponse``.

  - ciscoisesdk.api.v3_1_0.certificates.Certificates.export_csr
  - ciscoisesdk.api.v3_1_0.certificates.Certificates.export_system_certificate
  - ciscoisesdk.api.v3_1_0.certificates.Certificates.export_trusted_certificate
  - ciscoisesdk.api.v3_1_0.endpoint_certificate.EndpointCertificate.create_endpoint_certificate
  - ciscoisesdk.api.v3_1_0.endpoint_certificate.EndpointCertificate.create
  - ciscoisesdk.api.v3_1_0.support_bundle_download.SupportBundleDownload.download_support_bundle
  - ciscoisesdk.api.v3_1_0.support_bundle_download.SupportBundleDownload.download
  - ciscoisesdk.api.v3_1_1.certificates.Certificates.export_csr
  - ciscoisesdk.api.v3_1_1.certificates.Certificates.export_system_certificate
  - ciscoisesdk.api.v3_1_1.certificates.Certificates.export_trusted_certificate
  - ciscoisesdk.api.v3_1_1.endpoint_certificate.EndpointCertificate.create_endpoint_certificate
  - ciscoisesdk.api.v3_1_1.endpoint_certificate.EndpointCertificate.create
  - ciscoisesdk.api.v3_1_1.support_bundle_download.SupportBundleDownload.download_support_bundle
  - ciscoisesdk.api.v3_1_1.support_bundle_download.SupportBundleDownload.download

.. _section-21:

`2.0.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.5.1...v2.0.0>`__ - 2022-03-24
----------------------------------------------------------------------------------------

Removed
~~~~~~~

- Removed ``access_token`` property of ``IdentityServicesEngineAPI`` and
  ``RestSession``.
- Drop ISE version 3.0.0 support.

.. _section-22:

`1.5.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.5.0...v1.5.1>`__ - 2022-02-25
----------------------------------------------------------------------------------------

.. _changed-4:

Changed
-------

- Update docstring documentation of modules and functions.

.. _section-23:

`1.5.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.4.2...v1.5.0>`__ - 2022-02-23
----------------------------------------------------------------------------------------

.. _changed-5:

Changed
~~~~~~~

- Marked ``access_token`` property to be removed in
  ``IdentityServicesEngineAPI`` and ``RestSession``.
- Changed the way of notifying Deprecation of version 3.0.0 of ISE from
  print to warning.
- Incremented ``IdentityServicesEngineAPI`` and ``RestSession``
  constructor parameter count.
- Changed access method an imports used for environment variables and
  default values in api/**init**.py.
- Changed ``IdentityServicesEngineAPI``\ ’s inner properties, getters,
  and setters to handle only the class itself.
- ``RestSession`` to request for a refreshed CSRF token if
  ``uses_csrf_token`` is enabled.
- Replaced the name of headers checked for ERS methods from
  “X-CSRF-TOKEN” to “X-CSRF-Token”.
- Changed ``ApiError`` message when status_code is 401 or 403 to include
  reference to ``additional_data`` property.

.. _added-6:

Added
~~~~~

- Support for “CSRF Check for Enhanced Security” for the ISE ERS API
  (`#20 <https://github.com/CiscoISE/ciscoisesdk/issues/20>`__).
- Added ``status_code`` to ``RestResponse``
  (`#22 <https://github.com/CiscoISE/ciscoisesdk/issues/22>`__).
- Support to have additional_data for ``ApiError`` when HTTP status code
  are 401 or 403
  (`#21 <https://github.com/CiscoISE/ciscoisesdk/issues/21>`__). The
  additional_data returns a string with:

  - Authorization header used.
  - X-CSRF-Token header used if it was found.
  - Username used.
  - Password used.

- Support for managing changes of the ``IdentityServicesEngineAPI``\ ’s
  properties
  (`#21 <https://github.com/CiscoISE/ciscoisesdk/issues/21>`__):

  - ``initialize_authentication`` function.
  - ``initialize_sessions`` function.
  - ``initialize_api_wrappers`` function.
  - ``reinitialize`` function.
  - ``authentication`` getter function.
  - ``perform_initialize`` getter function.
  - ``username`` getter and setter functions.
  - ``is_password`` utility function.
  - ``is_encoded_auth`` utility function.
  - ``uses_api_gateway`` getter and setter functions.
  - ``base_url`` getter and setter functions.
  - ``ui_base_url`` getter and setter functions.
  - ``ers_base_url`` getter and setter functions.
  - ``mnt_base_url`` getter and setter functions.
  - ``px_grid_base_url`` getter and setter functions.
  - ``single_request_timeout`` getter and setter functions.
  - ``wait_on_rate_limit`` getter and setter functions.
  - ``verify`` getter and setter functions.
  - ``version`` getter and setter functions.
  - ``debug`` getter and setter functions.
  - ``uses_csrf_token`` getter and setter functions.
  - ``object_factory`` getter and setter functions.
  - ``validator`` getter and setter functions.
  - ``session`` getter function.
  - ``session_ui`` getter function.
  - ``session_ers`` getter function.
  - ``session_mnt`` getter function.
  - ``session_px_grid`` getter function.
  - ``username`` getter function.
  - ``change_password`` utility setter function.
  - ``change_encoded_auth`` utility setter function.

- Added warnings for changes of the ``IdentityServicesEngineAPI``\ ’s
  properties.
- Added a test importsdk to verify the behavior between environment
  variables and module import order.
- New ``perform_initialize`` parameter for ``IdentityServicesEngineAPI``
  constructor.
- New ``uses_csrf_token`` parameter for ``IdentityServicesEngineAPI``
  constructor.
- New ``get_csrf_token`` function for ``IdentityServicesEngineAPI``.
- New ``uses_csrf_token`` and ``get_csrf_token`` parameters for
  ``RestSession`` constructor.
- New ``DEFAULT_USES_CSRF_TOKEN`` value in config.py.
- New ``IDENTITY_SERVICES_ENGINE_USES_CSRF_TOKEN`` environment variable
  in environment.py.
- New ``initialize_authentication`` function for
  ``IdentityServicesEngineAPI``.
- New ``initialize_sessions`` function for
  ``IdentityServicesEngineAPI``.
- New ``initialize_api_wrappers`` function for
  ``IdentityServicesEngineAPI``.
- New ``reinitialize`` function for ``IdentityServicesEngineAPI``.
- New ``is_password`` function for ``IdentityServicesEngineAPI``.
- New ``is_encoded_auth`` function for ``IdentityServicesEngineAPI``.
- New ``change_password`` function for ``IdentityServicesEngineAPI``.
- New ``change_encoded_auth`` function for
  ``IdentityServicesEngineAPI``.
- New ``debug`` setter funtion for ``RestSession``.
- New ``uses_csrf_token`` getter and setter funtions for
  ``RestSession``.
- New ``additional_data`` property in ``ApiError``.

.. _fixed-10:

Fixed
~~~~~

- The process that gets the environment variables now can access the
  variables set after the module is imported, and not only before it.
- Fixed the docstring tables of the API modules.

.. _section-24:

`1.4.2 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.4.1...v1.4.2>`__ - 2022-02-18
----------------------------------------------------------------------------------------

.. _fixed-11:

Fixed
~~~~~

- Update pagination to capture and ignore 400 Bad Request in generators
  when they attempt to get_next_page. Previous version only captured and
  ignored 404 Not Found.

.. _section-25:

`1.4.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.4.0...v1.4.1>`__ - 2022-01-20
----------------------------------------------------------------------------------------

.. _changed-6:

Changed
~~~~~~~

- Update module inner documentation.
- Downgrade requirements file to use poetry versions.

.. _section-26:

`1.4.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.3.1...v1.4.0>`__ - 2022-01-19
----------------------------------------------------------------------------------------

.. _changed-7:

Changed
~~~~~~~

- Update requirements

.. _fixed-12:

Fixed
~~~~~

- Update pagination, get_next_page inner logic and location from utils
  to pagination.

.. _section-27:

`1.3.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.3.0...v1.3.1>`__ - 2021-12-13
----------------------------------------------------------------------------------------

.. _changed-8:

Changed
~~~~~~~

- Fixes utils.get_next_page generator starting default page

.. _section-28:

`1.3.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.2.0...v1.3.0>`__ - 2021-12-13
----------------------------------------------------------------------------------------

.. _added-7:

Added
~~~~~

- Adds licensing module
- Adds node_services module
- Adds patching module
- Adds proxy module
- Adds telemetry module
- Adds certificates.generate_self_signed_certificate function
- Adds node_deployment.make_primary function
- Adds node_deployment.make_standalone function
- Adds node_deployment.sync_node function
- Adds node_group.add_node function
- Adds node_group.get_nodes function
- Adds node_group.remove_node function
- Adds pan_ha.update_pan_ha function

.. _removed-1:

Removed
~~~~~~~

- Removes pan_ha.disable_pan_ha function
- Removes pan_ha.enable_pan_ha function
- Removes replication_status module
- Removes sync_ise_node module

.. _section-29:

`1.2.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.1.0...v1.2.0>`__ - 2021-11-24
----------------------------------------------------------------------------------------

.. _added-8:

Added
~~~~~

- Adds notice for 3.0.0 (soon to be deprecated)
- Adds Trust Sec endpoints to ISE version 3.1.0

.. _changed-9:

Changed
~~~~~~~

- Fixes paths for Policy endpoints (get_device_admin_profiles,
  get_network_access_profiles)
- Updates ISE version 3.1.0 as separate version

.. _removed-2:

Removed
~~~~~~~

- Removes link of 3.1.0 modules to 3.0.0 version

.. _section-30:

`1.1.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.0.1...v1.1.0>`__ - 2021-10-22
----------------------------------------------------------------------------------------

.. _added-9:

Added
~~~~~

- Link of 3.1.0 modules to 3.0.0 version

.. _changed-10:

Changed
~~~~~~~

- Default ISE DEFAULT_VERSION to 3.1.0
- Update documentation to use ISE v3.1.0

.. _section-31:

`1.0.1 <https://github.com/CiscoISE/ciscoisesdk/compare/v1.0.0...v1.0.1>`__ - 2021-09-14
----------------------------------------------------------------------------------------

.. _changed-11:

Changed
~~~~~~~

- Disabled warnings of urllib3 if verify is False

.. _section-32:

`1.0.0 <https://github.com/CiscoISE/ciscoisesdk/compare/v0.5.1...v1.0.0>`__ - 2021-07-21
----------------------------------------------------------------------------------------

.. _added-10:

Added
~~~~~

- Missing parameters for functions
- ``get_version`` functions for ERS wrapper classes.
- Missing functions:

  - AncPolicy.get_anc_policy_generator
  - BackupAndRestore.update_scheduled_config_backup
  - CertificateTemplate.get_certificate_template_generator
  - DeviceAdministrationAuthenticationRules.reset_hit_counts_device_admin_authentication_rules
  - DeviceAdministrationAuthorizationExceptionRules.reset_hit_counts_device_admin_local_exceptions
  - DeviceAdministrationAuthorizationGlobalExceptionRules.reset_hit_counts_device_admin_global_exceptions
  - DeviceAdministrationAuthorizationRules.reset_hit_counts_device_admin_authorization_rules
  - DeviceAdministrationPolicySet.reset_hit_counts_device_admin_policy_sets
  - MyDevicePortal.delete_my_device_portal_by_id
  - NetworkAccessAuthenticationRules.reset_hit_counts_network_access_authentication_rules
  - NetworkAccessAuthorizationExceptionRules.reset_hit_counts_network_access_local_exceptions
  - NetworkAccessAuthorizationRules.reset_hit_counts_network_access_authorization_rules
  - NetworkAccessPolicySet.reset_hit_counts_network_access_policy_sets
  - SessionServiceNode.get_session_service_node_generator
  - SupportBundleStatus.get_support_bundle_status_generator
  - TacacsCommandSets.get_tacacs_command_sets_generator

- Aliases for functions (eg. ``get_all``, ``get_by_id``,
  ``get_by_name``, ``update_by_id``, ``delete_by_id``, ``create``, and
  others)

.. _changed-12:

Changed
~~~~~~~

- Rename module names

  - ``deployment`` to ``pull_deployment_info``
  - ``threat`` to ``clear_threats_and_vulnerabilities``
  - ``endpoint_group`` to ``endpoint_identity_group``
  - ``identity_group`` to ``identity_groups``
  - ``identity_store_sequence`` to ``identity_sequence``
  - ``node`` to ``node_details``
  - ``endpoint_cert`` to ``endpoint_certificate``
  - ``guest_smtp_notifications`` to
    ``guest_smtp_notification_configuration``
  - ``session_service_node`` to ``psn_node_details_with_radius_service``
  - ``sg_acl`` to ``security_groups_acls``
  - ``sg_mapping_group`` to ``ip_to_sgt_mapping_group``
  - ``sg_mapping`` to ``ip_to_sgt_mapping``
  - ``sgt_vn_vlan`` to ``security_group_to_virtual_network``
  - ``sgt`` to ``security_groups``
  - ``support_bundle`` to ``support_bundle_download``,
    ``support_bundle_status`` & ``support_bundle_trigger_configuration``
  - ``version_`` to ``version_and_patch``

- Rename function names

  - (BackupAndRestore) ``schedule_config_backup`` to
    ``create_scheduled_config_backup``
  - (Certificates) ``get_csr`` to ``get_csrs``
  - (Certificates) ``get_csr_generator`` to ``get_csrs_generator``
  - (Certificates) ``renew_certificate`` to ``renew_certificates``
  - (Certificates) ``export_system_cert`` to
    ``export_system_certificate``
  - (Certificates) ``export_trusted_cert`` to
    ``export_trusted_certificate``
  - (DeviceAdministrationAuthenticationRules)
    ``create_device_admin_authentication_rules`` to
    ``create_device_admin_authentication_rule``
  - (DeviceAdministrationAuthorizationExceptionRules)
    ``delete_device_admin_policyset_global_exception_by_id`` to
    ``delete_device_admin_policy_set_global_exception_by_rule_id``
  - (DeviceAdministrationAuthorizationExceptionRules)
    ``get_device_admin_policy_set_global_exception`` to
    ``get_device_admin_policy_set_global_exception_rules``
  - (DeviceAdministrationAuthorizationExceptionRules)
    ``get_device_admin_policy_set_global_exception_by_id`` to
    ``get_device_admin_policy_set_global_exception_by_rule_id``
  - (DeviceAdministrationAuthorizationExceptionRules)
    ``update_device_admin_policyset_global_exception_by_id`` to
    ``update_device_admin_policy_set_global_exception_by_rule_id``
  - (DeviceAdministrationDictionaryAttributesList)
    ``get_device_admin_dictionaries_policyset`` to
    ``get_device_admin_dictionaries_policy_set``
  - (GuestType) ``update_guesttype_by_id`` to
    ``update_guest_type_by_id``
  - (IdentityStoreSequence) ``create_identity_store_sequence`` to
    ``create_identity_sequence``
  - (IdentityStoreSequence) ``delete_identity_store_sequence_by_id`` to
    ``delete_identity_sequence_by_id``
  - (IdentityStoreSequence) ``get_identity_store_sequence`` to
    ``get_identity_sequence``
  - (IdentityStoreSequence) ``get_identity_store_sequence_by_id`` to
    ``get_identity_sequence_by_id``
  - (IdentityStoreSequence) ``get_identity_store_sequence_by_name`` to
    ``get_identity_sequence_by_name``
  - (IdentityStoreSequence) ``get_identity_store_sequence_generator`` to
    ``get_identity_sequence_generator``
  - (IdentityStoreSequence) ``update_identity_store_sequence_by_id`` to
    ``update_identity_sequence_by_id``
  - (InternalUser) ``internaluser_by_id`` to ``get_internal_user_by_id``
  - (NetworkAccessAuthorizationGlobalExceptionRules)
    ``create_network_access_global_exception_rule`` to
    ``create_network_access_policy_set_global_exception_rule``
  - (NetworkAccessAuthorizationGlobalExceptionRules)
    ``delete_network_access_global_exception_rule_by_id`` to
    ``delete_network_access_policy_set_global_exception_rule_by_id``
  - (NetworkAccessAuthorizationGlobalExceptionRules)
    ``get_network_access_global_exception_rule_by_id`` to
    ``get_network_access_policy_set_global_exception_rule_by_id``
  - (NetworkAccessAuthorizationGlobalExceptionRules)
    ``get_network_access_global_exception_rules`` to
    ``get_network_access_policy_set_global_exception_rules``
  - (NetworkAccessAuthorizationGlobalExceptionRules)
    ``update_network_access_global_exception_rule_by_id`` to
    ``update_network_access_policy_set_global_exception_rule_by_id``
  - (DeviceAdministrationConditions)
    ``get_device_admin_conditions_for_authentication_rule`` to
    ``get_device_admin_conditions_for_authentication_rules``
  - (DeviceAdministrationConditions)
    ``get_device_admin_conditions_for_authorization_rule`` to
    ``get_device_admin_conditions_for_authorization_rules``
  - (DeviceAdministrationConditions)
    ``get_device_admin_conditions_for_policy_set`` to
    ``get_device_admin_conditions_for_policy_sets``
  - (NetworkAccessConditions)
    ``get_network_access_conditions_for_authorization_rule`` to
    ``get_network_access_conditions_for_authorization_rules``
  - (NetworkAccessConditions)
    ``get_network_access_conditions_for_policy_set`` to
    ``get_network_access_conditions_for_policy_sets``
  - (NetworkAccessDictionary)
    ``delete_network_access_dictionaries_by_name`` to
    ``delete_network_access_dictionary_by_name``
  - (NetworkAccessDictionary)
    ``update_network_access_dictionaries_by_name`` to
    ``update_network_access_dictionary_by_name``
  - (NetworkAccessDictionary)
    ``create_network_access_dictionary_attribute_for_dictionary`` to
    ``create_network_access_dictionary_attribute``
  - (NetworkAccessDictionaryAttributesList)
    ``get_network_access_dictionaries_policyset`` to
    ``get_network_access_dictionaries_policy_set``
  - (Node) ``get_node_by_id`` to ``get_node_detail_by_id``
  - (Node) ``get_node_by_name`` to ``get_node_detail_by_name``
  - (Node) ``get_nodes`` to ``get_node_details``
  - (PxGridSettings) ``autoapprove_px_grid_node`` to
    ``autoapprove_px_grid_settings``
  - (Repository) ``delete_repository_by_name`` to ``delete_repository``
  - (Repository) ``get_repository_by_name`` to ``get_repository``
  - (Repository) ``update_repository_by_name`` to ``update_repository``

.. _removed-3:

Removed
~~~~~~~

- Removed module

  - ``service``

- Removed unknown functions for the API

  - ``identity_group.delete_identity_group_by_id``
