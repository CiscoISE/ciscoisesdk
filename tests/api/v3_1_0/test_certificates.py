# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI certificates API fixtures and tests.

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

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.1.0', reason='version does not match')


def is_valid_get_csrs(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2eeef18d70b159f788b717e301dd3643_v3_1_0').validate(obj.response)
    return True


def get_csrs(api):
    endpoint_result = api.certificates.get_csrs(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_csrs(api, validator):
    try:
        assert is_valid_get_csrs(
            validator,
            get_csrs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_csrs_default(api):
    endpoint_result = api.certificates.get_csrs(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_csrs_default(api, validator):
    try:
        assert is_valid_get_csrs(
            validator,
            get_csrs_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_generate_csr(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_e39868ea7aec5efcaaf55009699eda5d_v3_1_0').validate(obj.response)
    return True


def generate_csr(api):
    endpoint_result = api.certificates.generate_csr(
        active_validation=False,
        allow_wild_card_cert=True,
        certificate_policies='string',
        digest_type='string',
        hostnames=['string'],
        key_length='string',
        key_type='string',
        payload=None,
        portal_group_tag='string',
        san_dir=['string'],
        san_dns=['string'],
        san_ip=['string'],
        san_uri=['string'],
        subject_city='string',
        subject_common_name='string',
        subject_country='string',
        subject_org='string',
        subject_org_unit='string',
        subject_state='string',
        used_for='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_generate_csr(api, validator):
    try:
        assert is_valid_generate_csr(
            validator,
            generate_csr(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def generate_csr_default(api):
    endpoint_result = api.certificates.generate_csr(
        active_validation=False,
        allow_wild_card_cert=None,
        certificate_policies=None,
        digest_type=None,
        hostnames=None,
        key_length=None,
        key_type=None,
        payload=None,
        portal_group_tag=None,
        san_dir=None,
        san_dns=None,
        san_ip=None,
        san_uri=None,
        subject_city=None,
        subject_common_name=None,
        subject_country=None,
        subject_org=None,
        subject_org_unit=None,
        subject_state=None,
        used_for=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_generate_csr_default(api, validator):
    try:
        assert is_valid_generate_csr(
            validator,
            generate_csr_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_csr(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'data')
    return True


def export_csr(api):
    endpoint_result = api.certificates.export_csr(
        dirpath=None,
        save_file=None,
        filename=None,
        hostname='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_export_csr(api, validator):
    try:
        assert is_valid_export_csr(
            validator,
            export_csr(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def export_csr_default(api):
    endpoint_result = api.certificates.export_csr(
        dirpath=None,
        save_file=None,
        filename=None,
        hostname='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_export_csr_default(api, validator):
    try:
        assert is_valid_export_csr(
            validator,
            export_csr_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_generate_intermediate_ca_csr(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bf95f099207a5b6599e04c47c22789c0_v3_1_0').validate(obj.response)
    return True


def generate_intermediate_ca_csr(api):
    endpoint_result = api.certificates.generate_intermediate_ca_csr(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_generate_intermediate_ca_csr(api, validator):
    try:
        assert is_valid_generate_intermediate_ca_csr(
            validator,
            generate_intermediate_ca_csr(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def generate_intermediate_ca_csr_default(api):
    endpoint_result = api.certificates.generate_intermediate_ca_csr(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_generate_intermediate_ca_csr_default(api, validator):
    try:
        assert is_valid_generate_intermediate_ca_csr(
            validator,
            generate_intermediate_ca_csr_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_csr_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_b8104a50fc565ae9a756d6d0152e0e5b_v3_1_0').validate(obj.response)
    return True


def get_csr_by_id(api):
    endpoint_result = api.certificates.get_csr_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_csr_by_id(api, validator):
    try:
        assert is_valid_get_csr_by_id(
            validator,
            get_csr_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_csr_by_id_default(api):
    endpoint_result = api.certificates.get_csr_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_csr_by_id_default(api, validator):
    try:
        assert is_valid_get_csr_by_id(
            validator,
            get_csr_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_csr_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_bf792ec664fa5202beb776556908b0c1_v3_1_0').validate(obj.response)
    return True


def delete_csr_by_id(api):
    endpoint_result = api.certificates.delete_csr_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_delete_csr_by_id(api, validator):
    try:
        assert is_valid_delete_csr_by_id(
            validator,
            delete_csr_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_csr_by_id_default(api):
    endpoint_result = api.certificates.delete_csr_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_delete_csr_by_id_default(api, validator):
    try:
        assert is_valid_delete_csr_by_id(
            validator,
            delete_csr_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_regenerate_ise_root_ca(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_18e6d1b224e058288a8c4d70be72c9a6_v3_1_0').validate(obj.response)
    return True


def regenerate_ise_root_ca(api):
    endpoint_result = api.certificates.regenerate_ise_root_ca(
        active_validation=False,
        payload=None,
        remove_existing_ise_intermediate_csr=True
    )
    return endpoint_result


@pytest.mark.certificates
def test_regenerate_ise_root_ca(api, validator):
    try:
        assert is_valid_regenerate_ise_root_ca(
            validator,
            regenerate_ise_root_ca(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def regenerate_ise_root_ca_default(api):
    endpoint_result = api.certificates.regenerate_ise_root_ca(
        active_validation=False,
        payload=None,
        remove_existing_ise_intermediate_csr=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_regenerate_ise_root_ca_default(api, validator):
    try:
        assert is_valid_regenerate_ise_root_ca(
            validator,
            regenerate_ise_root_ca_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_renew_certificates(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_254c288192f954309b4b35aa612ff226_v3_1_0').validate(obj.response)
    return True


def renew_certificates(api):
    endpoint_result = api.certificates.renew_certificates(
        active_validation=False,
        cert_type='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_renew_certificates(api, validator):
    try:
        assert is_valid_renew_certificates(
            validator,
            renew_certificates(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def renew_certificates_default(api):
    endpoint_result = api.certificates.renew_certificates(
        active_validation=False,
        cert_type=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_renew_certificates_default(api, validator):
    try:
        assert is_valid_renew_certificates(
            validator,
            renew_certificates_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bind_csr(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_2b94d7d3f0ed5d0b938151ae2cae9fa4_v3_1_0').validate(obj.response)
    return True


def bind_csr(api):
    endpoint_result = api.certificates.bind_csr(
        active_validation=False,
        admin=True,
        allow_extended_validity=True,
        allow_out_of_date_cert=True,
        allow_replacement_of_certificates=True,
        allow_replacement_of_portal_group_tag=True,
        data='string',
        eap=True,
        host_name='string',
        id='string',
        ims=True,
        name='string',
        payload=None,
        portal=True,
        portal_group_tag='string',
        pxgrid=True,
        radius=True,
        saml=True,
        validate_certificate_extensions=True
    )
    return endpoint_result


@pytest.mark.certificates
def test_bind_csr(api, validator):
    try:
        assert is_valid_bind_csr(
            validator,
            bind_csr(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def bind_csr_default(api):
    endpoint_result = api.certificates.bind_csr(
        active_validation=False,
        admin=None,
        allow_extended_validity=None,
        allow_out_of_date_cert=None,
        allow_replacement_of_certificates=None,
        allow_replacement_of_portal_group_tag=None,
        data=None,
        eap=None,
        host_name=None,
        id=None,
        ims=None,
        name=None,
        payload=None,
        portal=None,
        portal_group_tag=None,
        pxgrid=None,
        radius=None,
        saml=None,
        validate_certificate_extensions=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_bind_csr_default(api, validator):
    try:
        assert is_valid_bind_csr(
            validator,
            bind_csr_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_system_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'data')
    return True


def export_system_certificate(api):
    endpoint_result = api.certificates.export_system_certificate(
        dirpath=None,
        save_file=None,
        filename=None,
        active_validation=False,
        export='string',
        id='string',
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_export_system_certificate(api, validator):
    try:
        assert is_valid_export_system_certificate(
            validator,
            export_system_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def export_system_certificate_default(api):
    endpoint_result = api.certificates.export_system_certificate(
        dirpath=None,
        save_file=None,
        filename=None,
        active_validation=False,
        export=None,
        id=None,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_export_system_certificate_default(api, validator):
    try:
        assert is_valid_export_system_certificate(
            validator,
            export_system_certificate_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_system_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_517e6c7251a8508597f1b7ae61cbf953_v3_1_0').validate(obj.response)
    return True


def import_system_certificate(api):
    endpoint_result = api.certificates.import_system_certificate(
        active_validation=False,
        admin=True,
        allow_extended_validity=True,
        allow_out_of_date_cert=True,
        allow_replacement_of_certificates=True,
        allow_replacement_of_portal_group_tag=True,
        allow_sha1_certificates=True,
        allow_wild_card_certificates=True,
        data='string',
        eap=True,
        ims=True,
        name='string',
        password='string',
        payload=None,
        portal=True,
        portal_group_tag='string',
        portal_tag_transfer_for_same_subject=True,
        private_key_data='string',
        pxgrid=True,
        radius=True,
        role_transfer_for_same_subject=True,
        saml=True,
        validate_certificate_extensions=True
    )
    return endpoint_result


@pytest.mark.certificates
def test_import_system_certificate(api, validator):
    try:
        assert is_valid_import_system_certificate(
            validator,
            import_system_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def import_system_certificate_default(api):
    endpoint_result = api.certificates.import_system_certificate(
        active_validation=False,
        admin=None,
        allow_extended_validity=None,
        allow_out_of_date_cert=None,
        allow_replacement_of_certificates=None,
        allow_replacement_of_portal_group_tag=None,
        allow_sha1_certificates=None,
        allow_wild_card_certificates=None,
        data=None,
        eap=None,
        ims=None,
        name=None,
        password=None,
        payload=None,
        portal=None,
        portal_group_tag=None,
        portal_tag_transfer_for_same_subject=None,
        private_key_data=None,
        pxgrid=None,
        radius=None,
        role_transfer_for_same_subject=None,
        saml=None,
        validate_certificate_extensions=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_import_system_certificate_default(api, validator):
    try:
        assert is_valid_import_system_certificate(
            validator,
            import_system_certificate_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_system_certificates(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_662594a56f5c5f739a83e8806da16be5_v3_1_0').validate(obj.response)
    return True


def get_system_certificates(api):
    endpoint_result = api.certificates.get_system_certificates(
        filter='value1,value2',
        filter_type='string',
        host_name='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_system_certificates(api, validator):
    try:
        assert is_valid_get_system_certificates(
            validator,
            get_system_certificates(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_system_certificates_default(api):
    endpoint_result = api.certificates.get_system_certificates(
        host_name='string',
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_system_certificates_default(api, validator):
    try:
        assert is_valid_get_system_certificates(
            validator,
            get_system_certificates_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_system_certificate_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_3f36e90115b05416a71506061fed7e5c_v3_1_0').validate(obj.response)
    return True


def get_system_certificate_by_id(api):
    endpoint_result = api.certificates.get_system_certificate_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_system_certificate_by_id(api, validator):
    try:
        assert is_valid_get_system_certificate_by_id(
            validator,
            get_system_certificate_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_system_certificate_by_id_default(api):
    endpoint_result = api.certificates.get_system_certificate_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_system_certificate_by_id_default(api, validator):
    try:
        assert is_valid_get_system_certificate_by_id(
            validator,
            get_system_certificate_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_system_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_48fb9c22ad9a5eddb590c85abdab460b_v3_1_0').validate(obj.response)
    return True


def update_system_certificate(api):
    endpoint_result = api.certificates.update_system_certificate(
        active_validation=False,
        admin=True,
        allow_replacement_of_portal_group_tag=True,
        description='string',
        eap=True,
        expiration_ttl_period=0,
        expiration_ttl_units='string',
        host_name='string',
        id='string',
        ims=True,
        name='string',
        payload=None,
        portal=True,
        portal_group_tag='string',
        portal_tag_transfer_for_same_subject=True,
        pxgrid=True,
        radius=True,
        renew_self_signed_certificate=True,
        role_transfer_for_same_subject=True,
        saml=True
    )
    return endpoint_result


@pytest.mark.certificates
def test_update_system_certificate(api, validator):
    try:
        assert is_valid_update_system_certificate(
            validator,
            update_system_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_system_certificate_default(api):
    endpoint_result = api.certificates.update_system_certificate(
        active_validation=False,
        host_name='string',
        id='string',
        admin=None,
        allow_replacement_of_portal_group_tag=None,
        description=None,
        eap=None,
        expiration_ttl_period=None,
        expiration_ttl_units=None,
        ims=None,
        name=None,
        payload=None,
        portal=None,
        portal_group_tag=None,
        portal_tag_transfer_for_same_subject=None,
        pxgrid=None,
        radius=None,
        renew_self_signed_certificate=None,
        role_transfer_for_same_subject=None,
        saml=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_update_system_certificate_default(api, validator):
    try:
        assert is_valid_update_system_certificate(
            validator,
            update_system_certificate_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_system_certificate_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_35241dc2eec65ad680a3c5de47cd87c8_v3_1_0').validate(obj.response)
    return True


def delete_system_certificate_by_id(api):
    endpoint_result = api.certificates.delete_system_certificate_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_delete_system_certificate_by_id(api, validator):
    try:
        assert is_valid_delete_system_certificate_by_id(
            validator,
            delete_system_certificate_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_system_certificate_by_id_default(api):
    endpoint_result = api.certificates.delete_system_certificate_by_id(
        host_name='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_delete_system_certificate_by_id_default(api, validator):
    try:
        assert is_valid_delete_system_certificate_by_id(
            validator,
            delete_system_certificate_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trusted_certificates(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c654a18faf1b5571ac5ba61145d298c4_v3_1_0').validate(obj.response)
    return True


def get_trusted_certificates(api):
    endpoint_result = api.certificates.get_trusted_certificates(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sort='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_trusted_certificates(api, validator):
    try:
        assert is_valid_get_trusted_certificates(
            validator,
            get_trusted_certificates(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_trusted_certificates_default(api):
    endpoint_result = api.certificates.get_trusted_certificates(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sort=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_trusted_certificates_default(api, validator):
    try:
        assert is_valid_get_trusted_certificates(
            validator,
            get_trusted_certificates_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_trusted_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'data')
    return True


def export_trusted_certificate(api):
    endpoint_result = api.certificates.export_trusted_certificate(
        dirpath=None,
        save_file=None,
        filename=None,
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_export_trusted_certificate(api, validator):
    try:
        assert is_valid_export_trusted_certificate(
            validator,
            export_trusted_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def export_trusted_certificate_default(api):
    endpoint_result = api.certificates.export_trusted_certificate(
        dirpath=None,
        save_file=None,
        filename=None,
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_export_trusted_certificate_default(api, validator):
    try:
        assert is_valid_export_trusted_certificate(
            validator,
            export_trusted_certificate_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_import_trust_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c8cd2f618b655d988ce626e579486596_v3_1_0').validate(obj.response)
    return True


def import_trust_certificate(api):
    endpoint_result = api.certificates.import_trust_certificate(
        active_validation=False,
        allow_basic_constraint_cafalse=True,
        allow_out_of_date_cert=True,
        allow_sha1_certificates=True,
        data='string',
        description='string',
        name='string',
        payload=None,
        trust_for_certificate_based_admin_auth=True,
        trust_for_cisco_services_auth=True,
        trust_for_client_auth=True,
        trust_for_ise_auth=True,
        validate_certificate_extensions=True
    )
    return endpoint_result


@pytest.mark.certificates
def test_import_trust_certificate(api, validator):
    try:
        assert is_valid_import_trust_certificate(
            validator,
            import_trust_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def import_trust_certificate_default(api):
    endpoint_result = api.certificates.import_trust_certificate(
        active_validation=False,
        allow_basic_constraint_cafalse=None,
        allow_out_of_date_cert=None,
        allow_sha1_certificates=None,
        data=None,
        description=None,
        name=None,
        payload=None,
        trust_for_certificate_based_admin_auth=None,
        trust_for_cisco_services_auth=None,
        trust_for_client_auth=None,
        trust_for_ise_auth=None,
        validate_certificate_extensions=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_import_trust_certificate_default(api, validator):
    try:
        assert is_valid_import_trust_certificate(
            validator,
            import_trust_certificate_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trusted_certificate_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_1091757f8f4956d29b821fa9bbf23266_v3_1_0').validate(obj.response)
    return True


def get_trusted_certificate_by_id(api):
    endpoint_result = api.certificates.get_trusted_certificate_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_trusted_certificate_by_id(api, validator):
    try:
        assert is_valid_get_trusted_certificate_by_id(
            validator,
            get_trusted_certificate_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def get_trusted_certificate_by_id_default(api):
    endpoint_result = api.certificates.get_trusted_certificate_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_get_trusted_certificate_by_id_default(api, validator):
    try:
        assert is_valid_get_trusted_certificate_by_id(
            validator,
            get_trusted_certificate_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_trusted_certificate(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_239661cb625d5ad0ad76b93282f5818a_v3_1_0').validate(obj.response)
    return True


def update_trusted_certificate(api):
    endpoint_result = api.certificates.update_trusted_certificate(
        active_validation=False,
        authenticate_before_crl_received=True,
        automatic_crl_update=True,
        automatic_crl_update_period=0,
        automatic_crl_update_units='string',
        crl_distribution_url='string',
        crl_download_failure_retries=0,
        crl_download_failure_retries_units='string',
        description='string',
        download_crl=True,
        enable_ocsp_validation=True,
        enable_server_identity_check=True,
        id='string',
        ignore_crl_expiration=True,
        name='string',
        non_automatic_crl_update_period=0,
        non_automatic_crl_update_units='string',
        payload=None,
        reject_if_no_status_from_ocs_p=True,
        reject_if_unreachable_from_ocs_p=True,
        selected_ocsp_service='string',
        status='string',
        trust_for_certificate_based_admin_auth=True,
        trust_for_cisco_services_auth=True,
        trust_for_client_auth=True,
        trust_for_ise_auth=True
    )
    return endpoint_result


@pytest.mark.certificates
def test_update_trusted_certificate(api, validator):
    try:
        assert is_valid_update_trusted_certificate(
            validator,
            update_trusted_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def update_trusted_certificate_default(api):
    endpoint_result = api.certificates.update_trusted_certificate(
        active_validation=False,
        id='string',
        authenticate_before_crl_received=None,
        automatic_crl_update=None,
        automatic_crl_update_period=None,
        automatic_crl_update_units=None,
        crl_distribution_url=None,
        crl_download_failure_retries=None,
        crl_download_failure_retries_units=None,
        description=None,
        download_crl=None,
        enable_ocsp_validation=None,
        enable_server_identity_check=None,
        ignore_crl_expiration=None,
        name=None,
        non_automatic_crl_update_period=None,
        non_automatic_crl_update_units=None,
        payload=None,
        reject_if_no_status_from_ocs_p=None,
        reject_if_unreachable_from_ocs_p=None,
        selected_ocsp_service=None,
        status=None,
        trust_for_certificate_based_admin_auth=None,
        trust_for_cisco_services_auth=None,
        trust_for_client_auth=None,
        trust_for_ise_auth=None
    )
    return endpoint_result


@pytest.mark.certificates
def test_update_trusted_certificate_default(api, validator):
    try:
        assert is_valid_update_trusted_certificate(
            validator,
            update_trusted_certificate_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_trusted_certificate_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    assert hasattr(obj, 'status_code')
    json_schema_validate('jsd_c578ef80918b5d038024d126cd6e3b8d_v3_1_0').validate(obj.response)
    return True


def delete_trusted_certificate_by_id(api):
    endpoint_result = api.certificates.delete_trusted_certificate_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_delete_trusted_certificate_by_id(api, validator):
    try:
        assert is_valid_delete_trusted_certificate_by_id(
            validator,
            delete_trusted_certificate_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print("ERROR: {error}".format(error=original_e))
            raise original_e


def delete_trusted_certificate_by_id_default(api):
    endpoint_result = api.certificates.delete_trusted_certificate_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificates
def test_delete_trusted_certificate_by_id_default(api, validator):
    try:
        assert is_valid_delete_trusted_certificate_by_id(
            validator,
            delete_trusted_certificate_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
