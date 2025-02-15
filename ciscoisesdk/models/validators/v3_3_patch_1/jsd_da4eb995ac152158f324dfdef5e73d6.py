# -*- coding: utf-8 -*-
"""Identity Services Engine patchAllowedprotocolsId data model.

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


from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema
from ciscoisesdk.exceptions import MalformedRequest


class JSONSchemaValidatorDa4Eb995Ac152158F324Dfdef5E73D6(object):
    """patchAllowedprotocolsId request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDa4Eb995Ac152158F324Dfdef5E73D6, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "AllowedProtocols": {
                "properties": {
                "allowChap": {
                "type": "boolean"
                },
                "allowEapFast": {
                "type": "boolean"
                },
                "allowEapMd5": {
                "type": "boolean"
                },
                "allowEapTls": {
                "type": "boolean"
                },
                "allowEapTtls": {
                "type": "boolean"
                },
                "allowLeap": {
                "type": "boolean"
                },
                "allowMsChapV1": {
                "type": "boolean"
                },
                "allowMsChapV2": {
                "type": "boolean"
                },
                "allowPapAscii": {
                "type": "boolean"
                },
                "allowPeap": {
                "type": "boolean"
                },
                "allowPreferredEapProtocol": {
                "type": "boolean"
                },
                "allowTeap": {
                "type": "boolean"
                },
                "allowWeakCiphersForEap": {
                "type": "boolean"
                },
                "description":
                 {
                "type": "string"
                },
                "eapFast": {
                "properties": {
                "allowEapFastEapGtc": {
                "type": "boolean"
                },
                "allowEapFastEapGtcPwdChange": {
                "type": "boolean"
                },
                "allowEapFastEapGtcPwdChangeRetries": {
                "type": "object"
                },
                "allowEapFastEapMsChapV2": {
                "type": "boolean"
                },
                "allowEapFastEapMsChapV2PwdChange": {
                "type": "boolean"
                },
                "allowEapFastEapMsChapV2PwdChangeRetries": {
                "type": "object"
                },
                "allowEapFastEapTls": {
                "type": "boolean"
                },
                "allowEapFastEapTlsAuthOfExpiredCerts": {
                "type": "boolean"
                },
                "eapFastDontUsePacsAcceptClientCert": {
                "type": "boolean"
                },
                "eapFastDontUsePacsAllowMachineAuthentication": {
                "type": "boolean"
                },
                "eapFastEnableEAPChaining": {
                "type": "boolean"
                },
                "eapFastUsePacs": {
                "type": "boolean"
                },
                "eapFastUsePacsAcceptClientCert": {
                "type": "boolean"
                },
                "eapFastUsePacsAllowAnonymProvisioning": {
                "type": "boolean"
                },
                "eapFastUsePacsAllowAuthenProvisioning": {
                "type": "boolean"
                },
                "eapFastUsePacsAllowMachineAuthentication": {
                "type": "boolean"
                },
                "eapFastUsePacsAuthorizationPacTtl": {
                "type": "object"
                },
                "eapFastUsePacsAuthorizationPacTtlUnits": {
                "type": "string"
                },
                "eapFastUsePacsMachinePacTtl": {
                "type": "object"
                },
                "eapFastUsePacsMachinePacTtlUnits": {
                "type": "string"
                },
                "eapFastUsePacsServerReturns": {
                "type": "boolean"
                },
                "eapFastUsePacsStatelessSessionResume": {
                "type": "boolean"
                },
                "eapFastUsePacsTunnelPacTtl": {
                "type": "object"
                },
                "eapFastUsePacsTunnelPacTtlUnits": {
                "type": "string"
                },
                "eapFastUsePacsUseProactivePacUpdatePrecentage": {
                "type": "object"
                }
                }
                },
                "eapTls": {
                "properties": {
                "allowEapTlsAuthOfExpiredCerts": {
                "type": "boolean"
                },
                "eapTlsEnableStatelessSessionResume": {
                "type": "boolean"
                },
                "eapTlsSessionTicketPrecentage": {
                "type": "object"
                },
                "eapTlsSessionTicketTtl": {
                "type": "object"
                },
                "eapTlsSessionTicketTtlUnits": {
                "type": "object"
                }
                }
                },
                "eapTlsLBit": {
                "type": "boolean"
                },
                "eapTtls": {
                "properties": {
                "eapTtlsChap": {
                "type": "boolean"
                },
                "eapTtlsEapMd5": {
                "type": "boolean"
                },
                "eapTtlsEapMsChapV2": {
                "type": "boolean"
                },
                "eapTtlsEapMsChapV2PwdChange": {
                "type": "boolean"
                },
                "eapTtlsEapMsChapV2PwdChangeRetries": {
                "type": "object"
                },
                "eapTtlsMsChapV1": {
                "type": "boolean"
                },
                "eapTtlsMsChapV2": {
                "type": "boolean"
                },
                "eapTtlsPapAscii": {
                "type": "boolean"
                }
                }
                },
                "fiveG": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "peap": {
                "properties": {
                "allowPeapEapGtc": {
                "type": "boolean"
                },
                "allowPeapEapGtcPwdChange": {
                "type": "boolean"
                },
                "allowPeapEapGtcPwdChangeRetries": {
                "type": "object"
                },
                "allowPeapEapMsChapV2": {
                "type": "boolean"
                },
                "allowPeapEapMsChapV2PwdChange": {
                "type": "boolean"
                },
                "allowPeapEapMsChapV2PwdChangeRetries": {
                "type": "object"
                },
                "allowPeapEapTls": {
                "type": "boolean"
                },
                "allowPeapEapTlsAuthOfExpiredCerts": {
                "type": "boolean"
                },
                "allowPeapV0": {
                "type": "boolean"
                },
                "requireCryptobinding": {
                "type": "boolean"
                }
                }
                },
                "preferredEapProtocol": {
                "type": "string"
                },
                "processHostLookup": {
                "type": "boolean"
                },
                "requireMessageAuth": {
                "type": "boolean"
                },
                "rsaPss": {
                "type": "boolean"
                },
                "teap": {
                "properties": {
                "acceptClientCertDuringTunnelEst": {
                "type": "boolean"
                },
                "allowDowngradeMsk": {
                "type": "boolean"
                },
                "allowTeapEapMsChapV2": {
                "type": "boolean"
                },
                "allowTeapEapMsChapV2PwdChange": {
                "type": "boolean"
                },
                "allowTeapEapMsChapV2PwdChangeRetries": {
                "type": "object"
                },
                "allowTeapEapTls": {
                "type": "boolean"
                },
                "allowTeapEapTlsAuthOfExpiredCerts": {
                "type": "boolean"
                },
                "enableEapChaining": {
                "type": "boolean"
                }
                }
                }
                }
                }
                },
                "required": [
                "AllowedProtocols"
                ],
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
