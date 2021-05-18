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
from .validators.v3_0_0.jsd_ab7717877a539b9b87f499817aee15 \
    import JSONSchemaValidatorAb7717877A539B9B87F499817Aee15 \
    as JSONSchemaValidatorAb7717877A539B9B87F499817Aee15_v3_0_0
from .validators.v3_0_0.jsd_db1d9dda53369e35d33138b29c16 \
    import JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16 \
    as JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16_v3_0_0
from .validators.v3_0_0.jsd_ab015a9eb6d5f2b91002af068cb4ce2 \
    import JSONSchemaValidatorAb015A9Eb6D5F2B91002Af068Cb4Ce2 \
    as JSONSchemaValidatorAb015A9Eb6D5F2B91002Af068Cb4Ce2_v3_0_0
from .validators.v3_0_0.jsd_ac243ecb8c157658a4bcfe77a102c14 \
    import JSONSchemaValidatorAc243EcB8C157658A4BCfe77A102C14 \
    as JSONSchemaValidatorAc243EcB8C157658A4BCfe77A102C14_v3_0_0
from .validators.v3_0_0.jsd_b3fe0f3ea8a5368aea79a847288993e \
    import JSONSchemaValidatorB3Fe0F3Ea8A5368Aea79A847288993E \
    as JSONSchemaValidatorB3Fe0F3Ea8A5368Aea79A847288993E_v3_0_0
from .validators.v3_0_0.jsd_cdc971b23285b87945021bd5983d1cd \
    import JSONSchemaValidatorCdc971B23285B87945021Bd5983D1Cd \
    as JSONSchemaValidatorCdc971B23285B87945021Bd5983D1Cd_v3_0_0
from .validators.v3_0_0.jsd_d1df0e230765104863b8d63d5beb68e \
    import JSONSchemaValidatorD1Df0E230765104863B8D63D5Beb68E \
    as JSONSchemaValidatorD1Df0E230765104863B8D63D5Beb68E_v3_0_0
from .validators.v3_0_0.jsd_dedf09f59e754c6ae5212d43b1c8fb2 \
    import JSONSchemaValidatorDedf09F59E754C6Ae5212D43B1C8Fb2 \
    as JSONSchemaValidatorDedf09F59E754C6Ae5212D43B1C8Fb2_v3_0_0
from .validators.v3_0_0.jsd_f41a1e47105581fabf212f259626903 \
    import JSONSchemaValidatorF41A1E47105581FAbf212F259626903 \
    as JSONSchemaValidatorF41A1E47105581FAbf212F259626903_v3_0_0
from .validators.v3_0_0.jsd_e34177d675622acd0a532f5b7c41b \
    import JSONSchemaValidatorE34177D675622Acd0A532F5B7C41B \
    as JSONSchemaValidatorE34177D675622Acd0A532F5B7C41B_v3_0_0
from .validators.v3_0_0.jsd_f8f4956d29b821fa9bbf23266 \
    import JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266 \
    as JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266_v3_0_0
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
from .validators.v3_0_0.jsd_ea10f18c3655db84657ad855bf6972 \
    import JSONSchemaValidatorEa10F18C3655Db84657Ad855Bf6972 \
    as JSONSchemaValidatorEa10F18C3655Db84657Ad855Bf6972_v3_0_0
from .validators.v3_0_0.jsd_b9e8541f25c4ea29944f659f68994 \
    import JSONSchemaValidatorB9E8541F25C4EA29944F659F68994 \
    as JSONSchemaValidatorB9E8541F25C4EA29944F659F68994_v3_0_0
from .validators.v3_0_0.jsd_c8aec23a55399a175acf105dbe1c2 \
    import JSONSchemaValidatorC8Aec23A55399A175Acf105Dbe1C2 \
    as JSONSchemaValidatorC8Aec23A55399A175Acf105Dbe1C2_v3_0_0
from .validators.v3_0_0.jsd_cfcc7615d0492e2dd1b04dd03a9 \
    import JSONSchemaValidatorCfcC7615D0492E2Dd1B04Dd03A9 \
    as JSONSchemaValidatorCfcC7615D0492E2Dd1B04Dd03A9_v3_0_0
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
from .validators.v3_0_0.jsd_c7d6bb4abf53f6aa2f40b6986f58a9 \
    import JSONSchemaValidatorC7D6Bb4Abf53F6Aa2F40B6986F58A9 \
    as JSONSchemaValidatorC7D6Bb4Abf53F6Aa2F40B6986F58A9_v3_0_0
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
from .validators.v3_0_0.jsd_f78898b7d655b2b81085dc7c0a964e \
    import JSONSchemaValidatorF78898B7D655B2B81085Dc7C0A964E \
    as JSONSchemaValidatorF78898B7D655B2B81085Dc7C0A964E_v3_0_0
from .validators.v3_0_0.jsd_a599ae00f5e47b9ece23cd3183d1c \
    import JSONSchemaValidatorA599AE00F5E47B9EcE23Cd3183D1C \
    as JSONSchemaValidatorA599AE00F5E47B9EcE23Cd3183D1C_v3_0_0
from .validators.v3_0_0.jsd_c288192f954309b4b35aa612ff226 \
    import JSONSchemaValidatorC288192F954309B4B35Aa612Ff226 \
    as JSONSchemaValidatorC288192F954309B4B35Aa612Ff226_v3_0_0
from .validators.v3_0_0.jsd_f64c3c08518e9eef83a92d69cde3 \
    import JSONSchemaValidatorF64C3C08518E9Eef83A92D69Cde3 \
    as JSONSchemaValidatorF64C3C08518E9Eef83A92D69Cde3_v3_0_0
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
from .validators.v3_0_0.jsd_c0ec3a56f65447ba863ae0cac5ef6a \
    import JSONSchemaValidatorC0Ec3A56F65447Ba863Ae0Cac5Ef6A \
    as JSONSchemaValidatorC0Ec3A56F65447Ba863Ae0Cac5Ef6A_v3_0_0
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
from .validators.v3_0_0.jsd_a9f1f24542dbd244e31691a2e09 \
    import JSONSchemaValidatorA9F1F24542DBd244E31691A2E09 \
    as JSONSchemaValidatorA9F1F24542DBd244E31691A2E09_v3_0_0
from .validators.v3_0_0.jsd_e9cc593c395c48b31b30149467c846 \
    import JSONSchemaValidatorE9Cc593C395C48B31B30149467C846 \
    as JSONSchemaValidatorE9Cc593C395C48B31B30149467C846_v3_0_0
from .validators.v3_0_0.jsd_f8ba0e97135ca6bacff94d5a76df97 \
    import JSONSchemaValidatorF8Ba0E97135Ca6BacfF94D5A76Df97 \
    as JSONSchemaValidatorF8Ba0E97135Ca6BacfF94D5A76Df97_v3_0_0
from .validators.v3_0_0.jsd_dc2eec65ad680a3c5de47cd87c8 \
    import JSONSchemaValidatorDc2Eec65Ad680A3C5De47Cd87C8 \
    as JSONSchemaValidatorDc2Eec65Ad680A3C5De47Cd87C8_v3_0_0
from .validators.v3_0_0.jsd_b8696d875b12b0a3ab735b397d7a \
    import JSONSchemaValidatorB8696D875B12B0A3Ab735B397D7A \
    as JSONSchemaValidatorB8696D875B12B0A3Ab735B397D7A_v3_0_0
from .validators.v3_0_0.jsd_c5c9b7ab72b5442ae7026a5dcc0fec3 \
    import JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3 \
    as JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3_v3_0_0
from .validators.v3_0_0.jsd_ccba98a61555ae495f6a05284e3b5ae \
    import JSONSchemaValidatorCcba98A61555Ae495F6A05284E3B5Ae \
    as JSONSchemaValidatorCcba98A61555Ae495F6A05284E3B5Ae_v3_0_0
from .validators.v3_0_0.jsd_e155669bc74586e9ef2580ec5752902 \
    import JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902 \
    as JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902_v3_0_0
from .validators.v3_0_0.jsd_f36e90115b05416a71506061fed7e5c \
    import JSONSchemaValidatorF36E90115B05416A71506061Fed7E5C \
    as JSONSchemaValidatorF36E90115B05416A71506061Fed7E5C_v3_0_0
from .validators.v3_0_0.jsd_fd9e7e03a6056d1b6e9705e3096d946 \
    import JSONSchemaValidatorFd9E7E03A6056D1B6E9705E3096D946 \
    as JSONSchemaValidatorFd9E7E03A6056D1B6E9705E3096D946_v3_0_0
from .validators.v3_0_0.jsd_c4fada6c558d9aba09cc373d5b266 \
    import JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266 \
    as JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0
from .validators.v3_0_0.jsd_b11e2f1af656bcb5880a7b33720ec5 \
    import JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5 \
    as JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0
from .validators.v3_0_0.jsd_c9722c56108cac8ca50bf8f01c \
    import JSONSchemaValidatorC9722C56108Cac8Ca50Bf8F01C \
    as JSONSchemaValidatorC9722C56108Cac8Ca50Bf8F01C_v3_0_0
from .validators.v3_0_0.jsd_b1da14ba95aa48b498c76d0bc1017 \
    import JSONSchemaValidatorB1Da14Ba95Aa48B498C76D0Bc1017 \
    as JSONSchemaValidatorB1Da14Ba95Aa48B498C76D0Bc1017_v3_0_0
from .validators.v3_0_0.jsd_cb9345e58f5433ae80f5d8f855978b \
    import JSONSchemaValidatorCb9345E58F5433Ae80F5D8F855978B \
    as JSONSchemaValidatorCb9345E58F5433Ae80F5D8F855978B_v3_0_0
from .validators.v3_0_0.jsd_e603092f597ab6c25381e59c4a70 \
    import JSONSchemaValidatorE603092F597AB6C25381E59C4A70 \
    as JSONSchemaValidatorE603092F597AB6C25381E59C4A70_v3_0_0
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
from .validators.v3_0_0.jsd_cf65cd559628b26f6eb5ea20f14 \
    import JSONSchemaValidatorCf65Cd559628B26F6Eb5Ea20F14 \
    as JSONSchemaValidatorCf65Cd559628B26F6Eb5Ea20F14_v3_0_0
from .validators.v3_0_0.jsd_acb5a41fe395b158a3fe1cda996b0cf \
    import JSONSchemaValidatorAcb5A41Fe395B158A3FE1Cda996B0Cf \
    as JSONSchemaValidatorAcb5A41Fe395B158A3FE1Cda996B0Cf_v3_0_0
from .validators.v3_0_0.jsd_e6c7251a8508597f1b7ae61cbf953 \
    import JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953 \
    as JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953_v3_0_0
from .validators.v3_0_0.jsd_dc966c73c65649a244d507bd53fd19 \
    import JSONSchemaValidatorDc966C73C65649A244D507Bd53Fd19 \
    as JSONSchemaValidatorDc966C73C65649A244D507Bd53Fd19_v3_0_0
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
from .validators.v3_0_0.jsd_feb825519f98bd1541ef3c367d \
    import JSONSchemaValidatorFeB825519F98Bd1541Ef3C367D \
    as JSONSchemaValidatorFeB825519F98Bd1541Ef3C367D_v3_0_0
from .validators.v3_0_0.jsd_d1132a216d54d091022aec0ad018f8 \
    import JSONSchemaValidatorD1132A216D54D091022Aec0Ad018F8 \
    as JSONSchemaValidatorD1132A216D54D091022Aec0Ad018F8_v3_0_0
from .validators.v3_0_0.jsd_a588d29d5a527388ee8498f746d1f5 \
    import JSONSchemaValidatorA588D29D5A527388Ee8498F746D1F5 \
    as JSONSchemaValidatorA588D29D5A527388Ee8498F746D1F5_v3_0_0
from .validators.v3_0_0.jsd_ad69fa1d850f4993bbfc888749fa0 \
    import JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0 \
    as JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0
from .validators.v3_0_0.jsd_f564c3eda5c20bb807b8c062c8e7b \
    import JSONSchemaValidatorF564C3Eda5C20Bb807B8C062C8E7B \
    as JSONSchemaValidatorF564C3Eda5C20Bb807B8C062C8E7B_v3_0_0
from .validators.v3_0_0.jsd_abc25887a5daab1216195e08cbd49 \
    import JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49 \
    as JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49_v3_0_0
from .validators.v3_0_0.jsd_d1e1fc98a5588b8bbdda06c4fc012 \
    import JSONSchemaValidatorD1E1FC98A5588B8BbDda06C4Fc012 \
    as JSONSchemaValidatorD1E1FC98A5588B8BbDda06C4Fc012_v3_0_0
from .validators.v3_0_0.jsd_ad233598ed75e0c97ddd3c3f1af50e4 \
    import JSONSchemaValidatorAd233598Ed75E0C97DdD3C3F1Af50E4 \
    as JSONSchemaValidatorAd233598Ed75E0C97DdD3C3F1Af50E4_v3_0_0
from .validators.v3_0_0.jsd_c475afd2a5e57e4bd0952f2c5349c6c \
    import JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C \
    as JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C_v3_0_0
from .validators.v3_0_0.jsd_ce70db7732c596aa82bd7d1725ac02d \
    import JSONSchemaValidatorCe70Db7732C596AA82BD7D1725Ac02D \
    as JSONSchemaValidatorCe70Db7732C596AA82BD7D1725Ac02D_v3_0_0
from .validators.v3_0_0.jsd_dec8e9d819b5bc088e351b69efd0369 \
    import JSONSchemaValidatorDec8E9D819B5Bc088E351B69Efd0369 \
    as JSONSchemaValidatorDec8E9D819B5Bc088E351B69Efd0369_v3_0_0
from .validators.v3_0_0.jsd_e4bfa620f76545d9887045cd24d99a2 \
    import JSONSchemaValidatorE4Bfa620F76545D9887045Cd24D99A2 \
    as JSONSchemaValidatorE4Bfa620F76545D9887045Cd24D99A2_v3_0_0
from .validators.v3_0_0.jsd_fb4ef0633057a1acdc47e23b120073 \
    import JSONSchemaValidatorFb4Ef0633057A1Acdc47E23B120073 \
    as JSONSchemaValidatorFb4Ef0633057A1Acdc47E23B120073_v3_0_0
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
from .validators.v3_0_0.jsd_cbcecf65a0155fcad602d3ac16531a7 \
    import JSONSchemaValidatorCbcecf65A0155FcAd602D3Ac16531A7 \
    as JSONSchemaValidatorCbcecf65A0155FcAd602D3Ac16531A7_v3_0_0
from .validators.v3_0_0.jsd_df4fb303a3e5661ba12058f18b225af \
    import JSONSchemaValidatorDf4Fb303A3E5661Ba12058F18B225Af \
    as JSONSchemaValidatorDf4Fb303A3E5661Ba12058F18B225Af_v3_0_0
from .validators.v3_0_0.jsd_e58eabefef15feb880ecfe2906d805f \
    import JSONSchemaValidatorE58EabeFef15Feb880ECfe2906D805F \
    as JSONSchemaValidatorE58EabeFef15Feb880ECfe2906D805F_v3_0_0
from .validators.v3_0_0.jsd_ee1780a38a85d1ba57c9a38e1093721 \
    import JSONSchemaValidatorEe1780A38A85D1BA57C9A38E1093721 \
    as JSONSchemaValidatorEe1780A38A85D1BA57C9A38E1093721_v3_0_0
from .validators.v3_0_0.jsd_faa7211d68e5b329034e17c82b78694 \
    import JSONSchemaValidatorFaa7211D68E5B329034E17C82B78694 \
    as JSONSchemaValidatorFaa7211D68E5B329034E17C82B78694_v3_0_0
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
from .validators.v3_0_0.jsd_d9f17adde53e2a08a650b9fe1714c \
    import JSONSchemaValidatorD9F17Adde53E2A08A650B9Fe1714C \
    as JSONSchemaValidatorD9F17Adde53E2A08A650B9Fe1714C_v3_0_0
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
from .validators.v3_0_0.jsd_c0b4d1bbda75355912f208521362a41 \
    import JSONSchemaValidatorC0B4D1BBda75355912F208521362A41 \
    as JSONSchemaValidatorC0B4D1BBda75355912F208521362A41_v3_0_0
from .validators.v3_0_0.jsd_c6be021c4ca59e48c97afe218219bb1 \
    import JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1 \
    as JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1_v3_0_0
from .validators.v3_0_0.jsd_d0ed84901325292ad4e2a91a174f6b2 \
    import JSONSchemaValidatorD0Ed84901325292Ad4E2A91A174F6B2 \
    as JSONSchemaValidatorD0Ed84901325292Ad4E2A91A174F6B2_v3_0_0
from .validators.v3_0_0.jsd_d53842e83f0538cab91e097aa6800ce \
    import JSONSchemaValidatorD53842E83F0538CAb91E097Aa6800Ce \
    as JSONSchemaValidatorD53842E83F0538CAb91E097Aa6800Ce_v3_0_0
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
from .validators.v3_0_0.jsd_fd707ac0454be8fecc73a918a27b6 \
    import JSONSchemaValidatorFd707Ac0454Be8FecC73A918A27B6 \
    as JSONSchemaValidatorFd707Ac0454Be8FecC73A918A27B6_v3_0_0
from .validators.v3_0_0.jsd_fff985b5159a0aa52bfe9e62ba7 \
    import JSONSchemaValidatorFff985B5159A0Aa52Bfe9E62Ba7 \
    as JSONSchemaValidatorFff985B5159A0Aa52Bfe9E62Ba7_v3_0_0
from .validators.v3_0_0.jsd_a57687cef65891a6f48dd17f456c4e \
    import JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E \
    as JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E_v3_0_0
from .validators.v3_0_0.jsd_af104d12b5c5e668af1504feca5c9b1 \
    import JSONSchemaValidatorAf104D12B5C5E668Af1504Feca5C9B1 \
    as JSONSchemaValidatorAf104D12B5C5E668Af1504Feca5C9B1_v3_0_0
from .validators.v3_0_0.jsd_b9eb9547216547cab8b9e686eee674b \
    import JSONSchemaValidatorB9Eb9547216547CAb8B9E686Eee674B \
    as JSONSchemaValidatorB9Eb9547216547CAb8B9E686Eee674B_v3_0_0
from .validators.v3_0_0.jsd_c6c2a4908ee5f48b7e9cae7572f6a94 \
    import JSONSchemaValidatorC6C2A4908Ee5F48B7E9Cae7572F6A94 \
    as JSONSchemaValidatorC6C2A4908Ee5F48B7E9Cae7572F6A94_v3_0_0
from .validators.v3_0_0.jsd_ea7e01261355dcfae6412e0615ba1f5 \
    import JSONSchemaValidatorEa7E01261355DcfAe6412E0615Ba1F5 \
    as JSONSchemaValidatorEa7E01261355DcfAe6412E0615Ba1F5_v3_0_0
from .validators.v3_0_0.jsd_bc200af85d598885a990ff9bcbf8 \
    import JSONSchemaValidatorBc200Af85D598885A990Ff9Bcbf8 \
    as JSONSchemaValidatorBc200Af85D598885A990Ff9Bcbf8_v3_0_0
from .validators.v3_0_0.jsd_e92c6e47625711b9ce06f92bd4d219 \
    import JSONSchemaValidatorE92C6E47625711B9Ce06F92Bd4D219 \
    as JSONSchemaValidatorE92C6E47625711B9Ce06F92Bd4D219_v3_0_0
from .validators.v3_0_0.jsd_bdae59219027b4d40b94fa3d \
    import JSONSchemaValidatorBdae59219027B4D40B94Fa3D \
    as JSONSchemaValidatorBdae59219027B4D40B94Fa3D_v3_0_0
from .validators.v3_0_0.jsd_a160f293375ae9924d8240c4efdc6a \
    import JSONSchemaValidatorA160F293375Ae9924D8240C4Efdc6A \
    as JSONSchemaValidatorA160F293375Ae9924D8240C4Efdc6A_v3_0_0
from .validators.v3_0_0.jsd_a095b061f564ebba331f66505b0e3 \
    import JSONSchemaValidatorA095B061F564EBba331F66505B0E3 \
    as JSONSchemaValidatorA095B061F564EBba331F66505B0E3_v3_0_0
from .validators.v3_0_0.jsd_b22d6ad9f595ab7e3eee5cf44de8a \
    import JSONSchemaValidatorB22D6Ad9F595AB7E3Eee5Cf44De8A \
    as JSONSchemaValidatorB22D6Ad9F595AB7E3Eee5Cf44De8A_v3_0_0
from .validators.v3_0_0.jsd_a4cccea3c9567498f6f688e0cf86e7 \
    import JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7 \
    as JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7_v3_0_0
from .validators.v3_0_0.jsd_d87a24994c514d955149d33e1a99fb \
    import JSONSchemaValidatorD87A24994C514D955149D33E1A99Fb \
    as JSONSchemaValidatorD87A24994C514D955149D33E1A99Fb_v3_0_0
from .validators.v3_0_0.jsd_afa6d7527045ebc928ee7e30ad3092a \
    import JSONSchemaValidatorAfa6D7527045Ebc928EE7E30Ad3092A \
    as JSONSchemaValidatorAfa6D7527045Ebc928EE7E30Ad3092A_v3_0_0
from .validators.v3_0_0.jsd_b641825a9555ecba105cabbdf50fc78 \
    import JSONSchemaValidatorB641825A9555EcbA105Cabbdf50Fc78 \
    as JSONSchemaValidatorB641825A9555EcbA105Cabbdf50Fc78_v3_0_0
from .validators.v3_0_0.jsd_d904c521059563490c4a93871b33d51 \
    import JSONSchemaValidatorD904C521059563490C4A93871B33D51 \
    as JSONSchemaValidatorD904C521059563490C4A93871B33D51_v3_0_0
from .validators.v3_0_0.jsd_dfe1db8729d541fb3a17d31d47d1881 \
    import JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881 \
    as JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881_v3_0_0
from .validators.v3_0_0.jsd_ed5bf99062d5dee87fe5cd96e360ec2 \
    import JSONSchemaValidatorEd5Bf99062D5Dee87Fe5Cd96E360Ec2 \
    as JSONSchemaValidatorEd5Bf99062D5Dee87Fe5Cd96E360Ec2_v3_0_0
from .validators.v3_0_0.jsd_a0824f9a589c58cd8df522524cb550ad \
    import JSONSchemaValidatorA0824F9A589C58Cd8Df522524Cb550Ad \
    as JSONSchemaValidatorA0824F9A589C58Cd8Df522524Cb550Ad_v3_0_0
from .validators.v3_0_0.jsd_a0fdb67d95475cd39382171dec96d6c1 \
    import JSONSchemaValidatorA0Fdb67D95475Cd39382171Dec96D6C1 \
    as JSONSchemaValidatorA0Fdb67D95475Cd39382171Dec96D6C1_v3_0_0
from .validators.v3_0_0.jsd_a1e3cde0c3f254b39caaaf7c907ae67e \
    import JSONSchemaValidatorA1E3Cde0C3F254B39CaaAf7C907Ae67E \
    as JSONSchemaValidatorA1E3Cde0C3F254B39CaaAf7C907Ae67E_v3_0_0
from .validators.v3_0_0.jsd_a22b2304dcc855abb2a298de6ecddb65 \
    import JSONSchemaValidatorA22B2304Dcc855AbB2A298De6Ecddb65 \
    as JSONSchemaValidatorA22B2304Dcc855AbB2A298De6Ecddb65_v3_0_0
from .validators.v3_0_0.jsd_a4ab683ce53052e089626a096abaf451 \
    import JSONSchemaValidatorA4Ab683CE53052E089626A096Abaf451 \
    as JSONSchemaValidatorA4Ab683CE53052E089626A096Abaf451_v3_0_0
from .validators.v3_0_0.jsd_a50d1bd34d5f593aadf8eb02083c67b0 \
    import JSONSchemaValidatorA50D1Bd34D5F593AAdf8Eb02083C67B0 \
    as JSONSchemaValidatorA50D1Bd34D5F593AAdf8Eb02083C67B0_v3_0_0
from .validators.v3_0_0.jsd_a60b29bfe2b055299e4360d84380ddd4 \
    import JSONSchemaValidatorA60B29BfE2B055299E4360D84380Ddd4 \
    as JSONSchemaValidatorA60B29BfE2B055299E4360D84380Ddd4_v3_0_0
from .validators.v3_0_0.jsd_a69c7f1ad54e5e9cae1f871e19eed61b \
    import JSONSchemaValidatorA69C7F1AD54E5E9CAe1F871E19Eed61B \
    as JSONSchemaValidatorA69C7F1AD54E5E9CAe1F871E19Eed61B_v3_0_0
from .validators.v3_0_0.jsd_a87d60d590485830aed781bfb15b5c95 \
    import JSONSchemaValidatorA87D60D590485830Aed781Bfb15B5C95 \
    as JSONSchemaValidatorA87D60D590485830Aed781Bfb15B5C95_v3_0_0
from .validators.v3_0_0.jsd_aa4daefaa3b95ecca521188a43eacbd9 \
    import JSONSchemaValidatorAa4DaefaA3B95EccA521188A43Eacbd9 \
    as JSONSchemaValidatorAa4DaefaA3B95EccA521188A43Eacbd9_v3_0_0
from .validators.v3_0_0.jsd_ab916b19789c59b79dddbc2d0a3c57fc \
    import JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc \
    as JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc_v3_0_0
from .validators.v3_0_0.jsd_ac171b8ccf79502fbc4b35909970a1cb \
    import JSONSchemaValidatorAc171B8CCf79502FBc4B35909970A1Cb \
    as JSONSchemaValidatorAc171B8CCf79502FBc4B35909970A1Cb_v3_0_0
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
from .validators.v3_0_0.jsd_b3d905ee2883501281de916733b4025c \
    import JSONSchemaValidatorB3D905Ee2883501281De916733B4025C \
    as JSONSchemaValidatorB3D905Ee2883501281De916733B4025C_v3_0_0
from .validators.v3_0_0.jsd_b4ceac9ee830523ca5ddbfdf3e1b44be \
    import JSONSchemaValidatorB4Ceac9EE830523CA5DdBfdf3E1B44Be \
    as JSONSchemaValidatorB4Ceac9EE830523CA5DdBfdf3E1B44Be_v3_0_0
from .validators.v3_0_0.jsd_b5c6ed4306f059cc963895a04f219d5d \
    import JSONSchemaValidatorB5C6Ed4306F059Cc963895A04F219D5D \
    as JSONSchemaValidatorB5C6Ed4306F059Cc963895A04F219D5D_v3_0_0
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
from .validators.v3_0_0.jsd_bdea52558473565c9963ec14c65727b8 \
    import JSONSchemaValidatorBdea52558473565C9963Ec14C65727B8 \
    as JSONSchemaValidatorBdea52558473565C9963Ec14C65727B8_v3_0_0
from .validators.v3_0_0.jsd_beebf3641335579e99c08f038303601e \
    import JSONSchemaValidatorBeebf3641335579E99C08F038303601E \
    as JSONSchemaValidatorBeebf3641335579E99C08F038303601E_v3_0_0
from .validators.v3_0_0.jsd_bf792ec664fa5202beb776556908b0c1 \
    import JSONSchemaValidatorBf792Ec664Fa5202Beb776556908B0C1 \
    as JSONSchemaValidatorBf792Ec664Fa5202Beb776556908B0C1_v3_0_0
from .validators.v3_0_0.jsd_bf95f099207a5b6599e04c47c22789c0 \
    import JSONSchemaValidatorBf95F099207A5B6599E04C47C22789C0 \
    as JSONSchemaValidatorBf95F099207A5B6599E04C47C22789C0_v3_0_0
from .validators.v3_0_0.jsd_c0984cde5e925c209ab87472ab905476 \
    import JSONSchemaValidatorC0984Cde5E925C209Ab87472Ab905476 \
    as JSONSchemaValidatorC0984Cde5E925C209Ab87472Ab905476_v3_0_0
from .validators.v3_0_0.jsd_c1052ac49dd35088a9874a4350182015 \
    import JSONSchemaValidatorC1052Ac49Dd35088A9874A4350182015 \
    as JSONSchemaValidatorC1052Ac49Dd35088A9874A4350182015_v3_0_0
from .validators.v3_0_0.jsd_c14128e5729b55e9b1feb638a8295e10 \
    import JSONSchemaValidatorC14128E5729B55E9B1FeB638A8295E10 \
    as JSONSchemaValidatorC14128E5729B55E9B1FeB638A8295E10_v3_0_0
from .validators.v3_0_0.jsd_c37778a2faa5552894cc60cec13c56c7 \
    import JSONSchemaValidatorC37778A2Faa5552894Cc60Cec13C56C7 \
    as JSONSchemaValidatorC37778A2Faa5552894Cc60Cec13C56C7_v3_0_0
from .validators.v3_0_0.jsd_c578ef80918b5d038024d126cd6e3b8d \
    import JSONSchemaValidatorC578Ef80918B5D038024D126Cd6E3B8D \
    as JSONSchemaValidatorC578Ef80918B5D038024D126Cd6E3B8D_v3_0_0
from .validators.v3_0_0.jsd_c5e52706e7095a81b8d32f3024e01cf6 \
    import JSONSchemaValidatorC5E52706E7095A81B8D32F3024E01Cf6 \
    as JSONSchemaValidatorC5E52706E7095A81B8D32F3024E01Cf6_v3_0_0
from .validators.v3_0_0.jsd_c654a18faf1b5571ac5ba61145d298c4 \
    import JSONSchemaValidatorC654A18FAf1B5571Ac5BA61145D298C4 \
    as JSONSchemaValidatorC654A18FAf1B5571Ac5BA61145D298C4_v3_0_0
from .validators.v3_0_0.jsd_c6c330dace185a548f70f4e5d67776ea \
    import JSONSchemaValidatorC6C330DaCe185A548F70F4E5D67776Ea \
    as JSONSchemaValidatorC6C330DaCe185A548F70F4E5D67776Ea_v3_0_0
from .validators.v3_0_0.jsd_c77600d349fc5c259dbd22d65b3ffa1d \
    import JSONSchemaValidatorC77600D349Fc5C259Dbd22D65B3Ffa1D \
    as JSONSchemaValidatorC77600D349Fc5C259Dbd22D65B3Ffa1D_v3_0_0
from .validators.v3_0_0.jsd_c7aa2a6cac155a6cb7ace3fd76a81e0f \
    import JSONSchemaValidatorC7Aa2A6CAc155A6CB7AcE3Fd76A81E0F \
    as JSONSchemaValidatorC7Aa2A6CAc155A6CB7AcE3Fd76A81E0F_v3_0_0
from .validators.v3_0_0.jsd_c8cd2f618b655d988ce626e579486596 \
    import JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596 \
    as JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596_v3_0_0
from .validators.v3_0_0.jsd_c8dbec9679d453f78cb47d894c507a7b \
    import JSONSchemaValidatorC8Dbec9679D453F78Cb47D894C507A7B \
    as JSONSchemaValidatorC8Dbec9679D453F78Cb47D894C507A7B_v3_0_0
from .validators.v3_0_0.jsd_c941303330bc5615b3eb8d4d2702b874 \
    import JSONSchemaValidatorC941303330Bc5615B3Eb8D4D2702B874 \
    as JSONSchemaValidatorC941303330Bc5615B3Eb8D4D2702B874_v3_0_0
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
from .validators.v3_0_0.jsd_cc909c2717cf55f1863a04a785166fe0 \
    import JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0 \
    as JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0_v3_0_0
from .validators.v3_0_0.jsd_cd429bb8ff3556a796570480f742028b \
    import JSONSchemaValidatorCd429Bb8Ff3556A796570480F742028B \
    as JSONSchemaValidatorCd429Bb8Ff3556A796570480F742028B_v3_0_0
from .validators.v3_0_0.jsd_cd6793a4a8e7576c8b290bdc88001f6f \
    import JSONSchemaValidatorCd6793A4A8E7576C8B290Bdc88001F6F \
    as JSONSchemaValidatorCd6793A4A8E7576C8B290Bdc88001F6F_v3_0_0
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
from .validators.v3_0_0.jsd_d810359e31e453ac8145981b7d5bb7e4 \
    import JSONSchemaValidatorD810359E31E453Ac8145981B7D5Bb7E4 \
    as JSONSchemaValidatorD810359E31E453Ac8145981B7D5Bb7E4_v3_0_0
from .validators.v3_0_0.jsd_d82fe0f9e4635b74af809beaaf98bd07 \
    import JSONSchemaValidatorD82Fe0F9E4635B74Af809Beaaf98Bd07 \
    as JSONSchemaValidatorD82Fe0F9E4635B74Af809Beaaf98Bd07_v3_0_0
from .validators.v3_0_0.jsd_d8e470a4ef6a58b3b21f9adbbdcc7a46 \
    import JSONSchemaValidatorD8E470A4Ef6A58B3B21F9Adbbdcc7A46 \
    as JSONSchemaValidatorD8E470A4Ef6A58B3B21F9Adbbdcc7A46_v3_0_0
from .validators.v3_0_0.jsd_d912b1c21e2b5dca8b56332d3a8ad13d \
    import JSONSchemaValidatorD912B1C21E2B5Dca8B56332D3A8Ad13D \
    as JSONSchemaValidatorD912B1C21E2B5Dca8B56332D3A8Ad13D_v3_0_0
from .validators.v3_0_0.jsd_d9ddc2557a495493bca08b8b973601aa \
    import JSONSchemaValidatorD9Ddc2557A495493Bca08B8B973601Aa \
    as JSONSchemaValidatorD9Ddc2557A495493Bca08B8B973601Aa_v3_0_0
from .validators.v3_0_0.jsd_db686413cf4558188ea60ccc05c3e920 \
    import JSONSchemaValidatorDb686413Cf4558188Ea60Ccc05C3E920 \
    as JSONSchemaValidatorDb686413Cf4558188Ea60Ccc05C3E920_v3_0_0
from .validators.v3_0_0.jsd_dd6c2553ae0053c1bbbdbd46c1df0ef9 \
    import JSONSchemaValidatorDd6C2553Ae0053C1BbbdBd46C1Df0Ef9 \
    as JSONSchemaValidatorDd6C2553Ae0053C1BbbdBd46C1Df0Ef9_v3_0_0
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
from .validators.v3_0_0.jsd_e2a697abfe2058d3adc7ad9922f5a5d6 \
    import JSONSchemaValidatorE2A697AbFe2058D3Adc7Ad9922F5A5D6 \
    as JSONSchemaValidatorE2A697AbFe2058D3Adc7Ad9922F5A5D6_v3_0_0
from .validators.v3_0_0.jsd_e2c930d3d75859b8b7d30e79f3eab084 \
    import JSONSchemaValidatorE2C930D3D75859B8B7D30E79F3Eab084 \
    as JSONSchemaValidatorE2C930D3D75859B8B7D30E79F3Eab084_v3_0_0
from .validators.v3_0_0.jsd_e39868ea7aec5efcaaf55009699eda5d \
    import JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D \
    as JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D_v3_0_0
from .validators.v3_0_0.jsd_e405a20316825460a1f37a2f161e7ac5 \
    import JSONSchemaValidatorE405A20316825460A1F37A2F161E7Ac5 \
    as JSONSchemaValidatorE405A20316825460A1F37A2F161E7Ac5_v3_0_0
from .validators.v3_0_0.jsd_e56dd3caaf62589f9e827d03e8427467 \
    import JSONSchemaValidatorE56Dd3CaAf62589F9E827D03E8427467 \
    as JSONSchemaValidatorE56Dd3CaAf62589F9E827D03E8427467_v3_0_0
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
from .validators.v3_0_0.jsd_ea5b356b4bc053068a0052b6c807d286 \
    import JSONSchemaValidatorEa5B356B4Bc053068A0052B6C807D286 \
    as JSONSchemaValidatorEa5B356B4Bc053068A0052B6C807D286_v3_0_0
from .validators.v3_0_0.jsd_ea5e5a095d05598db7b99ddfd1d7f7fa \
    import JSONSchemaValidatorEa5E5A095D05598DB7B99Ddfd1D7F7Fa \
    as JSONSchemaValidatorEa5E5A095D05598DB7B99Ddfd1D7F7Fa_v3_0_0
from .validators.v3_0_0.jsd_ea658190e73c5ce1b27e7def4aea28e3 \
    import JSONSchemaValidatorEa658190E73C5Ce1B27E7Def4Aea28E3 \
    as JSONSchemaValidatorEa658190E73C5Ce1B27E7Def4Aea28E3_v3_0_0
from .validators.v3_0_0.jsd_eaa0d7c339d152b688876c2e10f51fe7 \
    import JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7 \
    as JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7_v3_0_0
from .validators.v3_0_0.jsd_eb8e0ce63376573995a49178435f7747 \
    import JSONSchemaValidatorEb8E0Ce63376573995A49178435F7747 \
    as JSONSchemaValidatorEb8E0Ce63376573995A49178435F7747_v3_0_0
from .validators.v3_0_0.jsd_ec26ec11d92356a594a6efa55ccb9be7 \
    import JSONSchemaValidatorEc26Ec11D92356A594A6Efa55Ccb9Be7 \
    as JSONSchemaValidatorEc26Ec11D92356A594A6Efa55Ccb9Be7_v3_0_0
from .validators.v3_0_0.jsd_ecff2eb67fe5591f8d9026f928a0d8aa \
    import JSONSchemaValidatorEcff2Eb67Fe5591F8D9026F928A0D8Aa \
    as JSONSchemaValidatorEcff2Eb67Fe5591F8D9026F928A0D8Aa_v3_0_0
from .validators.v3_0_0.jsd_ed1ef503c091506aa8e446182e625365 \
    import JSONSchemaValidatorEd1Ef503C091506AA8E446182E625365 \
    as JSONSchemaValidatorEd1Ef503C091506AA8E446182E625365_v3_0_0
from .validators.v3_0_0.jsd_f1196f1f6fde5978b0522f096926d443 \
    import JSONSchemaValidatorF1196F1F6Fde5978B0522F096926D443 \
    as JSONSchemaValidatorF1196F1F6Fde5978B0522F096926D443_v3_0_0
from .validators.v3_0_0.jsd_f16d14057660520dba53cc0df60db4a8 \
    import JSONSchemaValidatorF16D14057660520DBa53Cc0Df60Db4A8 \
    as JSONSchemaValidatorF16D14057660520DBa53Cc0Df60Db4A8_v3_0_0
from .validators.v3_0_0.jsd_f1b8eaf23e795f1a8525eb5905187aa9 \
    import JSONSchemaValidatorF1B8Eaf23E795F1A8525Eb5905187Aa9 \
    as JSONSchemaValidatorF1B8Eaf23E795F1A8525Eb5905187Aa9_v3_0_0
from .validators.v3_0_0.jsd_f1ff2b82953f5131884f0779db37190c \
    import JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C \
    as JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C_v3_0_0
from .validators.v3_0_0.jsd_f2b0a67d389a592dba005895594b77cc \
    import JSONSchemaValidatorF2B0A67D389A592DBa005895594B77Cc \
    as JSONSchemaValidatorF2B0A67D389A592DBa005895594B77Cc_v3_0_0
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
from .validators.v3_0_0.jsd_f92e61297eb05379bd9b92bc60735912 \
    import JSONSchemaValidatorF92E61297Eb05379Bd9B92Bc60735912 \
    as JSONSchemaValidatorF92E61297Eb05379Bd9B92Bc60735912_v3_0_0
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
from .validators.v3_0_0.jsd_fcf7754d5b45523a8227d37c476a1880 \
    import JSONSchemaValidatorFcf7754D5B45523A8227D37C476A1880 \
    as JSONSchemaValidatorFcf7754D5B45523A8227D37C476A1880_v3_0_0
from .validators.v3_0_0.jsd_fd4b5a56f8bd5f8f919e9fffc172e72f \
    import JSONSchemaValidatorFd4B5A56F8Bd5F8F919E9Fffc172E72F \
    as JSONSchemaValidatorFd4B5A56F8Bd5F8F919E9Fffc172E72F_v3_0_0
from .validators.v3_0_0.jsd_fe54c96ccba65af1abe3cd08f4fc69cb \
    import JSONSchemaValidatorFe54C96CCba65Af1Abe3Cd08F4Fc69Cb \
    as JSONSchemaValidatorFe54C96CCba65Af1Abe3Cd08F4Fc69Cb_v3_0_0
from .validators.v3_0_0.jsd_feb30ca768795eed82c118d009d7bcd4 \
    import JSONSchemaValidatorFeb30Ca768795Eed82C118D009D7Bcd4 \
    as JSONSchemaValidatorFeb30Ca768795Eed82C118D009D7Bcd4_v3_0_0
from .validators.v3_0_0.jsd_ff0055f9ef115a42bea6ffdd8e57d41b \
    import JSONSchemaValidatorFf0055F9Ef115A42Bea6Ffdd8E57D41B \
    as JSONSchemaValidatorFf0055F9Ef115A42Bea6Ffdd8E57D41B_v3_0_0
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
            self.json_schema_validators['jsd_ab7717877a539b9b87f499817aee15_v3_0_0'] =\
                JSONSchemaValidatorAb7717877A539B9B87F499817Aee15_v3_0_0()
            self.json_schema_validators['jsd_db1d9dda53369e35d33138b29c16_v3_0_0'] =\
                JSONSchemaValidatorDb1D9Dda53369E35D33138B29C16_v3_0_0()
            self.json_schema_validators['jsd_ab015a9eb6d5f2b91002af068cb4ce2_v3_0_0'] =\
                JSONSchemaValidatorAb015A9Eb6D5F2B91002Af068Cb4Ce2_v3_0_0()
            self.json_schema_validators['jsd_ac243ecb8c157658a4bcfe77a102c14_v3_0_0'] =\
                JSONSchemaValidatorAc243EcB8C157658A4BCfe77A102C14_v3_0_0()
            self.json_schema_validators['jsd_b3fe0f3ea8a5368aea79a847288993e_v3_0_0'] =\
                JSONSchemaValidatorB3Fe0F3Ea8A5368Aea79A847288993E_v3_0_0()
            self.json_schema_validators['jsd_cdc971b23285b87945021bd5983d1cd_v3_0_0'] =\
                JSONSchemaValidatorCdc971B23285B87945021Bd5983D1Cd_v3_0_0()
            self.json_schema_validators['jsd_d1df0e230765104863b8d63d5beb68e_v3_0_0'] =\
                JSONSchemaValidatorD1Df0E230765104863B8D63D5Beb68E_v3_0_0()
            self.json_schema_validators['jsd_dedf09f59e754c6ae5212d43b1c8fb2_v3_0_0'] =\
                JSONSchemaValidatorDedf09F59E754C6Ae5212D43B1C8Fb2_v3_0_0()
            self.json_schema_validators['jsd_f41a1e47105581fabf212f259626903_v3_0_0'] =\
                JSONSchemaValidatorF41A1E47105581FAbf212F259626903_v3_0_0()
            self.json_schema_validators['jsd_e34177d675622acd0a532f5b7c41b_v3_0_0'] =\
                JSONSchemaValidatorE34177D675622Acd0A532F5B7C41B_v3_0_0()
            self.json_schema_validators['jsd_f8f4956d29b821fa9bbf23266_v3_0_0'] =\
                JSONSchemaValidatorF8F4956D29B821Fa9Bbf23266_v3_0_0()
            self.json_schema_validators['jsd_a518d5655f69e8687c9c98740c6_v3_0_0'] =\
                JSONSchemaValidatorA518D5655F69E8687C9C98740C6_v3_0_0()
            self.json_schema_validators['jsd_c45ba035019803dacdbf15cf193_v3_0_0'] =\
                JSONSchemaValidatorC45Ba035019803DAcdbf15Cf193_v3_0_0()
            self.json_schema_validators['jsd_ca61ff725fedb94fba602d7afe46_v3_0_0'] =\
                JSONSchemaValidatorCa61Ff725FedB94FBa602D7Afe46_v3_0_0()
            self.json_schema_validators['jsd_ebcdc835e9b8d6844c1da6cf252_v3_0_0'] =\
                JSONSchemaValidatorEbcDc835E9B8D6844C1Da6Cf252_v3_0_0()
            self.json_schema_validators['jsd_ea10f18c3655db84657ad855bf6972_v3_0_0'] =\
                JSONSchemaValidatorEa10F18C3655Db84657Ad855Bf6972_v3_0_0()
            self.json_schema_validators['jsd_b9e8541f25c4ea29944f659f68994_v3_0_0'] =\
                JSONSchemaValidatorB9E8541F25C4EA29944F659F68994_v3_0_0()
            self.json_schema_validators['jsd_c8aec23a55399a175acf105dbe1c2_v3_0_0'] =\
                JSONSchemaValidatorC8Aec23A55399A175Acf105Dbe1C2_v3_0_0()
            self.json_schema_validators['jsd_cfcc7615d0492e2dd1b04dd03a9_v3_0_0'] =\
                JSONSchemaValidatorCfcC7615D0492E2Dd1B04Dd03A9_v3_0_0()
            self.json_schema_validators['jsd_d26670a205a78800cb50673027a6e_v3_0_0'] =\
                JSONSchemaValidatorD26670A205A78800CB50673027A6E_v3_0_0()
            self.json_schema_validators['jsd_f5d5ab6568d8bf5f9932f7ed7f4_v3_0_0'] =\
                JSONSchemaValidatorF5D5Ab6568D8Bf5F9932F7Ed7F4_v3_0_0()
            self.json_schema_validators['jsd_daac88943a5cd2bd745c483448e231_v3_0_0'] =\
                JSONSchemaValidatorDaac88943A5Cd2Bd745C483448E231_v3_0_0()
            self.json_schema_validators['jsd_e6d1b224e058288a8c4d70be72c9a6_v3_0_0'] =\
                JSONSchemaValidatorE6D1B224E058288A8C4D70Be72C9A6_v3_0_0()
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
            self.json_schema_validators['jsd_c7d6bb4abf53f6aa2f40b6986f58a9_v3_0_0'] =\
                JSONSchemaValidatorC7D6Bb4Abf53F6Aa2F40B6986F58A9_v3_0_0()
            self.json_schema_validators['jsd_c53b22885f5e5d82fb8cadd0332136_v3_0_0'] =\
                JSONSchemaValidatorC53B22885F5E5D82Fb8Cadd0332136_v3_0_0()
            self.json_schema_validators['jsd_e23ac4c658f5b75f19d13d6f7189_v3_0_0'] =\
                JSONSchemaValidatorE23AC4C658F5B75F19D13D6F7189_v3_0_0()
            self.json_schema_validators['jsd_ce65f2bd375be1ba41a7d6f02ad7b6_v3_0_0'] =\
                JSONSchemaValidatorCe65F2Bd375Be1Ba41A7D6F02Ad7B6_v3_0_0()
            self.json_schema_validators['jsd_cb625d5ad0ad76b93282f5818a_v3_0_0'] =\
                JSONSchemaValidatorCb625D5Ad0Ad76B93282F5818A_v3_0_0()
            self.json_schema_validators['jsd_f78898b7d655b2b81085dc7c0a964e_v3_0_0'] =\
                JSONSchemaValidatorF78898B7D655B2B81085Dc7C0A964E_v3_0_0()
            self.json_schema_validators['jsd_a599ae00f5e47b9ece23cd3183d1c_v3_0_0'] =\
                JSONSchemaValidatorA599AE00F5E47B9EcE23Cd3183D1C_v3_0_0()
            self.json_schema_validators['jsd_c288192f954309b4b35aa612ff226_v3_0_0'] =\
                JSONSchemaValidatorC288192F954309B4B35Aa612Ff226_v3_0_0()
            self.json_schema_validators['jsd_f64c3c08518e9eef83a92d69cde3_v3_0_0'] =\
                JSONSchemaValidatorF64C3C08518E9Eef83A92D69Cde3_v3_0_0()
            self.json_schema_validators['jsd_c3c7d5a3a83d9f7441972d399_v3_0_0'] =\
                JSONSchemaValidatorC3C7D5A3A83D9F7441972D399_v3_0_0()
            self.json_schema_validators['jsd_a4d5b5da6a50bfaaecc180543fd952_v3_0_0'] =\
                JSONSchemaValidatorA4D5B5Da6A50BfAaecC180543Fd952_v3_0_0()
            self.json_schema_validators['jsd_a99695fd5ee0b00efce79a5761ff_v3_0_0'] =\
                JSONSchemaValidatorA99695Fd5Ee0B00EFce79A5761Ff_v3_0_0()
            self.json_schema_validators['jsd_da0a59db7654cfa89df49ca3ac3414_v3_0_0'] =\
                JSONSchemaValidatorDa0A59Db7654CfA89DF49Ca3Ac3414_v3_0_0()
            self.json_schema_validators['jsd_c0ec3a56f65447ba863ae0cac5ef6a_v3_0_0'] =\
                JSONSchemaValidatorC0Ec3A56F65447Ba863Ae0Cac5Ef6A_v3_0_0()
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
            self.json_schema_validators['jsd_a9f1f24542dbd244e31691a2e09_v3_0_0'] =\
                JSONSchemaValidatorA9F1F24542DBd244E31691A2E09_v3_0_0()
            self.json_schema_validators['jsd_e9cc593c395c48b31b30149467c846_v3_0_0'] =\
                JSONSchemaValidatorE9Cc593C395C48B31B30149467C846_v3_0_0()
            self.json_schema_validators['jsd_f8ba0e97135ca6bacff94d5a76df97_v3_0_0'] =\
                JSONSchemaValidatorF8Ba0E97135Ca6BacfF94D5A76Df97_v3_0_0()
            self.json_schema_validators['jsd_dc2eec65ad680a3c5de47cd87c8_v3_0_0'] =\
                JSONSchemaValidatorDc2Eec65Ad680A3C5De47Cd87C8_v3_0_0()
            self.json_schema_validators['jsd_b8696d875b12b0a3ab735b397d7a_v3_0_0'] =\
                JSONSchemaValidatorB8696D875B12B0A3Ab735B397D7A_v3_0_0()
            self.json_schema_validators['jsd_c5c9b7ab72b5442ae7026a5dcc0fec3_v3_0_0'] =\
                JSONSchemaValidatorC5C9B7AB72B5442Ae7026A5Dcc0Fec3_v3_0_0()
            self.json_schema_validators['jsd_ccba98a61555ae495f6a05284e3b5ae_v3_0_0'] =\
                JSONSchemaValidatorCcba98A61555Ae495F6A05284E3B5Ae_v3_0_0()
            self.json_schema_validators['jsd_e155669bc74586e9ef2580ec5752902_v3_0_0'] =\
                JSONSchemaValidatorE155669Bc74586E9Ef2580Ec5752902_v3_0_0()
            self.json_schema_validators['jsd_f36e90115b05416a71506061fed7e5c_v3_0_0'] =\
                JSONSchemaValidatorF36E90115B05416A71506061Fed7E5C_v3_0_0()
            self.json_schema_validators['jsd_fd9e7e03a6056d1b6e9705e3096d946_v3_0_0'] =\
                JSONSchemaValidatorFd9E7E03A6056D1B6E9705E3096D946_v3_0_0()
            self.json_schema_validators['jsd_c4fada6c558d9aba09cc373d5b266_v3_0_0'] =\
                JSONSchemaValidatorC4FadA6C558D9Aba09Cc373D5B266_v3_0_0()
            self.json_schema_validators['jsd_b11e2f1af656bcb5880a7b33720ec5_v3_0_0'] =\
                JSONSchemaValidatorB11E2F1Af656BcB5880A7B33720Ec5_v3_0_0()
            self.json_schema_validators['jsd_c9722c56108cac8ca50bf8f01c_v3_0_0'] =\
                JSONSchemaValidatorC9722C56108Cac8Ca50Bf8F01C_v3_0_0()
            self.json_schema_validators['jsd_b1da14ba95aa48b498c76d0bc1017_v3_0_0'] =\
                JSONSchemaValidatorB1Da14Ba95Aa48B498C76D0Bc1017_v3_0_0()
            self.json_schema_validators['jsd_cb9345e58f5433ae80f5d8f855978b_v3_0_0'] =\
                JSONSchemaValidatorCb9345E58F5433Ae80F5D8F855978B_v3_0_0()
            self.json_schema_validators['jsd_e603092f597ab6c25381e59c4a70_v3_0_0'] =\
                JSONSchemaValidatorE603092F597AB6C25381E59C4A70_v3_0_0()
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
            self.json_schema_validators['jsd_cf65cd559628b26f6eb5ea20f14_v3_0_0'] =\
                JSONSchemaValidatorCf65Cd559628B26F6Eb5Ea20F14_v3_0_0()
            self.json_schema_validators['jsd_acb5a41fe395b158a3fe1cda996b0cf_v3_0_0'] =\
                JSONSchemaValidatorAcb5A41Fe395B158A3FE1Cda996B0Cf_v3_0_0()
            self.json_schema_validators['jsd_e6c7251a8508597f1b7ae61cbf953_v3_0_0'] =\
                JSONSchemaValidatorE6C7251A8508597F1B7Ae61Cbf953_v3_0_0()
            self.json_schema_validators['jsd_dc966c73c65649a244d507bd53fd19_v3_0_0'] =\
                JSONSchemaValidatorDc966C73C65649A244D507Bd53Fd19_v3_0_0()
            self.json_schema_validators['jsd_e4c74e9b4e559e95c73e81183a6c7a_v3_0_0'] =\
                JSONSchemaValidatorE4C74E9B4E559E95C73E81183A6C7A_v3_0_0()
            self.json_schema_validators['jsd_a03a30be865ca599e77c63a332978b_v3_0_0'] =\
                JSONSchemaValidatorA03A30Be865Ca599E77C63A332978B_v3_0_0()
            self.json_schema_validators['jsd_c189f2f5f6b8bab3931c206c949_v3_0_0'] =\
                JSONSchemaValidatorC189F2F5F6B8Bab3931C206C949_v3_0_0()
            self.json_schema_validators['jsd_d8610d4a355b63aaaa364447d5fa00_v3_0_0'] =\
                JSONSchemaValidatorD8610D4A355B63Aaaa364447D5Fa00_v3_0_0()
            self.json_schema_validators['jsd_feb825519f98bd1541ef3c367d_v3_0_0'] =\
                JSONSchemaValidatorFeB825519F98Bd1541Ef3C367D_v3_0_0()
            self.json_schema_validators['jsd_d1132a216d54d091022aec0ad018f8_v3_0_0'] =\
                JSONSchemaValidatorD1132A216D54D091022Aec0Ad018F8_v3_0_0()
            self.json_schema_validators['jsd_a588d29d5a527388ee8498f746d1f5_v3_0_0'] =\
                JSONSchemaValidatorA588D29D5A527388Ee8498F746D1F5_v3_0_0()
            self.json_schema_validators['jsd_ad69fa1d850f4993bbfc888749fa0_v3_0_0'] =\
                JSONSchemaValidatorAd69FA1D850F4993BBfc888749Fa0_v3_0_0()
            self.json_schema_validators['jsd_f564c3eda5c20bb807b8c062c8e7b_v3_0_0'] =\
                JSONSchemaValidatorF564C3Eda5C20Bb807B8C062C8E7B_v3_0_0()
            self.json_schema_validators['jsd_abc25887a5daab1216195e08cbd49_v3_0_0'] =\
                JSONSchemaValidatorAbc25887A5DaaB1216195E08Cbd49_v3_0_0()
            self.json_schema_validators['jsd_d1e1fc98a5588b8bbdda06c4fc012_v3_0_0'] =\
                JSONSchemaValidatorD1E1FC98A5588B8BbDda06C4Fc012_v3_0_0()
            self.json_schema_validators['jsd_ad233598ed75e0c97ddd3c3f1af50e4_v3_0_0'] =\
                JSONSchemaValidatorAd233598Ed75E0C97DdD3C3F1Af50E4_v3_0_0()
            self.json_schema_validators['jsd_c475afd2a5e57e4bd0952f2c5349c6c_v3_0_0'] =\
                JSONSchemaValidatorC475Afd2A5E57E4Bd0952F2C5349C6C_v3_0_0()
            self.json_schema_validators['jsd_ce70db7732c596aa82bd7d1725ac02d_v3_0_0'] =\
                JSONSchemaValidatorCe70Db7732C596AA82BD7D1725Ac02D_v3_0_0()
            self.json_schema_validators['jsd_dec8e9d819b5bc088e351b69efd0369_v3_0_0'] =\
                JSONSchemaValidatorDec8E9D819B5Bc088E351B69Efd0369_v3_0_0()
            self.json_schema_validators['jsd_e4bfa620f76545d9887045cd24d99a2_v3_0_0'] =\
                JSONSchemaValidatorE4Bfa620F76545D9887045Cd24D99A2_v3_0_0()
            self.json_schema_validators['jsd_fb4ef0633057a1acdc47e23b120073_v3_0_0'] =\
                JSONSchemaValidatorFb4Ef0633057A1Acdc47E23B120073_v3_0_0()
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
            self.json_schema_validators['jsd_cbcecf65a0155fcad602d3ac16531a7_v3_0_0'] =\
                JSONSchemaValidatorCbcecf65A0155FcAd602D3Ac16531A7_v3_0_0()
            self.json_schema_validators['jsd_df4fb303a3e5661ba12058f18b225af_v3_0_0'] =\
                JSONSchemaValidatorDf4Fb303A3E5661Ba12058F18B225Af_v3_0_0()
            self.json_schema_validators['jsd_e58eabefef15feb880ecfe2906d805f_v3_0_0'] =\
                JSONSchemaValidatorE58EabeFef15Feb880ECfe2906D805F_v3_0_0()
            self.json_schema_validators['jsd_ee1780a38a85d1ba57c9a38e1093721_v3_0_0'] =\
                JSONSchemaValidatorEe1780A38A85D1BA57C9A38E1093721_v3_0_0()
            self.json_schema_validators['jsd_faa7211d68e5b329034e17c82b78694_v3_0_0'] =\
                JSONSchemaValidatorFaa7211D68E5B329034E17C82B78694_v3_0_0()
            self.json_schema_validators['jsd_f4508bb3352ff920dbdc229e0fc50_v3_0_0'] =\
                JSONSchemaValidatorF4508Bb3352Ff920DBdc229E0Fc50_v3_0_0()
            self.json_schema_validators['jsd_e68f07767522ba1e49dc474e936d2_v3_0_0'] =\
                JSONSchemaValidatorE68F07767522BA1E49Dc474E936D2_v3_0_0()
            self.json_schema_validators['jsd_b7f7285d71be4645db91b0fc74_v3_0_0'] =\
                JSONSchemaValidatorB7F7285D71Be4645Db91B0Fc74_v3_0_0()
            self.json_schema_validators['jsd_eca5db5147b1e3b35a032ced4b_v3_0_0'] =\
                JSONSchemaValidatorEcA5Db5147B1E3B35A032Ced4B_v3_0_0()
            self.json_schema_validators['jsd_d9f17adde53e2a08a650b9fe1714c_v3_0_0'] =\
                JSONSchemaValidatorD9F17Adde53E2A08A650B9Fe1714C_v3_0_0()
            self.json_schema_validators['jsd_b314d32b258a1b53c5c84cf84d396_v3_0_0'] =\
                JSONSchemaValidatorB314D32B258A1B53C5C84Cf84D396_v3_0_0()
            self.json_schema_validators['jsd_cba3f7ace597da668acfbe00364be_v3_0_0'] =\
                JSONSchemaValidatorCba3F7Ace597DA668Acfbe00364Be_v3_0_0()
            self.json_schema_validators['jsd_bee301e7f5ccfa2e788dcafbf92cc_v3_0_0'] =\
                JSONSchemaValidatorBee301E7F5CcfA2E788Dcafbf92Cc_v3_0_0()
            self.json_schema_validators['jsd_ae615b5e28c54639f44bd10e5b36601_v3_0_0'] =\
                JSONSchemaValidatorAe615B5E28C54639F44Bd10E5B36601_v3_0_0()
            self.json_schema_validators['jsd_c0b4d1bbda75355912f208521362a41_v3_0_0'] =\
                JSONSchemaValidatorC0B4D1BBda75355912F208521362A41_v3_0_0()
            self.json_schema_validators['jsd_c6be021c4ca59e48c97afe218219bb1_v3_0_0'] =\
                JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1_v3_0_0()
            self.json_schema_validators['jsd_d0ed84901325292ad4e2a91a174f6b2_v3_0_0'] =\
                JSONSchemaValidatorD0Ed84901325292Ad4E2A91A174F6B2_v3_0_0()
            self.json_schema_validators['jsd_d53842e83f0538cab91e097aa6800ce_v3_0_0'] =\
                JSONSchemaValidatorD53842E83F0538CAb91E097Aa6800Ce_v3_0_0()
            self.json_schema_validators['jsd_f403dda9440503191536993f569cc6f_v3_0_0'] =\
                JSONSchemaValidatorF403Dda9440503191536993F569Cc6F_v3_0_0()
            self.json_schema_validators['jsd_e6734850fabb2097fa969948cb_v3_0_0'] =\
                JSONSchemaValidatorE6734850FaBb2097Fa969948Cb_v3_0_0()
            self.json_schema_validators['jsd_e84541805d1da1fa3d4d581102a9_v3_0_0'] =\
                JSONSchemaValidatorE84541805D1DA1Fa3D4D581102A9_v3_0_0()
            self.json_schema_validators['jsd_c137cad852579f4b810ff8adf661_v3_0_0'] =\
                JSONSchemaValidatorC137Cad852579F4B810Ff8Adf661_v3_0_0()
            self.json_schema_validators['jsd_fd707ac0454be8fecc73a918a27b6_v3_0_0'] =\
                JSONSchemaValidatorFd707Ac0454Be8FecC73A918A27B6_v3_0_0()
            self.json_schema_validators['jsd_fff985b5159a0aa52bfe9e62ba7_v3_0_0'] =\
                JSONSchemaValidatorFff985B5159A0Aa52Bfe9E62Ba7_v3_0_0()
            self.json_schema_validators['jsd_a57687cef65891a6f48dd17f456c4e_v3_0_0'] =\
                JSONSchemaValidatorA57687Cef65891A6F48Dd17F456C4E_v3_0_0()
            self.json_schema_validators['jsd_af104d12b5c5e668af1504feca5c9b1_v3_0_0'] =\
                JSONSchemaValidatorAf104D12B5C5E668Af1504Feca5C9B1_v3_0_0()
            self.json_schema_validators['jsd_b9eb9547216547cab8b9e686eee674b_v3_0_0'] =\
                JSONSchemaValidatorB9Eb9547216547CAb8B9E686Eee674B_v3_0_0()
            self.json_schema_validators['jsd_c6c2a4908ee5f48b7e9cae7572f6a94_v3_0_0'] =\
                JSONSchemaValidatorC6C2A4908Ee5F48B7E9Cae7572F6A94_v3_0_0()
            self.json_schema_validators['jsd_ea7e01261355dcfae6412e0615ba1f5_v3_0_0'] =\
                JSONSchemaValidatorEa7E01261355DcfAe6412E0615Ba1F5_v3_0_0()
            self.json_schema_validators['jsd_bc200af85d598885a990ff9bcbf8_v3_0_0'] =\
                JSONSchemaValidatorBc200Af85D598885A990Ff9Bcbf8_v3_0_0()
            self.json_schema_validators['jsd_e92c6e47625711b9ce06f92bd4d219_v3_0_0'] =\
                JSONSchemaValidatorE92C6E47625711B9Ce06F92Bd4D219_v3_0_0()
            self.json_schema_validators['jsd_bdae59219027b4d40b94fa3d_v3_0_0'] =\
                JSONSchemaValidatorBdae59219027B4D40B94Fa3D_v3_0_0()
            self.json_schema_validators['jsd_a160f293375ae9924d8240c4efdc6a_v3_0_0'] =\
                JSONSchemaValidatorA160F293375Ae9924D8240C4Efdc6A_v3_0_0()
            self.json_schema_validators['jsd_a095b061f564ebba331f66505b0e3_v3_0_0'] =\
                JSONSchemaValidatorA095B061F564EBba331F66505B0E3_v3_0_0()
            self.json_schema_validators['jsd_b22d6ad9f595ab7e3eee5cf44de8a_v3_0_0'] =\
                JSONSchemaValidatorB22D6Ad9F595AB7E3Eee5Cf44De8A_v3_0_0()
            self.json_schema_validators['jsd_a4cccea3c9567498f6f688e0cf86e7_v3_0_0'] =\
                JSONSchemaValidatorA4CcceA3C9567498F6F688E0Cf86E7_v3_0_0()
            self.json_schema_validators['jsd_d87a24994c514d955149d33e1a99fb_v3_0_0'] =\
                JSONSchemaValidatorD87A24994C514D955149D33E1A99Fb_v3_0_0()
            self.json_schema_validators['jsd_afa6d7527045ebc928ee7e30ad3092a_v3_0_0'] =\
                JSONSchemaValidatorAfa6D7527045Ebc928EE7E30Ad3092A_v3_0_0()
            self.json_schema_validators['jsd_b641825a9555ecba105cabbdf50fc78_v3_0_0'] =\
                JSONSchemaValidatorB641825A9555EcbA105Cabbdf50Fc78_v3_0_0()
            self.json_schema_validators['jsd_d904c521059563490c4a93871b33d51_v3_0_0'] =\
                JSONSchemaValidatorD904C521059563490C4A93871B33D51_v3_0_0()
            self.json_schema_validators['jsd_dfe1db8729d541fb3a17d31d47d1881_v3_0_0'] =\
                JSONSchemaValidatorDfe1Db8729D541FB3A17D31D47D1881_v3_0_0()
            self.json_schema_validators['jsd_ed5bf99062d5dee87fe5cd96e360ec2_v3_0_0'] =\
                JSONSchemaValidatorEd5Bf99062D5Dee87Fe5Cd96E360Ec2_v3_0_0()
            self.json_schema_validators['jsd_a0824f9a589c58cd8df522524cb550ad_v3_0_0'] =\
                JSONSchemaValidatorA0824F9A589C58Cd8Df522524Cb550Ad_v3_0_0()
            self.json_schema_validators['jsd_a0fdb67d95475cd39382171dec96d6c1_v3_0_0'] =\
                JSONSchemaValidatorA0Fdb67D95475Cd39382171Dec96D6C1_v3_0_0()
            self.json_schema_validators['jsd_a1e3cde0c3f254b39caaaf7c907ae67e_v3_0_0'] =\
                JSONSchemaValidatorA1E3Cde0C3F254B39CaaAf7C907Ae67E_v3_0_0()
            self.json_schema_validators['jsd_a22b2304dcc855abb2a298de6ecddb65_v3_0_0'] =\
                JSONSchemaValidatorA22B2304Dcc855AbB2A298De6Ecddb65_v3_0_0()
            self.json_schema_validators['jsd_a4ab683ce53052e089626a096abaf451_v3_0_0'] =\
                JSONSchemaValidatorA4Ab683CE53052E089626A096Abaf451_v3_0_0()
            self.json_schema_validators['jsd_a50d1bd34d5f593aadf8eb02083c67b0_v3_0_0'] =\
                JSONSchemaValidatorA50D1Bd34D5F593AAdf8Eb02083C67B0_v3_0_0()
            self.json_schema_validators['jsd_a60b29bfe2b055299e4360d84380ddd4_v3_0_0'] =\
                JSONSchemaValidatorA60B29BfE2B055299E4360D84380Ddd4_v3_0_0()
            self.json_schema_validators['jsd_a69c7f1ad54e5e9cae1f871e19eed61b_v3_0_0'] =\
                JSONSchemaValidatorA69C7F1AD54E5E9CAe1F871E19Eed61B_v3_0_0()
            self.json_schema_validators['jsd_a87d60d590485830aed781bfb15b5c95_v3_0_0'] =\
                JSONSchemaValidatorA87D60D590485830Aed781Bfb15B5C95_v3_0_0()
            self.json_schema_validators['jsd_aa4daefaa3b95ecca521188a43eacbd9_v3_0_0'] =\
                JSONSchemaValidatorAa4DaefaA3B95EccA521188A43Eacbd9_v3_0_0()
            self.json_schema_validators['jsd_ab916b19789c59b79dddbc2d0a3c57fc_v3_0_0'] =\
                JSONSchemaValidatorAb916B19789C59B79DddBc2D0A3C57Fc_v3_0_0()
            self.json_schema_validators['jsd_ac171b8ccf79502fbc4b35909970a1cb_v3_0_0'] =\
                JSONSchemaValidatorAc171B8CCf79502FBc4B35909970A1Cb_v3_0_0()
            self.json_schema_validators['jsd_acf0372068885036baee3c4524638f31_v3_0_0'] =\
                JSONSchemaValidatorAcf0372068885036Baee3C4524638F31_v3_0_0()
            self.json_schema_validators['jsd_ae8d7c8f33bb52ceb04880845f2f45ba_v3_0_0'] =\
                JSONSchemaValidatorAe8D7C8F33Bb52CeB04880845F2F45Ba_v3_0_0()
            self.json_schema_validators['jsd_af14464cc6a05f6f87bbe7c174b6d5f6_v3_0_0'] =\
                JSONSchemaValidatorAf14464CC6A05F6F87BbE7C174B6D5F6_v3_0_0()
            self.json_schema_validators['jsd_afe1108b1a59539ebe3de3e5652c9653_v3_0_0'] =\
                JSONSchemaValidatorAfe1108B1A59539EBe3DE3E5652C9653_v3_0_0()
            self.json_schema_validators['jsd_b09ea91f72885e05b6aa73e89546f969_v3_0_0'] =\
                JSONSchemaValidatorB09Ea91F72885E05B6Aa73E89546F969_v3_0_0()
            self.json_schema_validators['jsd_b227e1b5bbac556a9f577d3a3ea407af_v3_0_0'] =\
                JSONSchemaValidatorB227E1B5Bbac556A9F577D3A3Ea407Af_v3_0_0()
            self.json_schema_validators['jsd_b3284240745e5b929c51495fe80bc1c4_v3_0_0'] =\
                JSONSchemaValidatorB3284240745E5B929C51495Fe80Bc1C4_v3_0_0()
            self.json_schema_validators['jsd_b3c356cfc48a5da4b13b8ecbae5748b7_v3_0_0'] =\
                JSONSchemaValidatorB3C356CfC48A5Da4B13B8Ecbae5748B7_v3_0_0()
            self.json_schema_validators['jsd_b3d905ee2883501281de916733b4025c_v3_0_0'] =\
                JSONSchemaValidatorB3D905Ee2883501281De916733B4025C_v3_0_0()
            self.json_schema_validators['jsd_b4ceac9ee830523ca5ddbfdf3e1b44be_v3_0_0'] =\
                JSONSchemaValidatorB4Ceac9EE830523CA5DdBfdf3E1B44Be_v3_0_0()
            self.json_schema_validators['jsd_b5c6ed4306f059cc963895a04f219d5d_v3_0_0'] =\
                JSONSchemaValidatorB5C6Ed4306F059Cc963895A04F219D5D_v3_0_0()
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
            self.json_schema_validators['jsd_bdea52558473565c9963ec14c65727b8_v3_0_0'] =\
                JSONSchemaValidatorBdea52558473565C9963Ec14C65727B8_v3_0_0()
            self.json_schema_validators['jsd_beebf3641335579e99c08f038303601e_v3_0_0'] =\
                JSONSchemaValidatorBeebf3641335579E99C08F038303601E_v3_0_0()
            self.json_schema_validators['jsd_bf792ec664fa5202beb776556908b0c1_v3_0_0'] =\
                JSONSchemaValidatorBf792Ec664Fa5202Beb776556908B0C1_v3_0_0()
            self.json_schema_validators['jsd_bf95f099207a5b6599e04c47c22789c0_v3_0_0'] =\
                JSONSchemaValidatorBf95F099207A5B6599E04C47C22789C0_v3_0_0()
            self.json_schema_validators['jsd_c0984cde5e925c209ab87472ab905476_v3_0_0'] =\
                JSONSchemaValidatorC0984Cde5E925C209Ab87472Ab905476_v3_0_0()
            self.json_schema_validators['jsd_c1052ac49dd35088a9874a4350182015_v3_0_0'] =\
                JSONSchemaValidatorC1052Ac49Dd35088A9874A4350182015_v3_0_0()
            self.json_schema_validators['jsd_c14128e5729b55e9b1feb638a8295e10_v3_0_0'] =\
                JSONSchemaValidatorC14128E5729B55E9B1FeB638A8295E10_v3_0_0()
            self.json_schema_validators['jsd_c37778a2faa5552894cc60cec13c56c7_v3_0_0'] =\
                JSONSchemaValidatorC37778A2Faa5552894Cc60Cec13C56C7_v3_0_0()
            self.json_schema_validators['jsd_c578ef80918b5d038024d126cd6e3b8d_v3_0_0'] =\
                JSONSchemaValidatorC578Ef80918B5D038024D126Cd6E3B8D_v3_0_0()
            self.json_schema_validators['jsd_c5e52706e7095a81b8d32f3024e01cf6_v3_0_0'] =\
                JSONSchemaValidatorC5E52706E7095A81B8D32F3024E01Cf6_v3_0_0()
            self.json_schema_validators['jsd_c654a18faf1b5571ac5ba61145d298c4_v3_0_0'] =\
                JSONSchemaValidatorC654A18FAf1B5571Ac5BA61145D298C4_v3_0_0()
            self.json_schema_validators['jsd_c6c330dace185a548f70f4e5d67776ea_v3_0_0'] =\
                JSONSchemaValidatorC6C330DaCe185A548F70F4E5D67776Ea_v3_0_0()
            self.json_schema_validators['jsd_c77600d349fc5c259dbd22d65b3ffa1d_v3_0_0'] =\
                JSONSchemaValidatorC77600D349Fc5C259Dbd22D65B3Ffa1D_v3_0_0()
            self.json_schema_validators['jsd_c7aa2a6cac155a6cb7ace3fd76a81e0f_v3_0_0'] =\
                JSONSchemaValidatorC7Aa2A6CAc155A6CB7AcE3Fd76A81E0F_v3_0_0()
            self.json_schema_validators['jsd_c8cd2f618b655d988ce626e579486596_v3_0_0'] =\
                JSONSchemaValidatorC8Cd2F618B655D988Ce626E579486596_v3_0_0()
            self.json_schema_validators['jsd_c8dbec9679d453f78cb47d894c507a7b_v3_0_0'] =\
                JSONSchemaValidatorC8Dbec9679D453F78Cb47D894C507A7B_v3_0_0()
            self.json_schema_validators['jsd_c941303330bc5615b3eb8d4d2702b874_v3_0_0'] =\
                JSONSchemaValidatorC941303330Bc5615B3Eb8D4D2702B874_v3_0_0()
            self.json_schema_validators['jsd_c97e7851003e5a63a2a8005ac8807dc7_v3_0_0'] =\
                JSONSchemaValidatorC97E7851003E5A63A2A8005Ac8807Dc7_v3_0_0()
            self.json_schema_validators['jsd_c9a67d3e9015580f93a52627f19e9916_v3_0_0'] =\
                JSONSchemaValidatorC9A67D3E9015580F93A52627F19E9916_v3_0_0()
            self.json_schema_validators['jsd_ca28129793d1569bb50de9f43b0d0ee8_v3_0_0'] =\
                JSONSchemaValidatorCa28129793D1569BB50DE9F43B0D0Ee8_v3_0_0()
            self.json_schema_validators['jsd_ca3df31c13b857e6b5dbc8357a8ab010_v3_0_0'] =\
                JSONSchemaValidatorCa3Df31C13B857E6B5DbC8357A8Ab010_v3_0_0()
            self.json_schema_validators['jsd_cc909c2717cf55f1863a04a785166fe0_v3_0_0'] =\
                JSONSchemaValidatorCc909C2717Cf55F1863A04A785166Fe0_v3_0_0()
            self.json_schema_validators['jsd_cd429bb8ff3556a796570480f742028b_v3_0_0'] =\
                JSONSchemaValidatorCd429Bb8Ff3556A796570480F742028B_v3_0_0()
            self.json_schema_validators['jsd_cd6793a4a8e7576c8b290bdc88001f6f_v3_0_0'] =\
                JSONSchemaValidatorCd6793A4A8E7576C8B290Bdc88001F6F_v3_0_0()
            self.json_schema_validators['jsd_d0e432f52e2a5863858c7dc0c3eda277_v3_0_0'] =\
                JSONSchemaValidatorD0E432F52E2A5863858C7Dc0C3Eda277_v3_0_0()
            self.json_schema_validators['jsd_d388e26255a15233ac682c0406880cfb_v3_0_0'] =\
                JSONSchemaValidatorD388E26255A15233Ac682C0406880Cfb_v3_0_0()
            self.json_schema_validators['jsd_d43fec9e7dc556cbb9bf0ebd1dcd6aad_v3_0_0'] =\
                JSONSchemaValidatorD43Fec9E7Dc556CbB9Bf0Ebd1Dcd6Aad_v3_0_0()
            self.json_schema_validators['jsd_d5572c56526151cb8ea42de44b2db52c_v3_0_0'] =\
                JSONSchemaValidatorD5572C56526151Cb8Ea42De44B2Db52C_v3_0_0()
            self.json_schema_validators['jsd_d810359e31e453ac8145981b7d5bb7e4_v3_0_0'] =\
                JSONSchemaValidatorD810359E31E453Ac8145981B7D5Bb7E4_v3_0_0()
            self.json_schema_validators['jsd_d82fe0f9e4635b74af809beaaf98bd07_v3_0_0'] =\
                JSONSchemaValidatorD82Fe0F9E4635B74Af809Beaaf98Bd07_v3_0_0()
            self.json_schema_validators['jsd_d8e470a4ef6a58b3b21f9adbbdcc7a46_v3_0_0'] =\
                JSONSchemaValidatorD8E470A4Ef6A58B3B21F9Adbbdcc7A46_v3_0_0()
            self.json_schema_validators['jsd_d912b1c21e2b5dca8b56332d3a8ad13d_v3_0_0'] =\
                JSONSchemaValidatorD912B1C21E2B5Dca8B56332D3A8Ad13D_v3_0_0()
            self.json_schema_validators['jsd_d9ddc2557a495493bca08b8b973601aa_v3_0_0'] =\
                JSONSchemaValidatorD9Ddc2557A495493Bca08B8B973601Aa_v3_0_0()
            self.json_schema_validators['jsd_db686413cf4558188ea60ccc05c3e920_v3_0_0'] =\
                JSONSchemaValidatorDb686413Cf4558188Ea60Ccc05C3E920_v3_0_0()
            self.json_schema_validators['jsd_dd6c2553ae0053c1bbbdbd46c1df0ef9_v3_0_0'] =\
                JSONSchemaValidatorDd6C2553Ae0053C1BbbdBd46C1Df0Ef9_v3_0_0()
            self.json_schema_validators['jsd_ded7f8573c255c318bb1f04bfdbf01e1_v3_0_0'] =\
                JSONSchemaValidatorDed7F8573C255C318Bb1F04Bfdbf01E1_v3_0_0()
            self.json_schema_validators['jsd_dfa8f48210e85715beebb44e62fac408_v3_0_0'] =\
                JSONSchemaValidatorDfa8F48210E85715BeebB44E62Fac408_v3_0_0()
            self.json_schema_validators['jsd_dfae2409eecc551298e9fa31d14f43d0_v3_0_0'] =\
                JSONSchemaValidatorDfae2409Eecc551298E9Fa31D14F43D0_v3_0_0()
            self.json_schema_validators['jsd_e1d938f110e059a5abcb9cc8fb3cbd7c_v3_0_0'] =\
                JSONSchemaValidatorE1D938F110E059A5Abcb9Cc8Fb3Cbd7C_v3_0_0()
            self.json_schema_validators['jsd_e2a697abfe2058d3adc7ad9922f5a5d6_v3_0_0'] =\
                JSONSchemaValidatorE2A697AbFe2058D3Adc7Ad9922F5A5D6_v3_0_0()
            self.json_schema_validators['jsd_e2c930d3d75859b8b7d30e79f3eab084_v3_0_0'] =\
                JSONSchemaValidatorE2C930D3D75859B8B7D30E79F3Eab084_v3_0_0()
            self.json_schema_validators['jsd_e39868ea7aec5efcaaf55009699eda5d_v3_0_0'] =\
                JSONSchemaValidatorE39868Ea7Aec5EfcAaf55009699Eda5D_v3_0_0()
            self.json_schema_validators['jsd_e405a20316825460a1f37a2f161e7ac5_v3_0_0'] =\
                JSONSchemaValidatorE405A20316825460A1F37A2F161E7Ac5_v3_0_0()
            self.json_schema_validators['jsd_e56dd3caaf62589f9e827d03e8427467_v3_0_0'] =\
                JSONSchemaValidatorE56Dd3CaAf62589F9E827D03E8427467_v3_0_0()
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
            self.json_schema_validators['jsd_ea5b356b4bc053068a0052b6c807d286_v3_0_0'] =\
                JSONSchemaValidatorEa5B356B4Bc053068A0052B6C807D286_v3_0_0()
            self.json_schema_validators['jsd_ea5e5a095d05598db7b99ddfd1d7f7fa_v3_0_0'] =\
                JSONSchemaValidatorEa5E5A095D05598DB7B99Ddfd1D7F7Fa_v3_0_0()
            self.json_schema_validators['jsd_ea658190e73c5ce1b27e7def4aea28e3_v3_0_0'] =\
                JSONSchemaValidatorEa658190E73C5Ce1B27E7Def4Aea28E3_v3_0_0()
            self.json_schema_validators['jsd_eaa0d7c339d152b688876c2e10f51fe7_v3_0_0'] =\
                JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7_v3_0_0()
            self.json_schema_validators['jsd_eb8e0ce63376573995a49178435f7747_v3_0_0'] =\
                JSONSchemaValidatorEb8E0Ce63376573995A49178435F7747_v3_0_0()
            self.json_schema_validators['jsd_ec26ec11d92356a594a6efa55ccb9be7_v3_0_0'] =\
                JSONSchemaValidatorEc26Ec11D92356A594A6Efa55Ccb9Be7_v3_0_0()
            self.json_schema_validators['jsd_ecff2eb67fe5591f8d9026f928a0d8aa_v3_0_0'] =\
                JSONSchemaValidatorEcff2Eb67Fe5591F8D9026F928A0D8Aa_v3_0_0()
            self.json_schema_validators['jsd_ed1ef503c091506aa8e446182e625365_v3_0_0'] =\
                JSONSchemaValidatorEd1Ef503C091506AA8E446182E625365_v3_0_0()
            self.json_schema_validators['jsd_f1196f1f6fde5978b0522f096926d443_v3_0_0'] =\
                JSONSchemaValidatorF1196F1F6Fde5978B0522F096926D443_v3_0_0()
            self.json_schema_validators['jsd_f16d14057660520dba53cc0df60db4a8_v3_0_0'] =\
                JSONSchemaValidatorF16D14057660520DBa53Cc0Df60Db4A8_v3_0_0()
            self.json_schema_validators['jsd_f1b8eaf23e795f1a8525eb5905187aa9_v3_0_0'] =\
                JSONSchemaValidatorF1B8Eaf23E795F1A8525Eb5905187Aa9_v3_0_0()
            self.json_schema_validators['jsd_f1ff2b82953f5131884f0779db37190c_v3_0_0'] =\
                JSONSchemaValidatorF1Ff2B82953F5131884F0779Db37190C_v3_0_0()
            self.json_schema_validators['jsd_f2b0a67d389a592dba005895594b77cc_v3_0_0'] =\
                JSONSchemaValidatorF2B0A67D389A592DBa005895594B77Cc_v3_0_0()
            self.json_schema_validators['jsd_f3b45b8e4089574c9912407f88b1a5d2_v3_0_0'] =\
                JSONSchemaValidatorF3B45B8E4089574C9912407F88B1A5D2_v3_0_0()
            self.json_schema_validators['jsd_f41d844dbee15f7680920652004f69b6_v3_0_0'] =\
                JSONSchemaValidatorF41D844DBee15F7680920652004F69B6_v3_0_0()
            self.json_schema_validators['jsd_f41f77362663580d8cc3e6e88623889d_v3_0_0'] =\
                JSONSchemaValidatorF41F77362663580D8Cc3E6E88623889D_v3_0_0()
            self.json_schema_validators['jsd_f4dbfb874b3b56d7a651d6732f1bd55e_v3_0_0'] =\
                JSONSchemaValidatorF4Dbfb874B3B56D7A651D6732F1Bd55E_v3_0_0()
            self.json_schema_validators['jsd_f68aee0cdb425390b3ca90b0b46e6e2c_v3_0_0'] =\
                JSONSchemaValidatorF68Aee0CDb425390B3Ca90B0B46E6E2C_v3_0_0()
            self.json_schema_validators['jsd_f79ab23563d857e58e01a74e37333572_v3_0_0'] =\
                JSONSchemaValidatorF79Ab23563D857E58E01A74E37333572_v3_0_0()
            self.json_schema_validators['jsd_f831d9ed2beb5c2b967aa10db8c22046_v3_0_0'] =\
                JSONSchemaValidatorF831D9Ed2Beb5C2B967AA10Db8C22046_v3_0_0()
            self.json_schema_validators['jsd_f8a2f0834e625822bed1cb4cf34fde5e_v3_0_0'] =\
                JSONSchemaValidatorF8A2F0834E625822Bed1Cb4Cf34Fde5E_v3_0_0()
            self.json_schema_validators['jsd_f92e61297eb05379bd9b92bc60735912_v3_0_0'] =\
                JSONSchemaValidatorF92E61297Eb05379Bd9B92Bc60735912_v3_0_0()
            self.json_schema_validators['jsd_f9c9a5e917af53dbbb91733e82e72ebe_v3_0_0'] =\
                JSONSchemaValidatorF9C9A5E917Af53DbBb91733E82E72Ebe_v3_0_0()
            self.json_schema_validators['jsd_fa838e78175e51b4bcfb0821c19b81b7_v3_0_0'] =\
                JSONSchemaValidatorFa838E78175E51B4Bcfb0821C19B81B7_v3_0_0()
            self.json_schema_validators['jsd_fc9a4ee495785518bd2251b6b4fb41f4_v3_0_0'] =\
                JSONSchemaValidatorFc9A4Ee495785518Bd2251B6B4Fb41F4_v3_0_0()
            self.json_schema_validators['jsd_fc9ecf1e469154ae845236dbed070904_v3_0_0'] =\
                JSONSchemaValidatorFc9Ecf1E469154Ae845236Dbed070904_v3_0_0()
            self.json_schema_validators['jsd_fcf7754d5b45523a8227d37c476a1880_v3_0_0'] =\
                JSONSchemaValidatorFcf7754D5B45523A8227D37C476A1880_v3_0_0()
            self.json_schema_validators['jsd_fd4b5a56f8bd5f8f919e9fffc172e72f_v3_0_0'] =\
                JSONSchemaValidatorFd4B5A56F8Bd5F8F919E9Fffc172E72F_v3_0_0()
            self.json_schema_validators['jsd_fe54c96ccba65af1abe3cd08f4fc69cb_v3_0_0'] =\
                JSONSchemaValidatorFe54C96CCba65Af1Abe3Cd08F4Fc69Cb_v3_0_0()
            self.json_schema_validators['jsd_feb30ca768795eed82c118d009d7bcd4_v3_0_0'] =\
                JSONSchemaValidatorFeb30Ca768795Eed82C118D009D7Bcd4_v3_0_0()
            self.json_schema_validators['jsd_ff0055f9ef115a42bea6ffdd8e57d41b_v3_0_0'] =\
                JSONSchemaValidatorFf0055F9Ef115A42Bea6Ffdd8E57D41B_v3_0_0()
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
