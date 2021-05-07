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
from .v3_0_0.anc_policy import \
    AncPolicy as AncPolicy_v3_0_0
from .v3_0_0.active_directory import \
    ActiveDirectory as ActiveDirectory_v3_0_0
from .v3_0_0.allowed_protocols import \
    AllowedProtocols as AllowedProtocols_v3_0_0
from .v3_0_0.authorization_profile import \
    AuthorizationProfile as AuthorizationProfile_v3_0_0
from .v3_0_0.backup_and_restore import \
    BackupAndRestore as BackupAndRestore_v3_0_0
from .v3_0_0.certificates import \
    Certificates as Certificates_v3_0_0
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
from .v3_0_0.endpoint import \
    Endpoint as Endpoint_v3_0_0
from .v3_0_0.endpoint_group import \
    EndpointGroup as EndpointGroup_v3_0_0
from .v3_0_0.external_radius_server import \
    ExternalRadiusServer as ExternalRadiusServer_v3_0_0
from .v3_0_0.filter_policy import \
    FilterPolicy as FilterPolicy_v3_0_0
from .v3_0_0.guest_location import \
    GuestLocation as GuestLocation_v3_0_0
from .v3_0_0.guest_smtp_notifications import \
    GuestSmtpNotifications as GuestSmtpNotifications_v3_0_0
from .v3_0_0.guest_ssid import \
    GuestSsid as GuestSsid_v3_0_0
from .v3_0_0.guest_type import \
    GuestType as GuestType_v3_0_0
from .v3_0_0.guest_user import \
    GuestUser as GuestUser_v3_0_0
from .v3_0_0.hotspot_portal import \
    HotspotPortal as HotspotPortal_v3_0_0
from .v3_0_0.identity_group import \
    IdentityGroup as IdentityGroup_v3_0_0
from .v3_0_0.identity_store_sequence import \
    IdentityStoreSequence as IdentityStoreSequence_v3_0_0
from .v3_0_0.internal_user import \
    InternalUser as InternalUser_v3_0_0
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
from .v3_0_0.pan_ha import \
    PanHa as PanHa_v3_0_0
from .v3_0_0.portal import \
    Portal as Portal_v3_0_0
from .v3_0_0.portal_global_setting import \
    PortalGlobalSetting as PortalGlobalSetting_v3_0_0
from .v3_0_0.portal_theme import \
    PortalTheme as PortalTheme_v3_0_0
from .v3_0_0.radius_server_sequence import \
    RadiusServerSequence as RadiusServerSequence_v3_0_0
from .v3_0_0.restid_store import \
    RestidStore as RestidStore_v3_0_0
from .v3_0_0.replication_status import \
    ReplicationStatus as ReplicationStatus_v3_0_0
from .v3_0_0.sg_acl import \
    SgAcl as SgAcl_v3_0_0
from .v3_0_0.sgt import \
    Sgt as Sgt_v3_0_0
from .v3_0_0.sms_provider import \
    SmsProvider as SmsProvider_v3_0_0
from .v3_0_0.self_registered_portal import \
    SelfRegisteredPortal as SelfRegisteredPortal_v3_0_0
from .v3_0_0.sponsor_group import \
    SponsorGroup as SponsorGroup_v3_0_0
from .v3_0_0.sponsor_group_member import \
    SponsorGroupMember as SponsorGroupMember_v3_0_0
from .v3_0_0.sponsor_portal import \
    SponsorPortal as SponsorPortal_v3_0_0
from .v3_0_0.sponsored_guest_portal import \
    SponsoredGuestPortal as SponsoredGuestPortal_v3_0_0
from .v3_0_0.sync_ise_node import \
    SyncIseNode as SyncIseNode_v3_0_0
from .v3_0_0.tacacs_command_sets import \
    TacacsCommandSets as TacacsCommandSets_v3_0_0
from .v3_0_0.tacacs_external_servers import \
    TacacsExternalServers as TacacsExternalServers_v3_0_0
from .v3_0_0.tacacs_profile import \
    TacacsProfile as TacacsProfile_v3_0_0
from .v3_0_0.tacacs_server_sequence import \
    TacacsServerSequence as TacacsServerSequence_v3_0_0
from .custom_caller import CustomCaller


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
        This package supports two methods for you to generate the
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
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable or
                ciscoisesdk.config.DEFAULT_BASE_URL
                if the environment variable is not set.
            ui_base_url(basestring): The UI base URL to be prefixed to the
                individual ISE UI API endpoint suffixes.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            ers_base_url(basestring): The ERS base URL to be prefixed to the
                individual ISE ERS API endpoint suffixes.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            mnt_base_url(basestring): The MNT base URL to be prefixed to the
                individual ISE MNT API endpoint suffixes.
                Defaults to the IDENTITY_SERVICES_ENGINE_BASE_URL environment variable if set.
            px_grid_base_url(basestring): The PxGrid base URL to be prefixed to the
                individual ISE PxGrid API endpoint suffixes.
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
            validator(callable): The factory function to use to validate
                Python objects sent in the body of the request.

        Returns:
            IdentityServicesEngineAPI: A new IdentityServicesEngineAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.
            VersionError: If the version is not provided via the version
                argument or an environment variable, or it is not a
                Identity Services Engine API supported version
                ['3.0.0'].

        """
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)
        check_type(uses_api_gateway, (bool, basestring))
        check_type(debug, (bool, basestring), may_be_none=True)
        check_type(username, basestring, may_be_none=True)
        check_type(password, basestring, may_be_none=True)
        check_type(encoded_auth, basestring, may_be_none=True)
        check_type(verify, (bool, basestring), may_be_none=False)
        check_type(version, basestring, may_be_none=False)

        if uses_api_gateway:
            check_type(base_url, basestring, may_be_none=True)
        else:
            check_type(ui_base_url, basestring, may_be_none=True)
            check_type(ers_base_url, basestring, may_be_none=True)
            check_type(mnt_base_url, basestring, may_be_none=True)
            check_type(px_grid_base_url, basestring, may_be_none=True)

        if version not in ['3.0.0']:
            raise VersionError(
                'Unknown API version, '
                + 'known versions are {}'.format(
                    '3.0.0.'
                )
            )

        if isinstance(debug, str):
            debug = 'true' in debug.lower()

        if isinstance(uses_api_gateway, str):
            uses_api_gateway = 'true' in uses_api_gateway.lower()

        # Check if the user has provided the required basicAuth parameters
        if encoded_auth is None and (username is None or password is None):
            raise AccessTokenError(
                "You need an access token to interact with the Identity Services Engine"
                " APIs. Identity Services Engine uses HTTP Basic Auth to create an access"
                " token. You must provide the username and password or just"
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
        self._session = None
        self._session_main = None
        self._session_ui = None
        self._session_ers = None
        self._session_mnt = None
        self._session_px_grid = None
        if uses_api_gateway:
            self._session_main = RestSession(
                get_access_token=get_access_token,
                access_token=get_access_token(),
                base_url=base_url,
                single_request_timeout=single_request_timeout,
                wait_on_rate_limit=wait_on_rate_limit,
                verify=verify,
                version=version,
                debug=debug,
            )
            self._session = self._session_main
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
            self.anc_policy = \
                AncPolicy_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.active_directory = \
                ActiveDirectory_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.allowed_protocols = \
                AllowedProtocols_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.authorization_profile = \
                AuthorizationProfile_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.backup_and_restore = \
                BackupAndRestore_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.certificates = \
                Certificates_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_authentication_rules = \
                DeviceAdministrationAuthenticationRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_exception_rules = \
                DeviceAdministrationAuthorizationExceptionRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_global_exception_rules = \
                DeviceAdministrationAuthorizationGlobalExceptionRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_authorization_rules = \
                DeviceAdministrationAuthorizationRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_command_set = \
                DeviceAdministrationCommandSet_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_conditions = \
                DeviceAdministrationConditions_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_dictionary_attributes_list = \
                DeviceAdministrationDictionaryAttributesList_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_identity_stores = \
                DeviceAdministrationIdentityStores_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_network_conditions = \
                DeviceAdministrationNetworkConditions_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_policy_set = \
                DeviceAdministrationPolicySet_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_profiles = \
                DeviceAdministrationProfiles_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_service_names = \
                DeviceAdministrationServiceNames_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.device_administration_time_date_conditions = \
                DeviceAdministrationTimeDateConditions_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.downloadable_acl = \
                DownloadableAcl_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.egress_matrix_cell = \
                EgressMatrixCell_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.endpoint = \
                Endpoint_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.endpoint_group = \
                EndpointGroup_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.external_radius_server = \
                ExternalRadiusServer_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.filter_policy = \
                FilterPolicy_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.guest_location = \
                GuestLocation_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.guest_smtp_notifications = \
                GuestSmtpNotifications_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.guest_ssid = \
                GuestSsid_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.guest_type = \
                GuestType_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.guest_user = \
                GuestUser_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.hotspot_portal = \
                HotspotPortal_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.identity_group = \
                IdentityGroup_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.identity_store_sequence = \
                IdentityStoreSequence_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.internal_user = \
                InternalUser_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.network_access_authentication_rules = \
                NetworkAccessAuthenticationRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_exception_rules = \
                NetworkAccessAuthorizationExceptionRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_global_exception_rules = \
                NetworkAccessAuthorizationGlobalExceptionRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_authorization_rules = \
                NetworkAccessAuthorizationRules_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_conditions = \
                NetworkAccessConditions_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary = \
                NetworkAccessDictionary_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary_attribute = \
                NetworkAccessDictionaryAttribute_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_dictionary_attributes_list = \
                NetworkAccessDictionaryAttributesList_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_identity_stores = \
                NetworkAccessIdentityStores_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_network_conditions = \
                NetworkAccessNetworkConditions_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_policy_set = \
                NetworkAccessPolicySet_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_profiles = \
                NetworkAccessProfiles_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_security_groups = \
                NetworkAccessSecurityGroups_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_service_names = \
                NetworkAccessServiceNames_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_access_time_date_conditions = \
                NetworkAccessTimeDateConditions_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.network_device = \
                NetworkDevice_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.network_device_group = \
                NetworkDeviceGroup_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.node_deployment = \
                NodeDeployment_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.node_group = \
                NodeGroup_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.pan_ha = \
                PanHa_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.portal = \
                Portal_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.portal_global_setting = \
                PortalGlobalSetting_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.portal_theme = \
                PortalTheme_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.radius_server_sequence = \
                RadiusServerSequence_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.restid_store = \
                RestidStore_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.replication_status = \
                ReplicationStatus_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.sg_acl = \
                SgAcl_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.sgt = \
                Sgt_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.sms_provider = \
                SmsProvider_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.self_registered_portal = \
                SelfRegisteredPortal_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.sponsor_group = \
                SponsorGroup_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.sponsor_group_member = \
                SponsorGroupMember_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.sponsor_portal = \
                SponsorPortal_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.sponsored_guest_portal = \
                SponsoredGuestPortal_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.sync_ise_node = \
                SyncIseNode_v3_0_0(
                    self._session_main or self._session_ui, object_factory, _validator
                )
            self.tacacs_command_sets = \
                TacacsCommandSets_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.tacacs_external_servers = \
                TacacsExternalServers_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.tacacs_profile = \
                TacacsProfile_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
            self.tacacs_server_sequence = \
                TacacsServerSequence_v3_0_0(
                    self._session_main or self._session_ers, object_factory, _validator
                )
        self.custom_caller = \
            CustomCaller(self._session, object_factory)

    @property
    def uses_api_gateway(self):
        """The Identity Services Engine API uses_api_gateway."""
        return self._uses_api_gateway

    @property
    def session(self):
        """The Identity Services Engine API session."""
        return self._session

    @property
    def access_token(self):
        """The access token used for API calls to the Identity Services Engine service."""
        return self._session.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url

    @property
    def ui_base_url(self):
        """The ui base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url if self._uses_api_gateway else self._session_ui.base_url

    @property
    def ers_base_url(self):
        """The ers base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url if self._uses_api_gateway else self._session_ers.base_url

    @property
    def mnt_base_url(self):
        """The mnt base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url if self._uses_api_gateway else self._session_mnt.base_url

    @property
    def px_grid_base_url(self):
        """The px_grid base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url if self._uses_api_gateway else self._session_px_grid.base_url

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
        """The base URL for the API endpoints."""
        self._session.base_url = value

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """The timeout (seconds) for a single HTTP REST API request."""
        self.authentication.single_request_timeout = value
        self._session.single_request_timeout = value

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, value):
        """Enable or disable automatic rate-limit handling."""
        self._session.wait_on_rate_limit = value
