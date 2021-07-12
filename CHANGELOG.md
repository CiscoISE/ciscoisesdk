# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Missing parameters for functions
- `get_version` functions for ERS wrapper classes.
- Missing functions:
 + AncPolicy.get_anc_policy_generator
 + BackupAndRestore.update_scheduled_config_backup
 + CertificateTemplate.get_certificate_template_generator
 + DeviceAdministrationAuthenticationRules.reset_hit_counts_device_admin_authentication_rules
 + DeviceAdministrationAuthorizationExceptionRules.reset_hit_counts_device_admin_local_exceptions
 + DeviceAdministrationAuthorizationGlobalExceptionRules.reset_hit_counts_device_admin_global_exceptions
 + DeviceAdministrationAuthorizationRules.reset_hit_counts_device_admin_authorization_rules
 + DeviceAdministrationPolicySet.reset_hit_counts_device_admin_policy_sets
 + MyDevicePortal.delete_my_device_portal_by_id
 + NetworkAccessAuthenticationRules.reset_hit_counts_network_access_authentication_rules
 + NetworkAccessAuthorizationExceptionRules.reset_hit_counts_network_access_local_exceptions
 + NetworkAccessAuthorizationRules.reset_hit_counts_network_access_authorization_rules
 + NetworkAccessPolicySet.reset_hit_counts_network_access_policy_sets
 + SessionServiceNode.get_session_service_node_generator
 + SupportBundleStatus.get_support_bundle_status_generator
 + TacacsCommandSets.get_tacacs_command_sets_generator
- Aliases for functions (eg. `get_all`, `get_by_id`, `get_by_name`, `update_by_id`, `delete_by_id`, `create`, and others)

### Changed
- Rename module names
  + `deployment` to `pull_deployment_info`
  + `threat` to `clear_threats_and_vulnerabilities`
  + `endpoint_group` to `endpoint_identity_group`
  + `identity_group` to `identity_groups`
  + `identity_store_sequence` to `identity_sequence`
  + `node` to `node_details`
  + `endpoint_cert` to `endpoint_certificate`
  + `guest_smtp_notifications` to `guest_smtp_notification_configuration`
  + `session_service_node` to `psn_node_details_with_radius_service`
  + `sg_acl` to `security_groups_acls`
  + `sg_mapping_group` to `ip_to_sgt_mapping_group`
  + `sg_mapping` to `ip_to_sgt_mapping`
  + `sgt_vn_vlan` to `security_group_to_virtual_network`
  + `sgt` to `security_groups`
  + `support_bundle` to `support_bundle_download`, `support_bundle_status` & `support_bundle_trigger_configuration`
  + `version_` to `version_and_patch`
- Rename function names
  + (BackupAndRestore) `schedule_config_backup` to `create_scheduled_config_backup`
  + (Certificates) `export_trusted_certificate` to `export_trusted_cert`
  + (Certificates) `get_csr` to `get_csrs`
  + (Certificates) `get_csr_generator` to `get_csrs_generator`
  + (Certificates) `import_system_certificate` to `import_system_cert`
  + (Certificates) `import_trusted_certificate` to `import_trust_cert`
  + (Certificates) `renew_certificate` to `renew_certs`
  + (Certificates) `update_system_certificate` to `update_system_cert`
  + (DeviceAdministrationAuthenticationRules) `create_device_admin_authentication_rules` to `create_device_admin_authentication_rule`
  + (DeviceAdministrationAuthorizationExceptionRules) `delete_device_admin_policyset_global_exception_by_id` to `delete_device_admin_policy_set_global_exception_by_rule_id`
  + (DeviceAdministrationAuthorizationExceptionRules) `get_device_admin_policy_set_global_exception` to `get_device_admin_policy_set_global_exception_rules`
  + (DeviceAdministrationAuthorizationExceptionRules) `get_device_admin_policy_set_global_exception_by_id` to `get_device_admin_policy_set_global_exception_by_rule_id`
  + (DeviceAdministrationAuthorizationExceptionRules) `update_device_admin_policyset_global_exception_by_id` to `update_device_admin_policy_set_global_exception_by_rule_id`
  + (DeviceAdministrationDictionaryAttributesList) `get_device_admin_dictionaries_policyset` to `get_device_admin_dictionaries_policy_set`
  + (GuestType) `update_guesttype_by_id` to `update_guest_type_by_id`
  + (IdentityStoreSequence) `create_identity_store_sequence` to `create_identity_sequence`
  + (IdentityStoreSequence) `delete_identity_store_sequence_by_id` to `delete_identity_sequence_by_id`
  + (IdentityStoreSequence) `get_identity_store_sequence` to `get_identity_sequence`
  + (IdentityStoreSequence) `get_identity_store_sequence_by_id` to `get_identity_sequence_by_id`
  + (IdentityStoreSequence) `get_identity_store_sequence_by_name` to `get_identity_sequence_by_name`
  + (IdentityStoreSequence) `get_identity_store_sequence_generator` to `get_identity_sequence_generator`
  + (IdentityStoreSequence) `update_identity_store_sequence_by_id` to `update_identity_sequence_by_id`
  + (InternalUser) `internaluser_by_id` to `get_internal_user_by_id`
  + (NetworkAccessAuthorizationGlobalExceptionRules) `create_network_access_global_exception_rule` to `create_network_access_policy_set_global_exception_rule`
  + (NetworkAccessAuthorizationGlobalExceptionRules) `delete_network_access_global_exception_rule_by_id` to `delete_network_access_policy_set_global_exception_rule_by_id`
  + (NetworkAccessAuthorizationGlobalExceptionRules) `get_network_access_global_exception_rule_by_id` to `get_network_access_policy_set_global_exception_rule_by_id`
  + (NetworkAccessAuthorizationGlobalExceptionRules) `get_network_access_global_exception_rules` to `get_network_access_policy_set_global_exception_rules`
  + (NetworkAccessAuthorizationGlobalExceptionRules) `update_network_access_global_exception_rule_by_id` to `update_network_access_policy_set_global_exception_rule_by_id`
  + (DeviceAdministrationConditions) `get_device_admin_conditions_for_authentication_rule` to `get_device_admin_conditions_for_authentication_rules`
  + (DeviceAdministrationConditions) `get_device_admin_conditions_for_authorization_rule` to `get_device_admin_conditions_for_authorization_rules`
  + (DeviceAdministrationConditions) `get_device_admin_conditions_for_policy_set` to `get_device_admin_conditions_for_policy_sets`
  + (NetworkAccessConditions) `get_network_access_conditions_for_authorization_rule` to `get_network_access_conditions_for_authorization_rules`
  + (NetworkAccessConditions) `get_network_access_conditions_for_policy_set` to `get_network_access_conditions_for_policy_sets`
  + (NetworkAccessDictionary) `delete_network_access_dictionaries_by_name` to `delete_network_access_dictionary_by_name`
  + (NetworkAccessDictionary) `update_network_access_dictionaries_by_name` to `update_network_access_dictionary_by_name`
  + (NetworkAccessDictionary) `create_network_access_dictionary_attribute_for_dictionary` to `create_network_access_dictionary_attribute`
  + (NetworkAccessDictionaryAttributesList) `get_network_access_dictionaries_policyset` to `get_network_access_dictionaries_policy_set`
  + (Node) `get_node_by_id` to `get_node_detail_by_id`
  + (Node) `get_node_by_name` to `get_node_detail_by_name`
  + (Node) `get_nodes` to `get_node_details`
  + (PxGridSettings) `autoapprove_px_grid_node` => `autoapprove_px_grid_settings`
  + (Repository) `delete_repository_by_name` => `delete_repository`
  + (Repository) `get_repository_by_name` => `get_repository`
  + (Repository) `update_repository_by_name` => `update_repository`

### Removed
- Removed module
  + `service`
  + `version_info`
- Removed unknown functions for the API
  + `identity_group.delete_identity_group_by_id`


## [1.0.0] - 2021-07-xx


[Unreleased]: https://github.com/CiscoISE/ciscoisesdk/compare/v0.5.1...develop_v1
