
# -*- coding: utf-8 -*-
"""Test suite for the community-developed Python SDK for the Identity Services Engine APIs.

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

import ciscoisesdk
from tests.environment import (
    IDENTITY_SERVICES_ENGINE_USERNAME, IDENTITY_SERVICES_ENGINE_PASSWORD,
    IDENTITY_SERVICES_ENGINE_ENCODED_AUTH, IDENTITY_SERVICES_ENGINE_VERSION,
)

from ciscoisesdk.api.authentication import Authentication
from ciscoisesdk.api.v3_0_0.aci_bindings import \
    AciBindings as AciBindings_v3_0_0
from ciscoisesdk.api.v3_0_0.aci_settings import \
    AciSettings as AciSettings_v3_0_0
from ciscoisesdk.api.v3_0_0.anc_endpoint import \
    AncEndpoint as AncEndpoint_v3_0_0
from ciscoisesdk.api.v3_0_0.active_directory import \
    ActiveDirectory as ActiveDirectory_v3_0_0
from ciscoisesdk.api.v3_0_0.admin_user import \
    AdminUser as AdminUser_v3_0_0
from ciscoisesdk.api.v3_0_0.allowed_protocols import \
    AllowedProtocols as AllowedProtocols_v3_0_0
from ciscoisesdk.api.v3_0_0.anc_policy import \
    AncPolicy as AncPolicy_v3_0_0
from ciscoisesdk.api.v3_0_0.authorization_profile import \
    AuthorizationProfile as AuthorizationProfile_v3_0_0
from ciscoisesdk.api.v3_0_0.byod_portal import \
    ByodPortal as ByodPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.backup_and_restore import \
    BackupAndRestore as BackupAndRestore_v3_0_0
from ciscoisesdk.api.v3_0_0.certificate_profile import \
    CertificateProfile as CertificateProfile_v3_0_0
from ciscoisesdk.api.v3_0_0.certificate_template import \
    CertificateTemplate as CertificateTemplate_v3_0_0
from ciscoisesdk.api.v3_0_0.certificates import \
    Certificates as Certificates_v3_0_0
from ciscoisesdk.api.v3_0_0.clear_threats_and_vulnerabilities import \
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_0_0
from ciscoisesdk.api.v3_0_0.consumer import \
    Consumer as Consumer_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_authentication_rules import \
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_authorization_exception_rules import \
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_authorization_global_exception_rules import \
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_authorization_rules import \
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_command_set import \
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_conditions import \
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_dictionary_attributes_list import \
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_identity_stores import \
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_network_conditions import \
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_policy_set import \
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_profiles import \
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_service_names import \
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_0_0
from ciscoisesdk.api.v3_0_0.device_administration_time_date_conditions import \
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_0_0
from ciscoisesdk.api.v3_0_0.downloadable_acl import \
    DownloadableAcl as DownloadableAcl_v3_0_0
from ciscoisesdk.api.v3_0_0.egress_matrix_cell import \
    EgressMatrixCell as EgressMatrixCell_v3_0_0
from ciscoisesdk.api.v3_0_0.endpoint_certificate import \
    EndpointCertificate as EndpointCertificate_v3_0_0
from ciscoisesdk.api.v3_0_0.endpoint_identity_group import \
    EndpointIdentityGroup as EndpointIdentityGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.external_radius_server import \
    ExternalRadiusServer as ExternalRadiusServer_v3_0_0
from ciscoisesdk.api.v3_0_0.filter_policy import \
    FilterPolicy as FilterPolicy_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_location import \
    GuestLocation as GuestLocation_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_smtp_notification_configuration import \
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_ssid import \
    GuestSsid as GuestSsid_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_type import \
    GuestType as GuestType_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_user import \
    GuestUser as GuestUser_v3_0_0
from ciscoisesdk.api.v3_0_0.hotspot_portal import \
    HotspotPortal as HotspotPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.ip_to_sgt_mapping import \
    IpToSgtMapping as IpToSgtMapping_v3_0_0
from ciscoisesdk.api.v3_0_0.ip_to_sgt_mapping_group import \
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.identity_groups import \
    IdentityGroups as IdentityGroups_v3_0_0
from ciscoisesdk.api.v3_0_0.identity_sequence import \
    IdentitySequence as IdentitySequence_v3_0_0
from ciscoisesdk.api.v3_0_0.internal_user import \
    InternalUser as InternalUser_v3_0_0
from ciscoisesdk.api.v3_0_0.mdm import \
    Mdm as Mdm_v3_0_0
from ciscoisesdk.api.v3_0_0.misc import \
    Misc as Misc_v3_0_0
from ciscoisesdk.api.v3_0_0.my_device_portal import \
    MyDevicePortal as MyDevicePortal_v3_0_0
from ciscoisesdk.api.v3_0_0.native_supplicant_profile import \
    NativeSupplicantProfile as NativeSupplicantProfile_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_authentication_rules import \
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_authorization_exception_rules import \
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_authorization_global_exception_rules import \
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_authorization_rules import \
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_conditions import \
    NetworkAccessConditions as NetworkAccessConditions_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_dictionary import \
    NetworkAccessDictionary as NetworkAccessDictionary_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_dictionary_attribute import \
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_dictionary_attributes_list import \
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_identity_stores import \
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_network_conditions import \
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_policy_set import \
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_profiles import \
    NetworkAccessProfiles as NetworkAccessProfiles_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_security_groups import \
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_service_names import \
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_0_0
from ciscoisesdk.api.v3_0_0.network_access_time_date_conditions import \
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_0_0
from ciscoisesdk.api.v3_0_0.network_device import \
    NetworkDevice as NetworkDevice_v3_0_0
from ciscoisesdk.api.v3_0_0.network_device_group import \
    NetworkDeviceGroup as NetworkDeviceGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.node_deployment import \
    NodeDeployment as NodeDeployment_v3_0_0
from ciscoisesdk.api.v3_0_0.node_group import \
    NodeGroup as NodeGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.node_details import \
    NodeDetails as NodeDetails_v3_0_0
from ciscoisesdk.api.v3_0_0.pan_ha import \
    PanHa as PanHa_v3_0_0
from ciscoisesdk.api.v3_0_0.portal_global_setting import \
    PortalGlobalSetting as PortalGlobalSetting_v3_0_0
from ciscoisesdk.api.v3_0_0.portal_theme import \
    PortalTheme as PortalTheme_v3_0_0
from ciscoisesdk.api.v3_0_0.profiler import \
    Profiler as Profiler_v3_0_0
from ciscoisesdk.api.v3_0_0.profiler_profile import \
    ProfilerProfile as ProfilerProfile_v3_0_0
from ciscoisesdk.api.v3_0_0.provider import \
    Provider as Provider_v3_0_0
from ciscoisesdk.api.v3_0_0.psn_node_details_with_radius_service import \
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_0_0
from ciscoisesdk.api.v3_0_0.pull_deployment_info import \
    PullDeploymentInfo as PullDeploymentInfo_v3_0_0
from ciscoisesdk.api.v3_0_0.px_grid_settings import \
    PxGridSettings as PxGridSettings_v3_0_0
from ciscoisesdk.api.v3_0_0.radius_failure import \
    RadiusFailure as RadiusFailure_v3_0_0
from ciscoisesdk.api.v3_0_0.radius_server_sequence import \
    RadiusServerSequence as RadiusServerSequence_v3_0_0
from ciscoisesdk.api.v3_0_0.restid_store import \
    RestidStore as RestidStore_v3_0_0
from ciscoisesdk.api.v3_0_0.replication_status import \
    ReplicationStatus as ReplicationStatus_v3_0_0
from ciscoisesdk.api.v3_0_0.repository import \
    Repository as Repository_v3_0_0
from ciscoisesdk.api.v3_0_0.sms_provider import \
    SmsProvider as SmsProvider_v3_0_0
from ciscoisesdk.api.v3_0_0.sxp_connections import \
    SxpConnections as SxpConnections_v3_0_0
from ciscoisesdk.api.v3_0_0.sxp_local_bindings import \
    SxpLocalBindings as SxpLocalBindings_v3_0_0
from ciscoisesdk.api.v3_0_0.sxp_vpns import \
    SxpVpns as SxpVpns_v3_0_0
from ciscoisesdk.api.v3_0_0.security_group_to_virtual_network import \
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_0_0
from ciscoisesdk.api.v3_0_0.security_groups import \
    SecurityGroups as SecurityGroups_v3_0_0
from ciscoisesdk.api.v3_0_0.security_groups_acls import \
    SecurityGroupsAcls as SecurityGroupsAcls_v3_0_0
from ciscoisesdk.api.v3_0_0.self_registered_portal import \
    SelfRegisteredPortal as SelfRegisteredPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.session_directory import \
    SessionDirectory as SessionDirectory_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsor_group import \
    SponsorGroup as SponsorGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsor_group_member import \
    SponsorGroupMember as SponsorGroupMember_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsor_portal import \
    SponsorPortal as SponsorPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsored_guest_portal import \
    SponsoredGuestPortal as SponsoredGuestPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.support_bundle_download import \
    SupportBundleDownload as SupportBundleDownload_v3_0_0
from ciscoisesdk.api.v3_0_0.support_bundle_status import \
    SupportBundleStatus as SupportBundleStatus_v3_0_0
from ciscoisesdk.api.v3_0_0.support_bundle_trigger_configuration import \
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_0_0
from ciscoisesdk.api.v3_0_0.sync_ise_node import \
    SyncIseNode as SyncIseNode_v3_0_0
from ciscoisesdk.api.v3_0_0.system_health import \
    SystemHealth as SystemHealth_v3_0_0
from ciscoisesdk.api.v3_0_0.system_certificate import \
    SystemCertificate as SystemCertificate_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_command_sets import \
    TacacsCommandSets as TacacsCommandSets_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_external_servers import \
    TacacsExternalServers as TacacsExternalServers_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_profile import \
    TacacsProfile as TacacsProfile_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_server_sequence import \
    TacacsServerSequence as TacacsServerSequence_v3_0_0
from ciscoisesdk.api.v3_0_0.telemetry_information import \
    TelemetryInformation as TelemetryInformation_v3_0_0
from ciscoisesdk.api.v3_0_0.trust_sec_configuration import \
    TrustSecConfiguration as TrustSecConfiguration_v3_0_0
from ciscoisesdk.api.v3_0_0.trust_sec_sxp import \
    TrustSecSxp as TrustSecSxp_v3_0_0
from ciscoisesdk.api.v3_0_0.version_and_patch import \
    VersionAndPatch as VersionAndPatch_v3_0_0
from ciscoisesdk.api.v3_0_0.version_info import \
    VersionInfo as VersionInfo_v3_0_0
from ciscoisesdk.api.v3_0_0.endpoint import \
    Endpoint as Endpoint_v3_0_0
from ciscoisesdk.api.v3_0_0.portal import \
    Portal as Portal_v3_0_0
from ciscoisesdk.api.v3_0_0.px_grid_node import \
    PxGridNode as PxGridNode_v3_0_0
from ciscoisesdk.api.v3_0_0.tasks import \
    Tasks as Tasks_v3_0_0
from ciscoisesdk.api.v3_1_0.aci_bindings import \
    AciBindings as AciBindings_v3_1_0
from ciscoisesdk.api.v3_1_0.aci_settings import \
    AciSettings as AciSettings_v3_1_0
from ciscoisesdk.api.v3_1_0.anc_endpoint import \
    AncEndpoint as AncEndpoint_v3_1_0
from ciscoisesdk.api.v3_1_0.active_directory import \
    ActiveDirectory as ActiveDirectory_v3_1_0
from ciscoisesdk.api.v3_1_0.admin_user import \
    AdminUser as AdminUser_v3_1_0
from ciscoisesdk.api.v3_1_0.allowed_protocols import \
    AllowedProtocols as AllowedProtocols_v3_1_0
from ciscoisesdk.api.v3_1_0.anc_policy import \
    AncPolicy as AncPolicy_v3_1_0
from ciscoisesdk.api.v3_1_0.authorization_profile import \
    AuthorizationProfile as AuthorizationProfile_v3_1_0
from ciscoisesdk.api.v3_1_0.byod_portal import \
    ByodPortal as ByodPortal_v3_1_0
from ciscoisesdk.api.v3_1_0.backup_and_restore import \
    BackupAndRestore as BackupAndRestore_v3_1_0
from ciscoisesdk.api.v3_1_0.certificate_profile import \
    CertificateProfile as CertificateProfile_v3_1_0
from ciscoisesdk.api.v3_1_0.certificate_template import \
    CertificateTemplate as CertificateTemplate_v3_1_0
from ciscoisesdk.api.v3_1_0.certificates import \
    Certificates as Certificates_v3_1_0
from ciscoisesdk.api.v3_1_0.clear_threats_and_vulnerabilities import \
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_1_0
from ciscoisesdk.api.v3_1_0.consumer import \
    Consumer as Consumer_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_authentication_rules import \
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_authorization_exception_rules import \
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_authorization_global_exception_rules import \
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_authorization_rules import \
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_command_set import \
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_conditions import \
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_dictionary_attributes_list import \
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_identity_stores import \
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_network_conditions import \
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_policy_set import \
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_profiles import \
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_service_names import \
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_1_0
from ciscoisesdk.api.v3_1_0.device_administration_time_date_conditions import \
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_1_0
from ciscoisesdk.api.v3_1_0.downloadable_acl import \
    DownloadableAcl as DownloadableAcl_v3_1_0
from ciscoisesdk.api.v3_1_0.egress_matrix_cell import \
    EgressMatrixCell as EgressMatrixCell_v3_1_0
from ciscoisesdk.api.v3_1_0.endpoint_certificate import \
    EndpointCertificate as EndpointCertificate_v3_1_0
from ciscoisesdk.api.v3_1_0.endpoint_identity_group import \
    EndpointIdentityGroup as EndpointIdentityGroup_v3_1_0
from ciscoisesdk.api.v3_1_0.external_radius_server import \
    ExternalRadiusServer as ExternalRadiusServer_v3_1_0
from ciscoisesdk.api.v3_1_0.filter_policy import \
    FilterPolicy as FilterPolicy_v3_1_0
from ciscoisesdk.api.v3_1_0.guest_location import \
    GuestLocation as GuestLocation_v3_1_0
from ciscoisesdk.api.v3_1_0.guest_smtp_notification_configuration import \
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_1_0
from ciscoisesdk.api.v3_1_0.guest_ssid import \
    GuestSsid as GuestSsid_v3_1_0
from ciscoisesdk.api.v3_1_0.guest_type import \
    GuestType as GuestType_v3_1_0
from ciscoisesdk.api.v3_1_0.guest_user import \
    GuestUser as GuestUser_v3_1_0
from ciscoisesdk.api.v3_1_0.hotspot_portal import \
    HotspotPortal as HotspotPortal_v3_1_0
from ciscoisesdk.api.v3_1_0.ip_to_sgt_mapping import \
    IpToSgtMapping as IpToSgtMapping_v3_1_0
from ciscoisesdk.api.v3_1_0.ip_to_sgt_mapping_group import \
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_1_0
from ciscoisesdk.api.v3_1_0.identity_groups import \
    IdentityGroups as IdentityGroups_v3_1_0
from ciscoisesdk.api.v3_1_0.identity_sequence import \
    IdentitySequence as IdentitySequence_v3_1_0
from ciscoisesdk.api.v3_1_0.internal_user import \
    InternalUser as InternalUser_v3_1_0
from ciscoisesdk.api.v3_1_0.mdm import \
    Mdm as Mdm_v3_1_0
from ciscoisesdk.api.v3_1_0.misc import \
    Misc as Misc_v3_1_0
from ciscoisesdk.api.v3_1_0.my_device_portal import \
    MyDevicePortal as MyDevicePortal_v3_1_0
from ciscoisesdk.api.v3_1_0.native_supplicant_profile import \
    NativeSupplicantProfile as NativeSupplicantProfile_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_authentication_rules import \
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_authorization_exception_rules import \
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_authorization_global_exception_rules import \
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_authorization_rules import \
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_conditions import \
    NetworkAccessConditions as NetworkAccessConditions_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_dictionary import \
    NetworkAccessDictionary as NetworkAccessDictionary_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_dictionary_attribute import \
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_dictionary_attributes_list import \
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_identity_stores import \
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_network_conditions import \
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_policy_set import \
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_profiles import \
    NetworkAccessProfiles as NetworkAccessProfiles_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_security_groups import \
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_service_names import \
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_1_0
from ciscoisesdk.api.v3_1_0.network_access_time_date_conditions import \
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_1_0
from ciscoisesdk.api.v3_1_0.network_device import \
    NetworkDevice as NetworkDevice_v3_1_0
from ciscoisesdk.api.v3_1_0.network_device_group import \
    NetworkDeviceGroup as NetworkDeviceGroup_v3_1_0
from ciscoisesdk.api.v3_1_0.node_deployment import \
    NodeDeployment as NodeDeployment_v3_1_0
from ciscoisesdk.api.v3_1_0.node_group import \
    NodeGroup as NodeGroup_v3_1_0
from ciscoisesdk.api.v3_1_0.node_details import \
    NodeDetails as NodeDetails_v3_1_0
from ciscoisesdk.api.v3_1_0.pan_ha import \
    PanHa as PanHa_v3_1_0
from ciscoisesdk.api.v3_1_0.portal_global_setting import \
    PortalGlobalSetting as PortalGlobalSetting_v3_1_0
from ciscoisesdk.api.v3_1_0.portal_theme import \
    PortalTheme as PortalTheme_v3_1_0
from ciscoisesdk.api.v3_1_0.profiler import \
    Profiler as Profiler_v3_1_0
from ciscoisesdk.api.v3_1_0.profiler_profile import \
    ProfilerProfile as ProfilerProfile_v3_1_0
from ciscoisesdk.api.v3_1_0.provider import \
    Provider as Provider_v3_1_0
from ciscoisesdk.api.v3_1_0.psn_node_details_with_radius_service import \
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_1_0
from ciscoisesdk.api.v3_1_0.pull_deployment_info import \
    PullDeploymentInfo as PullDeploymentInfo_v3_1_0
from ciscoisesdk.api.v3_1_0.px_grid_settings import \
    PxGridSettings as PxGridSettings_v3_1_0
from ciscoisesdk.api.v3_1_0.radius_failure import \
    RadiusFailure as RadiusFailure_v3_1_0
from ciscoisesdk.api.v3_1_0.radius_server_sequence import \
    RadiusServerSequence as RadiusServerSequence_v3_1_0
from ciscoisesdk.api.v3_1_0.restid_store import \
    RestidStore as RestidStore_v3_1_0
from ciscoisesdk.api.v3_1_0.replication_status import \
    ReplicationStatus as ReplicationStatus_v3_1_0
from ciscoisesdk.api.v3_1_0.repository import \
    Repository as Repository_v3_1_0
from ciscoisesdk.api.v3_1_0.sms_provider import \
    SmsProvider as SmsProvider_v3_1_0
from ciscoisesdk.api.v3_1_0.sxp_connections import \
    SxpConnections as SxpConnections_v3_1_0
from ciscoisesdk.api.v3_1_0.sxp_local_bindings import \
    SxpLocalBindings as SxpLocalBindings_v3_1_0
from ciscoisesdk.api.v3_1_0.sxp_vpns import \
    SxpVpns as SxpVpns_v3_1_0
from ciscoisesdk.api.v3_1_0.security_group_to_virtual_network import \
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_1_0
from ciscoisesdk.api.v3_1_0.security_groups import \
    SecurityGroups as SecurityGroups_v3_1_0
from ciscoisesdk.api.v3_1_0.security_groups_acls import \
    SecurityGroupsAcls as SecurityGroupsAcls_v3_1_0
from ciscoisesdk.api.v3_1_0.self_registered_portal import \
    SelfRegisteredPortal as SelfRegisteredPortal_v3_1_0
from ciscoisesdk.api.v3_1_0.session_directory import \
    SessionDirectory as SessionDirectory_v3_1_0
from ciscoisesdk.api.v3_1_0.sponsor_group import \
    SponsorGroup as SponsorGroup_v3_1_0
from ciscoisesdk.api.v3_1_0.sponsor_group_member import \
    SponsorGroupMember as SponsorGroupMember_v3_1_0
from ciscoisesdk.api.v3_1_0.sponsor_portal import \
    SponsorPortal as SponsorPortal_v3_1_0
from ciscoisesdk.api.v3_1_0.sponsored_guest_portal import \
    SponsoredGuestPortal as SponsoredGuestPortal_v3_1_0
from ciscoisesdk.api.v3_1_0.support_bundle_download import \
    SupportBundleDownload as SupportBundleDownload_v3_1_0
from ciscoisesdk.api.v3_1_0.support_bundle_status import \
    SupportBundleStatus as SupportBundleStatus_v3_1_0
from ciscoisesdk.api.v3_1_0.support_bundle_trigger_configuration import \
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_1_0
from ciscoisesdk.api.v3_1_0.sync_ise_node import \
    SyncIseNode as SyncIseNode_v3_1_0
from ciscoisesdk.api.v3_1_0.system_health import \
    SystemHealth as SystemHealth_v3_1_0
from ciscoisesdk.api.v3_1_0.system_certificate import \
    SystemCertificate as SystemCertificate_v3_1_0
from ciscoisesdk.api.v3_1_0.tacacs_command_sets import \
    TacacsCommandSets as TacacsCommandSets_v3_1_0
from ciscoisesdk.api.v3_1_0.tacacs_external_servers import \
    TacacsExternalServers as TacacsExternalServers_v3_1_0
from ciscoisesdk.api.v3_1_0.tacacs_profile import \
    TacacsProfile as TacacsProfile_v3_1_0
from ciscoisesdk.api.v3_1_0.tacacs_server_sequence import \
    TacacsServerSequence as TacacsServerSequence_v3_1_0
from ciscoisesdk.api.v3_1_0.telemetry_information import \
    TelemetryInformation as TelemetryInformation_v3_1_0
from ciscoisesdk.api.v3_1_0.trust_sec_configuration import \
    TrustSecConfiguration as TrustSecConfiguration_v3_1_0
from ciscoisesdk.api.v3_1_0.trust_sec_sxp import \
    TrustSecSxp as TrustSecSxp_v3_1_0
from ciscoisesdk.api.v3_1_0.version_and_patch import \
    VersionAndPatch as VersionAndPatch_v3_1_0
from ciscoisesdk.api.v3_1_0.version_info import \
    VersionInfo as VersionInfo_v3_1_0
from ciscoisesdk.api.v3_1_0.endpoint import \
    Endpoint as Endpoint_v3_1_0
from ciscoisesdk.api.v3_1_0.nbar_app import \
    NbarApp as NbarApp_v3_1_0
from ciscoisesdk.api.v3_1_0.portal import \
    Portal as Portal_v3_1_0
from ciscoisesdk.api.v3_1_0.px_grid_node import \
    PxGridNode as PxGridNode_v3_1_0
from ciscoisesdk.api.v3_1_0.sg_vn_mapping import \
    SgVnMapping as SgVnMapping_v3_1_0
from ciscoisesdk.api.v3_1_0.tasks import \
    Tasks as Tasks_v3_1_0
from ciscoisesdk.api.v3_1_0.virtual_network import \
    VirtualNetwork as VirtualNetwork_v3_1_0
from ciscoisesdk.api.v3_1_0.vn_vlan_mapping import \
    VnVlanMapping as VnVlanMapping_v3_1_0
from ciscoisesdk.api.v3_1_1.aci_bindings import \
    AciBindings as AciBindings_v3_1_1
from ciscoisesdk.api.v3_1_1.aci_settings import \
    AciSettings as AciSettings_v3_1_1
from ciscoisesdk.api.v3_1_1.anc_endpoint import \
    AncEndpoint as AncEndpoint_v3_1_1
from ciscoisesdk.api.v3_1_1.active_directory import \
    ActiveDirectory as ActiveDirectory_v3_1_1
from ciscoisesdk.api.v3_1_1.admin_user import \
    AdminUser as AdminUser_v3_1_1
from ciscoisesdk.api.v3_1_1.allowed_protocols import \
    AllowedProtocols as AllowedProtocols_v3_1_1
from ciscoisesdk.api.v3_1_1.anc_policy import \
    AncPolicy as AncPolicy_v3_1_1
from ciscoisesdk.api.v3_1_1.authorization_profile import \
    AuthorizationProfile as AuthorizationProfile_v3_1_1
from ciscoisesdk.api.v3_1_1.byod_portal import \
    ByodPortal as ByodPortal_v3_1_1
from ciscoisesdk.api.v3_1_1.backup_and_restore import \
    BackupAndRestore as BackupAndRestore_v3_1_1
from ciscoisesdk.api.v3_1_1.certificate_profile import \
    CertificateProfile as CertificateProfile_v3_1_1
from ciscoisesdk.api.v3_1_1.certificate_template import \
    CertificateTemplate as CertificateTemplate_v3_1_1
from ciscoisesdk.api.v3_1_1.certificates import \
    Certificates as Certificates_v3_1_1
from ciscoisesdk.api.v3_1_1.clear_threats_and_vulnerabilities import \
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_1_1
from ciscoisesdk.api.v3_1_1.consumer import \
    Consumer as Consumer_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_authentication_rules import \
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_authorization_exception_rules import \
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_authorization_global_exception_rules import \
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_authorization_rules import \
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_command_set import \
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_conditions import \
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_dictionary_attributes_list import \
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_identity_stores import \
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_network_conditions import \
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_policy_set import \
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_profiles import \
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_service_names import \
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_1_1
from ciscoisesdk.api.v3_1_1.device_administration_time_date_conditions import \
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_1_1
from ciscoisesdk.api.v3_1_1.downloadable_acl import \
    DownloadableAcl as DownloadableAcl_v3_1_1
from ciscoisesdk.api.v3_1_1.egress_matrix_cell import \
    EgressMatrixCell as EgressMatrixCell_v3_1_1
from ciscoisesdk.api.v3_1_1.endpoint_certificate import \
    EndpointCertificate as EndpointCertificate_v3_1_1
from ciscoisesdk.api.v3_1_1.endpoint_identity_group import \
    EndpointIdentityGroup as EndpointIdentityGroup_v3_1_1
from ciscoisesdk.api.v3_1_1.external_radius_server import \
    ExternalRadiusServer as ExternalRadiusServer_v3_1_1
from ciscoisesdk.api.v3_1_1.filter_policy import \
    FilterPolicy as FilterPolicy_v3_1_1
from ciscoisesdk.api.v3_1_1.guest_location import \
    GuestLocation as GuestLocation_v3_1_1
from ciscoisesdk.api.v3_1_1.guest_smtp_notification_configuration import \
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_1_1
from ciscoisesdk.api.v3_1_1.guest_ssid import \
    GuestSsid as GuestSsid_v3_1_1
from ciscoisesdk.api.v3_1_1.guest_type import \
    GuestType as GuestType_v3_1_1
from ciscoisesdk.api.v3_1_1.guest_user import \
    GuestUser as GuestUser_v3_1_1
from ciscoisesdk.api.v3_1_1.hotspot_portal import \
    HotspotPortal as HotspotPortal_v3_1_1
from ciscoisesdk.api.v3_1_1.ip_to_sgt_mapping import \
    IpToSgtMapping as IpToSgtMapping_v3_1_1
from ciscoisesdk.api.v3_1_1.ip_to_sgt_mapping_group import \
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_1_1
from ciscoisesdk.api.v3_1_1.identity_groups import \
    IdentityGroups as IdentityGroups_v3_1_1
from ciscoisesdk.api.v3_1_1.identity_sequence import \
    IdentitySequence as IdentitySequence_v3_1_1
from ciscoisesdk.api.v3_1_1.internal_user import \
    InternalUser as InternalUser_v3_1_1
from ciscoisesdk.api.v3_1_1.mdm import \
    Mdm as Mdm_v3_1_1
from ciscoisesdk.api.v3_1_1.misc import \
    Misc as Misc_v3_1_1
from ciscoisesdk.api.v3_1_1.my_device_portal import \
    MyDevicePortal as MyDevicePortal_v3_1_1
from ciscoisesdk.api.v3_1_1.native_supplicant_profile import \
    NativeSupplicantProfile as NativeSupplicantProfile_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_authentication_rules import \
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_authorization_exception_rules import \
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_authorization_global_exception_rules import \
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_authorization_rules import \
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_conditions import \
    NetworkAccessConditions as NetworkAccessConditions_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_dictionary import \
    NetworkAccessDictionary as NetworkAccessDictionary_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_dictionary_attribute import \
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_dictionary_attributes_list import \
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_identity_stores import \
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_network_conditions import \
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_policy_set import \
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_profiles import \
    NetworkAccessProfiles as NetworkAccessProfiles_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_security_groups import \
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_service_names import \
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_1_1
from ciscoisesdk.api.v3_1_1.network_access_time_date_conditions import \
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_1_1
from ciscoisesdk.api.v3_1_1.network_device import \
    NetworkDevice as NetworkDevice_v3_1_1
from ciscoisesdk.api.v3_1_1.network_device_group import \
    NetworkDeviceGroup as NetworkDeviceGroup_v3_1_1
from ciscoisesdk.api.v3_1_1.node_deployment import \
    NodeDeployment as NodeDeployment_v3_1_1
from ciscoisesdk.api.v3_1_1.node_group import \
    NodeGroup as NodeGroup_v3_1_1
from ciscoisesdk.api.v3_1_1.node_details import \
    NodeDetails as NodeDetails_v3_1_1
from ciscoisesdk.api.v3_1_1.pan_ha import \
    PanHa as PanHa_v3_1_1
from ciscoisesdk.api.v3_1_1.portal_global_setting import \
    PortalGlobalSetting as PortalGlobalSetting_v3_1_1
from ciscoisesdk.api.v3_1_1.portal_theme import \
    PortalTheme as PortalTheme_v3_1_1
from ciscoisesdk.api.v3_1_1.profiler import \
    Profiler as Profiler_v3_1_1
from ciscoisesdk.api.v3_1_1.profiler_profile import \
    ProfilerProfile as ProfilerProfile_v3_1_1
from ciscoisesdk.api.v3_1_1.provider import \
    Provider as Provider_v3_1_1
from ciscoisesdk.api.v3_1_1.psn_node_details_with_radius_service import \
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_1_1
from ciscoisesdk.api.v3_1_1.pull_deployment_info import \
    PullDeploymentInfo as PullDeploymentInfo_v3_1_1
from ciscoisesdk.api.v3_1_1.px_grid_settings import \
    PxGridSettings as PxGridSettings_v3_1_1
from ciscoisesdk.api.v3_1_1.radius_failure import \
    RadiusFailure as RadiusFailure_v3_1_1
from ciscoisesdk.api.v3_1_1.radius_server_sequence import \
    RadiusServerSequence as RadiusServerSequence_v3_1_1
from ciscoisesdk.api.v3_1_1.restid_store import \
    RestidStore as RestidStore_v3_1_1
from ciscoisesdk.api.v3_1_1.repository import \
    Repository as Repository_v3_1_1
from ciscoisesdk.api.v3_1_1.sms_provider import \
    SmsProvider as SmsProvider_v3_1_1
from ciscoisesdk.api.v3_1_1.sxp_connections import \
    SxpConnections as SxpConnections_v3_1_1
from ciscoisesdk.api.v3_1_1.sxp_local_bindings import \
    SxpLocalBindings as SxpLocalBindings_v3_1_1
from ciscoisesdk.api.v3_1_1.sxp_vpns import \
    SxpVpns as SxpVpns_v3_1_1
from ciscoisesdk.api.v3_1_1.security_group_to_virtual_network import \
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_1_1
from ciscoisesdk.api.v3_1_1.security_groups import \
    SecurityGroups as SecurityGroups_v3_1_1
from ciscoisesdk.api.v3_1_1.security_groups_acls import \
    SecurityGroupsAcls as SecurityGroupsAcls_v3_1_1
from ciscoisesdk.api.v3_1_1.self_registered_portal import \
    SelfRegisteredPortal as SelfRegisteredPortal_v3_1_1
from ciscoisesdk.api.v3_1_1.session_directory import \
    SessionDirectory as SessionDirectory_v3_1_1
from ciscoisesdk.api.v3_1_1.sponsor_group import \
    SponsorGroup as SponsorGroup_v3_1_1
from ciscoisesdk.api.v3_1_1.sponsor_group_member import \
    SponsorGroupMember as SponsorGroupMember_v3_1_1
from ciscoisesdk.api.v3_1_1.sponsor_portal import \
    SponsorPortal as SponsorPortal_v3_1_1
from ciscoisesdk.api.v3_1_1.sponsored_guest_portal import \
    SponsoredGuestPortal as SponsoredGuestPortal_v3_1_1
from ciscoisesdk.api.v3_1_1.support_bundle_download import \
    SupportBundleDownload as SupportBundleDownload_v3_1_1
from ciscoisesdk.api.v3_1_1.support_bundle_status import \
    SupportBundleStatus as SupportBundleStatus_v3_1_1
from ciscoisesdk.api.v3_1_1.support_bundle_trigger_configuration import \
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_1_1
from ciscoisesdk.api.v3_1_1.system_health import \
    SystemHealth as SystemHealth_v3_1_1
from ciscoisesdk.api.v3_1_1.system_certificate import \
    SystemCertificate as SystemCertificate_v3_1_1
from ciscoisesdk.api.v3_1_1.tacacs_command_sets import \
    TacacsCommandSets as TacacsCommandSets_v3_1_1
from ciscoisesdk.api.v3_1_1.tacacs_external_servers import \
    TacacsExternalServers as TacacsExternalServers_v3_1_1
from ciscoisesdk.api.v3_1_1.tacacs_profile import \
    TacacsProfile as TacacsProfile_v3_1_1
from ciscoisesdk.api.v3_1_1.tacacs_server_sequence import \
    TacacsServerSequence as TacacsServerSequence_v3_1_1
from ciscoisesdk.api.v3_1_1.telemetry_information import \
    TelemetryInformation as TelemetryInformation_v3_1_1
from ciscoisesdk.api.v3_1_1.trust_sec_configuration import \
    TrustSecConfiguration as TrustSecConfiguration_v3_1_1
from ciscoisesdk.api.v3_1_1.trust_sec_sxp import \
    TrustSecSxp as TrustSecSxp_v3_1_1
from ciscoisesdk.api.v3_1_1.version_and_patch import \
    VersionAndPatch as VersionAndPatch_v3_1_1
from ciscoisesdk.api.v3_1_1.version_info import \
    VersionInfo as VersionInfo_v3_1_1
from ciscoisesdk.api.v3_1_1.endpoint import \
    Endpoint as Endpoint_v3_1_1
from ciscoisesdk.api.v3_1_1.portal import \
    Portal as Portal_v3_1_1
from ciscoisesdk.api.v3_1_1.px_grid_node import \
    PxGridNode as PxGridNode_v3_1_1
from ciscoisesdk.api.v3_1_1.tasks import \
    Tasks as Tasks_v3_1_1
from ciscoisesdk.api.custom_caller import CustomCaller

from tests.config import (
    DEFAULT_VERIFY,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT
)
import pytest


@pytest.mark.ciscoisesdk
class TestIdentityServicesEngineSDK:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""
        # Identity Services Engine API Wrapper
        assert hasattr(ciscoisesdk, "IdentityServicesEngineAPI")

        # Exceptions
        assert hasattr(ciscoisesdk, "AccessTokenError")
        assert hasattr(ciscoisesdk, "ApiError")
        assert hasattr(ciscoisesdk, "ciscoisesdkException")
        assert hasattr(ciscoisesdk, "DownloadFailure")
        assert hasattr(ciscoisesdk, "MalformedRequest")
        assert hasattr(ciscoisesdk, "RateLimitError")
        assert hasattr(ciscoisesdk, "RateLimitWarning")
        assert hasattr(ciscoisesdk, "VersionError")

        # Data Models
        assert hasattr(ciscoisesdk, "mydict_data_factory")

    @pytest.mark.ciscoisesdk
    def test_default_base_url(self, api, base_url):
        assert api.base_url == base_url

    @pytest.mark.ciscoisesdk
    def test_custom_base_url(self):
        custom_url = "https://custom.domain.com/v1/"
        connection_object = ciscoisesdk.IdentityServicesEngineAPI(username=IDENTITY_SERVICES_ENGINE_USERNAME,
                                                                  password=IDENTITY_SERVICES_ENGINE_PASSWORD,
                                                                  encoded_auth=IDENTITY_SERVICES_ENGINE_ENCODED_AUTH,
                                                                  base_url=custom_url,
                                                                  verify=DEFAULT_VERIFY,
                                                                  version=IDENTITY_SERVICES_ENGINE_VERSION,
                                                                  uses_api_gateway=True)
        assert connection_object.base_url == custom_url

    @pytest.mark.ciscoisesdk
    def test_default_single_request_timeout(self, api):
        assert api.single_request_timeout == \
            DEFAULT_SINGLE_REQUEST_TIMEOUT

    @pytest.mark.ciscoisesdk
    def test_custom_single_request_timeout(self, base_url):
        custom_timeout = 10
        connection_object = ciscoisesdk.IdentityServicesEngineAPI(username=IDENTITY_SERVICES_ENGINE_USERNAME,
                                                                  password=IDENTITY_SERVICES_ENGINE_PASSWORD,
                                                                  encoded_auth=IDENTITY_SERVICES_ENGINE_ENCODED_AUTH,
                                                                  base_url=base_url,
                                                                  single_request_timeout=custom_timeout,
                                                                  verify=DEFAULT_VERIFY,
                                                                  version=IDENTITY_SERVICES_ENGINE_VERSION,
                                                                  uses_api_gateway=True)
        assert connection_object.single_request_timeout == custom_timeout

    @pytest.mark.ciscoisesdk
    def test_default_wait_on_rate_limit(self, api):
        assert api.wait_on_rate_limit == \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.ciscoisesdk
    def test_non_default_wait_on_rate_limit(self, base_url):
        connection_object = ciscoisesdk.IdentityServicesEngineAPI(username=IDENTITY_SERVICES_ENGINE_USERNAME,
                                                                  password=IDENTITY_SERVICES_ENGINE_PASSWORD,
                                                                  encoded_auth=IDENTITY_SERVICES_ENGINE_ENCODED_AUTH,
                                                                  base_url=base_url,
                                                                  wait_on_rate_limit=not DEFAULT_WAIT_ON_RATE_LIMIT,
                                                                  verify=DEFAULT_VERIFY,
                                                                  version=IDENTITY_SERVICES_ENGINE_VERSION,
                                                                  uses_api_gateway=True)
        assert connection_object.wait_on_rate_limit != \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.ciscoisesdk
    def test_api_object_creation(self, api):
        assert isinstance(api.authentication, Authentication)
        assert isinstance(api.custom_caller, CustomCaller)
        if api.version == '3.0.0':
            assert isinstance(api.aci_bindings, AciBindings_v3_0_0)
            assert isinstance(api.aci_settings, AciSettings_v3_0_0)
            assert isinstance(api.anc_endpoint, AncEndpoint_v3_0_0)
            assert isinstance(api.active_directory, ActiveDirectory_v3_0_0)
            assert isinstance(api.admin_user, AdminUser_v3_0_0)
            assert isinstance(api.allowed_protocols, AllowedProtocols_v3_0_0)
            assert isinstance(api.anc_policy, AncPolicy_v3_0_0)
            assert isinstance(api.authorization_profile, AuthorizationProfile_v3_0_0)
            assert isinstance(api.byod_portal, ByodPortal_v3_0_0)
            assert isinstance(api.backup_and_restore, BackupAndRestore_v3_0_0)
            assert isinstance(api.certificate_profile, CertificateProfile_v3_0_0)
            assert isinstance(api.certificate_template, CertificateTemplate_v3_0_0)
            assert isinstance(api.certificates, Certificates_v3_0_0)
            assert isinstance(api.clear_threats_and_vulnerabilities, ClearThreatsAndVulnerabilities_v3_0_0)
            assert isinstance(api.consumer, Consumer_v3_0_0)
            assert isinstance(api.device_administration_authentication_rules, DeviceAdministrationAuthenticationRules_v3_0_0)
            assert isinstance(api.device_administration_authorization_exception_rules, DeviceAdministrationAuthorizationExceptionRules_v3_0_0)
            assert isinstance(api.device_administration_authorization_global_exception_rules, DeviceAdministrationAuthorizationGlobalExceptionRules_v3_0_0)
            assert isinstance(api.device_administration_authorization_rules, DeviceAdministrationAuthorizationRules_v3_0_0)
            assert isinstance(api.device_administration_command_set, DeviceAdministrationCommandSet_v3_0_0)
            assert isinstance(api.device_administration_conditions, DeviceAdministrationConditions_v3_0_0)
            assert isinstance(api.device_administration_dictionary_attributes_list, DeviceAdministrationDictionaryAttributesList_v3_0_0)
            assert isinstance(api.device_administration_identity_stores, DeviceAdministrationIdentityStores_v3_0_0)
            assert isinstance(api.device_administration_network_conditions, DeviceAdministrationNetworkConditions_v3_0_0)
            assert isinstance(api.device_administration_policy_set, DeviceAdministrationPolicySet_v3_0_0)
            assert isinstance(api.device_administration_profiles, DeviceAdministrationProfiles_v3_0_0)
            assert isinstance(api.device_administration_service_names, DeviceAdministrationServiceNames_v3_0_0)
            assert isinstance(api.device_administration_time_date_conditions, DeviceAdministrationTimeDateConditions_v3_0_0)
            assert isinstance(api.downloadable_acl, DownloadableAcl_v3_0_0)
            assert isinstance(api.egress_matrix_cell, EgressMatrixCell_v3_0_0)
            assert isinstance(api.endpoint_certificate, EndpointCertificate_v3_0_0)
            assert isinstance(api.endpoint_identity_group, EndpointIdentityGroup_v3_0_0)
            assert isinstance(api.external_radius_server, ExternalRadiusServer_v3_0_0)
            assert isinstance(api.filter_policy, FilterPolicy_v3_0_0)
            assert isinstance(api.guest_location, GuestLocation_v3_0_0)
            assert isinstance(api.guest_smtp_notification_configuration, GuestSmtpNotificationConfiguration_v3_0_0)
            assert isinstance(api.guest_ssid, GuestSsid_v3_0_0)
            assert isinstance(api.guest_type, GuestType_v3_0_0)
            assert isinstance(api.guest_user, GuestUser_v3_0_0)
            assert isinstance(api.hotspot_portal, HotspotPortal_v3_0_0)
            assert isinstance(api.ip_to_sgt_mapping, IpToSgtMapping_v3_0_0)
            assert isinstance(api.ip_to_sgt_mapping_group, IpToSgtMappingGroup_v3_0_0)
            assert isinstance(api.identity_groups, IdentityGroups_v3_0_0)
            assert isinstance(api.identity_sequence, IdentitySequence_v3_0_0)
            assert isinstance(api.internal_user, InternalUser_v3_0_0)
            assert isinstance(api.mdm, Mdm_v3_0_0)
            assert isinstance(api.misc, Misc_v3_0_0)
            assert isinstance(api.my_device_portal, MyDevicePortal_v3_0_0)
            assert isinstance(api.native_supplicant_profile, NativeSupplicantProfile_v3_0_0)
            assert isinstance(api.network_access_authentication_rules, NetworkAccessAuthenticationRules_v3_0_0)
            assert isinstance(api.network_access_authorization_exception_rules, NetworkAccessAuthorizationExceptionRules_v3_0_0)
            assert isinstance(api.network_access_authorization_global_exception_rules, NetworkAccessAuthorizationGlobalExceptionRules_v3_0_0)
            assert isinstance(api.network_access_authorization_rules, NetworkAccessAuthorizationRules_v3_0_0)
            assert isinstance(api.network_access_conditions, NetworkAccessConditions_v3_0_0)
            assert isinstance(api.network_access_dictionary, NetworkAccessDictionary_v3_0_0)
            assert isinstance(api.network_access_dictionary_attribute, NetworkAccessDictionaryAttribute_v3_0_0)
            assert isinstance(api.network_access_dictionary_attributes_list, NetworkAccessDictionaryAttributesList_v3_0_0)
            assert isinstance(api.network_access_identity_stores, NetworkAccessIdentityStores_v3_0_0)
            assert isinstance(api.network_access_network_conditions, NetworkAccessNetworkConditions_v3_0_0)
            assert isinstance(api.network_access_policy_set, NetworkAccessPolicySet_v3_0_0)
            assert isinstance(api.network_access_profiles, NetworkAccessProfiles_v3_0_0)
            assert isinstance(api.network_access_security_groups, NetworkAccessSecurityGroups_v3_0_0)
            assert isinstance(api.network_access_service_names, NetworkAccessServiceNames_v3_0_0)
            assert isinstance(api.network_access_time_date_conditions, NetworkAccessTimeDateConditions_v3_0_0)
            assert isinstance(api.network_device, NetworkDevice_v3_0_0)
            assert isinstance(api.network_device_group, NetworkDeviceGroup_v3_0_0)
            assert isinstance(api.node_deployment, NodeDeployment_v3_0_0)
            assert isinstance(api.node_group, NodeGroup_v3_0_0)
            assert isinstance(api.node_details, NodeDetails_v3_0_0)
            assert isinstance(api.pan_ha, PanHa_v3_0_0)
            assert isinstance(api.portal_global_setting, PortalGlobalSetting_v3_0_0)
            assert isinstance(api.portal_theme, PortalTheme_v3_0_0)
            assert isinstance(api.profiler, Profiler_v3_0_0)
            assert isinstance(api.profiler_profile, ProfilerProfile_v3_0_0)
            assert isinstance(api.provider, Provider_v3_0_0)
            assert isinstance(api.psn_node_details_with_radius_service, PsnNodeDetailsWithRadiusService_v3_0_0)
            assert isinstance(api.pull_deployment_info, PullDeploymentInfo_v3_0_0)
            assert isinstance(api.px_grid_settings, PxGridSettings_v3_0_0)
            assert isinstance(api.radius_failure, RadiusFailure_v3_0_0)
            assert isinstance(api.radius_server_sequence, RadiusServerSequence_v3_0_0)
            assert isinstance(api.restid_store, RestidStore_v3_0_0)
            assert isinstance(api.replication_status, ReplicationStatus_v3_0_0)
            assert isinstance(api.repository, Repository_v3_0_0)
            assert isinstance(api.sms_provider, SmsProvider_v3_0_0)
            assert isinstance(api.sxp_connections, SxpConnections_v3_0_0)
            assert isinstance(api.sxp_local_bindings, SxpLocalBindings_v3_0_0)
            assert isinstance(api.sxp_vpns, SxpVpns_v3_0_0)
            assert isinstance(api.security_group_to_virtual_network, SecurityGroupToVirtualNetwork_v3_0_0)
            assert isinstance(api.security_groups, SecurityGroups_v3_0_0)
            assert isinstance(api.security_groups_acls, SecurityGroupsAcls_v3_0_0)
            assert isinstance(api.self_registered_portal, SelfRegisteredPortal_v3_0_0)
            assert isinstance(api.session_directory, SessionDirectory_v3_0_0)
            assert isinstance(api.sponsor_group, SponsorGroup_v3_0_0)
            assert isinstance(api.sponsor_group_member, SponsorGroupMember_v3_0_0)
            assert isinstance(api.sponsor_portal, SponsorPortal_v3_0_0)
            assert isinstance(api.sponsored_guest_portal, SponsoredGuestPortal_v3_0_0)
            assert isinstance(api.support_bundle_download, SupportBundleDownload_v3_0_0)
            assert isinstance(api.support_bundle_status, SupportBundleStatus_v3_0_0)
            assert isinstance(api.support_bundle_trigger_configuration, SupportBundleTriggerConfiguration_v3_0_0)
            assert isinstance(api.sync_ise_node, SyncIseNode_v3_0_0)
            assert isinstance(api.system_health, SystemHealth_v3_0_0)
            assert isinstance(api.system_certificate, SystemCertificate_v3_0_0)
            assert isinstance(api.tacacs_command_sets, TacacsCommandSets_v3_0_0)
            assert isinstance(api.tacacs_external_servers, TacacsExternalServers_v3_0_0)
            assert isinstance(api.tacacs_profile, TacacsProfile_v3_0_0)
            assert isinstance(api.tacacs_server_sequence, TacacsServerSequence_v3_0_0)
            assert isinstance(api.telemetry_information, TelemetryInformation_v3_0_0)
            assert isinstance(api.trust_sec_configuration, TrustSecConfiguration_v3_0_0)
            assert isinstance(api.trust_sec_sxp, TrustSecSxp_v3_0_0)
            assert isinstance(api.version_and_patch, VersionAndPatch_v3_0_0)
            assert isinstance(api.version_info, VersionInfo_v3_0_0)
            assert isinstance(api.endpoint, Endpoint_v3_0_0)
            assert isinstance(api.portal, Portal_v3_0_0)
            assert isinstance(api.px_grid_node, PxGridNode_v3_0_0)
            assert isinstance(api.tasks, Tasks_v3_0_0)
        if api.version == '3.1.0':
            assert isinstance(api.aci_bindings, AciBindings_v3_1_0)
            assert isinstance(api.aci_settings, AciSettings_v3_1_0)
            assert isinstance(api.anc_endpoint, AncEndpoint_v3_1_0)
            assert isinstance(api.active_directory, ActiveDirectory_v3_1_0)
            assert isinstance(api.admin_user, AdminUser_v3_1_0)
            assert isinstance(api.allowed_protocols, AllowedProtocols_v3_1_0)
            assert isinstance(api.anc_policy, AncPolicy_v3_1_0)
            assert isinstance(api.authorization_profile, AuthorizationProfile_v3_1_0)
            assert isinstance(api.byod_portal, ByodPortal_v3_1_0)
            assert isinstance(api.backup_and_restore, BackupAndRestore_v3_1_0)
            assert isinstance(api.certificate_profile, CertificateProfile_v3_1_0)
            assert isinstance(api.certificate_template, CertificateTemplate_v3_1_0)
            assert isinstance(api.certificates, Certificates_v3_1_0)
            assert isinstance(api.clear_threats_and_vulnerabilities, ClearThreatsAndVulnerabilities_v3_1_0)
            assert isinstance(api.consumer, Consumer_v3_1_0)
            assert isinstance(api.device_administration_authentication_rules, DeviceAdministrationAuthenticationRules_v3_1_0)
            assert isinstance(api.device_administration_authorization_exception_rules, DeviceAdministrationAuthorizationExceptionRules_v3_1_0)
            assert isinstance(api.device_administration_authorization_global_exception_rules, DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_0)
            assert isinstance(api.device_administration_authorization_rules, DeviceAdministrationAuthorizationRules_v3_1_0)
            assert isinstance(api.device_administration_command_set, DeviceAdministrationCommandSet_v3_1_0)
            assert isinstance(api.device_administration_conditions, DeviceAdministrationConditions_v3_1_0)
            assert isinstance(api.device_administration_dictionary_attributes_list, DeviceAdministrationDictionaryAttributesList_v3_1_0)
            assert isinstance(api.device_administration_identity_stores, DeviceAdministrationIdentityStores_v3_1_0)
            assert isinstance(api.device_administration_network_conditions, DeviceAdministrationNetworkConditions_v3_1_0)
            assert isinstance(api.device_administration_policy_set, DeviceAdministrationPolicySet_v3_1_0)
            assert isinstance(api.device_administration_profiles, DeviceAdministrationProfiles_v3_1_0)
            assert isinstance(api.device_administration_service_names, DeviceAdministrationServiceNames_v3_1_0)
            assert isinstance(api.device_administration_time_date_conditions, DeviceAdministrationTimeDateConditions_v3_1_0)
            assert isinstance(api.downloadable_acl, DownloadableAcl_v3_1_0)
            assert isinstance(api.egress_matrix_cell, EgressMatrixCell_v3_1_0)
            assert isinstance(api.endpoint_certificate, EndpointCertificate_v3_1_0)
            assert isinstance(api.endpoint_identity_group, EndpointIdentityGroup_v3_1_0)
            assert isinstance(api.external_radius_server, ExternalRadiusServer_v3_1_0)
            assert isinstance(api.filter_policy, FilterPolicy_v3_1_0)
            assert isinstance(api.guest_location, GuestLocation_v3_1_0)
            assert isinstance(api.guest_smtp_notification_configuration, GuestSmtpNotificationConfiguration_v3_1_0)
            assert isinstance(api.guest_ssid, GuestSsid_v3_1_0)
            assert isinstance(api.guest_type, GuestType_v3_1_0)
            assert isinstance(api.guest_user, GuestUser_v3_1_0)
            assert isinstance(api.hotspot_portal, HotspotPortal_v3_1_0)
            assert isinstance(api.ip_to_sgt_mapping, IpToSgtMapping_v3_1_0)
            assert isinstance(api.ip_to_sgt_mapping_group, IpToSgtMappingGroup_v3_1_0)
            assert isinstance(api.identity_groups, IdentityGroups_v3_1_0)
            assert isinstance(api.identity_sequence, IdentitySequence_v3_1_0)
            assert isinstance(api.internal_user, InternalUser_v3_1_0)
            assert isinstance(api.mdm, Mdm_v3_1_0)
            assert isinstance(api.misc, Misc_v3_1_0)
            assert isinstance(api.my_device_portal, MyDevicePortal_v3_1_0)
            assert isinstance(api.native_supplicant_profile, NativeSupplicantProfile_v3_1_0)
            assert isinstance(api.network_access_authentication_rules, NetworkAccessAuthenticationRules_v3_1_0)
            assert isinstance(api.network_access_authorization_exception_rules, NetworkAccessAuthorizationExceptionRules_v3_1_0)
            assert isinstance(api.network_access_authorization_global_exception_rules, NetworkAccessAuthorizationGlobalExceptionRules_v3_1_0)
            assert isinstance(api.network_access_authorization_rules, NetworkAccessAuthorizationRules_v3_1_0)
            assert isinstance(api.network_access_conditions, NetworkAccessConditions_v3_1_0)
            assert isinstance(api.network_access_dictionary, NetworkAccessDictionary_v3_1_0)
            assert isinstance(api.network_access_dictionary_attribute, NetworkAccessDictionaryAttribute_v3_1_0)
            assert isinstance(api.network_access_dictionary_attributes_list, NetworkAccessDictionaryAttributesList_v3_1_0)
            assert isinstance(api.network_access_identity_stores, NetworkAccessIdentityStores_v3_1_0)
            assert isinstance(api.network_access_network_conditions, NetworkAccessNetworkConditions_v3_1_0)
            assert isinstance(api.network_access_policy_set, NetworkAccessPolicySet_v3_1_0)
            assert isinstance(api.network_access_profiles, NetworkAccessProfiles_v3_1_0)
            assert isinstance(api.network_access_security_groups, NetworkAccessSecurityGroups_v3_1_0)
            assert isinstance(api.network_access_service_names, NetworkAccessServiceNames_v3_1_0)
            assert isinstance(api.network_access_time_date_conditions, NetworkAccessTimeDateConditions_v3_1_0)
            assert isinstance(api.network_device, NetworkDevice_v3_1_0)
            assert isinstance(api.network_device_group, NetworkDeviceGroup_v3_1_0)
            assert isinstance(api.node_deployment, NodeDeployment_v3_1_0)
            assert isinstance(api.node_group, NodeGroup_v3_1_0)
            assert isinstance(api.node_details, NodeDetails_v3_1_0)
            assert isinstance(api.pan_ha, PanHa_v3_1_0)
            assert isinstance(api.portal_global_setting, PortalGlobalSetting_v3_1_0)
            assert isinstance(api.portal_theme, PortalTheme_v3_1_0)
            assert isinstance(api.profiler, Profiler_v3_1_0)
            assert isinstance(api.profiler_profile, ProfilerProfile_v3_1_0)
            assert isinstance(api.provider, Provider_v3_1_0)
            assert isinstance(api.psn_node_details_with_radius_service, PsnNodeDetailsWithRadiusService_v3_1_0)
            assert isinstance(api.pull_deployment_info, PullDeploymentInfo_v3_1_0)
            assert isinstance(api.px_grid_settings, PxGridSettings_v3_1_0)
            assert isinstance(api.radius_failure, RadiusFailure_v3_1_0)
            assert isinstance(api.radius_server_sequence, RadiusServerSequence_v3_1_0)
            assert isinstance(api.restid_store, RestidStore_v3_1_0)
            assert isinstance(api.replication_status, ReplicationStatus_v3_1_0)
            assert isinstance(api.repository, Repository_v3_1_0)
            assert isinstance(api.sms_provider, SmsProvider_v3_1_0)
            assert isinstance(api.sxp_connections, SxpConnections_v3_1_0)
            assert isinstance(api.sxp_local_bindings, SxpLocalBindings_v3_1_0)
            assert isinstance(api.sxp_vpns, SxpVpns_v3_1_0)
            assert isinstance(api.security_group_to_virtual_network, SecurityGroupToVirtualNetwork_v3_1_0)
            assert isinstance(api.security_groups, SecurityGroups_v3_1_0)
            assert isinstance(api.security_groups_acls, SecurityGroupsAcls_v3_1_0)
            assert isinstance(api.self_registered_portal, SelfRegisteredPortal_v3_1_0)
            assert isinstance(api.session_directory, SessionDirectory_v3_1_0)
            assert isinstance(api.sponsor_group, SponsorGroup_v3_1_0)
            assert isinstance(api.sponsor_group_member, SponsorGroupMember_v3_1_0)
            assert isinstance(api.sponsor_portal, SponsorPortal_v3_1_0)
            assert isinstance(api.sponsored_guest_portal, SponsoredGuestPortal_v3_1_0)
            assert isinstance(api.support_bundle_download, SupportBundleDownload_v3_1_0)
            assert isinstance(api.support_bundle_status, SupportBundleStatus_v3_1_0)
            assert isinstance(api.support_bundle_trigger_configuration, SupportBundleTriggerConfiguration_v3_1_0)
            assert isinstance(api.sync_ise_node, SyncIseNode_v3_1_0)
            assert isinstance(api.system_health, SystemHealth_v3_1_0)
            assert isinstance(api.system_certificate, SystemCertificate_v3_1_0)
            assert isinstance(api.tacacs_command_sets, TacacsCommandSets_v3_1_0)
            assert isinstance(api.tacacs_external_servers, TacacsExternalServers_v3_1_0)
            assert isinstance(api.tacacs_profile, TacacsProfile_v3_1_0)
            assert isinstance(api.tacacs_server_sequence, TacacsServerSequence_v3_1_0)
            assert isinstance(api.telemetry_information, TelemetryInformation_v3_1_0)
            assert isinstance(api.trust_sec_configuration, TrustSecConfiguration_v3_1_0)
            assert isinstance(api.trust_sec_sxp, TrustSecSxp_v3_1_0)
            assert isinstance(api.version_and_patch, VersionAndPatch_v3_1_0)
            assert isinstance(api.version_info, VersionInfo_v3_1_0)
            assert isinstance(api.endpoint, Endpoint_v3_1_0)
            assert isinstance(api.nbar_app, NbarApp_v3_1_0)
            assert isinstance(api.portal, Portal_v3_1_0)
            assert isinstance(api.px_grid_node, PxGridNode_v3_1_0)
            assert isinstance(api.sg_vn_mapping, SgVnMapping_v3_1_0)
            assert isinstance(api.tasks, Tasks_v3_1_0)
            assert isinstance(api.virtual_network, VirtualNetwork_v3_1_0)
            assert isinstance(api.vn_vlan_mapping, VnVlanMapping_v3_1_0)
        if api.version == '3.1.1':
            assert isinstance(api.aci_bindings, AciBindings_v3_1_1)
            assert isinstance(api.aci_settings, AciSettings_v3_1_1)
            assert isinstance(api.anc_endpoint, AncEndpoint_v3_1_1)
            assert isinstance(api.active_directory, ActiveDirectory_v3_1_1)
            assert isinstance(api.admin_user, AdminUser_v3_1_1)
            assert isinstance(api.allowed_protocols, AllowedProtocols_v3_1_1)
            assert isinstance(api.anc_policy, AncPolicy_v3_1_1)
            assert isinstance(api.authorization_profile, AuthorizationProfile_v3_1_1)
            assert isinstance(api.byod_portal, ByodPortal_v3_1_1)
            assert isinstance(api.backup_and_restore, BackupAndRestore_v3_1_1)
            assert isinstance(api.certificate_profile, CertificateProfile_v3_1_1)
            assert isinstance(api.certificate_template, CertificateTemplate_v3_1_1)
            assert isinstance(api.certificates, Certificates_v3_1_1)
            assert isinstance(api.clear_threats_and_vulnerabilities, ClearThreatsAndVulnerabilities_v3_1_1)
            assert isinstance(api.consumer, Consumer_v3_1_1)
            assert isinstance(api.device_administration_authentication_rules, DeviceAdministrationAuthenticationRules_v3_1_1)
            assert isinstance(api.device_administration_authorization_exception_rules, DeviceAdministrationAuthorizationExceptionRules_v3_1_1)
            assert isinstance(api.device_administration_authorization_global_exception_rules, DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_1)
            assert isinstance(api.device_administration_authorization_rules, DeviceAdministrationAuthorizationRules_v3_1_1)
            assert isinstance(api.device_administration_command_set, DeviceAdministrationCommandSet_v3_1_1)
            assert isinstance(api.device_administration_conditions, DeviceAdministrationConditions_v3_1_1)
            assert isinstance(api.device_administration_dictionary_attributes_list, DeviceAdministrationDictionaryAttributesList_v3_1_1)
            assert isinstance(api.device_administration_identity_stores, DeviceAdministrationIdentityStores_v3_1_1)
            assert isinstance(api.device_administration_network_conditions, DeviceAdministrationNetworkConditions_v3_1_1)
            assert isinstance(api.device_administration_policy_set, DeviceAdministrationPolicySet_v3_1_1)
            assert isinstance(api.device_administration_profiles, DeviceAdministrationProfiles_v3_1_1)
            assert isinstance(api.device_administration_service_names, DeviceAdministrationServiceNames_v3_1_1)
            assert isinstance(api.device_administration_time_date_conditions, DeviceAdministrationTimeDateConditions_v3_1_1)
            assert isinstance(api.downloadable_acl, DownloadableAcl_v3_1_1)
            assert isinstance(api.egress_matrix_cell, EgressMatrixCell_v3_1_1)
            assert isinstance(api.endpoint_certificate, EndpointCertificate_v3_1_1)
            assert isinstance(api.endpoint_identity_group, EndpointIdentityGroup_v3_1_1)
            assert isinstance(api.external_radius_server, ExternalRadiusServer_v3_1_1)
            assert isinstance(api.filter_policy, FilterPolicy_v3_1_1)
            assert isinstance(api.guest_location, GuestLocation_v3_1_1)
            assert isinstance(api.guest_smtp_notification_configuration, GuestSmtpNotificationConfiguration_v3_1_1)
            assert isinstance(api.guest_ssid, GuestSsid_v3_1_1)
            assert isinstance(api.guest_type, GuestType_v3_1_1)
            assert isinstance(api.guest_user, GuestUser_v3_1_1)
            assert isinstance(api.hotspot_portal, HotspotPortal_v3_1_1)
            assert isinstance(api.ip_to_sgt_mapping, IpToSgtMapping_v3_1_1)
            assert isinstance(api.ip_to_sgt_mapping_group, IpToSgtMappingGroup_v3_1_1)
            assert isinstance(api.identity_groups, IdentityGroups_v3_1_1)
            assert isinstance(api.identity_sequence, IdentitySequence_v3_1_1)
            assert isinstance(api.internal_user, InternalUser_v3_1_1)
            assert isinstance(api.mdm, Mdm_v3_1_1)
            assert isinstance(api.misc, Misc_v3_1_1)
            assert isinstance(api.my_device_portal, MyDevicePortal_v3_1_1)
            assert isinstance(api.native_supplicant_profile, NativeSupplicantProfile_v3_1_1)
            assert isinstance(api.network_access_authentication_rules, NetworkAccessAuthenticationRules_v3_1_1)
            assert isinstance(api.network_access_authorization_exception_rules, NetworkAccessAuthorizationExceptionRules_v3_1_1)
            assert isinstance(api.network_access_authorization_global_exception_rules, NetworkAccessAuthorizationGlobalExceptionRules_v3_1_1)
            assert isinstance(api.network_access_authorization_rules, NetworkAccessAuthorizationRules_v3_1_1)
            assert isinstance(api.network_access_conditions, NetworkAccessConditions_v3_1_1)
            assert isinstance(api.network_access_dictionary, NetworkAccessDictionary_v3_1_1)
            assert isinstance(api.network_access_dictionary_attribute, NetworkAccessDictionaryAttribute_v3_1_1)
            assert isinstance(api.network_access_dictionary_attributes_list, NetworkAccessDictionaryAttributesList_v3_1_1)
            assert isinstance(api.network_access_identity_stores, NetworkAccessIdentityStores_v3_1_1)
            assert isinstance(api.network_access_network_conditions, NetworkAccessNetworkConditions_v3_1_1)
            assert isinstance(api.network_access_policy_set, NetworkAccessPolicySet_v3_1_1)
            assert isinstance(api.network_access_profiles, NetworkAccessProfiles_v3_1_1)
            assert isinstance(api.network_access_security_groups, NetworkAccessSecurityGroups_v3_1_1)
            assert isinstance(api.network_access_service_names, NetworkAccessServiceNames_v3_1_1)
            assert isinstance(api.network_access_time_date_conditions, NetworkAccessTimeDateConditions_v3_1_1)
            assert isinstance(api.network_device, NetworkDevice_v3_1_1)
            assert isinstance(api.network_device_group, NetworkDeviceGroup_v3_1_1)
            assert isinstance(api.node_deployment, NodeDeployment_v3_1_1)
            assert isinstance(api.node_group, NodeGroup_v3_1_1)
            assert isinstance(api.node_details, NodeDetails_v3_1_1)
            assert isinstance(api.pan_ha, PanHa_v3_1_1)
            assert isinstance(api.portal_global_setting, PortalGlobalSetting_v3_1_1)
            assert isinstance(api.portal_theme, PortalTheme_v3_1_1)
            assert isinstance(api.profiler, Profiler_v3_1_1)
            assert isinstance(api.profiler_profile, ProfilerProfile_v3_1_1)
            assert isinstance(api.provider, Provider_v3_1_1)
            assert isinstance(api.psn_node_details_with_radius_service, PsnNodeDetailsWithRadiusService_v3_1_1)
            assert isinstance(api.pull_deployment_info, PullDeploymentInfo_v3_1_1)
            assert isinstance(api.px_grid_settings, PxGridSettings_v3_1_1)
            assert isinstance(api.radius_failure, RadiusFailure_v3_1_1)
            assert isinstance(api.radius_server_sequence, RadiusServerSequence_v3_1_1)
            assert isinstance(api.restid_store, RestidStore_v3_1_1)
            assert isinstance(api.repository, Repository_v3_1_1)
            assert isinstance(api.sms_provider, SmsProvider_v3_1_1)
            assert isinstance(api.sxp_connections, SxpConnections_v3_1_1)
            assert isinstance(api.sxp_local_bindings, SxpLocalBindings_v3_1_1)
            assert isinstance(api.sxp_vpns, SxpVpns_v3_1_1)
            assert isinstance(api.security_group_to_virtual_network, SecurityGroupToVirtualNetwork_v3_1_1)
            assert isinstance(api.security_groups, SecurityGroups_v3_1_1)
            assert isinstance(api.security_groups_acls, SecurityGroupsAcls_v3_1_1)
            assert isinstance(api.self_registered_portal, SelfRegisteredPortal_v3_1_1)
            assert isinstance(api.session_directory, SessionDirectory_v3_1_1)
            assert isinstance(api.sponsor_group, SponsorGroup_v3_1_1)
            assert isinstance(api.sponsor_group_member, SponsorGroupMember_v3_1_1)
            assert isinstance(api.sponsor_portal, SponsorPortal_v3_1_1)
            assert isinstance(api.sponsored_guest_portal, SponsoredGuestPortal_v3_1_1)
            assert isinstance(api.support_bundle_download, SupportBundleDownload_v3_1_1)
            assert isinstance(api.support_bundle_status, SupportBundleStatus_v3_1_1)
            assert isinstance(api.support_bundle_trigger_configuration, SupportBundleTriggerConfiguration_v3_1_1)
            assert isinstance(api.system_health, SystemHealth_v3_1_1)
            assert isinstance(api.system_certificate, SystemCertificate_v3_1_1)
            assert isinstance(api.tacacs_command_sets, TacacsCommandSets_v3_1_1)
            assert isinstance(api.tacacs_external_servers, TacacsExternalServers_v3_1_1)
            assert isinstance(api.tacacs_profile, TacacsProfile_v3_1_1)
            assert isinstance(api.tacacs_server_sequence, TacacsServerSequence_v3_1_1)
            assert isinstance(api.telemetry_information, TelemetryInformation_v3_1_1)
            assert isinstance(api.trust_sec_configuration, TrustSecConfiguration_v3_1_1)
            assert isinstance(api.trust_sec_sxp, TrustSecSxp_v3_1_1)
            assert isinstance(api.version_and_patch, VersionAndPatch_v3_1_1)
            assert isinstance(api.version_info, VersionInfo_v3_1_1)
            assert isinstance(api.endpoint, Endpoint_v3_1_1)
            assert isinstance(api.portal, Portal_v3_1_1)
            assert isinstance(api.px_grid_node, PxGridNode_v3_1_1)
            assert isinstance(api.tasks, Tasks_v3_1_1)
