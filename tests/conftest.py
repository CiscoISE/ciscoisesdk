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
    'tests.test_ciscoisesdk',
    'tests.api',
    'tests.api.v3_0_0',
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
        "markers", "anc_policy: anc_policy wrapper test"
    )
    config.addinivalue_line(
        "markers", "active_directory: active_directory wrapper test"
    )
    config.addinivalue_line(
        "markers", "allowed_protocols: allowed_protocols wrapper test"
    )
    config.addinivalue_line(
        "markers", "authentication: authentication wrapper test"
    )
    config.addinivalue_line(
        "markers", "authorization_profile: authorization_profile wrapper test"
    )
    config.addinivalue_line(
        "markers", "backup_and_restore: backup_and_restore wrapper test"
    )
    config.addinivalue_line(
        "markers", "certificates: certificates wrapper test"
    )
    config.addinivalue_line(
        "markers", "custom_caller: custom_caller wrapper test"
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
        "markers", "egress_matrix_cell: egress_matrix_cell wrapper test"
    )
    config.addinivalue_line(
        "markers", "endpoint: endpoint wrapper test"
    )
    config.addinivalue_line(
        "markers", "endpoint_group: endpoint_group wrapper test"
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
        "markers", "guest_smtp_notifications: guest_smtp_notifications wrapper test"
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
        "markers", "identity_group: identity_group wrapper test"
    )
    config.addinivalue_line(
        "markers", "identity_store_sequence: identity_store_sequence wrapper test"
    )
    config.addinivalue_line(
        "markers", "internal_user: internal_user wrapper test"
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
        "markers", "pan_ha: pan_ha wrapper test"
    )
    config.addinivalue_line(
        "markers", "portal: portal wrapper test"
    )
    config.addinivalue_line(
        "markers", "portal_global_setting: portal_global_setting wrapper test"
    )
    config.addinivalue_line(
        "markers", "portal_theme: portal_theme wrapper test"
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
        "markers", "sg_acl: sg_acl wrapper test"
    )
    config.addinivalue_line(
        "markers", "sgt: sgt wrapper test"
    )
    config.addinivalue_line(
        "markers", "sms_provider: sms_provider wrapper test"
    )
    config.addinivalue_line(
        "markers", "self_registered_portal: self_registered_portal wrapper test"
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
        "markers", "sync_ise_node: sync_ise_node wrapper test"
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
