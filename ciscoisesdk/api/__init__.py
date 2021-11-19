# -*- coding: utf-8 -*-
"""Identity Services Engine API wrappers.

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

from past.types import basestring

from ciscoisesdk.environment import (
    IDENTITY_SERVICES_ENGINE_USERNAME,
    IDENTITY_SERVICES_ENGINE_PASSWORD,
    IDENTITY_SERVICES_ENGINE_ENCODED_AUTH,
    IDENTITY_SERVICES_ENGINE_DEBUG,
    IDENTITY_SERVICES_ENGINE_VERSION,
    IDENTITY_SERVICES_ENGINE_BASE_URL,
    IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT,
    IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT,
    IDENTITY_SERVICES_ENGINE_VERIFY,
    IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY,
    IDENTITY_SERVICES_ENGINE_UI_BASE_URL,
    IDENTITY_SERVICES_ENGINE_ERS_BASE_URL,
    IDENTITY_SERVICES_ENGINE_MNT_BASE_URL,
    IDENTITY_SERVICES_ENGINE_PX_GRID_BASE_URL,
)
from ciscoisesdk.exceptions import AccessTokenError, VersionError
from ciscoisesdk.models.mydict import mydict_data_factory
from ciscoisesdk.models.schema_validator import SchemaValidator
from ciscoisesdk.restsession import RestSession
from ciscoisesdk.utils import check_type

from .authentication import Authentication
from .v3_0_0.aci_bindings import \
    AciBindings as AciBindings_v3_0_0
from .v3_0_0.aci_settings import \
    AciSettings as AciSettings_v3_0_0
from .v3_0_0.anc_endpoint import \
    AncEndpoint as AncEndpoint_v3_0_0
from .v3_0_0.active_directory import \
    ActiveDirectory as ActiveDirectory_v3_0_0
from .v3_0_0.admin_user import \
    AdminUser as AdminUser_v3_0_0
from .v3_0_0.allowed_protocols import \
    AllowedProtocols as AllowedProtocols_v3_0_0
from .v3_0_0.anc_policy import \
    AncPolicy as AncPolicy_v3_0_0
from .v3_0_0.authorization_profile import \
    AuthorizationProfile as AuthorizationProfile_v3_0_0
from .v3_0_0.byod_portal import \
    ByodPortal as ByodPortal_v3_0_0
from .v3_0_0.backup_and_restore import \
    BackupAndRestore as BackupAndRestore_v3_0_0
from .v3_0_0.certificate_profile import \
    CertificateProfile as CertificateProfile_v3_0_0
from .v3_0_0.certificate_template import \
    CertificateTemplate as CertificateTemplate_v3_0_0
from .v3_0_0.certificates import \
    Certificates as Certificates_v3_0_0
from .v3_0_0.clear_threats_and_vulnerabilities import \
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_0_0
from .v3_0_0.consumer import \
    Consumer as Consumer_v3_0_0
from .v3_0_0.device_administration_authentication_rules import \
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_0_0
from .v3_0_0.device_administration_authorization_exception_rules import \
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_0_0
from .v3_0_0.device_administration_authorization_global_exception_rules import \
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_0_0
from .v3_0_0.device_administration_authorization_rules import \
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_0_0
from .v3_0_0.device_administration_command_set import \
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_0_0
from .v3_0_0.device_administration_conditions import \
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_0_0
from .v3_0_0.device_administration_dictionary_attributes_list import \
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_0_0
from .v3_0_0.device_administration_identity_stores import \
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_0_0
from .v3_0_0.device_administration_network_conditions import \
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_0_0
from .v3_0_0.device_administration_policy_set import \
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_0_0
from .v3_0_0.device_administration_profiles import \
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_0_0
from .v3_0_0.device_administration_service_names import \
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_0_0
from .v3_0_0.device_administration_time_date_conditions import \
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_0_0
from .v3_0_0.downloadable_acl import \
    DownloadableAcl as DownloadableAcl_v3_0_0
from .v3_0_0.egress_matrix_cell import \
    EgressMatrixCell as EgressMatrixCell_v3_0_0
from .v3_0_0.endpoint_certificate import \
    EndpointCertificate as EndpointCertificate_v3_0_0
from .v3_0_0.endpoint_identity_group import \
    EndpointIdentityGroup as EndpointIdentityGroup_v3_0_0
from .v3_0_0.external_radius_server import \
    ExternalRadiusServer as ExternalRadiusServer_v3_0_0
from .v3_0_0.filter_policy import \
    FilterPolicy as FilterPolicy_v3_0_0
from .v3_0_0.guest_location import \
    GuestLocation as GuestLocation_v3_0_0
from .v3_0_0.guest_smtp_notification_configuration import \
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_0_0
from .v3_0_0.guest_ssid import \
    GuestSsid as GuestSsid_v3_0_0
from .v3_0_0.guest_type import \
    GuestType as GuestType_v3_0_0
from .v3_0_0.guest_user import \
    GuestUser as GuestUser_v3_0_0
from .v3_0_0.hotspot_portal import \
    HotspotPortal as HotspotPortal_v3_0_0
from .v3_0_0.ip_to_sgt_mapping import \
    IpToSgtMapping as IpToSgtMapping_v3_0_0
from .v3_0_0.ip_to_sgt_mapping_group import \
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_0_0
from .v3_0_0.identity_groups import \
    IdentityGroups as IdentityGroups_v3_0_0
from .v3_0_0.identity_sequence import \
    IdentitySequence as IdentitySequence_v3_0_0
from .v3_0_0.internal_user import \
    InternalUser as InternalUser_v3_0_0
from .v3_0_0.mdm import \
    Mdm as Mdm_v3_0_0
from .v3_0_0.misc import \
    Misc as Misc_v3_0_0
from .v3_0_0.my_device_portal import \
    MyDevicePortal as MyDevicePortal_v3_0_0
from .v3_0_0.native_supplicant_profile import \
    NativeSupplicantProfile as NativeSupplicantProfile_v3_0_0
from .v3_0_0.network_access_authentication_rules import \
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_0_0
from .v3_0_0.network_access_authorization_exception_rules import \
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_0_0
from .v3_0_0.network_access_authorization_global_exception_rules import \
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_0_0
from .v3_0_0.network_access_authorization_rules import \
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_0_0
from .v3_0_0.network_access_conditions import \
    NetworkAccessConditions as NetworkAccessConditions_v3_0_0
from .v3_0_0.network_access_dictionary import \
    NetworkAccessDictionary as NetworkAccessDictionary_v3_0_0
from .v3_0_0.network_access_dictionary_attribute import \
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_0_0
from .v3_0_0.network_access_dictionary_attributes_list import \
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_0_0
from .v3_0_0.network_access_identity_stores import \
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_0_0
from .v3_0_0.network_access_network_conditions import \
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_0_0
from .v3_0_0.network_access_policy_set import \
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_0_0
from .v3_0_0.network_access_profiles import \
    NetworkAccessProfiles as NetworkAccessProfiles_v3_0_0
from .v3_0_0.network_access_security_groups import \
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_0_0
from .v3_0_0.network_access_service_names import \
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_0_0
from .v3_0_0.network_access_time_date_conditions import \
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_0_0
from .v3_0_0.network_device import \
    NetworkDevice as NetworkDevice_v3_0_0
from .v3_0_0.network_device_group import \
    NetworkDeviceGroup as NetworkDeviceGroup_v3_0_0
from .v3_0_0.node_deployment import \
    NodeDeployment as NodeDeployment_v3_0_0
from .v3_0_0.node_group import \
    NodeGroup as NodeGroup_v3_0_0
from .v3_0_0.node_details import \
    NodeDetails as NodeDetails_v3_0_0
from .v3_0_0.pan_ha import \
    PanHa as PanHa_v3_0_0
from .v3_0_0.portal_global_setting import \
    PortalGlobalSetting as PortalGlobalSetting_v3_0_0
from .v3_0_0.portal_theme import \
    PortalTheme as PortalTheme_v3_0_0
from .v3_0_0.profiler import \
    Profiler as Profiler_v3_0_0
from .v3_0_0.profiler_profile import \
    ProfilerProfile as ProfilerProfile_v3_0_0
from .v3_0_0.provider import \
    Provider as Provider_v3_0_0
from .v3_0_0.psn_node_details_with_radius_service import \
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_0_0
from .v3_0_0.pull_deployment_info import \
    PullDeploymentInfo as PullDeploymentInfo_v3_0_0
from .v3_0_0.px_grid_settings import \
    PxGridSettings as PxGridSettings_v3_0_0
from .v3_0_0.radius_failure import \
    RadiusFailure as RadiusFailure_v3_0_0
from .v3_0_0.radius_server_sequence import \
    RadiusServerSequence as RadiusServerSequence_v3_0_0
from .v3_0_0.restid_store import \
    RestidStore as RestidStore_v3_0_0
from .v3_0_0.replication_status import \
    ReplicationStatus as ReplicationStatus_v3_0_0
from .v3_0_0.repository import \
    Repository as Repository_v3_0_0
from .v3_0_0.sms_provider import \
    SmsProvider as SmsProvider_v3_0_0
from .v3_0_0.sxp_connections import \
    SxpConnections as SxpConnections_v3_0_0
from .v3_0_0.sxp_local_bindings import \
    SxpLocalBindings as SxpLocalBindings_v3_0_0
from .v3_0_0.sxp_vpns import \
    SxpVpns as SxpVpns_v3_0_0
from .v3_0_0.security_group_to_virtual_network import \
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_0_0
from .v3_0_0.security_groups import \
    SecurityGroups as SecurityGroups_v3_0_0
from .v3_0_0.security_groups_acls import \
    SecurityGroupsAcls as SecurityGroupsAcls_v3_0_0
from .v3_0_0.self_registered_portal import \
    SelfRegisteredPortal as SelfRegisteredPortal_v3_0_0
from .v3_0_0.session_directory import \
    SessionDirectory as SessionDirectory_v3_0_0
from .v3_0_0.sponsor_group import \
    SponsorGroup as SponsorGroup_v3_0_0
from .v3_0_0.sponsor_group_member import \
    SponsorGroupMember as SponsorGroupMember_v3_0_0
from .v3_0_0.sponsor_portal import \
    SponsorPortal as SponsorPortal_v3_0_0
from .v3_0_0.sponsored_guest_portal import \
    SponsoredGuestPortal as SponsoredGuestPortal_v3_0_0
from .v3_0_0.support_bundle_download import \
    SupportBundleDownload as SupportBundleDownload_v3_0_0
from .v3_0_0.support_bundle_status import \
    SupportBundleStatus as SupportBundleStatus_v3_0_0
from .v3_0_0.support_bundle_trigger_configuration import \
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_0_0
from .v3_0_0.sync_ise_node import \
    SyncIseNode as SyncIseNode_v3_0_0
from .v3_0_0.system_health import \
    SystemHealth as SystemHealth_v3_0_0
from .v3_0_0.system_certificate import \
    SystemCertificate as SystemCertificate_v3_0_0
from .v3_0_0.tacacs_command_sets import \
    TacacsCommandSets as TacacsCommandSets_v3_0_0
from .v3_0_0.tacacs_external_servers import \
    TacacsExternalServers as TacacsExternalServers_v3_0_0
from .v3_0_0.tacacs_profile import \
    TacacsProfile as TacacsProfile_v3_0_0
from .v3_0_0.tacacs_server_sequence import \
    TacacsServerSequence as TacacsServerSequence_v3_0_0
from .v3_0_0.telemetry_information import \
    TelemetryInformation as TelemetryInformation_v3_0_0
from .v3_0_0.trust_sec_configuration import \
    TrustSecConfiguration as TrustSecConfiguration_v3_0_0
from .v3_0_0.trust_sec_sxp import \
    TrustSecSxp as TrustSecSxp_v3_0_0
from .v3_0_0.version_and_patch import \
    VersionAndPatch as VersionAndPatch_v3_0_0
from .v3_0_0.version_info import \
    VersionInfo as VersionInfo_v3_0_0
from .v3_0_0.endpoint import \
    Endpoint as Endpoint_v3_0_0
from .v3_0_0.portal import \
    Portal as Portal_v3_0_0
from .v3_0_0.px_grid_node import \
    PxGridNode as PxGridNode_v3_0_0
from .v3_0_0.tasks import \
    Tasks as Tasks_v3_0_0
from .v3_1_0.aci_bindings import \
    AciBindings as AciBindings_v3_1_0
from .v3_1_0.aci_settings import \
    AciSettings as AciSettings_v3_1_0
from .v3_1_0.anc_endpoint import \
    AncEndpoint as AncEndpoint_v3_1_0
from .v3_1_0.active_directory import \
    ActiveDirectory as ActiveDirectory_v3_1_0
from .v3_1_0.admin_user import \
    AdminUser as AdminUser_v3_1_0
from .v3_1_0.allowed_protocols import \
    AllowedProtocols as AllowedProtocols_v3_1_0
from .v3_1_0.anc_policy import \
    AncPolicy as AncPolicy_v3_1_0
from .v3_1_0.authorization_profile import \
    AuthorizationProfile as AuthorizationProfile_v3_1_0
from .v3_1_0.byod_portal import \
    ByodPortal as ByodPortal_v3_1_0
from .v3_1_0.backup_and_restore import \
    BackupAndRestore as BackupAndRestore_v3_1_0
from .v3_1_0.certificate_profile import \
    CertificateProfile as CertificateProfile_v3_1_0
from .v3_1_0.certificate_template import \
    CertificateTemplate as CertificateTemplate_v3_1_0
from .v3_1_0.certificates import \
    Certificates as Certificates_v3_1_0
from .v3_1_0.clear_threats_and_vulnerabilities import \
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_1_0
from .v3_1_0.consumer import \
    Consumer as Consumer_v3_1_0
from .v3_1_0.device_administration_authentication_rules import \
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_1_0
from .v3_1_0.device_administration_authorization_exception_rules import \
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_1_0
from .v3_1_0.device_administration_authorization_global_exception_rules import \
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_0
from .v3_1_0.device_administration_authorization_rules import \
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_1_0
from .v3_1_0.device_administration_command_set import \
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_1_0
from .v3_1_0.device_administration_conditions import \
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_1_0
from .v3_1_0.device_administration_dictionary_attributes_list import \
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_1_0
from .v3_1_0.device_administration_identity_stores import \
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_1_0
from .v3_1_0.device_administration_network_conditions import \
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_1_0
from .v3_1_0.device_administration_policy_set import \
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_1_0
from .v3_1_0.device_administration_profiles import \
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_1_0
from .v3_1_0.device_administration_service_names import \
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_1_0
from .v3_1_0.device_administration_time_date_conditions import \
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_1_0
from .v3_1_0.downloadable_acl import \
    DownloadableAcl as DownloadableAcl_v3_1_0
from .v3_1_0.egress_matrix_cell import \
    EgressMatrixCell as EgressMatrixCell_v3_1_0
from .v3_1_0.endpoint_certificate import \
    EndpointCertificate as EndpointCertificate_v3_1_0
from .v3_1_0.endpoint_identity_group import \
    EndpointIdentityGroup as EndpointIdentityGroup_v3_1_0
from .v3_1_0.external_radius_server import \
    ExternalRadiusServer as ExternalRadiusServer_v3_1_0
from .v3_1_0.filter_policy import \
    FilterPolicy as FilterPolicy_v3_1_0
from .v3_1_0.guest_location import \
    GuestLocation as GuestLocation_v3_1_0
from .v3_1_0.guest_smtp_notification_configuration import \
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_1_0
from .v3_1_0.guest_ssid import \
    GuestSsid as GuestSsid_v3_1_0
from .v3_1_0.guest_type import \
    GuestType as GuestType_v3_1_0
from .v3_1_0.guest_user import \
    GuestUser as GuestUser_v3_1_0
from .v3_1_0.hotspot_portal import \
    HotspotPortal as HotspotPortal_v3_1_0
from .v3_1_0.ip_to_sgt_mapping import \
    IpToSgtMapping as IpToSgtMapping_v3_1_0
from .v3_1_0.ip_to_sgt_mapping_group import \
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_1_0
from .v3_1_0.identity_groups import \
    IdentityGroups as IdentityGroups_v3_1_0
from .v3_1_0.identity_sequence import \
    IdentitySequence as IdentitySequence_v3_1_0
from .v3_1_0.internal_user import \
    InternalUser as InternalUser_v3_1_0
from .v3_1_0.mdm import \
    Mdm as Mdm_v3_1_0
from .v3_1_0.misc import \
    Misc as Misc_v3_1_0
from .v3_1_0.my_device_portal import \
    MyDevicePortal as MyDevicePortal_v3_1_0
from .v3_1_0.native_supplicant_profile import \
    NativeSupplicantProfile as NativeSupplicantProfile_v3_1_0
from .v3_1_0.network_access_authentication_rules import \
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_1_0
from .v3_1_0.network_access_authorization_exception_rules import \
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_1_0
from .v3_1_0.network_access_authorization_global_exception_rules import \
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_1_0
from .v3_1_0.network_access_authorization_rules import \
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_1_0
from .v3_1_0.network_access_conditions import \
    NetworkAccessConditions as NetworkAccessConditions_v3_1_0
from .v3_1_0.network_access_dictionary import \
    NetworkAccessDictionary as NetworkAccessDictionary_v3_1_0
from .v3_1_0.network_access_dictionary_attribute import \
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_1_0
from .v3_1_0.network_access_dictionary_attributes_list import \
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_1_0
from .v3_1_0.network_access_identity_stores import \
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_1_0
from .v3_1_0.network_access_network_conditions import \
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_1_0
from .v3_1_0.network_access_policy_set import \
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_1_0
from .v3_1_0.network_access_profiles import \
    NetworkAccessProfiles as NetworkAccessProfiles_v3_1_0
from .v3_1_0.network_access_security_groups import \
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_1_0
from .v3_1_0.network_access_service_names import \
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_1_0
from .v3_1_0.network_access_time_date_conditions import \
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_1_0
from .v3_1_0.network_device import \
    NetworkDevice as NetworkDevice_v3_1_0
from .v3_1_0.network_device_group import \
    NetworkDeviceGroup as NetworkDeviceGroup_v3_1_0
from .v3_1_0.node_deployment import \
    NodeDeployment as NodeDeployment_v3_1_0
from .v3_1_0.node_group import \
    NodeGroup as NodeGroup_v3_1_0
from .v3_1_0.node_details import \
    NodeDetails as NodeDetails_v3_1_0
from .v3_1_0.pan_ha import \
    PanHa as PanHa_v3_1_0
from .v3_1_0.portal_global_setting import \
    PortalGlobalSetting as PortalGlobalSetting_v3_1_0
from .v3_1_0.portal_theme import \
    PortalTheme as PortalTheme_v3_1_0
from .v3_1_0.profiler import \
    Profiler as Profiler_v3_1_0
from .v3_1_0.profiler_profile import \
    ProfilerProfile as ProfilerProfile_v3_1_0
from .v3_1_0.provider import \
    Provider as Provider_v3_1_0
from .v3_1_0.psn_node_details_with_radius_service import \
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_1_0
from .v3_1_0.pull_deployment_info import \
    PullDeploymentInfo as PullDeploymentInfo_v3_1_0
from .v3_1_0.px_grid_settings import \
    PxGridSettings as PxGridSettings_v3_1_0
from .v3_1_0.radius_failure import \
    RadiusFailure as RadiusFailure_v3_1_0
from .v3_1_0.radius_server_sequence import \
    RadiusServerSequence as RadiusServerSequence_v3_1_0
from .v3_1_0.restid_store import \
    RestidStore as RestidStore_v3_1_0
from .v3_1_0.replication_status import \
    ReplicationStatus as ReplicationStatus_v3_1_0
from .v3_1_0.repository import \
    Repository as Repository_v3_1_0
from .v3_1_0.sms_provider import \
    SmsProvider as SmsProvider_v3_1_0
from .v3_1_0.sxp_connections import \
    SxpConnections as SxpConnections_v3_1_0
from .v3_1_0.sxp_local_bindings import \
    SxpLocalBindings as SxpLocalBindings_v3_1_0
from .v3_1_0.sxp_vpns import \
    SxpVpns as SxpVpns_v3_1_0
from .v3_1_0.security_group_to_virtual_network import \
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_1_0
from .v3_1_0.security_groups import \
    SecurityGroups as SecurityGroups_v3_1_0
from .v3_1_0.security_groups_acls import \
    SecurityGroupsAcls as SecurityGroupsAcls_v3_1_0
from .v3_1_0.self_registered_portal import \
    SelfRegisteredPortal as SelfRegisteredPortal_v3_1_0
from .v3_1_0.session_directory import \
    SessionDirectory as SessionDirectory_v3_1_0
from .v3_1_0.sponsor_group import \
    SponsorGroup as SponsorGroup_v3_1_0
from .v3_1_0.sponsor_group_member import \
    SponsorGroupMember as SponsorGroupMember_v3_1_0
from .v3_1_0.sponsor_portal import \
    SponsorPortal as SponsorPortal_v3_1_0
from .v3_1_0.sponsored_guest_portal import \
    SponsoredGuestPortal as SponsoredGuestPortal_v3_1_0
from .v3_1_0.support_bundle_download import \
    SupportBundleDownload as SupportBundleDownload_v3_1_0
from .v3_1_0.support_bundle_status import \
    SupportBundleStatus as SupportBundleStatus_v3_1_0
from .v3_1_0.support_bundle_trigger_configuration import \
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_1_0
from .v3_1_0.sync_ise_node import \
    SyncIseNode as SyncIseNode_v3_1_0
from .v3_1_0.system_health import \
    SystemHealth as SystemHealth_v3_1_0
from .v3_1_0.system_certificate import \
    SystemCertificate as SystemCertificate_v3_1_0
from .v3_1_0.tacacs_command_sets import \
    TacacsCommandSets as TacacsCommandSets_v3_1_0
from .v3_1_0.tacacs_external_servers import \
    TacacsExternalServers as TacacsExternalServers_v3_1_0
from .v3_1_0.tacacs_profile import \
    TacacsProfile as TacacsProfile_v3_1_0
from .v3_1_0.tacacs_server_sequence import \
    TacacsServerSequence as TacacsServerSequence_v3_1_0
from .v3_1_0.telemetry_information import \
    TelemetryInformation as TelemetryInformation_v3_1_0
from .v3_1_0.trust_sec_configuration import \
    TrustSecConfiguration as TrustSecConfiguration_v3_1_0
from .v3_1_0.trust_sec_sxp import \
    TrustSecSxp as TrustSecSxp_v3_1_0
from .v3_1_0.version_and_patch import \
    VersionAndPatch as VersionAndPatch_v3_1_0
from .v3_1_0.version_info import \
    VersionInfo as VersionInfo_v3_1_0
from .v3_1_0.endpoint import \
    Endpoint as Endpoint_v3_1_0
from .v3_1_0.nbar_app import \
    NbarApp as NbarApp_v3_1_0
from .v3_1_0.portal import \
    Portal as Portal_v3_1_0
from .v3_1_0.px_grid_node import \
    PxGridNode as PxGridNode_v3_1_0
from .v3_1_0.sg_vn_mapping import \
    SgVnMapping as SgVnMapping_v3_1_0
from .v3_1_0.tasks import \
    Tasks as Tasks_v3_1_0
from .v3_1_0.virtual_network import \
    VirtualNetwork as VirtualNetwork_v3_1_0
from .v3_1_0.vn_vlan_mapping import \
    VnVlanMapping as VnVlanMapping_v3_1_0
from .custom_caller import CustomCaller
import copy


class IdentityServicesEngineAPI(object):
    """Identity Services Engine API wrapper.

    Creates a 'session' for all API calls through a created IdentityServicesEngineAPI
    object.  The 'session' handles authentication, provides the needed headers,
    and checks all responses for error conditions.

    IdentityServicesEngineAPI wraps all of the individual Identity Services Engine APIs and represents
    them in a simple hierarchical structure.
    """

    def __init__(self, username=IDENTITY_SERVICES_ENGINE_USERNAME,
                 password=IDENTITY_SERVICES_ENGINE_PASSWORD,
                 encoded_auth=IDENTITY_SERVICES_ENGINE_ENCODED_AUTH,
                 uses_api_gateway=IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY,
                 base_url=IDENTITY_SERVICES_ENGINE_BASE_URL,
                 ui_base_url=IDENTITY_SERVICES_ENGINE_UI_BASE_URL,
                 ers_base_url=IDENTITY_SERVICES_ENGINE_ERS_BASE_URL,
                 mnt_base_url=IDENTITY_SERVICES_ENGINE_MNT_BASE_URL,
                 px_grid_base_url=IDENTITY_SERVICES_ENGINE_PX_GRID_BASE_URL,
                 single_request_timeout=IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT,
                 wait_on_rate_limit=IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT,
                 verify=IDENTITY_SERVICES_ENGINE_VERIFY,
                 version=IDENTITY_SERVICES_ENGINE_VERSION,
                 debug=IDENTITY_SERVICES_ENGINE_DEBUG,
                 object_factory=mydict_data_factory,
                 validator=SchemaValidator):
        """Create a new IdentityServicesEngineAPI object.
        An access token is required to interact with the Identity Services Engine APIs.
        This package supports two methods for you to pass the
        authorization token:

          1. Provide a encoded_auth value (username:password encoded in
          base 64). *This has priority over the following method*

          2. Provide username and password values.

        This package supports two methods for you to set those values:

          1. Provide the parameter. That is the encoded_auth or
          username and password parameters.

          2. If an argument is not supplied, the package checks for
          its environment variable counterpart. That is the
          IDENTITY_SERVICES_ENGINE_ENCODED_AUTH, IDENTITY_SERVICES_ENGINE_USERNAME,
          IDENTITY_SERVICES_ENGINE_PASSWORD.

        When not given enough parameters an AccessTokenError is raised.

        Args:
            uses_api_gateway(bool,basestring): Controls whether we use the ISE's API
                Gateway to make the request. Defaults to the
                IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY
                (or IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY_STRING) environment variable or
                ciscoisesdk.config.DEFAULT_USES_API_GATEWAY if the environment
                variables are not set.
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes, used when uses_api_gateway is True.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable or
                ciscoisesdk.config.DEFAULT_BASE_URL
                if the environment variable is not set.
            ui_base_url(basestring): The UI base URL to be prefixed to the
                individual ISE UI API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            ers_base_url(basestring): The ERS base URL to be prefixed to the
                individual ISE ERS API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            mnt_base_url(basestring): The MNT base URL to be prefixed to the
                individual ISE MNT API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            px_grid_base_url(basestring): The PxGrid base URL to be prefixed to the
                individual ISE PxGrid API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            username(basestring): HTTP Basic Auth username.
            password(basestring): HTTP Basic Auth password.
            encoded_auth(basestring): HTTP Basic Auth base64 encoded string.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to the IDENTITY_SERVICES_ENGINE_SINGLE_REQUEST_TIMEOUT
                environment variable or
                ciscoisesdk.config.DEFAULT_SINGLE_REQUEST_TIMEOUT
                if the environment variable is not set.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to the IDENTITY_SERVICES_ENGINE_WAIT_ON_RATE_LIMIT
                environment variable or
                ciscoisesdk.config.DEFAULT_WAIT_ON_RATE_LIMIT
                if the environment variable is not set.
            verify(bool,basestring): Controls whether we verify the server's
                TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to the IDENTITY_SERVICES_ENGINE_VERIFY
                (or IDENTITY_SERVICES_ENGINE_VERIFY_STRING) environment variable or
                ciscoisesdk.config.DEFAULT_VERIFY if the environment
                variables are not set.
            version(basestring): Controls which version of IDENTITY_SERVICES_ENGINE to use.
                Defaults to the IDENTITY_SERVICES_ENGINE_VERSION environment variable or
                ciscoisesdk.config.DEFAULT_VERSION
                if the environment variable is not set.
            debug(bool,basestring): Controls whether to log information about
                Identity Services Engine APIs' request and response process.
                Defaults to the IDENTITY_SERVICES_ENGINE_DEBUG environment variable or False
                if the environment variable is not set.
            object_factory(callable): The factory function to use to create
                Python objects from the returned Identity Services Engine JSON data objects.
            validator(callable): The factory class with function
                json_schema_validate(model:string) that returns an object with
                function validate(obj:dict) is used to validate Python objects
                sent in the request body.

        Returns:
            IdentityServicesEngineAPI: A new IdentityServicesEngineAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.
            VersionError: If the version is not provided via the version
                argument or an environment variable, or it is not a
                Identity Services Engine API supported version
                ['3.0.0', '3.1.0'].

        """
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)
        check_type(uses_api_gateway, (bool, basestring), may_be_none=False)
        check_type(debug, (bool, basestring), may_be_none=True)
        check_type(username, basestring, may_be_none=True)
        check_type(password, basestring, may_be_none=True)
        check_type(encoded_auth, basestring, may_be_none=True)
        check_type(verify, (bool, basestring), may_be_none=False)
        check_type(version, basestring, may_be_none=False)

        if isinstance(uses_api_gateway, str):
            uses_api_gateway = 'true' in uses_api_gateway.lower()

        if uses_api_gateway:
            check_type(base_url, basestring, may_be_none=False)
        else:
            check_type(ui_base_url, basestring, may_be_none=False)
            check_type(ers_base_url, basestring, may_be_none=False)
            check_type(mnt_base_url, basestring, may_be_none=False)
            check_type(px_grid_base_url, basestring, may_be_none=False)

        if version not in ['3.0.0', '3.1.0']:
            raise VersionError(
                'Unknown API version, '
                + 'known versions are {}'.format(
                    '3.0.0 and 3.1.0.'
                )
            )

        if version == '3.0.0':
            print("The minimum supported version is ISE 3.1. Future releases may drop the current version (3.0.0)")

        if isinstance(debug, str):
            debug = 'true' in debug.lower()

        # Check if the user has provided the required basicAuth parameters
        if encoded_auth is None and (username is None or password is None):
            raise AccessTokenError(
                "You need an access token to interact with the Identity Services Engine"
                " APIs. Identity Services Engine uses HTTP Basic Auth."
                " You must provide the username and password or just"
                " the encoded_auth, either by setting each parameter or its"
                " environment variable counterpart ("
                "IDENTITY_SERVICES_ENGINE_USERNAME, IDENTITY_SERVICES_ENGINE_PASSWORD,"
                " IDENTITY_SERVICES_ENGINE_ENCODED_AUTH)."
            )

        # Init Authentication wrapper early to use for basicAuth requests
        self.authentication = Authentication(
            base_url or ers_base_url, object_factory,
            single_request_timeout=single_request_timeout,
            verify=verify,
        )

        def get_access_token():
            return self.authentication.authentication_api(
                username=username,
                password=password,
                encoded_auth=encoded_auth).Token

        self._uses_api_gateway = uses_api_gateway

        # Create the API session
        # All of the API calls associated with a IdentityServicesEngineAPI object will
        # leverage a single RESTful 'session' connecting to the Identity Services Engine
        # cloud.
        self._session_ui = None
        self._session_ers = None
        self._session = None
        self._session_mnt = None
        self._session_px_grid = None
        if uses_api_gateway:
            self._session_ui = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                debug=debug,
            )
            self._session_ers = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                debug=debug,
            )
            self._session = self._session_ers
            self._session_mnt = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                headers={'Content-type': 'application/xml;charset=utf-8',
                         'Accept': 'application/xml'},
                debug=debug,
            )
            self._session_px_grid = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                debug=debug,
            )
        else:
            self._session_ui = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=ui_base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                debug=debug,
            )
            self._session_ers = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=ers_base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                debug=debug,
            )
            self._session = self._session_ers
            self._session_mnt = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=mnt_base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                headers={'Content-type': 'application/xml;charset=utf-8',
                         'Accept': 'application/xml'},
                debug=debug,
            )
            self._session_px_grid = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=px_grid_base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                debug=debug,
            )

        _validator = validator(version).json_schema_validate

        # API wrappers
        if version == '3.0.0':
            self.aci_bindings = \
                AciBindings_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.aci_settings = \
                AciSettings_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.anc_endpoint = \
                AncEndpoint_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.active_directory = \
                ActiveDirectory_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.admin_user = \
                AdminUser_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.anc_policy = \
                AncPolicy_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.byod_portal = \
                ByodPortal_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.certificate_profile = \
                CertificateProfile_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.certificate_template = \
                CertificateTemplate_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.certificates = \
                Certificates_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.clear_threats_and_vulnerabilities = \
                ClearThreatsAndVulnerabilities_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.consumer = \
                Consumer_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.endpoint_certificate = \
                EndpointCertificate_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.endpoint_identity_group = \
                EndpointIdentityGroup_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.filter_policy = \
                FilterPolicy_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_location = \
                GuestLocation_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_smtp_notification_configuration = \
                GuestSmtpNotificationConfiguration_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_ssid = \
                GuestSsid_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_type = \
                GuestType_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_user = \
                GuestUser_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.ip_to_sgt_mapping = \
                IpToSgtMapping_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.ip_to_sgt_mapping_group = \
                IpToSgtMappingGroup_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.identity_groups = \
                IdentityGroups_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.identity_sequence = \
                IdentitySequence_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.internal_user = \
                InternalUser_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.mdm = \
                Mdm_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.misc = \
                Misc_v3_0_0(
                    self._session_mnt, object_factory, _validator
                )
            self.my_device_portal = \
                MyDevicePortal_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.native_supplicant_profile = \
                NativeSupplicantProfile_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_device = \
                NetworkDevice_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.node_deployment = \
                NodeDeployment_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.node_group = \
                NodeGroup_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.node_details = \
                NodeDetails_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.pan_ha = \
                PanHa_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.portal_theme = \
                PortalTheme_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.profiler = \
                Profiler_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.profiler_profile = \
                ProfilerProfile_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.provider = \
                Provider_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.psn_node_details_with_radius_service = \
                PsnNodeDetailsWithRadiusService_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.pull_deployment_info = \
                PullDeploymentInfo_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.px_grid_settings = \
                PxGridSettings_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.radius_failure = \
                RadiusFailure_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.restid_store = \
                RestidStore_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.replication_status = \
                ReplicationStatus_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.repository = \
                Repository_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.sms_provider = \
                SmsProvider_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.sxp_connections = \
                SxpConnections_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.sxp_local_bindings = \
                SxpLocalBindings_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.sxp_vpns = \
                SxpVpns_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.security_group_to_virtual_network = \
                SecurityGroupToVirtualNetwork_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.security_groups = \
                SecurityGroups_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.security_groups_acls = \
                SecurityGroupsAcls_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.session_directory = \
                SessionDirectory_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.support_bundle_download = \
                SupportBundleDownload_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.support_bundle_status = \
                SupportBundleStatus_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.support_bundle_trigger_configuration = \
                SupportBundleTriggerConfiguration_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.sync_ise_node = \
                SyncIseNode_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
            self.system_health = \
                SystemHealth_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.system_certificate = \
                SystemCertificate_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.telemetry_information = \
                TelemetryInformation_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.trust_sec_configuration = \
                TrustSecConfiguration_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.trust_sec_sxp = \
                TrustSecSxp_v3_0_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.version_and_patch = \
                VersionAndPatch_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.version_info = \
                VersionInfo_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.endpoint = \
                Endpoint_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.portal = \
                Portal_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.px_grid_node = \
                PxGridNode_v3_0_0(
                    self._session_ers, object_factory, _validator
                )
            self.tasks = \
                Tasks_v3_0_0(
                    self._session_ui, object_factory, _validator
                )
        if version == '3.1.0':
            self.aci_bindings = \
                AciBindings_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.aci_settings = \
                AciSettings_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.anc_endpoint = \
                AncEndpoint_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.active_directory = \
                ActiveDirectory_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.admin_user = \
                AdminUser_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.anc_policy = \
                AncPolicy_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.byod_portal = \
                ByodPortal_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.certificate_profile = \
                CertificateProfile_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.certificate_template = \
                CertificateTemplate_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.certificates = \
                Certificates_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.clear_threats_and_vulnerabilities = \
                ClearThreatsAndVulnerabilities_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.consumer = \
                Consumer_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.endpoint_certificate = \
                EndpointCertificate_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.endpoint_identity_group = \
                EndpointIdentityGroup_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.filter_policy = \
                FilterPolicy_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_location = \
                GuestLocation_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_smtp_notification_configuration = \
                GuestSmtpNotificationConfiguration_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_ssid = \
                GuestSsid_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_type = \
                GuestType_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.guest_user = \
                GuestUser_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.ip_to_sgt_mapping = \
                IpToSgtMapping_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.ip_to_sgt_mapping_group = \
                IpToSgtMappingGroup_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.identity_groups = \
                IdentityGroups_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.identity_sequence = \
                IdentitySequence_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.internal_user = \
                InternalUser_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.mdm = \
                Mdm_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.misc = \
                Misc_v3_1_0(
                    self._session_mnt, object_factory, _validator
                )
            self.my_device_portal = \
                MyDevicePortal_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.native_supplicant_profile = \
                NativeSupplicantProfile_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.network_device = \
                NetworkDevice_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.node_deployment = \
                NodeDeployment_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.node_group = \
                NodeGroup_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.node_details = \
                NodeDetails_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.pan_ha = \
                PanHa_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.portal_theme = \
                PortalTheme_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.profiler = \
                Profiler_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.profiler_profile = \
                ProfilerProfile_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.provider = \
                Provider_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.psn_node_details_with_radius_service = \
                PsnNodeDetailsWithRadiusService_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.pull_deployment_info = \
                PullDeploymentInfo_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.px_grid_settings = \
                PxGridSettings_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.radius_failure = \
                RadiusFailure_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.restid_store = \
                RestidStore_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.replication_status = \
                ReplicationStatus_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.repository = \
                Repository_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.sms_provider = \
                SmsProvider_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sxp_connections = \
                SxpConnections_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sxp_local_bindings = \
                SxpLocalBindings_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sxp_vpns = \
                SxpVpns_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.security_group_to_virtual_network = \
                SecurityGroupToVirtualNetwork_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.security_groups = \
                SecurityGroups_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.security_groups_acls = \
                SecurityGroupsAcls_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.session_directory = \
                SessionDirectory_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.support_bundle_download = \
                SupportBundleDownload_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.support_bundle_status = \
                SupportBundleStatus_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.support_bundle_trigger_configuration = \
                SupportBundleTriggerConfiguration_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sync_ise_node = \
                SyncIseNode_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.system_health = \
                SystemHealth_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.system_certificate = \
                SystemCertificate_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.telemetry_information = \
                TelemetryInformation_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.trust_sec_configuration = \
                TrustSecConfiguration_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.trust_sec_sxp = \
                TrustSecSxp_v3_1_0(
                    self._session_px_grid, object_factory, _validator
                )
            self.version_and_patch = \
                VersionAndPatch_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.version_info = \
                VersionInfo_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.endpoint = \
                Endpoint_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.nbar_app = \
                NbarApp_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.portal = \
                Portal_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.px_grid_node = \
                PxGridNode_v3_1_0(
                    self._session_ers, object_factory, _validator
                )
            self.sg_vn_mapping = \
                SgVnMapping_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.tasks = \
                Tasks_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.virtual_network = \
                VirtualNetwork_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
            self.vn_vlan_mapping = \
                VnVlanMapping_v3_1_0(
                    self._session_ui, object_factory, _validator
                )
        self.custom_caller = \
            CustomCaller(self._session, object_factory)

    @property
    def uses_api_gateway(self):
        """If the Identity Services Engine API uses an API Gateway."""
        return self._uses_api_gateway

    @property
    def session(self):
        """The Identity Services Engine API session."""
        return self._session

    @property
    def session_ui(self):
        """The Identity Services Engine UI API session."""
        return self._session_ui

    @property
    def session_ers(self):
        """The Identity Services Engine ERS API session."""
        return self._session_ers

    @property
    def session_mnt(self):
        """The Identity Services Engine MNT API session."""
        return self._session_mnt

    @property
    def session_px_grid(self):
        """The Identity Services Engine PxGrid API session."""
        return self._session_px_grid

    @property
    def access_token(self):
        """The access token used for API calls to the Identity Services Engine service."""
        return self._session.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes for ERS and Custom Caller operations."""
        return self._session.base_url

    @property
    def ui_base_url(self):
        """The ui base URL prefixed to the individual API endpoint suffixes for UI operations."""
        return self._session_ui.base_url

    @property
    def ers_base_url(self):
        """The ers base URL prefixed to the individual API endpoint suffixes for ERS operations."""
        return self._session_ers.base_url

    @property
    def mnt_base_url(self):
        """The mnt base URL prefixed to the individual API endpoint suffixes for MNT operations."""
        return self._session_mnt.base_url

    @property
    def px_grid_base_url(self):
        """The px_grid base URL prefixed to the individual API endpoint suffixes for PxGrid operations"""
        return self._session_px_grid.base_url

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self._session.single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self._session.wait_on_rate_limit

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._session._verify

    @property
    def version(self):
        """The API version of Identity Services Engine."""
        return self._session._version

    @verify.setter
    def verify(self, value):
        """The verify (TLS Certificate) for the API endpoints."""
        self.authentication.verify = value
        self._session.verify = value

    @base_url.setter
    def base_url(self, value):
        """The base URL for the API endpoints for ERS and Custom Caller operations."""
        self._session.base_url = value

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """The timeout (seconds) for a single HTTP REST API request."""
        self.authentication.single_request_timeout = value
        self._session_ui.single_request_timeout = value
        self._session_ers.single_request_timeout = value
        self._session_mnt.single_request_timeout = value
        self._session_px_grid.single_request_timeout = value

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, value):
        """Enable or disable automatic rate-limit handling."""
        self._session_ui.wait_on_rate_limit = value
        self._session_ers.wait_on_rate_limit = value
        self._session_mnt.wait_on_rate_limit = value
        self._session_px_grid.wait_on_rate_limit = value

    @ui_base_url.setter
    def ui_base_url(self, value):
        """The ui base URL prefixed to the individual API endpoint suffixes for UI operations."""
        self._session_ui.base_url = value

    @ers_base_url.setter
    def ers_base_url(self, value):
        """The ers base URL prefixed to the individual API endpoint suffixes for ERS operations."""
        self._session_ers.base_url = value

    @mnt_base_url.setter
    def mnt_base_url(self, value):
        """The mnt base URL prefixed to the individual API endpoint suffixes for MNT operations."""
        self._session_mnt.base_url = value

    @px_grid_base_url.setter
    def px_grid_base_url(self, value):
        """The px_grid base URL prefixed to the individual API endpoint suffixes for PxGrid operations."""
        self._session_px_grid.base_url = value
