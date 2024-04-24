# -*- coding: utf-8 -*-
"""pytest configuration and top-level fixtures.

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

pytest_plugins = [
    'tests.test_importsdk',
    'tests.test_ciscoisesdk',
    'tests.api',
    'tests.api.v3_1_0',
    'tests.api.v3_1_1',
    'tests.api.v3_1_patch_1',
    'tests.api.v3_2_beta',
    'tests.api.v3_3_patch_1',
]


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "ratelimit: run a ratelimit test",
    )
    config.addinivalue_line(
        "markers", "ciscoisesdk: package mark"
    )
    config.addinivalue_line(
        "markers", "api: ciscoisesdk mark"
    )
    config.addinivalue_line(
        "markers", "aci_bindings: aci_bindings wrapper test"
    )
    config.addinivalue_line(
        "markers", "aci_settings: aci_settings wrapper test"
    )
    config.addinivalue_line(
        "markers", "ad_groups: ad_groups wrapper test"
    )
    config.addinivalue_line(
        "markers", "anc_endpoint: anc_endpoint wrapper test"
    )
    config.addinivalue_line(
        "markers", "active_directories: active_directories wrapper test"
    )
    config.addinivalue_line(
        "markers", "active_directory: active_directory wrapper test"
    )
    config.addinivalue_line(
        "markers", "admin_user: admin_user wrapper test"
    )
    config.addinivalue_line(
        "markers", "allowed_protocols: allowed_protocols wrapper test"
    )
    config.addinivalue_line(
        "markers", "anc_policy: anc_policy wrapper test"
    )
    config.addinivalue_line(
        "markers", "authentication: authentication wrapper test"
    )
    config.addinivalue_line(
        "markers", "authorization_profile: authorization_profile wrapper test"
    )
    config.addinivalue_line(
        "markers", "byod_portal: byod_portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "backup_and_restore: backup_and_restore wrapper test"
    )
    config.addinivalue_line(
        "markers", "certificate_profile: certificate_profile wrapper test"
    )
    config.addinivalue_line(
        "markers", "certificate_template: certificate_template wrapper test"
    )
    config.addinivalue_line(
        "markers", "certificates: certificates wrapper test"
    )
    config.addinivalue_line(
        "markers", "clear_threats_and_vulnerabilities: clear_threats_and_vulnerabilities wrapper test"
    )
    config.addinivalue_line(
        "markers", "configuration: configuration wrapper test"
    )
    config.addinivalue_line(
        "markers", "consumer: consumer wrapper test"
    )
    config.addinivalue_line(
        "markers", "custom_caller: custom_caller wrapper test"
    )
    config.addinivalue_line(
        "markers", "dataconnect_services: dataconnect_services wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_authentication_rules: device_administration_authentication_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_authorization_exception_rules: device_administration_authorization_exception_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_authorization_global_exception_rules: device_administration_authorization_global_exception_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_authorization_rules: device_administration_authorization_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_command_set: device_administration_command_set wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_conditions: device_administration_conditions wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_dictionary_attributes_list: device_administration_dictionary_attributes_list wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_identity_stores: device_administration_identity_stores wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_network_conditions: device_administration_network_conditions wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_policy_set: device_administration_policy_set wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_profiles: device_administration_profiles wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_service_names: device_administration_service_names wrapper test"
    )
    config.addinivalue_line(
        "markers", "device_administration_time_date_conditions: device_administration_time_date_conditions wrapper test"
    )
    config.addinivalue_line(
        "markers", "downloadable_acl: downloadable_acl wrapper test"
    )
    config.addinivalue_line(
        "markers", "duo_identity_sync: duo_identity_sync wrapper test"
    )
    config.addinivalue_line(
        "markers", "duo_mfa: duo_mfa wrapper test"
    )
    config.addinivalue_line(
        "markers", "edda: edda wrapper test"
    )
    config.addinivalue_line(
        "markers", "egress_matrix_cell: egress_matrix_cell wrapper test"
    )
    config.addinivalue_line(
        "markers", "endpoint_stop_replication_service: endpoint_stop_replication_service wrapper test"
    )
    config.addinivalue_line(
        "markers", "endpoint_certificate: endpoint_certificate wrapper test"
    )
    config.addinivalue_line(
        "markers", "endpoint_identity_group: endpoint_identity_group wrapper test"
    )
    config.addinivalue_line(
        "markers", "external_radius_server: external_radius_server wrapper test"
    )
    config.addinivalue_line(
        "markers", "filter_policy: filter_policy wrapper test"
    )
    config.addinivalue_line(
        "markers", "guest_location: guest_location wrapper test"
    )
    config.addinivalue_line(
        "markers", "guest_smtp_notification_configuration: guest_smtp_notification_configuration wrapper test"
    )
    config.addinivalue_line(
        "markers", "guest_ssid: guest_ssid wrapper test"
    )
    config.addinivalue_line(
        "markers", "guest_type: guest_type wrapper test"
    )
    config.addinivalue_line(
        "markers", "guest_user: guest_user wrapper test"
    )
    config.addinivalue_line(
        "markers", "hotspot_portal: hotspot_portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "ip_to_sgt_mapping: ip_to_sgt_mapping wrapper test"
    )
    config.addinivalue_line(
        "markers", "ip_to_sgt_mapping_group: ip_to_sgt_mapping_group wrapper test"
    )
    config.addinivalue_line(
        "markers", "identity_groups: identity_groups wrapper test"
    )
    config.addinivalue_line(
        "markers", "identity_sequence: identity_sequence wrapper test"
    )
    config.addinivalue_line(
        "markers", "internal_user: internal_user wrapper test"
    )
    config.addinivalue_line(
        "markers", "licensing: licensing wrapper test"
    )
    config.addinivalue_line(
        "markers", "mdm: mdm wrapper test"
    )
    config.addinivalue_line(
        "markers", "misc: misc wrapper test"
    )
    config.addinivalue_line(
        "markers", "my_device_portal: my_device_portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "native_ipsec: native_ipsec wrapper test"
    )
    config.addinivalue_line(
        "markers", "native_supplicant_profile: native_supplicant_profile wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_authentication_rules: network_access_authentication_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_authorization_exception_rules: network_access_authorization_exception_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_authorization_global_exception_rules: network_access_authorization_global_exception_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_authorization_rules: network_access_authorization_rules wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_conditions: network_access_conditions wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_dictionary: network_access_dictionary wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_dictionary_attribute: network_access_dictionary_attribute wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_dictionary_attributes_list: network_access_dictionary_attributes_list wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_identity_stores: network_access_identity_stores wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_network_conditions: network_access_network_conditions wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_policy_set: network_access_policy_set wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_profiles: network_access_profiles wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_security_groups: network_access_security_groups wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_service_names: network_access_service_names wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_access_time_date_conditions: network_access_time_date_conditions wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_device: network_device wrapper test"
    )
    config.addinivalue_line(
        "markers", "network_device_group: network_device_group wrapper test"
    )
    config.addinivalue_line(
        "markers", "node_deployment: node_deployment wrapper test"
    )
    config.addinivalue_line(
        "markers", "node_group: node_group wrapper test"
    )
    config.addinivalue_line(
        "markers", "node_services: node_services wrapper test"
    )
    config.addinivalue_line(
        "markers", "node_details: node_details wrapper test"
    )
    config.addinivalue_line(
        "markers", "pan_ha: pan_ha wrapper test"
    )
    config.addinivalue_line(
        "markers", "patching: patching wrapper test"
    )
    config.addinivalue_line(
        "markers", "portal_global_setting: portal_global_setting wrapper test"
    )
    config.addinivalue_line(
        "markers", "portal_theme: portal_theme wrapper test"
    )
    config.addinivalue_line(
        "markers", "profiler: profiler wrapper test"
    )
    config.addinivalue_line(
        "markers", "profiler_profile: profiler_profile wrapper test"
    )
    config.addinivalue_line(
        "markers", "provider: provider wrapper test"
    )
    config.addinivalue_line(
        "markers", "psn_node_details_with_radius_service: psn_node_details_with_radius_service wrapper test"
    )
    config.addinivalue_line(
        "markers", "pull_deployment_info: pull_deployment_info wrapper test"
    )
    config.addinivalue_line(
        "markers", "px_grid_settings: px_grid_settings wrapper test"
    )
    config.addinivalue_line(
        "markers", "radius_failure: radius_failure wrapper test"
    )
    config.addinivalue_line(
        "markers", "radius_server_sequence: radius_server_sequence wrapper test"
    )
    config.addinivalue_line(
        "markers", "restid_store: restid_store wrapper test"
    )
    config.addinivalue_line(
        "markers", "replication_status: replication_status wrapper test"
    )
    config.addinivalue_line(
        "markers", "repository: repository wrapper test"
    )
    config.addinivalue_line(
        "markers", "sms_provider: sms_provider wrapper test"
    )
    config.addinivalue_line(
        "markers", "sxp_connections: sxp_connections wrapper test"
    )
    config.addinivalue_line(
        "markers", "sxp_local_bindings: sxp_local_bindings wrapper test"
    )
    config.addinivalue_line(
        "markers", "sxp_vpns: sxp_vpns wrapper test"
    )
    config.addinivalue_line(
        "markers", "security_group_to_virtual_network: security_group_to_virtual_network wrapper test"
    )
    config.addinivalue_line(
        "markers", "security_groups: security_groups wrapper test"
    )
    config.addinivalue_line(
        "markers", "security_groups_acls: security_groups_acls wrapper test"
    )
    config.addinivalue_line(
        "markers", "self_registered_portal: self_registered_portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "session_directory: session_directory wrapper test"
    )
    config.addinivalue_line(
        "markers", "sgt_range_reservation: sgt_range_reservation wrapper test"
    )
    config.addinivalue_line(
        "markers", "sponsor_group: sponsor_group wrapper test"
    )
    config.addinivalue_line(
        "markers", "sponsor_group_member: sponsor_group_member wrapper test"
    )
    config.addinivalue_line(
        "markers", "sponsor_portal: sponsor_portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "sponsored_guest_portal: sponsored_guest_portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "subscriber: subscriber wrapper test"
    )
    config.addinivalue_line(
        "markers", "support_bundle_download: support_bundle_download wrapper test"
    )
    config.addinivalue_line(
        "markers", "support_bundle_status: support_bundle_status wrapper test"
    )
    config.addinivalue_line(
        "markers", "support_bundle_trigger_configuration: support_bundle_trigger_configuration wrapper test"
    )
    config.addinivalue_line(
        "markers", "sync_ise_node: sync_ise_node wrapper test"
    )
    config.addinivalue_line(
        "markers", "system_health: system_health wrapper test"
    )
    config.addinivalue_line(
        "markers", "system_certificate: system_certificate wrapper test"
    )
    config.addinivalue_line(
        "markers", "tacacs_command_sets: tacacs_command_sets wrapper test"
    )
    config.addinivalue_line(
        "markers", "tacacs_external_servers: tacacs_external_servers wrapper test"
    )
    config.addinivalue_line(
        "markers", "tacacs_profile: tacacs_profile wrapper test"
    )
    config.addinivalue_line(
        "markers", "tacacs_server_sequence: tacacs_server_sequence wrapper test"
    )
    config.addinivalue_line(
        "markers", "telemetry_information: telemetry_information wrapper test"
    )
    config.addinivalue_line(
        "markers", "trust_sec_configuration: trust_sec_configuration wrapper test"
    )
    config.addinivalue_line(
        "markers", "trust_sec_sxp: trust_sec_sxp wrapper test"
    )
    config.addinivalue_line(
        "markers", "user_equipment: user_equipment wrapper test"
    )
    config.addinivalue_line(
        "markers", "version_and_patch: version_and_patch wrapper test"
    )
    config.addinivalue_line(
        "markers", "version_info: version_info wrapper test"
    )
    config.addinivalue_line(
        "markers", "custom_attributes: custom_attributes wrapper test"
    )
    config.addinivalue_line(
        "markers", "enable_mfa: enable_mfa wrapper test"
    )
    config.addinivalue_line(
        "markers", "endpoint: endpoint wrapper test"
    )
    config.addinivalue_line(
        "markers", "endpoints: endpoints wrapper test"
    )
    config.addinivalue_line(
        "markers", "full_upgrade: full_upgrade wrapper test"
    )
    config.addinivalue_line(
        "markers", "is_mfa_enabled: is_mfa_enabled wrapper test"
    )
    config.addinivalue_line(
        "markers", "nbar_app: nbar_app wrapper test"
    )
    config.addinivalue_line(
        "markers", "portal: portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "proxy: proxy wrapper test"
    )
    config.addinivalue_line(
        "markers", "px_grid_direct: px_grid_direct wrapper test"
    )
    config.addinivalue_line(
        "markers", "px_grid_node: px_grid_node wrapper test"
    )
    config.addinivalue_line(
        "markers", "sg_vn_mapping: sg_vn_mapping wrapper test"
    )
    config.addinivalue_line(
        "markers", "tasks: tasks wrapper test"
    )
    config.addinivalue_line(
        "markers", "telemetry: telemetry wrapper test"
    )
    config.addinivalue_line(
        "markers", "virtual_network: virtual_network wrapper test"
    )
    config.addinivalue_line(
        "markers", "vn_vlan_mapping: vn_vlan_mapping wrapper test"
    )
