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

import warnings

import ciscoisesdk.environment as ciscoise_environment
from ciscoisesdk.config import (
    DEFAULT_BASE_URL,
    DEFAULT_DEBUG,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_USES_API_GATEWAY,
    DEFAULT_USES_CSRF_TOKEN,
    DEFAULT_VERIFY,
    DEFAULT_VERSION,
    DEFAULT_WAIT_ON_RATE_LIMIT,
)
from ciscoisesdk.exceptions import AccessTokenError, VersionError
from ciscoisesdk.models.mydict import mydict_data_factory
from ciscoisesdk.models.schema_validator import SchemaValidator
from ciscoisesdk.restsession import RestSession
from ciscoisesdk.utils import check_type
from .authentication import Authentication
from .custom_caller import CustomCaller
from .v3_1_0.aci_bindings import (
    AciBindings as AciBindings_v3_1_0
)
from .v3_1_0.aci_settings import (
    AciSettings as AciSettings_v3_1_0
)
from .v3_1_0.anc_endpoint import (
    AncEndpoint as AncEndpoint_v3_1_0
)
from .v3_1_0.active_directory import (
    ActiveDirectory as ActiveDirectory_v3_1_0
)
from .v3_1_0.admin_user import (
    AdminUser as AdminUser_v3_1_0
)
from .v3_1_0.allowed_protocols import (
    AllowedProtocols as AllowedProtocols_v3_1_0
)
from .v3_1_0.anc_policy import (
    AncPolicy as AncPolicy_v3_1_0
)
from .v3_1_0.authorization_profile import (
    AuthorizationProfile as AuthorizationProfile_v3_1_0
)
from .v3_1_0.byod_portal import (
    ByodPortal as ByodPortal_v3_1_0
)
from .v3_1_0.backup_and_restore import (
    BackupAndRestore as BackupAndRestore_v3_1_0
)
from .v3_1_0.certificate_profile import (
    CertificateProfile as CertificateProfile_v3_1_0
)
from .v3_1_0.certificate_template import (
    CertificateTemplate as CertificateTemplate_v3_1_0
)
from .v3_1_0.certificates import (
    Certificates as Certificates_v3_1_0
)
from .v3_1_0.clear_threats_and_vulnerabilities import (
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_1_0
)
from .v3_1_0.consumer import (
    Consumer as Consumer_v3_1_0
)
from .v3_1_0.device_administration_authentication_rules import (
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_1_0
)
from .v3_1_0.device_administration_authorization_exception_rules import (
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_1_0
)
from .v3_1_0.device_administration_authorization_global_exception_rules import (
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_0
)
from .v3_1_0.device_administration_authorization_rules import (
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_1_0
)
from .v3_1_0.device_administration_command_set import (
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_1_0
)
from .v3_1_0.device_administration_conditions import (
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_1_0
)
from .v3_1_0.device_administration_dictionary_attributes_list import (
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_1_0
)
from .v3_1_0.device_administration_identity_stores import (
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_1_0
)
from .v3_1_0.device_administration_network_conditions import (
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_1_0
)
from .v3_1_0.device_administration_policy_set import (
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_1_0
)
from .v3_1_0.device_administration_profiles import (
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_1_0
)
from .v3_1_0.device_administration_service_names import (
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_1_0
)
from .v3_1_0.device_administration_time_date_conditions import (
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_1_0
)
from .v3_1_0.downloadable_acl import (
    DownloadableAcl as DownloadableAcl_v3_1_0
)
from .v3_1_0.egress_matrix_cell import (
    EgressMatrixCell as EgressMatrixCell_v3_1_0
)
from .v3_1_0.endpoint_certificate import (
    EndpointCertificate as EndpointCertificate_v3_1_0
)
from .v3_1_0.endpoint_identity_group import (
    EndpointIdentityGroup as EndpointIdentityGroup_v3_1_0
)
from .v3_1_0.external_radius_server import (
    ExternalRadiusServer as ExternalRadiusServer_v3_1_0
)
from .v3_1_0.filter_policy import (
    FilterPolicy as FilterPolicy_v3_1_0
)
from .v3_1_0.guest_location import (
    GuestLocation as GuestLocation_v3_1_0
)
from .v3_1_0.guest_smtp_notification_configuration import (
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_1_0
)
from .v3_1_0.guest_ssid import (
    GuestSsid as GuestSsid_v3_1_0
)
from .v3_1_0.guest_type import (
    GuestType as GuestType_v3_1_0
)
from .v3_1_0.guest_user import (
    GuestUser as GuestUser_v3_1_0
)
from .v3_1_0.hotspot_portal import (
    HotspotPortal as HotspotPortal_v3_1_0
)
from .v3_1_0.ip_to_sgt_mapping import (
    IpToSgtMapping as IpToSgtMapping_v3_1_0
)
from .v3_1_0.ip_to_sgt_mapping_group import (
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_1_0
)
from .v3_1_0.identity_groups import (
    IdentityGroups as IdentityGroups_v3_1_0
)
from .v3_1_0.identity_sequence import (
    IdentitySequence as IdentitySequence_v3_1_0
)
from .v3_1_0.internal_user import (
    InternalUser as InternalUser_v3_1_0
)
from .v3_1_0.mdm import (
    Mdm as Mdm_v3_1_0
)
from .v3_1_0.misc import (
    Misc as Misc_v3_1_0
)
from .v3_1_0.my_device_portal import (
    MyDevicePortal as MyDevicePortal_v3_1_0
)
from .v3_1_0.native_supplicant_profile import (
    NativeSupplicantProfile as NativeSupplicantProfile_v3_1_0
)
from .v3_1_0.network_access_authentication_rules import (
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_1_0
)
from .v3_1_0.network_access_authorization_exception_rules import (
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_1_0
)
from .v3_1_0.network_access_authorization_global_exception_rules import (
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_1_0
)
from .v3_1_0.network_access_authorization_rules import (
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_1_0
)
from .v3_1_0.network_access_conditions import (
    NetworkAccessConditions as NetworkAccessConditions_v3_1_0
)
from .v3_1_0.network_access_dictionary import (
    NetworkAccessDictionary as NetworkAccessDictionary_v3_1_0
)
from .v3_1_0.network_access_dictionary_attribute import (
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_1_0
)
from .v3_1_0.network_access_dictionary_attributes_list import (
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_1_0
)
from .v3_1_0.network_access_identity_stores import (
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_1_0
)
from .v3_1_0.network_access_network_conditions import (
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_1_0
)
from .v3_1_0.network_access_policy_set import (
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_1_0
)
from .v3_1_0.network_access_profiles import (
    NetworkAccessProfiles as NetworkAccessProfiles_v3_1_0
)
from .v3_1_0.network_access_security_groups import (
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_1_0
)
from .v3_1_0.network_access_service_names import (
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_1_0
)
from .v3_1_0.network_access_time_date_conditions import (
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_1_0
)
from .v3_1_0.network_device import (
    NetworkDevice as NetworkDevice_v3_1_0
)
from .v3_1_0.network_device_group import (
    NetworkDeviceGroup as NetworkDeviceGroup_v3_1_0
)
from .v3_1_0.node_deployment import (
    NodeDeployment as NodeDeployment_v3_1_0
)
from .v3_1_0.node_group import (
    NodeGroup as NodeGroup_v3_1_0
)
from .v3_1_0.node_details import (
    NodeDetails as NodeDetails_v3_1_0
)
from .v3_1_0.pan_ha import (
    PanHa as PanHa_v3_1_0
)
from .v3_1_0.portal_global_setting import (
    PortalGlobalSetting as PortalGlobalSetting_v3_1_0
)
from .v3_1_0.portal_theme import (
    PortalTheme as PortalTheme_v3_1_0
)
from .v3_1_0.profiler import (
    Profiler as Profiler_v3_1_0
)
from .v3_1_0.profiler_profile import (
    ProfilerProfile as ProfilerProfile_v3_1_0
)
from .v3_1_0.provider import (
    Provider as Provider_v3_1_0
)
from .v3_1_0.psn_node_details_with_radius_service import (
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_1_0
)
from .v3_1_0.pull_deployment_info import (
    PullDeploymentInfo as PullDeploymentInfo_v3_1_0
)
from .v3_1_0.px_grid_settings import (
    PxGridSettings as PxGridSettings_v3_1_0
)
from .v3_1_0.radius_failure import (
    RadiusFailure as RadiusFailure_v3_1_0
)
from .v3_1_0.radius_server_sequence import (
    RadiusServerSequence as RadiusServerSequence_v3_1_0
)
from .v3_1_0.restid_store import (
    RestidStore as RestidStore_v3_1_0
)
from .v3_1_0.replication_status import (
    ReplicationStatus as ReplicationStatus_v3_1_0
)
from .v3_1_0.repository import (
    Repository as Repository_v3_1_0
)
from .v3_1_0.sms_provider import (
    SmsProvider as SmsProvider_v3_1_0
)
from .v3_1_0.sxp_connections import (
    SxpConnections as SxpConnections_v3_1_0
)
from .v3_1_0.sxp_local_bindings import (
    SxpLocalBindings as SxpLocalBindings_v3_1_0
)
from .v3_1_0.sxp_vpns import (
    SxpVpns as SxpVpns_v3_1_0
)
from .v3_1_0.security_group_to_virtual_network import (
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_1_0
)
from .v3_1_0.security_groups import (
    SecurityGroups as SecurityGroups_v3_1_0
)
from .v3_1_0.security_groups_acls import (
    SecurityGroupsAcls as SecurityGroupsAcls_v3_1_0
)
from .v3_1_0.self_registered_portal import (
    SelfRegisteredPortal as SelfRegisteredPortal_v3_1_0
)
from .v3_1_0.session_directory import (
    SessionDirectory as SessionDirectory_v3_1_0
)
from .v3_1_0.sponsor_group import (
    SponsorGroup as SponsorGroup_v3_1_0
)
from .v3_1_0.sponsor_group_member import (
    SponsorGroupMember as SponsorGroupMember_v3_1_0
)
from .v3_1_0.sponsor_portal import (
    SponsorPortal as SponsorPortal_v3_1_0
)
from .v3_1_0.sponsored_guest_portal import (
    SponsoredGuestPortal as SponsoredGuestPortal_v3_1_0
)
from .v3_1_0.support_bundle_download import (
    SupportBundleDownload as SupportBundleDownload_v3_1_0
)
from .v3_1_0.support_bundle_status import (
    SupportBundleStatus as SupportBundleStatus_v3_1_0
)
from .v3_1_0.support_bundle_trigger_configuration import (
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_1_0
)
from .v3_1_0.sync_ise_node import (
    SyncIseNode as SyncIseNode_v3_1_0
)
from .v3_1_0.system_health import (
    SystemHealth as SystemHealth_v3_1_0
)
from .v3_1_0.system_certificate import (
    SystemCertificate as SystemCertificate_v3_1_0
)
from .v3_1_0.tacacs_command_sets import (
    TacacsCommandSets as TacacsCommandSets_v3_1_0
)
from .v3_1_0.tacacs_external_servers import (
    TacacsExternalServers as TacacsExternalServers_v3_1_0
)
from .v3_1_0.tacacs_profile import (
    TacacsProfile as TacacsProfile_v3_1_0
)
from .v3_1_0.tacacs_server_sequence import (
    TacacsServerSequence as TacacsServerSequence_v3_1_0
)
from .v3_1_0.telemetry_information import (
    TelemetryInformation as TelemetryInformation_v3_1_0
)
from .v3_1_0.trust_sec_configuration import (
    TrustSecConfiguration as TrustSecConfiguration_v3_1_0
)
from .v3_1_0.trust_sec_sxp import (
    TrustSecSxp as TrustSecSxp_v3_1_0
)
from .v3_1_0.version_and_patch import (
    VersionAndPatch as VersionAndPatch_v3_1_0
)
from .v3_1_0.version_info import (
    VersionInfo as VersionInfo_v3_1_0
)
from .v3_1_0.endpoint import (
    Endpoint as Endpoint_v3_1_0
)
from .v3_1_0.nbar_app import (
    NbarApp as NbarApp_v3_1_0
)
from .v3_1_0.portal import (
    Portal as Portal_v3_1_0
)
from .v3_1_0.px_grid_node import (
    PxGridNode as PxGridNode_v3_1_0
)
from .v3_1_0.sg_vn_mapping import (
    SgVnMapping as SgVnMapping_v3_1_0
)
from .v3_1_0.tasks import (
    Tasks as Tasks_v3_1_0
)
from .v3_1_0.virtual_network import (
    VirtualNetwork as VirtualNetwork_v3_1_0
)
from .v3_1_0.vn_vlan_mapping import (
    VnVlanMapping as VnVlanMapping_v3_1_0
)
from .v3_1_1.aci_bindings import (
    AciBindings as AciBindings_v3_1_1
)
from .v3_1_1.aci_settings import (
    AciSettings as AciSettings_v3_1_1
)
from .v3_1_1.anc_endpoint import (
    AncEndpoint as AncEndpoint_v3_1_1
)
from .v3_1_1.active_directory import (
    ActiveDirectory as ActiveDirectory_v3_1_1
)
from .v3_1_1.admin_user import (
    AdminUser as AdminUser_v3_1_1
)
from .v3_1_1.allowed_protocols import (
    AllowedProtocols as AllowedProtocols_v3_1_1
)
from .v3_1_1.anc_policy import (
    AncPolicy as AncPolicy_v3_1_1
)
from .v3_1_1.authorization_profile import (
    AuthorizationProfile as AuthorizationProfile_v3_1_1
)
from .v3_1_1.byod_portal import (
    ByodPortal as ByodPortal_v3_1_1
)
from .v3_1_1.backup_and_restore import (
    BackupAndRestore as BackupAndRestore_v3_1_1
)
from .v3_1_1.certificate_profile import (
    CertificateProfile as CertificateProfile_v3_1_1
)
from .v3_1_1.certificate_template import (
    CertificateTemplate as CertificateTemplate_v3_1_1
)
from .v3_1_1.certificates import (
    Certificates as Certificates_v3_1_1
)
from .v3_1_1.clear_threats_and_vulnerabilities import (
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_1_1
)
from .v3_1_1.consumer import (
    Consumer as Consumer_v3_1_1
)
from .v3_1_1.device_administration_authentication_rules import (
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_1_1
)
from .v3_1_1.device_administration_authorization_exception_rules import (
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_1_1
)
from .v3_1_1.device_administration_authorization_global_exception_rules import (
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_1
)
from .v3_1_1.device_administration_authorization_rules import (
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_1_1
)
from .v3_1_1.device_administration_command_set import (
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_1_1
)
from .v3_1_1.device_administration_conditions import (
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_1_1
)
from .v3_1_1.device_administration_dictionary_attributes_list import (
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_1_1
)
from .v3_1_1.device_administration_identity_stores import (
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_1_1
)
from .v3_1_1.device_administration_network_conditions import (
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_1_1
)
from .v3_1_1.device_administration_policy_set import (
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_1_1
)
from .v3_1_1.device_administration_profiles import (
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_1_1
)
from .v3_1_1.device_administration_service_names import (
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_1_1
)
from .v3_1_1.device_administration_time_date_conditions import (
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_1_1
)
from .v3_1_1.downloadable_acl import (
    DownloadableAcl as DownloadableAcl_v3_1_1
)
from .v3_1_1.egress_matrix_cell import (
    EgressMatrixCell as EgressMatrixCell_v3_1_1
)
from .v3_1_1.endpoint_certificate import (
    EndpointCertificate as EndpointCertificate_v3_1_1
)
from .v3_1_1.endpoint_identity_group import (
    EndpointIdentityGroup as EndpointIdentityGroup_v3_1_1
)
from .v3_1_1.external_radius_server import (
    ExternalRadiusServer as ExternalRadiusServer_v3_1_1
)
from .v3_1_1.filter_policy import (
    FilterPolicy as FilterPolicy_v3_1_1
)
from .v3_1_1.guest_location import (
    GuestLocation as GuestLocation_v3_1_1
)
from .v3_1_1.guest_smtp_notification_configuration import (
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_1_1
)
from .v3_1_1.guest_ssid import (
    GuestSsid as GuestSsid_v3_1_1
)
from .v3_1_1.guest_type import (
    GuestType as GuestType_v3_1_1
)
from .v3_1_1.guest_user import (
    GuestUser as GuestUser_v3_1_1
)
from .v3_1_1.hotspot_portal import (
    HotspotPortal as HotspotPortal_v3_1_1
)
from .v3_1_1.ip_to_sgt_mapping import (
    IpToSgtMapping as IpToSgtMapping_v3_1_1
)
from .v3_1_1.ip_to_sgt_mapping_group import (
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_1_1
)
from .v3_1_1.identity_groups import (
    IdentityGroups as IdentityGroups_v3_1_1
)
from .v3_1_1.identity_sequence import (
    IdentitySequence as IdentitySequence_v3_1_1
)
from .v3_1_1.internal_user import (
    InternalUser as InternalUser_v3_1_1
)
from .v3_1_1.licensing import (
    Licensing as Licensing_v3_1_1
)
from .v3_1_1.mdm import (
    Mdm as Mdm_v3_1_1
)
from .v3_1_1.misc import (
    Misc as Misc_v3_1_1
)
from .v3_1_1.my_device_portal import (
    MyDevicePortal as MyDevicePortal_v3_1_1
)
from .v3_1_1.native_supplicant_profile import (
    NativeSupplicantProfile as NativeSupplicantProfile_v3_1_1
)
from .v3_1_1.network_access_authentication_rules import (
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_1_1
)
from .v3_1_1.network_access_authorization_exception_rules import (
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_1_1
)
from .v3_1_1.network_access_authorization_global_exception_rules import (
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_1_1
)
from .v3_1_1.network_access_authorization_rules import (
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_1_1
)
from .v3_1_1.network_access_conditions import (
    NetworkAccessConditions as NetworkAccessConditions_v3_1_1
)
from .v3_1_1.network_access_dictionary import (
    NetworkAccessDictionary as NetworkAccessDictionary_v3_1_1
)
from .v3_1_1.network_access_dictionary_attribute import (
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_1_1
)
from .v3_1_1.network_access_dictionary_attributes_list import (
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_1_1
)
from .v3_1_1.network_access_identity_stores import (
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_1_1
)
from .v3_1_1.network_access_network_conditions import (
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_1_1
)
from .v3_1_1.network_access_policy_set import (
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_1_1
)
from .v3_1_1.network_access_profiles import (
    NetworkAccessProfiles as NetworkAccessProfiles_v3_1_1
)
from .v3_1_1.network_access_security_groups import (
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_1_1
)
from .v3_1_1.network_access_service_names import (
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_1_1
)
from .v3_1_1.network_access_time_date_conditions import (
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_1_1
)
from .v3_1_1.network_device import (
    NetworkDevice as NetworkDevice_v3_1_1
)
from .v3_1_1.network_device_group import (
    NetworkDeviceGroup as NetworkDeviceGroup_v3_1_1
)
from .v3_1_1.node_deployment import (
    NodeDeployment as NodeDeployment_v3_1_1
)
from .v3_1_1.node_group import (
    NodeGroup as NodeGroup_v3_1_1
)
from .v3_1_1.node_services import (
    NodeServices as NodeServices_v3_1_1
)
from .v3_1_1.node_details import (
    NodeDetails as NodeDetails_v3_1_1
)
from .v3_1_1.pan_ha import (
    PanHa as PanHa_v3_1_1
)
from .v3_1_1.patching import (
    Patching as Patching_v3_1_1
)
from .v3_1_1.portal_global_setting import (
    PortalGlobalSetting as PortalGlobalSetting_v3_1_1
)
from .v3_1_1.portal_theme import (
    PortalTheme as PortalTheme_v3_1_1
)
from .v3_1_1.profiler import (
    Profiler as Profiler_v3_1_1
)
from .v3_1_1.profiler_profile import (
    ProfilerProfile as ProfilerProfile_v3_1_1
)
from .v3_1_1.provider import (
    Provider as Provider_v3_1_1
)
from .v3_1_1.psn_node_details_with_radius_service import (
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_1_1
)
from .v3_1_1.pull_deployment_info import (
    PullDeploymentInfo as PullDeploymentInfo_v3_1_1
)
from .v3_1_1.px_grid_settings import (
    PxGridSettings as PxGridSettings_v3_1_1
)
from .v3_1_1.radius_failure import (
    RadiusFailure as RadiusFailure_v3_1_1
)
from .v3_1_1.radius_server_sequence import (
    RadiusServerSequence as RadiusServerSequence_v3_1_1
)
from .v3_1_1.restid_store import (
    RestidStore as RestidStore_v3_1_1
)
from .v3_1_1.repository import (
    Repository as Repository_v3_1_1
)
from .v3_1_1.sms_provider import (
    SmsProvider as SmsProvider_v3_1_1
)
from .v3_1_1.sxp_connections import (
    SxpConnections as SxpConnections_v3_1_1
)
from .v3_1_1.sxp_local_bindings import (
    SxpLocalBindings as SxpLocalBindings_v3_1_1
)
from .v3_1_1.sxp_vpns import (
    SxpVpns as SxpVpns_v3_1_1
)
from .v3_1_1.security_group_to_virtual_network import (
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_1_1
)
from .v3_1_1.security_groups import (
    SecurityGroups as SecurityGroups_v3_1_1
)
from .v3_1_1.security_groups_acls import (
    SecurityGroupsAcls as SecurityGroupsAcls_v3_1_1
)
from .v3_1_1.self_registered_portal import (
    SelfRegisteredPortal as SelfRegisteredPortal_v3_1_1
)
from .v3_1_1.session_directory import (
    SessionDirectory as SessionDirectory_v3_1_1
)
from .v3_1_1.sponsor_group import (
    SponsorGroup as SponsorGroup_v3_1_1
)
from .v3_1_1.sponsor_group_member import (
    SponsorGroupMember as SponsorGroupMember_v3_1_1
)
from .v3_1_1.sponsor_portal import (
    SponsorPortal as SponsorPortal_v3_1_1
)
from .v3_1_1.sponsored_guest_portal import (
    SponsoredGuestPortal as SponsoredGuestPortal_v3_1_1
)
from .v3_1_1.support_bundle_download import (
    SupportBundleDownload as SupportBundleDownload_v3_1_1
)
from .v3_1_1.support_bundle_status import (
    SupportBundleStatus as SupportBundleStatus_v3_1_1
)
from .v3_1_1.support_bundle_trigger_configuration import (
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_1_1
)
from .v3_1_1.system_health import (
    SystemHealth as SystemHealth_v3_1_1
)
from .v3_1_1.system_certificate import (
    SystemCertificate as SystemCertificate_v3_1_1
)
from .v3_1_1.tacacs_command_sets import (
    TacacsCommandSets as TacacsCommandSets_v3_1_1
)
from .v3_1_1.tacacs_external_servers import (
    TacacsExternalServers as TacacsExternalServers_v3_1_1
)
from .v3_1_1.tacacs_profile import (
    TacacsProfile as TacacsProfile_v3_1_1
)
from .v3_1_1.tacacs_server_sequence import (
    TacacsServerSequence as TacacsServerSequence_v3_1_1
)
from .v3_1_1.telemetry_information import (
    TelemetryInformation as TelemetryInformation_v3_1_1
)
from .v3_1_1.trust_sec_configuration import (
    TrustSecConfiguration as TrustSecConfiguration_v3_1_1
)
from .v3_1_1.trust_sec_sxp import (
    TrustSecSxp as TrustSecSxp_v3_1_1
)
from .v3_1_1.version_and_patch import (
    VersionAndPatch as VersionAndPatch_v3_1_1
)
from .v3_1_1.version_info import (
    VersionInfo as VersionInfo_v3_1_1
)
from .v3_1_1.endpoint import (
    Endpoint as Endpoint_v3_1_1
)
from .v3_1_1.nbar_app import (
    NbarApp as NbarApp_v3_1_1
)
from .v3_1_1.portal import (
    Portal as Portal_v3_1_1
)
from .v3_1_1.proxy import (
    Proxy as Proxy_v3_1_1
)
from .v3_1_1.px_grid_node import (
    PxGridNode as PxGridNode_v3_1_1
)
from .v3_1_1.sg_vn_mapping import (
    SgVnMapping as SgVnMapping_v3_1_1
)
from .v3_1_1.tasks import (
    Tasks as Tasks_v3_1_1
)
from .v3_1_1.telemetry import (
    Telemetry as Telemetry_v3_1_1
)
from .v3_1_1.virtual_network import (
    VirtualNetwork as VirtualNetwork_v3_1_1
)
from .v3_1_1.vn_vlan_mapping import (
    VnVlanMapping as VnVlanMapping_v3_1_1
)
from .v3_1_patch_1.aci_bindings import (
    AciBindings as AciBindings_v3_1_patch_1
)
from .v3_1_patch_1.aci_settings import (
    AciSettings as AciSettings_v3_1_patch_1
)
from .v3_1_patch_1.anc_endpoint import (
    AncEndpoint as AncEndpoint_v3_1_patch_1
)
from .v3_1_patch_1.active_directory import (
    ActiveDirectory as ActiveDirectory_v3_1_patch_1
)
from .v3_1_patch_1.admin_user import (
    AdminUser as AdminUser_v3_1_patch_1
)
from .v3_1_patch_1.allowed_protocols import (
    AllowedProtocols as AllowedProtocols_v3_1_patch_1
)
from .v3_1_patch_1.anc_policy import (
    AncPolicy as AncPolicy_v3_1_patch_1
)
from .v3_1_patch_1.authorization_profile import (
    AuthorizationProfile as AuthorizationProfile_v3_1_patch_1
)
from .v3_1_patch_1.byod_portal import (
    ByodPortal as ByodPortal_v3_1_patch_1
)
from .v3_1_patch_1.backup_and_restore import (
    BackupAndRestore as BackupAndRestore_v3_1_patch_1
)
from .v3_1_patch_1.certificate_profile import (
    CertificateProfile as CertificateProfile_v3_1_patch_1
)
from .v3_1_patch_1.certificate_template import (
    CertificateTemplate as CertificateTemplate_v3_1_patch_1
)
from .v3_1_patch_1.certificates import (
    Certificates as Certificates_v3_1_patch_1
)
from .v3_1_patch_1.clear_threats_and_vulnerabilities import (
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_1_patch_1
)
from .v3_1_patch_1.consumer import (
    Consumer as Consumer_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_authentication_rules import (
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_authorization_exception_rules import (
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_authorization_global_exception_rules import (
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_authorization_rules import (
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_command_set import (
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_conditions import (
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_dictionary_attributes_list import (
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_identity_stores import (
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_network_conditions import (
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_policy_set import (
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_profiles import (
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_service_names import (
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_1_patch_1
)
from .v3_1_patch_1.device_administration_time_date_conditions import (
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_1_patch_1
)
from .v3_1_patch_1.downloadable_acl import (
    DownloadableAcl as DownloadableAcl_v3_1_patch_1
)
from .v3_1_patch_1.egress_matrix_cell import (
    EgressMatrixCell as EgressMatrixCell_v3_1_patch_1
)
from .v3_1_patch_1.endpoint_certificate import (
    EndpointCertificate as EndpointCertificate_v3_1_patch_1
)
from .v3_1_patch_1.endpoint_identity_group import (
    EndpointIdentityGroup as EndpointIdentityGroup_v3_1_patch_1
)
from .v3_1_patch_1.external_radius_server import (
    ExternalRadiusServer as ExternalRadiusServer_v3_1_patch_1
)
from .v3_1_patch_1.filter_policy import (
    FilterPolicy as FilterPolicy_v3_1_patch_1
)
from .v3_1_patch_1.guest_location import (
    GuestLocation as GuestLocation_v3_1_patch_1
)
from .v3_1_patch_1.guest_smtp_notification_configuration import (
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_1_patch_1
)
from .v3_1_patch_1.guest_ssid import (
    GuestSsid as GuestSsid_v3_1_patch_1
)
from .v3_1_patch_1.guest_type import (
    GuestType as GuestType_v3_1_patch_1
)
from .v3_1_patch_1.guest_user import (
    GuestUser as GuestUser_v3_1_patch_1
)
from .v3_1_patch_1.hotspot_portal import (
    HotspotPortal as HotspotPortal_v3_1_patch_1
)
from .v3_1_patch_1.ip_to_sgt_mapping import (
    IpToSgtMapping as IpToSgtMapping_v3_1_patch_1
)
from .v3_1_patch_1.ip_to_sgt_mapping_group import (
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_1_patch_1
)
from .v3_1_patch_1.identity_groups import (
    IdentityGroups as IdentityGroups_v3_1_patch_1
)
from .v3_1_patch_1.identity_sequence import (
    IdentitySequence as IdentitySequence_v3_1_patch_1
)
from .v3_1_patch_1.internal_user import (
    InternalUser as InternalUser_v3_1_patch_1
)
from .v3_1_patch_1.licensing import (
    Licensing as Licensing_v3_1_patch_1
)
from .v3_1_patch_1.mdm import (
    Mdm as Mdm_v3_1_patch_1
)
from .v3_1_patch_1.misc import (
    Misc as Misc_v3_1_patch_1
)
from .v3_1_patch_1.my_device_portal import (
    MyDevicePortal as MyDevicePortal_v3_1_patch_1
)
from .v3_1_patch_1.native_supplicant_profile import (
    NativeSupplicantProfile as NativeSupplicantProfile_v3_1_patch_1
)
from .v3_1_patch_1.network_access_authentication_rules import (
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_1_patch_1
)
from .v3_1_patch_1.network_access_authorization_exception_rules import (
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_1_patch_1
)
from .v3_1_patch_1.network_access_authorization_global_exception_rules import (
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_1_patch_1
)
from .v3_1_patch_1.network_access_authorization_rules import (
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_1_patch_1
)
from .v3_1_patch_1.network_access_conditions import (
    NetworkAccessConditions as NetworkAccessConditions_v3_1_patch_1
)
from .v3_1_patch_1.network_access_dictionary import (
    NetworkAccessDictionary as NetworkAccessDictionary_v3_1_patch_1
)
from .v3_1_patch_1.network_access_dictionary_attribute import (
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_1_patch_1
)
from .v3_1_patch_1.network_access_dictionary_attributes_list import (
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_1_patch_1
)
from .v3_1_patch_1.network_access_identity_stores import (
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_1_patch_1
)
from .v3_1_patch_1.network_access_network_conditions import (
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_1_patch_1
)
from .v3_1_patch_1.network_access_policy_set import (
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_1_patch_1
)
from .v3_1_patch_1.network_access_profiles import (
    NetworkAccessProfiles as NetworkAccessProfiles_v3_1_patch_1
)
from .v3_1_patch_1.network_access_security_groups import (
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_1_patch_1
)
from .v3_1_patch_1.network_access_service_names import (
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_1_patch_1
)
from .v3_1_patch_1.network_access_time_date_conditions import (
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_1_patch_1
)
from .v3_1_patch_1.network_device import (
    NetworkDevice as NetworkDevice_v3_1_patch_1
)
from .v3_1_patch_1.network_device_group import (
    NetworkDeviceGroup as NetworkDeviceGroup_v3_1_patch_1
)
from .v3_1_patch_1.node_deployment import (
    NodeDeployment as NodeDeployment_v3_1_patch_1
)
from .v3_1_patch_1.node_group import (
    NodeGroup as NodeGroup_v3_1_patch_1
)
from .v3_1_patch_1.node_services import (
    NodeServices as NodeServices_v3_1_patch_1
)
from .v3_1_patch_1.node_details import (
    NodeDetails as NodeDetails_v3_1_patch_1
)
from .v3_1_patch_1.pan_ha import (
    PanHa as PanHa_v3_1_patch_1
)
from .v3_1_patch_1.patching import (
    Patching as Patching_v3_1_patch_1
)
from .v3_1_patch_1.portal_global_setting import (
    PortalGlobalSetting as PortalGlobalSetting_v3_1_patch_1
)
from .v3_1_patch_1.portal_theme import (
    PortalTheme as PortalTheme_v3_1_patch_1
)
from .v3_1_patch_1.profiler import (
    Profiler as Profiler_v3_1_patch_1
)
from .v3_1_patch_1.profiler_profile import (
    ProfilerProfile as ProfilerProfile_v3_1_patch_1
)
from .v3_1_patch_1.provider import (
    Provider as Provider_v3_1_patch_1
)
from .v3_1_patch_1.psn_node_details_with_radius_service import (
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_1_patch_1
)
from .v3_1_patch_1.pull_deployment_info import (
    PullDeploymentInfo as PullDeploymentInfo_v3_1_patch_1
)
from .v3_1_patch_1.px_grid_settings import (
    PxGridSettings as PxGridSettings_v3_1_patch_1
)
from .v3_1_patch_1.radius_failure import (
    RadiusFailure as RadiusFailure_v3_1_patch_1
)
from .v3_1_patch_1.radius_server_sequence import (
    RadiusServerSequence as RadiusServerSequence_v3_1_patch_1
)
from .v3_1_patch_1.restid_store import (
    RestidStore as RestidStore_v3_1_patch_1
)
from .v3_1_patch_1.repository import (
    Repository as Repository_v3_1_patch_1
)
from .v3_1_patch_1.sms_provider import (
    SmsProvider as SmsProvider_v3_1_patch_1
)
from .v3_1_patch_1.sxp_connections import (
    SxpConnections as SxpConnections_v3_1_patch_1
)
from .v3_1_patch_1.sxp_local_bindings import (
    SxpLocalBindings as SxpLocalBindings_v3_1_patch_1
)
from .v3_1_patch_1.sxp_vpns import (
    SxpVpns as SxpVpns_v3_1_patch_1
)
from .v3_1_patch_1.security_group_to_virtual_network import (
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_1_patch_1
)
from .v3_1_patch_1.security_groups import (
    SecurityGroups as SecurityGroups_v3_1_patch_1
)
from .v3_1_patch_1.security_groups_acls import (
    SecurityGroupsAcls as SecurityGroupsAcls_v3_1_patch_1
)
from .v3_1_patch_1.self_registered_portal import (
    SelfRegisteredPortal as SelfRegisteredPortal_v3_1_patch_1
)
from .v3_1_patch_1.session_directory import (
    SessionDirectory as SessionDirectory_v3_1_patch_1
)
from .v3_1_patch_1.sponsor_group import (
    SponsorGroup as SponsorGroup_v3_1_patch_1
)
from .v3_1_patch_1.sponsor_group_member import (
    SponsorGroupMember as SponsorGroupMember_v3_1_patch_1
)
from .v3_1_patch_1.sponsor_portal import (
    SponsorPortal as SponsorPortal_v3_1_patch_1
)
from .v3_1_patch_1.sponsored_guest_portal import (
    SponsoredGuestPortal as SponsoredGuestPortal_v3_1_patch_1
)
from .v3_1_patch_1.support_bundle_download import (
    SupportBundleDownload as SupportBundleDownload_v3_1_patch_1
)
from .v3_1_patch_1.support_bundle_status import (
    SupportBundleStatus as SupportBundleStatus_v3_1_patch_1
)
from .v3_1_patch_1.support_bundle_trigger_configuration import (
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_1_patch_1
)
from .v3_1_patch_1.system_health import (
    SystemHealth as SystemHealth_v3_1_patch_1
)
from .v3_1_patch_1.system_certificate import (
    SystemCertificate as SystemCertificate_v3_1_patch_1
)
from .v3_1_patch_1.tacacs_command_sets import (
    TacacsCommandSets as TacacsCommandSets_v3_1_patch_1
)
from .v3_1_patch_1.tacacs_external_servers import (
    TacacsExternalServers as TacacsExternalServers_v3_1_patch_1
)
from .v3_1_patch_1.tacacs_profile import (
    TacacsProfile as TacacsProfile_v3_1_patch_1
)
from .v3_1_patch_1.tacacs_server_sequence import (
    TacacsServerSequence as TacacsServerSequence_v3_1_patch_1
)
from .v3_1_patch_1.telemetry_information import (
    TelemetryInformation as TelemetryInformation_v3_1_patch_1
)
from .v3_1_patch_1.trust_sec_configuration import (
    TrustSecConfiguration as TrustSecConfiguration_v3_1_patch_1
)
from .v3_1_patch_1.trust_sec_sxp import (
    TrustSecSxp as TrustSecSxp_v3_1_patch_1
)
from .v3_1_patch_1.version_and_patch import (
    VersionAndPatch as VersionAndPatch_v3_1_patch_1
)
from .v3_1_patch_1.version_info import (
    VersionInfo as VersionInfo_v3_1_patch_1
)
from .v3_1_patch_1.endpoint import (
    Endpoint as Endpoint_v3_1_patch_1
)
from .v3_1_patch_1.nbar_app import (
    NbarApp as NbarApp_v3_1_patch_1
)
from .v3_1_patch_1.portal import (
    Portal as Portal_v3_1_patch_1
)
from .v3_1_patch_1.proxy import (
    Proxy as Proxy_v3_1_patch_1
)
from .v3_1_patch_1.px_grid_node import (
    PxGridNode as PxGridNode_v3_1_patch_1
)
from .v3_1_patch_1.sg_vn_mapping import (
    SgVnMapping as SgVnMapping_v3_1_patch_1
)
from .v3_1_patch_1.tasks import (
    Tasks as Tasks_v3_1_patch_1
)
from .v3_1_patch_1.telemetry import (
    Telemetry as Telemetry_v3_1_patch_1
)
from .v3_1_patch_1.virtual_network import (
    VirtualNetwork as VirtualNetwork_v3_1_patch_1
)
from .v3_1_patch_1.vn_vlan_mapping import (
    VnVlanMapping as VnVlanMapping_v3_1_patch_1
)
from .v3_2_beta.aci_bindings import (
    AciBindings as AciBindings_v3_2_beta
)
from .v3_2_beta.aci_settings import (
    AciSettings as AciSettings_v3_2_beta
)
from .v3_2_beta.anc_endpoint import (
    AncEndpoint as AncEndpoint_v3_2_beta
)
from .v3_2_beta.active_directory import (
    ActiveDirectory as ActiveDirectory_v3_2_beta
)
from .v3_2_beta.admin_user import (
    AdminUser as AdminUser_v3_2_beta
)
from .v3_2_beta.allowed_protocols import (
    AllowedProtocols as AllowedProtocols_v3_2_beta
)
from .v3_2_beta.anc_policy import (
    AncPolicy as AncPolicy_v3_2_beta
)
from .v3_2_beta.authorization_profile import (
    AuthorizationProfile as AuthorizationProfile_v3_2_beta
)
from .v3_2_beta.byod_portal import (
    ByodPortal as ByodPortal_v3_2_beta
)
from .v3_2_beta.backup_and_restore import (
    BackupAndRestore as BackupAndRestore_v3_2_beta
)
from .v3_2_beta.certificate_profile import (
    CertificateProfile as CertificateProfile_v3_2_beta
)
from .v3_2_beta.certificate_template import (
    CertificateTemplate as CertificateTemplate_v3_2_beta
)
from .v3_2_beta.certificates import (
    Certificates as Certificates_v3_2_beta
)
from .v3_2_beta.clear_threats_and_vulnerabilities import (
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_2_beta
)
from .v3_2_beta.configuration import (
    Configuration as Configuration_v3_2_beta
)
from .v3_2_beta.consumer import (
    Consumer as Consumer_v3_2_beta
)
from .v3_2_beta.dataconnect_services import (
    DataconnectServices as DataconnectServices_v3_2_beta
)
from .v3_2_beta.device_administration_authentication_rules import (
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_2_beta
)
from .v3_2_beta.device_administration_authorization_exception_rules import (
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_2_beta
)
from .v3_2_beta.device_administration_authorization_global_exception_rules import (
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_2_beta
)
from .v3_2_beta.device_administration_authorization_rules import (
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_2_beta
)
from .v3_2_beta.device_administration_command_set import (
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_2_beta
)
from .v3_2_beta.device_administration_conditions import (
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_2_beta
)
from .v3_2_beta.device_administration_dictionary_attributes_list import (
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_2_beta
)
from .v3_2_beta.device_administration_identity_stores import (
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_2_beta
)
from .v3_2_beta.device_administration_network_conditions import (
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_2_beta
)
from .v3_2_beta.device_administration_policy_set import (
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_2_beta
)
from .v3_2_beta.device_administration_profiles import (
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_2_beta
)
from .v3_2_beta.device_administration_service_names import (
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_2_beta
)
from .v3_2_beta.device_administration_time_date_conditions import (
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_2_beta
)
from .v3_2_beta.downloadable_acl import (
    DownloadableAcl as DownloadableAcl_v3_2_beta
)
from .v3_2_beta.edda import (
    Edda as Edda_v3_2_beta
)
from .v3_2_beta.egress_matrix_cell import (
    EgressMatrixCell as EgressMatrixCell_v3_2_beta
)
from .v3_2_beta.endpoint_certificate import (
    EndpointCertificate as EndpointCertificate_v3_2_beta
)
from .v3_2_beta.endpoint_identity_group import (
    EndpointIdentityGroup as EndpointIdentityGroup_v3_2_beta
)
from .v3_2_beta.external_radius_server import (
    ExternalRadiusServer as ExternalRadiusServer_v3_2_beta
)
from .v3_2_beta.filter_policy import (
    FilterPolicy as FilterPolicy_v3_2_beta
)
from .v3_2_beta.guest_location import (
    GuestLocation as GuestLocation_v3_2_beta
)
from .v3_2_beta.guest_smtp_notification_configuration import (
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_2_beta
)
from .v3_2_beta.guest_ssid import (
    GuestSsid as GuestSsid_v3_2_beta
)
from .v3_2_beta.guest_type import (
    GuestType as GuestType_v3_2_beta
)
from .v3_2_beta.guest_user import (
    GuestUser as GuestUser_v3_2_beta
)
from .v3_2_beta.hotspot_portal import (
    HotspotPortal as HotspotPortal_v3_2_beta
)
from .v3_2_beta.ip_to_sgt_mapping import (
    IpToSgtMapping as IpToSgtMapping_v3_2_beta
)
from .v3_2_beta.ip_to_sgt_mapping_group import (
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_2_beta
)
from .v3_2_beta.identity_groups import (
    IdentityGroups as IdentityGroups_v3_2_beta
)
from .v3_2_beta.identity_sequence import (
    IdentitySequence as IdentitySequence_v3_2_beta
)
from .v3_2_beta.internal_user import (
    InternalUser as InternalUser_v3_2_beta
)
from .v3_2_beta.licensing import (
    Licensing as Licensing_v3_2_beta
)
from .v3_2_beta.mdm import (
    Mdm as Mdm_v3_2_beta
)
from .v3_2_beta.misc import (
    Misc as Misc_v3_2_beta
)
from .v3_2_beta.my_device_portal import (
    MyDevicePortal as MyDevicePortal_v3_2_beta
)
from .v3_2_beta.native_supplicant_profile import (
    NativeSupplicantProfile as NativeSupplicantProfile_v3_2_beta
)
from .v3_2_beta.network_access_authentication_rules import (
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_2_beta
)
from .v3_2_beta.network_access_authorization_exception_rules import (
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_2_beta
)
from .v3_2_beta.network_access_authorization_global_exception_rules import (
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_2_beta
)
from .v3_2_beta.network_access_authorization_rules import (
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_2_beta
)
from .v3_2_beta.network_access_conditions import (
    NetworkAccessConditions as NetworkAccessConditions_v3_2_beta
)
from .v3_2_beta.network_access_dictionary import (
    NetworkAccessDictionary as NetworkAccessDictionary_v3_2_beta
)
from .v3_2_beta.network_access_dictionary_attribute import (
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_2_beta
)
from .v3_2_beta.network_access_dictionary_attributes_list import (
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_2_beta
)
from .v3_2_beta.network_access_identity_stores import (
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_2_beta
)
from .v3_2_beta.network_access_network_conditions import (
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_2_beta
)
from .v3_2_beta.network_access_policy_set import (
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_2_beta
)
from .v3_2_beta.network_access_profiles import (
    NetworkAccessProfiles as NetworkAccessProfiles_v3_2_beta
)
from .v3_2_beta.network_access_security_groups import (
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_2_beta
)
from .v3_2_beta.network_access_service_names import (
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_2_beta
)
from .v3_2_beta.network_access_time_date_conditions import (
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_2_beta
)
from .v3_2_beta.network_device import (
    NetworkDevice as NetworkDevice_v3_2_beta
)
from .v3_2_beta.network_device_group import (
    NetworkDeviceGroup as NetworkDeviceGroup_v3_2_beta
)
from .v3_2_beta.node_deployment import (
    NodeDeployment as NodeDeployment_v3_2_beta
)
from .v3_2_beta.node_group import (
    NodeGroup as NodeGroup_v3_2_beta
)
from .v3_2_beta.node_services import (
    NodeServices as NodeServices_v3_2_beta
)
from .v3_2_beta.node_details import (
    NodeDetails as NodeDetails_v3_2_beta
)
from .v3_2_beta.pan_ha import (
    PanHa as PanHa_v3_2_beta
)
from .v3_2_beta.patching import (
    Patching as Patching_v3_2_beta
)
from .v3_2_beta.portal_global_setting import (
    PortalGlobalSetting as PortalGlobalSetting_v3_2_beta
)
from .v3_2_beta.portal_theme import (
    PortalTheme as PortalTheme_v3_2_beta
)
from .v3_2_beta.profiler import (
    Profiler as Profiler_v3_2_beta
)
from .v3_2_beta.profiler_profile import (
    ProfilerProfile as ProfilerProfile_v3_2_beta
)
from .v3_2_beta.provider import (
    Provider as Provider_v3_2_beta
)
from .v3_2_beta.psn_node_details_with_radius_service import (
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_2_beta
)
from .v3_2_beta.pull_deployment_info import (
    PullDeploymentInfo as PullDeploymentInfo_v3_2_beta
)
from .v3_2_beta.px_grid_settings import (
    PxGridSettings as PxGridSettings_v3_2_beta
)
from .v3_2_beta.radius_failure import (
    RadiusFailure as RadiusFailure_v3_2_beta
)
from .v3_2_beta.radius_server_sequence import (
    RadiusServerSequence as RadiusServerSequence_v3_2_beta
)
from .v3_2_beta.restid_store import (
    RestidStore as RestidStore_v3_2_beta
)
from .v3_2_beta.repository import (
    Repository as Repository_v3_2_beta
)
from .v3_2_beta.sms_provider import (
    SmsProvider as SmsProvider_v3_2_beta
)
from .v3_2_beta.sxp_connections import (
    SxpConnections as SxpConnections_v3_2_beta
)
from .v3_2_beta.sxp_local_bindings import (
    SxpLocalBindings as SxpLocalBindings_v3_2_beta
)
from .v3_2_beta.sxp_vpns import (
    SxpVpns as SxpVpns_v3_2_beta
)
from .v3_2_beta.security_group_to_virtual_network import (
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_2_beta
)
from .v3_2_beta.security_groups import (
    SecurityGroups as SecurityGroups_v3_2_beta
)
from .v3_2_beta.security_groups_acls import (
    SecurityGroupsAcls as SecurityGroupsAcls_v3_2_beta
)
from .v3_2_beta.self_registered_portal import (
    SelfRegisteredPortal as SelfRegisteredPortal_v3_2_beta
)
from .v3_2_beta.session_directory import (
    SessionDirectory as SessionDirectory_v3_2_beta
)
from .v3_2_beta.sponsor_group import (
    SponsorGroup as SponsorGroup_v3_2_beta
)
from .v3_2_beta.sponsor_group_member import (
    SponsorGroupMember as SponsorGroupMember_v3_2_beta
)
from .v3_2_beta.sponsor_portal import (
    SponsorPortal as SponsorPortal_v3_2_beta
)
from .v3_2_beta.sponsored_guest_portal import (
    SponsoredGuestPortal as SponsoredGuestPortal_v3_2_beta
)
from .v3_2_beta.subscriber import (
    Subscriber as Subscriber_v3_2_beta
)
from .v3_2_beta.support_bundle_download import (
    SupportBundleDownload as SupportBundleDownload_v3_2_beta
)
from .v3_2_beta.support_bundle_status import (
    SupportBundleStatus as SupportBundleStatus_v3_2_beta
)
from .v3_2_beta.support_bundle_trigger_configuration import (
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_2_beta
)
from .v3_2_beta.system_health import (
    SystemHealth as SystemHealth_v3_2_beta
)
from .v3_2_beta.system_certificate import (
    SystemCertificate as SystemCertificate_v3_2_beta
)
from .v3_2_beta.tacacs_command_sets import (
    TacacsCommandSets as TacacsCommandSets_v3_2_beta
)
from .v3_2_beta.tacacs_external_servers import (
    TacacsExternalServers as TacacsExternalServers_v3_2_beta
)
from .v3_2_beta.tacacs_profile import (
    TacacsProfile as TacacsProfile_v3_2_beta
)
from .v3_2_beta.tacacs_server_sequence import (
    TacacsServerSequence as TacacsServerSequence_v3_2_beta
)
from .v3_2_beta.telemetry_information import (
    TelemetryInformation as TelemetryInformation_v3_2_beta
)
from .v3_2_beta.trust_sec_configuration import (
    TrustSecConfiguration as TrustSecConfiguration_v3_2_beta
)
from .v3_2_beta.trust_sec_sxp import (
    TrustSecSxp as TrustSecSxp_v3_2_beta
)
from .v3_2_beta.version_and_patch import (
    VersionAndPatch as VersionAndPatch_v3_2_beta
)
from .v3_2_beta.version_info import (
    VersionInfo as VersionInfo_v3_2_beta
)
from .v3_2_beta.endpoint import (
    Endpoint as Endpoint_v3_2_beta
)
from .v3_2_beta.portal import (
    Portal as Portal_v3_2_beta
)
from .v3_2_beta.proxy import (
    Proxy as Proxy_v3_2_beta
)
from .v3_2_beta.px_grid_node import (
    PxGridNode as PxGridNode_v3_2_beta
)
from .v3_2_beta.tasks import (
    Tasks as Tasks_v3_2_beta
)
from .v3_2_beta.telemetry import (
    Telemetry as Telemetry_v3_2_beta
)
from .v3_3_patch_1.aci_bindings import (
    AciBindings as AciBindings_v3_3_patch_1
)
from .v3_3_patch_1.aci_settings import (
    AciSettings as AciSettings_v3_3_patch_1
)
from .v3_3_patch_1.ad_groups import (
    ADGroups as ADGroups_v3_3_patch_1
)
from .v3_3_patch_1.anc_endpoint import (
    AncEndpoint as AncEndpoint_v3_3_patch_1
)
from .v3_3_patch_1.active_directories import (
    ActiveDirectories as ActiveDirectories_v3_3_patch_1
)
from .v3_3_patch_1.active_directory import (
    ActiveDirectory as ActiveDirectory_v3_3_patch_1
)
from .v3_3_patch_1.admin_user import (
    AdminUser as AdminUser_v3_3_patch_1
)
from .v3_3_patch_1.allowed_protocols import (
    AllowedProtocols as AllowedProtocols_v3_3_patch_1
)
from .v3_3_patch_1.anc_policy import (
    AncPolicy as AncPolicy_v3_3_patch_1
)
from .v3_3_patch_1.authorization_profile import (
    AuthorizationProfile as AuthorizationProfile_v3_3_patch_1
)
from .v3_3_patch_1.byod_portal import (
    ByodPortal as ByodPortal_v3_3_patch_1
)
from .v3_3_patch_1.backup_and_restore import (
    BackupAndRestore as BackupAndRestore_v3_3_patch_1
)
from .v3_3_patch_1.certificate_profile import (
    CertificateProfile as CertificateProfile_v3_3_patch_1
)
from .v3_3_patch_1.certificate_template import (
    CertificateTemplate as CertificateTemplate_v3_3_patch_1
)
from .v3_3_patch_1.certificates import (
    Certificates as Certificates_v3_3_patch_1
)
from .v3_3_patch_1.clear_threats_and_vulnerabilities import (
    ClearThreatsAndVulnerabilities as ClearThreatsAndVulnerabilities_v3_3_patch_1
)
from .v3_3_patch_1.configuration import (
    Configuration as Configuration_v3_3_patch_1
)
from .v3_3_patch_1.consumer import (
    Consumer as Consumer_v3_3_patch_1
)
from .v3_3_patch_1.dataconnect_services import (
    DataconnectServices as DataconnectServices_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_authentication_rules import (
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_authorization_exception_rules import (
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_authorization_global_exception_rules import (
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_authorization_rules import (
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_command_set import (
    DeviceAdministrationCommandSet as DeviceAdministrationCommandSet_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_conditions import (
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_dictionary_attributes_list import (
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_identity_stores import (
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_network_conditions import (
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_policy_set import (
    DeviceAdministrationPolicySet as DeviceAdministrationPolicySet_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_profiles import (
    DeviceAdministrationProfiles as DeviceAdministrationProfiles_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_service_names import (
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_3_patch_1
)
from .v3_3_patch_1.device_administration_time_date_conditions import (
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_3_patch_1
)
from .v3_3_patch_1.downloadable_acl import (
    DownloadableAcl as DownloadableAcl_v3_3_patch_1
)
from .v3_3_patch_1.duo_identity_sync import (
    DuoIdentitySync as DuoIdentitySync_v3_3_patch_1
)
from .v3_3_patch_1.duo_mfa import (
    DuoMfa as DuoMfa_v3_3_patch_1
)
from .v3_3_patch_1.egress_matrix_cell import (
    EgressMatrixCell as EgressMatrixCell_v3_3_patch_1
)
from .v3_3_patch_1.endpoint_stop_replication_service import (
    EndpointStopReplicationService as EndpointStopReplicationService_v3_3_patch_1
)
from .v3_3_patch_1.endpoint_certificate import (
    EndpointCertificate as EndpointCertificate_v3_3_patch_1
)
from .v3_3_patch_1.endpoint_identity_group import (
    EndpointIdentityGroup as EndpointIdentityGroup_v3_3_patch_1
)
from .v3_3_patch_1.external_radius_server import (
    ExternalRadiusServer as ExternalRadiusServer_v3_3_patch_1
)
from .v3_3_patch_1.filter_policy import (
    FilterPolicy as FilterPolicy_v3_3_patch_1
)
from .v3_3_patch_1.guest_location import (
    GuestLocation as GuestLocation_v3_3_patch_1
)
from .v3_3_patch_1.guest_smtp_notification_configuration import (
    GuestSmtpNotificationConfiguration as GuestSmtpNotificationConfiguration_v3_3_patch_1
)
from .v3_3_patch_1.guest_ssid import (
    GuestSsid as GuestSsid_v3_3_patch_1
)
from .v3_3_patch_1.guest_type import (
    GuestType as GuestType_v3_3_patch_1
)
from .v3_3_patch_1.guest_user import (
    GuestUser as GuestUser_v3_3_patch_1
)
from .v3_3_patch_1.hotspot_portal import (
    HotspotPortal as HotspotPortal_v3_3_patch_1
)
from .v3_3_patch_1.ip_to_sgt_mapping import (
    IpToSgtMapping as IpToSgtMapping_v3_3_patch_1
)
from .v3_3_patch_1.ip_to_sgt_mapping_group import (
    IpToSgtMappingGroup as IpToSgtMappingGroup_v3_3_patch_1
)
from .v3_3_patch_1.identity_groups import (
    IdentityGroups as IdentityGroups_v3_3_patch_1
)
from .v3_3_patch_1.identity_sequence import (
    IdentitySequence as IdentitySequence_v3_3_patch_1
)
from .v3_3_patch_1.internal_user import (
    InternalUser as InternalUser_v3_3_patch_1
)
from .v3_3_patch_1.licensing import (
    Licensing as Licensing_v3_3_patch_1
)
from .v3_3_patch_1.mdm import (
    Mdm as Mdm_v3_3_patch_1
)
from .v3_3_patch_1.misc import (
    Misc as Misc_v3_3_patch_1
)
from .v3_3_patch_1.my_device_portal import (
    MyDevicePortal as MyDevicePortal_v3_3_patch_1
)
from .v3_3_patch_1.native_ipsec import (
    NativeIpsec as NativeIpsec_v3_3_patch_1
)
from .v3_3_patch_1.native_supplicant_profile import (
    NativeSupplicantProfile as NativeSupplicantProfile_v3_3_patch_1
)
from .v3_3_patch_1.network_access_authentication_rules import (
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_3_patch_1
)
from .v3_3_patch_1.network_access_authorization_exception_rules import (
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_3_patch_1
)
from .v3_3_patch_1.network_access_authorization_global_exception_rules import (
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_3_patch_1
)
from .v3_3_patch_1.network_access_authorization_rules import (
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_3_patch_1
)
from .v3_3_patch_1.network_access_conditions import (
    NetworkAccessConditions as NetworkAccessConditions_v3_3_patch_1
)
from .v3_3_patch_1.network_access_dictionary import (
    NetworkAccessDictionary as NetworkAccessDictionary_v3_3_patch_1
)
from .v3_3_patch_1.network_access_dictionary_attribute import (
    NetworkAccessDictionaryAttribute as NetworkAccessDictionaryAttribute_v3_3_patch_1
)
from .v3_3_patch_1.network_access_dictionary_attributes_list import (
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_3_patch_1
)
from .v3_3_patch_1.network_access_identity_stores import (
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_3_patch_1
)
from .v3_3_patch_1.network_access_network_conditions import (
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_3_patch_1
)
from .v3_3_patch_1.network_access_policy_set import (
    NetworkAccessPolicySet as NetworkAccessPolicySet_v3_3_patch_1
)
from .v3_3_patch_1.network_access_profiles import (
    NetworkAccessProfiles as NetworkAccessProfiles_v3_3_patch_1
)
from .v3_3_patch_1.network_access_security_groups import (
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_3_patch_1
)
from .v3_3_patch_1.network_access_service_names import (
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_3_patch_1
)
from .v3_3_patch_1.network_access_time_date_conditions import (
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_3_patch_1
)
from .v3_3_patch_1.network_device import (
    NetworkDevice as NetworkDevice_v3_3_patch_1
)
from .v3_3_patch_1.network_device_group import (
    NetworkDeviceGroup as NetworkDeviceGroup_v3_3_patch_1
)
from .v3_3_patch_1.node_deployment import (
    NodeDeployment as NodeDeployment_v3_3_patch_1
)
from .v3_3_patch_1.node_group import (
    NodeGroup as NodeGroup_v3_3_patch_1
)
from .v3_3_patch_1.node_services import (
    NodeServices as NodeServices_v3_3_patch_1
)
from .v3_3_patch_1.node_details import (
    NodeDetails as NodeDetails_v3_3_patch_1
)
from .v3_3_patch_1.pan_ha import (
    PanHa as PanHa_v3_3_patch_1
)
from .v3_3_patch_1.patching import (
    Patching as Patching_v3_3_patch_1
)
from .v3_3_patch_1.portal_global_setting import (
    PortalGlobalSetting as PortalGlobalSetting_v3_3_patch_1
)
from .v3_3_patch_1.portal_theme import (
    PortalTheme as PortalTheme_v3_3_patch_1
)
from .v3_3_patch_1.profiler import (
    Profiler as Profiler_v3_3_patch_1
)
from .v3_3_patch_1.profiler_profile import (
    ProfilerProfile as ProfilerProfile_v3_3_patch_1
)
from .v3_3_patch_1.provider import (
    Provider as Provider_v3_3_patch_1
)
from .v3_3_patch_1.psn_node_details_with_radius_service import (
    PsnNodeDetailsWithRadiusService as PsnNodeDetailsWithRadiusService_v3_3_patch_1
)
from .v3_3_patch_1.pull_deployment_info import (
    PullDeploymentInfo as PullDeploymentInfo_v3_3_patch_1
)
from .v3_3_patch_1.px_grid_settings import (
    PxGridSettings as PxGridSettings_v3_3_patch_1
)
from .v3_3_patch_1.radius_failure import (
    RadiusFailure as RadiusFailure_v3_3_patch_1
)
from .v3_3_patch_1.radius_server_sequence import (
    RadiusServerSequence as RadiusServerSequence_v3_3_patch_1
)
from .v3_3_patch_1.restid_store import (
    RestidStore as RestidStore_v3_3_patch_1
)
from .v3_3_patch_1.repository import (
    Repository as Repository_v3_3_patch_1
)
from .v3_3_patch_1.sms_provider import (
    SmsProvider as SmsProvider_v3_3_patch_1
)
from .v3_3_patch_1.sxp_connections import (
    SxpConnections as SxpConnections_v3_3_patch_1
)
from .v3_3_patch_1.sxp_local_bindings import (
    SxpLocalBindings as SxpLocalBindings_v3_3_patch_1
)
from .v3_3_patch_1.sxp_vpns import (
    SxpVpns as SxpVpns_v3_3_patch_1
)
from .v3_3_patch_1.security_group_to_virtual_network import (
    SecurityGroupToVirtualNetwork as SecurityGroupToVirtualNetwork_v3_3_patch_1
)
from .v3_3_patch_1.security_groups import (
    SecurityGroups as SecurityGroups_v3_3_patch_1
)
from .v3_3_patch_1.security_groups_acls import (
    SecurityGroupsAcls as SecurityGroupsAcls_v3_3_patch_1
)
from .v3_3_patch_1.self_registered_portal import (
    SelfRegisteredPortal as SelfRegisteredPortal_v3_3_patch_1
)
from .v3_3_patch_1.session_directory import (
    SessionDirectory as SessionDirectory_v3_3_patch_1
)
from .v3_3_patch_1.sgt_range_reservation import (
    SgtRangeReservation as SgtRangeReservation_v3_3_patch_1
)
from .v3_3_patch_1.sponsor_group import (
    SponsorGroup as SponsorGroup_v3_3_patch_1
)
from .v3_3_patch_1.sponsor_group_member import (
    SponsorGroupMember as SponsorGroupMember_v3_3_patch_1
)
from .v3_3_patch_1.sponsor_portal import (
    SponsorPortal as SponsorPortal_v3_3_patch_1
)
from .v3_3_patch_1.sponsored_guest_portal import (
    SponsoredGuestPortal as SponsoredGuestPortal_v3_3_patch_1
)
from .v3_3_patch_1.subscriber import (
    Subscriber as Subscriber_v3_3_patch_1
)
from .v3_3_patch_1.support_bundle_download import (
    SupportBundleDownload as SupportBundleDownload_v3_3_patch_1
)
from .v3_3_patch_1.support_bundle_status import (
    SupportBundleStatus as SupportBundleStatus_v3_3_patch_1
)
from .v3_3_patch_1.support_bundle_trigger_configuration import (
    SupportBundleTriggerConfiguration as SupportBundleTriggerConfiguration_v3_3_patch_1
)
from .v3_3_patch_1.system_health import (
    SystemHealth as SystemHealth_v3_3_patch_1
)
from .v3_3_patch_1.system_certificate import (
    SystemCertificate as SystemCertificate_v3_3_patch_1
)
from .v3_3_patch_1.tacacs_command_sets import (
    TacacsCommandSets as TacacsCommandSets_v3_3_patch_1
)
from .v3_3_patch_1.tacacs_external_servers import (
    TacacsExternalServers as TacacsExternalServers_v3_3_patch_1
)
from .v3_3_patch_1.tacacs_profile import (
    TacacsProfile as TacacsProfile_v3_3_patch_1
)
from .v3_3_patch_1.tacacs_server_sequence import (
    TacacsServerSequence as TacacsServerSequence_v3_3_patch_1
)
from .v3_3_patch_1.telemetry_information import (
    TelemetryInformation as TelemetryInformation_v3_3_patch_1
)
from .v3_3_patch_1.trust_sec_configuration import (
    TrustSecConfiguration as TrustSecConfiguration_v3_3_patch_1
)
from .v3_3_patch_1.trust_sec_sxp import (
    TrustSecSxp as TrustSecSxp_v3_3_patch_1
)
from .v3_3_patch_1.user_equipment import (
    UserEquipment as UserEquipment_v3_3_patch_1
)
from .v3_3_patch_1.version_and_patch import (
    VersionAndPatch as VersionAndPatch_v3_3_patch_1
)
from .v3_3_patch_1.version_info import (
    VersionInfo as VersionInfo_v3_3_patch_1
)
from .v3_3_patch_1.custom_attributes import (
    CustomAttributes as CustomAttributes_v3_3_patch_1
)
from .v3_3_patch_1.enable_mfa import (
    EnableMFA as EnableMFA_v3_3_patch_1
)
from .v3_3_patch_1.endpoint import (
    Endpoint as Endpoint_v3_3_patch_1
)
from .v3_3_patch_1.endpoints import (
    Endpoints as Endpoints_v3_3_patch_1
)
from .v3_3_patch_1.full_upgrade import (
    FullUpgrade as FullUpgrade_v3_3_patch_1
)
from .v3_3_patch_1.is_mfa_enabled import (
    IsMFAEnabled as IsMFAEnabled_v3_3_patch_1
)
from .v3_3_patch_1.nbar_app import (
    NbarApp as NbarApp_v3_3_patch_1
)
from .v3_3_patch_1.portal import (
    Portal as Portal_v3_3_patch_1
)
from .v3_3_patch_1.proxy import (
    Proxy as Proxy_v3_3_patch_1
)
from .v3_3_patch_1.px_grid_direct import (
    PxGridDirect as PxGridDirect_v3_3_patch_1
)
from .v3_3_patch_1.px_grid_node import (
    PxGridNode as PxGridNode_v3_3_patch_1
)
from .v3_3_patch_1.sg_vn_mapping import (
    SgVnMapping as SgVnMapping_v3_3_patch_1
)
from .v3_3_patch_1.tasks import (
    Tasks as Tasks_v3_3_patch_1
)
from .v3_3_patch_1.telemetry import (
    Telemetry as Telemetry_v3_3_patch_1
)
from .v3_3_patch_1.virtual_network import (
    VirtualNetwork as VirtualNetwork_v3_3_patch_1
)
from .v3_3_patch_1.vn_vlan_mapping import (
    VnVlanMapping as VnVlanMapping_v3_3_patch_1
)

from .v3_5_0.aci_connection import (
    AciConnection as AciConnection_v3_5_0
)
from .v3_5_0.aci_data import (
    AciData as AciData_v3_5_0
)
from .v3_5_0.a_d_groups import (
    ADGroups as ADGroups_v3_5_0
)
from .v3_5_0.active_directories import (
    ActiveDirectories as ActiveDirectories_v3_5_0
)
from .v3_5_0.admin_groups import (
    AdminGroups as AdminGroups_v3_5_0
)
from .v3_5_0.admin_users import (
    AdminUsers as AdminUsers_v3_5_0
)
from .v3_5_0.backup_and_restore import (
    BackupAndRestore as BackupAndRestore_v3_5_0
)
from .v3_5_0.certificates import (
    Certificates as Certificates_v3_5_0
)
from .v3_5_0.classificationrule import (
    Classificationrule as Classificationrule_v3_5_0
)
from .v3_5_0.configuration import (
    Configuration as Configuration_v3_5_0
)
from .v3_5_0.data_access import (
    DataAccess as DataAccess_v3_5_0
)
from .v3_5_0.dataconnect_services import (
    DataconnectServices as DataconnectServices_v3_5_0
)
from .v3_5_0.device_admin_m_f_a_rules import (
    DeviceAdminMFARules as DeviceAdminMFARules_v3_5_0
)
from .v3_5_0.device_administration_authentication_rules import (
    DeviceAdministrationAuthenticationRules as DeviceAdministrationAuthenticationRules_v3_5_0
)
from .v3_5_0.device_administration_authorization_exception_rules import (
    DeviceAdministrationAuthorizationExceptionRules as DeviceAdministrationAuthorizationExceptionRules_v3_5_0
)
from .v3_5_0.device_administration_authorization_global_exception_rules import (
    DeviceAdministrationAuthorizationGlobalExceptionRules as DeviceAdministrationAuthorizationGlobalExceptionRules_v3_5_0
)
from .v3_5_0.device_administration_authorization_rules import (
    DeviceAdministrationAuthorizationRules as DeviceAdministrationAuthorizationRules_v3_5_0
)
from .v3_5_0.device_administration_command_sets import (
    DeviceAdministrationCommandSets as DeviceAdministrationCommandSets_v3_5_0
)
from .v3_5_0.device_administration_conditions import (
    DeviceAdministrationConditions as DeviceAdministrationConditions_v3_5_0
)
from .v3_5_0.device_administration_dictionary_attributes_list import (
    DeviceAdministrationDictionaryAttributesList as DeviceAdministrationDictionaryAttributesList_v3_5_0
)
from .v3_5_0.device_administration_identity_stores import (
    DeviceAdministrationIdentityStores as DeviceAdministrationIdentityStores_v3_5_0
)
from .v3_5_0.device_administration_network_conditions import (
    DeviceAdministrationNetworkConditions as DeviceAdministrationNetworkConditions_v3_5_0
)
from .v3_5_0.device_administration_policy_sets import (
    DeviceAdministrationPolicySets as DeviceAdministrationPolicySets_v3_5_0
)
from .v3_5_0.device_administration_service_names import (
    DeviceAdministrationServiceNames as DeviceAdministrationServiceNames_v3_5_0
)
from .v3_5_0.device_administration_shell_profiles import (
    DeviceAdministrationShellProfiles as DeviceAdministrationShellProfiles_v3_5_0
)
from .v3_5_0.device_administration_time_date_conditions import (
    DeviceAdministrationTimeDateConditions as DeviceAdministrationTimeDateConditions_v3_5_0
)
from .v3_5_0.duo_identity_sync import (
    DuoIdentitySync as DuoIdentitySync_v3_5_0
)
from .v3_5_0.duo_mfa import (
    DuoMfa as DuoMfa_v3_5_0
)
from .v3_5_0.endpoint_stop_replication_service import (
    EndpointStopReplicationService as EndpointStopReplicationService_v3_5_0
)
from .v3_5_0.inbound_rule import (
    InboundRule as InboundRule_v3_5_0
)
from .v3_5_0.licensing import (
    Licensing as Licensing_v3_5_0
)
from .v3_5_0.menu_access import (
    MenuAccess as MenuAccess_v3_5_0
)
from .v3_5_0.misc import (
    Misc as Misc_v3_5_0
)
from .v3_5_0.n_b_a_r_application_management import (
    NBARApplicationManagement as NBARApplicationManagement_v3_5_0
)
from .v3_5_0.native_ipsec import (
    NativeIpsec as NativeIpsec_v3_5_0
)
from .v3_5_0.network_access_authentication_rules import (
    NetworkAccessAuthenticationRules as NetworkAccessAuthenticationRules_v3_5_0
)
from .v3_5_0.network_access_authorization_exception_rules import (
    NetworkAccessAuthorizationExceptionRules as NetworkAccessAuthorizationExceptionRules_v3_5_0
)
from .v3_5_0.network_access_authorization_global_exception_rules import (
    NetworkAccessAuthorizationGlobalExceptionRules as NetworkAccessAuthorizationGlobalExceptionRules_v3_5_0
)
from .v3_5_0.network_access_authorization_profiles import (
    NetworkAccessAuthorizationProfiles as NetworkAccessAuthorizationProfiles_v3_5_0
)
from .v3_5_0.network_access_authorization_rules import (
    NetworkAccessAuthorizationRules as NetworkAccessAuthorizationRules_v3_5_0
)
from .v3_5_0.network_access_conditions import (
    NetworkAccessConditions as NetworkAccessConditions_v3_5_0
)
from .v3_5_0.network_access_dictionaries import (
    NetworkAccessDictionaries as NetworkAccessDictionaries_v3_5_0
)
from .v3_5_0.network_access_dictionary_attributes import (
    NetworkAccessDictionaryAttributes as NetworkAccessDictionaryAttributes_v3_5_0
)
from .v3_5_0.network_access_dictionary_attributes_list import (
    NetworkAccessDictionaryAttributesList as NetworkAccessDictionaryAttributesList_v3_5_0
)
from .v3_5_0.network_access_identity_stores import (
    NetworkAccessIdentityStores as NetworkAccessIdentityStores_v3_5_0
)
from .v3_5_0.network_access_m_f_a_rules import (
    NetworkAccessMFARules as NetworkAccessMFARules_v3_5_0
)
from .v3_5_0.network_access_network_conditions import (
    NetworkAccessNetworkConditions as NetworkAccessNetworkConditions_v3_5_0
)
from .v3_5_0.network_access_policy_sets import (
    NetworkAccessPolicySets as NetworkAccessPolicySets_v3_5_0
)
from .v3_5_0.network_access_security_groups import (
    NetworkAccessSecurityGroups as NetworkAccessSecurityGroups_v3_5_0
)
from .v3_5_0.network_access_service_names import (
    NetworkAccessServiceNames as NetworkAccessServiceNames_v3_5_0
)
from .v3_5_0.network_access_time_date_conditions import (
    NetworkAccessTimeDateConditions as NetworkAccessTimeDateConditions_v3_5_0
)
from .v3_5_0.node_deployment import (
    NodeDeployment as NodeDeployment_v3_5_0
)
from .v3_5_0.node_group import (
    NodeGroup as NodeGroup_v3_5_0
)
from .v3_5_0.nodeservices import (
    Nodeservices as Nodeservices_v3_5_0
)
from .v3_5_0.outbound_rule import (
    OutboundRule as OutboundRule_v3_5_0
)
from .v3_5_0.pan_ha import (
    PanHa as PanHa_v3_5_0
)
from .v3_5_0.patch import (
    Patch as Patch_v3_5_0
)
from .v3_5_0.patching import (
    Patching as Patching_v3_5_0
)
from .v3_5_0.prometheus_alertmanager import (
    PrometheusAlertmanager as PrometheusAlertmanager_v3_5_0
)
from .v3_5_0.r_b_a_c_policy import (
    RBACPolicy as RBACPolicy_v3_5_0
)
from .v3_5_0.repository import (
    Repository as Repository_v3_5_0
)
from .v3_5_0.sxp import (
    Sxp as Sxp_v3_5_0
)
from .v3_5_0.sxp_domainswithmappinganddevicescounts import (
    SxpDomainswithmappinganddevicescounts as SxpDomainswithmappinganddevicescounts_v3_5_0
)
from .v3_5_0.security_group_management import (
    SecurityGroupManagement as SecurityGroupManagement_v3_5_0
)
from .v3_5_0.sgt import (
    Sgt as Sgt_v3_5_0
)
from .v3_5_0.sgt_range_reservation import (
    SgtRangeReservation as SgtRangeReservation_v3_5_0
)
from .v3_5_0.subscriber import (
    Subscriber as Subscriber_v3_5_0
)
from .v3_5_0.trust_sec_open_api_view import (
    TrustSecOpenApiView as TrustSecOpenApiView_v3_5_0
)
from .v3_5_0.trustsec_c_o_a_push import (
    TrustsecCOAPush as TrustsecCOAPush_v3_5_0
)
from .v3_5_0.trustsec_http_s_server import (
    TrustsecHttpSServer as TrustsecHttpSServer_v3_5_0
)
from .v3_5_0.trustsec_integration_rule_default_trustsec_integration_ruleset import (
    TrustsecIntegrationRuleDefaultTrustsecIntegrationRuleset as TrustsecIntegrationRuleDefaultTrustsecIntegrationRuleset_v3_5_0
)
from .v3_5_0.trustsec_integration_rule_dictionaries import (
    TrustsecIntegrationRuleDictionaries as TrustsecIntegrationRuleDictionaries_v3_5_0
)
from .v3_5_0.trustsec_integration_rule_dictionary_attributes import (
    TrustsecIntegrationRuleDictionaryAttributes as TrustsecIntegrationRuleDictionaryAttributes_v3_5_0
)
from .v3_5_0.trustsec_settings import (
    TrustsecSettings as TrustsecSettings_v3_5_0
)
from .v3_5_0.trustsecdevicesreport import (
    Trustsecdevicesreport as Trustsecdevicesreport_v3_5_0
)
from .v3_5_0.upgrade import (
    Upgrade as Upgrade_v3_5_0
)
from .v3_5_0.user_equipment import (
    UserEquipment as UserEquipment_v3_5_0
)
from .v3_5_0.virtual_network_management import (
    VirtualNetworkManagement as VirtualNetworkManagement_v3_5_0
)
from .v3_5_0.acibindings import (
    Acibindings as Acibindings_v3_5_0
)
from .v3_5_0.acisettings import (
    Acisettings as Acisettings_v3_5_0
)
from .v3_5_0.activedirectory import (
    Activedirectory as Activedirectory_v3_5_0
)
from .v3_5_0.adminuser import (
    Adminuser as Adminuser_v3_5_0
)
from .v3_5_0.adresourcereservation import (
    Adresourcereservation as Adresourcereservation_v3_5_0
)
from .v3_5_0.allowedprotocols import (
    Allowedprotocols as Allowedprotocols_v3_5_0
)
from .v3_5_0.ancendpoint import (
    Ancendpoint as Ancendpoint_v3_5_0
)
from .v3_5_0.ancpolicy import (
    Ancpolicy as Ancpolicy_v3_5_0
)
from .v3_5_0.authorizationprofile import (
    Authorizationprofile as Authorizationprofile_v3_5_0
)
from .v3_5_0.byodportal import (
    Byodportal as Byodportal_v3_5_0
)
from .v3_5_0.certificateprofile import (
    Certificateprofile as Certificateprofile_v3_5_0
)
from .v3_5_0.certificatetemplate import (
    Certificatetemplate as Certificatetemplate_v3_5_0
)
from .v3_5_0.ctsenvdata import (
    Ctsenvdata as Ctsenvdata_v3_5_0
)
from .v3_5_0.ctsmatrix import (
    Ctsmatrix as Ctsmatrix_v3_5_0
)
from .v3_5_0.customattributes import (
    Customattributes as Customattributes_v3_5_0
)
from .v3_5_0.deploymentinfo import (
    Deploymentinfo as Deploymentinfo_v3_5_0
)
from .v3_5_0.downloadableacl import (
    Downloadableacl as Downloadableacl_v3_5_0
)
from .v3_5_0.egressmatrixcell import (
    Egressmatrixcell as Egressmatrixcell_v3_5_0
)
from .v3_5_0.enable_m_f_a import (
    EnableMFA as EnableMFA_v3_5_0
)
from .v3_5_0.endpoint import (
    Endpoint as Endpoint_v3_5_0
)
from .v3_5_0.endpointcert import (
    Endpointcert as Endpointcert_v3_5_0
)
from .v3_5_0.endpointgroup import (
    Endpointgroup as Endpointgroup_v3_5_0
)
from .v3_5_0.endpoints import (
    Endpoints as Endpoints_v3_5_0
)
from .v3_5_0.externalradiusserver import (
    Externalradiusserver as Externalradiusserver_v3_5_0
)
from .v3_5_0.filterpolicy import (
    Filterpolicy as Filterpolicy_v3_5_0
)
from .v3_5_0.guestlocation import (
    Guestlocation as Guestlocation_v3_5_0
)
from .v3_5_0.guestsmtpnotificationsettings import (
    Guestsmtpnotificationsettings as Guestsmtpnotificationsettings_v3_5_0
)
from .v3_5_0.guestssid import (
    Guestssid as Guestssid_v3_5_0
)
from .v3_5_0.guesttype import (
    Guesttype as Guesttype_v3_5_0
)
from .v3_5_0.guestuser import (
    Guestuser as Guestuser_v3_5_0
)
from .v3_5_0.hotspotportal import (
    Hotspotportal as Hotspotportal_v3_5_0
)
from .v3_5_0.identitygroup import (
    Identitygroup as Identitygroup_v3_5_0
)
from .v3_5_0.idstoresequence import (
    Idstoresequence as Idstoresequence_v3_5_0
)
from .v3_5_0.internaluser import (
    Internaluser as Internaluser_v3_5_0
)
from .v3_5_0.is_m_f_a_enabled import (
    IsMFAEnabled as IsMFAEnabled_v3_5_0
)
from .v3_5_0.ldap import (
    Ldap as Ldap_v3_5_0
)
from .v3_5_0.mydeviceportal import (
    Mydeviceportal as Mydeviceportal_v3_5_0
)
from .v3_5_0.networkdevice import (
    Networkdevice as Networkdevice_v3_5_0
)
from .v3_5_0.networkdevicegroup import (
    Networkdevicegroup as Networkdevicegroup_v3_5_0
)
from .v3_5_0.node import (
    Node as Node_v3_5_0
)
from .v3_5_0.nspprofile import (
    Nspprofile as Nspprofile_v3_5_0
)
from .v3_5_0.portal import (
    Portal as Portal_v3_5_0
)
from .v3_5_0.portalglobalsetting import (
    Portalglobalsetting as Portalglobalsetting_v3_5_0
)
from .v3_5_0.portaltheme import (
    Portaltheme as Portaltheme_v3_5_0
)
from .v3_5_0.profilerprofile import (
    Profilerprofile as Profilerprofile_v3_5_0
)
from .v3_5_0.proxy import (
    Proxy as Proxy_v3_5_0
)
from .v3_5_0.px_grid_cloud import (
    PxGridCloud as PxGridCloud_v3_5_0
)
from .v3_5_0.px_grid_direct import (
    PxGridDirect as PxGridDirect_v3_5_0
)
from .v3_5_0.px_grid_direct_push_apis import (
    PxGridDirectPushApis as PxGridDirectPushApis_v3_5_0
)
from .v3_5_0.pxgridnode import (
    Pxgridnode as Pxgridnode_v3_5_0
)
from .v3_5_0.pxgridsettings import (
    Pxgridsettings as Pxgridsettings_v3_5_0
)
from .v3_5_0.radiusserversequence import (
    Radiusserversequence as Radiusserversequence_v3_5_0
)
from .v3_5_0.reportconfig import (
    Reportconfig as Reportconfig_v3_5_0
)
from .v3_5_0.restidstore import (
    Restidstore as Restidstore_v3_5_0
)
from .v3_5_0.restidstoreattribute import (
    Restidstoreattribute as Restidstoreattribute_v3_5_0
)
from .v3_5_0.restidstoredeviceattribute import (
    Restidstoredeviceattribute as Restidstoredeviceattribute_v3_5_0
)
from .v3_5_0.restidstorepredefinedregex import (
    Restidstorepredefinedregex as Restidstorepredefinedregex_v3_5_0
)
from .v3_5_0.restidstoresettings import (
    Restidstoresettings as Restidstoresettings_v3_5_0
)
from .v3_5_0.selfregportal import (
    Selfregportal as Selfregportal_v3_5_0
)
from .v3_5_0.service import (
    Service as Service_v3_5_0
)
from .v3_5_0.sessionservicenode import (
    Sessionservicenode as Sessionservicenode_v3_5_0
)
from .v3_5_0.sgacl import (
    Sgacl as Sgacl_v3_5_0
)
from .v3_5_0.sgacls import (
    Sgacls as Sgacls_v3_5_0
)
from .v3_5_0.sgmapping import (
    Sgmapping as Sgmapping_v3_5_0
)
from .v3_5_0.sgmappinggroup import (
    Sgmappinggroup as Sgmappinggroup_v3_5_0
)
from .v3_5_0.sgt import (
    Sgt as Sgt_v3_5_0
)
from .v3_5_0.sgtvnvlan import (
    Sgtvnvlan as Sgtvnvlan_v3_5_0
)
from .v3_5_0.smsprovider import (
    Smsprovider as Smsprovider_v3_5_0
)
from .v3_5_0.sponsoredguestportal import (
    Sponsoredguestportal as Sponsoredguestportal_v3_5_0
)
from .v3_5_0.sponsorgroup import (
    Sponsorgroup as Sponsorgroup_v3_5_0
)
from .v3_5_0.sponsorgroupmember import (
    Sponsorgroupmember as Sponsorgroupmember_v3_5_0
)
from .v3_5_0.sponsorportal import (
    Sponsorportal as Sponsorportal_v3_5_0
)
from .v3_5_0.supportbundle import (
    Supportbundle as Supportbundle_v3_5_0
)
from .v3_5_0.supportbundledownload import (
    Supportbundledownload as Supportbundledownload_v3_5_0
)
from .v3_5_0.supportbundlestatus import (
    Supportbundlestatus as Supportbundlestatus_v3_5_0
)
from .v3_5_0.sxpconnections import (
    Sxpconnections as Sxpconnections_v3_5_0
)
from .v3_5_0.sxplocalbindings import (
    Sxplocalbindings as Sxplocalbindings_v3_5_0
)
from .v3_5_0.sxpvpns import (
    Sxpvpns as Sxpvpns_v3_5_0
)
from .v3_5_0.systemcertificate import (
    Systemcertificate as Systemcertificate_v3_5_0
)
from .v3_5_0.tacacscommandsets import (
    Tacacscommandsets as Tacacscommandsets_v3_5_0
)
from .v3_5_0.tacacsexternalservers import (
    Tacacsexternalservers as Tacacsexternalservers_v3_5_0
)
from .v3_5_0.tacacsprofile import (
    Tacacsprofile as Tacacsprofile_v3_5_0
)
from .v3_5_0.tacacsserversequence import (
    Tacacsserversequence as Tacacsserversequence_v3_5_0
)
from .v3_5_0.tasks import (
    Tasks as Tasks_v3_5_0
)
from .v3_5_0.telemetry import (
    Telemetry as Telemetry_v3_5_0
)
from .v3_5_0.telemetryinfo import (
    Telemetryinfo as Telemetryinfo_v3_5_0
)
from .v3_5_0.threat import (
    Threat as Threat_v3_5_0
)

class IdentityServicesEngineAPI(object):
    """Identity Services Engine API wrapper.

    Creates a 'session' for all API calls through a created IdentityServicesEngineAPI
    object.  The 'session' handles authentication, provides the needed headers,
    and checks all responses for error conditions.

    IdentityServicesEngineAPI wraps all of the individual Identity Services Engine APIs and represents
    them in a simple hierarchical structure.
    """

    def __init__(self, username=None,
                 password=None,
                 encoded_auth=None,
                 uses_api_gateway=None,
                 base_url=None,
                 ui_base_url=None,
                 ers_base_url=None,
                 mnt_base_url=None,
                 px_grid_base_url=None,
                 single_request_timeout=None,
                 wait_on_rate_limit=None,
                 verify=None,
                 version=None,
                 debug=None,
                 uses_csrf_token=None,
                 object_factory=mydict_data_factory,
                 validator=SchemaValidator,
                 perform_initialize=True):
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
            uses_api_gateway(bool,str): Controls whether we use the ISE's API
                Gateway to make the request. Defaults to the
                IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY
                (or IDENTITY_SERVICES_ENGINE_USES_API_GATEWAY_STRING) environment variable or
                ciscoisesdk.config.DEFAULT_USES_API_GATEWAY if the environment
                variables are not set.
            base_url(str): The base URL to be prefixed to the
                individual API endpoint suffixes, used when uses_api_gateway is True.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable or
                ciscoisesdk.config.DEFAULT_BASE_URL
                if the environment variable is not set.
            ui_base_url(str): The UI base URL to be prefixed to the
                individual ISE UI API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            ers_base_url(str): The ERS base URL to be prefixed to the
                individual ISE ERS API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            mnt_base_url(str): The MNT base URL to be prefixed to the
                individual ISE MNT API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            px_grid_base_url(str): The PxGrid base URL to be prefixed to the
                individual ISE PxGrid API endpoint suffixes, used when uses_api_gateway is False.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            username(str): HTTP Basic Auth username.
            password(str): HTTP Basic Auth password.
            encoded_auth(str): HTTP Basic Auth base64 encoded string.
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
            verify(bool,str): Controls whether we verify the server's
                TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to the IDENTITY_SERVICES_ENGINE_VERIFY
                (or IDENTITY_SERVICES_ENGINE_VERIFY_STRING) environment variable or
                ciscoisesdk.config.DEFAULT_VERIFY if the environment
                variables are not set.
            version(str): Controls which version of IDENTITY_SERVICES_ENGINE to use.
                Defaults to the IDENTITY_SERVICES_ENGINE_VERSION environment variable or
                ciscoisesdk.config.DEFAULT_VERSION
                if the environment variable is not set.
            debug(bool,str): Controls whether to log information about
                Identity Services Engine APIs' request and response process.
                Defaults to the IDENTITY_SERVICES_ENGINE_DEBUG environment variable or False
                if the environment variable is not set.
            uses_csrf_token(bool,str): Controls whether we send the CSRF token to ISE's ERS APIs.
                Defaults to the
                IDENTITY_SERVICES_ENGINE_USES_CSRF_TOKEN environment variable or
                ciscoisesdk.config.DEFAULT_USES_CSRF_TOKEN if the environment
                variables are not set.
            object_factory(callable): The factory function to use to create
                Python objects from the returned Identity Services Engine JSON data objects.
            validator(callable): The factory class with function
                json_schema_validate(model:string) that returns an object with
                function validate(obj:dict) is used to validate Python objects
                sent in the request body.
            perform_initialize(bool): The flag that, if enabled, initializes now all
                the related objects to manage information from Identity Services Engine, like the
                authentication, the sessions (requests library), and the API wrappers (for each ISE API family).
                Defaults to True.
                You can initialize/reinitialize later with `reinitialize <#ciscoisesdk.IdentityServicesEngineAPI.reinitialize>`_.
                The original value will not change.

        Returns:
            IdentityServicesEngineAPI: A new IdentityServicesEngineAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.
            VersionError: If the version is not provided via the version
                argument or an environment variable, or it is not a
                Identity Services Engine API supported version
                ['3.1.0', '3.1.1', '3.1_Patch_1', '3.2_beta', '3.3_patch_1'].

        """
        check_type(perform_initialize, bool, may_be_none=True)
        self._perform_initialize = perform_initialize
        self._username = username or ciscoise_environment.get_env_username()
        self._password = password or ciscoise_environment.get_env_password()
        self._encoded_auth = encoded_auth or ciscoise_environment.get_env_encoded_auth()
        self._version = version or ciscoise_environment.get_env_version() or DEFAULT_VERSION
        self._base_url = base_url or ciscoise_environment.get_env_base_url() or DEFAULT_BASE_URL
        self._ui_base_url = ui_base_url or ciscoise_environment.get_env_ui_base_url()
        self._ers_base_url = ers_base_url or ciscoise_environment.get_env_ers_base_url()
        self._mnt_base_url = mnt_base_url or ciscoise_environment.get_env_mnt_base_url()
        self._px_grid_base_url = px_grid_base_url or ciscoise_environment.get_env_px_grid_base_url()
        self._uses_api_gateway = uses_api_gateway
        self._uses_csrf_token = uses_csrf_token
        self._single_request_timeout = single_request_timeout
        self._wait_on_rate_limit = wait_on_rate_limit
        self._verify = verify
        self._debug = debug

        if uses_api_gateway is None:
            self._uses_api_gateway = ciscoise_environment.get_env_uses_api_gateway()
            if self._uses_api_gateway is None:
                self._uses_api_gateway = DEFAULT_USES_API_GATEWAY

        if uses_csrf_token is None:
            self._uses_csrf_token = ciscoise_environment.get_env_uses_csrf_token()
            if self._uses_csrf_token is None:
                self._uses_csrf_token = DEFAULT_USES_CSRF_TOKEN

        if single_request_timeout is None:
            self._single_request_timeout = ciscoise_environment.get_env_single_request_timeout()
            if self._single_request_timeout is None:
                self._single_request_timeout = DEFAULT_SINGLE_REQUEST_TIMEOUT

        if wait_on_rate_limit is None:
            self._wait_on_rate_limit = ciscoise_environment.get_env_wait_on_rate_limit()
            if self._wait_on_rate_limit is None:
                self._wait_on_rate_limit = DEFAULT_WAIT_ON_RATE_LIMIT

        if verify is None:
            self._verify = ciscoise_environment.get_env_verify()
            if self._verify is None:
                self._verify = DEFAULT_VERIFY

        if debug is None:
            self._debug = ciscoise_environment.get_env_debug()
            if self._debug is None:
                self._debug = DEFAULT_DEBUG

        check_type(self._single_request_timeout, int)
        check_type(self._wait_on_rate_limit, bool)
        check_type(self._uses_api_gateway, (bool, str), may_be_none=False)
        check_type(self._uses_csrf_token, (bool, str), may_be_none=False)
        check_type(self._debug, (bool, str), may_be_none=True)
        check_type(self._username, str, may_be_none=True)
        check_type(self._password, str, may_be_none=True)
        check_type(self._encoded_auth, str, may_be_none=True)
        check_type(self._verify, (bool, str), may_be_none=False)
        check_type(self._version, str, may_be_none=False)

        if isinstance(self._uses_api_gateway, str):
            self._uses_api_gateway = 'true' in self._uses_api_gateway.lower()

        if isinstance(self._uses_csrf_token, str):
            self._uses_csrf_token = 'true' in self._uses_csrf_token.lower()

        if self._uses_api_gateway:
            check_type(self._base_url, str, may_be_none=False)
        else:
            check_type(self._ui_base_url, str, may_be_none=False)
            check_type(self._ers_base_url, str, may_be_none=False)
            check_type(self._mnt_base_url, str, may_be_none=False)
            check_type(self._px_grid_base_url, str, may_be_none=False)

        if self._version not in ['3.1.0', '3.1.1', '3.1_Patch_1', '3.2_beta', '3.3_patch_1', '3.5.0']:
            raise VersionError(
                'Unknown API version, '
                + 'known versions are {0}'.format(
                    '3.1.0, 3.1.1, 3.1_Patch_1, 3.2_beta, 3.3_patch_1, 3.5.0.'
                )
            )

        if self._version == '3.1.1':
            warnings.warn("The ISE version 3.1.1 will be removed in future versions and replaced by 3.1_Patch_1", FutureWarning)

        if isinstance(self._debug, str):
            self._debug = 'true' in self._debug.lower()

        # Check if the user has provided the required basicAuth parameters
        if self._encoded_auth is None and (self._username is None or self._password is None):
            raise AccessTokenError(
                "You need an access token to interact with the Identity Services Engine"
                " APIs. Identity Services Engine uses HTTP Basic Auth."
                " You must provide the username and password or just"
                " the encoded_auth, either by setting each parameter or its"
                " environment variable counterpart ("
                "IDENTITY_SERVICES_ENGINE_USERNAME, IDENTITY_SERVICES_ENGINE_PASSWORD,"
                " IDENTITY_SERVICES_ENGINE_ENCODED_AUTH)."
            )

        self._authentication = None
        self._validator = validator(self._version).json_schema_validate
        self._original_validator = validator
        self._object_factory = object_factory

        # Create the API session
        # All of the API calls associated with a IdentityServicesEngineAPI object will
        # leverage a single RESTful 'session' connecting to the Identity Services Engine
        # cloud.
        self._session_ui = None
        self._session_ers = None
        self._session = None
        self._session_mnt = None
        self._session_px_grid = None
        self._px_grid_direct = None

        if self._perform_initialize:
            self._initialize_authentication()
            self._initialize_sessions()
            self._initialize_api_wrappers()
        else:
            self._not_initialize_api_wrappers()

    def _initialize_authentication(self):
        """
        Function used when perform_initialize is True in class init.
        Init Authentication wrapper early to use for basicAuth requests.
        """
        # Init Authentication wrapper early to use for basicAuth requests
        self._authentication = Authentication(
            self._base_url or self._ers_base_url, self._object_factory,
            single_request_timeout=self._single_request_timeout,
            verify=self._verify,
        )

    def _get_access_token(self):
        """
        Function that attempts to access authentication.authentication_api
        to get the Identity Services Engine access token using the
        username, password, encoded_auth defined.
        """
        if hasattr(self, '_authentication'):
            if hasattr(self._authentication, 'authentication_api'):
                return self._authentication.authentication_api(
                    username=self._username,
                    password=self._password,
                    encoded_auth=self._encoded_auth).Token
        return None

    def _initialize_sessions(self):
        """
        Performs initialization of "session_ui", "session_ers", "session", "session_mnt", "session_px_grid" properties.
        Creating for each one a RestSession object that handles the requests.
        """
        if self._uses_api_gateway:
            self._session_ui = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._session_ers = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._session = self._session_ers
            self._session_mnt = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                headers={'Content-type': 'application/xml;charset=utf-8',
                         'Accept': 'application/xml'},
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._session_px_grid = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._px_grid_direct = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
        else:
            self._session_ui = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._ui_base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._session_ers = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._ers_base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._session = self._session_ers
            self._session_mnt = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._mnt_base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                headers={'Content-type': 'application/xml;charset=utf-8',
                         'Accept': 'application/xml'},
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._session_px_grid = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._px_grid_base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )
            self._px_grid_direct = RestSession(
                get_access_token=self._get_access_token,
                access_token=self._get_access_token(),
                base_url=self._base_url,
                single_request_timeout=self._single_request_timeout,
                wait_on_rate_limit=self._wait_on_rate_limit,
                verify=self._verify,
                version=self._version,
                debug=self._debug,
                uses_csrf_token=self._uses_csrf_token,
                get_csrf_token=self._get_csrf_token,
            )

        # Provide a common session alias used by newer API wrappers
        # Prefer UI session when available, otherwise fallback to ERS
        self._session_main = self._session_ui or self._session_ers

    def _initialize_api_wrappers(self):
        """Initializes the API wrappers according to the defined version."""
        # API wrappers
        if self._version == '3.1.0':
            self.aci_bindings = \
                AciBindings_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.aci_settings = \
                AciSettings_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_endpoint = \
                AncEndpoint_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.active_directory = \
                ActiveDirectory_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.admin_user = \
                AdminUser_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_policy = \
                AncPolicy_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.byod_portal = \
                ByodPortal_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.certificate_profile = \
                CertificateProfile_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificate_template = \
                CertificateTemplate_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificates = \
                Certificates_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.clear_threats_and_vulnerabilities = \
                ClearThreatsAndVulnerabilities_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.consumer = \
                Consumer_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_certificate = \
                EndpointCertificate_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_identity_group = \
                EndpointIdentityGroup_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.filter_policy = \
                FilterPolicy_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_location = \
                GuestLocation_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_smtp_notification_configuration = \
                GuestSmtpNotificationConfiguration_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_ssid = \
                GuestSsid_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_type = \
                GuestType_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_user = \
                GuestUser_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping = \
                IpToSgtMapping_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping_group = \
                IpToSgtMappingGroup_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_groups = \
                IdentityGroups_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_sequence = \
                IdentitySequence_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.internal_user = \
                InternalUser_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.mdm = \
                Mdm_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.misc = \
                Misc_v3_1_0(
                    self._session_mnt, self.object_factory, self._validator
                )
            self.my_device_portal = \
                MyDevicePortal_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.native_supplicant_profile = \
                NativeSupplicantProfile_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_device = \
                NetworkDevice_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.node_deployment = \
                NodeDeployment_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_group = \
                NodeGroup_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_details = \
                NodeDetails_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pan_ha = \
                PanHa_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portal_theme = \
                PortalTheme_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.profiler = \
                Profiler_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.profiler_profile = \
                ProfilerProfile_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.provider = \
                Provider_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.psn_node_details_with_radius_service = \
                PsnNodeDetailsWithRadiusService_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pull_deployment_info = \
                PullDeploymentInfo_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.px_grid_settings = \
                PxGridSettings_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.radius_failure = \
                RadiusFailure_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restid_store = \
                RestidStore_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.replication_status = \
                ReplicationStatus_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.repository = \
                Repository_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.sms_provider = \
                SmsProvider_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_connections = \
                SxpConnections_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_local_bindings = \
                SxpLocalBindings_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_vpns = \
                SxpVpns_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_group_to_virtual_network = \
                SecurityGroupToVirtualNetwork_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups = \
                SecurityGroups_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups_acls = \
                SecurityGroupsAcls_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.session_directory = \
                SessionDirectory_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_download = \
                SupportBundleDownload_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_status = \
                SupportBundleStatus_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_trigger_configuration = \
                SupportBundleTriggerConfiguration_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sync_ise_node = \
                SyncIseNode_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.system_health = \
                SystemHealth_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.system_certificate = \
                SystemCertificate_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.telemetry_information = \
                TelemetryInformation_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.trust_sec_configuration = \
                TrustSecConfiguration_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.trust_sec_sxp = \
                TrustSecSxp_v3_1_0(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.version_and_patch = \
                VersionAndPatch_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.version_info = \
                VersionInfo_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint = \
                Endpoint_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.nbar_app = \
                NbarApp_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal = \
                Portal_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.px_grid_node = \
                PxGridNode_v3_1_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sg_vn_mapping = \
                SgVnMapping_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.tasks = \
                Tasks_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.virtual_network = \
                VirtualNetwork_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.vn_vlan_mapping = \
                VnVlanMapping_v3_1_0(
                    self._session_ui, self.object_factory, self._validator
                )
        if self._version == '3.1.1':
            self.aci_bindings = \
                AciBindings_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.aci_settings = \
                AciSettings_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_endpoint = \
                AncEndpoint_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.active_directory = \
                ActiveDirectory_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.admin_user = \
                AdminUser_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_policy = \
                AncPolicy_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.byod_portal = \
                ByodPortal_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.certificate_profile = \
                CertificateProfile_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificate_template = \
                CertificateTemplate_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificates = \
                Certificates_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.clear_threats_and_vulnerabilities = \
                ClearThreatsAndVulnerabilities_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.consumer = \
                Consumer_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_certificate = \
                EndpointCertificate_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_identity_group = \
                EndpointIdentityGroup_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.filter_policy = \
                FilterPolicy_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_location = \
                GuestLocation_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_smtp_notification_configuration = \
                GuestSmtpNotificationConfiguration_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_ssid = \
                GuestSsid_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_type = \
                GuestType_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_user = \
                GuestUser_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping = \
                IpToSgtMapping_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping_group = \
                IpToSgtMappingGroup_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_groups = \
                IdentityGroups_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_sequence = \
                IdentitySequence_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.internal_user = \
                InternalUser_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.licensing = \
                Licensing_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.mdm = \
                Mdm_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.misc = \
                Misc_v3_1_1(
                    self._session_mnt, self.object_factory, self._validator
                )
            self.my_device_portal = \
                MyDevicePortal_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.native_supplicant_profile = \
                NativeSupplicantProfile_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_device = \
                NetworkDevice_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.node_deployment = \
                NodeDeployment_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_group = \
                NodeGroup_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_services = \
                NodeServices_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_details = \
                NodeDetails_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pan_ha = \
                PanHa_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.patching = \
                Patching_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portal_theme = \
                PortalTheme_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.profiler = \
                Profiler_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.profiler_profile = \
                ProfilerProfile_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.provider = \
                Provider_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.psn_node_details_with_radius_service = \
                PsnNodeDetailsWithRadiusService_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pull_deployment_info = \
                PullDeploymentInfo_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.px_grid_settings = \
                PxGridSettings_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.radius_failure = \
                RadiusFailure_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restid_store = \
                RestidStore_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.repository = \
                Repository_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.sms_provider = \
                SmsProvider_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_connections = \
                SxpConnections_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_local_bindings = \
                SxpLocalBindings_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_vpns = \
                SxpVpns_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_group_to_virtual_network = \
                SecurityGroupToVirtualNetwork_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups = \
                SecurityGroups_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups_acls = \
                SecurityGroupsAcls_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.session_directory = \
                SessionDirectory_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_download = \
                SupportBundleDownload_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_status = \
                SupportBundleStatus_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_trigger_configuration = \
                SupportBundleTriggerConfiguration_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.system_health = \
                SystemHealth_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.system_certificate = \
                SystemCertificate_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.telemetry_information = \
                TelemetryInformation_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.trust_sec_configuration = \
                TrustSecConfiguration_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.trust_sec_sxp = \
                TrustSecSxp_v3_1_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.version_and_patch = \
                VersionAndPatch_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.version_info = \
                VersionInfo_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint = \
                Endpoint_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.nbar_app = \
                NbarApp_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal = \
                Portal_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.proxy = \
                Proxy_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.px_grid_node = \
                PxGridNode_v3_1_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sg_vn_mapping = \
                SgVnMapping_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.tasks = \
                Tasks_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.telemetry = \
                Telemetry_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.virtual_network = \
                VirtualNetwork_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.vn_vlan_mapping = \
                VnVlanMapping_v3_1_1(
                    self._session_ui, self.object_factory, self._validator
                )
        if self._version == '3.1_Patch_1':
            self.aci_bindings = \
                AciBindings_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.aci_settings = \
                AciSettings_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_endpoint = \
                AncEndpoint_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.active_directory = \
                ActiveDirectory_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.admin_user = \
                AdminUser_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_policy = \
                AncPolicy_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.byod_portal = \
                ByodPortal_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.certificate_profile = \
                CertificateProfile_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificate_template = \
                CertificateTemplate_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificates = \
                Certificates_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.clear_threats_and_vulnerabilities = \
                ClearThreatsAndVulnerabilities_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.consumer = \
                Consumer_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_certificate = \
                EndpointCertificate_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_identity_group = \
                EndpointIdentityGroup_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.filter_policy = \
                FilterPolicy_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_location = \
                GuestLocation_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_smtp_notification_configuration = \
                GuestSmtpNotificationConfiguration_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_ssid = \
                GuestSsid_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_type = \
                GuestType_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_user = \
                GuestUser_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping = \
                IpToSgtMapping_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping_group = \
                IpToSgtMappingGroup_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_groups = \
                IdentityGroups_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_sequence = \
                IdentitySequence_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.internal_user = \
                InternalUser_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.licensing = \
                Licensing_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.mdm = \
                Mdm_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.misc = \
                Misc_v3_1_patch_1(
                    self._session_mnt, self.object_factory, self._validator
                )
            self.my_device_portal = \
                MyDevicePortal_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.native_supplicant_profile = \
                NativeSupplicantProfile_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_device = \
                NetworkDevice_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.node_deployment = \
                NodeDeployment_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_group = \
                NodeGroup_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_services = \
                NodeServices_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_details = \
                NodeDetails_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pan_ha = \
                PanHa_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.patching = \
                Patching_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portal_theme = \
                PortalTheme_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.profiler = \
                Profiler_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.profiler_profile = \
                ProfilerProfile_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.provider = \
                Provider_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.psn_node_details_with_radius_service = \
                PsnNodeDetailsWithRadiusService_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pull_deployment_info = \
                PullDeploymentInfo_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.px_grid_settings = \
                PxGridSettings_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.radius_failure = \
                RadiusFailure_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restid_store = \
                RestidStore_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.repository = \
                Repository_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.sms_provider = \
                SmsProvider_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_connections = \
                SxpConnections_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_local_bindings = \
                SxpLocalBindings_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_vpns = \
                SxpVpns_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_group_to_virtual_network = \
                SecurityGroupToVirtualNetwork_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups = \
                SecurityGroups_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups_acls = \
                SecurityGroupsAcls_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.session_directory = \
                SessionDirectory_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_download = \
                SupportBundleDownload_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_status = \
                SupportBundleStatus_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_trigger_configuration = \
                SupportBundleTriggerConfiguration_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.system_health = \
                SystemHealth_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.system_certificate = \
                SystemCertificate_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.telemetry_information = \
                TelemetryInformation_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.trust_sec_configuration = \
                TrustSecConfiguration_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.trust_sec_sxp = \
                TrustSecSxp_v3_1_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.version_and_patch = \
                VersionAndPatch_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.version_info = \
                VersionInfo_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint = \
                Endpoint_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.nbar_app = \
                NbarApp_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal = \
                Portal_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.proxy = \
                Proxy_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.px_grid_node = \
                PxGridNode_v3_1_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sg_vn_mapping = \
                SgVnMapping_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.tasks = \
                Tasks_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.telemetry = \
                Telemetry_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.virtual_network = \
                VirtualNetwork_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.vn_vlan_mapping = \
                VnVlanMapping_v3_1_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
        if self._version == '3.2_beta':
            self.aci_bindings = \
                AciBindings_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.aci_settings = \
                AciSettings_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_endpoint = \
                AncEndpoint_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.active_directory = \
                ActiveDirectory_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.admin_user = \
                AdminUser_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_policy = \
                AncPolicy_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.byod_portal = \
                ByodPortal_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.certificate_profile = \
                CertificateProfile_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificate_template = \
                CertificateTemplate_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificates = \
                Certificates_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.clear_threats_and_vulnerabilities = \
                ClearThreatsAndVulnerabilities_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.configuration = \
                Configuration_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.consumer = \
                Consumer_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.dataconnect_services = \
                DataconnectServices_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.edda = \
                Edda_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_certificate = \
                EndpointCertificate_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_identity_group = \
                EndpointIdentityGroup_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.filter_policy = \
                FilterPolicy_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_location = \
                GuestLocation_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_smtp_notification_configuration = \
                GuestSmtpNotificationConfiguration_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_ssid = \
                GuestSsid_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_type = \
                GuestType_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_user = \
                GuestUser_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping = \
                IpToSgtMapping_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping_group = \
                IpToSgtMappingGroup_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_groups = \
                IdentityGroups_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_sequence = \
                IdentitySequence_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.internal_user = \
                InternalUser_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.licensing = \
                Licensing_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.mdm = \
                Mdm_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.misc = \
                Misc_v3_2_beta(
                    self._session_mnt, self.object_factory, self._validator
                )
            self.my_device_portal = \
                MyDevicePortal_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.native_supplicant_profile = \
                NativeSupplicantProfile_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_device = \
                NetworkDevice_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.node_deployment = \
                NodeDeployment_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_group = \
                NodeGroup_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_services = \
                NodeServices_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_details = \
                NodeDetails_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pan_ha = \
                PanHa_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.patching = \
                Patching_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portal_theme = \
                PortalTheme_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.profiler = \
                Profiler_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.profiler_profile = \
                ProfilerProfile_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.provider = \
                Provider_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.psn_node_details_with_radius_service = \
                PsnNodeDetailsWithRadiusService_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pull_deployment_info = \
                PullDeploymentInfo_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.px_grid_settings = \
                PxGridSettings_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.radius_failure = \
                RadiusFailure_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restid_store = \
                RestidStore_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.repository = \
                Repository_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.sms_provider = \
                SmsProvider_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_connections = \
                SxpConnections_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_local_bindings = \
                SxpLocalBindings_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_vpns = \
                SxpVpns_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_group_to_virtual_network = \
                SecurityGroupToVirtualNetwork_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups = \
                SecurityGroups_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups_acls = \
                SecurityGroupsAcls_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.session_directory = \
                SessionDirectory_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.subscriber = \
                Subscriber_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.support_bundle_download = \
                SupportBundleDownload_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_status = \
                SupportBundleStatus_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_trigger_configuration = \
                SupportBundleTriggerConfiguration_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.system_health = \
                SystemHealth_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.system_certificate = \
                SystemCertificate_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.telemetry_information = \
                TelemetryInformation_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.trust_sec_configuration = \
                TrustSecConfiguration_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.trust_sec_sxp = \
                TrustSecSxp_v3_2_beta(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.version_and_patch = \
                VersionAndPatch_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.version_info = \
                VersionInfo_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint = \
                Endpoint_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portal = \
                Portal_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.proxy = \
                Proxy_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.px_grid_node = \
                PxGridNode_v3_2_beta(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tasks = \
                Tasks_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
            self.telemetry = \
                Telemetry_v3_2_beta(
                    self._session_ui, self.object_factory, self._validator
                )
        if self._version == '3.3_patch_1':
            self.aci_bindings = \
                AciBindings_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.aci_settings = \
                AciSettings_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ad_groups = \
                ADGroups_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.anc_endpoint = \
                AncEndpoint_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.active_directories = \
                ActiveDirectories_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.active_directory = \
                ActiveDirectory_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.admin_user = \
                AdminUser_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.anc_policy = \
                AncPolicy_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.byod_portal = \
                ByodPortal_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.certificate_profile = \
                CertificateProfile_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificate_template = \
                CertificateTemplate_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificates = \
                Certificates_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.clear_threats_and_vulnerabilities = \
                ClearThreatsAndVulnerabilities_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.configuration = \
                Configuration_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.consumer = \
                Consumer_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.dataconnect_services = \
                DataconnectServices_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.duo_identity_sync = \
                DuoIdentitySync_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.duo_mfa = \
                DuoMfa_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_stop_replication_service = \
                EndpointStopReplicationService_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.endpoint_certificate = \
                EndpointCertificate_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoint_identity_group = \
                EndpointIdentityGroup_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.filter_policy = \
                FilterPolicy_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_location = \
                GuestLocation_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_smtp_notification_configuration = \
                GuestSmtpNotificationConfiguration_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_ssid = \
                GuestSsid_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_type = \
                GuestType_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guest_user = \
                GuestUser_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping = \
                IpToSgtMapping_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ip_to_sgt_mapping_group = \
                IpToSgtMappingGroup_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_groups = \
                IdentityGroups_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identity_sequence = \
                IdentitySequence_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.internal_user = \
                InternalUser_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.licensing = \
                Licensing_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.mdm = \
                Mdm_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.misc = \
                Misc_v3_3_patch_1(
                    self._session_mnt, self.object_factory, self._validator
                )
            self.my_device_portal = \
                MyDevicePortal_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.native_ipsec = \
                NativeIpsec_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.native_supplicant_profile = \
                NativeSupplicantProfile_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_device = \
                NetworkDevice_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.node_deployment = \
                NodeDeployment_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_group = \
                NodeGroup_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_services = \
                NodeServices_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_details = \
                NodeDetails_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pan_ha = \
                PanHa_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.patching = \
                Patching_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portal_theme = \
                PortalTheme_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.profiler = \
                Profiler_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.profiler_profile = \
                ProfilerProfile_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.provider = \
                Provider_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.psn_node_details_with_radius_service = \
                PsnNodeDetailsWithRadiusService_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pull_deployment_info = \
                PullDeploymentInfo_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.px_grid_settings = \
                PxGridSettings_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.radius_failure = \
                RadiusFailure_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restid_store = \
                RestidStore_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.repository = \
                Repository_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.sms_provider = \
                SmsProvider_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_connections = \
                SxpConnections_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_local_bindings = \
                SxpLocalBindings_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxp_vpns = \
                SxpVpns_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_group_to_virtual_network = \
                SecurityGroupToVirtualNetwork_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups = \
                SecurityGroups_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.security_groups_acls = \
                SecurityGroupsAcls_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.session_directory = \
                SessionDirectory_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.sgt_range_reservation = \
                SgtRangeReservation_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.subscriber = \
                Subscriber_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.support_bundle_download = \
                SupportBundleDownload_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_status = \
                SupportBundleStatus_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.support_bundle_trigger_configuration = \
                SupportBundleTriggerConfiguration_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.system_health = \
                SystemHealth_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.system_certificate = \
                SystemCertificate_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.telemetry_information = \
                TelemetryInformation_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.trust_sec_configuration = \
                TrustSecConfiguration_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.trust_sec_sxp = \
                TrustSecSxp_v3_3_patch_1(
                    self._session_px_grid, self.object_factory, self._validator
                )
            self.user_equipment = \
                UserEquipment_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.version_and_patch = \
                VersionAndPatch_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.version_info = \
                VersionInfo_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.custom_attributes = \
                CustomAttributes_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.enable_mfa = \
                EnableMFA_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.endpoint = \
                Endpoint_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoints = \
                Endpoints_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.full_upgrade = \
                FullUpgrade_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.is_mfa_enabled = \
                IsMFAEnabled_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.nbar_app = \
                NbarApp_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.portal = \
                Portal_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.proxy = \
                Proxy_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.px_grid_direct = \
                PxGridDirect_v3_3_patch_1(
                    self._px_grid_direct, self.object_factory, self._validator
                )
            self.px_grid_node = \
                PxGridNode_v3_3_patch_1(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sg_vn_mapping = \
                SgVnMapping_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.tasks = \
                Tasks_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.telemetry = \
                Telemetry_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.virtual_network = \
                VirtualNetwork_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
            self.vn_vlan_mapping = \
                VnVlanMapping_v3_3_patch_1(
                    self._session_ui, self.object_factory, self._validator
                )
        if self._version == '3.5.0':
            self.aci_connection = \
                AciConnection_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.aci_data = \
                AciData_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.a_d_groups = \
                ADGroups_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.active_directories = \
                ActiveDirectories_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.admin_groups = \
                AdminGroups_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.admin_users = \
                AdminUsers_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.certificates = \
                Certificates_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.classificationrule = \
                Classificationrule_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.configuration = \
                Configuration_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.data_access = \
                DataAccess_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.dataconnect_services = \
                DataconnectServices_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_admin_m_f_a_rules = \
                DeviceAdminMFARules_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_command_sets = \
                DeviceAdministrationCommandSets_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_policy_sets = \
                DeviceAdministrationPolicySets_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_shell_profiles = \
                DeviceAdministrationShellProfiles_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.duo_identity_sync = \
                DuoIdentitySync_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.duo_mfa = \
                DuoMfa_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.endpoint_stop_replication_service = \
                EndpointStopReplicationService_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.inbound_rule = \
                InboundRule_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.licensing = \
                Licensing_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.menu_access = \
                MenuAccess_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.misc = \
                Misc_v3_5_0(
                    self._session_mnt, self.object_factory, self._validator
                )
            self.n_b_a_r_application_management = \
                NBARApplicationManagement_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.native_ipsec = \
                NativeIpsec_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_profiles = \
                NetworkAccessAuthorizationProfiles_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionaries = \
                NetworkAccessDictionaries_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attributes = \
                NetworkAccessDictionaryAttributes_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_m_f_a_rules = \
                NetworkAccessMFARules_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_policy_sets = \
                NetworkAccessPolicySets_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_deployment = \
                NodeDeployment_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.node_group = \
                NodeGroup_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.nodeservices = \
                Nodeservices_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.outbound_rule = \
                OutboundRule_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.pan_ha = \
                PanHa_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.patch = \
                Patch_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.patching = \
                Patching_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.prometheus_alertmanager = \
                PrometheusAlertmanager_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.r_b_a_c_policy = \
                RBACPolicy_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.repository = \
                Repository_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.sxp = \
                Sxp_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.sxp_domainswithmappinganddevicescounts = \
                SxpDomainswithmappinganddevicescounts_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.security_group_management = \
                SecurityGroupManagement_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.sgt = \
                Sgt_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.sgt_range_reservation = \
                SgtRangeReservation_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.subscriber = \
                Subscriber_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.trust_sec_open_api_view = \
                TrustSecOpenApiView_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.trustsec_c_o_a_push = \
                TrustsecCOAPush_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.trustsec_http_s_server = \
                TrustsecHttpSServer_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.trustsec_integration_rule_default_trustsec_integration_ruleset = \
                TrustsecIntegrationRuleDefaultTrustsecIntegrationRuleset_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.trustsec_integration_rule_dictionaries = \
                TrustsecIntegrationRuleDictionaries_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.trustsec_integration_rule_dictionary_attributes = \
                TrustsecIntegrationRuleDictionaryAttributes_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.trustsec_settings = \
                TrustsecSettings_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.trustsecdevicesreport = \
                Trustsecdevicesreport_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.upgrade = \
                Upgrade_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.user_equipment = \
                UserEquipment_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.virtual_network_management = \
                VirtualNetworkManagement_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.acibindings = \
                Acibindings_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.acisettings = \
                Acisettings_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.activedirectory = \
                Activedirectory_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.adminuser = \
                Adminuser_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.adresourcereservation = \
                Adresourcereservation_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.allowedprotocols = \
                Allowedprotocols_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ancendpoint = \
                Ancendpoint_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ancpolicy = \
                Ancpolicy_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.authorizationprofile = \
                Authorizationprofile_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.byodportal = \
                Byodportal_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificateprofile = \
                Certificateprofile_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.certificatetemplate = \
                Certificatetemplate_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.ctsenvdata = \
                Ctsenvdata_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.ctsmatrix = \
                Ctsmatrix_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.customattributes = \
                Customattributes_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.deploymentinfo = \
                Deploymentinfo_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.downloadableacl = \
                Downloadableacl_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.egressmatrixcell = \
                Egressmatrixcell_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.enable_m_f_a = \
                EnableMFA_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.endpoint = \
                Endpoint_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.endpointcert = \
                Endpointcert_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpointgroup = \
                Endpointgroup_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.endpoints = \
                Endpoints_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.externalradiusserver = \
                Externalradiusserver_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.filterpolicy = \
                Filterpolicy_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guestlocation = \
                Guestlocation_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guestsmtpnotificationsettings = \
                Guestsmtpnotificationsettings_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guestssid = \
                Guestssid_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guesttype = \
                Guesttype_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.guestuser = \
                Guestuser_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.hotspotportal = \
                Hotspotportal_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.identitygroup = \
                Identitygroup_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.idstoresequence = \
                Idstoresequence_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.internaluser = \
                Internaluser_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.is_m_f_a_enabled = \
                IsMFAEnabled_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.ldap = \
                Ldap_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.mydeviceportal = \
                Mydeviceportal_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.networkdevice = \
                Networkdevice_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.networkdevicegroup = \
                Networkdevicegroup_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.node = \
                Node_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.nspprofile = \
                Nspprofile_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portal = \
                Portal_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.portalglobalsetting = \
                Portalglobalsetting_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.portaltheme = \
                Portaltheme_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.profilerprofile = \
                Profilerprofile_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.proxy = \
                Proxy_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.px_grid_cloud = \
                PxGridCloud_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.px_grid_direct = \
                PxGridDirect_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.px_grid_direct_push_apis = \
                PxGridDirectPushApis_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.pxgridnode = \
                Pxgridnode_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.pxgridsettings = \
                Pxgridsettings_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.radiusserversequence = \
                Radiusserversequence_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.reportconfig = \
                Reportconfig_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.restidstore = \
                Restidstore_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restidstoreattribute = \
                Restidstoreattribute_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restidstoredeviceattribute = \
                Restidstoredeviceattribute_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.restidstorepredefinedregex = \
                Restidstorepredefinedregex_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.restidstoresettings = \
                Restidstoresettings_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.selfregportal = \
                Selfregportal_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.service = \
                Service_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sessionservicenode = \
                Sessionservicenode_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sgacl = \
                Sgacl_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sgacls = \
                Sgacls_v3_5_0(
                    self._session_main, self.object_factory, self._validator
                )
            self.sgmapping = \
                Sgmapping_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sgmappinggroup = \
                Sgmappinggroup_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sgt = \
                Sgt_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sgtvnvlan = \
                Sgtvnvlan_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.smsprovider = \
                Smsprovider_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsoredguestportal = \
                Sponsoredguestportal_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsorgroup = \
                Sponsorgroup_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsorgroupmember = \
                Sponsorgroupmember_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sponsorportal = \
                Sponsorportal_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.supportbundle = \
                Supportbundle_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.supportbundledownload = \
                Supportbundledownload_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.supportbundlestatus = \
                Supportbundlestatus_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxpconnections = \
                Sxpconnections_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxplocalbindings = \
                Sxplocalbindings_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.sxpvpns = \
                Sxpvpns_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.systemcertificate = \
                Systemcertificate_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacscommandsets = \
                Tacacscommandsets_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacsexternalservers = \
                Tacacsexternalservers_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacsprofile = \
                Tacacsprofile_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tacacsserversequence = \
                Tacacsserversequence_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.tasks = \
                Tasks_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.telemetry = \
                Telemetry_v3_5_0(
                    self._session_ui, self.object_factory, self._validator
                )
            self.telemetryinfo = \
                Telemetryinfo_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
            self.threat = \
                Threat_v3_5_0(
                    self._session_ers, self.object_factory, self._validator
                )
        self.custom_caller = \
            CustomCaller(self._session, self.object_factory)

    def _not_initialize_api_wrappers(self):
        """Function used when perform_initialize is False in class init.
        Defines the top-level properties as None."""
        self.aci_connection = None
        self.aci_data = None
        self.acibindings = None
        self.acisettings = None
        self.active_directories = None
        self.activedirectory = None
        self.a_d_groups = None
        self.admin_groups = None
        self.admin_users = None
        self.adminuser = None
        self.adresourcereservation = None
        self.allowedprotocols = None
        self.ancendpoint = None
        self.ancpolicy = None
        self.authorizationprofile = None
        self.backup_and_restore = None
        self.byodportal = None
        self.certificateprofile = None
        self.certificates = None
        self.certificatetemplate = None
        self.classificationrule = None
        self.configuration = None
        self.ctsenvdata = None
        self.ctsmatrix = None
        self.custom_caller = None
        self.customattributes = None
        self.data_access = None
        self.dataconnect_services = None
        self.deploymentinfo = None
        self.device_admin_m_f_a_rules = None
        self.device_administration_authentication_rules = None
        self.device_administration_authorization_exception_rules = None
        self.device_administration_authorization_global_exception_rules = None
        self.device_administration_authorization_rules = None
        self.device_administration_command_sets = None
        self.device_administration_conditions = None
        self.device_administration_dictionary_attributes_list = None
        self.device_administration_identity_stores = None
        self.device_administration_network_conditions = None
        self.device_administration_policy_sets = None
        self.device_administration_service_names = None
        self.device_administration_shell_profiles = None
        self.device_administration_time_date_conditions = None
        self.downloadableacl = None
        self.duo_identity_sync = None
        self.duo_mfa = None
        self.egressmatrixcell = None
        self.enable_m_f_a = None
        self.endpoint = None
        self.endpoint_stop_replication_service = None
        self.endpointcert = None
        self.endpointgroup = None
        self.endpoints = None
        self.externalradiusserver = None
        self.filterpolicy = None
        self.guestlocation = None
        self.guestsmtpnotificationsettings = None
        self.guestssid = None
        self.guesttype = None
        self.guestuser = None
        self.hotspotportal = None
        self.identitygroup = None
        self.idstoresequence = None
        self.inbound_rule = None
        self.internaluser = None
        self.is_m_f_a_enabled = None
        self.ldap = None
        self.licensing = None
        self.menu_access = None
        self.misc = None
        self.mydeviceportal = None
        self.native_ipsec = None
        self.n_b_a_r_application_management = None
        self.network_access_authentication_rules = None
        self.network_access_authorization_exception_rules = None
        self.network_access_authorization_global_exception_rules = None
        self.network_access_authorization_profiles = None
        self.network_access_authorization_rules = None
        self.network_access_conditions = None
        self.network_access_dictionaries = None
        self.network_access_dictionary_attributes = None
        self.network_access_dictionary_attributes_list = None
        self.network_access_identity_stores = None
        self.network_access_m_f_a_rules = None
        self.network_access_network_conditions = None
        self.network_access_policy_sets = None
        self.network_access_security_groups = None
        self.network_access_service_names = None
        self.network_access_time_date_conditions = None
        self.networkdevice = None
        self.networkdevicegroup = None
        self.node = None
        self.node_deployment = None
        self.node_group = None
        self.nodeservices = None
        self.nspprofile = None
        self.outbound_rule = None
        self.pan_ha = None
        self.patch = None
        self.patching = None
        self.portal = None
        self.portalglobalsetting = None
        self.portaltheme = None
        self.profilerprofile = None
        self.prometheus_alertmanager = None
        self.proxy = None
        self.px_grid_cloud = None
        self.px_grid_direct = None
        self.px_grid_direct_push_apis = None
        self.pxgridnode = None
        self.pxgridsettings = None
        self.radiusserversequence = None
        self.r_b_a_c_policy = None
        self.reportconfig = None
        self.repository = None
        self.restidstore = None
        self.restidstoreattribute = None
        self.restidstoredeviceattribute = None
        self.restidstorepredefinedregex = None
        self.restidstoresettings = None
        self.security_group_management = None
        self.selfregportal = None
        self.service = None
        self.sessionservicenode = None
        self.sgacl = None
        self.sgacls = None
        self.sgmapping = None
        self.sgmappinggroup = None
        self.sgt = None
        self.sgt_range_reservation = None
        self.sgtvnvlan = None
        self.smsprovider = None
        self.sponsoredguestportal = None
        self.sponsorgroup = None
        self.sponsorgroupmember = None
        self.sponsorportal = None
        self.subscriber = None
        self.supportbundle = None
        self.supportbundledownload = None
        self.supportbundlestatus = None
        self.sxp = None
        self.sxp_domainswithmappinganddevicescounts = None
        self.sxpconnections = None
        self.sxplocalbindings = None
        self.sxpvpns = None
        self.systemcertificate = None
        self.tacacscommandsets = None
        self.tacacsexternalservers = None
        self.tacacsprofile = None
        self.tacacsserversequence = None
        self.tasks = None
        self.telemetry = None
        self.telemetryinfo = None
        self.threat = None
        self.trustsec_c_o_a_push = None
        self.trustsecdevicesreport = None
        self.trustsec_http_s_server = None
        self.trustsec_integration_rule_default_trustsec_integration_ruleset = None
        self.trustsec_integration_rule_dictionaries = None
        self.trustsec_integration_rule_dictionary_attributes = None
        self.trust_sec_open_api_view = None
        self.trustsec_settings = None
        self.upgrade = None
        self.user_equipment = None
        self.virtual_network_management = None

  

    def initialize_authentication(self):
        """
        Function used when perform_initialize is True in class init.
        Init Authentication wrapper early to use for basicAuth requests.
        """
        warnings.warn("Performing initialization of authentication property", UserWarning)
        self._initialize_authentication()

    def initialize_sessions(self):
        """
        Performs initialization of "session_ui", "session_ers", "session", "session_mnt", "session_px_grid" properties.
        Creating for each one a RestSession object that handles the requests.
        """
        sessions = '"session_ui", "session_ers", "session", "session_mnt", "session_px_grid"'
        warnings.warn("Performing initialization of properties: {0}".format(sessions), UserWarning)
        self._initialize_sessions()

    def initialize_api_wrappers(self):
        """Initializes the API wrappers according to the defined version."""
        warnings.warn("Performing initialization of API wrappers", UserWarning)
        self._initialize_api_wrappers()

    def reinitialize(self):
        """Calls all the methods necessary to initialize/reinitialize the IdentityServicesEngineAPI."""
        self.initialize_authentication()
        self.initialize_sessions()
        self.initialize_api_wrappers()

    @property
    def authentication(self):
        """Utility object that provides authentication method."""
        return self._authentication

    @property
    def perform_initialize(self):
        """The flag that, if enabled, initialized in the constructor all
            the related objects to manage information from Identity Services Engine."""
        return self._perform_initialize

    @property
    def username(self):
        """HTTP Basic Auth username"""
        return self._username

    def is_password(self, password):
        """Check if the value of the current password match"""
        return self._password == password

    def is_encoded_auth(self, encoded_auth):
        """Check if the value of the current encoded_auth match"""
        return self._encoded_auth == encoded_auth

    @property
    def uses_api_gateway(self):
        """If the Identity Services Engine API uses an API Gateway."""
        return self._uses_api_gateway

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes for ERS and Custom Caller operations."""
        return self._base_url

    @property
    def ui_base_url(self):
        """The ui base URL prefixed to the individual API endpoint suffixes for UI operations."""
        return self._ui_base_url

    @property
    def ers_base_url(self):
        """The ers base URL prefixed to the individual API endpoint suffixes for ERS operations."""
        return self._ers_base_url

    @property
    def mnt_base_url(self):
        """The mnt base URL prefixed to the individual API endpoint suffixes for MNT operations."""
        return self._mnt_base_url

    @property
    def px_grid_base_url(self):
        """The px_grid base URL prefixed to the individual API endpoint suffixes for PxGrid operations"""
        return self._px_grid_base_url

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self._single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self._wait_on_rate_limit

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._verify

    @property
    def version(self):
        """The API version of Identity Services Engine."""
        return self._version

    @property
    def debug(self):
        """If log information about Identity Services Engine APIs' request and response process is shown."""
        return self._debug

    @property
    def uses_csrf_token(self):
        """If the Identity Services Engine ERS API requires the X-CSRF-Token to be sent."""
        return self._uses_csrf_token

    @property
    def object_factory(self):
        """The factory function to use to create
            Python objects from the returned Identity Services Engine JSON data objects."""
        return self._object_factory

    @property
    def validator(self):
        """The function used to validate Python objects
            sent in the request body."""
        return self._validator

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

    @username.setter
    def username(self, value):
        """HTTP Basic Auth username.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, str, may_be_none=True)
        self._username = value
        warnings.warn("Changed username. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    def change_password(self, password):
        """HTTP Basic Auth password.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(password, str, may_be_none=True)
        self._password = password
        warnings.warn("Changed password. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    def change_encoded_auth(self, encoded_auth):
        """HTTP Basic Auth base64 encoded string.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(encoded_auth, str, may_be_none=True)
        self._encoded_auth = encoded_auth
        warnings.warn("Changed encoded_auth. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @uses_api_gateway.setter
    def uses_api_gateway(self, value):
        """If the Identity Services Engine API uses an API Gateway.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, (bool, str), may_be_none=False)
        self._uses_api_gateway = value
        if isinstance(self._uses_api_gateway, str):
            self._uses_api_gateway = 'true' in self._uses_api_gateway.lower()
        warnings.warn("Changed uses_api_gateway. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @base_url.setter
    def base_url(self, value):
        """The base URL prefixed to the individual API endpoint suffixes for ERS and Custom Caller operations.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, str, may_be_none=not self._uses_api_gateway)
        self.base_url = value
        warnings.warn("Changed base_url. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @ui_base_url.setter
    def ui_base_url(self, value):
        """The ui base URL prefixed to the individual API endpoint suffixes for UI operations.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, str, may_be_none=self._uses_api_gateway)
        self._ui_base_url = value
        warnings.warn("Changed ui_base_url. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @ers_base_url.setter
    def ers_base_url(self, value):
        """The ers base URL prefixed to the individual API endpoint suffixes for ERS operations.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, str, may_be_none=self._uses_api_gateway)
        self._ers_base_url = value
        warnings.warn("Changed ers_base_url. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @mnt_base_url.setter
    def mnt_base_url(self, value):
        """The mnt base URL prefixed to the individual API endpoint suffixes for MNT operations.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, str, may_be_none=self._uses_api_gateway)
        self._mnt_base_url = value
        warnings.warn("Changed mnt_base_url. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @px_grid_base_url.setter
    def px_grid_base_url(self, value):
        """The px_grid base URL prefixed to the individual API endpoint suffixes for PxGrid operations

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, str, may_be_none=self._uses_api_gateway)
        self._px_grid_base_url = value
        warnings.warn("Changed px_grid_base_url. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """Timeout (in seconds) for an single HTTP request.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, int)
        assert value is None or value > 0
        self._single_request_timeout = value
        warnings.warn("Changed single_request_timeout. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, value):
        """Automatic rate-limit handling enabled / disabled.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, bool)
        self._wait_on_rate_limit = value
        warnings.warn("Changed wait_on_rate_limit. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @verify.setter
    def verify(self, value):
        """The verify (TLS Certificate) for the API endpoints.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, (bool, str), may_be_none=False)
        self._verify = value
        warnings.warn("Changed verify. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @version.setter
    def version(self, value):
        """The API version of Identity Services Engine.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, str, may_be_none=False)
        if value not in ['3.1.0', '3.1.1', '3.1_Patch_1', '3.2_beta', '3.3_patch_1']:
            raise VersionError(
                'Unknown API version, '
                + 'known versions are {0}'.format(
                    '3.1.0, 3.1.1, 3.1_Patch_1, 3.2_beta and 3.3_patch_1.'
                )
            )
        self._version = value
        if self._version == '3.1.1':
            warnings.warn("The ISE version 3.1.1 will be removed in future versions and replaced by 3.1_Patch_1", FutureWarning)
        self._validator = self._original_validator(self._version).json_schema_validate
        warnings.warn("Changed version. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @debug.setter
    def debug(self, value):
        """If log information about Identity Services Engine APIs' request and response process is shown.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, (bool, str), may_be_none=False)
        self._debug = value
        if isinstance(self._debug, str):
            self._debug = 'true' in self._debug.lower()
        warnings.warn("Changed debug. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @uses_csrf_token.setter
    def uses_csrf_token(self, value):
        """If the Identity Services Engine ERS API requires the X-CSRF-Token to be sent.

        It may require to call reinitialize to distribute the changes accross the SDK objects."""
        check_type(value, (bool, str), may_be_none=False)
        self._uses_csrf_token = value
        if isinstance(self._uses_csrf_token, str):
            self._uses_csrf_token = 'true' in self._uses_csrf_token.lower()
        warnings.warn("Changed uses_csrf_token. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @object_factory.setter
    def object_factory(self, value):
        """The factory function to use to create
            objects from the returned Identity Services Engine JSON data objects.

            It may require to call reinitialize to distribute the changes accross the SDK objects."""
        self._object_factory = value
        warnings.warn("Changed object_factory. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    @validator.setter
    def validator(self, value):
        """The factory class with function
            json_schema_validate(model:string) that returns an object with
            function validate(obj:dict) is used to validate Python objects
            sent in the request body

            It may require to call reinitialize to distribute the changes accross the SDK objects."""
        if value is not None and callable(value):
            if hasattr(value(self._version), 'json_schema_validate'):
                self._validator = value(self._version).json_schema_validate
                self._original_validator = value
            else:
                raise TypeError("validator(version) does not have json_schema_validate")
        else:
            raise TypeError("validator value is not callable")
        warnings.warn("Changed validator. It requires to call reinitialize to distribute the change accross the SDK objects.", UserWarning)

    def _get_csrf_token(self):
        csrf_token = None
        if not self._uses_csrf_token:
            return csrf_token

        family = "endpoint"
        function = 'get_version'
        if not hasattr(self, family):
            return csrf_token
        if not hasattr(self.endpoint, function):
            return csrf_token
        get_request = self.endpoint.get_version(headers={"X-CSRF-Token": "fetch"})
        if get_request is None:
            return csrf_token
        if get_request.headers is None:
            return csrf_token
        if get_request.headers.get("X-CSRF-Token") is None:
            return csrf_token
        csrf_token = get_request.headers["X-CSRF-Token"]
        return csrf_token
