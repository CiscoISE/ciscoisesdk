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

from .validators.v3_0_0.jsd_6e4f594f8a8980361d0ab9e1 \
    import JSONSchemaValidator6E4F594F8A8980361D0Ab9E1 \
    as JSONSchemaValidator6E4F594F8A8980361D0Ab9E1_v3_0_0
from .validators.v3_0_0.jsd_de7c6f75f68b0d7df00dc72808d \
    import JSONSchemaValidatorDe7C6F75F68B0D7Df00Dc72808D \
    as JSONSchemaValidatorDe7C6F75F68B0D7Df00Dc72808D_v3_0_0
from .validators.v3_0_0.jsd_c7aed7320e54bfac29f13c8717a6b5 \
    import JSONSchemaValidatorC7Aed7320E54BfAc29F13C8717A6B5 \
    as JSONSchemaValidatorC7Aed7320E54BfAc29F13C8717A6B5_v3_0_0
from .validators.v3_0_0.jsd_a5a26c964e53b3be3f9f0c103f304c \
    import JSONSchemaValidatorA5A26C964E53B3Be3F9F0C103F304C \
    as JSONSchemaValidatorA5A26C964E53B3Be3F9F0C103F304C_v3_0_0
from .validators.v3_0_0.jsd_c21f51995bff8d6468a1e9c0b2e9 \
    import JSONSchemaValidatorC21F51995Bff8D6468A1E9C0B2E9 \
    as JSONSchemaValidatorC21F51995Bff8D6468A1E9C0B2E9_v3_0_0
from .validators.v3_0_0.jsd_be5b1e320e55f4a181370417471d9e \
    import JSONSchemaValidatorBe5B1E320E55F4A181370417471D9E \
    as JSONSchemaValidatorBe5B1E320E55F4A181370417471D9E_v3_0_0
from .validators.v3_0_0.jsd_ae4af25df565334b20a24c4878b68e4 \
    import JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4 \
    as JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4_v3_0_0
from .validators.v3_0_0.jsd_d39172f68fd5cbd897f03f1440f98a4 \
    import JSONSchemaValidatorD39172F68Fd5Cbd897F03F1440F98A4 \
    as JSONSchemaValidatorD39172F68Fd5Cbd897F03F1440F98A4_v3_0_0
from .validators.v3_0_0.jsd_df78c9a3f72584dbd1c7b667b0e312f \
    import JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F \
    as JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F_v3_0_0
from .validators.v3_0_0.jsd_e3e7b0bc717508a979ccac3b986792d \
    import JSONSchemaValidatorE3E7B0BC717508A979CCac3B986792D \
    as JSONSchemaValidatorE3E7B0BC717508A979CCac3B986792D_v3_0_0
from .validators.v3_0_0.jsd_c23243c950f29b51f502c03d7058 \
    import JSONSchemaValidatorC23243C950F29B51F502C03D7058 \
    as JSONSchemaValidatorC23243C950F29B51F502C03D7058_v3_0_0
from .validators.v3_0_0.jsd_bc936bcb25464b9f3f227647b0443 \
    import JSONSchemaValidatorBc936Bcb25464B9F3F227647B0443 \
    as JSONSchemaValidatorBc936Bcb25464B9F3F227647B0443_v3_0_0
from .validators.v3_0_0.jsd_b05e80058df96e685baa727d578 \
    import JSONSchemaValidatorB05E80058Df96E685Baa727D578 \
    as JSONSchemaValidatorB05E80058Df96E685Baa727D578_v3_0_0
from .validators.v3_0_0.jsd_edcb0e8c6b54709d4d61ea23b45f84 \
    import JSONSchemaValidatorEdcb0E8C6B54709D4D61Ea23B45F84 \
    as JSONSchemaValidatorEdcb0E8C6B54709D4D61Ea23B45F84_v3_0_0
from .validators.v3_0_0.jsd_b4e8d45639975c226dacd53e7b \
    import JSONSchemaValidatorB4E8D45639975C226Dacd53E7B \
    as JSONSchemaValidatorB4E8D45639975C226Dacd53E7B_v3_0_0
from .validators.v3_0_0.jsd_f6de5797735bbd95dc8683c6a7aebf \
    import JSONSchemaValidatorF6De5797735Bbd95Dc8683C6A7Aebf \
    as JSONSchemaValidatorF6De5797735Bbd95Dc8683C6A7Aebf_v3_0_0
from .validators.v3_0_0.jsd_a693347bdd15bb19d69a75f088498ce \
    import JSONSchemaValidatorA693347Bdd15Bb19D69A75F088498Ce \
    as JSONSchemaValidatorA693347Bdd15Bb19D69A75F088498Ce_v3_0_0
from .validators.v3_0_0.jsd_b40ad23ab0a5a7b8adade320c8912e7 \
    import JSONSchemaValidatorB40Ad23Ab0A5A7B8AdaDe320C8912E7 \
    as JSONSchemaValidatorB40Ad23Ab0A5A7B8AdaDe320C8912E7_v3_0_0
from .validators.v3_0_0.jsd_b84eb28aeb55ab7af7469c854ca1814 \
    import JSONSchemaValidatorB84Eb28Aeb55Ab7Af7469C854Ca1814 \
    as JSONSchemaValidatorB84Eb28Aeb55Ab7Af7469C854Ca1814_v3_0_0
from .validators.v3_0_0.jsd_c0689e940ba5526946ad15976cc3365 \
    import JSONSchemaValidatorC0689E940Ba5526946AD15976Cc3365 \
    as JSONSchemaValidatorC0689E940Ba5526946AD15976Cc3365_v3_0_0
from .validators.v3_0_0.jsd_cab8440e21553c3a807d23d05e5e1aa \
    import JSONSchemaValidatorCab8440E21553C3A807D23D05E5E1Aa \
    as JSONSchemaValidatorCab8440E21553C3A807D23D05E5E1Aa_v3_0_0
from .validators.v3_0_0.jsd_d0290eb241f5bd79221afc8d6cb32da \
    import JSONSchemaValidatorD0290Eb241F5Bd79221Afc8D6Cb32Da \
    as JSONSchemaValidatorD0290Eb241F5Bd79221Afc8D6Cb32Da_v3_0_0
from .validators.v3_0_0.jsd_d79b507bda155c180d42f0a67ef64d5 \
    import JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5 \
    as JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5_v3_0_0
from .validators.v3_0_0.jsd_f15d19b858d59218ab56b7323ca2fae \
    import JSONSchemaValidatorF15D19B858D59218Ab56B7323Ca2Fae \
    as JSONSchemaValidatorF15D19B858D59218Ab56B7323Ca2Fae_v3_0_0
from .validators.v3_0_0.jsd_fc1c74b35ae5050b4f7fd702570ad5b \
    import JSONSchemaValidatorFc1C74B35Ae5050B4F7Fd702570Ad5B \
    as JSONSchemaValidatorFc1C74B35Ae5050B4F7Fd702570Ad5B_v3_0_0
from .validators.v3_0_0.jsd_eb6323be425816a4116eea48f16f4b \
    import JSONSchemaValidatorEb6323Be425816A4116Eea48F16F4B \
    as JSONSchemaValidatorEb6323Be425816A4116Eea48F16F4B_v3_0_0
from .validators.v3_0_0.jsd_fc6670fd50dfb04b1f6b16981256 \
    import JSONSchemaValidatorFc6670Fd50DfB04B1F6B16981256 \
    as JSONSchemaValidatorFc6670Fd50DfB04B1F6B16981256_v3_0_0
from .validators.v3_0_0.jsd_f8082b07ce528f82545e210b84d7de \
    import JSONSchemaValidatorF8082B07Ce528F82545E210B84D7De \
    as JSONSchemaValidatorF8082B07Ce528F82545E210B84D7De_v3_0_0
from .validators.v3_0_0.jsd_a746755c588c928d15a59f8a693d \
    import JSONSchemaValidatorA746755C588C928D15A59F8A693D \
    as JSONSchemaValidatorA746755C588C928D15A59F8A693D_v3_0_0
from .validators.v3_0_0.jsd_e94f5eba9d9615a3ecc18ebc \
    import JSONSchemaValidatorE94F5Eba9D9615A3Ecc18Ebc \
    as JSONSchemaValidatorE94F5Eba9D9615A3Ecc18Ebc_v3_0_0
from .validators.v3_0_0.jsd_a99695fd5ee0b00efce79a5761ff \
    import JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff \
    as JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff_v3_0_0
from .validators.v3_0_0.jsd_a31eb33e3535754b3f754a9199e0d25 \
    import JSONSchemaValidatorA31Eb33E3535754B3F754A9199E0D25 \
    as JSONSchemaValidatorA31Eb33E3535754B3F754A9199E0D25_v3_0_0
from .validators.v3_0_0.jsd_acfdb4060de5a1895b383238c205986 \
    import JSONSchemaValidatorAcfdb4060De5A1895B383238C205986 \
    as JSONSchemaValidatorAcfdb4060De5A1895B383238C205986_v3_0_0
from .validators.v3_0_0.jsd_d40ae38628c51c49af42a4ede3d66d9 \
    import JSONSchemaValidatorD40Ae38628C51C49Af42A4Ede3D66D9 \
    as JSONSchemaValidatorD40Ae38628C51C49Af42A4Ede3D66D9_v3_0_0
from .validators.v3_0_0.jsd_d8c7ba0cb8f56d99135e16d2d973d11 \
    import JSONSchemaValidatorD8C7Ba0Cb8F56D99135E16D2D973D11 \
    as JSONSchemaValidatorD8C7Ba0Cb8F56D99135E16D2D973D11_v3_0_0
from .validators.v3_0_0.jsd_ea2c4586b845888b2a9375126f70de2 \
    import JSONSchemaValidatorEa2C4586B845888B2A9375126F70De2 \
    as JSONSchemaValidatorEa2C4586B845888B2A9375126F70De2_v3_0_0
from .validators.v3_0_0.jsd_eb3472c4de150828b2dae61e2285313 \
    import JSONSchemaValidatorEb3472C4De150828B2DAe61E2285313 \
    as JSONSchemaValidatorEb3472C4De150828B2DAe61E2285313_v3_0_0
from .validators.v3_0_0.jsd_e07cb8ea65820863cce345c67926b \
    import JSONSchemaValidatorE07Cb8Ea65820863CCe345C67926B \
    as JSONSchemaValidatorE07Cb8Ea65820863CCe345C67926B_v3_0_0
from .validators.v3_0_0.jsd_e5dd2909045a90bdce4848865662c2 \
    import JSONSchemaValidatorE5Dd2909045A90Bdce4848865662C2 \
    as JSONSchemaValidatorE5Dd2909045A90Bdce4848865662C2_v3_0_0
from .validators.v3_0_0.jsd_edfca30e8e514d9bab840c3c2d4c0f \
    import JSONSchemaValidatorEdfca30E8E514D9Bab840C3C2D4C0F \
    as JSONSchemaValidatorEdfca30E8E514D9Bab840C3C2D4C0F_v3_0_0
from .validators.v3_0_0.jsd_e38d10b1ea257d49ebce893e87b3419 \
    import JSONSchemaValidatorE38D10B1Ea257D49EbcE893E87B3419 \
    as JSONSchemaValidatorE38D10B1Ea257D49EbcE893E87B3419_v3_0_0
from .validators.v3_0_0.jsd_c4fada6c558d9aba09cc373d5b266 \
    import JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266 \
    as JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0
from .validators.v3_0_0.jsd_fa27e5a779143ed557b417535 \
    import JSONSchemaValidatorFA27E5A779143Ed557B417535 \
    as JSONSchemaValidatorFA27E5A779143Ed557B417535_v3_0_0
from .validators.v3_0_0.jsd_b11e2f1af656bcb5880a7b33720ec5 \
    import JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5 \
    as JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0
from .validators.v3_0_0.jsd_ce666e64a958229cfd8da70945935e \
    import JSONSchemaValidatorCe666E64A958229Cfd8Da70945935E \
    as JSONSchemaValidatorCe666E64A958229Cfd8Da70945935E_v3_0_0
from .validators.v3_0_0.jsd_e1af4e392c5790a01685b9687208c0 \
    import JSONSchemaValidatorE1Af4E392C5790A01685B9687208C0 \
    as JSONSchemaValidatorE1Af4E392C5790A01685B9687208C0_v3_0_0
from .validators.v3_0_0.jsd_a9f304a4ec54afa6e3484978aacbbb \
    import JSONSchemaValidatorA9F304A4Ec54AfA6E3484978Aacbbb \
    as JSONSchemaValidatorA9F304A4Ec54AfA6E3484978Aacbbb_v3_0_0
from .validators.v3_0_0.jsd_19d9509db339e3b27dc56b37 \
    import JSONSchemaValidator19D9509DB339E3B27Dc56B37 \
    as JSONSchemaValidator19D9509DB339E3B27Dc56B37_v3_0_0
from .validators.v3_0_0.jsd_fd729f50e65695966359b589a1606b \
    import JSONSchemaValidatorFd729F50E65695966359B589A1606B \
    as JSONSchemaValidatorFd729F50E65695966359B589A1606B_v3_0_0
from .validators.v3_0_0.jsd_fac48e5c63abfe2feec6fd1903 \
    import JSONSchemaValidatorFaC48E5C63Abfe2Feec6Fd1903 \
    as JSONSchemaValidatorFaC48E5C63Abfe2Feec6Fd1903_v3_0_0
from .validators.v3_0_0.jsd_a0db9ec45c05879a6f016a1edf54793 \
    import JSONSchemaValidatorA0Db9Ec45C05879A6F016A1Edf54793 \
    as JSONSchemaValidatorA0Db9Ec45C05879A6F016A1Edf54793_v3_0_0
from .validators.v3_0_0.jsd_d67f9f6fba65dcbbcf64ca3e31b39a6 \
    import JSONSchemaValidatorD67F9F6Fba65DcbBcf64Ca3E31B39A6 \
    as JSONSchemaValidatorD67F9F6Fba65DcbBcf64Ca3E31B39A6_v3_0_0
from .validators.v3_0_0.jsd_dd838b268f5dd298a123ac58448ea9 \
    import JSONSchemaValidatorDd838B268F5Dd298A123Ac58448Ea9 \
    as JSONSchemaValidatorDd838B268F5Dd298A123Ac58448Ea9_v3_0_0
from .validators.v3_0_0.jsd_1872577f8d1efe131783009c \
    import JSONSchemaValidator1872577F8D1EFe131783009C \
    as JSONSchemaValidator1872577F8D1EFe131783009C_v3_0_0
from .validators.v3_0_0.jsd_d31fa60f5575a2ed23cee473c0fc \
    import JSONSchemaValidatorD31FA60F5575A2Ed23Cee473C0Fc \
    as JSONSchemaValidatorD31FA60F5575A2Ed23Cee473C0Fc_v3_0_0
from .validators.v3_0_0.jsd_a3c8e0ddc5b40a250affc4be1700a \
    import JSONSchemaValidatorA3C8E0Ddc5B40A250Affc4Be1700A \
    as JSONSchemaValidatorA3C8E0Ddc5B40A250Affc4Be1700A_v3_0_0
from .validators.v3_0_0.jsd_c2e3af6da356009f6499f00a4115e9 \
    import JSONSchemaValidatorC2E3Af6Da356009F6499F00A4115E9 \
    as JSONSchemaValidatorC2E3Af6Da356009F6499F00A4115E9_v3_0_0
from .validators.v3_0_0.jsd_acd30d35ee2ae16ff23757de7d8 \
    import JSONSchemaValidatorAcd30D35Ee2Ae16Ff23757De7D8 \
    as JSONSchemaValidatorAcd30D35Ee2Ae16Ff23757De7D8_v3_0_0
from .validators.v3_0_0.jsd_cea2e785ee57908a9ee3b118e49cfa \
    import JSONSchemaValidatorCea2E785Ee57908A9EE3B118E49Cfa \
    as JSONSchemaValidatorCea2E785Ee57908A9EE3B118E49Cfa_v3_0_0
from .validators.v3_0_0.jsd_ca6ab8ec556c3bc9531dc380b230a \
    import JSONSchemaValidatorCa6Ab8Ec556C3Bc9531Dc380B230A \
    as JSONSchemaValidatorCa6Ab8Ec556C3Bc9531Dc380B230A_v3_0_0
from .validators.v3_0_0.jsd_ac3ccf225801ad8ba0bb1ad9de0b \
    import JSONSchemaValidatorAc3CCf225801Ad8BA0Bb1Ad9De0B \
    as JSONSchemaValidatorAc3CCf225801Ad8BA0Bb1Ad9De0B_v3_0_0
from .validators.v3_0_0.jsd_ad69fa1d850f4993bbfc888749fa0 \
    import JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0 \
    as JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0
from .validators.v3_0_0.jsd_a1e26e595667bd98f84dd29232e2 \
    import JSONSchemaValidatorA1E26E595667Bd98F84Dd29232E2 \
    as JSONSchemaValidatorA1E26E595667Bd98F84Dd29232E2_v3_0_0
from .validators.v3_0_0.jsd_bf19f653f9a5c48d1fb1890409 \
    import JSONSchemaValidatorBf19F653F9A5C48D1Fb1890409 \
    as JSONSchemaValidatorBf19F653F9A5C48D1Fb1890409_v3_0_0
from .validators.v3_0_0.jsd_e6167fc5cb6593b8b48429187a26a67 \
    import JSONSchemaValidatorE6167Fc5Cb6593B8B48429187A26A67 \
    as JSONSchemaValidatorE6167Fc5Cb6593B8B48429187A26A67_v3_0_0
from .validators.v3_0_0.jsd_a0b312f70257b1bfa90d0260f0c971 \
    import JSONSchemaValidatorA0B312F70257B1Bfa90D0260F0C971 \
    as JSONSchemaValidatorA0B312F70257B1Bfa90D0260F0C971_v3_0_0
from .validators.v3_0_0.jsd_c9daa26d4b5b80a41d4b7ff9359380 \
    import JSONSchemaValidatorC9Daa26D4B5B80A41D4B7Ff9359380 \
    as JSONSchemaValidatorC9Daa26D4B5B80A41D4B7Ff9359380_v3_0_0
from .validators.v3_0_0.jsd_ad8eb56595e86c4300607ec4dd3 \
    import JSONSchemaValidatorAd8Eb56595E86C4300607Ec4Dd3 \
    as JSONSchemaValidatorAd8Eb56595E86C4300607Ec4Dd3_v3_0_0
from .validators.v3_0_0.jsd_f014ee45351ba163e3be6fa217b \
    import JSONSchemaValidatorF014Ee45351Ba163E3Be6Fa217B \
    as JSONSchemaValidatorF014Ee45351Ba163E3Be6Fa217B_v3_0_0
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
from .validators.v3_0_0.jsd_a48341446b15729abf624695b20b9f5 \
    import JSONSchemaValidatorA48341446B15729Abf624695B20B9F5 \
    as JSONSchemaValidatorA48341446B15729Abf624695B20B9F5_v3_0_0
from .validators.v3_0_0.jsd_c38fb2e2dd45f4dab6ec3a19effd15a \
    import JSONSchemaValidatorC38Fb2E2Dd45F4DAb6EC3A19Effd15A \
    as JSONSchemaValidatorC38Fb2E2Dd45F4DAb6EC3A19Effd15A_v3_0_0
from .validators.v3_0_0.jsd_cc0a87094bf5d96af61403dfc3747db \
    import JSONSchemaValidatorCc0A87094Bf5D96Af61403Dfc3747Db \
    as JSONSchemaValidatorCc0A87094Bf5D96Af61403Dfc3747Db_v3_0_0
from .validators.v3_0_0.jsd_be755dae5251bd2d8348eeebfdde \
    import JSONSchemaValidatorBe755Dae5251Bd2D8348Eeebfdde \
    as JSONSchemaValidatorBe755Dae5251Bd2D8348Eeebfdde_v3_0_0
from .validators.v3_0_0.jsd_70e85c38bcad4249948c550b \
    import JSONSchemaValidator70E85C38Bcad4249948C550B \
    as JSONSchemaValidator70E85C38Bcad4249948C550B_v3_0_0
from .validators.v3_0_0.jsd_e6e4b7d022556a80f1948efb3d5c61 \
    import JSONSchemaValidatorE6E4B7D022556A80F1948Efb3D5C61 \
    as JSONSchemaValidatorE6E4B7D022556A80F1948Efb3D5C61_v3_0_0
from .validators.v3_0_0.jsd_e92c5af5344b4d9fdc45a282ce5 \
    import JSONSchemaValidatorE92C5Af5344B4D9Fdc45A282Ce5 \
    as JSONSchemaValidatorE92C5Af5344B4D9Fdc45A282Ce5_v3_0_0
from .validators.v3_0_0.jsd_6d125b968b9d362a3458621d \
    import JSONSchemaValidator6D125B968B9D362A3458621D \
    as JSONSchemaValidator6D125B968B9D362A3458621D_v3_0_0
from .validators.v3_0_0.jsd_f7bd03a835c95b7a759b39ce7f680 \
    import JSONSchemaValidatorF7Bd03A835C95B7A759B39Ce7F680 \
    as JSONSchemaValidatorF7Bd03A835C95B7A759B39Ce7F680_v3_0_0
from .validators.v3_0_0.jsd_ad357457f45e07a13674d462c4270d \
    import JSONSchemaValidatorAd357457F45E07A13674D462C4270D \
    as JSONSchemaValidatorAd357457F45E07A13674D462C4270D_v3_0_0
from .validators.v3_0_0.jsd_9f955525b0b38a57a3bed311 \
    import JSONSchemaValidator9F955525B0B38A57A3Bed311 \
    as JSONSchemaValidator9F955525B0B38A57A3Bed311_v3_0_0
from .validators.v3_0_0.jsd_c39f0f97cb53e19a03f2ea53f5b831 \
    import JSONSchemaValidatorC39F0F97Cb53E19A03F2Ea53F5B831 \
    as JSONSchemaValidatorC39F0F97Cb53E19A03F2Ea53F5B831_v3_0_0
from .validators.v3_0_0.jsd_e5dd9b5979a409b9f456265db0 \
    import JSONSchemaValidatorE5Dd9B5979A409B9F456265Db0 \
    as JSONSchemaValidatorE5Dd9B5979A409B9F456265Db0_v3_0_0
from .validators.v3_0_0.jsd_c371214c759f791c0a522b9eaf5b5 \
    import JSONSchemaValidatorC371214C759F791C0A522B9Eaf5B5 \
    as JSONSchemaValidatorC371214C759F791C0A522B9Eaf5B5_v3_0_0
from .validators.v3_0_0.jsd_a7cffe3bfae55aa81b7b4447519e4cd \
    import JSONSchemaValidatorA7Cffe3Bfae55Aa81B7B4447519E4Cd \
    as JSONSchemaValidatorA7Cffe3Bfae55Aa81B7B4447519E4Cd_v3_0_0
from .validators.v3_0_0.jsd_da250e23ac05e6a8dcf32a81effcee9 \
    import JSONSchemaValidatorDa250E23Ac05E6A8Dcf32A81Effcee9 \
    as JSONSchemaValidatorDa250E23Ac05E6A8Dcf32A81Effcee9_v3_0_0
from .validators.v3_0_0.jsd_e6734850fabb2097fa969948cb \
    import JSONSchemaValidatorE6734850FaBb2097Fa969948Cb \
    as JSONSchemaValidatorE6734850FaBb2097Fa969948Cb_v3_0_0
from .validators.v3_0_0.jsd_e84541805d1da1fa3d4d581102a9 \
    import JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9 \
    as JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9_v3_0_0
from .validators.v3_0_0.jsd_c64b769537ea7c586565f6ed2a2 \
    import JSONSchemaValidatorC64B769537EA7C586565F6Ed2A2 \
    as JSONSchemaValidatorC64B769537EA7C586565F6Ed2A2_v3_0_0
from .validators.v3_0_0.jsd_ad6ca0642c5750af6ca9905721a9d7 \
    import JSONSchemaValidatorAd6Ca0642C5750Af6CA9905721A9D7 \
    as JSONSchemaValidatorAd6Ca0642C5750Af6CA9905721A9D7_v3_0_0
from .validators.v3_0_0.jsd_ea4e38c44e5b1c90b19af25b88546e \
    import JSONSchemaValidatorEa4E38C44E5B1C90B19Af25B88546E \
    as JSONSchemaValidatorEa4E38C44E5B1C90B19Af25B88546E_v3_0_0
from .validators.v3_0_0.jsd_a5fd2b5d5306b9941387f400c7a0 \
    import JSONSchemaValidatorA5Fd2B5D5306B9941387F400C7A0 \
    as JSONSchemaValidatorA5Fd2B5D5306B9941387F400C7A0_v3_0_0
from .validators.v3_0_0.jsd_ab88be5092bf4ba9f522e8e26f \
    import JSONSchemaValidatorAb88Be5092Bf4BA9F522E8E26F \
    as JSONSchemaValidatorAb88Be5092Bf4BA9F522E8E26F_v3_0_0
from .validators.v3_0_0.jsd_cf67e0155eab895b50d1a377f21 \
    import JSONSchemaValidatorCf67E0155EaB895B50D1A377F21 \
    as JSONSchemaValidatorCf67E0155EaB895B50D1A377F21_v3_0_0
from .validators.v3_0_0.jsd_ade26d445251a45cc753f68d21bc \
    import JSONSchemaValidatorAde26D445251A45CC753F68D21Bc \
    as JSONSchemaValidatorAde26D445251A45CC753F68D21Bc_v3_0_0
from .validators.v3_0_0.jsd_ad86a47e15d45ab1cc0cadc5b248f \
    import JSONSchemaValidatorAd86A47E15D45Ab1CC0Cadc5B248F \
    as JSONSchemaValidatorAd86A47E15D45Ab1CC0Cadc5B248F_v3_0_0
from .validators.v3_0_0.jsd_bd1af169fa52c59cbc87b010c36f9e \
    import JSONSchemaValidatorBd1Af169Fa52C59Cbc87B010C36F9E \
    as JSONSchemaValidatorBd1Af169Fa52C59Cbc87B010C36F9E_v3_0_0
from .validators.v3_0_0.jsd_b9c7c5847b17684c49399ff95 \
    import JSONSchemaValidatorB9C7C5847B17684C49399Ff95 \
    as JSONSchemaValidatorB9C7C5847B17684C49399Ff95_v3_0_0
from .validators.v3_0_0.jsd_f7cf06a1655d6da606ace9b0950bcf \
    import JSONSchemaValidatorF7Cf06A1655D6DA606Ace9B0950Bcf \
    as JSONSchemaValidatorF7Cf06A1655D6DA606Ace9B0950Bcf_v3_0_0
from .validators.v3_0_0.jsd_e27d5df9cbe5b29a7e16bb7c877a4ce \
    import JSONSchemaValidatorE27D5Df9Cbe5B29A7E16Bb7C877A4Ce \
    as JSONSchemaValidatorE27D5Df9Cbe5B29A7E16Bb7C877A4Ce_v3_0_0
from .validators.v3_0_0.jsd_b93b991556cae0fdd562c5e3f63 \
    import JSONSchemaValidatorB93B991556CAe0FDd562C5E3F63 \
    as JSONSchemaValidatorB93B991556CAe0FDd562C5E3F63_v3_0_0
from .validators.v3_0_0.jsd_eb833980f55025bfacbfcb8de814c8 \
    import JSONSchemaValidatorEb833980F55025BfacBfcb8De814C8 \
    as JSONSchemaValidatorEb833980F55025BfacBfcb8De814C8_v3_0_0
from .validators.v3_0_0.jsd_de3cecd62e5153881245a8613fbeea \
    import JSONSchemaValidatorDe3CecD62E5153881245A8613Fbeea \
    as JSONSchemaValidatorDe3CecD62E5153881245A8613Fbeea_v3_0_0
from .validators.v3_0_0.jsd_d0006cc03d53c89a3593526bf8dc0f \
    import JSONSchemaValidatorD0006CC03D53C89A3593526Bf8Dc0F \
    as JSONSchemaValidatorD0006CC03D53C89A3593526Bf8Dc0F_v3_0_0
from .validators.v3_0_0.jsd_a0710ba581da4d3fd00e84d59e3 \
    import JSONSchemaValidatorA0710Ba581DA4D3Fd00E84D59E3 \
    as JSONSchemaValidatorA0710Ba581DA4D3Fd00E84D59E3_v3_0_0
from .validators.v3_0_0.jsd_b30f809e275589bd7154b5b4093d3f \
    import JSONSchemaValidatorB30F809E275589Bd7154B5B4093D3F \
    as JSONSchemaValidatorB30F809E275589Bd7154B5B4093D3F_v3_0_0
from .validators.v3_0_0.jsd_c8ffe8c6095203a83131f49d4c8bb2 \
    import JSONSchemaValidatorC8Ffe8C6095203A83131F49D4C8Bb2 \
    as JSONSchemaValidatorC8Ffe8C6095203A83131F49D4C8Bb2_v3_0_0
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
from .validators.v3_0_0.jsd_d3034483aaa5563bb287ef0cd502130 \
    import JSONSchemaValidatorD3034483Aaa5563Bb287Ef0Cd502130 \
    as JSONSchemaValidatorD3034483Aaa5563Bb287Ef0Cd502130_v3_0_0
from .validators.v3_0_0.jsd_f47dca835fa58fcb08bcdd672dfbaa7 \
    import JSONSchemaValidatorF47Dca835Fa58FcB08BCdd672Dfbaa7 \
    as JSONSchemaValidatorF47Dca835Fa58FcB08BCdd672Dfbaa7_v3_0_0
from .validators.v3_0_0.jsd_a39fa17ffcd45736aa221dd27916e843 \
    import JSONSchemaValidatorA39Fa17FFcd45736Aa221Dd27916E843 \
    as JSONSchemaValidatorA39Fa17FFcd45736Aa221Dd27916E843_v3_0_0
from .validators.v3_0_0.jsd_a7500f6e473a50e19452683e303dd021 \
    import JSONSchemaValidatorA7500F6E473A50E19452683E303Dd021 \
    as JSONSchemaValidatorA7500F6E473A50E19452683E303Dd021_v3_0_0
from .validators.v3_0_0.jsd_aa333658bf83576eb36a025283516518 \
    import JSONSchemaValidatorAa333658Bf83576EB36A025283516518 \
    as JSONSchemaValidatorAa333658Bf83576EB36A025283516518_v3_0_0
from .validators.v3_0_0.jsd_ab203a1dd0015924bf2005a84ae85477 \
    import JSONSchemaValidatorAb203A1DD0015924Bf2005A84Ae85477 \
    as JSONSchemaValidatorAb203A1DD0015924Bf2005A84Ae85477_v3_0_0
from .validators.v3_0_0.jsd_adcf947c42fe5588b7b82d9c43a3bbf0 \
    import JSONSchemaValidatorAdcf947C42Fe5588B7B82D9C43A3Bbf0 \
    as JSONSchemaValidatorAdcf947C42Fe5588B7B82D9C43A3Bbf0_v3_0_0
from .validators.v3_0_0.jsd_adde5bf7c9185218b955ff0c365fcc4c \
    import JSONSchemaValidatorAdde5Bf7C9185218B955Ff0C365Fcc4C \
    as JSONSchemaValidatorAdde5Bf7C9185218B955Ff0C365Fcc4C_v3_0_0
from .validators.v3_0_0.jsd_afc81cd1e25c50319f75606b97c23b3d \
    import JSONSchemaValidatorAfc81Cd1E25C50319F75606B97C23B3D \
    as JSONSchemaValidatorAfc81Cd1E25C50319F75606B97C23B3D_v3_0_0
from .validators.v3_0_0.jsd_afcce33ec863567f94f3b9b73719ff8d \
    import JSONSchemaValidatorAfcce33EC863567F94F3B9B73719Ff8D \
    as JSONSchemaValidatorAfcce33EC863567F94F3B9B73719Ff8D_v3_0_0
from .validators.v3_0_0.jsd_b14d63c641e95ac0a8c2da2fb65909c7 \
    import JSONSchemaValidatorB14D63C641E95Ac0A8C2Da2Fb65909C7 \
    as JSONSchemaValidatorB14D63C641E95Ac0A8C2Da2Fb65909C7_v3_0_0
from .validators.v3_0_0.jsd_b1edfeb182025176bb250633937177ae \
    import JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae \
    as JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae_v3_0_0
from .validators.v3_0_0.jsd_b3284240745e5b929c51495fe80bc1c4 \
    import JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4 \
    as JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4_v3_0_0
from .validators.v3_0_0.jsd_b5097e4db7505ba390914b50b1c2046b \
    import JSONSchemaValidatorB5097E4DB7505Ba390914B50B1C2046B \
    as JSONSchemaValidatorB5097E4DB7505Ba390914B50B1C2046B_v3_0_0
from .validators.v3_0_0.jsd_b5151e49a2b65befb488985ed973fed2 \
    import JSONSchemaValidatorB5151E49A2B65BefB488985Ed973Fed2 \
    as JSONSchemaValidatorB5151E49A2B65BefB488985Ed973Fed2_v3_0_0
from .validators.v3_0_0.jsd_b734aeeb768d568684706bff5e3fa5bb \
    import JSONSchemaValidatorB734Aeeb768D568684706Bff5E3Fa5Bb \
    as JSONSchemaValidatorB734Aeeb768D568684706Bff5E3Fa5Bb_v3_0_0
from .validators.v3_0_0.jsd_b839d4dee9b958e48ccef056603e253f \
    import JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F \
    as JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F_v3_0_0
from .validators.v3_0_0.jsd_b84dbd77c49f5056b9bf3c1e496ebe5f \
    import JSONSchemaValidatorB84Dbd77C49F5056B9Bf3C1E496Ebe5F \
    as JSONSchemaValidatorB84Dbd77C49F5056B9Bf3C1E496Ebe5F_v3_0_0
from .validators.v3_0_0.jsd_b9500d6c2f365927aa3dbe6d7ecbae22 \
    import JSONSchemaValidatorB9500D6C2F365927Aa3DBe6D7Ecbae22 \
    as JSONSchemaValidatorB9500D6C2F365927Aa3DBe6D7Ecbae22_v3_0_0
from .validators.v3_0_0.jsd_b9638a67f60d5a6aa476af13632d96bd \
    import JSONSchemaValidatorB9638A67F60D5A6AA476Af13632D96Bd \
    as JSONSchemaValidatorB9638A67F60D5A6AA476Af13632D96Bd_v3_0_0
from .validators.v3_0_0.jsd_b9de636ff2e25f849f468556c53b7b9a \
    import JSONSchemaValidatorB9De636FF2E25F849F468556C53B7B9A \
    as JSONSchemaValidatorB9De636FF2E25F849F468556C53B7B9A_v3_0_0
from .validators.v3_0_0.jsd_bac6d4d95ac45a0a8933b8712dcbe70d \
    import JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D \
    as JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D_v3_0_0
from .validators.v3_0_0.jsd_bd8691c5d9435e48a3c7a08658bda585 \
    import JSONSchemaValidatorBd8691C5D9435E48A3C7A08658Bda585 \
    as JSONSchemaValidatorBd8691C5D9435E48A3C7A08658Bda585_v3_0_0
from .validators.v3_0_0.jsd_bf175c04fcb051b9a6fd70a2252903fa \
    import JSONSchemaValidatorBf175C04Fcb051B9A6Fd70A2252903Fa \
    as JSONSchemaValidatorBf175C04Fcb051B9A6Fd70A2252903Fa_v3_0_0
from .validators.v3_0_0.jsd_c03505504e8e5af8a715e27c40f16eab \
    import JSONSchemaValidatorC03505504E8E5Af8A715E27C40F16Eab \
    as JSONSchemaValidatorC03505504E8E5Af8A715E27C40F16Eab_v3_0_0
from .validators.v3_0_0.jsd_c094086382485201ad36d4641fc6822e \
    import JSONSchemaValidatorC094086382485201Ad36D4641Fc6822E \
    as JSONSchemaValidatorC094086382485201Ad36D4641Fc6822E_v3_0_0
from .validators.v3_0_0.jsd_c26e318c3c405713a55b4e162be8c890 \
    import JSONSchemaValidatorC26E318C3C405713A55B4E162Be8C890 \
    as JSONSchemaValidatorC26E318C3C405713A55B4E162Be8C890_v3_0_0
from .validators.v3_0_0.jsd_c54a2ad63f46527dbec140a05f1213b7 \
    import JSONSchemaValidatorC54A2Ad63F46527DBec140A05F1213B7 \
    as JSONSchemaValidatorC54A2Ad63F46527DBec140A05F1213B7_v3_0_0
from .validators.v3_0_0.jsd_c730e85640aa5a59bc0e0fd95dacf889 \
    import JSONSchemaValidatorC730E85640Aa5A59Bc0E0Fd95Dacf889 \
    as JSONSchemaValidatorC730E85640Aa5A59Bc0E0Fd95Dacf889_v3_0_0
from .validators.v3_0_0.jsd_c82dcf6f2c3d5d399045050b02208db2 \
    import JSONSchemaValidatorC82Dcf6F2C3D5D399045050B02208Db2 \
    as JSONSchemaValidatorC82Dcf6F2C3D5D399045050B02208Db2_v3_0_0
from .validators.v3_0_0.jsd_c85464a04f0e5ddc99f8e6b8ed0f7eac \
    import JSONSchemaValidatorC85464A04F0E5Ddc99F8E6B8Ed0F7Eac \
    as JSONSchemaValidatorC85464A04F0E5Ddc99F8E6B8Ed0F7Eac_v3_0_0
from .validators.v3_0_0.jsd_c8b30af4b84b5a90be2fc152cf26ad42 \
    import JSONSchemaValidatorC8B30Af4B84B5A90Be2FC152Cf26Ad42 \
    as JSONSchemaValidatorC8B30Af4B84B5A90Be2FC152Cf26Ad42_v3_0_0
from .validators.v3_0_0.jsd_c97e7851003e5a63a2a8005ac8807dc7 \
    import JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7 \
    as JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7_v3_0_0
from .validators.v3_0_0.jsd_ca78559d8a9f559c87f53ea85169a2c7 \
    import JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7 \
    as JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7_v3_0_0
from .validators.v3_0_0.jsd_cd32d094f1815c388d1392bb90f3744d \
    import JSONSchemaValidatorCd32D094F1815C388D1392Bb90F3744D \
    as JSONSchemaValidatorCd32D094F1815C388D1392Bb90F3744D_v3_0_0
from .validators.v3_0_0.jsd_ce788c3408de5056a2e71955f86d6f05 \
    import JSONSchemaValidatorCe788C3408De5056A2E71955F86D6F05 \
    as JSONSchemaValidatorCe788C3408De5056A2E71955F86D6F05_v3_0_0
from .validators.v3_0_0.jsd_ce83fba942c25938bae0c7012df68317 \
    import JSONSchemaValidatorCe83Fba942C25938Bae0C7012Df68317 \
    as JSONSchemaValidatorCe83Fba942C25938Bae0C7012Df68317_v3_0_0
from .validators.v3_0_0.jsd_d011417d18d055ccb864c1dc2ae0456d \
    import JSONSchemaValidatorD011417D18D055CcB864C1Dc2Ae0456D \
    as JSONSchemaValidatorD011417D18D055CcB864C1Dc2Ae0456D_v3_0_0
from .validators.v3_0_0.jsd_d1f92a9024975e9dad6114255be546bd \
    import JSONSchemaValidatorD1F92A9024975E9DAd6114255Be546Bd \
    as JSONSchemaValidatorD1F92A9024975E9DAd6114255Be546Bd_v3_0_0
from .validators.v3_0_0.jsd_d30aa7529c245c549eafde4c17a809a4 \
    import JSONSchemaValidatorD30Aa7529C245C549EafDe4C17A809A4 \
    as JSONSchemaValidatorD30Aa7529C245C549EafDe4C17A809A4_v3_0_0
from .validators.v3_0_0.jsd_d524614e122d53d68324daf1681eb753 \
    import JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753 \
    as JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753_v3_0_0
from .validators.v3_0_0.jsd_d9cc879878ee5a34ac1c32f2f0cb8c6d \
    import JSONSchemaValidatorD9Cc879878Ee5A34Ac1C32F2F0Cb8C6D \
    as JSONSchemaValidatorD9Cc879878Ee5A34Ac1C32F2F0Cb8C6D_v3_0_0
from .validators.v3_0_0.jsd_da5ac537bf475538b7bc42c8cce2e530 \
    import JSONSchemaValidatorDa5Ac537Bf475538B7Bc42C8Cce2E530 \
    as JSONSchemaValidatorDa5Ac537Bf475538B7Bc42C8Cce2E530_v3_0_0
from .validators.v3_0_0.jsd_db3505847b4e5f37a5c74bc41df54be3 \
    import JSONSchemaValidatorDb3505847B4E5F37A5C74Bc41Df54Be3 \
    as JSONSchemaValidatorDb3505847B4E5F37A5C74Bc41Df54Be3_v3_0_0
from .validators.v3_0_0.jsd_dd4581dd32f65e8c83cca2f0a97af3e2 \
    import JSONSchemaValidatorDd4581Dd32F65E8C83CcA2F0A97Af3E2 \
    as JSONSchemaValidatorDd4581Dd32F65E8C83CcA2F0A97Af3E2_v3_0_0
from .validators.v3_0_0.jsd_dd469dcee9445c72a3861ef94fb3b096 \
    import JSONSchemaValidatorDd469DceE9445C72A3861Ef94Fb3B096 \
    as JSONSchemaValidatorDd469DceE9445C72A3861Ef94Fb3B096_v3_0_0
from .validators.v3_0_0.jsd_dd7a13ef2dea5b9fa6c4d67839133bbf \
    import JSONSchemaValidatorDd7A13Ef2Dea5B9FA6C4D67839133Bbf \
    as JSONSchemaValidatorDd7A13Ef2Dea5B9FA6C4D67839133Bbf_v3_0_0
from .validators.v3_0_0.jsd_ded7f8573c255c318bb1f04bfdbf01e1 \
    import JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1 \
    as JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1_v3_0_0
from .validators.v3_0_0.jsd_df9ab8ff636353279d5c787585dcb6af \
    import JSONSchemaValidatorDf9Ab8Ff636353279D5C787585Dcb6Af \
    as JSONSchemaValidatorDf9Ab8Ff636353279D5C787585Dcb6Af_v3_0_0
from .validators.v3_0_0.jsd_dfaeea899c185169ae2a3b70b5491008 \
    import JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008 \
    as JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008_v3_0_0
from .validators.v3_0_0.jsd_dfc44f7f24d153d789efa48e904b3832 \
    import JSONSchemaValidatorDfc44F7F24D153D789EfA48E904B3832 \
    as JSONSchemaValidatorDfc44F7F24D153D789EfA48E904B3832_v3_0_0
from .validators.v3_0_0.jsd_e09287aba99c56a6a9171b7e3a635a43 \
    import JSONSchemaValidatorE09287AbA99C56A6A9171B7E3A635A43 \
    as JSONSchemaValidatorE09287AbA99C56A6A9171B7E3A635A43_v3_0_0
from .validators.v3_0_0.jsd_e3110fc63ecb5428a075a8af8497fb35 \
    import JSONSchemaValidatorE3110Fc63Ecb5428A075A8Af8497Fb35 \
    as JSONSchemaValidatorE3110Fc63Ecb5428A075A8Af8497Fb35_v3_0_0
from .validators.v3_0_0.jsd_e390313557e95aa9b8c2453d6f1de1e8 \
    import JSONSchemaValidatorE390313557E95Aa9B8C2453D6F1De1E8 \
    as JSONSchemaValidatorE390313557E95Aa9B8C2453D6F1De1E8_v3_0_0
from .validators.v3_0_0.jsd_e4f1e31aca1558f782a2cdb43853aaf2 \
    import JSONSchemaValidatorE4F1E31ACa1558F782A2Cdb43853Aaf2 \
    as JSONSchemaValidatorE4F1E31ACa1558F782A2Cdb43853Aaf2_v3_0_0
from .validators.v3_0_0.jsd_e5f90d642cfa5ee6a1645dd99fb3065e \
    import JSONSchemaValidatorE5F90D642Cfa5Ee6A1645Dd99Fb3065E \
    as JSONSchemaValidatorE5F90D642Cfa5Ee6A1645Dd99Fb3065E_v3_0_0
from .validators.v3_0_0.jsd_e643a5ac8bca55f58ea8d6260c57eafe \
    import JSONSchemaValidatorE643A5Ac8Bca55F58Ea8D6260C57Eafe \
    as JSONSchemaValidatorE643A5Ac8Bca55F58Ea8D6260C57Eafe_v3_0_0
from .validators.v3_0_0.jsd_e82e46732de25832a543c4640312588c \
    import JSONSchemaValidatorE82E46732De25832A543C4640312588C \
    as JSONSchemaValidatorE82E46732De25832A543C4640312588C_v3_0_0
from .validators.v3_0_0.jsd_e84705b918955b53afe61fc37911eb8b \
    import JSONSchemaValidatorE84705B918955B53Afe61Fc37911Eb8B \
    as JSONSchemaValidatorE84705B918955B53Afe61Fc37911Eb8B_v3_0_0
from .validators.v3_0_0.jsd_e9594a91bd735eaabe2eb50038e9d05a \
    import JSONSchemaValidatorE9594A91Bd735EaaBe2EB50038E9D05A \
    as JSONSchemaValidatorE9594A91Bd735EaaBe2EB50038E9D05A_v3_0_0
from .validators.v3_0_0.jsd_eaad68e7996c5562901de57bf5a0420a \
    import JSONSchemaValidatorEaad68E7996C5562901DE57Bf5A0420A \
    as JSONSchemaValidatorEaad68E7996C5562901DE57Bf5A0420A_v3_0_0
from .validators.v3_0_0.jsd_eae60ece5110590e97ddd910e8144ed2 \
    import JSONSchemaValidatorEae60Ece5110590E97DdD910E8144Ed2 \
    as JSONSchemaValidatorEae60Ece5110590E97DdD910E8144Ed2_v3_0_0
from .validators.v3_0_0.jsd_eae98db0c24b5ecca77cce8279e20785 \
    import JSONSchemaValidatorEae98Db0C24B5EccA77CCe8279E20785 \
    as JSONSchemaValidatorEae98Db0C24B5EccA77CCe8279E20785_v3_0_0
from .validators.v3_0_0.jsd_ed4e0ba952525984acfe4a151689c2eb \
    import JSONSchemaValidatorEd4E0Ba952525984Acfe4A151689C2Eb \
    as JSONSchemaValidatorEd4E0Ba952525984Acfe4A151689C2Eb_v3_0_0
from .validators.v3_0_0.jsd_f24049df29d059c48eef86d381ffad5d \
    import JSONSchemaValidatorF24049Df29D059C48Eef86D381Ffad5D \
    as JSONSchemaValidatorF24049Df29D059C48Eef86D381Ffad5D_v3_0_0
from .validators.v3_0_0.jsd_f385b6330ef6500cb599f55407695a3e \
    import JSONSchemaValidatorF385B6330Ef6500CB599F55407695A3E \
    as JSONSchemaValidatorF385B6330Ef6500CB599F55407695A3E_v3_0_0
from .validators.v3_0_0.jsd_f41d844dbee15f7680920652004f69b6 \
    import JSONSchemaValidatorF41D844DBee15F7680920652004F69B6 \
    as JSONSchemaValidatorF41D844DBee15F7680920652004F69B6_v3_0_0
from .validators.v3_0_0.jsd_f46c01449d585b088490c4db530c56d5 \
    import JSONSchemaValidatorF46C01449D585B088490C4Db530C56D5 \
    as JSONSchemaValidatorF46C01449D585B088490C4Db530C56D5_v3_0_0
from .validators.v3_0_0.jsd_f7227b280b745b94bb801369b168a529 \
    import JSONSchemaValidatorF7227B280B745B94Bb801369B168A529 \
    as JSONSchemaValidatorF7227B280B745B94Bb801369B168A529_v3_0_0
from .validators.v3_0_0.jsd_f9661f7c85c2570897cffc3d02668263 \
    import JSONSchemaValidatorF9661F7C85C2570897CfFc3D02668263 \
    as JSONSchemaValidatorF9661F7C85C2570897CfFc3D02668263_v3_0_0
from .validators.v3_0_0.jsd_f9df6a3c6cf953319db3b8c36720997d \
    import JSONSchemaValidatorF9Df6A3C6Cf953319Db3B8C36720997D \
    as JSONSchemaValidatorF9Df6A3C6Cf953319Db3B8C36720997D_v3_0_0
from .validators.v3_0_0.jsd_fc5800b01699562cb563664affdd7757 \
    import JSONSchemaValidatorFc5800B01699562CB563664Affdd7757 \
    as JSONSchemaValidatorFc5800B01699562CB563664Affdd7757_v3_0_0
from .validators.v3_0_0.jsd_fc9a4ee495785518bd2251b6b4fb41f4 \
    import JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4 \
    as JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4_v3_0_0
from .validators.v3_0_0.jsd_fccec47b460255028363021e7936d17a \
    import JSONSchemaValidatorFccec47B460255028363021E7936D17A \
    as JSONSchemaValidatorFccec47B460255028363021E7936D17A_v3_0_0
from .validators.v3_0_0.jsd_fe40d457cbdb5794a5ed2808469ed2e2 \
    import JSONSchemaValidatorFe40D457Cbdb5794A5Ed2808469Ed2E2 \
    as JSONSchemaValidatorFe40D457Cbdb5794A5Ed2808469Ed2E2_v3_0_0


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
            self.json_schema_validators['jsd_6e4f594f8a8980361d0ab9e1_v3_0_0'] =\
                JSONSchemaValidator6E4F594F8A8980361D0Ab9E1_v3_0_0()
            self.json_schema_validators['jsd_de7c6f75f68b0d7df00dc72808d_v3_0_0'] =\
                JSONSchemaValidatorDe7C6F75F68B0D7Df00Dc72808D_v3_0_0()
            self.json_schema_validators['jsd_c7aed7320e54bfac29f13c8717a6b5_v3_0_0'] =\
                JSONSchemaValidatorC7Aed7320E54BfAc29F13C8717A6B5_v3_0_0()
            self.json_schema_validators['jsd_a5a26c964e53b3be3f9f0c103f304c_v3_0_0'] =\
                JSONSchemaValidatorA5A26C964E53B3Be3F9F0C103F304C_v3_0_0()
            self.json_schema_validators['jsd_c21f51995bff8d6468a1e9c0b2e9_v3_0_0'] =\
                JSONSchemaValidatorC21F51995Bff8D6468A1E9C0B2E9_v3_0_0()
            self.json_schema_validators['jsd_be5b1e320e55f4a181370417471d9e_v3_0_0'] =\
                JSONSchemaValidatorBe5B1E320E55F4A181370417471D9E_v3_0_0()
            self.json_schema_validators['jsd_ae4af25df565334b20a24c4878b68e4_v3_0_0'] =\
                JSONSchemaValidatorAe4Af25Df565334B20A24C4878B68E4_v3_0_0()
            self.json_schema_validators['jsd_d39172f68fd5cbd897f03f1440f98a4_v3_0_0'] =\
                JSONSchemaValidatorD39172F68Fd5Cbd897F03F1440F98A4_v3_0_0()
            self.json_schema_validators['jsd_df78c9a3f72584dbd1c7b667b0e312f_v3_0_0'] =\
                JSONSchemaValidatorDf78C9A3F72584DBd1C7B667B0E312F_v3_0_0()
            self.json_schema_validators['jsd_e3e7b0bc717508a979ccac3b986792d_v3_0_0'] =\
                JSONSchemaValidatorE3E7B0BC717508A979CCac3B986792D_v3_0_0()
            self.json_schema_validators['jsd_c23243c950f29b51f502c03d7058_v3_0_0'] =\
                JSONSchemaValidatorC23243C950F29B51F502C03D7058_v3_0_0()
            self.json_schema_validators['jsd_bc936bcb25464b9f3f227647b0443_v3_0_0'] =\
                JSONSchemaValidatorBc936Bcb25464B9F3F227647B0443_v3_0_0()
            self.json_schema_validators['jsd_b05e80058df96e685baa727d578_v3_0_0'] =\
                JSONSchemaValidatorB05E80058Df96E685Baa727D578_v3_0_0()
            self.json_schema_validators['jsd_edcb0e8c6b54709d4d61ea23b45f84_v3_0_0'] =\
                JSONSchemaValidatorEdcb0E8C6B54709D4D61Ea23B45F84_v3_0_0()
            self.json_schema_validators['jsd_b4e8d45639975c226dacd53e7b_v3_0_0'] =\
                JSONSchemaValidatorB4E8D45639975C226Dacd53E7B_v3_0_0()
            self.json_schema_validators['jsd_f6de5797735bbd95dc8683c6a7aebf_v3_0_0'] =\
                JSONSchemaValidatorF6De5797735Bbd95Dc8683C6A7Aebf_v3_0_0()
            self.json_schema_validators['jsd_a693347bdd15bb19d69a75f088498ce_v3_0_0'] =\
                JSONSchemaValidatorA693347Bdd15Bb19D69A75F088498Ce_v3_0_0()
            self.json_schema_validators['jsd_b40ad23ab0a5a7b8adade320c8912e7_v3_0_0'] =\
                JSONSchemaValidatorB40Ad23Ab0A5A7B8AdaDe320C8912E7_v3_0_0()
            self.json_schema_validators['jsd_b84eb28aeb55ab7af7469c854ca1814_v3_0_0'] =\
                JSONSchemaValidatorB84Eb28Aeb55Ab7Af7469C854Ca1814_v3_0_0()
            self.json_schema_validators['jsd_c0689e940ba5526946ad15976cc3365_v3_0_0'] =\
                JSONSchemaValidatorC0689E940Ba5526946AD15976Cc3365_v3_0_0()
            self.json_schema_validators['jsd_cab8440e21553c3a807d23d05e5e1aa_v3_0_0'] =\
                JSONSchemaValidatorCab8440E21553C3A807D23D05E5E1Aa_v3_0_0()
            self.json_schema_validators['jsd_d0290eb241f5bd79221afc8d6cb32da_v3_0_0'] =\
                JSONSchemaValidatorD0290Eb241F5Bd79221Afc8D6Cb32Da_v3_0_0()
            self.json_schema_validators['jsd_d79b507bda155c180d42f0a67ef64d5_v3_0_0'] =\
                JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5_v3_0_0()
            self.json_schema_validators['jsd_f15d19b858d59218ab56b7323ca2fae_v3_0_0'] =\
                JSONSchemaValidatorF15D19B858D59218Ab56B7323Ca2Fae_v3_0_0()
            self.json_schema_validators['jsd_fc1c74b35ae5050b4f7fd702570ad5b_v3_0_0'] =\
                JSONSchemaValidatorFc1C74B35Ae5050B4F7Fd702570Ad5B_v3_0_0()
            self.json_schema_validators['jsd_eb6323be425816a4116eea48f16f4b_v3_0_0'] =\
                JSONSchemaValidatorEb6323Be425816A4116Eea48F16F4B_v3_0_0()
            self.json_schema_validators['jsd_fc6670fd50dfb04b1f6b16981256_v3_0_0'] =\
                JSONSchemaValidatorFc6670Fd50DfB04B1F6B16981256_v3_0_0()
            self.json_schema_validators['jsd_f8082b07ce528f82545e210b84d7de_v3_0_0'] =\
                JSONSchemaValidatorF8082B07Ce528F82545E210B84D7De_v3_0_0()
            self.json_schema_validators['jsd_a746755c588c928d15a59f8a693d_v3_0_0'] =\
                JSONSchemaValidatorA746755C588C928D15A59F8A693D_v3_0_0()
            self.json_schema_validators['jsd_e94f5eba9d9615a3ecc18ebc_v3_0_0'] =\
                JSONSchemaValidatorE94F5Eba9D9615A3Ecc18Ebc_v3_0_0()
            self.json_schema_validators['jsd_a99695fd5ee0b00efce79a5761ff_v3_0_0'] =\
                JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff_v3_0_0()
            self.json_schema_validators['jsd_a31eb33e3535754b3f754a9199e0d25_v3_0_0'] =\
                JSONSchemaValidatorA31Eb33E3535754B3F754A9199E0D25_v3_0_0()
            self.json_schema_validators['jsd_acfdb4060de5a1895b383238c205986_v3_0_0'] =\
                JSONSchemaValidatorAcfdb4060De5A1895B383238C205986_v3_0_0()
            self.json_schema_validators['jsd_d40ae38628c51c49af42a4ede3d66d9_v3_0_0'] =\
                JSONSchemaValidatorD40Ae38628C51C49Af42A4Ede3D66D9_v3_0_0()
            self.json_schema_validators['jsd_d8c7ba0cb8f56d99135e16d2d973d11_v3_0_0'] =\
                JSONSchemaValidatorD8C7Ba0Cb8F56D99135E16D2D973D11_v3_0_0()
            self.json_schema_validators['jsd_ea2c4586b845888b2a9375126f70de2_v3_0_0'] =\
                JSONSchemaValidatorEa2C4586B845888B2A9375126F70De2_v3_0_0()
            self.json_schema_validators['jsd_eb3472c4de150828b2dae61e2285313_v3_0_0'] =\
                JSONSchemaValidatorEb3472C4De150828B2DAe61E2285313_v3_0_0()
            self.json_schema_validators['jsd_e07cb8ea65820863cce345c67926b_v3_0_0'] =\
                JSONSchemaValidatorE07Cb8Ea65820863CCe345C67926B_v3_0_0()
            self.json_schema_validators['jsd_e5dd2909045a90bdce4848865662c2_v3_0_0'] =\
                JSONSchemaValidatorE5Dd2909045A90Bdce4848865662C2_v3_0_0()
            self.json_schema_validators['jsd_edfca30e8e514d9bab840c3c2d4c0f_v3_0_0'] =\
                JSONSchemaValidatorEdfca30E8E514D9Bab840C3C2D4C0F_v3_0_0()
            self.json_schema_validators['jsd_e38d10b1ea257d49ebce893e87b3419_v3_0_0'] =\
                JSONSchemaValidatorE38D10B1Ea257D49EbcE893E87B3419_v3_0_0()
            self.json_schema_validators['jsd_c4fada6c558d9aba09cc373d5b266_v3_0_0'] =\
                JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0()
            self.json_schema_validators['jsd_fa27e5a779143ed557b417535_v3_0_0'] =\
                JSONSchemaValidatorFA27E5A779143Ed557B417535_v3_0_0()
            self.json_schema_validators['jsd_b11e2f1af656bcb5880a7b33720ec5_v3_0_0'] =\
                JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0()
            self.json_schema_validators['jsd_ce666e64a958229cfd8da70945935e_v3_0_0'] =\
                JSONSchemaValidatorCe666E64A958229Cfd8Da70945935E_v3_0_0()
            self.json_schema_validators['jsd_e1af4e392c5790a01685b9687208c0_v3_0_0'] =\
                JSONSchemaValidatorE1Af4E392C5790A01685B9687208C0_v3_0_0()
            self.json_schema_validators['jsd_a9f304a4ec54afa6e3484978aacbbb_v3_0_0'] =\
                JSONSchemaValidatorA9F304A4Ec54AfA6E3484978Aacbbb_v3_0_0()
            self.json_schema_validators['jsd_19d9509db339e3b27dc56b37_v3_0_0'] =\
                JSONSchemaValidator19D9509DB339E3B27Dc56B37_v3_0_0()
            self.json_schema_validators['jsd_fd729f50e65695966359b589a1606b_v3_0_0'] =\
                JSONSchemaValidatorFd729F50E65695966359B589A1606B_v3_0_0()
            self.json_schema_validators['jsd_fac48e5c63abfe2feec6fd1903_v3_0_0'] =\
                JSONSchemaValidatorFaC48E5C63Abfe2Feec6Fd1903_v3_0_0()
            self.json_schema_validators['jsd_a0db9ec45c05879a6f016a1edf54793_v3_0_0'] =\
                JSONSchemaValidatorA0Db9Ec45C05879A6F016A1Edf54793_v3_0_0()
            self.json_schema_validators['jsd_d67f9f6fba65dcbbcf64ca3e31b39a6_v3_0_0'] =\
                JSONSchemaValidatorD67F9F6Fba65DcbBcf64Ca3E31B39A6_v3_0_0()
            self.json_schema_validators['jsd_dd838b268f5dd298a123ac58448ea9_v3_0_0'] =\
                JSONSchemaValidatorDd838B268F5Dd298A123Ac58448Ea9_v3_0_0()
            self.json_schema_validators['jsd_1872577f8d1efe131783009c_v3_0_0'] =\
                JSONSchemaValidator1872577F8D1EFe131783009C_v3_0_0()
            self.json_schema_validators['jsd_d31fa60f5575a2ed23cee473c0fc_v3_0_0'] =\
                JSONSchemaValidatorD31FA60F5575A2Ed23Cee473C0Fc_v3_0_0()
            self.json_schema_validators['jsd_a3c8e0ddc5b40a250affc4be1700a_v3_0_0'] =\
                JSONSchemaValidatorA3C8E0Ddc5B40A250Affc4Be1700A_v3_0_0()
            self.json_schema_validators['jsd_c2e3af6da356009f6499f00a4115e9_v3_0_0'] =\
                JSONSchemaValidatorC2E3Af6Da356009F6499F00A4115E9_v3_0_0()
            self.json_schema_validators['jsd_acd30d35ee2ae16ff23757de7d8_v3_0_0'] =\
                JSONSchemaValidatorAcd30D35Ee2Ae16Ff23757De7D8_v3_0_0()
            self.json_schema_validators['jsd_cea2e785ee57908a9ee3b118e49cfa_v3_0_0'] =\
                JSONSchemaValidatorCea2E785Ee57908A9EE3B118E49Cfa_v3_0_0()
            self.json_schema_validators['jsd_ca6ab8ec556c3bc9531dc380b230a_v3_0_0'] =\
                JSONSchemaValidatorCa6Ab8Ec556C3Bc9531Dc380B230A_v3_0_0()
            self.json_schema_validators['jsd_ac3ccf225801ad8ba0bb1ad9de0b_v3_0_0'] =\
                JSONSchemaValidatorAc3CCf225801Ad8BA0Bb1Ad9De0B_v3_0_0()
            self.json_schema_validators['jsd_ad69fa1d850f4993bbfc888749fa0_v3_0_0'] =\
                JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0()
            self.json_schema_validators['jsd_a1e26e595667bd98f84dd29232e2_v3_0_0'] =\
                JSONSchemaValidatorA1E26E595667Bd98F84Dd29232E2_v3_0_0()
            self.json_schema_validators['jsd_bf19f653f9a5c48d1fb1890409_v3_0_0'] =\
                JSONSchemaValidatorBf19F653F9A5C48D1Fb1890409_v3_0_0()
            self.json_schema_validators['jsd_e6167fc5cb6593b8b48429187a26a67_v3_0_0'] =\
                JSONSchemaValidatorE6167Fc5Cb6593B8B48429187A26A67_v3_0_0()
            self.json_schema_validators['jsd_a0b312f70257b1bfa90d0260f0c971_v3_0_0'] =\
                JSONSchemaValidatorA0B312F70257B1Bfa90D0260F0C971_v3_0_0()
            self.json_schema_validators['jsd_c9daa26d4b5b80a41d4b7ff9359380_v3_0_0'] =\
                JSONSchemaValidatorC9Daa26D4B5B80A41D4B7Ff9359380_v3_0_0()
            self.json_schema_validators['jsd_ad8eb56595e86c4300607ec4dd3_v3_0_0'] =\
                JSONSchemaValidatorAd8Eb56595E86C4300607Ec4Dd3_v3_0_0()
            self.json_schema_validators['jsd_f014ee45351ba163e3be6fa217b_v3_0_0'] =\
                JSONSchemaValidatorF014Ee45351Ba163E3Be6Fa217B_v3_0_0()
            self.json_schema_validators['jsd_b2eebd5c245e58a503aa53115eec53_v3_0_0'] =\
                JSONSchemaValidatorB2Eebd5C245E58A503Aa53115Eec53_v3_0_0()
            self.json_schema_validators['jsd_c560004d8b5f64a10f2cc070368c12_v3_0_0'] =\
                JSONSchemaValidatorC560004D8B5F64A10F2Cc070368C12_v3_0_0()
            self.json_schema_validators['jsd_e9318040a456978757d7abfa3e66b1_v3_0_0'] =\
                JSONSchemaValidatorE9318040A456978757D7Abfa3E66B1_v3_0_0()
            self.json_schema_validators['jsd_c1fa3bf115c77be99b602aca1493b_v3_0_0'] =\
                JSONSchemaValidatorC1Fa3Bf115C77Be99B602Aca1493B_v3_0_0()
            self.json_schema_validators['jsd_a48341446b15729abf624695b20b9f5_v3_0_0'] =\
                JSONSchemaValidatorA48341446B15729Abf624695B20B9F5_v3_0_0()
            self.json_schema_validators['jsd_c38fb2e2dd45f4dab6ec3a19effd15a_v3_0_0'] =\
                JSONSchemaValidatorC38Fb2E2Dd45F4DAb6EC3A19Effd15A_v3_0_0()
            self.json_schema_validators['jsd_cc0a87094bf5d96af61403dfc3747db_v3_0_0'] =\
                JSONSchemaValidatorCc0A87094Bf5D96Af61403Dfc3747Db_v3_0_0()
            self.json_schema_validators['jsd_be755dae5251bd2d8348eeebfdde_v3_0_0'] =\
                JSONSchemaValidatorBe755Dae5251Bd2D8348Eeebfdde_v3_0_0()
            self.json_schema_validators['jsd_70e85c38bcad4249948c550b_v3_0_0'] =\
                JSONSchemaValidator70E85C38Bcad4249948C550B_v3_0_0()
            self.json_schema_validators['jsd_e6e4b7d022556a80f1948efb3d5c61_v3_0_0'] =\
                JSONSchemaValidatorE6E4B7D022556A80F1948Efb3D5C61_v3_0_0()
            self.json_schema_validators['jsd_e92c5af5344b4d9fdc45a282ce5_v3_0_0'] =\
                JSONSchemaValidatorE92C5Af5344B4D9Fdc45A282Ce5_v3_0_0()
            self.json_schema_validators['jsd_6d125b968b9d362a3458621d_v3_0_0'] =\
                JSONSchemaValidator6D125B968B9D362A3458621D_v3_0_0()
            self.json_schema_validators['jsd_f7bd03a835c95b7a759b39ce7f680_v3_0_0'] =\
                JSONSchemaValidatorF7Bd03A835C95B7A759B39Ce7F680_v3_0_0()
            self.json_schema_validators['jsd_ad357457f45e07a13674d462c4270d_v3_0_0'] =\
                JSONSchemaValidatorAd357457F45E07A13674D462C4270D_v3_0_0()
            self.json_schema_validators['jsd_9f955525b0b38a57a3bed311_v3_0_0'] =\
                JSONSchemaValidator9F955525B0B38A57A3Bed311_v3_0_0()
            self.json_schema_validators['jsd_c39f0f97cb53e19a03f2ea53f5b831_v3_0_0'] =\
                JSONSchemaValidatorC39F0F97Cb53E19A03F2Ea53F5B831_v3_0_0()
            self.json_schema_validators['jsd_e5dd9b5979a409b9f456265db0_v3_0_0'] =\
                JSONSchemaValidatorE5Dd9B5979A409B9F456265Db0_v3_0_0()
            self.json_schema_validators['jsd_c371214c759f791c0a522b9eaf5b5_v3_0_0'] =\
                JSONSchemaValidatorC371214C759F791C0A522B9Eaf5B5_v3_0_0()
            self.json_schema_validators['jsd_a7cffe3bfae55aa81b7b4447519e4cd_v3_0_0'] =\
                JSONSchemaValidatorA7Cffe3Bfae55Aa81B7B4447519E4Cd_v3_0_0()
            self.json_schema_validators['jsd_da250e23ac05e6a8dcf32a81effcee9_v3_0_0'] =\
                JSONSchemaValidatorDa250E23Ac05E6A8Dcf32A81Effcee9_v3_0_0()
            self.json_schema_validators['jsd_e6734850fabb2097fa969948cb_v3_0_0'] =\
                JSONSchemaValidatorE6734850FaBb2097Fa969948Cb_v3_0_0()
            self.json_schema_validators['jsd_e84541805d1da1fa3d4d581102a9_v3_0_0'] =\
                JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9_v3_0_0()
            self.json_schema_validators['jsd_c64b769537ea7c586565f6ed2a2_v3_0_0'] =\
                JSONSchemaValidatorC64B769537EA7C586565F6Ed2A2_v3_0_0()
            self.json_schema_validators['jsd_ad6ca0642c5750af6ca9905721a9d7_v3_0_0'] =\
                JSONSchemaValidatorAd6Ca0642C5750Af6CA9905721A9D7_v3_0_0()
            self.json_schema_validators['jsd_ea4e38c44e5b1c90b19af25b88546e_v3_0_0'] =\
                JSONSchemaValidatorEa4E38C44E5B1C90B19Af25B88546E_v3_0_0()
            self.json_schema_validators['jsd_a5fd2b5d5306b9941387f400c7a0_v3_0_0'] =\
                JSONSchemaValidatorA5Fd2B5D5306B9941387F400C7A0_v3_0_0()
            self.json_schema_validators['jsd_ab88be5092bf4ba9f522e8e26f_v3_0_0'] =\
                JSONSchemaValidatorAb88Be5092Bf4BA9F522E8E26F_v3_0_0()
            self.json_schema_validators['jsd_cf67e0155eab895b50d1a377f21_v3_0_0'] =\
                JSONSchemaValidatorCf67E0155EaB895B50D1A377F21_v3_0_0()
            self.json_schema_validators['jsd_ade26d445251a45cc753f68d21bc_v3_0_0'] =\
                JSONSchemaValidatorAde26D445251A45CC753F68D21Bc_v3_0_0()
            self.json_schema_validators['jsd_ad86a47e15d45ab1cc0cadc5b248f_v3_0_0'] =\
                JSONSchemaValidatorAd86A47E15D45Ab1CC0Cadc5B248F_v3_0_0()
            self.json_schema_validators['jsd_bd1af169fa52c59cbc87b010c36f9e_v3_0_0'] =\
                JSONSchemaValidatorBd1Af169Fa52C59Cbc87B010C36F9E_v3_0_0()
            self.json_schema_validators['jsd_b9c7c5847b17684c49399ff95_v3_0_0'] =\
                JSONSchemaValidatorB9C7C5847B17684C49399Ff95_v3_0_0()
            self.json_schema_validators['jsd_f7cf06a1655d6da606ace9b0950bcf_v3_0_0'] =\
                JSONSchemaValidatorF7Cf06A1655D6DA606Ace9B0950Bcf_v3_0_0()
            self.json_schema_validators['jsd_e27d5df9cbe5b29a7e16bb7c877a4ce_v3_0_0'] =\
                JSONSchemaValidatorE27D5Df9Cbe5B29A7E16Bb7C877A4Ce_v3_0_0()
            self.json_schema_validators['jsd_b93b991556cae0fdd562c5e3f63_v3_0_0'] =\
                JSONSchemaValidatorB93B991556CAe0FDd562C5E3F63_v3_0_0()
            self.json_schema_validators['jsd_eb833980f55025bfacbfcb8de814c8_v3_0_0'] =\
                JSONSchemaValidatorEb833980F55025BfacBfcb8De814C8_v3_0_0()
            self.json_schema_validators['jsd_de3cecd62e5153881245a8613fbeea_v3_0_0'] =\
                JSONSchemaValidatorDe3CecD62E5153881245A8613Fbeea_v3_0_0()
            self.json_schema_validators['jsd_d0006cc03d53c89a3593526bf8dc0f_v3_0_0'] =\
                JSONSchemaValidatorD0006CC03D53C89A3593526Bf8Dc0F_v3_0_0()
            self.json_schema_validators['jsd_a0710ba581da4d3fd00e84d59e3_v3_0_0'] =\
                JSONSchemaValidatorA0710Ba581DA4D3Fd00E84D59E3_v3_0_0()
            self.json_schema_validators['jsd_b30f809e275589bd7154b5b4093d3f_v3_0_0'] =\
                JSONSchemaValidatorB30F809E275589Bd7154B5B4093D3F_v3_0_0()
            self.json_schema_validators['jsd_c8ffe8c6095203a83131f49d4c8bb2_v3_0_0'] =\
                JSONSchemaValidatorC8Ffe8C6095203A83131F49D4C8Bb2_v3_0_0()
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
            self.json_schema_validators['jsd_d3034483aaa5563bb287ef0cd502130_v3_0_0'] =\
                JSONSchemaValidatorD3034483Aaa5563Bb287Ef0Cd502130_v3_0_0()
            self.json_schema_validators['jsd_f47dca835fa58fcb08bcdd672dfbaa7_v3_0_0'] =\
                JSONSchemaValidatorF47Dca835Fa58FcB08BCdd672Dfbaa7_v3_0_0()
            self.json_schema_validators['jsd_a39fa17ffcd45736aa221dd27916e843_v3_0_0'] =\
                JSONSchemaValidatorA39Fa17FFcd45736Aa221Dd27916E843_v3_0_0()
            self.json_schema_validators['jsd_a7500f6e473a50e19452683e303dd021_v3_0_0'] =\
                JSONSchemaValidatorA7500F6E473A50E19452683E303Dd021_v3_0_0()
            self.json_schema_validators['jsd_aa333658bf83576eb36a025283516518_v3_0_0'] =\
                JSONSchemaValidatorAa333658Bf83576EB36A025283516518_v3_0_0()
            self.json_schema_validators['jsd_ab203a1dd0015924bf2005a84ae85477_v3_0_0'] =\
                JSONSchemaValidatorAb203A1DD0015924Bf2005A84Ae85477_v3_0_0()
            self.json_schema_validators['jsd_adcf947c42fe5588b7b82d9c43a3bbf0_v3_0_0'] =\
                JSONSchemaValidatorAdcf947C42Fe5588B7B82D9C43A3Bbf0_v3_0_0()
            self.json_schema_validators['jsd_adde5bf7c9185218b955ff0c365fcc4c_v3_0_0'] =\
                JSONSchemaValidatorAdde5Bf7C9185218B955Ff0C365Fcc4C_v3_0_0()
            self.json_schema_validators['jsd_afc81cd1e25c50319f75606b97c23b3d_v3_0_0'] =\
                JSONSchemaValidatorAfc81Cd1E25C50319F75606B97C23B3D_v3_0_0()
            self.json_schema_validators['jsd_afcce33ec863567f94f3b9b73719ff8d_v3_0_0'] =\
                JSONSchemaValidatorAfcce33EC863567F94F3B9B73719Ff8D_v3_0_0()
            self.json_schema_validators['jsd_b14d63c641e95ac0a8c2da2fb65909c7_v3_0_0'] =\
                JSONSchemaValidatorB14D63C641E95Ac0A8C2Da2Fb65909C7_v3_0_0()
            self.json_schema_validators['jsd_b1edfeb182025176bb250633937177ae_v3_0_0'] =\
                JSONSchemaValidatorB1Edfeb182025176Bb250633937177Ae_v3_0_0()
            self.json_schema_validators['jsd_b3284240745e5b929c51495fe80bc1c4_v3_0_0'] =\
                JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4_v3_0_0()
            self.json_schema_validators['jsd_b5097e4db7505ba390914b50b1c2046b_v3_0_0'] =\
                JSONSchemaValidatorB5097E4DB7505Ba390914B50B1C2046B_v3_0_0()
            self.json_schema_validators['jsd_b5151e49a2b65befb488985ed973fed2_v3_0_0'] =\
                JSONSchemaValidatorB5151E49A2B65BefB488985Ed973Fed2_v3_0_0()
            self.json_schema_validators['jsd_b734aeeb768d568684706bff5e3fa5bb_v3_0_0'] =\
                JSONSchemaValidatorB734Aeeb768D568684706Bff5E3Fa5Bb_v3_0_0()
            self.json_schema_validators['jsd_b839d4dee9b958e48ccef056603e253f_v3_0_0'] =\
                JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F_v3_0_0()
            self.json_schema_validators['jsd_b84dbd77c49f5056b9bf3c1e496ebe5f_v3_0_0'] =\
                JSONSchemaValidatorB84Dbd77C49F5056B9Bf3C1E496Ebe5F_v3_0_0()
            self.json_schema_validators['jsd_b9500d6c2f365927aa3dbe6d7ecbae22_v3_0_0'] =\
                JSONSchemaValidatorB9500D6C2F365927Aa3DBe6D7Ecbae22_v3_0_0()
            self.json_schema_validators['jsd_b9638a67f60d5a6aa476af13632d96bd_v3_0_0'] =\
                JSONSchemaValidatorB9638A67F60D5A6AA476Af13632D96Bd_v3_0_0()
            self.json_schema_validators['jsd_b9de636ff2e25f849f468556c53b7b9a_v3_0_0'] =\
                JSONSchemaValidatorB9De636FF2E25F849F468556C53B7B9A_v3_0_0()
            self.json_schema_validators['jsd_bac6d4d95ac45a0a8933b8712dcbe70d_v3_0_0'] =\
                JSONSchemaValidatorBac6D4D95Ac45A0A8933B8712Dcbe70D_v3_0_0()
            self.json_schema_validators['jsd_bd8691c5d9435e48a3c7a08658bda585_v3_0_0'] =\
                JSONSchemaValidatorBd8691C5D9435E48A3C7A08658Bda585_v3_0_0()
            self.json_schema_validators['jsd_bf175c04fcb051b9a6fd70a2252903fa_v3_0_0'] =\
                JSONSchemaValidatorBf175C04Fcb051B9A6Fd70A2252903Fa_v3_0_0()
            self.json_schema_validators['jsd_c03505504e8e5af8a715e27c40f16eab_v3_0_0'] =\
                JSONSchemaValidatorC03505504E8E5Af8A715E27C40F16Eab_v3_0_0()
            self.json_schema_validators['jsd_c094086382485201ad36d4641fc6822e_v3_0_0'] =\
                JSONSchemaValidatorC094086382485201Ad36D4641Fc6822E_v3_0_0()
            self.json_schema_validators['jsd_c26e318c3c405713a55b4e162be8c890_v3_0_0'] =\
                JSONSchemaValidatorC26E318C3C405713A55B4E162Be8C890_v3_0_0()
            self.json_schema_validators['jsd_c54a2ad63f46527dbec140a05f1213b7_v3_0_0'] =\
                JSONSchemaValidatorC54A2Ad63F46527DBec140A05F1213B7_v3_0_0()
            self.json_schema_validators['jsd_c730e85640aa5a59bc0e0fd95dacf889_v3_0_0'] =\
                JSONSchemaValidatorC730E85640Aa5A59Bc0E0Fd95Dacf889_v3_0_0()
            self.json_schema_validators['jsd_c82dcf6f2c3d5d399045050b02208db2_v3_0_0'] =\
                JSONSchemaValidatorC82Dcf6F2C3D5D399045050B02208Db2_v3_0_0()
            self.json_schema_validators['jsd_c85464a04f0e5ddc99f8e6b8ed0f7eac_v3_0_0'] =\
                JSONSchemaValidatorC85464A04F0E5Ddc99F8E6B8Ed0F7Eac_v3_0_0()
            self.json_schema_validators['jsd_c8b30af4b84b5a90be2fc152cf26ad42_v3_0_0'] =\
                JSONSchemaValidatorC8B30Af4B84B5A90Be2FC152Cf26Ad42_v3_0_0()
            self.json_schema_validators['jsd_c97e7851003e5a63a2a8005ac8807dc7_v3_0_0'] =\
                JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7_v3_0_0()
            self.json_schema_validators['jsd_ca78559d8a9f559c87f53ea85169a2c7_v3_0_0'] =\
                JSONSchemaValidatorCa78559D8A9F559C87F53Ea85169A2C7_v3_0_0()
            self.json_schema_validators['jsd_cd32d094f1815c388d1392bb90f3744d_v3_0_0'] =\
                JSONSchemaValidatorCd32D094F1815C388D1392Bb90F3744D_v3_0_0()
            self.json_schema_validators['jsd_ce788c3408de5056a2e71955f86d6f05_v3_0_0'] =\
                JSONSchemaValidatorCe788C3408De5056A2E71955F86D6F05_v3_0_0()
            self.json_schema_validators['jsd_ce83fba942c25938bae0c7012df68317_v3_0_0'] =\
                JSONSchemaValidatorCe83Fba942C25938Bae0C7012Df68317_v3_0_0()
            self.json_schema_validators['jsd_d011417d18d055ccb864c1dc2ae0456d_v3_0_0'] =\
                JSONSchemaValidatorD011417D18D055CcB864C1Dc2Ae0456D_v3_0_0()
            self.json_schema_validators['jsd_d1f92a9024975e9dad6114255be546bd_v3_0_0'] =\
                JSONSchemaValidatorD1F92A9024975E9DAd6114255Be546Bd_v3_0_0()
            self.json_schema_validators['jsd_d30aa7529c245c549eafde4c17a809a4_v3_0_0'] =\
                JSONSchemaValidatorD30Aa7529C245C549EafDe4C17A809A4_v3_0_0()
            self.json_schema_validators['jsd_d524614e122d53d68324daf1681eb753_v3_0_0'] =\
                JSONSchemaValidatorD524614E122D53D68324Daf1681Eb753_v3_0_0()
            self.json_schema_validators['jsd_d9cc879878ee5a34ac1c32f2f0cb8c6d_v3_0_0'] =\
                JSONSchemaValidatorD9Cc879878Ee5A34Ac1C32F2F0Cb8C6D_v3_0_0()
            self.json_schema_validators['jsd_da5ac537bf475538b7bc42c8cce2e530_v3_0_0'] =\
                JSONSchemaValidatorDa5Ac537Bf475538B7Bc42C8Cce2E530_v3_0_0()
            self.json_schema_validators['jsd_db3505847b4e5f37a5c74bc41df54be3_v3_0_0'] =\
                JSONSchemaValidatorDb3505847B4E5F37A5C74Bc41Df54Be3_v3_0_0()
            self.json_schema_validators['jsd_dd4581dd32f65e8c83cca2f0a97af3e2_v3_0_0'] =\
                JSONSchemaValidatorDd4581Dd32F65E8C83CcA2F0A97Af3E2_v3_0_0()
            self.json_schema_validators['jsd_dd469dcee9445c72a3861ef94fb3b096_v3_0_0'] =\
                JSONSchemaValidatorDd469DceE9445C72A3861Ef94Fb3B096_v3_0_0()
            self.json_schema_validators['jsd_dd7a13ef2dea5b9fa6c4d67839133bbf_v3_0_0'] =\
                JSONSchemaValidatorDd7A13Ef2Dea5B9FA6C4D67839133Bbf_v3_0_0()
            self.json_schema_validators['jsd_ded7f8573c255c318bb1f04bfdbf01e1_v3_0_0'] =\
                JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1_v3_0_0()
            self.json_schema_validators['jsd_df9ab8ff636353279d5c787585dcb6af_v3_0_0'] =\
                JSONSchemaValidatorDf9Ab8Ff636353279D5C787585Dcb6Af_v3_0_0()
            self.json_schema_validators['jsd_dfaeea899c185169ae2a3b70b5491008_v3_0_0'] =\
                JSONSchemaValidatorDfaeea899C185169Ae2A3B70B5491008_v3_0_0()
            self.json_schema_validators['jsd_dfc44f7f24d153d789efa48e904b3832_v3_0_0'] =\
                JSONSchemaValidatorDfc44F7F24D153D789EfA48E904B3832_v3_0_0()
            self.json_schema_validators['jsd_e09287aba99c56a6a9171b7e3a635a43_v3_0_0'] =\
                JSONSchemaValidatorE09287AbA99C56A6A9171B7E3A635A43_v3_0_0()
            self.json_schema_validators['jsd_e3110fc63ecb5428a075a8af8497fb35_v3_0_0'] =\
                JSONSchemaValidatorE3110Fc63Ecb5428A075A8Af8497Fb35_v3_0_0()
            self.json_schema_validators['jsd_e390313557e95aa9b8c2453d6f1de1e8_v3_0_0'] =\
                JSONSchemaValidatorE390313557E95Aa9B8C2453D6F1De1E8_v3_0_0()
            self.json_schema_validators['jsd_e4f1e31aca1558f782a2cdb43853aaf2_v3_0_0'] =\
                JSONSchemaValidatorE4F1E31ACa1558F782A2Cdb43853Aaf2_v3_0_0()
            self.json_schema_validators['jsd_e5f90d642cfa5ee6a1645dd99fb3065e_v3_0_0'] =\
                JSONSchemaValidatorE5F90D642Cfa5Ee6A1645Dd99Fb3065E_v3_0_0()
            self.json_schema_validators['jsd_e643a5ac8bca55f58ea8d6260c57eafe_v3_0_0'] =\
                JSONSchemaValidatorE643A5Ac8Bca55F58Ea8D6260C57Eafe_v3_0_0()
            self.json_schema_validators['jsd_e82e46732de25832a543c4640312588c_v3_0_0'] =\
                JSONSchemaValidatorE82E46732De25832A543C4640312588C_v3_0_0()
            self.json_schema_validators['jsd_e84705b918955b53afe61fc37911eb8b_v3_0_0'] =\
                JSONSchemaValidatorE84705B918955B53Afe61Fc37911Eb8B_v3_0_0()
            self.json_schema_validators['jsd_e9594a91bd735eaabe2eb50038e9d05a_v3_0_0'] =\
                JSONSchemaValidatorE9594A91Bd735EaaBe2EB50038E9D05A_v3_0_0()
            self.json_schema_validators['jsd_eaad68e7996c5562901de57bf5a0420a_v3_0_0'] =\
                JSONSchemaValidatorEaad68E7996C5562901DE57Bf5A0420A_v3_0_0()
            self.json_schema_validators['jsd_eae60ece5110590e97ddd910e8144ed2_v3_0_0'] =\
                JSONSchemaValidatorEae60Ece5110590E97DdD910E8144Ed2_v3_0_0()
            self.json_schema_validators['jsd_eae98db0c24b5ecca77cce8279e20785_v3_0_0'] =\
                JSONSchemaValidatorEae98Db0C24B5EccA77CCe8279E20785_v3_0_0()
            self.json_schema_validators['jsd_ed4e0ba952525984acfe4a151689c2eb_v3_0_0'] =\
                JSONSchemaValidatorEd4E0Ba952525984Acfe4A151689C2Eb_v3_0_0()
            self.json_schema_validators['jsd_f24049df29d059c48eef86d381ffad5d_v3_0_0'] =\
                JSONSchemaValidatorF24049Df29D059C48Eef86D381Ffad5D_v3_0_0()
            self.json_schema_validators['jsd_f385b6330ef6500cb599f55407695a3e_v3_0_0'] =\
                JSONSchemaValidatorF385B6330Ef6500CB599F55407695A3E_v3_0_0()
            self.json_schema_validators['jsd_f41d844dbee15f7680920652004f69b6_v3_0_0'] =\
                JSONSchemaValidatorF41D844DBee15F7680920652004F69B6_v3_0_0()
            self.json_schema_validators['jsd_f46c01449d585b088490c4db530c56d5_v3_0_0'] =\
                JSONSchemaValidatorF46C01449D585B088490C4Db530C56D5_v3_0_0()
            self.json_schema_validators['jsd_f7227b280b745b94bb801369b168a529_v3_0_0'] =\
                JSONSchemaValidatorF7227B280B745B94Bb801369B168A529_v3_0_0()
            self.json_schema_validators['jsd_f9661f7c85c2570897cffc3d02668263_v3_0_0'] =\
                JSONSchemaValidatorF9661F7C85C2570897CfFc3D02668263_v3_0_0()
            self.json_schema_validators['jsd_f9df6a3c6cf953319db3b8c36720997d_v3_0_0'] =\
                JSONSchemaValidatorF9Df6A3C6Cf953319Db3B8C36720997D_v3_0_0()
            self.json_schema_validators['jsd_fc5800b01699562cb563664affdd7757_v3_0_0'] =\
                JSONSchemaValidatorFc5800B01699562CB563664Affdd7757_v3_0_0()
            self.json_schema_validators['jsd_fc9a4ee495785518bd2251b6b4fb41f4_v3_0_0'] =\
                JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4_v3_0_0()
            self.json_schema_validators['jsd_fccec47b460255028363021e7936d17a_v3_0_0'] =\
                JSONSchemaValidatorFccec47B460255028363021E7936D17A_v3_0_0()
            self.json_schema_validators['jsd_fe40d457cbdb5794a5ed2808469ed2e2_v3_0_0'] =\
                JSONSchemaValidatorFe40D457Cbdb5794A5Ed2808469Ed2E2_v3_0_0()

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
