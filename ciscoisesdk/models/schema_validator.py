# -*- coding: utf-8 -*-
"""Validates Identity Services Engine JSON request objects.

Classes:
    SchemaValidator: Validates Identity Services Engine JSON request objects.

The SchemaValidator class validates any dict structure passed by
the user with the JSON schema of the request.

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

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *
import json

import fastjsonschema
from ciscoisesdk.exceptions import MalformedRequest

from .validators.v3_0_0.jsd_f2fcf04554db9ea4cdc3a7024322 \
    import JSONSchemaValidatorF2FcF04554Db9Ea4Cdc3A7024322 \
    as JSONSchemaValidatorF2FcF04554Db9Ea4Cdc3A7024322_v3_0_0
from .validators.v3_0_0.jsd_de7c6f75f68b0d7df00dc72808d \
    import JSONSchemaValidatorDe7C6F75F68B0D7Df00Dc72808D \
    as JSONSchemaValidatorDe7C6F75F68B0D7Df00Dc72808D_v3_0_0
from .validators.v3_0_0.jsd_eb42e79d5cc38bd1a6eef20613d6 \
    import JSONSchemaValidatorEb42E79D5Cc38Bd1A6Eef20613D6 \
    as JSONSchemaValidatorEb42E79D5Cc38Bd1A6Eef20613D6_v3_0_0
from .validators.v3_0_0.jsd_db1d9dda53369e35d33138b29c16 \
    import JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16 \
    as JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16_v3_0_0
from .validators.v3_0_0.jsd_ae4af25df565334b20a24c4878b68e4 \
    import JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4 \
    as JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4_v3_0_0
from .validators.v3_0_0.jsd_d39172f68fd5cbd897f03f1440f98a4 \
    import JSONSchemaValidatorD39172F68Fd5Cbd897F03F1440F98A4 \
    as JSONSchemaValidatorD39172F68Fd5Cbd897F03F1440F98A4_v3_0_0
from .validators.v3_0_0.jsd_df78c9a3f72584dbd1c7b667b0e312f \
    import JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F \
    as JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F_v3_0_0
from .validators.v3_0_0.jsd_c23243c950f29b51f502c03d7058 \
    import JSONSchemaValidatorC23243C950F29B51F502C03D7058 \
    as JSONSchemaValidatorC23243C950F29B51F502C03D7058_v3_0_0
from .validators.v3_0_0.jsd_a518d5655f69e8687c9c98740c6 \
    import JSONSchemaValidatorA518D5655F69E8687C9C98740C6 \
    as JSONSchemaValidatorA518D5655F69E8687C9C98740C6_v3_0_0
from .validators.v3_0_0.jsd_c45ba035019803dacdbf15cf193 \
    import JSONSchemaValidatorC45Ba035019803DAcdbf15Cf193 \
    as JSONSchemaValidatorC45Ba035019803DAcdbf15Cf193_v3_0_0
from .validators.v3_0_0.jsd_ca61ff725fedb94fba602d7afe46 \
    import JSONSchemaValidatorCa61Ff725FedB94FBa602D7Afe46 \
    as JSONSchemaValidatorCa61Ff725FedB94FBa602D7Afe46_v3_0_0
from .validators.v3_0_0.jsd_ebcdc835e9b8d6844c1da6cf252 \
    import JSONSchemaValidatorEbcDc835E9B8D6844C1Da6Cf252 \
    as JSONSchemaValidatorEbcDc835E9B8D6844C1Da6Cf252_v3_0_0
from .validators.v3_0_0.jsd_b05e80058df96e685baa727d578 \
    import JSONSchemaValidatorB05E80058Df96E685Baa727D578 \
    as JSONSchemaValidatorB05E80058Df96E685Baa727D578_v3_0_0
from .validators.v3_0_0.jsd_b4e8d45639975c226dacd53e7b \
    import JSONSchemaValidatorB4E8D45639975C226Dacd53E7B \
    as JSONSchemaValidatorB4E8D45639975C226Dacd53E7B_v3_0_0
from .validators.v3_0_0.jsd_e6d1b224e058288a8c4d70be72c9a6 \
    import JSONSchemaValidatorE6D1B224E058288A8C4D70Be72C9A6 \
    as JSONSchemaValidatorE6D1B224E058288A8C4D70Be72C9A6_v3_0_0
from .validators.v3_0_0.jsd_b40ad23ab0a5a7b8adade320c8912e7 \
    import JSONSchemaValidatorB40Ad23Ab0A5A7B8AdaDe320C8912E7 \
    as JSONSchemaValidatorB40Ad23Ab0A5A7B8AdaDe320C8912E7_v3_0_0
from .validators.v3_0_0.jsd_c0689e940ba5526946ad15976cc3365 \
    import JSONSchemaValidatorC0689E940Ba5526946AD15976Cc3365 \
    as JSONSchemaValidatorC0689E940Ba5526946AD15976Cc3365_v3_0_0
from .validators.v3_0_0.jsd_d0290eb241f5bd79221afc8d6cb32da \
    import JSONSchemaValidatorD0290Eb241F5Bd79221Afc8D6Cb32Da \
    as JSONSchemaValidatorD0290Eb241F5Bd79221Afc8D6Cb32Da_v3_0_0
from .validators.v3_0_0.jsd_d79b507bda155c180d42f0a67ef64d5 \
    import JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5 \
    as JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5_v3_0_0
from .validators.v3_0_0.jsd_dbe47028859573988880de76fec0936 \
    import JSONSchemaValidatorDbe47028859573988880De76Fec0936 \
    as JSONSchemaValidatorDbe47028859573988880De76Fec0936_v3_0_0
from .validators.v3_0_0.jsd_fc1c74b35ae5050b4f7fd702570ad5b \
    import JSONSchemaValidatorFc1C74B35Ae5050B4F7Fd702570Ad5B \
    as JSONSchemaValidatorFc1C74B35Ae5050B4F7Fd702570Ad5B_v3_0_0
from .validators.v3_0_0.jsd_f8082b07ce528f82545e210b84d7de \
    import JSONSchemaValidatorF8082B07Ce528F82545E210B84D7De \
    as JSONSchemaValidatorF8082B07Ce528F82545E210B84D7De_v3_0_0
from .validators.v3_0_0.jsd_cb625d5ad0ad76b93282f5818a \
    import JSONSchemaValidatorCb625D5Ad0Ad76B93282F5818A \
    as JSONSchemaValidatorCb625D5Ad0Ad76B93282F5818A_v3_0_0
from .validators.v3_0_0.jsd_f78898b7d655b2b81085dc7c0a964e \
    import JSONSchemaValidatorF78898B7D655B2B81085Dc7C0A964E \
    as JSONSchemaValidatorF78898B7D655B2B81085Dc7C0A964E_v3_0_0
from .validators.v3_0_0.jsd_c288192f954309b4b35aa612ff226 \
    import JSONSchemaValidatorC288192F954309B4B35Aa612Ff226 \
    as JSONSchemaValidatorC288192F954309B4B35Aa612Ff226_v3_0_0
from .validators.v3_0_0.jsd_a4d5b5da6a50bfaaecc180543fd952 \
    import JSONSchemaValidatorA4D5B5Da6A50BfAaecC180543Fd952 \
    as JSONSchemaValidatorA4D5B5Da6A50BfAaecC180543Fd952_v3_0_0
from .validators.v3_0_0.jsd_a99695fd5ee0b00efce79a5761ff \
    import JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff \
    as JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff_v3_0_0
from .validators.v3_0_0.jsd_da0a59db7654cfa89df49ca3ac3414 \
    import JSONSchemaValidatorDa0A59Db7654CfA89DF49Ca3Ac3414 \
    as JSONSchemaValidatorDa0A59Db7654CfA89DF49Ca3Ac3414_v3_0_0
from .validators.v3_0_0.jsd_a31eb33e3535754b3f754a9199e0d25 \
    import JSONSchemaValidatorA31Eb33E3535754B3F754A9199E0D25 \
    as JSONSchemaValidatorA31Eb33E3535754B3F754A9199E0D25_v3_0_0
from .validators.v3_0_0.jsd_acfdb4060de5a1895b383238c205986 \
    import JSONSchemaValidatorAcfdb4060De5A1895B383238C205986 \
    as JSONSchemaValidatorAcfdb4060De5A1895B383238C205986_v3_0_0
from .validators.v3_0_0.jsd_b94d7d3f0ed5d0b938151ae2cae9fa4 \
    import JSONSchemaValidatorB94D7D3F0Ed5D0B938151Ae2Cae9Fa4 \
    as JSONSchemaValidatorB94D7D3F0Ed5D0B938151Ae2Cae9Fa4_v3_0_0
from .validators.v3_0_0.jsd_b994e6c8b8d53f29230686824c9fafa \
    import JSONSchemaValidatorB994E6C8B8D53F29230686824C9Fafa \
    as JSONSchemaValidatorB994E6C8B8D53F29230686824C9Fafa_v3_0_0
from .validators.v3_0_0.jsd_d8c7ba0cb8f56d99135e16d2d973d11 \
    import JSONSchemaValidatorD8C7Ba0Cb8F56D99135E16D2D973D11 \
    as JSONSchemaValidatorD8C7Ba0Cb8F56D99135E16D2D973D11_v3_0_0
from .validators.v3_0_0.jsd_ea2c4586b845888b2a9375126f70de2 \
    import JSONSchemaValidatorEa2C4586B845888B2A9375126F70De2 \
    as JSONSchemaValidatorEa2C4586B845888B2A9375126F70De2_v3_0_0
from .validators.v3_0_0.jsd_eb3472c4de150828b2dae61e2285313 \
    import JSONSchemaValidatorEb3472C4De150828B2DAe61E2285313 \
    as JSONSchemaValidatorEb3472C4De150828B2DAe61E2285313_v3_0_0
from .validators.v3_0_0.jsd_edfca30e8e514d9bab840c3c2d4c0f \
    import JSONSchemaValidatorEdfca30E8E514D9Bab840C3C2D4C0F \
    as JSONSchemaValidatorEdfca30E8E514D9Bab840C3C2D4C0F_v3_0_0
from .validators.v3_0_0.jsd_c5c9b7ab72b5442ae7026a5dcc0fec3 \
    import JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3 \
    as JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3_v3_0_0
from .validators.v3_0_0.jsd_fd9e7e03a6056d1b6e9705e3096d946 \
    import JSONSchemaValidatorFd9E7E03A6056D1B6E9705E3096D946 \
    as JSONSchemaValidatorFd9E7E03A6056D1B6E9705E3096D946_v3_0_0
from .validators.v3_0_0.jsd_c4fada6c558d9aba09cc373d5b266 \
    import JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266 \
    as JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0
from .validators.v3_0_0.jsd_b11e2f1af656bcb5880a7b33720ec5 \
    import JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5 \
    as JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0
from .validators.v3_0_0.jsd_ce666e64a958229cfd8da70945935e \
    import JSONSchemaValidatorCe666E64A958229Cfd8Da70945935E \
    as JSONSchemaValidatorCe666E64A958229Cfd8Da70945935E_v3_0_0
from .validators.v3_0_0.jsd_19d9509db339e3b27dc56b37 \
    import JSONSchemaValidator19D9509DB339E3B27Dc56B37 \
    as JSONSchemaValidator19D9509DB339E3B27Dc56B37_v3_0_0
from .validators.v3_0_0.jsd_fb9c22ad9a5eddb590c85abdab460b \
    import JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B \
    as JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B_v3_0_0
from .validators.v3_0_0.jsd_fd729f50e65695966359b589a1606b \
    import JSONSchemaValidatorFd729F50E65695966359B589A1606B \
    as JSONSchemaValidatorFd729F50E65695966359B589A1606B_v3_0_0
from .validators.v3_0_0.jsd_cf65cd559628b26f6eb5ea20f14 \
    import JSONSchemaValidatorCf65Cd559628B26F6Eb5Ea20F14 \
    as JSONSchemaValidatorCf65Cd559628B26F6Eb5Ea20F14_v3_0_0
from .validators.v3_0_0.jsd_d67f9f6fba65dcbbcf64ca3e31b39a6 \
    import JSONSchemaValidatorD67F9F6Fba65DcbBcf64Ca3E31B39A6 \
    as JSONSchemaValidatorD67F9F6Fba65DcbBcf64Ca3E31B39A6_v3_0_0
from .validators.v3_0_0.jsd_e6c7251a8508597f1b7ae61cbf953 \
    import JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953 \
    as JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953_v3_0_0
from .validators.v3_0_0.jsd_a03a30be865ca599e77c63a332978b \
    import JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B \
    as JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B_v3_0_0
from .validators.v3_0_0.jsd_ca6ab8ec556c3bc9531dc380b230a \
    import JSONSchemaValidatorCa6Ab8Ec556C3Bc9531Dc380B230A \
    as JSONSchemaValidatorCa6Ab8Ec556C3Bc9531Dc380B230A_v3_0_0
from .validators.v3_0_0.jsd_ad69fa1d850f4993bbfc888749fa0 \
    import JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0 \
    as JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0
from .validators.v3_0_0.jsd_bf19f653f9a5c48d1fb1890409 \
    import JSONSchemaValidatorBf19F653F9A5C48D1Fb1890409 \
    as JSONSchemaValidatorBf19F653F9A5C48D1Fb1890409_v3_0_0
from .validators.v3_0_0.jsd_abc25887a5daab1216195e08cbd49 \
    import JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49 \
    as JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49_v3_0_0
from .validators.v3_0_0.jsd_d1e1fc98a5588b8bbdda06c4fc012 \
    import JSONSchemaValidatorD1E1FC98A5588B8BbDda06C4Fc012 \
    as JSONSchemaValidatorD1E1FC98A5588B8BbDda06C4Fc012_v3_0_0
from .validators.v3_0_0.jsd_c6536d17325c84a54189f46d4bbad2 \
    import JSONSchemaValidatorC6536D17325C84A54189F46D4Bbad2 \
    as JSONSchemaValidatorC6536D17325C84A54189F46D4Bbad2_v3_0_0
from .validators.v3_0_0.jsd_c475afd2a5e57e4bd0952f2c5349c6c \
    import JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C \
    as JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C_v3_0_0
from .validators.v3_0_0.jsd_a0b312f70257b1bfa90d0260f0c971 \
    import JSONSchemaValidatorA0B312F70257B1Bfa90D0260F0C971 \
    as JSONSchemaValidatorA0B312F70257B1Bfa90D0260F0C971_v3_0_0
from .validators.v3_0_0.jsd_b2eebd5c245e58a503aa53115eec53 \
    import JSONSchemaValidatorB2Eebd5C245E58A503Aa53115Eec53 \
    as JSONSchemaValidatorB2Eebd5C245E58A503Aa53115Eec53_v3_0_0
from .validators.v3_0_0.jsd_c560004d8b5f64a10f2cc070368c12 \
    import JSONSchemaValidatorC560004D8B5F64A10F2Cc070368C12 \
    as JSONSchemaValidatorC560004D8B5F64A10F2Cc070368C12_v3_0_0
from .validators.v3_0_0.jsd_e9318040a456978757d7abfa3e66b1 \
    import JSONSchemaValidatorE9318040A456978757D7Abfa3E66B1 \
    as JSONSchemaValidatorE9318040A456978757D7Abfa3E66B1_v3_0_0
from .validators.v3_0_0.jsd_c1fa3bf115c77be99b602aca1493b \
    import JSONSchemaValidatorC1Fa3Bf115C77Be99B602Aca1493B \
    as JSONSchemaValidatorC1Fa3Bf115C77Be99B602Aca1493B_v3_0_0
from .validators.v3_0_0.jsd_c38fb2e2dd45f4dab6ec3a19effd15a \
    import JSONSchemaValidatorC38Fb2E2Dd45F4DAb6EC3A19Effd15A \
    as JSONSchemaValidatorC38Fb2E2Dd45F4DAb6EC3A19Effd15A_v3_0_0
from .validators.v3_0_0.jsd_cc0a87094bf5d96af61403dfc3747db \
    import JSONSchemaValidatorCc0A87094Bf5D96Af61403Dfc3747Db \
    as JSONSchemaValidatorCc0A87094Bf5D96Af61403Dfc3747Db_v3_0_0
from .validators.v3_0_0.jsd_ee1780a38a85d1ba57c9a38e1093721 \
    import JSONSchemaValidatorEe1780A38A85D1BA57C9A38E1093721 \
    as JSONSchemaValidatorEe1780A38A85D1BA57C9A38E1093721_v3_0_0
from .validators.v3_0_0.jsd_f4508bb3352ff920dbdc229e0fc50 \
    import JSONSchemaValidatorF4508Bb3352Ff920DBdc229E0Fc50 \
    as JSONSchemaValidatorF4508Bb3352Ff920DBdc229E0Fc50_v3_0_0
from .validators.v3_0_0.jsd_e6e4b7d022556a80f1948efb3d5c61 \
    import JSONSchemaValidatorE6E4B7D022556A80F1948Efb3D5C61 \
    as JSONSchemaValidatorE6E4B7D022556A80F1948Efb3D5C61_v3_0_0
from .validators.v3_0_0.jsd_eca5db5147b1e3b35a032ced4b \
    import JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B \
    as JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B_v3_0_0
from .validators.v3_0_0.jsd_f7bd03a835c95b7a759b39ce7f680 \
    import JSONSchemaValidatorF7Bd03A835C95B7A759B39Ce7F680 \
    as JSONSchemaValidatorF7Bd03A835C95B7A759B39Ce7F680_v3_0_0
from .validators.v3_0_0.jsd_b314d32b258a1b53c5c84cf84d396 \
    import JSONSchemaValidatorB314D32B258A1B53C5C84Cf84D396 \
    as JSONSchemaValidatorB314D32B258A1B53C5C84Cf84D396_v3_0_0
from .validators.v3_0_0.jsd_da250e23ac05e6a8dcf32a81effcee9 \
    import JSONSchemaValidatorDa250E23Ac05E6A8Dcf32A81Effcee9 \
    as JSONSchemaValidatorDa250E23Ac05E6A8Dcf32A81Effcee9_v3_0_0
from .validators.v3_0_0.jsd_e6734850fabb2097fa969948cb \
    import JSONSchemaValidatorE6734850FaBb2097Fa969948Cb \
    as JSONSchemaValidatorE6734850FaBb2097Fa969948Cb_v3_0_0
from .validators.v3_0_0.jsd_e84541805d1da1fa3d4d581102a9 \
    import JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9 \
    as JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9_v3_0_0
from .validators.v3_0_0.jsd_ad6ca0642c5750af6ca9905721a9d7 \
    import JSONSchemaValidatorAd6Ca0642C5750Af6CA9905721A9D7 \
    as JSONSchemaValidatorAd6Ca0642C5750Af6CA9905721A9D7_v3_0_0
from .validators.v3_0_0.jsd_ab88be5092bf4ba9f522e8e26f \
    import JSONSchemaValidatorAb88Be5092Bf4BA9F522E8E26F \
    as JSONSchemaValidatorAb88Be5092Bf4BA9F522E8E26F_v3_0_0
from .validators.v3_0_0.jsd_b9c7c5847b17684c49399ff95 \
    import JSONSchemaValidatorB9C7C5847B17684C49399Ff95 \
    as JSONSchemaValidatorB9C7C5847B17684C49399Ff95_v3_0_0
from .validators.v3_0_0.jsd_a57687cef65891a6f48dd17f456c4e \
    import JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E \
    as JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E_v3_0_0
from .validators.v3_0_0.jsd_f7cf06a1655d6da606ace9b0950bcf \
    import JSONSchemaValidatorF7Cf06A1655D6DA606Ace9B0950Bcf \
    as JSONSchemaValidatorF7Cf06A1655D6DA606Ace9B0950Bcf_v3_0_0
from .validators.v3_0_0.jsd_eb833980f55025bfacbfcb8de814c8 \
    import JSONSchemaValidatorEb833980F55025BfacBfcb8De814C8 \
    as JSONSchemaValidatorEb833980F55025BfacBfcb8De814C8_v3_0_0
from .validators.v3_0_0.jsd_d0006cc03d53c89a3593526bf8dc0f \
    import JSONSchemaValidatorD0006CC03D53C89A3593526Bf8Dc0F \
    as JSONSchemaValidatorD0006CC03D53C89A3593526Bf8Dc0F_v3_0_0
from .validators.v3_0_0.jsd_a4cccea3c9567498f6f688e0cf86e7 \
    import JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7 \
    as JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7_v3_0_0
from .validators.v3_0_0.jsd_a9fa9cbccbe50fcb1cd6a63fed47578 \
    import JSONSchemaValidatorA9Fa9CbCcbe50FcB1Cd6A63Fed47578 \
    as JSONSchemaValidatorA9Fa9CbCcbe50FcB1Cd6A63Fed47578_v3_0_0
from .validators.v3_0_0.jsd_ab61f24bdaf508590f7686e1130913f \
    import JSONSchemaValidatorAb61F24Bdaf508590F7686E1130913F \
    as JSONSchemaValidatorAb61F24Bdaf508590F7686E1130913F_v3_0_0
from .validators.v3_0_0.jsd_c316d5e2fdd51bdab039ea9e2a417bd \
    import JSONSchemaValidatorC316D5E2Fdd51BdAb039Ea9E2A417Bd \
    as JSONSchemaValidatorC316D5E2Fdd51BdAb039Ea9E2A417Bd_v3_0_0
from .validators.v3_0_0.jsd_c43118f80d4556a8ec759a8c41e2097 \
    import JSONSchemaValidatorC43118F80D4556A8Ec759A8C41E2097 \
    as JSONSchemaValidatorC43118F80D4556A8Ec759A8C41E2097_v3_0_0
from .validators.v3_0_0.jsd_cb9f26e93655e7d89995b172f6fd97f \
    import JSONSchemaValidatorCb9F26E93655E7D89995B172F6Fd97F \
    as JSONSchemaValidatorCb9F26E93655E7D89995B172F6Fd97F_v3_0_0
from .validators.v3_0_0.jsd_dfe1db8729d541fb3a17d31d47d1881 \
    import JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881 \
    as JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881_v3_0_0
from .validators.v3_0_0.jsd_ed5bf99062d5dee87fe5cd96e360ec2 \
    import JSONSchemaValidatorEd5Bf99062D5Dee87Fe5Cd96E360Ec2 \
    as JSONSchemaValidatorEd5Bf99062D5Dee87Fe5Cd96E360Ec2_v3_0_0
from .validators.v3_0_0.jsd_a22b2304dcc855abb2a298de6ecddb65 \
    import JSONSchemaValidatorA22B2304Dcc855AbB2A298De6Ecddb65 \
    as JSONSchemaValidatorA22B2304Dcc855AbB2A298De6Ecddb65_v3_0_0
from .validators.v3_0_0.jsd_a60b29bfe2b055299e4360d84380ddd4 \
    import JSONSchemaValidatorA60B29BfE2B055299E4360D84380Ddd4 \
    as JSONSchemaValidatorA60B29BfE2B055299E4360D84380Ddd4_v3_0_0
from .validators.v3_0_0.jsd_a7500f6e473a50e19452683e303dd021 \
    import JSONSchemaValidatorA7500F6E473A50E19452683E303Dd021 \
    as JSONSchemaValidatorA7500F6E473A50E19452683E303Dd021_v3_0_0
from .validators.v3_0_0.jsd_a87d60d590485830aed781bfb15b5c95 \
    import JSONSchemaValidatorA87D60D590485830Aed781Bfb15B5C95 \
    as JSONSchemaValidatorA87D60D590485830Aed781Bfb15B5C95_v3_0_0
from .validators.v3_0_0.jsd_aa333658bf83576eb36a025283516518 \
    import JSONSchemaValidatorAa333658Bf83576EB36A025283516518 \
    as JSONSchemaValidatorAa333658Bf83576EB36A025283516518_v3_0_0
from .validators.v3_0_0.jsd_aa4daefaa3b95ecca521188a43eacbd9 \
    import JSONSchemaValidatorAa4DaefaA3B95EccA521188A43Eacbd9 \
    as JSONSchemaValidatorAa4DaefaA3B95EccA521188A43Eacbd9_v3_0_0
from .validators.v3_0_0.jsd_ac171b8ccf79502fbc4b35909970a1cb \
    import JSONSchemaValidatorAc171B8CCf79502FBc4B35909970A1Cb \
    as JSONSchemaValidatorAc171B8CCf79502FBc4B35909970A1Cb_v3_0_0
from .validators.v3_0_0.jsd_adcf947c42fe5588b7b82d9c43a3bbf0 \
    import JSONSchemaValidatorAdcf947C42Fe5588B7B82D9C43A3Bbf0 \
    as JSONSchemaValidatorAdcf947C42Fe5588B7B82D9C43A3Bbf0_v3_0_0
from .validators.v3_0_0.jsd_afc81cd1e25c50319f75606b97c23b3d \
    import JSONSchemaValidatorAfc81Cd1E25C50319F75606B97C23B3D \
    as JSONSchemaValidatorAfc81Cd1E25C50319F75606B97C23B3D_v3_0_0
from .validators.v3_0_0.jsd_b14d63c641e95ac0a8c2da2fb65909c7 \
    import JSONSchemaValidatorB14D63C641E95Ac0A8C2Da2Fb65909C7 \
    as JSONSchemaValidatorB14D63C641E95Ac0A8C2Da2Fb65909C7_v3_0_0
from .validators.v3_0_0.jsd_b1edfeb182025176bb250633937177ae \
    import JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae \
    as JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae_v3_0_0
from .validators.v3_0_0.jsd_b3284240745e5b929c51495fe80bc1c4 \
    import JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4 \
    as JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4_v3_0_0
from .validators.v3_0_0.jsd_b8319a8b5d195348a8763acd95ca2967 \
    import JSONSchemaValidatorB8319A8B5D195348A8763Acd95Ca2967 \
    as JSONSchemaValidatorB8319A8B5D195348A8763Acd95Ca2967_v3_0_0
from .validators.v3_0_0.jsd_b839d4dee9b958e48ccef056603e253f \
    import JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F \
    as JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F_v3_0_0
from .validators.v3_0_0.jsd_b95cf8c9aed95518b38be1fa4b514b67 \
    import JSONSchemaValidatorB95Cf8C9Aed95518B38BE1Fa4B514B67 \
    as JSONSchemaValidatorB95Cf8C9Aed95518B38BE1Fa4B514B67_v3_0_0
from .validators.v3_0_0.jsd_bac6d4d95ac45a0a8933b8712dcbe70d \
    import JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D \
    as JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D_v3_0_0
from .validators.v3_0_0.jsd_bf175c04fcb051b9a6fd70a2252903fa \
    import JSONSchemaValidatorBf175C04Fcb051B9A6Fd70A2252903Fa \
    as JSONSchemaValidatorBf175C04Fcb051B9A6Fd70A2252903Fa_v3_0_0
from .validators.v3_0_0.jsd_c03505504e8e5af8a715e27c40f16eab \
    import JSONSchemaValidatorC03505504E8E5Af8A715E27C40F16Eab \
    as JSONSchemaValidatorC03505504E8E5Af8A715E27C40F16Eab_v3_0_0
from .validators.v3_0_0.jsd_c82dcf6f2c3d5d399045050b02208db2 \
    import JSONSchemaValidatorC82Dcf6F2C3D5D399045050B02208Db2 \
    as JSONSchemaValidatorC82Dcf6F2C3D5D399045050B02208Db2_v3_0_0
from .validators.v3_0_0.jsd_c8b30af4b84b5a90be2fc152cf26ad42 \
    import JSONSchemaValidatorC8B30Af4B84B5A90Be2FC152Cf26Ad42 \
    as JSONSchemaValidatorC8B30Af4B84B5A90Be2FC152Cf26Ad42_v3_0_0
from .validators.v3_0_0.jsd_c8cd2f618b655d988ce626e579486596 \
    import JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596 \
    as JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596_v3_0_0
from .validators.v3_0_0.jsd_c97e7851003e5a63a2a8005ac8807dc7 \
    import JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7 \
    as JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7_v3_0_0
from .validators.v3_0_0.jsd_ca78559d8a9f559c87f53ea85169a2c7 \
    import JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7 \
    as JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7_v3_0_0
from .validators.v3_0_0.jsd_cc909c2717cf55f1863a04a785166fe0 \
    import JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0 \
    as JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0_v3_0_0
from .validators.v3_0_0.jsd_ce83fba942c25938bae0c7012df68317 \
    import JSONSchemaValidatorCe83Fba942C25938Bae0C7012Df68317 \
    as JSONSchemaValidatorCe83Fba942C25938Bae0C7012Df68317_v3_0_0
from .validators.v3_0_0.jsd_cf310e621a395bb7bac7b90d7d4c8603 \
    import JSONSchemaValidatorCf310E621A395Bb7Bac7B90D7D4C8603 \
    as JSONSchemaValidatorCf310E621A395Bb7Bac7B90D7D4C8603_v3_0_0
from .validators.v3_0_0.jsd_d011417d18d055ccb864c1dc2ae0456d \
    import JSONSchemaValidatorD011417D18D055CcB864C1Dc2Ae0456D \
    as JSONSchemaValidatorD011417D18D055CcB864C1Dc2Ae0456D_v3_0_0
from .validators.v3_0_0.jsd_d0e432f52e2a5863858c7dc0c3eda277 \
    import JSONSchemaValidatorD0E432F52E2A5863858C7Dc0C3Eda277 \
    as JSONSchemaValidatorD0E432F52E2A5863858C7Dc0C3Eda277_v3_0_0
from .validators.v3_0_0.jsd_d524614e122d53d68324daf1681eb753 \
    import JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753 \
    as JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753_v3_0_0
from .validators.v3_0_0.jsd_d9ddc2557a495493bca08b8b973601aa \
    import JSONSchemaValidatorD9Ddc2557A495493Bca08B8B973601Aa \
    as JSONSchemaValidatorD9Ddc2557A495493Bca08B8B973601Aa_v3_0_0
from .validators.v3_0_0.jsd_ded7f8573c255c318bb1f04bfdbf01e1 \
    import JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1 \
    as JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1_v3_0_0
from .validators.v3_0_0.jsd_df9ab8ff636353279d5c787585dcb6af \
    import JSONSchemaValidatorDf9Ab8Ff636353279D5C787585Dcb6Af \
    as JSONSchemaValidatorDf9Ab8Ff636353279D5C787585Dcb6Af_v3_0_0
from .validators.v3_0_0.jsd_dfaeea899c185169ae2a3b70b5491008 \
    import JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008 \
    as JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008_v3_0_0
from .validators.v3_0_0.jsd_e2c930d3d75859b8b7d30e79f3eab084 \
    import JSONSchemaValidatorE2C930D3D75859B8B7D30E79F3Eab084 \
    as JSONSchemaValidatorE2C930D3D75859B8B7D30E79F3Eab084_v3_0_0
from .validators.v3_0_0.jsd_e39868ea7aec5efcaaf55009699eda5d \
    import JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D \
    as JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D_v3_0_0
from .validators.v3_0_0.jsd_e405a20316825460a1f37a2f161e7ac5 \
    import JSONSchemaValidatorE405A20316825460A1F37A2F161E7Ac5 \
    as JSONSchemaValidatorE405A20316825460A1F37A2F161E7Ac5_v3_0_0
from .validators.v3_0_0.jsd_e7bd468ee94f53869e52e84454efd0e6 \
    import JSONSchemaValidatorE7Bd468EE94F53869E52E84454Efd0E6 \
    as JSONSchemaValidatorE7Bd468EE94F53869E52E84454Efd0E6_v3_0_0
from .validators.v3_0_0.jsd_e82e46732de25832a543c4640312588c \
    import JSONSchemaValidatorE82E46732De25832A543C4640312588C \
    as JSONSchemaValidatorE82E46732De25832A543C4640312588C_v3_0_0
from .validators.v3_0_0.jsd_e84705b918955b53afe61fc37911eb8b \
    import JSONSchemaValidatorE84705B918955B53Afe61Fc37911Eb8B \
    as JSONSchemaValidatorE84705B918955B53Afe61Fc37911Eb8B_v3_0_0
from .validators.v3_0_0.jsd_eae60ece5110590e97ddd910e8144ed2 \
    import JSONSchemaValidatorEae60Ece5110590E97DdD910E8144Ed2 \
    as JSONSchemaValidatorEae60Ece5110590E97DdD910E8144Ed2_v3_0_0
from .validators.v3_0_0.jsd_f1ff2b82953f5131884f0779db37190c \
    import JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C \
    as JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C_v3_0_0
from .validators.v3_0_0.jsd_f24049df29d059c48eef86d381ffad5d \
    import JSONSchemaValidatorF24049Df29D059C48Eef86D381Ffad5D \
    as JSONSchemaValidatorF24049Df29D059C48Eef86D381Ffad5D_v3_0_0
from .validators.v3_0_0.jsd_f41d844dbee15f7680920652004f69b6 \
    import JSONSchemaValidatorF41D844DBee15F7680920652004F69B6 \
    as JSONSchemaValidatorF41D844DBee15F7680920652004F69B6_v3_0_0
from .validators.v3_0_0.jsd_f46c01449d585b088490c4db530c56d5 \
    import JSONSchemaValidatorF46C01449D585B088490C4Db530C56D5 \
    as JSONSchemaValidatorF46C01449D585B088490C4Db530C56D5_v3_0_0
from .validators.v3_0_0.jsd_f4dbfb874b3b56d7a651d6732f1bd55e \
    import JSONSchemaValidatorF4Dbfb874B3B56D7A651D6732F1Bd55E \
    as JSONSchemaValidatorF4Dbfb874B3B56D7A651D6732F1Bd55E_v3_0_0
from .validators.v3_0_0.jsd_f7227b280b745b94bb801369b168a529 \
    import JSONSchemaValidatorF7227B280B745B94Bb801369B168A529 \
    as JSONSchemaValidatorF7227B280B745B94Bb801369B168A529_v3_0_0
from .validators.v3_0_0.jsd_f92e61297eb05379bd9b92bc60735912 \
    import JSONSchemaValidatorF92E61297Eb05379Bd9B92Bc60735912 \
    as JSONSchemaValidatorF92E61297Eb05379Bd9B92Bc60735912_v3_0_0
from .validators.v3_0_0.jsd_fc9a4ee495785518bd2251b6b4fb41f4 \
    import JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4 \
    as JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4_v3_0_0
from .validators.v3_0_0.jsd_ff0055f9ef115a42bea6ffdd8e57d41b \
    import JSONSchemaValidatorFf0055F9Ef115A42Bea6Ffdd8E57D41B \
    as JSONSchemaValidatorFf0055F9Ef115A42Bea6Ffdd8E57D41B_v3_0_0


class JSONSchemaValidator(object):
    """Validates a Identity Services Engine JSON request."""

    def __init__(self):
        super(JSONSchemaValidator, self).__init__()
        self._validator = fastjsonschema.compile({})

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(
                request, e.message
            ))


class SchemaValidator:
    def __init__(self, version):
        self.json_schema_validators = {}
        self.load_validators(version)

    def load_validators(self, version):
        if version == '3.0.0':
            self.json_schema_validators['jsd_f2fcf04554db9ea4cdc3a7024322_v3_0_0'] =\
                JSONSchemaValidatorF2FcF04554Db9Ea4Cdc3A7024322_v3_0_0()
            self.json_schema_validators['jsd_de7c6f75f68b0d7df00dc72808d_v3_0_0'] =\
                JSONSchemaValidatorDe7C6F75F68B0D7Df00Dc72808D_v3_0_0()
            self.json_schema_validators['jsd_eb42e79d5cc38bd1a6eef20613d6_v3_0_0'] =\
                JSONSchemaValidatorEb42E79D5Cc38Bd1A6Eef20613D6_v3_0_0()
            self.json_schema_validators['jsd_db1d9dda53369e35d33138b29c16_v3_0_0'] =\
                JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16_v3_0_0()
            self.json_schema_validators['jsd_ae4af25df565334b20a24c4878b68e4_v3_0_0'] =\
                JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4_v3_0_0()
            self.json_schema_validators['jsd_d39172f68fd5cbd897f03f1440f98a4_v3_0_0'] =\
                JSONSchemaValidatorD39172F68Fd5Cbd897F03F1440F98A4_v3_0_0()
            self.json_schema_validators['jsd_df78c9a3f72584dbd1c7b667b0e312f_v3_0_0'] =\
                JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F_v3_0_0()
            self.json_schema_validators['jsd_c23243c950f29b51f502c03d7058_v3_0_0'] =\
                JSONSchemaValidatorC23243C950F29B51F502C03D7058_v3_0_0()
            self.json_schema_validators['jsd_a518d5655f69e8687c9c98740c6_v3_0_0'] =\
                JSONSchemaValidatorA518D5655F69E8687C9C98740C6_v3_0_0()
            self.json_schema_validators['jsd_c45ba035019803dacdbf15cf193_v3_0_0'] =\
                JSONSchemaValidatorC45Ba035019803DAcdbf15Cf193_v3_0_0()
            self.json_schema_validators['jsd_ca61ff725fedb94fba602d7afe46_v3_0_0'] =\
                JSONSchemaValidatorCa61Ff725FedB94FBa602D7Afe46_v3_0_0()
            self.json_schema_validators['jsd_ebcdc835e9b8d6844c1da6cf252_v3_0_0'] =\
                JSONSchemaValidatorEbcDc835E9B8D6844C1Da6Cf252_v3_0_0()
            self.json_schema_validators['jsd_b05e80058df96e685baa727d578_v3_0_0'] =\
                JSONSchemaValidatorB05E80058Df96E685Baa727D578_v3_0_0()
            self.json_schema_validators['jsd_b4e8d45639975c226dacd53e7b_v3_0_0'] =\
                JSONSchemaValidatorB4E8D45639975C226Dacd53E7B_v3_0_0()
            self.json_schema_validators['jsd_e6d1b224e058288a8c4d70be72c9a6_v3_0_0'] =\
                JSONSchemaValidatorE6D1B224E058288A8C4D70Be72C9A6_v3_0_0()
            self.json_schema_validators['jsd_b40ad23ab0a5a7b8adade320c8912e7_v3_0_0'] =\
                JSONSchemaValidatorB40Ad23Ab0A5A7B8AdaDe320C8912E7_v3_0_0()
            self.json_schema_validators['jsd_c0689e940ba5526946ad15976cc3365_v3_0_0'] =\
                JSONSchemaValidatorC0689E940Ba5526946AD15976Cc3365_v3_0_0()
            self.json_schema_validators['jsd_d0290eb241f5bd79221afc8d6cb32da_v3_0_0'] =\
                JSONSchemaValidatorD0290Eb241F5Bd79221Afc8D6Cb32Da_v3_0_0()
            self.json_schema_validators['jsd_d79b507bda155c180d42f0a67ef64d5_v3_0_0'] =\
                JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5_v3_0_0()
            self.json_schema_validators['jsd_dbe47028859573988880de76fec0936_v3_0_0'] =\
                JSONSchemaValidatorDbe47028859573988880De76Fec0936_v3_0_0()
            self.json_schema_validators['jsd_fc1c74b35ae5050b4f7fd702570ad5b_v3_0_0'] =\
                JSONSchemaValidatorFc1C74B35Ae5050B4F7Fd702570Ad5B_v3_0_0()
            self.json_schema_validators['jsd_f8082b07ce528f82545e210b84d7de_v3_0_0'] =\
                JSONSchemaValidatorF8082B07Ce528F82545E210B84D7De_v3_0_0()
            self.json_schema_validators['jsd_cb625d5ad0ad76b93282f5818a_v3_0_0'] =\
                JSONSchemaValidatorCb625D5Ad0Ad76B93282F5818A_v3_0_0()
            self.json_schema_validators['jsd_f78898b7d655b2b81085dc7c0a964e_v3_0_0'] =\
                JSONSchemaValidatorF78898B7D655B2B81085Dc7C0A964E_v3_0_0()
            self.json_schema_validators['jsd_c288192f954309b4b35aa612ff226_v3_0_0'] =\
                JSONSchemaValidatorC288192F954309B4B35Aa612Ff226_v3_0_0()
            self.json_schema_validators['jsd_a4d5b5da6a50bfaaecc180543fd952_v3_0_0'] =\
                JSONSchemaValidatorA4D5B5Da6A50BfAaecC180543Fd952_v3_0_0()
            self.json_schema_validators['jsd_a99695fd5ee0b00efce79a5761ff_v3_0_0'] =\
                JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff_v3_0_0()
            self.json_schema_validators['jsd_da0a59db7654cfa89df49ca3ac3414_v3_0_0'] =\
                JSONSchemaValidatorDa0A59Db7654CfA89DF49Ca3Ac3414_v3_0_0()
            self.json_schema_validators['jsd_a31eb33e3535754b3f754a9199e0d25_v3_0_0'] =\
                JSONSchemaValidatorA31Eb33E3535754B3F754A9199E0D25_v3_0_0()
            self.json_schema_validators['jsd_acfdb4060de5a1895b383238c205986_v3_0_0'] =\
                JSONSchemaValidatorAcfdb4060De5A1895B383238C205986_v3_0_0()
            self.json_schema_validators['jsd_b94d7d3f0ed5d0b938151ae2cae9fa4_v3_0_0'] =\
                JSONSchemaValidatorB94D7D3F0Ed5D0B938151Ae2Cae9Fa4_v3_0_0()
            self.json_schema_validators['jsd_b994e6c8b8d53f29230686824c9fafa_v3_0_0'] =\
                JSONSchemaValidatorB994E6C8B8D53F29230686824C9Fafa_v3_0_0()
            self.json_schema_validators['jsd_d8c7ba0cb8f56d99135e16d2d973d11_v3_0_0'] =\
                JSONSchemaValidatorD8C7Ba0Cb8F56D99135E16D2D973D11_v3_0_0()
            self.json_schema_validators['jsd_ea2c4586b845888b2a9375126f70de2_v3_0_0'] =\
                JSONSchemaValidatorEa2C4586B845888B2A9375126F70De2_v3_0_0()
            self.json_schema_validators['jsd_eb3472c4de150828b2dae61e2285313_v3_0_0'] =\
                JSONSchemaValidatorEb3472C4De150828B2DAe61E2285313_v3_0_0()
            self.json_schema_validators['jsd_edfca30e8e514d9bab840c3c2d4c0f_v3_0_0'] =\
                JSONSchemaValidatorEdfca30E8E514D9Bab840C3C2D4C0F_v3_0_0()
            self.json_schema_validators['jsd_c5c9b7ab72b5442ae7026a5dcc0fec3_v3_0_0'] =\
                JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3_v3_0_0()
            self.json_schema_validators['jsd_fd9e7e03a6056d1b6e9705e3096d946_v3_0_0'] =\
                JSONSchemaValidatorFd9E7E03A6056D1B6E9705E3096D946_v3_0_0()
            self.json_schema_validators['jsd_c4fada6c558d9aba09cc373d5b266_v3_0_0'] =\
                JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0()
            self.json_schema_validators['jsd_b11e2f1af656bcb5880a7b33720ec5_v3_0_0'] =\
                JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0()
            self.json_schema_validators['jsd_ce666e64a958229cfd8da70945935e_v3_0_0'] =\
                JSONSchemaValidatorCe666E64A958229Cfd8Da70945935E_v3_0_0()
            self.json_schema_validators['jsd_19d9509db339e3b27dc56b37_v3_0_0'] =\
                JSONSchemaValidator19D9509DB339E3B27Dc56B37_v3_0_0()
            self.json_schema_validators['jsd_fb9c22ad9a5eddb590c85abdab460b_v3_0_0'] =\
                JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B_v3_0_0()
            self.json_schema_validators['jsd_fd729f50e65695966359b589a1606b_v3_0_0'] =\
                JSONSchemaValidatorFd729F50E65695966359B589A1606B_v3_0_0()
            self.json_schema_validators['jsd_cf65cd559628b26f6eb5ea20f14_v3_0_0'] =\
                JSONSchemaValidatorCf65Cd559628B26F6Eb5Ea20F14_v3_0_0()
            self.json_schema_validators['jsd_d67f9f6fba65dcbbcf64ca3e31b39a6_v3_0_0'] =\
                JSONSchemaValidatorD67F9F6Fba65DcbBcf64Ca3E31B39A6_v3_0_0()
            self.json_schema_validators['jsd_e6c7251a8508597f1b7ae61cbf953_v3_0_0'] =\
                JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953_v3_0_0()
            self.json_schema_validators['jsd_a03a30be865ca599e77c63a332978b_v3_0_0'] =\
                JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B_v3_0_0()
            self.json_schema_validators['jsd_ca6ab8ec556c3bc9531dc380b230a_v3_0_0'] =\
                JSONSchemaValidatorCa6Ab8Ec556C3Bc9531Dc380B230A_v3_0_0()
            self.json_schema_validators['jsd_ad69fa1d850f4993bbfc888749fa0_v3_0_0'] =\
                JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0()
            self.json_schema_validators['jsd_bf19f653f9a5c48d1fb1890409_v3_0_0'] =\
                JSONSchemaValidatorBf19F653F9A5C48D1Fb1890409_v3_0_0()
            self.json_schema_validators['jsd_abc25887a5daab1216195e08cbd49_v3_0_0'] =\
                JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49_v3_0_0()
            self.json_schema_validators['jsd_d1e1fc98a5588b8bbdda06c4fc012_v3_0_0'] =\
                JSONSchemaValidatorD1E1FC98A5588B8BbDda06C4Fc012_v3_0_0()
            self.json_schema_validators['jsd_c6536d17325c84a54189f46d4bbad2_v3_0_0'] =\
                JSONSchemaValidatorC6536D17325C84A54189F46D4Bbad2_v3_0_0()
            self.json_schema_validators['jsd_c475afd2a5e57e4bd0952f2c5349c6c_v3_0_0'] =\
                JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C_v3_0_0()
            self.json_schema_validators['jsd_a0b312f70257b1bfa90d0260f0c971_v3_0_0'] =\
                JSONSchemaValidatorA0B312F70257B1Bfa90D0260F0C971_v3_0_0()
            self.json_schema_validators['jsd_b2eebd5c245e58a503aa53115eec53_v3_0_0'] =\
                JSONSchemaValidatorB2Eebd5C245E58A503Aa53115Eec53_v3_0_0()
            self.json_schema_validators['jsd_c560004d8b5f64a10f2cc070368c12_v3_0_0'] =\
                JSONSchemaValidatorC560004D8B5F64A10F2Cc070368C12_v3_0_0()
            self.json_schema_validators['jsd_e9318040a456978757d7abfa3e66b1_v3_0_0'] =\
                JSONSchemaValidatorE9318040A456978757D7Abfa3E66B1_v3_0_0()
            self.json_schema_validators['jsd_c1fa3bf115c77be99b602aca1493b_v3_0_0'] =\
                JSONSchemaValidatorC1Fa3Bf115C77Be99B602Aca1493B_v3_0_0()
            self.json_schema_validators['jsd_c38fb2e2dd45f4dab6ec3a19effd15a_v3_0_0'] =\
                JSONSchemaValidatorC38Fb2E2Dd45F4DAb6EC3A19Effd15A_v3_0_0()
            self.json_schema_validators['jsd_cc0a87094bf5d96af61403dfc3747db_v3_0_0'] =\
                JSONSchemaValidatorCc0A87094Bf5D96Af61403Dfc3747Db_v3_0_0()
            self.json_schema_validators['jsd_ee1780a38a85d1ba57c9a38e1093721_v3_0_0'] =\
                JSONSchemaValidatorEe1780A38A85D1BA57C9A38E1093721_v3_0_0()
            self.json_schema_validators['jsd_f4508bb3352ff920dbdc229e0fc50_v3_0_0'] =\
                JSONSchemaValidatorF4508Bb3352Ff920DBdc229E0Fc50_v3_0_0()
            self.json_schema_validators['jsd_e6e4b7d022556a80f1948efb3d5c61_v3_0_0'] =\
                JSONSchemaValidatorE6E4B7D022556A80F1948Efb3D5C61_v3_0_0()
            self.json_schema_validators['jsd_eca5db5147b1e3b35a032ced4b_v3_0_0'] =\
                JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B_v3_0_0()
            self.json_schema_validators['jsd_f7bd03a835c95b7a759b39ce7f680_v3_0_0'] =\
                JSONSchemaValidatorF7Bd03A835C95B7A759B39Ce7F680_v3_0_0()
            self.json_schema_validators['jsd_b314d32b258a1b53c5c84cf84d396_v3_0_0'] =\
                JSONSchemaValidatorB314D32B258A1B53C5C84Cf84D396_v3_0_0()
            self.json_schema_validators['jsd_da250e23ac05e6a8dcf32a81effcee9_v3_0_0'] =\
                JSONSchemaValidatorDa250E23Ac05E6A8Dcf32A81Effcee9_v3_0_0()
            self.json_schema_validators['jsd_e6734850fabb2097fa969948cb_v3_0_0'] =\
                JSONSchemaValidatorE6734850FaBb2097Fa969948Cb_v3_0_0()
            self.json_schema_validators['jsd_e84541805d1da1fa3d4d581102a9_v3_0_0'] =\
                JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9_v3_0_0()
            self.json_schema_validators['jsd_ad6ca0642c5750af6ca9905721a9d7_v3_0_0'] =\
                JSONSchemaValidatorAd6Ca0642C5750Af6CA9905721A9D7_v3_0_0()
            self.json_schema_validators['jsd_ab88be5092bf4ba9f522e8e26f_v3_0_0'] =\
                JSONSchemaValidatorAb88Be5092Bf4BA9F522E8E26F_v3_0_0()
            self.json_schema_validators['jsd_b9c7c5847b17684c49399ff95_v3_0_0'] =\
                JSONSchemaValidatorB9C7C5847B17684C49399Ff95_v3_0_0()
            self.json_schema_validators['jsd_a57687cef65891a6f48dd17f456c4e_v3_0_0'] =\
                JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E_v3_0_0()
            self.json_schema_validators['jsd_f7cf06a1655d6da606ace9b0950bcf_v3_0_0'] =\
                JSONSchemaValidatorF7Cf06A1655D6DA606Ace9B0950Bcf_v3_0_0()
            self.json_schema_validators['jsd_eb833980f55025bfacbfcb8de814c8_v3_0_0'] =\
                JSONSchemaValidatorEb833980F55025BfacBfcb8De814C8_v3_0_0()
            self.json_schema_validators['jsd_d0006cc03d53c89a3593526bf8dc0f_v3_0_0'] =\
                JSONSchemaValidatorD0006CC03D53C89A3593526Bf8Dc0F_v3_0_0()
            self.json_schema_validators['jsd_a4cccea3c9567498f6f688e0cf86e7_v3_0_0'] =\
                JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7_v3_0_0()
            self.json_schema_validators['jsd_a9fa9cbccbe50fcb1cd6a63fed47578_v3_0_0'] =\
                JSONSchemaValidatorA9Fa9CbCcbe50FcB1Cd6A63Fed47578_v3_0_0()
            self.json_schema_validators['jsd_ab61f24bdaf508590f7686e1130913f_v3_0_0'] =\
                JSONSchemaValidatorAb61F24Bdaf508590F7686E1130913F_v3_0_0()
            self.json_schema_validators['jsd_c316d5e2fdd51bdab039ea9e2a417bd_v3_0_0'] =\
                JSONSchemaValidatorC316D5E2Fdd51BdAb039Ea9E2A417Bd_v3_0_0()
            self.json_schema_validators['jsd_c43118f80d4556a8ec759a8c41e2097_v3_0_0'] =\
                JSONSchemaValidatorC43118F80D4556A8Ec759A8C41E2097_v3_0_0()
            self.json_schema_validators['jsd_cb9f26e93655e7d89995b172f6fd97f_v3_0_0'] =\
                JSONSchemaValidatorCb9F26E93655E7D89995B172F6Fd97F_v3_0_0()
            self.json_schema_validators['jsd_dfe1db8729d541fb3a17d31d47d1881_v3_0_0'] =\
                JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881_v3_0_0()
            self.json_schema_validators['jsd_ed5bf99062d5dee87fe5cd96e360ec2_v3_0_0'] =\
                JSONSchemaValidatorEd5Bf99062D5Dee87Fe5Cd96E360Ec2_v3_0_0()
            self.json_schema_validators['jsd_a22b2304dcc855abb2a298de6ecddb65_v3_0_0'] =\
                JSONSchemaValidatorA22B2304Dcc855AbB2A298De6Ecddb65_v3_0_0()
            self.json_schema_validators['jsd_a60b29bfe2b055299e4360d84380ddd4_v3_0_0'] =\
                JSONSchemaValidatorA60B29BfE2B055299E4360D84380Ddd4_v3_0_0()
            self.json_schema_validators['jsd_a7500f6e473a50e19452683e303dd021_v3_0_0'] =\
                JSONSchemaValidatorA7500F6E473A50E19452683E303Dd021_v3_0_0()
            self.json_schema_validators['jsd_a87d60d590485830aed781bfb15b5c95_v3_0_0'] =\
                JSONSchemaValidatorA87D60D590485830Aed781Bfb15B5C95_v3_0_0()
            self.json_schema_validators['jsd_aa333658bf83576eb36a025283516518_v3_0_0'] =\
                JSONSchemaValidatorAa333658Bf83576EB36A025283516518_v3_0_0()
            self.json_schema_validators['jsd_aa4daefaa3b95ecca521188a43eacbd9_v3_0_0'] =\
                JSONSchemaValidatorAa4DaefaA3B95EccA521188A43Eacbd9_v3_0_0()
            self.json_schema_validators['jsd_ac171b8ccf79502fbc4b35909970a1cb_v3_0_0'] =\
                JSONSchemaValidatorAc171B8CCf79502FBc4B35909970A1Cb_v3_0_0()
            self.json_schema_validators['jsd_adcf947c42fe5588b7b82d9c43a3bbf0_v3_0_0'] =\
                JSONSchemaValidatorAdcf947C42Fe5588B7B82D9C43A3Bbf0_v3_0_0()
            self.json_schema_validators['jsd_afc81cd1e25c50319f75606b97c23b3d_v3_0_0'] =\
                JSONSchemaValidatorAfc81Cd1E25C50319F75606B97C23B3D_v3_0_0()
            self.json_schema_validators['jsd_b14d63c641e95ac0a8c2da2fb65909c7_v3_0_0'] =\
                JSONSchemaValidatorB14D63C641E95Ac0A8C2Da2Fb65909C7_v3_0_0()
            self.json_schema_validators['jsd_b1edfeb182025176bb250633937177ae_v3_0_0'] =\
                JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae_v3_0_0()
            self.json_schema_validators['jsd_b3284240745e5b929c51495fe80bc1c4_v3_0_0'] =\
                JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4_v3_0_0()
            self.json_schema_validators['jsd_b8319a8b5d195348a8763acd95ca2967_v3_0_0'] =\
                JSONSchemaValidatorB8319A8B5D195348A8763Acd95Ca2967_v3_0_0()
            self.json_schema_validators['jsd_b839d4dee9b958e48ccef056603e253f_v3_0_0'] =\
                JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F_v3_0_0()
            self.json_schema_validators['jsd_b95cf8c9aed95518b38be1fa4b514b67_v3_0_0'] =\
                JSONSchemaValidatorB95Cf8C9Aed95518B38BE1Fa4B514B67_v3_0_0()
            self.json_schema_validators['jsd_bac6d4d95ac45a0a8933b8712dcbe70d_v3_0_0'] =\
                JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D_v3_0_0()
            self.json_schema_validators['jsd_bf175c04fcb051b9a6fd70a2252903fa_v3_0_0'] =\
                JSONSchemaValidatorBf175C04Fcb051B9A6Fd70A2252903Fa_v3_0_0()
            self.json_schema_validators['jsd_c03505504e8e5af8a715e27c40f16eab_v3_0_0'] =\
                JSONSchemaValidatorC03505504E8E5Af8A715E27C40F16Eab_v3_0_0()
            self.json_schema_validators['jsd_c82dcf6f2c3d5d399045050b02208db2_v3_0_0'] =\
                JSONSchemaValidatorC82Dcf6F2C3D5D399045050B02208Db2_v3_0_0()
            self.json_schema_validators['jsd_c8b30af4b84b5a90be2fc152cf26ad42_v3_0_0'] =\
                JSONSchemaValidatorC8B30Af4B84B5A90Be2FC152Cf26Ad42_v3_0_0()
            self.json_schema_validators['jsd_c8cd2f618b655d988ce626e579486596_v3_0_0'] =\
                JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596_v3_0_0()
            self.json_schema_validators['jsd_c97e7851003e5a63a2a8005ac8807dc7_v3_0_0'] =\
                JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7_v3_0_0()
            self.json_schema_validators['jsd_ca78559d8a9f559c87f53ea85169a2c7_v3_0_0'] =\
                JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7_v3_0_0()
            self.json_schema_validators['jsd_cc909c2717cf55f1863a04a785166fe0_v3_0_0'] =\
                JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0_v3_0_0()
            self.json_schema_validators['jsd_ce83fba942c25938bae0c7012df68317_v3_0_0'] =\
                JSONSchemaValidatorCe83Fba942C25938Bae0C7012Df68317_v3_0_0()
            self.json_schema_validators['jsd_cf310e621a395bb7bac7b90d7d4c8603_v3_0_0'] =\
                JSONSchemaValidatorCf310E621A395Bb7Bac7B90D7D4C8603_v3_0_0()
            self.json_schema_validators['jsd_d011417d18d055ccb864c1dc2ae0456d_v3_0_0'] =\
                JSONSchemaValidatorD011417D18D055CcB864C1Dc2Ae0456D_v3_0_0()
            self.json_schema_validators['jsd_d0e432f52e2a5863858c7dc0c3eda277_v3_0_0'] =\
                JSONSchemaValidatorD0E432F52E2A5863858C7Dc0C3Eda277_v3_0_0()
            self.json_schema_validators['jsd_d524614e122d53d68324daf1681eb753_v3_0_0'] =\
                JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753_v3_0_0()
            self.json_schema_validators['jsd_d9ddc2557a495493bca08b8b973601aa_v3_0_0'] =\
                JSONSchemaValidatorD9Ddc2557A495493Bca08B8B973601Aa_v3_0_0()
            self.json_schema_validators['jsd_ded7f8573c255c318bb1f04bfdbf01e1_v3_0_0'] =\
                JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1_v3_0_0()
            self.json_schema_validators['jsd_df9ab8ff636353279d5c787585dcb6af_v3_0_0'] =\
                JSONSchemaValidatorDf9Ab8Ff636353279D5C787585Dcb6Af_v3_0_0()
            self.json_schema_validators['jsd_dfaeea899c185169ae2a3b70b5491008_v3_0_0'] =\
                JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008_v3_0_0()
            self.json_schema_validators['jsd_e2c930d3d75859b8b7d30e79f3eab084_v3_0_0'] =\
                JSONSchemaValidatorE2C930D3D75859B8B7D30E79F3Eab084_v3_0_0()
            self.json_schema_validators['jsd_e39868ea7aec5efcaaf55009699eda5d_v3_0_0'] =\
                JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D_v3_0_0()
            self.json_schema_validators['jsd_e405a20316825460a1f37a2f161e7ac5_v3_0_0'] =\
                JSONSchemaValidatorE405A20316825460A1F37A2F161E7Ac5_v3_0_0()
            self.json_schema_validators['jsd_e7bd468ee94f53869e52e84454efd0e6_v3_0_0'] =\
                JSONSchemaValidatorE7Bd468EE94F53869E52E84454Efd0E6_v3_0_0()
            self.json_schema_validators['jsd_e82e46732de25832a543c4640312588c_v3_0_0'] =\
                JSONSchemaValidatorE82E46732De25832A543C4640312588C_v3_0_0()
            self.json_schema_validators['jsd_e84705b918955b53afe61fc37911eb8b_v3_0_0'] =\
                JSONSchemaValidatorE84705B918955B53Afe61Fc37911Eb8B_v3_0_0()
            self.json_schema_validators['jsd_eae60ece5110590e97ddd910e8144ed2_v3_0_0'] =\
                JSONSchemaValidatorEae60Ece5110590E97DdD910E8144Ed2_v3_0_0()
            self.json_schema_validators['jsd_f1ff2b82953f5131884f0779db37190c_v3_0_0'] =\
                JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C_v3_0_0()
            self.json_schema_validators['jsd_f24049df29d059c48eef86d381ffad5d_v3_0_0'] =\
                JSONSchemaValidatorF24049Df29D059C48Eef86D381Ffad5D_v3_0_0()
            self.json_schema_validators['jsd_f41d844dbee15f7680920652004f69b6_v3_0_0'] =\
                JSONSchemaValidatorF41D844DBee15F7680920652004F69B6_v3_0_0()
            self.json_schema_validators['jsd_f46c01449d585b088490c4db530c56d5_v3_0_0'] =\
                JSONSchemaValidatorF46C01449D585B088490C4Db530C56D5_v3_0_0()
            self.json_schema_validators['jsd_f4dbfb874b3b56d7a651d6732f1bd55e_v3_0_0'] =\
                JSONSchemaValidatorF4Dbfb874B3B56D7A651D6732F1Bd55E_v3_0_0()
            self.json_schema_validators['jsd_f7227b280b745b94bb801369b168a529_v3_0_0'] =\
                JSONSchemaValidatorF7227B280B745B94Bb801369B168A529_v3_0_0()
            self.json_schema_validators['jsd_f92e61297eb05379bd9b92bc60735912_v3_0_0'] =\
                JSONSchemaValidatorF92E61297Eb05379Bd9B92Bc60735912_v3_0_0()
            self.json_schema_validators['jsd_fc9a4ee495785518bd2251b6b4fb41f4_v3_0_0'] =\
                JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4_v3_0_0()
            self.json_schema_validators['jsd_ff0055f9ef115a42bea6ffdd8e57d41b_v3_0_0'] =\
                JSONSchemaValidatorFf0055F9Ef115A42Bea6Ffdd8E57D41B_v3_0_0()

    def json_schema_validate(self, model):
        """Factory function for creating JSONSchemaValidator objects.

        Args:
            model(basestring).

        Returns:
            JSONSchemaValidator: The created JSONSchemaValidator object.

        Raises:
            MalformedRequest.
        """
        return self.json_schema_validators.get(model, JSONSchemaValidator())
