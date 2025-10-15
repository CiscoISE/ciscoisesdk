# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI activedirectory API fixtures and tests.

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
from fastjsonschema.exceptions import JsonSchemaException
from ciscoisesdk.exceptions import MalformedRequest
from ciscoisesdk.exceptions import ciscoisesdkException
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.5.0', reason='version does not match')


def is_valid_getalljoinpoints(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def getalljoinpoints(api):
    endpoint_result = api.activedirectory.getalljoinpoints(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getalljoinpoints(api, validator):
    try:
        assert is_valid_getalljoinpoints(
            validator,
            getalljoinpoints(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def getalljoinpoints_default(api):
    endpoint_result = api.activedirectory.getalljoinpoints(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getalljoinpoints_default(api, validator):
    try:
        assert is_valid_getalljoinpoints(
            validator,
            getalljoinpoints_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_getalljoinpoints_generator(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def getalljoinpoints_generator(api):
    endpoint_result = api.activedirectory.getalljoinpoints_generator(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getalljoinpoints_generator(api, validator):
    try:
        assert is_valid_getalljoinpoints_generator(
            validator,
            getalljoinpoints_generator(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def getalljoinpoints_generator_default(api):
    endpoint_result = api.activedirectory.getalljoinpoints_generator(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getalljoinpoints_generator_default(api, validator):
    try:
        assert is_valid_getalljoinpoints_generator(
            validator,
            getalljoinpoints_generator_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_createjoinpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def createjoinpoint(api):
    endpoint_result = api.activedirectory.createjoinpoint(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_createjoinpoint(api, validator):
    try:
        assert is_valid_createjoinpoint(
            validator,
            createjoinpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def createjoinpoint_default(api):
    endpoint_result = api.activedirectory.createjoinpoint(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_createjoinpoint_default(api, validator):
    try:
        assert is_valid_createjoinpoint(
            validator,
            createjoinpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updatespassive_idsettings(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def updatespassive_idsettings(api):
    endpoint_result = api.activedirectory.updatespassive_idsettings(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_updatespassive_idsettings(api, validator):
    try:
        assert is_valid_updatespassive_idsettings(
            validator,
            updatespassive_idsettings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def updatespassive_idsettings_default(api):
    endpoint_result = api.activedirectory.updatespassive_idsettings(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_updatespassive_idsettings_default(api, validator):
    try:
        assert is_valid_updatespassive_idsettings(
            validator,
            updatespassive_idsettings_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_loadgroupsfromdomain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def loadgroupsfromdomain(api):
    endpoint_result = api.activedirectory.loadgroupsfromdomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_loadgroupsfromdomain(api, validator):
    try:
        assert is_valid_loadgroupsfromdomain(
            validator,
            loadgroupsfromdomain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def loadgroupsfromdomain_default(api):
    endpoint_result = api.activedirectory.loadgroupsfromdomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_loadgroupsfromdomain_default(api, validator):
    try:
        assert is_valid_loadgroupsfromdomain(
            validator,
            loadgroupsfromdomain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_getusergroups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def getusergroups(api):
    endpoint_result = api.activedirectory.getusergroups(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getusergroups(api, validator):
    try:
        assert is_valid_getusergroups(
            validator,
            getusergroups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def getusergroups_default(api):
    endpoint_result = api.activedirectory.getusergroups(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getusergroups_default(api, validator):
    try:
        assert is_valid_getusergroups(
            validator,
            getusergroups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def get_by_name(api):
    endpoint_result = api.activedirectory.get_by_name(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_get_by_name(api, validator):
    try:
        assert is_valid_get_by_name(
            validator,
            get_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_by_name_default(api):
    endpoint_result = api.activedirectory.get_by_name(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_get_by_name_default(api, validator):
    try:
        assert is_valid_get_by_name(
            validator,
            get_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gettrusteddomains(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def gettrusteddomains(api):
    endpoint_result = api.activedirectory.gettrusteddomains(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_gettrusteddomains(api, validator):
    try:
        assert is_valid_gettrusteddomains(
            validator,
            gettrusteddomains(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def gettrusteddomains_default(api):
    endpoint_result = api.activedirectory.gettrusteddomains(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_gettrusteddomains_default(api, validator):
    try:
        assert is_valid_gettrusteddomains(
            validator,
            gettrusteddomains_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_leaveadomainwithallnodes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def leaveadomainwithallnodes(api):
    endpoint_result = api.activedirectory.leaveadomainwithallnodes(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_leaveadomainwithallnodes(api, validator):
    try:
        assert is_valid_leaveadomainwithallnodes(
            validator,
            leaveadomainwithallnodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def leaveadomainwithallnodes_default(api):
    endpoint_result = api.activedirectory.leaveadomainwithallnodes(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_leaveadomainwithallnodes_default(api, validator):
    try:
        assert is_valid_leaveadomainwithallnodes(
            validator,
            leaveadomainwithallnodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_joinadomain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def joinadomain(api):
    endpoint_result = api.activedirectory.joinadomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_joinadomain(api, validator):
    try:
        assert is_valid_joinadomain(
            validator,
            joinadomain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def joinadomain_default(api):
    endpoint_result = api.activedirectory.joinadomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_joinadomain_default(api, validator):
    try:
        assert is_valid_joinadomain(
            validator,
            joinadomain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_joinadomainwithallnodes(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def joinadomainwithallnodes(api):
    endpoint_result = api.activedirectory.joinadomainwithallnodes(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_joinadomainwithallnodes(api, validator):
    try:
        assert is_valid_joinadomainwithallnodes(
            validator,
            joinadomainwithallnodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def joinadomainwithallnodes_default(api):
    endpoint_result = api.activedirectory.joinadomainwithallnodes(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_joinadomainwithallnodes_default(api, validator):
    try:
        assert is_valid_joinadomainwithallnodes(
            validator,
            joinadomainwithallnodes_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_getdomainusers(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def getdomainusers(api):
    endpoint_result = api.activedirectory.getdomainusers(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getdomainusers(api, validator):
    try:
        assert is_valid_getdomainusers(
            validator,
            getdomainusers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def getdomainusers_default(api):
    endpoint_result = api.activedirectory.getdomainusers(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getdomainusers_default(api, validator):
    try:
        assert is_valid_getdomainusers(
            validator,
            getdomainusers_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_isuseramemberofgroups(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def isuseramemberofgroups(api):
    endpoint_result = api.activedirectory.isuseramemberofgroups(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_isuseramemberofgroups(api, validator):
    try:
        assert is_valid_isuseramemberofgroups(
            validator,
            isuseramemberofgroups(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def isuseramemberofgroups_default(api):
    endpoint_result = api.activedirectory.isuseramemberofgroups(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_isuseramemberofgroups_default(api, validator):
    try:
        assert is_valid_isuseramemberofgroups(
            validator,
            isuseramemberofgroups_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_getgroupsbydomain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def getgroupsbydomain(api):
    endpoint_result = api.activedirectory.getgroupsbydomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getgroupsbydomain(api, validator):
    try:
        assert is_valid_getgroupsbydomain(
            validator,
            getgroupsbydomain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def getgroupsbydomain_default(api):
    endpoint_result = api.activedirectory.getgroupsbydomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getgroupsbydomain_default(api, validator):
    try:
        assert is_valid_getgroupsbydomain(
            validator,
            getgroupsbydomain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_getjoinpointdetails(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def getjoinpointdetails(api):
    endpoint_result = api.activedirectory.getjoinpointdetails(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getjoinpointdetails(api, validator):
    try:
        assert is_valid_getjoinpointdetails(
            validator,
            getjoinpointdetails(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def getjoinpointdetails_default(api):
    endpoint_result = api.activedirectory.getjoinpointdetails(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_getjoinpointdetails_default(api, validator):
    try:
        assert is_valid_getjoinpointdetails(
            validator,
            getjoinpointdetails_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletejoinpoint(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def deletejoinpoint(api):
    endpoint_result = api.activedirectory.deletejoinpoint(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_deletejoinpoint(api, validator):
    try:
        assert is_valid_deletejoinpoint(
            validator,
            deletejoinpoint(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def deletejoinpoint_default(api):
    endpoint_result = api.activedirectory.deletejoinpoint(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_deletejoinpoint_default(api, validator):
    try:
        assert is_valid_deletejoinpoint(
            validator,
            deletejoinpoint_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_leaveadomain(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    return True


def leaveadomain(api):
    endpoint_result = api.activedirectory.leaveadomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_leaveadomain(api, validator):
    try:
        assert is_valid_leaveadomain(
            validator,
            leaveadomain(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def leaveadomain_default(api):
    endpoint_result = api.activedirectory.leaveadomain(
    )
    return endpoint_result


@pytest.mark.activedirectory
def test_leaveadomain_default(api, validator):
    try:
        assert is_valid_leaveadomain(
            validator,
            leaveadomain_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


