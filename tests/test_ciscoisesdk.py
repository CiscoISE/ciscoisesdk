
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
from ciscoisesdk.api.v3_0_0.anc_policy import \
    AncPolicy as AncPolicy_v3_0_0
from ciscoisesdk.api.v3_0_0.active_directory import \
    ActiveDirectory as ActiveDirectory_v3_0_0
from ciscoisesdk.api.v3_0_0.allowed_protocols import \
    AllowedProtocols as AllowedProtocols_v3_0_0
from ciscoisesdk.api.v3_0_0.authorization_profile import \
    AuthorizationProfile as AuthorizationProfile_v3_0_0
from ciscoisesdk.api.v3_0_0.backup_and_restore import \
    BackupAndRestore as BackupAndRestore_v3_0_0
from ciscoisesdk.api.v3_0_0.certificates import \
    Certificates as Certificates_v3_0_0
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
from ciscoisesdk.api.v3_0_0.endpoint import \
    Endpoint as Endpoint_v3_0_0
from ciscoisesdk.api.v3_0_0.endpoint_group import \
    EndpointGroup as EndpointGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.external_radius_server import \
    ExternalRadiusServer as ExternalRadiusServer_v3_0_0
from ciscoisesdk.api.v3_0_0.filter_policy import \
    FilterPolicy as FilterPolicy_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_location import \
    GuestLocation as GuestLocation_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_smtp_notifications import \
    GuestSmtpNotifications as GuestSmtpNotifications_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_ssid import \
    GuestSsid as GuestSsid_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_type import \
    GuestType as GuestType_v3_0_0
from ciscoisesdk.api.v3_0_0.guest_user import \
    GuestUser as GuestUser_v3_0_0
from ciscoisesdk.api.v3_0_0.hotspot_portal import \
    HotspotPortal as HotspotPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.identity_group import \
    IdentityGroup as IdentityGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.identity_store_sequence import \
    IdentityStoreSequence as IdentityStoreSequence_v3_0_0
from ciscoisesdk.api.v3_0_0.internal_user import \
    InternalUser as InternalUser_v3_0_0
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
from ciscoisesdk.api.v3_0_0.pan_ha import \
    PanHa as PanHa_v3_0_0
from ciscoisesdk.api.v3_0_0.portal import \
    Portal as Portal_v3_0_0
from ciscoisesdk.api.v3_0_0.portal_global_setting import \
    PortalGlobalSetting as PortalGlobalSetting_v3_0_0
from ciscoisesdk.api.v3_0_0.portal_theme import \
    PortalTheme as PortalTheme_v3_0_0
from ciscoisesdk.api.v3_0_0.radius_server_sequence import \
    RadiusServerSequence as RadiusServerSequence_v3_0_0
from ciscoisesdk.api.v3_0_0.restid_store import \
    RestidStore as RestidStore_v3_0_0
from ciscoisesdk.api.v3_0_0.replication_status import \
    ReplicationStatus as ReplicationStatus_v3_0_0
from ciscoisesdk.api.v3_0_0.repository import \
    Repository as Repository_v3_0_0
from ciscoisesdk.api.v3_0_0.sg_acl import \
    SgAcl as SgAcl_v3_0_0
from ciscoisesdk.api.v3_0_0.sgt import \
    Sgt as Sgt_v3_0_0
from ciscoisesdk.api.v3_0_0.sms_provider import \
    SmsProvider as SmsProvider_v3_0_0
from ciscoisesdk.api.v3_0_0.self_registered_portal import \
    SelfRegisteredPortal as SelfRegisteredPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsor_group import \
    SponsorGroup as SponsorGroup_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsor_group_member import \
    SponsorGroupMember as SponsorGroupMember_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsor_portal import \
    SponsorPortal as SponsorPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.sponsored_guest_portal import \
    SponsoredGuestPortal as SponsoredGuestPortal_v3_0_0
from ciscoisesdk.api.v3_0_0.sync_ise_node import \
    SyncIseNode as SyncIseNode_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_command_sets import \
    TacacsCommandSets as TacacsCommandSets_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_external_servers import \
    TacacsExternalServers as TacacsExternalServers_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_profile import \
    TacacsProfile as TacacsProfile_v3_0_0
from ciscoisesdk.api.v3_0_0.tacacs_server_sequence import \
    TacacsServerSequence as TacacsServerSequence_v3_0_0
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
            assert isinstance(api.anc_policy, AncPolicy_v3_0_0)
            assert isinstance(api.active_directory, ActiveDirectory_v3_0_0)
            assert isinstance(api.allowed_protocols, AllowedProtocols_v3_0_0)
            assert isinstance(api.authorization_profile, AuthorizationProfile_v3_0_0)
            assert isinstance(api.backup_and_restore, BackupAndRestore_v3_0_0)
            assert isinstance(api.certificates, Certificates_v3_0_0)
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
            assert isinstance(api.endpoint, Endpoint_v3_0_0)
            assert isinstance(api.endpoint_group, EndpointGroup_v3_0_0)
            assert isinstance(api.external_radius_server, ExternalRadiusServer_v3_0_0)
            assert isinstance(api.filter_policy, FilterPolicy_v3_0_0)
            assert isinstance(api.guest_location, GuestLocation_v3_0_0)
            assert isinstance(api.guest_smtp_notifications, GuestSmtpNotifications_v3_0_0)
            assert isinstance(api.guest_ssid, GuestSsid_v3_0_0)
            assert isinstance(api.guest_type, GuestType_v3_0_0)
            assert isinstance(api.guest_user, GuestUser_v3_0_0)
            assert isinstance(api.hotspot_portal, HotspotPortal_v3_0_0)
            assert isinstance(api.identity_group, IdentityGroup_v3_0_0)
            assert isinstance(api.identity_store_sequence, IdentityStoreSequence_v3_0_0)
            assert isinstance(api.internal_user, InternalUser_v3_0_0)
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
            assert isinstance(api.pan_ha, PanHa_v3_0_0)
            assert isinstance(api.portal, Portal_v3_0_0)
            assert isinstance(api.portal_global_setting, PortalGlobalSetting_v3_0_0)
            assert isinstance(api.portal_theme, PortalTheme_v3_0_0)
            assert isinstance(api.radius_server_sequence, RadiusServerSequence_v3_0_0)
            assert isinstance(api.restid_store, RestidStore_v3_0_0)
            assert isinstance(api.replication_status, ReplicationStatus_v3_0_0)
            assert isinstance(api.repository, Repository_v3_0_0)
            assert isinstance(api.sg_acl, SgAcl_v3_0_0)
            assert isinstance(api.sgt, Sgt_v3_0_0)
            assert isinstance(api.sms_provider, SmsProvider_v3_0_0)
            assert isinstance(api.self_registered_portal, SelfRegisteredPortal_v3_0_0)
            assert isinstance(api.sponsor_group, SponsorGroup_v3_0_0)
            assert isinstance(api.sponsor_group_member, SponsorGroupMember_v3_0_0)
            assert isinstance(api.sponsor_portal, SponsorPortal_v3_0_0)
            assert isinstance(api.sponsored_guest_portal, SponsoredGuestPortal_v3_0_0)
            assert isinstance(api.sync_ise_node, SyncIseNode_v3_0_0)
            assert isinstance(api.tacacs_command_sets, TacacsCommandSets_v3_0_0)
            assert isinstance(api.tacacs_external_servers, TacacsExternalServers_v3_0_0)
            assert isinstance(api.tacacs_profile, TacacsProfile_v3_0_0)
            assert isinstance(api.tacacs_server_sequence, TacacsServerSequence_v3_0_0)
