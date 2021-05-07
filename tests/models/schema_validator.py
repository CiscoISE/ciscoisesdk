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
from .validators.v3_0_0.jsd_ac8c8cb9b5007a1e1a6434a20a881 \
    import JSONSchemaValidatorAc8C8Cb9B5007A1E1A6434A20A881 \
    as JSONSchemaValidatorAc8C8Cb9B5007A1E1A6434A20A881_v3_0_0
from .validators.v3_0_0.jsd_d6b1385f4cb9381c13a1fa4356 \
    import JSONSchemaValidatorD6B1385F4CB9381C13A1Fa4356 \
    as JSONSchemaValidatorD6B1385F4CB9381C13A1Fa4356_v3_0_0
from .validators.v3_0_0.jsd_daa171ab765a02a714c48376b3790d \
    import JSONSchemaValidatorDaa171Ab765A02A714C48376B3790D \
    as JSONSchemaValidatorDaa171Ab765A02A714C48376B3790D_v3_0_0
from .validators.v3_0_0.jsd_fde0cbd2de50f680d0b0f681771829 \
    import JSONSchemaValidatorFde0CbD2De50F680D0B0F681771829 \
    as JSONSchemaValidatorFde0CbD2De50F680D0B0F681771829_v3_0_0
from .validators.v3_0_0.jsd_d8f04f3635c6c9e6e94f76fe8cf7b \
    import JSONSchemaValidatorD8F04F3635C6C9E6E94F76Fe8Cf7B \
    as JSONSchemaValidatorD8F04F3635C6C9E6E94F76Fe8Cf7B_v3_0_0
from .validators.v3_0_0.jsd_fbd7ec7052709e5d0e0a46dc7f68 \
    import JSONSchemaValidatorFbd7Ec7052709E5D0E0A46Dc7F68 \
    as JSONSchemaValidatorFbd7Ec7052709E5D0E0A46Dc7F68_v3_0_0
from .validators.v3_0_0.jsd_f9f734e2f058f59e13801f1ed4780e \
    import JSONSchemaValidatorF9F734E2F058F59E13801F1Ed4780E \
    as JSONSchemaValidatorF9F734E2F058F59E13801F1Ed4780E_v3_0_0
from .validators.v3_0_0.jsd_db1d9dda53369e35d33138b29c16 \
    import JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16 \
    as JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16_v3_0_0
from .validators.v3_0_0.jsd_e3c94fb105cd4a6eac4ace8c87f9f \
    import JSONSchemaValidatorE3C94Fb105Cd4A6EaC4Ace8C87F9F \
    as JSONSchemaValidatorE3C94Fb105Cd4A6EaC4Ace8C87F9F_v3_0_0
from .validators.v3_0_0.jsd_e4686a7511884fd3eee7c582efb \
    import JSONSchemaValidatorE4686A7511884Fd3Eee7C582Efb \
    as JSONSchemaValidatorE4686A7511884Fd3Eee7C582Efb_v3_0_0
from .validators.v3_0_0.jsd_d5a4d54609f344c0d766b7c16 \
    import JSONSchemaValidatorD5A4D54609F344C0D766B7C16 \
    as JSONSchemaValidatorD5A4D54609F344C0D766B7C16_v3_0_0
from .validators.v3_0_0.jsd_da54f237752bd84ccfc8341f89bf8 \
    import JSONSchemaValidatorDa54F237752Bd84CcFc8341F89Bf8 \
    as JSONSchemaValidatorDa54F237752Bd84CcFc8341F89Bf8_v3_0_0
from .validators.v3_0_0.jsd_ac243ecb8c157658a4bcfe77a102c14 \
    import JSONSchemaValidatorAc243EcB8C157658A4BCfe77A102C14 \
    as JSONSchemaValidatorAc243EcB8C157658A4BCfe77A102C14_v3_0_0
from .validators.v3_0_0.jsd_ad47b73307755749ca8182a34affb38 \
    import JSONSchemaValidatorAd47B73307755749Ca8182A34Affb38 \
    as JSONSchemaValidatorAd47B73307755749Ca8182A34Affb38_v3_0_0
from .validators.v3_0_0.jsd_cdc971b23285b87945021bd5983d1cd \
    import JSONSchemaValidatorCdc971B23285B87945021Bd5983D1Cd \
    as JSONSchemaValidatorCdc971B23285B87945021Bd5983D1Cd_v3_0_0
from .validators.v3_0_0.jsd_d1df0e230765104863b8d63d5beb68e \
    import JSONSchemaValidatorD1Df0E230765104863B8D63D5Beb68E \
    as JSONSchemaValidatorD1Df0E230765104863B8D63D5Beb68E_v3_0_0
from .validators.v3_0_0.jsd_f41a1e47105581fabf212f259626903 \
    import JSONSchemaValidatorF41A1E47105581FAbf212F259626903 \
    as JSONSchemaValidatorF41A1E47105581FAbf212F259626903_v3_0_0
from .validators.v3_0_0.jsd_e34177d675622acd0a532f5b7c41b \
    import JSONSchemaValidatorE34177D675622Acd0A532F5B7C41B \
    as JSONSchemaValidatorE34177D675622Acd0A532F5B7C41B_v3_0_0
from .validators.v3_0_0.jsd_f8f4956d29b821fa9bbf23266 \
    import JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266 \
    as JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266_v3_0_0
from .validators.v3_0_0.jsd_ab05dc6105e47b391030a5fe50ecb \
    import JSONSchemaValidatorAb05DC6105E47B391030A5Fe50Ecb \
    as JSONSchemaValidatorAb05DC6105E47B391030A5Fe50Ecb_v3_0_0
from .validators.v3_0_0.jsd_ebcdc835e9b8d6844c1da6cf252 \
    import JSONSchemaValidatorEbcDc835E9B8D6844C1Da6Cf252 \
    as JSONSchemaValidatorEbcDc835E9B8D6844C1Da6Cf252_v3_0_0
from .validators.v3_0_0.jsd_3bfe54779ae1b3edccb16fa7 \
    import JSONSchemaValidator3Bfe54779Ae1B3Edccb16Fa7 \
    as JSONSchemaValidator3Bfe54779Ae1B3Edccb16Fa7_v3_0_0
from .validators.v3_0_0.jsd_ea10f18c3655db84657ad855bf6972 \
    import JSONSchemaValidatorEa10F18C3655Db84657Ad855Bf6972 \
    as JSONSchemaValidatorEa10F18C3655Db84657Ad855Bf6972_v3_0_0
from .validators.v3_0_0.jsd_b9e8541f25c4ea29944f659f68994 \
    import JSONSchemaValidatorB9E8541F25C4EA29944F659F68994 \
    as JSONSchemaValidatorB9E8541F25C4EA29944F659F68994_v3_0_0
from .validators.v3_0_0.jsd_c8aec23a55399a175acf105dbe1c2 \
    import JSONSchemaValidatorC8Aec23A55399A175Acf105Dbe1C2 \
    as JSONSchemaValidatorC8Aec23A55399A175Acf105Dbe1C2_v3_0_0
from .validators.v3_0_0.jsd_a35a4deda255abb3933e64d74679c1 \
    import JSONSchemaValidatorA35A4DEda255AbB3933E64D74679C1 \
    as JSONSchemaValidatorA35A4DEda255AbB3933E64D74679C1_v3_0_0
from .validators.v3_0_0.jsd_cfcc7615d0492e2dd1b04dd03a9 \
    import JSONSchemaValidatorCfcC7615D0492E2Dd1B04Dd03A9 \
    as JSONSchemaValidatorCfcC7615D0492E2Dd1B04Dd03A9_v3_0_0
from .validators.v3_0_0.jsd_c813c9b5a73b6d00cac1ca5a41f \
    import JSONSchemaValidatorC813C9B5A73B6D00Cac1Ca5A41F \
    as JSONSchemaValidatorC813C9B5A73B6D00Cac1Ca5A41F_v3_0_0
from .validators.v3_0_0.jsd_d26670a205a78800cb50673027a6e \
    import JSONSchemaValidatorD26670A205A78800CB50673027A6E \
    as JSONSchemaValidatorD26670A205A78800CB50673027A6E_v3_0_0
from .validators.v3_0_0.jsd_f5d5ab6568d8bf5f9932f7ed7f4 \
    import JSONSchemaValidatorF5D5Ab6568D8Bf5F9932F7Ed7F4 \
    as JSONSchemaValidatorF5D5Ab6568D8Bf5F9932F7Ed7F4_v3_0_0
from .validators.v3_0_0.jsd_daac88943a5cd2bd745c483448e231 \
    import JSONSchemaValidatorDaac88943A5Cd2Bd745C483448E231 \
    as JSONSchemaValidatorDaac88943A5Cd2Bd745C483448E231_v3_0_0
from .validators.v3_0_0.jsd_e6d1b224e058288a8c4d70be72c9a6 \
    import JSONSchemaValidatorE6D1B224E058288A8C4D70Be72C9A6 \
    as JSONSchemaValidatorE6D1B224E058288A8C4D70Be72C9A6_v3_0_0
from .validators.v3_0_0.jsd_d6d09f7a5084ac7036167214b0e1 \
    import JSONSchemaValidatorD6D09F7A5084Ac7036167214B0E1 \
    as JSONSchemaValidatorD6D09F7A5084Ac7036167214B0E1_v3_0_0
from .validators.v3_0_0.jsd_a11a1ff1ee5387b669bcde99f86fbf \
    import JSONSchemaValidatorA11A1FF1Ee5387B669Bcde99F86Fbf \
    as JSONSchemaValidatorA11A1FF1Ee5387B669Bcde99F86Fbf_v3_0_0
from .validators.v3_0_0.jsd_f1fd8e2bd1581aabf7cd87bff65137 \
    import JSONSchemaValidatorF1Fd8E2Bd1581AAbf7Cd87Bff65137 \
    as JSONSchemaValidatorF1Fd8E2Bd1581AAbf7Cd87Bff65137_v3_0_0
from .validators.v3_0_0.jsd_a5abd33eeaa52e39e926472751ef79e \
    import JSONSchemaValidatorA5Abd33Eeaa52E39E926472751Ef79E \
    as JSONSchemaValidatorA5Abd33Eeaa52E39E926472751Ef79E_v3_0_0
from .validators.v3_0_0.jsd_b62a711ce705542b5d1d92b7d3ca431 \
    import JSONSchemaValidatorB62A711Ce705542B5D1D92B7D3Ca431 \
    as JSONSchemaValidatorB62A711Ce705542B5D1D92B7D3Ca431_v3_0_0
from .validators.v3_0_0.jsd_d79b507bda155c180d42f0a67ef64d5 \
    import JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5 \
    as JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5_v3_0_0
from .validators.v3_0_0.jsd_dbe47028859573988880de76fec0936 \
    import JSONSchemaValidatorDbe47028859573988880De76Fec0936 \
    as JSONSchemaValidatorDbe47028859573988880De76Fec0936_v3_0_0
from .validators.v3_0_0.jsd_f18bdd1938755409bf6db6b29e85d3a \
    import JSONSchemaValidatorF18Bdd1938755409Bf6Db6B29E85D3A \
    as JSONSchemaValidatorF18Bdd1938755409Bf6Db6B29E85D3A_v3_0_0
from .validators.v3_0_0.jsd_c53b22885f5e5d82fb8cadd0332136 \
    import JSONSchemaValidatorC53B22885F5E5D82Fb8Cadd0332136 \
    as JSONSchemaValidatorC53B22885F5E5D82Fb8Cadd0332136_v3_0_0
from .validators.v3_0_0.jsd_e23ac4c658f5b75f19d13d6f7189 \
    import JSONSchemaValidatorE23AC4C658F5B75F19D13D6F7189 \
    as JSONSchemaValidatorE23AC4C658F5B75F19D13D6F7189_v3_0_0
from .validators.v3_0_0.jsd_ce65f2bd375be1ba41a7d6f02ad7b6 \
    import JSONSchemaValidatorCe65F2Bd375Be1Ba41A7D6F02Ad7B6 \
    as JSONSchemaValidatorCe65F2Bd375Be1Ba41A7D6F02Ad7B6_v3_0_0
from .validators.v3_0_0.jsd_cb625d5ad0ad76b93282f5818a \
    import JSONSchemaValidatorCb625D5Ad0Ad76B93282F5818A \
    as JSONSchemaValidatorCb625D5Ad0Ad76B93282F5818A_v3_0_0
from .validators.v3_0_0.jsd_a599ae00f5e47b9ece23cd3183d1c \
    import JSONSchemaValidatorA599AE00F5E47B9EcE23Cd3183D1C \
    as JSONSchemaValidatorA599AE00F5E47B9EcE23Cd3183D1C_v3_0_0
from .validators.v3_0_0.jsd_c288192f954309b4b35aa612ff226 \
    import JSONSchemaValidatorC288192F954309B4B35Aa612Ff226 \
    as JSONSchemaValidatorC288192F954309B4B35Aa612Ff226_v3_0_0
from .validators.v3_0_0.jsd_f64c3c08518e9eef83a92d69cde3 \
    import JSONSchemaValidatorF64C3C08518E9Eef83A92D69Cde3 \
    as JSONSchemaValidatorF64C3C08518E9Eef83A92D69Cde3_v3_0_0
from .validators.v3_0_0.jsd_a60516435c6abd996dd616781c16 \
    import JSONSchemaValidatorA60516435C6ABd996Dd616781C16 \
    as JSONSchemaValidatorA60516435C6ABd996Dd616781C16_v3_0_0
from .validators.v3_0_0.jsd_c3c7d5a3a83d9f7441972d399 \
    import JSONSchemaValidatorC3C7D5A3A83D9F7441972D399 \
    as JSONSchemaValidatorC3C7D5A3A83D9F7441972D399_v3_0_0
from .validators.v3_0_0.jsd_a4d5b5da6a50bfaaecc180543fd952 \
    import JSONSchemaValidatorA4D5B5Da6A50BfAaecC180543Fd952 \
    as JSONSchemaValidatorA4D5B5Da6A50BfAaecC180543Fd952_v3_0_0
from .validators.v3_0_0.jsd_a99695fd5ee0b00efce79a5761ff \
    import JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff \
    as JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff_v3_0_0
from .validators.v3_0_0.jsd_da0a59db7654cfa89df49ca3ac3414 \
    import JSONSchemaValidatorDa0A59Db7654CfA89DF49Ca3Ac3414 \
    as JSONSchemaValidatorDa0A59Db7654CfA89DF49Ca3Ac3414_v3_0_0
from .validators.v3_0_0.jsd_f59cbefb9504fb36b3e50c355f1c0 \
    import JSONSchemaValidatorF59CbEfb9504FB36B3E50C355F1C0 \
    as JSONSchemaValidatorF59CbEfb9504FB36B3E50C355F1C0_v3_0_0
from .validators.v3_0_0.jsd_a1af553d663556ca429a10ed82effda \
    import JSONSchemaValidatorA1Af553D663556CA429A10Ed82Effda \
    as JSONSchemaValidatorA1Af553D663556CA429A10Ed82Effda_v3_0_0
from .validators.v3_0_0.jsd_a40f9e169a95d6dbf3ebbb020291007 \
    import JSONSchemaValidatorA40F9E169A95D6DBf3EBbb020291007 \
    as JSONSchemaValidatorA40F9E169A95D6DBf3EBbb020291007_v3_0_0
from .validators.v3_0_0.jsd_a72ae8af1075d0c94912b008003b13e \
    import JSONSchemaValidatorA72Ae8AF1075D0C94912B008003B13E \
    as JSONSchemaValidatorA72Ae8AF1075D0C94912B008003B13E_v3_0_0
from .validators.v3_0_0.jsd_ab96d3d76de5d05bbac1f27feacb7b0 \
    import JSONSchemaValidatorAb96D3D76De5D05Bbac1F27Feacb7B0 \
    as JSONSchemaValidatorAb96D3D76De5D05Bbac1F27Feacb7B0_v3_0_0
from .validators.v3_0_0.jsd_b94d7d3f0ed5d0b938151ae2cae9fa4 \
    import JSONSchemaValidatorB94D7D3F0Ed5D0B938151Ae2Cae9Fa4 \
    as JSONSchemaValidatorB94D7D3F0Ed5D0B938151Ae2Cae9Fa4_v3_0_0
from .validators.v3_0_0.jsd_b994e6c8b8d53f29230686824c9fafa \
    import JSONSchemaValidatorB994E6C8B8D53F29230686824C9Fafa \
    as JSONSchemaValidatorB994E6C8B8D53F29230686824C9Fafa_v3_0_0
from .validators.v3_0_0.jsd_c5c37c343c050e0af67b2223e64faf3 \
    import JSONSchemaValidatorC5C37C343C050E0Af67B2223E64Faf3 \
    as JSONSchemaValidatorC5C37C343C050E0Af67B2223E64Faf3_v3_0_0
from .validators.v3_0_0.jsd_caefe2cb042513ab4a4a76f227330cb \
    import JSONSchemaValidatorCaefe2CB042513AB4A4A76F227330Cb \
    as JSONSchemaValidatorCaefe2CB042513AB4A4A76F227330Cb_v3_0_0
from .validators.v3_0_0.jsd_e232c5666ab5ed783588f413c3bc644 \
    import JSONSchemaValidatorE232C5666Ab5Ed783588F413C3Bc644 \
    as JSONSchemaValidatorE232C5666Ab5Ed783588F413C3Bc644_v3_0_0
from .validators.v3_0_0.jsd_eeef18d70b159f788b717e301dd3643 \
    import JSONSchemaValidatorEeef18D70B159F788B717E301Dd3643 \
    as JSONSchemaValidatorEeef18D70B159F788B717E301Dd3643_v3_0_0
from .validators.v3_0_0.jsd_f8ba0e97135ca6bacff94d5a76df97 \
    import JSONSchemaValidatorF8Ba0E97135Ca6BacfF94D5A76Df97 \
    as JSONSchemaValidatorF8Ba0E97135Ca6BacfF94D5A76Df97_v3_0_0
from .validators.v3_0_0.jsd_dc2eec65ad680a3c5de47cd87c8 \
    import JSONSchemaValidatorDc2Eec65Ad680A3C5De47Cd87C8 \
    as JSONSchemaValidatorDc2Eec65Ad680A3C5De47Cd87C8_v3_0_0
from .validators.v3_0_0.jsd_b8696d875b12b0a3ab735b397d7a \
    import JSONSchemaValidatorB8696D875B12B0A3Ab735B397D7A \
    as JSONSchemaValidatorB8696D875B12B0A3Ab735B397D7A_v3_0_0
from .validators.v3_0_0.jsd_e5355db6a478daa29f318303 \
    import JSONSchemaValidatorE5355Db6A478Daa29F318303 \
    as JSONSchemaValidatorE5355Db6A478Daa29F318303_v3_0_0
from .validators.v3_0_0.jsd_b9e7d29b0356b2b1d5fdb2e1069265 \
    import JSONSchemaValidatorB9E7D29B0356B2B1D5Fdb2E1069265 \
    as JSONSchemaValidatorB9E7D29B0356B2B1D5Fdb2E1069265_v3_0_0
from .validators.v3_0_0.jsd_c5c9b7ab72b5442ae7026a5dcc0fec3 \
    import JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3 \
    as JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3_v3_0_0
from .validators.v3_0_0.jsd_ccba98a61555ae495f6a05284e3b5ae \
    import JSONSchemaValidatorCcba98A61555Ae495F6A05284E3B5Ae \
    as JSONSchemaValidatorCcba98A61555Ae495F6A05284E3B5Ae_v3_0_0
from .validators.v3_0_0.jsd_d14f56096ec518086b3e5d386bd3139 \
    import JSONSchemaValidatorD14F56096Ec518086B3E5D386Bd3139 \
    as JSONSchemaValidatorD14F56096Ec518086B3E5D386Bd3139_v3_0_0
from .validators.v3_0_0.jsd_e155669bc74586e9ef2580ec5752902 \
    import JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902 \
    as JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902_v3_0_0
from .validators.v3_0_0.jsd_f36e90115b05416a71506061fed7e5c \
    import JSONSchemaValidatorF36E90115B05416A71506061Fed7E5C \
    as JSONSchemaValidatorF36E90115B05416A71506061Fed7E5C_v3_0_0
from .validators.v3_0_0.jsd_c4fada6c558d9aba09cc373d5b266 \
    import JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266 \
    as JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0
from .validators.v3_0_0.jsd_b11e2f1af656bcb5880a7b33720ec5 \
    import JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5 \
    as JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0
from .validators.v3_0_0.jsd_c9722c56108cac8ca50bf8f01c \
    import JSONSchemaValidatorC9722C56108Cac8Ca50Bf8F01C \
    as JSONSchemaValidatorC9722C56108Cac8Ca50Bf8F01C_v3_0_0
from .validators.v3_0_0.jsd_cb9345e58f5433ae80f5d8f855978b \
    import JSONSchemaValidatorCb9345E58F5433Ae80F5D8F855978B \
    as JSONSchemaValidatorCb9345E58F5433Ae80F5D8F855978B_v3_0_0
from .validators.v3_0_0.jsd_b986fa0f0d54ef98eb135eeb88808a \
    import JSONSchemaValidatorB986Fa0F0D54Ef98Eb135Eeb88808A \
    as JSONSchemaValidatorB986Fa0F0D54Ef98Eb135Eeb88808A_v3_0_0
from .validators.v3_0_0.jsd_c47e28f13659658b3e6af9409a1177 \
    import JSONSchemaValidatorC47E28F13659658B3E6Af9409A1177 \
    as JSONSchemaValidatorC47E28F13659658B3E6Af9409A1177_v3_0_0
from .validators.v3_0_0.jsd_fb9c22ad9a5eddb590c85abdab460b \
    import JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B \
    as JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B_v3_0_0
from .validators.v3_0_0.jsd_fd729f50e65695966359b589a1606b \
    import JSONSchemaValidatorFd729F50E65695966359B589A1606B \
    as JSONSchemaValidatorFd729F50E65695966359B589A1606B_v3_0_0
from .validators.v3_0_0.jsd_b03900a2e5027b615d9f1bdcf9f63 \
    import JSONSchemaValidatorB03900A2E5027B615D9F1Bdcf9F63 \
    as JSONSchemaValidatorB03900A2E5027B615D9F1Bdcf9F63_v3_0_0
from .validators.v3_0_0.jsd_acb5a41fe395b158a3fe1cda996b0cf \
    import JSONSchemaValidatorAcb5A41Fe395B158A3FE1Cda996B0Cf \
    as JSONSchemaValidatorAcb5A41Fe395B158A3FE1Cda996B0Cf_v3_0_0
from .validators.v3_0_0.jsd_cb8a98ab3d456f387ad6ef911a7293f \
    import JSONSchemaValidatorCb8A98AB3D456F387Ad6Ef911A7293F \
    as JSONSchemaValidatorCb8A98AB3D456F387Ad6Ef911A7293F_v3_0_0
from .validators.v3_0_0.jsd_e6c7251a8508597f1b7ae61cbf953 \
    import JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953 \
    as JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953_v3_0_0
from .validators.v3_0_0.jsd_e4c74e9b4e559e95c73e81183a6c7a \
    import JSONSchemaValidatorE4C74E9B4E559E95C73E81183A6C7A \
    as JSONSchemaValidatorE4C74E9B4E559E95C73E81183A6C7A_v3_0_0
from .validators.v3_0_0.jsd_a03a30be865ca599e77c63a332978b \
    import JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B \
    as JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B_v3_0_0
from .validators.v3_0_0.jsd_c189f2f5f6b8bab3931c206c949 \
    import JSONSchemaValidatorC189F2F5F6B8Bab3931C206C949 \
    as JSONSchemaValidatorC189F2F5F6B8Bab3931C206C949_v3_0_0
from .validators.v3_0_0.jsd_d8610d4a355b63aaaa364447d5fa00 \
    import JSONSchemaValidatorD8610D4A355B63Aaaa364447D5Fa00 \
    as JSONSchemaValidatorD8610D4A355B63Aaaa364447D5Fa00_v3_0_0
from .validators.v3_0_0.jsd_dee8ff57265324a99fa2011bb4dc5f \
    import JSONSchemaValidatorDee8Ff57265324A99FA2011Bb4Dc5F \
    as JSONSchemaValidatorDee8Ff57265324A99FA2011Bb4Dc5F_v3_0_0
from .validators.v3_0_0.jsd_feb825519f98bd1541ef3c367d \
    import JSONSchemaValidatorFeB825519F98Bd1541Ef3C367D \
    as JSONSchemaValidatorFeB825519F98Bd1541Ef3C367D_v3_0_0
from .validators.v3_0_0.jsd_d1132a216d54d091022aec0ad018f8 \
    import JSONSchemaValidatorD1132A216D54D091022Aec0Ad018F8 \
    as JSONSchemaValidatorD1132A216D54D091022Aec0Ad018F8_v3_0_0
from .validators.v3_0_0.jsd_ad69fa1d850f4993bbfc888749fa0 \
    import JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0 \
    as JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0
from .validators.v3_0_0.jsd_f723c1a3e533893ec03335e072cfe \
    import JSONSchemaValidatorF723C1A3E533893Ec03335E072Cfe \
    as JSONSchemaValidatorF723C1A3E533893Ec03335E072Cfe_v3_0_0
from .validators.v3_0_0.jsd_f564c3eda5c20bb807b8c062c8e7b \
    import JSONSchemaValidatorF564C3Eda5C20Bb807B8C062C8E7B \
    as JSONSchemaValidatorF564C3Eda5C20Bb807B8C062C8E7B_v3_0_0
from .validators.v3_0_0.jsd_abc25887a5daab1216195e08cbd49 \
    import JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49 \
    as JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49_v3_0_0
from .validators.v3_0_0.jsd_ad233598ed75e0c97ddd3c3f1af50e4 \
    import JSONSchemaValidatorAd233598Ed75E0C97DdD3C3F1Af50E4 \
    as JSONSchemaValidatorAd233598Ed75E0C97DdD3C3F1Af50E4_v3_0_0
from .validators.v3_0_0.jsd_c475afd2a5e57e4bd0952f2c5349c6c \
    import JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C \
    as JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C_v3_0_0
from .validators.v3_0_0.jsd_ce70db7732c596aa82bd7d1725ac02d \
    import JSONSchemaValidatorCe70Db7732C596AA82BD7D1725Ac02D \
    as JSONSchemaValidatorCe70Db7732C596AA82BD7D1725Ac02D_v3_0_0
from .validators.v3_0_0.jsd_d6be8d877485969954d2574f0448247 \
    import JSONSchemaValidatorD6Be8D877485969954D2574F0448247 \
    as JSONSchemaValidatorD6Be8D877485969954D2574F0448247_v3_0_0
from .validators.v3_0_0.jsd_e4bfa620f76545d9887045cd24d99a2 \
    import JSONSchemaValidatorE4Bfa620F76545D9887045Cd24D99A2 \
    as JSONSchemaValidatorE4Bfa620F76545D9887045Cd24D99A2_v3_0_0
from .validators.v3_0_0.jsd_a0aadd33595645bf671efc4912f89a \
    import JSONSchemaValidatorA0Aadd33595645Bf671Efc4912F89A \
    as JSONSchemaValidatorA0Aadd33595645Bf671Efc4912F89A_v3_0_0
from .validators.v3_0_0.jsd_a56f5c5f739a83e8806da16be5 \
    import JSONSchemaValidatorA56F5C5F739A83E8806Da16Be5 \
    as JSONSchemaValidatorA56F5C5F739A83E8806Da16Be5_v3_0_0
from .validators.v3_0_0.jsd_f9ada2e275fa2934fdb4825266a2c \
    import JSONSchemaValidatorF9Ada2E275Fa2934FDb4825266A2C \
    as JSONSchemaValidatorF9Ada2E275Fa2934FDb4825266A2C_v3_0_0
from .validators.v3_0_0.jsd_c1fa3bf115c77be99b602aca1493b \
    import JSONSchemaValidatorC1Fa3Bf115C77Be99B602Aca1493B \
    as JSONSchemaValidatorC1Fa3Bf115C77Be99B602Aca1493B_v3_0_0
from .validators.v3_0_0.jsd_e3ddfddd45e299f14ed194926f8de \
    import JSONSchemaValidatorE3DdfDdd45E299F14Ed194926F8De \
    as JSONSchemaValidatorE3DdfDdd45E299F14Ed194926F8De_v3_0_0
from .validators.v3_0_0.jsd_aa24c1260a568b93c283ecd2c3510e \
    import JSONSchemaValidatorAa24C1260A568B93C283Ecd2C3510E \
    as JSONSchemaValidatorAa24C1260A568B93C283Ecd2C3510E_v3_0_0
from .validators.v3_0_0.jsd_a62af279ca25af0a1837f2cbf10a04d \
    import JSONSchemaValidatorA62Af279Ca25Af0A1837F2Cbf10A04D \
    as JSONSchemaValidatorA62Af279Ca25Af0A1837F2Cbf10A04D_v3_0_0
from .validators.v3_0_0.jsd_af2cc85852f52b0aad5a067b2c69286 \
    import JSONSchemaValidatorAf2Cc85852F52B0Aad5A067B2C69286 \
    as JSONSchemaValidatorAf2Cc85852F52B0Aad5A067B2C69286_v3_0_0
from .validators.v3_0_0.jsd_cbcecf65a0155fcad602d3ac16531a7 \
    import JSONSchemaValidatorCbcecf65A0155FcAd602D3Ac16531A7 \
    as JSONSchemaValidatorCbcecf65A0155FcAd602D3Ac16531A7_v3_0_0
from .validators.v3_0_0.jsd_da7b2773c485400980369a543ddbabf \
    import JSONSchemaValidatorDa7B2773C485400980369A543Ddbabf \
    as JSONSchemaValidatorDa7B2773C485400980369A543Ddbabf_v3_0_0
from .validators.v3_0_0.jsd_df4fb303a3e5661ba12058f18b225af \
    import JSONSchemaValidatorDf4Fb303A3E5661Ba12058F18B225Af \
    as JSONSchemaValidatorDf4Fb303A3E5661Ba12058F18B225Af_v3_0_0
from .validators.v3_0_0.jsd_e43a67028515bf193c102cd077ea764 \
    import JSONSchemaValidatorE43A67028515Bf193C102Cd077Ea764 \
    as JSONSchemaValidatorE43A67028515Bf193C102Cd077Ea764_v3_0_0
from .validators.v3_0_0.jsd_e58eabefef15feb880ecfe2906d805f \
    import JSONSchemaValidatorE58EabeFef15Feb880ECfe2906D805F \
    as JSONSchemaValidatorE58EabeFef15Feb880ECfe2906D805F_v3_0_0
from .validators.v3_0_0.jsd_faa7211d68e5b329034e17c82b78694 \
    import JSONSchemaValidatorFaa7211D68E5B329034E17C82B78694 \
    as JSONSchemaValidatorFaa7211D68E5B329034E17C82B78694_v3_0_0
from .validators.v3_0_0.jsd_feb530ce19c5bcf96d57f49cd84bc1f \
    import JSONSchemaValidatorFeb530CE19C5Bcf96D57F49Cd84Bc1F \
    as JSONSchemaValidatorFeb530CE19C5Bcf96D57F49Cd84Bc1F_v3_0_0
from .validators.v3_0_0.jsd_f4508bb3352ff920dbdc229e0fc50 \
    import JSONSchemaValidatorF4508Bb3352Ff920DBdc229E0Fc50 \
    as JSONSchemaValidatorF4508Bb3352Ff920DBdc229E0Fc50_v3_0_0
from .validators.v3_0_0.jsd_e68f07767522ba1e49dc474e936d2 \
    import JSONSchemaValidatorE68F07767522BA1E49Dc474E936D2 \
    as JSONSchemaValidatorE68F07767522BA1E49Dc474E936D2_v3_0_0
from .validators.v3_0_0.jsd_b7f7285d71be4645db91b0fc74 \
    import JSONSchemaValidatorB7F7285D71Be4645Db91B0Fc74 \
    as JSONSchemaValidatorB7F7285D71Be4645Db91B0Fc74_v3_0_0
from .validators.v3_0_0.jsd_eca5db5147b1e3b35a032ced4b \
    import JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B \
    as JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B_v3_0_0
from .validators.v3_0_0.jsd_eddb567508080061e51d5f40c4c \
    import JSONSchemaValidatorEddB567508080061E51D5F40C4C \
    as JSONSchemaValidatorEddB567508080061E51D5F40C4C_v3_0_0
from .validators.v3_0_0.jsd_b314d32b258a1b53c5c84cf84d396 \
    import JSONSchemaValidatorB314D32B258A1B53C5C84Cf84D396 \
    as JSONSchemaValidatorB314D32B258A1B53C5C84Cf84D396_v3_0_0
from .validators.v3_0_0.jsd_cba3f7ace597da668acfbe00364be \
    import JSONSchemaValidatorCba3F7Ace597DA668Acfbe00364Be \
    as JSONSchemaValidatorCba3F7Ace597DA668Acfbe00364Be_v3_0_0
from .validators.v3_0_0.jsd_bee301e7f5ccfa2e788dcafbf92cc \
    import JSONSchemaValidatorBee301E7F5CcfA2E788Dcafbf92Cc \
    as JSONSchemaValidatorBee301E7F5CcfA2E788Dcafbf92Cc_v3_0_0
from .validators.v3_0_0.jsd_ae615b5e28c54639f44bd10e5b36601 \
    import JSONSchemaValidatorAe615B5E28C54639F44Bd10E5B36601 \
    as JSONSchemaValidatorAe615B5E28C54639F44Bd10E5B36601_v3_0_0
from .validators.v3_0_0.jsd_c6be021c4ca59e48c97afe218219bb1 \
    import JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1 \
    as JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1_v3_0_0
from .validators.v3_0_0.jsd_cc29554d7925fb1abbfb633e9b00f04 \
    import JSONSchemaValidatorCc29554D7925Fb1AbbfB633E9B00F04 \
    as JSONSchemaValidatorCc29554D7925Fb1AbbfB633E9B00F04_v3_0_0
from .validators.v3_0_0.jsd_d0ed84901325292ad4e2a91a174f6b2 \
    import JSONSchemaValidatorD0Ed84901325292Ad4E2A91A174F6B2 \
    as JSONSchemaValidatorD0Ed84901325292Ad4E2A91A174F6B2_v3_0_0
from .validators.v3_0_0.jsd_d53842e83f0538cab91e097aa6800ce \
    import JSONSchemaValidatorD53842E83F0538CAb91E097Aa6800Ce \
    as JSONSchemaValidatorD53842E83F0538CAb91E097Aa6800Ce_v3_0_0
from .validators.v3_0_0.jsd_dae42fe107a5d4fa53289574a0baa84 \
    import JSONSchemaValidatorDae42Fe107A5D4FA53289574A0Baa84 \
    as JSONSchemaValidatorDae42Fe107A5D4FA53289574A0Baa84_v3_0_0
from .validators.v3_0_0.jsd_f403dda9440503191536993f569cc6f \
    import JSONSchemaValidatorF403Dda9440503191536993F569Cc6F \
    as JSONSchemaValidatorF403Dda9440503191536993F569Cc6F_v3_0_0
from .validators.v3_0_0.jsd_e6734850fabb2097fa969948cb \
    import JSONSchemaValidatorE6734850FaBb2097Fa969948Cb \
    as JSONSchemaValidatorE6734850FaBb2097Fa969948Cb_v3_0_0
from .validators.v3_0_0.jsd_e84541805d1da1fa3d4d581102a9 \
    import JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9 \
    as JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9_v3_0_0
from .validators.v3_0_0.jsd_c137cad852579f4b810ff8adf661 \
    import JSONSchemaValidatorC137Cad852579F4B810Ff8Adf661 \
    as JSONSchemaValidatorC137Cad852579F4B810Ff8Adf661_v3_0_0
from .validators.v3_0_0.jsd_fff985b5159a0aa52bfe9e62ba7 \
    import JSONSchemaValidatorFff985B5159A0Aa52Bfe9E62Ba7 \
    as JSONSchemaValidatorFff985B5159A0Aa52Bfe9E62Ba7_v3_0_0
from .validators.v3_0_0.jsd_a57687cef65891a6f48dd17f456c4e \
    import JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E \
    as JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E_v3_0_0
from .validators.v3_0_0.jsd_b9eb9547216547cab8b9e686eee674b \
    import JSONSchemaValidatorB9Eb9547216547CAb8B9E686Eee674B \
    as JSONSchemaValidatorB9Eb9547216547CAb8B9E686Eee674B_v3_0_0
from .validators.v3_0_0.jsd_c6c2a4908ee5f48b7e9cae7572f6a94 \
    import JSONSchemaValidatorC6C2A4908Ee5F48B7E9Cae7572F6A94 \
    as JSONSchemaValidatorC6C2A4908Ee5F48B7E9Cae7572F6A94_v3_0_0
from .validators.v3_0_0.jsd_ea7e01261355dcfae6412e0615ba1f5 \
    import JSONSchemaValidatorEa7E01261355DcfAe6412E0615Ba1F5 \
    as JSONSchemaValidatorEa7E01261355DcfAe6412E0615Ba1F5_v3_0_0
from .validators.v3_0_0.jsd_b305804a95e2fb51ab50c039e6c66 \
    import JSONSchemaValidatorB305804A95E2FB51AB50C039E6C66 \
    as JSONSchemaValidatorB305804A95E2FB51AB50C039E6C66_v3_0_0
from .validators.v3_0_0.jsd_bc200af85d598885a990ff9bcbf8 \
    import JSONSchemaValidatorBc200Af85D598885A990Ff9Bcbf8 \
    as JSONSchemaValidatorBc200Af85D598885A990Ff9Bcbf8_v3_0_0
from .validators.v3_0_0.jsd_b58a72c9ff567896a15555ecc9564f \
    import JSONSchemaValidatorB58A72C9Ff567896A15555Ecc9564F \
    as JSONSchemaValidatorB58A72C9Ff567896A15555Ecc9564F_v3_0_0
from .validators.v3_0_0.jsd_a70be83785373b264d21e84fbfa7d \
    import JSONSchemaValidatorA70Be83785373B264D21E84Fbfa7D \
    as JSONSchemaValidatorA70Be83785373B264D21E84Fbfa7D_v3_0_0
from .validators.v3_0_0.jsd_e4ce332e5cdc97399fe9f01b163e \
    import JSONSchemaValidatorE4Ce332E5Cdc97399Fe9F01B163E \
    as JSONSchemaValidatorE4Ce332E5Cdc97399Fe9F01B163E_v3_0_0
from .validators.v3_0_0.jsd_f4bceb4d5500fa2bab08326fd66cb \
    import JSONSchemaValidatorF4BceB4D5500FA2BaB08326Fd66Cb \
    as JSONSchemaValidatorF4BceB4D5500FA2BaB08326Fd66Cb_v3_0_0
from .validators.v3_0_0.jsd_bdae59219027b4d40b94fa3d \
    import JSONSchemaValidatorBdae59219027B4D40B94Fa3D \
    as JSONSchemaValidatorBdae59219027B4D40B94Fa3D_v3_0_0
from .validators.v3_0_0.jsd_a095b061f564ebba331f66505b0e3 \
    import JSONSchemaValidatorA095B061F564EBba331F66505B0E3 \
    as JSONSchemaValidatorA095B061F564EBba331F66505B0E3_v3_0_0
from .validators.v3_0_0.jsd_b22d6ad9f595ab7e3eee5cf44de8a \
    import JSONSchemaValidatorB22D6Ad9F595AB7E3Eee5Cf44De8A \
    as JSONSchemaValidatorB22D6Ad9F595AB7E3Eee5Cf44De8A_v3_0_0
from .validators.v3_0_0.jsd_a4cccea3c9567498f6f688e0cf86e7 \
    import JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7 \
    as JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7_v3_0_0
from .validators.v3_0_0.jsd_afa6d7527045ebc928ee7e30ad3092a \
    import JSONSchemaValidatorAfa6D7527045Ebc928EE7E30Ad3092A \
    as JSONSchemaValidatorAfa6D7527045Ebc928EE7E30Ad3092A_v3_0_0
from .validators.v3_0_0.jsd_b641825a9555ecba105cabbdf50fc78 \
    import JSONSchemaValidatorB641825A9555EcbA105Cabbdf50Fc78 \
    as JSONSchemaValidatorB641825A9555EcbA105Cabbdf50Fc78_v3_0_0
from .validators.v3_0_0.jsd_c052306febd5865ada5df348e18a889 \
    import JSONSchemaValidatorC052306Febd5865Ada5Df348E18A889 \
    as JSONSchemaValidatorC052306Febd5865Ada5Df348E18A889_v3_0_0
from .validators.v3_0_0.jsd_d904c521059563490c4a93871b33d51 \
    import JSONSchemaValidatorD904C521059563490C4A93871B33D51 \
    as JSONSchemaValidatorD904C521059563490C4A93871B33D51_v3_0_0
from .validators.v3_0_0.jsd_dfe1db8729d541fb3a17d31d47d1881 \
    import JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881 \
    as JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881_v3_0_0
from .validators.v3_0_0.jsd_a0824f9a589c58cd8df522524cb550ad \
    import JSONSchemaValidatorA0824F9A589C58Cd8Df522524Cb550Ad \
    as JSONSchemaValidatorA0824F9A589C58Cd8Df522524Cb550Ad_v3_0_0
from .validators.v3_0_0.jsd_a0fdb67d95475cd39382171dec96d6c1 \
    import JSONSchemaValidatorA0Fdb67D95475Cd39382171Dec96D6C1 \
    as JSONSchemaValidatorA0Fdb67D95475Cd39382171Dec96D6C1_v3_0_0
from .validators.v3_0_0.jsd_a1e3cde0c3f254b39caaaf7c907ae67e \
    import JSONSchemaValidatorA1E3Cde0C3F254B39CaaAf7C907Ae67E \
    as JSONSchemaValidatorA1E3Cde0C3F254B39CaaAf7C907Ae67E_v3_0_0
from .validators.v3_0_0.jsd_a4ab683ce53052e089626a096abaf451 \
    import JSONSchemaValidatorA4Ab683CE53052E089626A096Abaf451 \
    as JSONSchemaValidatorA4Ab683CE53052E089626A096Abaf451_v3_0_0
from .validators.v3_0_0.jsd_a4af71bd9e705f1bb1d236b3c16e5f51 \
    import JSONSchemaValidatorA4Af71Bd9E705F1BB1D236B3C16E5F51 \
    as JSONSchemaValidatorA4Af71Bd9E705F1BB1D236B3C16E5F51_v3_0_0
from .validators.v3_0_0.jsd_a50d1bd34d5f593aadf8eb02083c67b0 \
    import JSONSchemaValidatorA50D1Bd34D5F593AAdf8Eb02083C67B0 \
    as JSONSchemaValidatorA50D1Bd34D5F593AAdf8Eb02083C67B0_v3_0_0
from .validators.v3_0_0.jsd_a69c7f1ad54e5e9cae1f871e19eed61b \
    import JSONSchemaValidatorA69C7F1AD54E5E9CAe1F871E19Eed61B \
    as JSONSchemaValidatorA69C7F1AD54E5E9CAe1F871E19Eed61B_v3_0_0
from .validators.v3_0_0.jsd_a78585b436685873813e3804cdec7d2b \
    import JSONSchemaValidatorA78585B436685873813E3804Cdec7D2B \
    as JSONSchemaValidatorA78585B436685873813E3804Cdec7D2B_v3_0_0
from .validators.v3_0_0.jsd_ab916b19789c59b79dddbc2d0a3c57fc \
    import JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc \
    as JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc_v3_0_0
from .validators.v3_0_0.jsd_ac3aa12d3b5551638c3867aa9584f87b \
    import JSONSchemaValidatorAc3Aa12D3B5551638C3867Aa9584F87B \
    as JSONSchemaValidatorAc3Aa12D3B5551638C3867Aa9584F87B_v3_0_0
from .validators.v3_0_0.jsd_acf0372068885036baee3c4524638f31 \
    import JSONSchemaValidatorAcf0372068885036Baee3C4524638F31 \
    as JSONSchemaValidatorAcf0372068885036Baee3C4524638F31_v3_0_0
from .validators.v3_0_0.jsd_ae8d7c8f33bb52ceb04880845f2f45ba \
    import JSONSchemaValidatorAe8D7C8F33Bb52CeB04880845F2F45Ba \
    as JSONSchemaValidatorAe8D7C8F33Bb52CeB04880845F2F45Ba_v3_0_0
from .validators.v3_0_0.jsd_af14464cc6a05f6f87bbe7c174b6d5f6 \
    import JSONSchemaValidatorAf14464CC6A05F6F87BbE7C174B6D5F6 \
    as JSONSchemaValidatorAf14464CC6A05F6F87BbE7C174B6D5F6_v3_0_0
from .validators.v3_0_0.jsd_afe1108b1a59539ebe3de3e5652c9653 \
    import JSONSchemaValidatorAfe1108B1A59539EBe3DE3E5652C9653 \
    as JSONSchemaValidatorAfe1108B1A59539EBe3DE3E5652C9653_v3_0_0
from .validators.v3_0_0.jsd_b06719c4a49753408438f661dd2f6f7e \
    import JSONSchemaValidatorB06719C4A49753408438F661Dd2F6F7E \
    as JSONSchemaValidatorB06719C4A49753408438F661Dd2F6F7E_v3_0_0
from .validators.v3_0_0.jsd_b09ea91f72885e05b6aa73e89546f969 \
    import JSONSchemaValidatorB09Ea91F72885E05B6Aa73E89546F969 \
    as JSONSchemaValidatorB09Ea91F72885E05B6Aa73E89546F969_v3_0_0
from .validators.v3_0_0.jsd_b227e1b5bbac556a9f577d3a3ea407af \
    import JSONSchemaValidatorB227E1B5Bbac556A9F577D3A3Ea407Af \
    as JSONSchemaValidatorB227E1B5Bbac556A9F577D3A3Ea407Af_v3_0_0
from .validators.v3_0_0.jsd_b3284240745e5b929c51495fe80bc1c4 \
    import JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4 \
    as JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4_v3_0_0
from .validators.v3_0_0.jsd_b3c356cfc48a5da4b13b8ecbae5748b7 \
    import JSONSchemaValidatorB3C356CfC48A5Da4B13B8Ecbae5748B7 \
    as JSONSchemaValidatorB3C356CfC48A5Da4B13B8Ecbae5748B7_v3_0_0
from .validators.v3_0_0.jsd_b4ceac9ee830523ca5ddbfdf3e1b44be \
    import JSONSchemaValidatorB4Ceac9EE830523CA5DdBfdf3E1B44Be \
    as JSONSchemaValidatorB4Ceac9EE830523CA5DdBfdf3E1B44Be_v3_0_0
from .validators.v3_0_0.jsd_b8104a50fc565ae9a756d6d0152e0e5b \
    import JSONSchemaValidatorB8104A50Fc565Ae9A756D6D0152E0E5B \
    as JSONSchemaValidatorB8104A50Fc565Ae9A756D6D0152E0E5B_v3_0_0
from .validators.v3_0_0.jsd_b8319a8b5d195348a8763acd95ca2967 \
    import JSONSchemaValidatorB8319A8B5D195348A8763Acd95Ca2967 \
    as JSONSchemaValidatorB8319A8B5D195348A8763Acd95Ca2967_v3_0_0
from .validators.v3_0_0.jsd_b839d4dee9b958e48ccef056603e253f \
    import JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F \
    as JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F_v3_0_0
from .validators.v3_0_0.jsd_b95cf8c9aed95518b38be1fa4b514b67 \
    import JSONSchemaValidatorB95Cf8C9Aed95518B38BE1Fa4B514B67 \
    as JSONSchemaValidatorB95Cf8C9Aed95518B38BE1Fa4B514B67_v3_0_0
from .validators.v3_0_0.jsd_bacf1abfc35e509183c9a7f055cbbfec \
    import JSONSchemaValidatorBacf1AbfC35E509183C9A7F055Cbbfec \
    as JSONSchemaValidatorBacf1AbfC35E509183C9A7F055Cbbfec_v3_0_0
from .validators.v3_0_0.jsd_bb165bd00a6653ac9da440f23ee62ecc \
    import JSONSchemaValidatorBb165Bd00A6653Ac9Da440F23Ee62Ecc \
    as JSONSchemaValidatorBb165Bd00A6653Ac9Da440F23Ee62Ecc_v3_0_0
from .validators.v3_0_0.jsd_bba3187f0be4563aa8b6ff5931a123e7 \
    import JSONSchemaValidatorBba3187F0Be4563AA8B6Ff5931A123E7 \
    as JSONSchemaValidatorBba3187F0Be4563AA8B6Ff5931A123E7_v3_0_0
from .validators.v3_0_0.jsd_bcb7ec29968e5d5899df4a90d94ed659 \
    import JSONSchemaValidatorBcb7Ec29968E5D5899Df4A90D94Ed659 \
    as JSONSchemaValidatorBcb7Ec29968E5D5899Df4A90D94Ed659_v3_0_0
from .validators.v3_0_0.jsd_bcdb4d3a659653e498da5ab77440c070 \
    import JSONSchemaValidatorBcdb4D3A659653E498Da5Ab77440C070 \
    as JSONSchemaValidatorBcdb4D3A659653E498Da5Ab77440C070_v3_0_0
from .validators.v3_0_0.jsd_bdea52558473565c9963ec14c65727b8 \
    import JSONSchemaValidatorBdea52558473565C9963Ec14C65727B8 \
    as JSONSchemaValidatorBdea52558473565C9963Ec14C65727B8_v3_0_0
from .validators.v3_0_0.jsd_bf792ec664fa5202beb776556908b0c1 \
    import JSONSchemaValidatorBf792Ec664Fa5202Beb776556908B0C1 \
    as JSONSchemaValidatorBf792Ec664Fa5202Beb776556908B0C1_v3_0_0
from .validators.v3_0_0.jsd_bf95f099207a5b6599e04c47c22789c0 \
    import JSONSchemaValidatorBf95F099207A5B6599E04C47C22789C0 \
    as JSONSchemaValidatorBf95F099207A5B6599E04C47C22789C0_v3_0_0
from .validators.v3_0_0.jsd_c0984cde5e925c209ab87472ab905476 \
    import JSONSchemaValidatorC0984Cde5E925C209Ab87472Ab905476 \
    as JSONSchemaValidatorC0984Cde5E925C209Ab87472Ab905476_v3_0_0
from .validators.v3_0_0.jsd_c37778a2faa5552894cc60cec13c56c7 \
    import JSONSchemaValidatorC37778A2Faa5552894Cc60Cec13C56C7 \
    as JSONSchemaValidatorC37778A2Faa5552894Cc60Cec13C56C7_v3_0_0
from .validators.v3_0_0.jsd_c37d788b1f9251ddb1742ed73f42abc3 \
    import JSONSchemaValidatorC37D788B1F9251DdB1742Ed73F42Abc3 \
    as JSONSchemaValidatorC37D788B1F9251DdB1742Ed73F42Abc3_v3_0_0
from .validators.v3_0_0.jsd_c578ef80918b5d038024d126cd6e3b8d \
    import JSONSchemaValidatorC578Ef80918B5D038024D126Cd6E3B8D \
    as JSONSchemaValidatorC578Ef80918B5D038024D126Cd6E3B8D_v3_0_0
from .validators.v3_0_0.jsd_c5e52706e7095a81b8d32f3024e01cf6 \
    import JSONSchemaValidatorC5E52706E7095A81B8D32F3024E01Cf6 \
    as JSONSchemaValidatorC5E52706E7095A81B8D32F3024E01Cf6_v3_0_0
from .validators.v3_0_0.jsd_c638f98ea11b5c3882966cb0d1758a64 \
    import JSONSchemaValidatorC638F98EA11B5C3882966Cb0D1758A64 \
    as JSONSchemaValidatorC638F98EA11B5C3882966Cb0D1758A64_v3_0_0
from .validators.v3_0_0.jsd_c654a18faf1b5571ac5ba61145d298c4 \
    import JSONSchemaValidatorC654A18FAf1B5571Ac5BA61145D298C4 \
    as JSONSchemaValidatorC654A18FAf1B5571Ac5BA61145D298C4_v3_0_0
from .validators.v3_0_0.jsd_c67c56a249ce5721863328be9da81573 \
    import JSONSchemaValidatorC67C56A249Ce5721863328Be9Da81573 \
    as JSONSchemaValidatorC67C56A249Ce5721863328Be9Da81573_v3_0_0
from .validators.v3_0_0.jsd_c6c330dace185a548f70f4e5d67776ea \
    import JSONSchemaValidatorC6C330DaCe185A548F70F4E5D67776Ea \
    as JSONSchemaValidatorC6C330DaCe185A548F70F4E5D67776Ea_v3_0_0
from .validators.v3_0_0.jsd_c7aa2a6cac155a6cb7ace3fd76a81e0f \
    import JSONSchemaValidatorC7Aa2A6CAc155A6CB7AcE3Fd76A81E0F \
    as JSONSchemaValidatorC7Aa2A6CAc155A6CB7AcE3Fd76A81E0F_v3_0_0
from .validators.v3_0_0.jsd_c8acebd86a8151aeb2c17d973696fdfa \
    import JSONSchemaValidatorC8Acebd86A8151AeB2C17D973696Fdfa \
    as JSONSchemaValidatorC8Acebd86A8151AeB2C17D973696Fdfa_v3_0_0
from .validators.v3_0_0.jsd_c8cd2f618b655d988ce626e579486596 \
    import JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596 \
    as JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596_v3_0_0
from .validators.v3_0_0.jsd_c8dbec9679d453f78cb47d894c507a7b \
    import JSONSchemaValidatorC8Dbec9679D453F78Cb47D894C507A7B \
    as JSONSchemaValidatorC8Dbec9679D453F78Cb47D894C507A7B_v3_0_0
from .validators.v3_0_0.jsd_c97e7851003e5a63a2a8005ac8807dc7 \
    import JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7 \
    as JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7_v3_0_0
from .validators.v3_0_0.jsd_c9a67d3e9015580f93a52627f19e9916 \
    import JSONSchemaValidatorC9A67D3E9015580F93A52627F19E9916 \
    as JSONSchemaValidatorC9A67D3E9015580F93A52627F19E9916_v3_0_0
from .validators.v3_0_0.jsd_ca28129793d1569bb50de9f43b0d0ee8 \
    import JSONSchemaValidatorCa28129793D1569BB50DE9F43B0D0Ee8 \
    as JSONSchemaValidatorCa28129793D1569BB50DE9F43B0D0Ee8_v3_0_0
from .validators.v3_0_0.jsd_ca3df31c13b857e6b5dbc8357a8ab010 \
    import JSONSchemaValidatorCa3Df31C13B857E6B5DbC8357A8Ab010 \
    as JSONSchemaValidatorCa3Df31C13B857E6B5DbC8357A8Ab010_v3_0_0
from .validators.v3_0_0.jsd_cc6dfd258c49529db4c580411afe868b \
    import JSONSchemaValidatorCc6Dfd258C49529DB4C580411Afe868B \
    as JSONSchemaValidatorCc6Dfd258C49529DB4C580411Afe868B_v3_0_0
from .validators.v3_0_0.jsd_cc909c2717cf55f1863a04a785166fe0 \
    import JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0 \
    as JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0_v3_0_0
from .validators.v3_0_0.jsd_cd04558011d055b1ac3386e24728083d \
    import JSONSchemaValidatorCd04558011D055B1Ac3386E24728083D \
    as JSONSchemaValidatorCd04558011D055B1Ac3386E24728083D_v3_0_0
from .validators.v3_0_0.jsd_cd429bb8ff3556a796570480f742028b \
    import JSONSchemaValidatorCd429Bb8Ff3556A796570480F742028B \
    as JSONSchemaValidatorCd429Bb8Ff3556A796570480F742028B_v3_0_0
from .validators.v3_0_0.jsd_cd6793a4a8e7576c8b290bdc88001f6f \
    import JSONSchemaValidatorCd6793A4A8E7576C8B290Bdc88001F6F \
    as JSONSchemaValidatorCd6793A4A8E7576C8B290Bdc88001F6F_v3_0_0
from .validators.v3_0_0.jsd_ce3085eebdd15be7ac56b5970265d8df \
    import JSONSchemaValidatorCe3085EeBdd15Be7Ac56B5970265D8Df \
    as JSONSchemaValidatorCe3085EeBdd15Be7Ac56B5970265D8Df_v3_0_0
from .validators.v3_0_0.jsd_d0e432f52e2a5863858c7dc0c3eda277 \
    import JSONSchemaValidatorD0E432F52E2A5863858C7Dc0C3Eda277 \
    as JSONSchemaValidatorD0E432F52E2A5863858C7Dc0C3Eda277_v3_0_0
from .validators.v3_0_0.jsd_d388e26255a15233ac682c0406880cfb \
    import JSONSchemaValidatorD388E26255A15233Ac682C0406880Cfb \
    as JSONSchemaValidatorD388E26255A15233Ac682C0406880Cfb_v3_0_0
from .validators.v3_0_0.jsd_d43fec9e7dc556cbb9bf0ebd1dcd6aad \
    import JSONSchemaValidatorD43Fec9E7Dc556CbB9Bf0Ebd1Dcd6Aad \
    as JSONSchemaValidatorD43Fec9E7Dc556CbB9Bf0Ebd1Dcd6Aad_v3_0_0
from .validators.v3_0_0.jsd_d5572c56526151cb8ea42de44b2db52c \
    import JSONSchemaValidatorD5572C56526151Cb8Ea42De44B2Db52C \
    as JSONSchemaValidatorD5572C56526151Cb8Ea42De44B2Db52C_v3_0_0
from .validators.v3_0_0.jsd_d5e00a8e6aa0577ea81e11e796912053 \
    import JSONSchemaValidatorD5E00A8E6Aa0577EA81E11E796912053 \
    as JSONSchemaValidatorD5E00A8E6Aa0577EA81E11E796912053_v3_0_0
from .validators.v3_0_0.jsd_d810359e31e453ac8145981b7d5bb7e4 \
    import JSONSchemaValidatorD810359E31E453Ac8145981B7D5Bb7E4 \
    as JSONSchemaValidatorD810359E31E453Ac8145981B7D5Bb7E4_v3_0_0
from .validators.v3_0_0.jsd_d82fe0f9e4635b74af809beaaf98bd07 \
    import JSONSchemaValidatorD82Fe0F9E4635B74Af809Beaaf98Bd07 \
    as JSONSchemaValidatorD82Fe0F9E4635B74Af809Beaaf98Bd07_v3_0_0
from .validators.v3_0_0.jsd_d912b1c21e2b5dca8b56332d3a8ad13d \
    import JSONSchemaValidatorD912B1C21E2B5Dca8B56332D3A8Ad13D \
    as JSONSchemaValidatorD912B1C21E2B5Dca8B56332D3A8Ad13D_v3_0_0
from .validators.v3_0_0.jsd_da4bb24b7e4d594cb026335a75248e1a \
    import JSONSchemaValidatorDa4Bb24B7E4D594CB026335A75248E1A \
    as JSONSchemaValidatorDa4Bb24B7E4D594CB026335A75248E1A_v3_0_0
from .validators.v3_0_0.jsd_db686413cf4558188ea60ccc05c3e920 \
    import JSONSchemaValidatorDb686413Cf4558188Ea60Ccc05C3E920 \
    as JSONSchemaValidatorDb686413Cf4558188Ea60Ccc05C3E920_v3_0_0
from .validators.v3_0_0.jsd_ded7f8573c255c318bb1f04bfdbf01e1 \
    import JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1 \
    as JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1_v3_0_0
from .validators.v3_0_0.jsd_dfa8f48210e85715beebb44e62fac408 \
    import JSONSchemaValidatorDfa8F48210E85715BeebB44E62Fac408 \
    as JSONSchemaValidatorDfa8F48210E85715BeebB44E62Fac408_v3_0_0
from .validators.v3_0_0.jsd_dfae2409eecc551298e9fa31d14f43d0 \
    import JSONSchemaValidatorDfae2409Eecc551298E9Fa31D14F43D0 \
    as JSONSchemaValidatorDfae2409Eecc551298E9Fa31D14F43D0_v3_0_0
from .validators.v3_0_0.jsd_e1d938f110e059a5abcb9cc8fb3cbd7c \
    import JSONSchemaValidatorE1D938F110E059A5Abcb9Cc8Fb3Cbd7C \
    as JSONSchemaValidatorE1D938F110E059A5Abcb9Cc8Fb3Cbd7C_v3_0_0
from .validators.v3_0_0.jsd_e313d50be9155acca1082ef11895aeb8 \
    import JSONSchemaValidatorE313D50BE9155AccA1082Ef11895Aeb8 \
    as JSONSchemaValidatorE313D50BE9155AccA1082Ef11895Aeb8_v3_0_0
from .validators.v3_0_0.jsd_e39868ea7aec5efcaaf55009699eda5d \
    import JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D \
    as JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D_v3_0_0
from .validators.v3_0_0.jsd_e623dba049b5569c83e13ccf4360e369 \
    import JSONSchemaValidatorE623Dba049B5569C83E13Ccf4360E369 \
    as JSONSchemaValidatorE623Dba049B5569C83E13Ccf4360E369_v3_0_0
from .validators.v3_0_0.jsd_e75d766151e85011870229f30e4f5ec3 \
    import JSONSchemaValidatorE75D766151E85011870229F30E4F5Ec3 \
    as JSONSchemaValidatorE75D766151E85011870229F30E4F5Ec3_v3_0_0
from .validators.v3_0_0.jsd_e7bd468ee94f53869e52e84454efd0e6 \
    import JSONSchemaValidatorE7Bd468EE94F53869E52E84454Efd0E6 \
    as JSONSchemaValidatorE7Bd468EE94F53869E52E84454Efd0E6_v3_0_0
from .validators.v3_0_0.jsd_e82e46732de25832a543c4640312588c \
    import JSONSchemaValidatorE82E46732De25832A543C4640312588C \
    as JSONSchemaValidatorE82E46732De25832A543C4640312588C_v3_0_0
from .validators.v3_0_0.jsd_e9ce4a1e1cf955f098343646760e9d58 \
    import JSONSchemaValidatorE9Ce4A1E1Cf955F098343646760E9D58 \
    as JSONSchemaValidatorE9Ce4A1E1Cf955F098343646760E9D58_v3_0_0
from .validators.v3_0_0.jsd_ea658190e73c5ce1b27e7def4aea28e3 \
    import JSONSchemaValidatorEa658190E73C5Ce1B27E7Def4Aea28E3 \
    as JSONSchemaValidatorEa658190E73C5Ce1B27E7Def4Aea28E3_v3_0_0
from .validators.v3_0_0.jsd_eaa0d7c339d152b688876c2e10f51fe7 \
    import JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7 \
    as JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7_v3_0_0
from .validators.v3_0_0.jsd_eb8e0ce63376573995a49178435f7747 \
    import JSONSchemaValidatorEb8E0Ce63376573995A49178435F7747 \
    as JSONSchemaValidatorEb8E0Ce63376573995A49178435F7747_v3_0_0
from .validators.v3_0_0.jsd_eba5dd37c1f5532992a96c2db7ecff5d \
    import JSONSchemaValidatorEba5Dd37C1F5532992A96C2Db7Ecff5D \
    as JSONSchemaValidatorEba5Dd37C1F5532992A96C2Db7Ecff5D_v3_0_0
from .validators.v3_0_0.jsd_ec26ec11d92356a594a6efa55ccb9be7 \
    import JSONSchemaValidatorEc26Ec11D92356A594A6Efa55Ccb9Be7 \
    as JSONSchemaValidatorEc26Ec11D92356A594A6Efa55Ccb9Be7_v3_0_0
from .validators.v3_0_0.jsd_ecff2eb67fe5591f8d9026f928a0d8aa \
    import JSONSchemaValidatorEcff2Eb67Fe5591F8D9026F928A0D8Aa \
    as JSONSchemaValidatorEcff2Eb67Fe5591F8D9026F928A0D8Aa_v3_0_0
from .validators.v3_0_0.jsd_ed1ef503c091506aa8e446182e625365 \
    import JSONSchemaValidatorEd1Ef503C091506AA8E446182E625365 \
    as JSONSchemaValidatorEd1Ef503C091506AA8E446182E625365_v3_0_0
from .validators.v3_0_0.jsd_ed8575d86539534082d6e83ced01c40b \
    import JSONSchemaValidatorEd8575D86539534082D6E83Ced01C40B \
    as JSONSchemaValidatorEd8575D86539534082D6E83Ced01C40B_v3_0_0
from .validators.v3_0_0.jsd_eea0f876f20c59ed8eff33f1f4fe10a8 \
    import JSONSchemaValidatorEea0F876F20C59Ed8Eff33F1F4Fe10A8 \
    as JSONSchemaValidatorEea0F876F20C59Ed8Eff33F1F4Fe10A8_v3_0_0
from .validators.v3_0_0.jsd_f1196f1f6fde5978b0522f096926d443 \
    import JSONSchemaValidatorF1196F1F6Fde5978B0522F096926D443 \
    as JSONSchemaValidatorF1196F1F6Fde5978B0522F096926D443_v3_0_0
from .validators.v3_0_0.jsd_f130b53af83c5b7baa2acd190b57fd75 \
    import JSONSchemaValidatorF130B53AF83C5B7BAa2ACd190B57Fd75 \
    as JSONSchemaValidatorF130B53AF83C5B7BAa2ACd190B57Fd75_v3_0_0
from .validators.v3_0_0.jsd_f1b8eaf23e795f1a8525eb5905187aa9 \
    import JSONSchemaValidatorF1B8Eaf23E795F1A8525Eb5905187Aa9 \
    as JSONSchemaValidatorF1B8Eaf23E795F1A8525Eb5905187Aa9_v3_0_0
from .validators.v3_0_0.jsd_f1ff2b82953f5131884f0779db37190c \
    import JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C \
    as JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C_v3_0_0
from .validators.v3_0_0.jsd_f3b45b8e4089574c9912407f88b1a5d2 \
    import JSONSchemaValidatorF3B45B8E4089574C9912407F88B1A5D2 \
    as JSONSchemaValidatorF3B45B8E4089574C9912407F88B1A5D2_v3_0_0
from .validators.v3_0_0.jsd_f41d844dbee15f7680920652004f69b6 \
    import JSONSchemaValidatorF41D844DBee15F7680920652004F69B6 \
    as JSONSchemaValidatorF41D844DBee15F7680920652004F69B6_v3_0_0
from .validators.v3_0_0.jsd_f41f77362663580d8cc3e6e88623889d \
    import JSONSchemaValidatorF41F77362663580D8Cc3E6E88623889D \
    as JSONSchemaValidatorF41F77362663580D8Cc3E6E88623889D_v3_0_0
from .validators.v3_0_0.jsd_f4dbfb874b3b56d7a651d6732f1bd55e \
    import JSONSchemaValidatorF4Dbfb874B3B56D7A651D6732F1Bd55E \
    as JSONSchemaValidatorF4Dbfb874B3B56D7A651D6732F1Bd55E_v3_0_0
from .validators.v3_0_0.jsd_f5175ff711535ff2b1b85a3a4525e886 \
    import JSONSchemaValidatorF5175Ff711535Ff2B1B85A3A4525E886 \
    as JSONSchemaValidatorF5175Ff711535Ff2B1B85A3A4525E886_v3_0_0
from .validators.v3_0_0.jsd_f68aee0cdb425390b3ca90b0b46e6e2c \
    import JSONSchemaValidatorF68Aee0CDb425390B3Ca90B0B46E6E2C \
    as JSONSchemaValidatorF68Aee0CDb425390B3Ca90B0B46E6E2C_v3_0_0
from .validators.v3_0_0.jsd_f79ab23563d857e58e01a74e37333572 \
    import JSONSchemaValidatorF79Ab23563D857E58E01A74E37333572 \
    as JSONSchemaValidatorF79Ab23563D857E58E01A74E37333572_v3_0_0
from .validators.v3_0_0.jsd_f831d9ed2beb5c2b967aa10db8c22046 \
    import JSONSchemaValidatorF831D9Ed2Beb5C2B967AA10Db8C22046 \
    as JSONSchemaValidatorF831D9Ed2Beb5C2B967AA10Db8C22046_v3_0_0
from .validators.v3_0_0.jsd_f8a2f0834e625822bed1cb4cf34fde5e \
    import JSONSchemaValidatorF8A2F0834E625822Bed1Cb4Cf34Fde5E \
    as JSONSchemaValidatorF8A2F0834E625822Bed1Cb4Cf34Fde5E_v3_0_0
from .validators.v3_0_0.jsd_f9c9a5e917af53dbbb91733e82e72ebe \
    import JSONSchemaValidatorF9C9A5E917Af53DbBb91733E82E72Ebe \
    as JSONSchemaValidatorF9C9A5E917Af53DbBb91733E82E72Ebe_v3_0_0
from .validators.v3_0_0.jsd_fa838e78175e51b4bcfb0821c19b81b7 \
    import JSONSchemaValidatorFa838E78175E51B4Bcfb0821C19B81B7 \
    as JSONSchemaValidatorFa838E78175E51B4Bcfb0821C19B81B7_v3_0_0
from .validators.v3_0_0.jsd_fc9a4ee495785518bd2251b6b4fb41f4 \
    import JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4 \
    as JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4_v3_0_0
from .validators.v3_0_0.jsd_fc9ecf1e469154ae845236dbed070904 \
    import JSONSchemaValidatorFc9Ecf1E469154Ae845236Dbed070904 \
    as JSONSchemaValidatorFc9Ecf1E469154Ae845236Dbed070904_v3_0_0
from .validators.v3_0_0.jsd_fda64cd1ab7d53448962f61de0f76948 \
    import JSONSchemaValidatorFda64Cd1Ab7D53448962F61De0F76948 \
    as JSONSchemaValidatorFda64Cd1Ab7D53448962F61De0F76948_v3_0_0
from .validators.v3_0_0.jsd_fe54c96ccba65af1abe3cd08f4fc69cb \
    import JSONSchemaValidatorFe54C96CCba65Af1Abe3Cd08F4Fc69Cb \
    as JSONSchemaValidatorFe54C96CCba65Af1Abe3Cd08F4Fc69Cb_v3_0_0
from .validators.v3_0_0.jsd_feb30ca768795eed82c118d009d7bcd4 \
    import JSONSchemaValidatorFeb30Ca768795Eed82C118D009D7Bcd4 \
    as JSONSchemaValidatorFeb30Ca768795Eed82C118D009D7Bcd4_v3_0_0
from .validators.v3_0_0.jsd_ffff1c792bf559ebb39b789421be6966 \
    import JSONSchemaValidatorFfff1C792Bf559EbB39B789421Be6966 \
    as JSONSchemaValidatorFfff1C792Bf559EbB39B789421Be6966_v3_0_0


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
            self.json_schema_validators['jsd_ac8c8cb9b5007a1e1a6434a20a881_v3_0_0'] =\
                JSONSchemaValidatorAc8C8Cb9B5007A1E1A6434A20A881_v3_0_0()
            self.json_schema_validators['jsd_d6b1385f4cb9381c13a1fa4356_v3_0_0'] =\
                JSONSchemaValidatorD6B1385F4CB9381C13A1Fa4356_v3_0_0()
            self.json_schema_validators['jsd_daa171ab765a02a714c48376b3790d_v3_0_0'] =\
                JSONSchemaValidatorDaa171Ab765A02A714C48376B3790D_v3_0_0()
            self.json_schema_validators['jsd_fde0cbd2de50f680d0b0f681771829_v3_0_0'] =\
                JSONSchemaValidatorFde0CbD2De50F680D0B0F681771829_v3_0_0()
            self.json_schema_validators['jsd_d8f04f3635c6c9e6e94f76fe8cf7b_v3_0_0'] =\
                JSONSchemaValidatorD8F04F3635C6C9E6E94F76Fe8Cf7B_v3_0_0()
            self.json_schema_validators['jsd_fbd7ec7052709e5d0e0a46dc7f68_v3_0_0'] =\
                JSONSchemaValidatorFbd7Ec7052709E5D0E0A46Dc7F68_v3_0_0()
            self.json_schema_validators['jsd_f9f734e2f058f59e13801f1ed4780e_v3_0_0'] =\
                JSONSchemaValidatorF9F734E2F058F59E13801F1Ed4780E_v3_0_0()
            self.json_schema_validators['jsd_db1d9dda53369e35d33138b29c16_v3_0_0'] =\
                JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16_v3_0_0()
            self.json_schema_validators['jsd_e3c94fb105cd4a6eac4ace8c87f9f_v3_0_0'] =\
                JSONSchemaValidatorE3C94Fb105Cd4A6EaC4Ace8C87F9F_v3_0_0()
            self.json_schema_validators['jsd_e4686a7511884fd3eee7c582efb_v3_0_0'] =\
                JSONSchemaValidatorE4686A7511884Fd3Eee7C582Efb_v3_0_0()
            self.json_schema_validators['jsd_d5a4d54609f344c0d766b7c16_v3_0_0'] =\
                JSONSchemaValidatorD5A4D54609F344C0D766B7C16_v3_0_0()
            self.json_schema_validators['jsd_da54f237752bd84ccfc8341f89bf8_v3_0_0'] =\
                JSONSchemaValidatorDa54F237752Bd84CcFc8341F89Bf8_v3_0_0()
            self.json_schema_validators['jsd_ac243ecb8c157658a4bcfe77a102c14_v3_0_0'] =\
                JSONSchemaValidatorAc243EcB8C157658A4BCfe77A102C14_v3_0_0()
            self.json_schema_validators['jsd_ad47b73307755749ca8182a34affb38_v3_0_0'] =\
                JSONSchemaValidatorAd47B73307755749Ca8182A34Affb38_v3_0_0()
            self.json_schema_validators['jsd_cdc971b23285b87945021bd5983d1cd_v3_0_0'] =\
                JSONSchemaValidatorCdc971B23285B87945021Bd5983D1Cd_v3_0_0()
            self.json_schema_validators['jsd_d1df0e230765104863b8d63d5beb68e_v3_0_0'] =\
                JSONSchemaValidatorD1Df0E230765104863B8D63D5Beb68E_v3_0_0()
            self.json_schema_validators['jsd_f41a1e47105581fabf212f259626903_v3_0_0'] =\
                JSONSchemaValidatorF41A1E47105581FAbf212F259626903_v3_0_0()
            self.json_schema_validators['jsd_e34177d675622acd0a532f5b7c41b_v3_0_0'] =\
                JSONSchemaValidatorE34177D675622Acd0A532F5B7C41B_v3_0_0()
            self.json_schema_validators['jsd_f8f4956d29b821fa9bbf23266_v3_0_0'] =\
                JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266_v3_0_0()
            self.json_schema_validators['jsd_ab05dc6105e47b391030a5fe50ecb_v3_0_0'] =\
                JSONSchemaValidatorAb05DC6105E47B391030A5Fe50Ecb_v3_0_0()
            self.json_schema_validators['jsd_ebcdc835e9b8d6844c1da6cf252_v3_0_0'] =\
                JSONSchemaValidatorEbcDc835E9B8D6844C1Da6Cf252_v3_0_0()
            self.json_schema_validators['jsd_3bfe54779ae1b3edccb16fa7_v3_0_0'] =\
                JSONSchemaValidator3Bfe54779Ae1B3Edccb16Fa7_v3_0_0()
            self.json_schema_validators['jsd_ea10f18c3655db84657ad855bf6972_v3_0_0'] =\
                JSONSchemaValidatorEa10F18C3655Db84657Ad855Bf6972_v3_0_0()
            self.json_schema_validators['jsd_b9e8541f25c4ea29944f659f68994_v3_0_0'] =\
                JSONSchemaValidatorB9E8541F25C4EA29944F659F68994_v3_0_0()
            self.json_schema_validators['jsd_c8aec23a55399a175acf105dbe1c2_v3_0_0'] =\
                JSONSchemaValidatorC8Aec23A55399A175Acf105Dbe1C2_v3_0_0()
            self.json_schema_validators['jsd_a35a4deda255abb3933e64d74679c1_v3_0_0'] =\
                JSONSchemaValidatorA35A4DEda255AbB3933E64D74679C1_v3_0_0()
            self.json_schema_validators['jsd_cfcc7615d0492e2dd1b04dd03a9_v3_0_0'] =\
                JSONSchemaValidatorCfcC7615D0492E2Dd1B04Dd03A9_v3_0_0()
            self.json_schema_validators['jsd_c813c9b5a73b6d00cac1ca5a41f_v3_0_0'] =\
                JSONSchemaValidatorC813C9B5A73B6D00Cac1Ca5A41F_v3_0_0()
            self.json_schema_validators['jsd_d26670a205a78800cb50673027a6e_v3_0_0'] =\
                JSONSchemaValidatorD26670A205A78800CB50673027A6E_v3_0_0()
            self.json_schema_validators['jsd_f5d5ab6568d8bf5f9932f7ed7f4_v3_0_0'] =\
                JSONSchemaValidatorF5D5Ab6568D8Bf5F9932F7Ed7F4_v3_0_0()
            self.json_schema_validators['jsd_daac88943a5cd2bd745c483448e231_v3_0_0'] =\
                JSONSchemaValidatorDaac88943A5Cd2Bd745C483448E231_v3_0_0()
            self.json_schema_validators['jsd_e6d1b224e058288a8c4d70be72c9a6_v3_0_0'] =\
                JSONSchemaValidatorE6D1B224E058288A8C4D70Be72C9A6_v3_0_0()
            self.json_schema_validators['jsd_d6d09f7a5084ac7036167214b0e1_v3_0_0'] =\
                JSONSchemaValidatorD6D09F7A5084Ac7036167214B0E1_v3_0_0()
            self.json_schema_validators['jsd_a11a1ff1ee5387b669bcde99f86fbf_v3_0_0'] =\
                JSONSchemaValidatorA11A1FF1Ee5387B669Bcde99F86Fbf_v3_0_0()
            self.json_schema_validators['jsd_f1fd8e2bd1581aabf7cd87bff65137_v3_0_0'] =\
                JSONSchemaValidatorF1Fd8E2Bd1581AAbf7Cd87Bff65137_v3_0_0()
            self.json_schema_validators['jsd_a5abd33eeaa52e39e926472751ef79e_v3_0_0'] =\
                JSONSchemaValidatorA5Abd33Eeaa52E39E926472751Ef79E_v3_0_0()
            self.json_schema_validators['jsd_b62a711ce705542b5d1d92b7d3ca431_v3_0_0'] =\
                JSONSchemaValidatorB62A711Ce705542B5D1D92B7D3Ca431_v3_0_0()
            self.json_schema_validators['jsd_d79b507bda155c180d42f0a67ef64d5_v3_0_0'] =\
                JSONSchemaValidatorD79B507Bda155C180D42F0A67Ef64D5_v3_0_0()
            self.json_schema_validators['jsd_dbe47028859573988880de76fec0936_v3_0_0'] =\
                JSONSchemaValidatorDbe47028859573988880De76Fec0936_v3_0_0()
            self.json_schema_validators['jsd_f18bdd1938755409bf6db6b29e85d3a_v3_0_0'] =\
                JSONSchemaValidatorF18Bdd1938755409Bf6Db6B29E85D3A_v3_0_0()
            self.json_schema_validators['jsd_c53b22885f5e5d82fb8cadd0332136_v3_0_0'] =\
                JSONSchemaValidatorC53B22885F5E5D82Fb8Cadd0332136_v3_0_0()
            self.json_schema_validators['jsd_e23ac4c658f5b75f19d13d6f7189_v3_0_0'] =\
                JSONSchemaValidatorE23AC4C658F5B75F19D13D6F7189_v3_0_0()
            self.json_schema_validators['jsd_ce65f2bd375be1ba41a7d6f02ad7b6_v3_0_0'] =\
                JSONSchemaValidatorCe65F2Bd375Be1Ba41A7D6F02Ad7B6_v3_0_0()
            self.json_schema_validators['jsd_cb625d5ad0ad76b93282f5818a_v3_0_0'] =\
                JSONSchemaValidatorCb625D5Ad0Ad76B93282F5818A_v3_0_0()
            self.json_schema_validators['jsd_a599ae00f5e47b9ece23cd3183d1c_v3_0_0'] =\
                JSONSchemaValidatorA599AE00F5E47B9EcE23Cd3183D1C_v3_0_0()
            self.json_schema_validators['jsd_c288192f954309b4b35aa612ff226_v3_0_0'] =\
                JSONSchemaValidatorC288192F954309B4B35Aa612Ff226_v3_0_0()
            self.json_schema_validators['jsd_f64c3c08518e9eef83a92d69cde3_v3_0_0'] =\
                JSONSchemaValidatorF64C3C08518E9Eef83A92D69Cde3_v3_0_0()
            self.json_schema_validators['jsd_a60516435c6abd996dd616781c16_v3_0_0'] =\
                JSONSchemaValidatorA60516435C6ABd996Dd616781C16_v3_0_0()
            self.json_schema_validators['jsd_c3c7d5a3a83d9f7441972d399_v3_0_0'] =\
                JSONSchemaValidatorC3C7D5A3A83D9F7441972D399_v3_0_0()
            self.json_schema_validators['jsd_a4d5b5da6a50bfaaecc180543fd952_v3_0_0'] =\
                JSONSchemaValidatorA4D5B5Da6A50BfAaecC180543Fd952_v3_0_0()
            self.json_schema_validators['jsd_a99695fd5ee0b00efce79a5761ff_v3_0_0'] =\
                JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff_v3_0_0()
            self.json_schema_validators['jsd_da0a59db7654cfa89df49ca3ac3414_v3_0_0'] =\
                JSONSchemaValidatorDa0A59Db7654CfA89DF49Ca3Ac3414_v3_0_0()
            self.json_schema_validators['jsd_f59cbefb9504fb36b3e50c355f1c0_v3_0_0'] =\
                JSONSchemaValidatorF59CbEfb9504FB36B3E50C355F1C0_v3_0_0()
            self.json_schema_validators['jsd_a1af553d663556ca429a10ed82effda_v3_0_0'] =\
                JSONSchemaValidatorA1Af553D663556CA429A10Ed82Effda_v3_0_0()
            self.json_schema_validators['jsd_a40f9e169a95d6dbf3ebbb020291007_v3_0_0'] =\
                JSONSchemaValidatorA40F9E169A95D6DBf3EBbb020291007_v3_0_0()
            self.json_schema_validators['jsd_a72ae8af1075d0c94912b008003b13e_v3_0_0'] =\
                JSONSchemaValidatorA72Ae8AF1075D0C94912B008003B13E_v3_0_0()
            self.json_schema_validators['jsd_ab96d3d76de5d05bbac1f27feacb7b0_v3_0_0'] =\
                JSONSchemaValidatorAb96D3D76De5D05Bbac1F27Feacb7B0_v3_0_0()
            self.json_schema_validators['jsd_b94d7d3f0ed5d0b938151ae2cae9fa4_v3_0_0'] =\
                JSONSchemaValidatorB94D7D3F0Ed5D0B938151Ae2Cae9Fa4_v3_0_0()
            self.json_schema_validators['jsd_b994e6c8b8d53f29230686824c9fafa_v3_0_0'] =\
                JSONSchemaValidatorB994E6C8B8D53F29230686824C9Fafa_v3_0_0()
            self.json_schema_validators['jsd_c5c37c343c050e0af67b2223e64faf3_v3_0_0'] =\
                JSONSchemaValidatorC5C37C343C050E0Af67B2223E64Faf3_v3_0_0()
            self.json_schema_validators['jsd_caefe2cb042513ab4a4a76f227330cb_v3_0_0'] =\
                JSONSchemaValidatorCaefe2CB042513AB4A4A76F227330Cb_v3_0_0()
            self.json_schema_validators['jsd_e232c5666ab5ed783588f413c3bc644_v3_0_0'] =\
                JSONSchemaValidatorE232C5666Ab5Ed783588F413C3Bc644_v3_0_0()
            self.json_schema_validators['jsd_eeef18d70b159f788b717e301dd3643_v3_0_0'] =\
                JSONSchemaValidatorEeef18D70B159F788B717E301Dd3643_v3_0_0()
            self.json_schema_validators['jsd_f8ba0e97135ca6bacff94d5a76df97_v3_0_0'] =\
                JSONSchemaValidatorF8Ba0E97135Ca6BacfF94D5A76Df97_v3_0_0()
            self.json_schema_validators['jsd_dc2eec65ad680a3c5de47cd87c8_v3_0_0'] =\
                JSONSchemaValidatorDc2Eec65Ad680A3C5De47Cd87C8_v3_0_0()
            self.json_schema_validators['jsd_b8696d875b12b0a3ab735b397d7a_v3_0_0'] =\
                JSONSchemaValidatorB8696D875B12B0A3Ab735B397D7A_v3_0_0()
            self.json_schema_validators['jsd_e5355db6a478daa29f318303_v3_0_0'] =\
                JSONSchemaValidatorE5355Db6A478Daa29F318303_v3_0_0()
            self.json_schema_validators['jsd_b9e7d29b0356b2b1d5fdb2e1069265_v3_0_0'] =\
                JSONSchemaValidatorB9E7D29B0356B2B1D5Fdb2E1069265_v3_0_0()
            self.json_schema_validators['jsd_c5c9b7ab72b5442ae7026a5dcc0fec3_v3_0_0'] =\
                JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3_v3_0_0()
            self.json_schema_validators['jsd_ccba98a61555ae495f6a05284e3b5ae_v3_0_0'] =\
                JSONSchemaValidatorCcba98A61555Ae495F6A05284E3B5Ae_v3_0_0()
            self.json_schema_validators['jsd_d14f56096ec518086b3e5d386bd3139_v3_0_0'] =\
                JSONSchemaValidatorD14F56096Ec518086B3E5D386Bd3139_v3_0_0()
            self.json_schema_validators['jsd_e155669bc74586e9ef2580ec5752902_v3_0_0'] =\
                JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902_v3_0_0()
            self.json_schema_validators['jsd_f36e90115b05416a71506061fed7e5c_v3_0_0'] =\
                JSONSchemaValidatorF36E90115B05416A71506061Fed7E5C_v3_0_0()
            self.json_schema_validators['jsd_c4fada6c558d9aba09cc373d5b266_v3_0_0'] =\
                JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0()
            self.json_schema_validators['jsd_b11e2f1af656bcb5880a7b33720ec5_v3_0_0'] =\
                JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0()
            self.json_schema_validators['jsd_c9722c56108cac8ca50bf8f01c_v3_0_0'] =\
                JSONSchemaValidatorC9722C56108Cac8Ca50Bf8F01C_v3_0_0()
            self.json_schema_validators['jsd_cb9345e58f5433ae80f5d8f855978b_v3_0_0'] =\
                JSONSchemaValidatorCb9345E58F5433Ae80F5D8F855978B_v3_0_0()
            self.json_schema_validators['jsd_b986fa0f0d54ef98eb135eeb88808a_v3_0_0'] =\
                JSONSchemaValidatorB986Fa0F0D54Ef98Eb135Eeb88808A_v3_0_0()
            self.json_schema_validators['jsd_c47e28f13659658b3e6af9409a1177_v3_0_0'] =\
                JSONSchemaValidatorC47E28F13659658B3E6Af9409A1177_v3_0_0()
            self.json_schema_validators['jsd_fb9c22ad9a5eddb590c85abdab460b_v3_0_0'] =\
                JSONSchemaValidatorFb9C22Ad9A5EddB590C85Abdab460B_v3_0_0()
            self.json_schema_validators['jsd_fd729f50e65695966359b589a1606b_v3_0_0'] =\
                JSONSchemaValidatorFd729F50E65695966359B589A1606B_v3_0_0()
            self.json_schema_validators['jsd_b03900a2e5027b615d9f1bdcf9f63_v3_0_0'] =\
                JSONSchemaValidatorB03900A2E5027B615D9F1Bdcf9F63_v3_0_0()
            self.json_schema_validators['jsd_acb5a41fe395b158a3fe1cda996b0cf_v3_0_0'] =\
                JSONSchemaValidatorAcb5A41Fe395B158A3FE1Cda996B0Cf_v3_0_0()
            self.json_schema_validators['jsd_cb8a98ab3d456f387ad6ef911a7293f_v3_0_0'] =\
                JSONSchemaValidatorCb8A98AB3D456F387Ad6Ef911A7293F_v3_0_0()
            self.json_schema_validators['jsd_e6c7251a8508597f1b7ae61cbf953_v3_0_0'] =\
                JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953_v3_0_0()
            self.json_schema_validators['jsd_e4c74e9b4e559e95c73e81183a6c7a_v3_0_0'] =\
                JSONSchemaValidatorE4C74E9B4E559E95C73E81183A6C7A_v3_0_0()
            self.json_schema_validators['jsd_a03a30be865ca599e77c63a332978b_v3_0_0'] =\
                JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B_v3_0_0()
            self.json_schema_validators['jsd_c189f2f5f6b8bab3931c206c949_v3_0_0'] =\
                JSONSchemaValidatorC189F2F5F6B8Bab3931C206C949_v3_0_0()
            self.json_schema_validators['jsd_d8610d4a355b63aaaa364447d5fa00_v3_0_0'] =\
                JSONSchemaValidatorD8610D4A355B63Aaaa364447D5Fa00_v3_0_0()
            self.json_schema_validators['jsd_dee8ff57265324a99fa2011bb4dc5f_v3_0_0'] =\
                JSONSchemaValidatorDee8Ff57265324A99FA2011Bb4Dc5F_v3_0_0()
            self.json_schema_validators['jsd_feb825519f98bd1541ef3c367d_v3_0_0'] =\
                JSONSchemaValidatorFeB825519F98Bd1541Ef3C367D_v3_0_0()
            self.json_schema_validators['jsd_d1132a216d54d091022aec0ad018f8_v3_0_0'] =\
                JSONSchemaValidatorD1132A216D54D091022Aec0Ad018F8_v3_0_0()
            self.json_schema_validators['jsd_ad69fa1d850f4993bbfc888749fa0_v3_0_0'] =\
                JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0()
            self.json_schema_validators['jsd_f723c1a3e533893ec03335e072cfe_v3_0_0'] =\
                JSONSchemaValidatorF723C1A3E533893Ec03335E072Cfe_v3_0_0()
            self.json_schema_validators['jsd_f564c3eda5c20bb807b8c062c8e7b_v3_0_0'] =\
                JSONSchemaValidatorF564C3Eda5C20Bb807B8C062C8E7B_v3_0_0()
            self.json_schema_validators['jsd_abc25887a5daab1216195e08cbd49_v3_0_0'] =\
                JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49_v3_0_0()
            self.json_schema_validators['jsd_ad233598ed75e0c97ddd3c3f1af50e4_v3_0_0'] =\
                JSONSchemaValidatorAd233598Ed75E0C97DdD3C3F1Af50E4_v3_0_0()
            self.json_schema_validators['jsd_c475afd2a5e57e4bd0952f2c5349c6c_v3_0_0'] =\
                JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C_v3_0_0()
            self.json_schema_validators['jsd_ce70db7732c596aa82bd7d1725ac02d_v3_0_0'] =\
                JSONSchemaValidatorCe70Db7732C596AA82BD7D1725Ac02D_v3_0_0()
            self.json_schema_validators['jsd_d6be8d877485969954d2574f0448247_v3_0_0'] =\
                JSONSchemaValidatorD6Be8D877485969954D2574F0448247_v3_0_0()
            self.json_schema_validators['jsd_e4bfa620f76545d9887045cd24d99a2_v3_0_0'] =\
                JSONSchemaValidatorE4Bfa620F76545D9887045Cd24D99A2_v3_0_0()
            self.json_schema_validators['jsd_a0aadd33595645bf671efc4912f89a_v3_0_0'] =\
                JSONSchemaValidatorA0Aadd33595645Bf671Efc4912F89A_v3_0_0()
            self.json_schema_validators['jsd_a56f5c5f739a83e8806da16be5_v3_0_0'] =\
                JSONSchemaValidatorA56F5C5F739A83E8806Da16Be5_v3_0_0()
            self.json_schema_validators['jsd_f9ada2e275fa2934fdb4825266a2c_v3_0_0'] =\
                JSONSchemaValidatorF9Ada2E275Fa2934FDb4825266A2C_v3_0_0()
            self.json_schema_validators['jsd_c1fa3bf115c77be99b602aca1493b_v3_0_0'] =\
                JSONSchemaValidatorC1Fa3Bf115C77Be99B602Aca1493B_v3_0_0()
            self.json_schema_validators['jsd_e3ddfddd45e299f14ed194926f8de_v3_0_0'] =\
                JSONSchemaValidatorE3DdfDdd45E299F14Ed194926F8De_v3_0_0()
            self.json_schema_validators['jsd_aa24c1260a568b93c283ecd2c3510e_v3_0_0'] =\
                JSONSchemaValidatorAa24C1260A568B93C283Ecd2C3510E_v3_0_0()
            self.json_schema_validators['jsd_a62af279ca25af0a1837f2cbf10a04d_v3_0_0'] =\
                JSONSchemaValidatorA62Af279Ca25Af0A1837F2Cbf10A04D_v3_0_0()
            self.json_schema_validators['jsd_af2cc85852f52b0aad5a067b2c69286_v3_0_0'] =\
                JSONSchemaValidatorAf2Cc85852F52B0Aad5A067B2C69286_v3_0_0()
            self.json_schema_validators['jsd_cbcecf65a0155fcad602d3ac16531a7_v3_0_0'] =\
                JSONSchemaValidatorCbcecf65A0155FcAd602D3Ac16531A7_v3_0_0()
            self.json_schema_validators['jsd_da7b2773c485400980369a543ddbabf_v3_0_0'] =\
                JSONSchemaValidatorDa7B2773C485400980369A543Ddbabf_v3_0_0()
            self.json_schema_validators['jsd_df4fb303a3e5661ba12058f18b225af_v3_0_0'] =\
                JSONSchemaValidatorDf4Fb303A3E5661Ba12058F18B225Af_v3_0_0()
            self.json_schema_validators['jsd_e43a67028515bf193c102cd077ea764_v3_0_0'] =\
                JSONSchemaValidatorE43A67028515Bf193C102Cd077Ea764_v3_0_0()
            self.json_schema_validators['jsd_e58eabefef15feb880ecfe2906d805f_v3_0_0'] =\
                JSONSchemaValidatorE58EabeFef15Feb880ECfe2906D805F_v3_0_0()
            self.json_schema_validators['jsd_faa7211d68e5b329034e17c82b78694_v3_0_0'] =\
                JSONSchemaValidatorFaa7211D68E5B329034E17C82B78694_v3_0_0()
            self.json_schema_validators['jsd_feb530ce19c5bcf96d57f49cd84bc1f_v3_0_0'] =\
                JSONSchemaValidatorFeb530CE19C5Bcf96D57F49Cd84Bc1F_v3_0_0()
            self.json_schema_validators['jsd_f4508bb3352ff920dbdc229e0fc50_v3_0_0'] =\
                JSONSchemaValidatorF4508Bb3352Ff920DBdc229E0Fc50_v3_0_0()
            self.json_schema_validators['jsd_e68f07767522ba1e49dc474e936d2_v3_0_0'] =\
                JSONSchemaValidatorE68F07767522BA1E49Dc474E936D2_v3_0_0()
            self.json_schema_validators['jsd_b7f7285d71be4645db91b0fc74_v3_0_0'] =\
                JSONSchemaValidatorB7F7285D71Be4645Db91B0Fc74_v3_0_0()
            self.json_schema_validators['jsd_eca5db5147b1e3b35a032ced4b_v3_0_0'] =\
                JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B_v3_0_0()
            self.json_schema_validators['jsd_eddb567508080061e51d5f40c4c_v3_0_0'] =\
                JSONSchemaValidatorEddB567508080061E51D5F40C4C_v3_0_0()
            self.json_schema_validators['jsd_b314d32b258a1b53c5c84cf84d396_v3_0_0'] =\
                JSONSchemaValidatorB314D32B258A1B53C5C84Cf84D396_v3_0_0()
            self.json_schema_validators['jsd_cba3f7ace597da668acfbe00364be_v3_0_0'] =\
                JSONSchemaValidatorCba3F7Ace597DA668Acfbe00364Be_v3_0_0()
            self.json_schema_validators['jsd_bee301e7f5ccfa2e788dcafbf92cc_v3_0_0'] =\
                JSONSchemaValidatorBee301E7F5CcfA2E788Dcafbf92Cc_v3_0_0()
            self.json_schema_validators['jsd_ae615b5e28c54639f44bd10e5b36601_v3_0_0'] =\
                JSONSchemaValidatorAe615B5E28C54639F44Bd10E5B36601_v3_0_0()
            self.json_schema_validators['jsd_c6be021c4ca59e48c97afe218219bb1_v3_0_0'] =\
                JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1_v3_0_0()
            self.json_schema_validators['jsd_cc29554d7925fb1abbfb633e9b00f04_v3_0_0'] =\
                JSONSchemaValidatorCc29554D7925Fb1AbbfB633E9B00F04_v3_0_0()
            self.json_schema_validators['jsd_d0ed84901325292ad4e2a91a174f6b2_v3_0_0'] =\
                JSONSchemaValidatorD0Ed84901325292Ad4E2A91A174F6B2_v3_0_0()
            self.json_schema_validators['jsd_d53842e83f0538cab91e097aa6800ce_v3_0_0'] =\
                JSONSchemaValidatorD53842E83F0538CAb91E097Aa6800Ce_v3_0_0()
            self.json_schema_validators['jsd_dae42fe107a5d4fa53289574a0baa84_v3_0_0'] =\
                JSONSchemaValidatorDae42Fe107A5D4FA53289574A0Baa84_v3_0_0()
            self.json_schema_validators['jsd_f403dda9440503191536993f569cc6f_v3_0_0'] =\
                JSONSchemaValidatorF403Dda9440503191536993F569Cc6F_v3_0_0()
            self.json_schema_validators['jsd_e6734850fabb2097fa969948cb_v3_0_0'] =\
                JSONSchemaValidatorE6734850FaBb2097Fa969948Cb_v3_0_0()
            self.json_schema_validators['jsd_e84541805d1da1fa3d4d581102a9_v3_0_0'] =\
                JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9_v3_0_0()
            self.json_schema_validators['jsd_c137cad852579f4b810ff8adf661_v3_0_0'] =\
                JSONSchemaValidatorC137Cad852579F4B810Ff8Adf661_v3_0_0()
            self.json_schema_validators['jsd_fff985b5159a0aa52bfe9e62ba7_v3_0_0'] =\
                JSONSchemaValidatorFff985B5159A0Aa52Bfe9E62Ba7_v3_0_0()
            self.json_schema_validators['jsd_a57687cef65891a6f48dd17f456c4e_v3_0_0'] =\
                JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E_v3_0_0()
            self.json_schema_validators['jsd_b9eb9547216547cab8b9e686eee674b_v3_0_0'] =\
                JSONSchemaValidatorB9Eb9547216547CAb8B9E686Eee674B_v3_0_0()
            self.json_schema_validators['jsd_c6c2a4908ee5f48b7e9cae7572f6a94_v3_0_0'] =\
                JSONSchemaValidatorC6C2A4908Ee5F48B7E9Cae7572F6A94_v3_0_0()
            self.json_schema_validators['jsd_ea7e01261355dcfae6412e0615ba1f5_v3_0_0'] =\
                JSONSchemaValidatorEa7E01261355DcfAe6412E0615Ba1F5_v3_0_0()
            self.json_schema_validators['jsd_b305804a95e2fb51ab50c039e6c66_v3_0_0'] =\
                JSONSchemaValidatorB305804A95E2FB51AB50C039E6C66_v3_0_0()
            self.json_schema_validators['jsd_bc200af85d598885a990ff9bcbf8_v3_0_0'] =\
                JSONSchemaValidatorBc200Af85D598885A990Ff9Bcbf8_v3_0_0()
            self.json_schema_validators['jsd_b58a72c9ff567896a15555ecc9564f_v3_0_0'] =\
                JSONSchemaValidatorB58A72C9Ff567896A15555Ecc9564F_v3_0_0()
            self.json_schema_validators['jsd_a70be83785373b264d21e84fbfa7d_v3_0_0'] =\
                JSONSchemaValidatorA70Be83785373B264D21E84Fbfa7D_v3_0_0()
            self.json_schema_validators['jsd_e4ce332e5cdc97399fe9f01b163e_v3_0_0'] =\
                JSONSchemaValidatorE4Ce332E5Cdc97399Fe9F01B163E_v3_0_0()
            self.json_schema_validators['jsd_f4bceb4d5500fa2bab08326fd66cb_v3_0_0'] =\
                JSONSchemaValidatorF4BceB4D5500FA2BaB08326Fd66Cb_v3_0_0()
            self.json_schema_validators['jsd_bdae59219027b4d40b94fa3d_v3_0_0'] =\
                JSONSchemaValidatorBdae59219027B4D40B94Fa3D_v3_0_0()
            self.json_schema_validators['jsd_a095b061f564ebba331f66505b0e3_v3_0_0'] =\
                JSONSchemaValidatorA095B061F564EBba331F66505B0E3_v3_0_0()
            self.json_schema_validators['jsd_b22d6ad9f595ab7e3eee5cf44de8a_v3_0_0'] =\
                JSONSchemaValidatorB22D6Ad9F595AB7E3Eee5Cf44De8A_v3_0_0()
            self.json_schema_validators['jsd_a4cccea3c9567498f6f688e0cf86e7_v3_0_0'] =\
                JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7_v3_0_0()
            self.json_schema_validators['jsd_afa6d7527045ebc928ee7e30ad3092a_v3_0_0'] =\
                JSONSchemaValidatorAfa6D7527045Ebc928EE7E30Ad3092A_v3_0_0()
            self.json_schema_validators['jsd_b641825a9555ecba105cabbdf50fc78_v3_0_0'] =\
                JSONSchemaValidatorB641825A9555EcbA105Cabbdf50Fc78_v3_0_0()
            self.json_schema_validators['jsd_c052306febd5865ada5df348e18a889_v3_0_0'] =\
                JSONSchemaValidatorC052306Febd5865Ada5Df348E18A889_v3_0_0()
            self.json_schema_validators['jsd_d904c521059563490c4a93871b33d51_v3_0_0'] =\
                JSONSchemaValidatorD904C521059563490C4A93871B33D51_v3_0_0()
            self.json_schema_validators['jsd_dfe1db8729d541fb3a17d31d47d1881_v3_0_0'] =\
                JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881_v3_0_0()
            self.json_schema_validators['jsd_a0824f9a589c58cd8df522524cb550ad_v3_0_0'] =\
                JSONSchemaValidatorA0824F9A589C58Cd8Df522524Cb550Ad_v3_0_0()
            self.json_schema_validators['jsd_a0fdb67d95475cd39382171dec96d6c1_v3_0_0'] =\
                JSONSchemaValidatorA0Fdb67D95475Cd39382171Dec96D6C1_v3_0_0()
            self.json_schema_validators['jsd_a1e3cde0c3f254b39caaaf7c907ae67e_v3_0_0'] =\
                JSONSchemaValidatorA1E3Cde0C3F254B39CaaAf7C907Ae67E_v3_0_0()
            self.json_schema_validators['jsd_a4ab683ce53052e089626a096abaf451_v3_0_0'] =\
                JSONSchemaValidatorA4Ab683CE53052E089626A096Abaf451_v3_0_0()
            self.json_schema_validators['jsd_a4af71bd9e705f1bb1d236b3c16e5f51_v3_0_0'] =\
                JSONSchemaValidatorA4Af71Bd9E705F1BB1D236B3C16E5F51_v3_0_0()
            self.json_schema_validators['jsd_a50d1bd34d5f593aadf8eb02083c67b0_v3_0_0'] =\
                JSONSchemaValidatorA50D1Bd34D5F593AAdf8Eb02083C67B0_v3_0_0()
            self.json_schema_validators['jsd_a69c7f1ad54e5e9cae1f871e19eed61b_v3_0_0'] =\
                JSONSchemaValidatorA69C7F1AD54E5E9CAe1F871E19Eed61B_v3_0_0()
            self.json_schema_validators['jsd_a78585b436685873813e3804cdec7d2b_v3_0_0'] =\
                JSONSchemaValidatorA78585B436685873813E3804Cdec7D2B_v3_0_0()
            self.json_schema_validators['jsd_ab916b19789c59b79dddbc2d0a3c57fc_v3_0_0'] =\
                JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc_v3_0_0()
            self.json_schema_validators['jsd_ac3aa12d3b5551638c3867aa9584f87b_v3_0_0'] =\
                JSONSchemaValidatorAc3Aa12D3B5551638C3867Aa9584F87B_v3_0_0()
            self.json_schema_validators['jsd_acf0372068885036baee3c4524638f31_v3_0_0'] =\
                JSONSchemaValidatorAcf0372068885036Baee3C4524638F31_v3_0_0()
            self.json_schema_validators['jsd_ae8d7c8f33bb52ceb04880845f2f45ba_v3_0_0'] =\
                JSONSchemaValidatorAe8D7C8F33Bb52CeB04880845F2F45Ba_v3_0_0()
            self.json_schema_validators['jsd_af14464cc6a05f6f87bbe7c174b6d5f6_v3_0_0'] =\
                JSONSchemaValidatorAf14464CC6A05F6F87BbE7C174B6D5F6_v3_0_0()
            self.json_schema_validators['jsd_afe1108b1a59539ebe3de3e5652c9653_v3_0_0'] =\
                JSONSchemaValidatorAfe1108B1A59539EBe3DE3E5652C9653_v3_0_0()
            self.json_schema_validators['jsd_b06719c4a49753408438f661dd2f6f7e_v3_0_0'] =\
                JSONSchemaValidatorB06719C4A49753408438F661Dd2F6F7E_v3_0_0()
            self.json_schema_validators['jsd_b09ea91f72885e05b6aa73e89546f969_v3_0_0'] =\
                JSONSchemaValidatorB09Ea91F72885E05B6Aa73E89546F969_v3_0_0()
            self.json_schema_validators['jsd_b227e1b5bbac556a9f577d3a3ea407af_v3_0_0'] =\
                JSONSchemaValidatorB227E1B5Bbac556A9F577D3A3Ea407Af_v3_0_0()
            self.json_schema_validators['jsd_b3284240745e5b929c51495fe80bc1c4_v3_0_0'] =\
                JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4_v3_0_0()
            self.json_schema_validators['jsd_b3c356cfc48a5da4b13b8ecbae5748b7_v3_0_0'] =\
                JSONSchemaValidatorB3C356CfC48A5Da4B13B8Ecbae5748B7_v3_0_0()
            self.json_schema_validators['jsd_b4ceac9ee830523ca5ddbfdf3e1b44be_v3_0_0'] =\
                JSONSchemaValidatorB4Ceac9EE830523CA5DdBfdf3E1B44Be_v3_0_0()
            self.json_schema_validators['jsd_b8104a50fc565ae9a756d6d0152e0e5b_v3_0_0'] =\
                JSONSchemaValidatorB8104A50Fc565Ae9A756D6D0152E0E5B_v3_0_0()
            self.json_schema_validators['jsd_b8319a8b5d195348a8763acd95ca2967_v3_0_0'] =\
                JSONSchemaValidatorB8319A8B5D195348A8763Acd95Ca2967_v3_0_0()
            self.json_schema_validators['jsd_b839d4dee9b958e48ccef056603e253f_v3_0_0'] =\
                JSONSchemaValidatorB839D4DeE9B958E48CceF056603E253F_v3_0_0()
            self.json_schema_validators['jsd_b95cf8c9aed95518b38be1fa4b514b67_v3_0_0'] =\
                JSONSchemaValidatorB95Cf8C9Aed95518B38BE1Fa4B514B67_v3_0_0()
            self.json_schema_validators['jsd_bacf1abfc35e509183c9a7f055cbbfec_v3_0_0'] =\
                JSONSchemaValidatorBacf1AbfC35E509183C9A7F055Cbbfec_v3_0_0()
            self.json_schema_validators['jsd_bb165bd00a6653ac9da440f23ee62ecc_v3_0_0'] =\
                JSONSchemaValidatorBb165Bd00A6653Ac9Da440F23Ee62Ecc_v3_0_0()
            self.json_schema_validators['jsd_bba3187f0be4563aa8b6ff5931a123e7_v3_0_0'] =\
                JSONSchemaValidatorBba3187F0Be4563AA8B6Ff5931A123E7_v3_0_0()
            self.json_schema_validators['jsd_bcb7ec29968e5d5899df4a90d94ed659_v3_0_0'] =\
                JSONSchemaValidatorBcb7Ec29968E5D5899Df4A90D94Ed659_v3_0_0()
            self.json_schema_validators['jsd_bcdb4d3a659653e498da5ab77440c070_v3_0_0'] =\
                JSONSchemaValidatorBcdb4D3A659653E498Da5Ab77440C070_v3_0_0()
            self.json_schema_validators['jsd_bdea52558473565c9963ec14c65727b8_v3_0_0'] =\
                JSONSchemaValidatorBdea52558473565C9963Ec14C65727B8_v3_0_0()
            self.json_schema_validators['jsd_bf792ec664fa5202beb776556908b0c1_v3_0_0'] =\
                JSONSchemaValidatorBf792Ec664Fa5202Beb776556908B0C1_v3_0_0()
            self.json_schema_validators['jsd_bf95f099207a5b6599e04c47c22789c0_v3_0_0'] =\
                JSONSchemaValidatorBf95F099207A5B6599E04C47C22789C0_v3_0_0()
            self.json_schema_validators['jsd_c0984cde5e925c209ab87472ab905476_v3_0_0'] =\
                JSONSchemaValidatorC0984Cde5E925C209Ab87472Ab905476_v3_0_0()
            self.json_schema_validators['jsd_c37778a2faa5552894cc60cec13c56c7_v3_0_0'] =\
                JSONSchemaValidatorC37778A2Faa5552894Cc60Cec13C56C7_v3_0_0()
            self.json_schema_validators['jsd_c37d788b1f9251ddb1742ed73f42abc3_v3_0_0'] =\
                JSONSchemaValidatorC37D788B1F9251DdB1742Ed73F42Abc3_v3_0_0()
            self.json_schema_validators['jsd_c578ef80918b5d038024d126cd6e3b8d_v3_0_0'] =\
                JSONSchemaValidatorC578Ef80918B5D038024D126Cd6E3B8D_v3_0_0()
            self.json_schema_validators['jsd_c5e52706e7095a81b8d32f3024e01cf6_v3_0_0'] =\
                JSONSchemaValidatorC5E52706E7095A81B8D32F3024E01Cf6_v3_0_0()
            self.json_schema_validators['jsd_c638f98ea11b5c3882966cb0d1758a64_v3_0_0'] =\
                JSONSchemaValidatorC638F98EA11B5C3882966Cb0D1758A64_v3_0_0()
            self.json_schema_validators['jsd_c654a18faf1b5571ac5ba61145d298c4_v3_0_0'] =\
                JSONSchemaValidatorC654A18FAf1B5571Ac5BA61145D298C4_v3_0_0()
            self.json_schema_validators['jsd_c67c56a249ce5721863328be9da81573_v3_0_0'] =\
                JSONSchemaValidatorC67C56A249Ce5721863328Be9Da81573_v3_0_0()
            self.json_schema_validators['jsd_c6c330dace185a548f70f4e5d67776ea_v3_0_0'] =\
                JSONSchemaValidatorC6C330DaCe185A548F70F4E5D67776Ea_v3_0_0()
            self.json_schema_validators['jsd_c7aa2a6cac155a6cb7ace3fd76a81e0f_v3_0_0'] =\
                JSONSchemaValidatorC7Aa2A6CAc155A6CB7AcE3Fd76A81E0F_v3_0_0()
            self.json_schema_validators['jsd_c8acebd86a8151aeb2c17d973696fdfa_v3_0_0'] =\
                JSONSchemaValidatorC8Acebd86A8151AeB2C17D973696Fdfa_v3_0_0()
            self.json_schema_validators['jsd_c8cd2f618b655d988ce626e579486596_v3_0_0'] =\
                JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596_v3_0_0()
            self.json_schema_validators['jsd_c8dbec9679d453f78cb47d894c507a7b_v3_0_0'] =\
                JSONSchemaValidatorC8Dbec9679D453F78Cb47D894C507A7B_v3_0_0()
            self.json_schema_validators['jsd_c97e7851003e5a63a2a8005ac8807dc7_v3_0_0'] =\
                JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7_v3_0_0()
            self.json_schema_validators['jsd_c9a67d3e9015580f93a52627f19e9916_v3_0_0'] =\
                JSONSchemaValidatorC9A67D3E9015580F93A52627F19E9916_v3_0_0()
            self.json_schema_validators['jsd_ca28129793d1569bb50de9f43b0d0ee8_v3_0_0'] =\
                JSONSchemaValidatorCa28129793D1569BB50DE9F43B0D0Ee8_v3_0_0()
            self.json_schema_validators['jsd_ca3df31c13b857e6b5dbc8357a8ab010_v3_0_0'] =\
                JSONSchemaValidatorCa3Df31C13B857E6B5DbC8357A8Ab010_v3_0_0()
            self.json_schema_validators['jsd_cc6dfd258c49529db4c580411afe868b_v3_0_0'] =\
                JSONSchemaValidatorCc6Dfd258C49529DB4C580411Afe868B_v3_0_0()
            self.json_schema_validators['jsd_cc909c2717cf55f1863a04a785166fe0_v3_0_0'] =\
                JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0_v3_0_0()
            self.json_schema_validators['jsd_cd04558011d055b1ac3386e24728083d_v3_0_0'] =\
                JSONSchemaValidatorCd04558011D055B1Ac3386E24728083D_v3_0_0()
            self.json_schema_validators['jsd_cd429bb8ff3556a796570480f742028b_v3_0_0'] =\
                JSONSchemaValidatorCd429Bb8Ff3556A796570480F742028B_v3_0_0()
            self.json_schema_validators['jsd_cd6793a4a8e7576c8b290bdc88001f6f_v3_0_0'] =\
                JSONSchemaValidatorCd6793A4A8E7576C8B290Bdc88001F6F_v3_0_0()
            self.json_schema_validators['jsd_ce3085eebdd15be7ac56b5970265d8df_v3_0_0'] =\
                JSONSchemaValidatorCe3085EeBdd15Be7Ac56B5970265D8Df_v3_0_0()
            self.json_schema_validators['jsd_d0e432f52e2a5863858c7dc0c3eda277_v3_0_0'] =\
                JSONSchemaValidatorD0E432F52E2A5863858C7Dc0C3Eda277_v3_0_0()
            self.json_schema_validators['jsd_d388e26255a15233ac682c0406880cfb_v3_0_0'] =\
                JSONSchemaValidatorD388E26255A15233Ac682C0406880Cfb_v3_0_0()
            self.json_schema_validators['jsd_d43fec9e7dc556cbb9bf0ebd1dcd6aad_v3_0_0'] =\
                JSONSchemaValidatorD43Fec9E7Dc556CbB9Bf0Ebd1Dcd6Aad_v3_0_0()
            self.json_schema_validators['jsd_d5572c56526151cb8ea42de44b2db52c_v3_0_0'] =\
                JSONSchemaValidatorD5572C56526151Cb8Ea42De44B2Db52C_v3_0_0()
            self.json_schema_validators['jsd_d5e00a8e6aa0577ea81e11e796912053_v3_0_0'] =\
                JSONSchemaValidatorD5E00A8E6Aa0577EA81E11E796912053_v3_0_0()
            self.json_schema_validators['jsd_d810359e31e453ac8145981b7d5bb7e4_v3_0_0'] =\
                JSONSchemaValidatorD810359E31E453Ac8145981B7D5Bb7E4_v3_0_0()
            self.json_schema_validators['jsd_d82fe0f9e4635b74af809beaaf98bd07_v3_0_0'] =\
                JSONSchemaValidatorD82Fe0F9E4635B74Af809Beaaf98Bd07_v3_0_0()
            self.json_schema_validators['jsd_d912b1c21e2b5dca8b56332d3a8ad13d_v3_0_0'] =\
                JSONSchemaValidatorD912B1C21E2B5Dca8B56332D3A8Ad13D_v3_0_0()
            self.json_schema_validators['jsd_da4bb24b7e4d594cb026335a75248e1a_v3_0_0'] =\
                JSONSchemaValidatorDa4Bb24B7E4D594CB026335A75248E1A_v3_0_0()
            self.json_schema_validators['jsd_db686413cf4558188ea60ccc05c3e920_v3_0_0'] =\
                JSONSchemaValidatorDb686413Cf4558188Ea60Ccc05C3E920_v3_0_0()
            self.json_schema_validators['jsd_ded7f8573c255c318bb1f04bfdbf01e1_v3_0_0'] =\
                JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1_v3_0_0()
            self.json_schema_validators['jsd_dfa8f48210e85715beebb44e62fac408_v3_0_0'] =\
                JSONSchemaValidatorDfa8F48210E85715BeebB44E62Fac408_v3_0_0()
            self.json_schema_validators['jsd_dfae2409eecc551298e9fa31d14f43d0_v3_0_0'] =\
                JSONSchemaValidatorDfae2409Eecc551298E9Fa31D14F43D0_v3_0_0()
            self.json_schema_validators['jsd_e1d938f110e059a5abcb9cc8fb3cbd7c_v3_0_0'] =\
                JSONSchemaValidatorE1D938F110E059A5Abcb9Cc8Fb3Cbd7C_v3_0_0()
            self.json_schema_validators['jsd_e313d50be9155acca1082ef11895aeb8_v3_0_0'] =\
                JSONSchemaValidatorE313D50BE9155AccA1082Ef11895Aeb8_v3_0_0()
            self.json_schema_validators['jsd_e39868ea7aec5efcaaf55009699eda5d_v3_0_0'] =\
                JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D_v3_0_0()
            self.json_schema_validators['jsd_e623dba049b5569c83e13ccf4360e369_v3_0_0'] =\
                JSONSchemaValidatorE623Dba049B5569C83E13Ccf4360E369_v3_0_0()
            self.json_schema_validators['jsd_e75d766151e85011870229f30e4f5ec3_v3_0_0'] =\
                JSONSchemaValidatorE75D766151E85011870229F30E4F5Ec3_v3_0_0()
            self.json_schema_validators['jsd_e7bd468ee94f53869e52e84454efd0e6_v3_0_0'] =\
                JSONSchemaValidatorE7Bd468EE94F53869E52E84454Efd0E6_v3_0_0()
            self.json_schema_validators['jsd_e82e46732de25832a543c4640312588c_v3_0_0'] =\
                JSONSchemaValidatorE82E46732De25832A543C4640312588C_v3_0_0()
            self.json_schema_validators['jsd_e9ce4a1e1cf955f098343646760e9d58_v3_0_0'] =\
                JSONSchemaValidatorE9Ce4A1E1Cf955F098343646760E9D58_v3_0_0()
            self.json_schema_validators['jsd_ea658190e73c5ce1b27e7def4aea28e3_v3_0_0'] =\
                JSONSchemaValidatorEa658190E73C5Ce1B27E7Def4Aea28E3_v3_0_0()
            self.json_schema_validators['jsd_eaa0d7c339d152b688876c2e10f51fe7_v3_0_0'] =\
                JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7_v3_0_0()
            self.json_schema_validators['jsd_eb8e0ce63376573995a49178435f7747_v3_0_0'] =\
                JSONSchemaValidatorEb8E0Ce63376573995A49178435F7747_v3_0_0()
            self.json_schema_validators['jsd_eba5dd37c1f5532992a96c2db7ecff5d_v3_0_0'] =\
                JSONSchemaValidatorEba5Dd37C1F5532992A96C2Db7Ecff5D_v3_0_0()
            self.json_schema_validators['jsd_ec26ec11d92356a594a6efa55ccb9be7_v3_0_0'] =\
                JSONSchemaValidatorEc26Ec11D92356A594A6Efa55Ccb9Be7_v3_0_0()
            self.json_schema_validators['jsd_ecff2eb67fe5591f8d9026f928a0d8aa_v3_0_0'] =\
                JSONSchemaValidatorEcff2Eb67Fe5591F8D9026F928A0D8Aa_v3_0_0()
            self.json_schema_validators['jsd_ed1ef503c091506aa8e446182e625365_v3_0_0'] =\
                JSONSchemaValidatorEd1Ef503C091506AA8E446182E625365_v3_0_0()
            self.json_schema_validators['jsd_ed8575d86539534082d6e83ced01c40b_v3_0_0'] =\
                JSONSchemaValidatorEd8575D86539534082D6E83Ced01C40B_v3_0_0()
            self.json_schema_validators['jsd_eea0f876f20c59ed8eff33f1f4fe10a8_v3_0_0'] =\
                JSONSchemaValidatorEea0F876F20C59Ed8Eff33F1F4Fe10A8_v3_0_0()
            self.json_schema_validators['jsd_f1196f1f6fde5978b0522f096926d443_v3_0_0'] =\
                JSONSchemaValidatorF1196F1F6Fde5978B0522F096926D443_v3_0_0()
            self.json_schema_validators['jsd_f130b53af83c5b7baa2acd190b57fd75_v3_0_0'] =\
                JSONSchemaValidatorF130B53AF83C5B7BAa2ACd190B57Fd75_v3_0_0()
            self.json_schema_validators['jsd_f1b8eaf23e795f1a8525eb5905187aa9_v3_0_0'] =\
                JSONSchemaValidatorF1B8Eaf23E795F1A8525Eb5905187Aa9_v3_0_0()
            self.json_schema_validators['jsd_f1ff2b82953f5131884f0779db37190c_v3_0_0'] =\
                JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C_v3_0_0()
            self.json_schema_validators['jsd_f3b45b8e4089574c9912407f88b1a5d2_v3_0_0'] =\
                JSONSchemaValidatorF3B45B8E4089574C9912407F88B1A5D2_v3_0_0()
            self.json_schema_validators['jsd_f41d844dbee15f7680920652004f69b6_v3_0_0'] =\
                JSONSchemaValidatorF41D844DBee15F7680920652004F69B6_v3_0_0()
            self.json_schema_validators['jsd_f41f77362663580d8cc3e6e88623889d_v3_0_0'] =\
                JSONSchemaValidatorF41F77362663580D8Cc3E6E88623889D_v3_0_0()
            self.json_schema_validators['jsd_f4dbfb874b3b56d7a651d6732f1bd55e_v3_0_0'] =\
                JSONSchemaValidatorF4Dbfb874B3B56D7A651D6732F1Bd55E_v3_0_0()
            self.json_schema_validators['jsd_f5175ff711535ff2b1b85a3a4525e886_v3_0_0'] =\
                JSONSchemaValidatorF5175Ff711535Ff2B1B85A3A4525E886_v3_0_0()
            self.json_schema_validators['jsd_f68aee0cdb425390b3ca90b0b46e6e2c_v3_0_0'] =\
                JSONSchemaValidatorF68Aee0CDb425390B3Ca90B0B46E6E2C_v3_0_0()
            self.json_schema_validators['jsd_f79ab23563d857e58e01a74e37333572_v3_0_0'] =\
                JSONSchemaValidatorF79Ab23563D857E58E01A74E37333572_v3_0_0()
            self.json_schema_validators['jsd_f831d9ed2beb5c2b967aa10db8c22046_v3_0_0'] =\
                JSONSchemaValidatorF831D9Ed2Beb5C2B967AA10Db8C22046_v3_0_0()
            self.json_schema_validators['jsd_f8a2f0834e625822bed1cb4cf34fde5e_v3_0_0'] =\
                JSONSchemaValidatorF8A2F0834E625822Bed1Cb4Cf34Fde5E_v3_0_0()
            self.json_schema_validators['jsd_f9c9a5e917af53dbbb91733e82e72ebe_v3_0_0'] =\
                JSONSchemaValidatorF9C9A5E917Af53DbBb91733E82E72Ebe_v3_0_0()
            self.json_schema_validators['jsd_fa838e78175e51b4bcfb0821c19b81b7_v3_0_0'] =\
                JSONSchemaValidatorFa838E78175E51B4Bcfb0821C19B81B7_v3_0_0()
            self.json_schema_validators['jsd_fc9a4ee495785518bd2251b6b4fb41f4_v3_0_0'] =\
                JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4_v3_0_0()
            self.json_schema_validators['jsd_fc9ecf1e469154ae845236dbed070904_v3_0_0'] =\
                JSONSchemaValidatorFc9Ecf1E469154Ae845236Dbed070904_v3_0_0()
            self.json_schema_validators['jsd_fda64cd1ab7d53448962f61de0f76948_v3_0_0'] =\
                JSONSchemaValidatorFda64Cd1Ab7D53448962F61De0F76948_v3_0_0()
            self.json_schema_validators['jsd_fe54c96ccba65af1abe3cd08f4fc69cb_v3_0_0'] =\
                JSONSchemaValidatorFe54C96CCba65Af1Abe3Cd08F4Fc69Cb_v3_0_0()
            self.json_schema_validators['jsd_feb30ca768795eed82c118d009d7bcd4_v3_0_0'] =\
                JSONSchemaValidatorFeb30Ca768795Eed82C118D009D7Bcd4_v3_0_0()
            self.json_schema_validators['jsd_ffff1c792bf559ebb39b789421be6966_v3_0_0'] =\
                JSONSchemaValidatorFfff1C792Bf559EbB39B789421Be6966_v3_0_0()

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
