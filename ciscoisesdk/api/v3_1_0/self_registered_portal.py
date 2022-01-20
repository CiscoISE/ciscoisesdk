# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SelfRegisteredPortal API wrapper.

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

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)
from ...pagination import get_next_page


class SelfRegisteredPortal(object):
    """Identity Services Engine SelfRegisteredPortal API (version: 3.1.0).

    Wraps the Identity Services Engine SelfRegisteredPortal
    API and exposes the API as native Python
    methods that return native Python objects.
    Self Registered Guest Portal API provides the ability to create, read,
    update, delete and search self registered portals.

    Revision History
    ----------------

    +----------------+----------------+----------------+----------------+
    | **Revision #** | **Resource     | **Cisco ISE    | *              |
    |                | Version**      | Version**      | *Description** |
    +----------------+----------------+----------------+----------------+
    | 0              | 1.0            | 2.2            | Initial Cisco  |
    |                |                |                | ISE Version    |
    +----------------+----------------+----------------+----------------+

    |

    Resource Definition
    -------------------

    +-----------+-----------+-----------+-----------+-----------+-----------+
    | **At      | **Type**  | **R       | **Desc    | **Default | **Example |
    | tribute** |           | equired** | ription** | Values**  | Values**  |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | name      | String    | Yes       | Resource  |           | Self-R    |
    |           |           |           | Name      |           | egistered |
    |           |           |           |           |           | Guest     |
    |           |           |           |           |           | Portal    |
    |           |           |           |           |           | (default) |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | id        | String    | No        | Resource  |           | 4e8ade36- |
    |           |           |           | UUID,     |           | 4048-472a |
    |           |           |           | mandatory |           | -b345-632 |
    |           |           |           | for       |           | cc155acfc |
    |           |           |           | update    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | de        | String    | No        |           |           | Guests    |
    | scription |           |           |           |           | may       |
    |           |           |           |           |           | create    |
    |           |           |           |           |           | their own |
    |           |           |           |           |           | accounts  |
    |           |           |           |           |           | and be    |
    |           |           |           |           |           | assigned  |
    |           |           |           |           |           | a         |
    |           |           |           |           |           | username  |
    |           |           |           |           |           | and       |
    |           |           |           |           |           | password, |
    |           |           |           |           |           | or use    |
    |           |           |           |           |           | their     |
    |           |           |           |           |           | social    |
    |           |           |           |           |           | login to  |
    |           |           |           |           |           | access    |
    |           |           |           |           |           | the       |
    |           |           |           |           |           | network   |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | port      | String    | No        | URL to    |           | h         |
    | alTestUrl |           |           | bring up  |           | ttps://{i |
    |           |           |           | a test    |           | se-ip}:84 |
    |           |           |           | page for  |           | 43/portal |
    |           |           |           | this      |           | /PortalSe |
    |           |           |           | portal    |           | tup.actio |
    |           |           |           |           |           | n?portal= |
    |           |           |           |           |           | 4e8ade36- |
    |           |           |           |           |           | 4048-472a |
    |           |           |           |           |           | -b345-632 |
    |           |           |           |           |           | cc155acfc |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | p         | Enum      | Yes       | Allowed   | SEL       |           |
    | ortalType |           |           | values:   | FREGGUEST |           |
    |           |           |           | - BYOD,   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | HOTS      |           |           |
    |           |           |           | POTGUEST, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | MYDEVICE, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | SELF      |           |           |
    |           |           |           | REGGUEST, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | SPONSOR,  |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | SPONS     |           |           |
    |           |           |           | OREDGUEST |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | settings  | List      | No        | Defines   |           |           |
    |           |           |           | all of    |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | settings  |           |           |
    |           |           |           | groups    |           |           |
    |           |           |           | available |           |           |
    |           |           |           | for a     |           |           |
    |           |           |           | portal    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | The port, |           |           |
    | porta     |           |           | i         |           |           |
    | lSettings |           |           | nterface, |           |           |
    |           |           |           | cer       |           |           |
    |           |           |           | tificate, |           |           |
    |           |           |           | and other |           |           |
    |           |           |           | basic     |           |           |
    |           |           |           | settings  |           |           |
    |           |           |           | of a      |           |           |
    |           |           |           | portal    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | Yes       | The port  |           | 8443      |
    | httpsPort |           |           | number    |           |           |
    |           |           |           | that the  |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | nterfaces |           |           |
    |           |           |           | will      |           |           |
    |           |           |           | listen    |           |           |
    |           |           |           | on. Range |           |           |
    |           |           |           | from 8000 |           |           |
    |           |           |           | to 8999   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | Yes       | I         |           | [ "eth0", |
    | allowedI  |           |           | nterfaces |           | "bond0" ] |
    | nterfaces |           |           | that the  |           |           |
    |           |           |           | portal    |           |           |
    |           |           |           | will be   |           |           |
    |           |           |           | reachable |           |           |
    |           |           |           | on.       |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | - eth0,   |           |           |
    |           |           |           | - eth1,   |           |           |
    |           |           |           | - eth2,   |           |           |
    |           |           |           | - eth3,   |           |           |
    |           |           |           | - eth4,   |           |           |
    |           |           |           | - eth5,   |           |           |
    |           |           |           | - bond0,  |           |           |
    |           |           |           | - bond1,  |           |           |
    |           |           |           | - bond2   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Logical   |           | Default   |
    | c         |           |           | name of   |           | Portal    |
    | ertificat |           |           | the x.509 |           | Ce        |
    | eGroupTag |           |           | server    |           | rtificate |
    |           |           |           | ce        |           | Group     |
    |           |           |           | rtificate |           |           |
    |           |           |           | that will |           |           |
    |           |           |           | be used   |           |           |
    |           |           |           | for the   |           |           |
    |           |           |           | portal    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Unique Id |           | 92e50f80- |
    | au        |           |           | of the    |           | 8c01-11e6 |
    | thenticat |           |           | identity  |           | -996c-525 |
    | ionMethod |           |           | source    |           | 400b48521 |
    |           |           |           | sequence  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Unique Id |           | C         |
    | a         |           |           | of a      |           | ontractor |
    | ssignedGu |           |           | guest     |           | (default) |
    | estTypeFo |           |           | type.     |           |           |
    | rEmployee |           |           | Employees |           |           |
    |           |           |           | using     |           |           |
    |           |           |           | this      |           |           |
    |           |           |           | portal as |           |           |
    |           |           |           | a guest   |           |           |
    |           |           |           | inherit   |           |           |
    |           |           |           | login     |           |           |
    |           |           |           | options   |           |           |
    |           |           |           | from the  |           |           |
    |           |           |           | guest     |           |           |
    |           |           |           | type      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | Allowed   |           | USEBROW   |
    | di        |           |           | values:   |           | SERLOCALE |
    | splayLang |           |           | -         |           |           |
    |           |           |           | USEBROWS  |           |           |
    |           |           |           | ERLOCALE, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | ALWAYSUSE |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | Used when |           | English   |
    | fallbac   |           |           | di        |           |           |
    | kLanguage |           |           | splayLang |           |           |
    |           |           |           | =         |           |           |
    |           |           |           | USEBROW   |           |           |
    |           |           |           | SERLOCALE |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | Used when |           | English   |
    | alwaysUse |           |           | di        |           |           |
    | dLanguage |           |           | splayLang |           |           |
    |           |           |           | =         |           |           |
    |           |           |           | ALWAYSUSE |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Portal    |           |           |
    | loginPag  |           |           | Login     |           |           |
    | eSettings |           |           | Page      |           |           |
    |           |           |           | settings  |           |           |
    |           |           |           | groups    |           |           |
    |           |           |           | follow    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | No        | Maximum   | 5         |           |
    | maxFa     |           |           | failed    |           |           |
    | iledAttem |           |           | login     |           |           |
    | ptsBefore |           |           | attempts  |           |           |
    | RateLimit |           |           | before    |           |           |
    |           |           |           | rate      |           |           |
    |           |           |           | limiting  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | No        | Time      | 2         |           |
    | timeB     |           |           | between   |           |           |
    | etweenLog |           |           | login     |           |           |
    | insDuring |           |           | attempts  |           |           |
    | RateLimit |           |           | when rate |           |           |
    |           |           |           | limiting  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Include   | false     |           |
    | i         |           |           | an        |           |           |
    | ncludeAup |           |           | A         |           |           |
    |           |           |           | cceptable |           |           |
    |           |           |           | Use       |           |           |
    |           |           |           | Policy    |           |           |
    |           |           |           | (AUP)     |           |           |
    |           |           |           | that      |           |           |
    |           |           |           | should be |           |           |
    |           |           |           | displayed |           |           |
    |           |           |           | during    |           |           |
    |           |           |           | login     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | How the   | ASLINK    |           |
    | a         |           |           | AUP       |           |           |
    | upDisplay |           |           | should be |           |           |
    |           |           |           | d         |           |           |
    |           |           |           | isplayed, |           |           |
    |           |           |           | either on |           |           |
    |           |           |           | page or   |           |           |
    |           |           |           | as a      |           |           |
    |           |           |           | link.     |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | ncludeAup |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | - ONPAGE, |           |           |
    |           |           |           | - ASLINK  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Require   | false     |           |
    | re        |           |           | the       |           |           |
    | quireAupA |           |           | portal    |           |           |
    | cceptance |           |           | user to   |           |           |
    |           |           |           | accept    |           |           |
    |           |           |           | the AUP.  |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | ncludeAup |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Require   | false     |           |
    | requireA  |           |           | the       |           |           |
    | ccessCode |           |           | portal    |           |           |
    |           |           |           | user to   |           |           |
    |           |           |           | enter an  |           |           |
    |           |           |           | access    |           |           |
    |           |           |           | code      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | Access    |           |           |
    | a         |           |           | code that |           |           |
    | ccessCode |           |           | must be   |           |           |
    |           |           |           | entered   |           |           |
    |           |           |           | by the    |           |           |
    |           |           |           | portal    |           |           |
    |           |           |           | user      |           |           |
    |           |           |           | (only     |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | requireA  |           |           |
    |           |           |           | ccessCode |           |           |
    |           |           |           | = true)   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | allowGue  |           |           |           |           |           |
    | stToCreat |           |           |           |           |           |
    | eAccounts |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Require   | false     |           |
    | allowGue  |           |           | the       |           |           |
    | stToChang |           |           | portal    |           |           |
    | ePassword |           |           | user to   |           |           |
    |           |           |           | enter an  |           |           |
    |           |           |           | access    |           |           |
    |           |           |           | code      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           |           | false     |
    | allowAl   |           |           |           |           |           |
    | ternateGu |           |           |           |           |           |
    | estPortal |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           |           |
    | al        |           |           |           |           |           |
    | ternateGu |           |           |           |           |           |
    | estPortal |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        |           |           |           |
    | s         |           |           |           |           |           |
    | elfRegPag |           |           |           |           |           |
    | eSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | Guests    |           |           |
    | assig     |           |           | are       |           |           |
    | nGuestsTo |           |           | assigned  |           |           |
    | GuestType |           |           | to this   |           |           |
    |           |           |           | guest     |           |           |
    |           |           |           | type      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | No        | Self-r    | 1         |           |
    | accou     |           |           | egistered |           |           |
    | ntValidit |           |           | guest     |           |           |
    | yDuration |           |           | account   |           |           |
    |           |           |           | is valid  |           |           |
    |           |           |           | for this  |           |           |
    |           |           |           | many      |           |           |
    |           |           |           | account_v |           |           |
    |           |           |           | alidity_t |           |           |
    |           |           |           | ime_units |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | Time      | DAYS      |           |
    | accoun    |           |           | units for |           |           |
    | tValidity |           |           | account_  |           |           |
    | TimeUnits |           |           | validity_ |           |           |
    |           |           |           | duration. |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | Values:   |           |           |
    |           |           |           | - DAYS,   |           |           |
    |           |           |           | - HOURS,  |           |           |
    |           |           |           | - MINUTES |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Self-r    | false     |           |
    | requi     |           |           | egistered |           |           |
    | reRegistr |           |           | guests    |           |           |
    | ationCode |           |           | are       |           |           |
    |           |           |           | required  |           |           |
    |           |           |           | to enter  |           |           |
    |           |           |           | a         |           |           |
    |           |           |           | reg       |           |           |
    |           |           |           | istration |           |           |
    |           |           |           | code      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | The       |           |           |
    | registr   |           |           | reg       |           |           |
    | ationCode |           |           | istration |           |           |
    |           |           |           | code that |           |           |
    |           |           |           | the guest |           |           |
    |           |           |           | user must |           |           |
    |           |           |           | enter     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | fiel      |           |           |           |           |           |
    | dUserName |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | field     |           |           |           |           |           |
    | FirstName |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | fiel      |           |           |           |           |           |
    | dLastName |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | field     |           |           |           |           |           |
    | EmailAddr |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | fie       |           |           |           |           |           |
    | ldPhoneNo |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | fie       |           |           |           |           |           |
    | ldCompany |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | fiel      |           |           |           |           |           |
    | dLocation |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | Guests    |           | ["San     |
    | s         |           |           | can       |           | Jose"]    |
    | electable |           |           | choose    |           |           |
    | Locations |           |           | from      |           |           |
    |           |           |           | these     |           |           |
    |           |           |           | locations |           |           |
    |           |           |           | to set    |           |           |
    |           |           |           | their     |           |           |
    |           |           |           | time zone |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | fieldSm   |           |           |           |           |           |
    | sProvider |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | This      |           | ["Global  |
    | sele      |           |           | attribute |           | Default"] |
    | ctableSms |           |           | is an     |           |           |
    | Providers |           |           | array of  |           |           |
    |           |           |           | SMS       |           |           |
    |           |           |           | provider  |           |           |
    |           |           |           | names     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | field     |           |           |           |           |           |
    | PersonBei |           |           |           |           |           |
    | ngVisited |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        |           |           |           |
    | f         |           |           |           |           |           |
    | ieldReaso |           |           |           |           |           |
    | nForVisit |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           |           | true      |
    | include   |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Only      |           | false     |
    | require   |           |           | a         |           |           |
    |           |           |           | pplicable |           |           |
    |           |           |           | if        |           |           |
    |           |           |           | include = |           |           |
    |           |           |           | true      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Include   | false     |           |
    | i         |           |           | an        |           |           |
    | ncludeAup |           |           | A         |           |           |
    |           |           |           | cceptable |           |           |
    |           |           |           | Use       |           |           |
    |           |           |           | Policy    |           |           |
    |           |           |           | (AUP)     |           |           |
    |           |           |           | that      |           |           |
    |           |           |           | should be |           |           |
    |           |           |           | displayed |           |           |
    |           |           |           | during    |           |           |
    |           |           |           | login     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | How the   | ASLINK    |           |
    | a         |           |           | AUP       |           |           |
    | upDisplay |           |           | should be |           |           |
    |           |           |           | d         |           |           |
    |           |           |           | isplayed, |           |           |
    |           |           |           | either on |           |           |
    |           |           |           | page or   |           |           |
    |           |           |           | as a      |           |           |
    |           |           |           | link.     |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | ncludeAup |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | - ONPAGE, |           |           |
    |           |           |           | - ASLINK  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Require   | false     |           |
    | re        |           |           | the       |           |           |
    | quireAupA |           |           | portal    |           |           |
    | cceptance |           |           | user to   |           |           |
    |           |           |           | accept    |           |           |
    |           |           |           | the AUP.  |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | ncludeAup |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Allow     | false     |           |
    | enableG   |           |           | guests    |           |           |
    | uestEmail |           |           | with an   |           |           |
    | Whitelist |           |           | e-mail    |           |           |
    |           |           |           | address   |           |           |
    |           |           |           | from      |           |           |
    |           |           |           | selected  |           |           |
    |           |           |           | domains   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | Self-r    |           |           |
    | guestEma  |           |           | egistered |           |           |
    | ilWhiteli |           |           | guests    |           |           |
    | stDomains |           |           | whose     |           |           |
    |           |           |           | e-mail    |           |           |
    |           |           |           | address   |           |           |
    |           |           |           | is in one |           |           |
    |           |           |           | of these  |           |           |
    |           |           |           | domains   |           |           |
    |           |           |           | will be   |           |           |
    |           |           |           | allowed.  |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | enableG   |           |           |
    |           |           |           | uestEmail |           |           |
    |           |           |           | Whitelist |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Disallow  | false     |           |
    | enableG   |           |           | guests    |           |           |
    | uestEmail |           |           | with an   |           |           |
    | Blacklist |           |           | e-mail    |           |           |
    |           |           |           | address   |           |           |
    |           |           |           | from      |           |           |
    |           |           |           | selected  |           |           |
    |           |           |           | domains   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | Self-r    |           |           |
    | guestEma  |           |           | egistered |           |           |
    | ilBlackli |           |           | guests    |           |           |
    | stDomains |           |           | whose     |           |           |
    |           |           |           | e-mail    |           |           |
    |           |           |           | address   |           |           |
    |           |           |           | is in one |           |           |
    |           |           |           | of these  |           |           |
    |           |           |           | domains   |           |           |
    |           |           |           | will be   |           |           |
    |           |           |           | di        |           |           |
    |           |           |           | sallowed. |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | enableG   |           |           |
    |           |           |           | uestEmail |           |           |
    |           |           |           | Blacklist |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Require   | false     |           |
    | re        |           |           | self-r    |           |           |
    | quireGues |           |           | egistered |           |           |
    | tApproval |           |           | guests to |           |           |
    |           |           |           | be        |           |           |
    |           |           |           | approved  |           |           |
    |           |           |           | if true   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Allow     | false     |           |
    | autoLogi  |           |           | guests to |           |           |
    | nSelfWait |           |           | login     |           |           |
    |           |           |           | auto      |           |           |
    |           |           |           | matically |           |           |
    |           |           |           | from      |           |           |
    |           |           |           | self-reg  |           |           |
    |           |           |           | istration |           |           |
    |           |           |           | after     |           |           |
    |           |           |           | sponsor's |           |           |
    |           |           |           | approval. |           |           |
    |           |           |           | No need   |           |           |
    |           |           |           | to        |           |           |
    |           |           |           | provide   |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | cr        |           |           |
    |           |           |           | edentials |           |           |
    |           |           |           | by guest  |           |           |
    |           |           |           | to login  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | No        | Waiting   | 5         |           |
    | a         |           |           | period    |           |           |
    | utoLoginT |           |           | for auto  |           |           |
    | imePeriod |           |           | login     |           |           |
    |           |           |           | until     |           |           |
    |           |           |           | sponsor's |           |           |
    |           |           |           | approval. |           |           |
    |           |           |           | If time   |           |           |
    |           |           |           | exceeds,  |           |           |
    |           |           |           | guest has |           |           |
    |           |           |           | to login  |           |           |
    |           |           |           | manually  |           |           |
    |           |           |           | by        |           |           |
    |           |           |           | providing |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | cre       |           |           |
    |           |           |           | dentials. |           |           |
    |           |           |           | Default   |           |           |
    |           |           |           | value is  |           |           |
    |           |           |           | 5 minutes |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | Specifies | SELE      |           |
    | sen       |           |           | where     | CTEDEMAIL |           |
    | dApproval |           |           | approval  | ADDRESSES |           |
    | RequestTo |           |           | requests  |           |           |
    |           |           |           | are sent. |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | Values:   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | SELEC     |           |           |
    |           |           |           | TEDEMAILA |           |           |
    |           |           |           | DDRESSES, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | PERSONBEI |           |           |
    |           |           |           | NGVISITED |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | Only      |           |           |
    | appr      |           |           | valid if  |           |           |
    | ovalEmail |           |           | re        |           |           |
    | Addresses |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true    |           |           |
    |           |           |           | and       |           |           |
    |           |           |           | sen       |           |           |
    |           |           |           | dApproval |           |           |
    |           |           |           | RequestTo |           |           |
    |           |           |           | =         |           |           |
    |           |           |           | SELE      |           |           |
    |           |           |           | CTEDEMAIL |           |           |
    |           |           |           | ADDRESSES |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | After the | SELFR     |           |
    | postRe    |           |           | reg       | EGISTRATI |           |
    | gistratio |           |           | istration | ONSUCCESS |           |
    | nRedirect |           |           | s         |           |           |
    |           |           |           | ubmission |           |           |
    |           |           |           | direct    |           |           |
    |           |           |           | the guest |           |           |
    |           |           |           | user to   |           |           |
    |           |           |           | one of    |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | following |           |           |
    |           |           |           | pages.    |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | Values:   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | SELFRE    |           |           |
    |           |           |           | GISTRATIO |           |           |
    |           |           |           | NSUCCESS, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | LOGINPA   |           |           |
    |           |           |           | GEWITHINS |           |           |
    |           |           |           | TRUCTIONS |           |           |
    |           |           |           | - URL     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | URL where |           |           |
    | postRegis |           |           | guest     |           |           |
    | trationRe |           |           | user is   |           |           |
    | directUrl |           |           | r         |           |           |
    |           |           |           | edirected |           |           |
    |           |           |           | after     |           |           |
    |           |           |           | regi      |           |           |
    |           |           |           | stration. |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true    |           |           |
    |           |           |           | and       |           |           |
    |           |           |           | postRe    |           |           |
    |           |           |           | gistratio |           |           |
    |           |           |           | nRedirect |           |           |
    |           |           |           | = URL     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | If true,  | false     |           |
    | crede     |           |           | send      |           |           |
    | ntialNoti |           |           | c         |           |           |
    | ficationU |           |           | redential |           |           |
    | singEmail |           |           | not       |           |           |
    |           |           |           | ification |           |           |
    |           |           |           | upon      |           |           |
    |           |           |           | approval  |           |           |
    |           |           |           | using     |           |           |
    |           |           |           | email.    |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | If true,  | false     |           |
    | cre       |           |           | send      |           |           |
    | dentialNo |           |           | c         |           |           |
    | tificatio |           |           | redential |           |           |
    | nUsingSms |           |           | not       |           |           |
    |           |           |           | ification |           |           |
    |           |           |           | upon      |           |           |
    |           |           |           | approval  |           |           |
    |           |           |           | using     |           |           |
    |           |           |           | SMS. Only |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | No        | This      | 1440      |           |
    | approv    |           |           | a         |           |           |
    | eDenyLink |           |           | ttribute, |           |           |
    | sValidFor |           |           | along     |           |           |
    |           |           |           | with      |           |           |
    |           |           |           | approveD  |           |           |
    |           |           |           | enyLinksT |           |           |
    |           |           |           | imeUnits, |           |           |
    |           |           |           | specifies |           |           |
    |           |           |           | how long  |           |           |
    |           |           |           | the link  |           |           |
    |           |           |           | can be    |           |           |
    |           |           |           | used.     |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | This      | DAYS      |           |
    | approve   |           |           | a         |           |           |
    | DenyLinks |           |           | ttribute, |           |           |
    | TimeUnits |           |           | along     |           |           |
    |           |           |           | with      |           |           |
    |           |           |           | approve   |           |           |
    |           |           |           | DenyLinks |           |           |
    |           |           |           | ValidFor, |           |           |
    |           |           |           | specifies |           |           |
    |           |           |           | how long  |           |           |
    |           |           |           | the link  |           |           |
    |           |           |           | can be    |           |           |
    |           |           |           | used.     |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | Values:   |           |           |
    |           |           |           | - DAYS,   |           |           |
    |           |           |           | - HOURS,  |           |           |
    |           |           |           | - MINUTES |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | When      | false     |           |
    | re        |           |           | self-r    |           |           |
    | quireAppr |           |           | egistered |           |           |
    | overToAut |           |           | guests    |           |           |
    | henticate |           |           | require   |           |           |
    |           |           |           | approval, |           |           |
    |           |           |           | an        |           |           |
    |           |           |           | approval  |           |           |
    |           |           |           | request   |           |           |
    |           |           |           | is        |           |           |
    |           |           |           | e-mailed  |           |           |
    |           |           |           | to one or |           |           |
    |           |           |           | more      |           |           |
    |           |           |           | sponsor   |           |           |
    |           |           |           | users. If |           |           |
    |           |           |           | the Cisco |           |           |
    |           |           |           | ISE       |           |           |
    |           |           |           | Admi      |           |           |
    |           |           |           | nistrator |           |           |
    |           |           |           | chooses   |           |           |
    |           |           |           | to        |           |           |
    |           |           |           | include   |           |           |
    |           |           |           | an        |           |           |
    |           |           |           | approval  |           |           |
    |           |           |           | link in   |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | e-mail, a |           |           |
    |           |           |           | sponsor   |           |           |
    |           |           |           | user who  |           |           |
    |           |           |           | clicks    |           |           |
    |           |           |           | the link  |           |           |
    |           |           |           | will be   |           |           |
    |           |           |           | required  |           |           |
    |           |           |           | to enter  |           |           |
    |           |           |           | their     |           |           |
    |           |           |           | username  |           |           |
    |           |           |           | and       |           |           |
    |           |           |           | password  |           |           |
    |           |           |           | if this   |           |           |
    |           |           |           | attribute |           |           |
    |           |           |           | is true.  |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | When      |           |           |
    | sponsorP  |           |           | self-r    |           |           |
    | ortalList |           |           | egistered |           |           |
    |           |           |           | guests    |           |           |
    |           |           |           | require   |           |           |
    |           |           |           | approval, |           |           |
    |           |           |           | an        |           |           |
    |           |           |           | approval  |           |           |
    |           |           |           | request   |           |           |
    |           |           |           | is        |           |           |
    |           |           |           | e-mailed  |           |           |
    |           |           |           | to one or |           |           |
    |           |           |           | more      |           |           |
    |           |           |           | sponsor   |           |           |
    |           |           |           | users. If |           |           |
    |           |           |           | the Cisco |           |           |
    |           |           |           | ISE       |           |           |
    |           |           |           | Admi      |           |           |
    |           |           |           | nistrator |           |           |
    |           |           |           | chooses   |           |           |
    |           |           |           | to        |           |           |
    |           |           |           | include   |           |           |
    |           |           |           | an        |           |           |
    |           |           |           | approval  |           |           |
    |           |           |           | link in   |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | e-mail, a |           |           |
    |           |           |           | sponsor   |           |           |
    |           |           |           | user who  |           |           |
    |           |           |           | clicks    |           |           |
    |           |           |           | the link  |           |           |
    |           |           |           | will be   |           |           |
    |           |           |           | auth      |           |           |
    |           |           |           | enticated |           |           |
    |           |           |           | against   |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | selected  |           |           |
    |           |           |           | sponsor   |           |           |
    |           |           |           | portals   |           |           |
    |           |           |           | in the    |           |           |
    |           |           |           | order     |           |           |
    |           |           |           | s         |           |           |
    |           |           |           | pecified. |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireGues |           |           |
    |           |           |           | tApproval |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | The array |           |           |
    |           |           |           | should    |           |           |
    |           |           |           | contain   |           |           |
    |           |           |           | the names |           |           |
    |           |           |           | of the    |           |           |
    |           |           |           | selected  |           |           |
    |           |           |           | portals   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        |           |           |           |
    | self      |           |           |           |           |           |
    | RegSucces |           |           |           |           |           |
    | sSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | includ    |           |           |           |           |           |
    | eUserName |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | includ    |           |           |           |           |           |
    | ePassword |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | include   |           |           |           |           |           |
    | FirstName |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | includ    |           |           |           |           |           |
    | eLastName |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | include   |           |           |           |           |           |
    | EmailAddr |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | inclu     |           |           |           |           |           |
    | dePhoneNo |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | inclu     |           |           |           |           |           |
    | deCompany |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | includ    |           |           |           |           |           |
    | eLocation |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | includeSm |           |           |           |           |           |
    | sProvider |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | include   |           |           |           |           |           |
    | PersonBei |           |           |           |           |           |
    | ngVisited |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | true      |           |
    | inc       |           |           |           |           |           |
    | ludeReaso |           |           |           |           |           |
    | nForVisit |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | a         |           |           |           |           |           |
    | llowGuest |           |           |           |           |           |
    | SendSelfU |           |           |           |           |           |
    | singPrint |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | a         |           |           |           |           |           |
    | llowGuest |           |           |           |           |           |
    | SendSelfU |           |           |           |           |           |
    | singEmail |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | allowGue  |           |           |           |           |           |
    | stSendSel |           |           |           |           |           |
    | fUsingSms |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | i         |           |           |           |           |           |
    | ncludeAup |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | aupOnPage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | re        |           |           |           |           |           |
    | quireAupA |           |           |           |           |           |
    | cceptance |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | r         |           |           |           |           |           |
    | equireAup |           |           |           |           |           |
    | Scrolling |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | a         |           |           |           |           |           |
    | llowGuest |           |           |           |           |           |
    | LoginFrom |           |           |           |           |           |
    | SelfregSu |           |           |           |           |           |
    | ccessPage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Conf      |           |           |
    | au        |           |           | iguration |           |           |
    | pSettings |           |           | of the    |           |           |
    |           |           |           | A         |           |           |
    |           |           |           | cceptable |           |           |
    |           |           |           | Use       |           |           |
    |           |           |           | Policy    |           |           |
    |           |           |           | (AUP) for |           |           |
    |           |           |           | a portal  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | How the   | F         |           |
    | display   |           |           | AUP       | IRSTLOGIN |           |
    | Frequency |           |           | should be |           |           |
    |           |           |           | d         |           |           |
    |           |           |           | isplayed, |           |           |
    |           |           |           | either on |           |           |
    |           |           |           | page or   |           |           |
    |           |           |           | as a      |           |           |
    |           |           |           | link.     |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | ncludeAup |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | Values:   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | FI        |           |           |
    |           |           |           | RSTLOGIN, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | EV        |           |           |
    |           |           |           | ERYLOGIN, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | RECURRING |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Require   | true      |           |
    | i         |           |           | the       |           |           |
    | ncludeAup |           |           | portal    |           |           |
    |           |           |           | user to   |           |           |
    |           |           |           | read and  |           |           |
    |           |           |           | accept an |           |           |
    |           |           |           | AUP       |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Require   | false     |           |
    | r         |           |           | the       |           |           |
    | equireAup |           |           | portal    |           |           |
    | Scrolling |           |           | user to   |           |           |
    |           |           |           | scroll to |           |           |
    |           |           |           | the end   |           |           |
    |           |           |           | of the    |           |           |
    |           |           |           | AUP. Only |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | quireAupA |           |           |
    |           |           |           | cceptance |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Only      | false     |           |
    | useD      |           |           | valid if  |           |           |
    | iffAupFor |           |           | re        |           |           |
    | Employees |           |           | quireAupA |           |           |
    |           |           |           | cceptance |           |           |
    |           |           |           | = trueG   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Only      | false     |           |
    | s         |           |           | valid if  |           |           |
    | kipAupFor |           |           | re        |           |           |
    | Employees |           |           | quireAupA |           |           |
    |           |           |           | cceptance |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | No        | Number of | 7         |           |
    | d         |           |           | days      |           |           |
    | isplayFre |           |           | between   |           |           |
    | quencyInt |           |           | AUP       |           |           |
    | ervalDays |           |           | conf      |           |           |
    |           |           |           | irmations |           |           |
    |           |           |           | (when     |           |           |
    |           |           |           | display   |           |           |
    |           |           |           | Frequency |           |           |
    |           |           |           | =         |           |           |
    |           |           |           | r         |           |           |
    |           |           |           | ecurring) |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        |           |           |           |
    | GuestChan |           |           |           |           |           |
    | gePasswor |           |           |           |           |           |
    | dSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Allow     | false     |           |
    | al        |           |           | guest to  |           |           |
    | lowChange |           |           | change    |           |           |
    | PasswdAtF |           |           | their own |           |           |
    | irstLogin |           |           | passwords |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        |           |           |           |
    | gues      |           |           |           |           |           |
    | tDeviceRe |           |           |           |           |           |
    | gistratio |           |           |           |           |           |
    | nSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Auto      | true      |           |
    | autoRe    |           |           | matically |           |           |
    | gisterGue |           |           | register  |           |           |
    | stDevices |           |           | guest     |           |           |
    |           |           |           | devices   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Allow     | false     |           |
    | a         |           |           | guests to |           |           |
    | llowGuest |           |           | register  |           |           |
    | sToRegist |           |           | devices   |           |           |
    | erDevices |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Conf      |           |           |
    | byo       |           |           | iguration |           |           |
    | dSettings |           |           | of BYOD   |           |           |
    |           |           |           | Device    |           |           |
    |           |           |           | Welcome,  |           |           |
    |           |           |           | Reg       |           |           |
    |           |           |           | istration |           |           |
    |           |           |           | and       |           |           |
    |           |           |           | Success   |           |           |
    |           |           |           | steps     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | Conf      |           |           |
    | b         |           |           | iguration |           |           |
    | yodWelcom |           |           | of BYOD   |           |           |
    | eSettings |           |           | endpoint  |           |           |
    |           |           |           | welcome   |           |           |
    |           |           |           | step      |           |           |
    |           |           |           | conf      |           |           |
    |           |           |           | iguration |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           | true      |           |
    | e         |           |           |           |           |           |
    | nableBYOD |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           | false     |           |
    | enableGu  |           |           |           |           |           |
    | estAccess |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           | false     |           |
    | r         |           |           |           |           |           |
    | equireMDM |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           | true      |           |
    | i         |           |           |           |           |           |
    | ncludeAup |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Enum      | No        | How the   | ONPAGE    |           |
    | a         |           |           | AUP       |           |           |
    | upDisplay |           |           | should be |           |           |
    |           |           |           | d         |           |           |
    |           |           |           | isplayed, |           |           |
    |           |           |           | either on |           |           |
    |           |           |           | page or   |           |           |
    |           |           |           | as a      |           |           |
    |           |           |           | link.     |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | ncludeAup |           |           |
    |           |           |           | = true.   |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | - ONPAGE, |           |           |
    |           |           |           | - ASLINK  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        |           | false     |           |
    | re        |           |           |           |           |           |
    | quireAupA |           |           |           |           |           |
    | cceptance |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Require   | false     |           |
    | require   |           |           | BYOD      |           |           |
    | Scrolling |           |           | devices   |           |           |
    |           |           |           | to scroll |           |           |
    |           |           |           | down to   |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | bottom of |           |           |
    |           |           |           | the AUP,  |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid if  |           |           |
    |           |           |           | i         |           |           |
    |           |           |           | ncludeAup |           |           |
    |           |           |           | = true    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | Conf      |           |           |
    | byodRe    |           |           | iguration |           |           |
    | gistratio |           |           | of BYOD   |           |           |
    | nSettings |           |           | endpoint  |           |           |
    |           |           |           | Reg       |           |           |
    |           |           |           | istration |           |           |
    |           |           |           | step      |           |           |
    |           |           |           | conf      |           |           |
    |           |           |           | iguration |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Boolean   | No        | Display   | true      |           |
    | sho       |           |           | Device ID |           |           |
    | wDeviceID |           |           | field     |           |           |
    |           |           |           | during    |           |           |
    |           |           |           | reg       |           |           |
    |           |           |           | istration |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | String    | No        | Identity  |           | aa13bb40- |
    | endPo     |           |           | group id  |           | 8bff-11e6 |
    | intIdenti |           |           | for which |           | -996c-525 |
    | tyGroupId |           |           | endpoint  |           | 400b48521 |
    |           |           |           | belongs   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | List      | No        | Conf      |           |           |
    | byod      |           |           | iguration |           |           |
    | Registrat |           |           | of BYOD   |           |           |
    | ionSucces |           |           | endpoint  |           |           |
    | sSettings |           |           | Reg       |           |           |
    |           |           |           | istration |           |           |
    |           |           |           | Success   |           |           |
    |           |           |           | step      |           |           |
    |           |           |           | conf      |           |           |
    |           |           |           | iguration |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | Enum      | No        | After an  | AUTHSU    |           |
    | succes    |           |           | Authe     | CCESSPAGE |           |
    | sRedirect |           |           | ntication |           |           |
    |           |           |           | Success   |           |           |
    |           |           |           | where     |           |           |
    |           |           |           | should    |           |           |
    |           |           |           | device be |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | directed. |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | AUTHSUC   |           |           |
    |           |           |           | CESSPAGE, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | ORIGIN    |           |           |
    |           |           |           | ATINGURL, |           |           |
    |           |           |           | - URL     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | String    | No        | Target    |           |           |
    | re        |           |           | URL for   |           |           |
    | directUrl |           |           | red       |           |           |
    |           |           |           | irection, |           |           |
    |           |           |           | used when |           |           |
    |           |           |           | succes    |           |           |
    |           |           |           | sRedirect |           |           |
    |           |           |           | = URL     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        |           |           |           |
    | a         |           |           |           |           |           |
    | uthSucces |           |           |           |           |           |
    | sSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | After an  | AUTHSU    |           |
    | succes    |           |           | Authe     | CCESSPAGE |           |
    | sRedirect |           |           | ntication |           |           |
    |           |           |           | Success   |           |           |
    |           |           |           | where     |           |           |
    |           |           |           | should    |           |           |
    |           |           |           | device be |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | directed. |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | AUTHSUC   |           |           |
    |           |           |           | CESSPAGE, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | ORIGIN    |           |           |
    |           |           |           | ATINGURL, |           |           |
    |           |           |           | - URL     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | Target    |           | www.      |
    | re        |           |           | URL for   |           | cisco.com |
    | directUrl |           |           | red       |           |           |
    |           |           |           | irection, |           |           |
    |           |           |           | used when |           |           |
    |           |           |           | succes    |           |           |
    |           |           |           | sRedirect |           |           |
    |           |           |           | = URL     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        |           |           |           |
    | postL     |           |           |           |           |           |
    | oginBanne |           |           |           |           |           |
    | rSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Include a | false     |           |
    | inclu     |           |           | P         |           |           |
    | dePostAcc |           |           | ost-Login |           |           |
    | essBanner |           |           | Banner    |           |           |
    |           |           |           | page      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Portal    |           |           |
    | s         |           |           | Support   |           |           |
    | upportInf |           |           | In        |           |           |
    | oSettings |           |           | formation |           |           |
    |           |           |           | Settings  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | incl      |           |           |           |           |           |
    | udeSuppor |           |           |           |           |           |
    | tInfoPage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | inclu     |           |           |           |           |           |
    | deMacAddr |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | include   |           |           |           |           |           |
    | IpAddress |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | inclu     |           |           |           |           |           |
    | deBrowser |           |           |           |           |           |
    | UserAgent |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | i         |           |           |           |           |           |
    | ncludePol |           |           |           |           |           |
    | icyServer |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        |           | false     |           |
    | includeFa |           |           |           |           |           |
    | ilureCode |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Enum      | No        | Specifies |           | HIDE      |
    | emptyFie  |           |           | how empty |           |           |
    | ldDisplay |           |           | fields    |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | handled   |           |           |
    |           |           |           | on the    |           |           |
    |           |           |           | Support   |           |           |
    |           |           |           | In        |           |           |
    |           |           |           | formation |           |           |
    |           |           |           | Page.     |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | - HIDE,   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | D         |           |           |
    |           |           |           | ISPLAYWIT |           |           |
    |           |           |           | HNOVALUE, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | DISPL     |           |           |
    |           |           |           | AYWITHDEF |           |           |
    |           |           |           | AULTVALUE |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | The       |           |           |
    | defa      |           |           | default   |           |           |
    | ultEmptyF |           |           | value     |           |           |
    | ieldValue |           |           | displayed |           |           |
    |           |           |           | for an    |           |           |
    |           |           |           | empty     |           |           |
    |           |           |           | field     |           |           |
    |           |           |           | Only      |           |           |
    |           |           |           | valid     |           |           |
    |           |           |           | when      |           |           |
    |           |           |           | emptyFie  |           |           |
    |           |           |           | ldDisplay |           |           |
    |           |           |           | =         |           |           |
    |           |           |           | DISPL     |           |           |
    |           |           |           | AYWITHDEF |           |           |
    |           |           |           | AULTVALUE |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | custo     | List      | No        | Defines   |           |           |
    | mizations |           |           | all of    |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | Portal    |           |           |
    |           |           |           | Custo     |           |           |
    |           |           |           | mizations |           |           |
    |           |           |           | available |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Defines   |           |           |
    | po        |           |           | the       |           |           |
    | rtalTheme |           |           | conf      |           |           |
    |           |           |           | iguration |           |           |
    |           |           |           | for       |           |           |
    |           |           |           | portal    |           |           |
    |           |           |           | theme     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - id    | String    | No        | The       |           | 9eb421c0- |
    |           |           |           | unique    |           | 8c01-11e6 |
    |           |           |           | internal  |           | -996c-525 |
    |           |           |           | i         |           | 400b48521 |
    |           |           |           | dentifier |           |           |
    |           |           |           | of the    |           |           |
    |           |           |           | portal    |           |           |
    |           |           |           | theme     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - name  | String    | Yes       | The       |           | Default   |
    |           |           |           | system-   |           | Blue      |
    |           |           |           | or        |           | theme     |
    |           |           |           | user      |           |           |
    |           |           |           | -assigned |           |           |
    |           |           |           | name of   |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | portal    |           |           |
    |           |           |           | theme     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | A CSS     |           | Base 64   |
    | themeData |           |           | file,     |           | encoded   |
    |           |           |           | re        |           | string of |
    |           |           |           | presented |           | Theme CSS |
    |           |           |           | as a      |           | file      |
    |           |           |           | Base6     |           |           |
    |           |           |           | 4-encoded |           |           |
    |           |           |           | byte      |           |           |
    |           |           |           | array     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | The Tweak |           |           |
    | p         |           |           | Settings  |           |           |
    | ortalTwea |           |           | are a     |           |           |
    | kSettings |           |           | cust      |           |           |
    |           |           |           | omization |           |           |
    |           |           |           | of the    |           |           |
    |           |           |           | Portal    |           |           |
    |           |           |           | Theme     |           |           |
    |           |           |           | that has  |           |           |
    |           |           |           | been      |           |           |
    |           |           |           | selected  |           |           |
    |           |           |           | for the   |           |           |
    |           |           |           | portal.   |           |           |
    |           |           |           | When the  |           |           |
    |           |           |           | Portal    |           |           |
    |           |           |           | Theme     |           |           |
    |           |           |           | selection |           |           |
    |           |           |           | is        |           |           |
    |           |           |           | changed,  |           |           |
    |           |           |           | the Tweak |           |           |
    |           |           |           | Settings  |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | ov        |           |           |
    |           |           |           | erwritten |           |           |
    |           |           |           | to match  |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | values in |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | theme.    |           |           |
    |           |           |           | The Tweak |           |           |
    |           |           |           | Settings  |           |           |
    |           |           |           | can       |           |           |
    |           |           |           | sub       |           |           |
    |           |           |           | sequently |           |           |
    |           |           |           | be        |           |           |
    |           |           |           | changed   |           |           |
    |           |           |           | by the    |           |           |
    |           |           |           | user      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        | Hex value |           | #0000FF   |
    | ba        |           |           | of color  |           |           |
    | nnerColor |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           | Banner    |
    | banner    |           |           |           |           | Text      |
    | TextColor |           |           |           |           | color     |
    |           |           |           |           |           | code from |
    |           |           |           |           |           | GUI       |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           | Color     |
    | p         |           |           |           |           | code from |
    | ageBackgr |           |           |           |           | GUI       |
    | oundColor |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           | Label and |
    | pag       |           |           |           |           | Text      |
    | eLabelAnd |           |           |           |           | color     |
    | TextColor |           |           |           |           | from GUI  |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | This      |           |           |
    | language  |           |           | property  |           |           |
    |           |           |           | is        |           |           |
    |           |           |           | supported |           |           |
    |           |           |           | only for  |           |           |
    |           |           |           | Read      |           |           |
    |           |           |           | operation |           |           |
    |           |           |           | and it    |           |           |
    |           |           |           | allows to |           |           |
    |           |           |           | show the  |           |           |
    |           |           |           | custo     |           |           |
    |           |           |           | mizations |           |           |
    |           |           |           | in        |           |           |
    |           |           |           | English.  |           |           |
    |           |           |           | Other     |           |           |
    |           |           |           | languages |           |           |
    |           |           |           | are not   |           |           |
    |           |           |           | supported |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           | English   |
    | vie       |           |           |           |           |           |
    | wLanguage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Represent |           |           |
    | gl        |           |           | the       |           |           |
    | obalCusto |           |           | portal    |           |           |
    | mizations |           |           | Global    |           |           |
    |           |           |           | custo     |           |           |
    |           |           |           | mizations |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           | Guest     |
    | ba        |           |           |           |           | Portal    |
    | nnerTitle |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           | Contact   |
    | co        |           |           |           |           | Support   |
    | ntactText |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | No        |           |           | Footer    |
    | foot      |           |           |           |           | Element   |
    | erElement |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Image     | No        |           |           |           |
    | mobile    |           |           |           |           |           |
    | LogoImage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | String    | No        | Re        |           | base 64   |
    | data      |           |           | presented |           | encoded   |
    |           |           |           | as base   |           | value of  |
    |           |           |           | 64        |           | image     |
    |           |           |           | encoded   |           |           |
    |           |           |           | string of |           |           |
    |           |           |           | the image |           |           |
    |           |           |           | byte      |           |           |
    |           |           |           | array     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Image     | No        |           |           |           |
    | desktop   |           |           |           |           |           |
    | LogoImage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | String    | No        | Re        |           | base 64   |
    | data      |           |           | presented |           | encoded   |
    |           |           |           | as base   |           | value of  |
    |           |           |           | 64        |           | image     |
    |           |           |           | encoded   |           |           |
    |           |           |           | string of |           |           |
    |           |           |           | the image |           |           |
    |           |           |           | byte      |           |           |
    |           |           |           | array     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Image     | No        |           |           |           |
    | ba        |           |           |           |           |           |
    | nnerImage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | String    | No        | Re        |           | base 64   |
    | data      |           |           | presented |           | encoded   |
    |           |           |           | as base   |           | value of  |
    |           |           |           | 64        |           | image     |
    |           |           |           | encoded   |           |           |
    |           |           |           | string of |           |           |
    |           |           |           | the image |           |           |
    |           |           |           | byte      |           |           |
    |           |           |           | array     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Image     | No        |           |           |           |
    | backgr    |           |           |           |           |           |
    | oundImage |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | String    | No        | Re        |           | base 64   |
    | data      |           |           | presented |           | encoded   |
    |           |           |           | as base   |           | value of  |
    |           |           |           | 64        |           | image     |
    |           |           |           | encoded   |           |           |
    |           |           |           | string of |           |           |
    |           |           |           | the image |           |           |
    |           |           |           | byte      |           |           |
    |           |           |           | array     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Represent |           |           |
    | pageCusto |           |           | the       |           |           |
    | mizations |           |           | entire    |           |           |
    |           |           |           | page      |           |           |
    |           |           |           | cust      |           |           |
    |           |           |           | omization |           |           |
    |           |           |           | as a      |           |           |
    |           |           |           | giant     |           |           |
    |           |           |           | d         |           |           |
    |           |           |           | ictionary |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - data  | List      | No        | The       |           |           |
    |           |           |           | D         |           |           |
    |           |           |           | ictionary |           |           |
    |           |           |           | will be   |           |           |
    |           |           |           | exposed   |           |           |
    |           |           |           | here as   |           |           |
    |           |           |           | key value |           |           |
    |           |           |           | pair      |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     - key | String    | Yes       |           |           | ui_contac |
    |           |           |           |           |           | t_ip_addr |
    |           |           |           |           |           | ess_label |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |     -     | String    | Yes       |           |           | SVAgYWR   |
    | value     |           |           |           |           | kcmVzczo= |
    +-----------+-----------+-----------+-----------+-----------+-----------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SelfRegisteredPortal
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SelfRegisteredPortal, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_self_registered_portal_by_id(self,
                                         id,
                                         headers=None,
                                         **query_parameters):
        """This API allows the client to get a self registered portal by
        ID.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/selfregportal/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f9c9a5e917af53dbbb91733e82e72ebe_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_self_registered_portal_by_id <#ciscoisesdk.
        api.v3_1_0.self_registered_portal.
        SelfRegisteredPortal.get_self_registered_portal_by_id>`_
        """
        return self.get_self_registered_portal_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_self_registered_portal_by_id(self,
                                            id,
                                            customizations=None,
                                            description=None,
                                            name=None,
                                            portal_test_url=None,
                                            portal_type=None,
                                            settings=None,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **query_parameters):
        """This API allows the client to update a self registered portal by
        ID.

        Args:
            customizations(object): Defines all of the Portal
                Customizations available, property of
                the request body.
            description(string): description, property of the
                request body.
            id(string): id, property of the request body.
            name(string): name, property of the request body.
            portal_test_url(string): URL to bring up a test page for
                this portal, property of the request
                body.
            portal_type(string): Allowed values: BYOD, HOTSPOTGUEST,
                MYDEVICE, SELFREGGUEST, SPONSOR,
                SPONSOREDGUEST, property of the request
                body.
            settings(object): Defines all of the settings groups
                available for a portal, property of the
                request body.
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'portalType':
                    portal_type,
                'portalTestUrl':
                    portal_test_url,
                'settings':
                    settings,
                'customizations':
                    customizations,
            }
            _payload = {
                'SelfRegPortal': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_c4fada6c558d9aba09cc373d5b266_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/selfregportal/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_c4fada6c558d9aba09cc373d5b266_v3_1_0', _api_response)

    def update_by_id(self,
                     id,
                     customizations=None,
                     description=None,
                     name=None,
                     portal_test_url=None,
                     portal_type=None,
                     settings=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_self_registered_portal_by_id <#ciscoisesdk.
        api.v3_1_0.self_registered_portal.
        SelfRegisteredPortal.update_self_registered_portal_by_id>`_
        """
        return self.update_self_registered_portal_by_id(
            id=id,
            customizations=customizations,
            description=description,
            name=name,
            portal_test_url=portal_test_url,
            portal_type=portal_type,
            settings=settings,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_self_registered_portal_by_id(self,
                                            id,
                                            headers=None,
                                            **query_parameters):
        """This API deletes a self registered portal by ID.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/selfregportal/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f9ada2e275fa2934fdb4825266a2c_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_self_registered_portal_by_id <#ciscoisesdk.
        api.v3_1_0.self_registered_portal.
        SelfRegisteredPortal.delete_self_registered_portal_by_id>`_
        """
        return self.delete_self_registered_portal_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_self_registered_portals(self,
                                    filter=None,
                                    filter_type=None,
                                    page=None,
                                    size=None,
                                    sortasc=None,
                                    sortdsc=None,
                                    headers=None,
                                    **query_parameters):
        """This API allows the client to get all the self registered
        portals.   Filter:   [name]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [name, description].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
            filter(basestring, list, set, tuple): filter query
                parameter.               **Simple
                filtering** should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or" query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.              (Operator:
                Description),
                (EQ: Equals),               (NEQ: Not
                Equals),               (GT: Greater
                Than),               (LT: Less Then),
                (STARTSW: Starts With),
                (NSTARTSW: Not Starts With),
                (ENDSW: Ends With),
                (NENDSW: Not Ends With),
                (CONTAINS: Contains),
                (NCONTAINS: Not Contains),
                .
            filter_type(basestring): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))
        check_type(sortasc, basestring)
        check_type(sortdsc, basestring)
        check_type(filter, (basestring, list, set, tuple))
        check_type(filter_type, basestring)

        _params = {
            'page':
                page,
            'size':
                size,
            'sortasc':
                sortasc,
            'sortdsc':
                sortdsc,
            'filter':
                filter,
            'filterType':
                filter_type,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/selfregportal')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bb165bd00a6653ac9da440f23ee62ecc_v3_1_0', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_self_registered_portals <#ciscoisesdk.
        api.v3_1_0.self_registered_portal.
        SelfRegisteredPortal.get_self_registered_portals>`_
        """
        return self.get_self_registered_portals(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_self_registered_portals_generator(self,
                                              filter=None,
                                              filter_type=None,
                                              page=None,
                                              size=None,
                                              sortasc=None,
                                              sortdsc=None,
                                              headers=None,
                                              **query_parameters):
        """This API allows the client to get all the self registered
        portals.   Filter:   [name]   To search resources by
        using  toDate  column,follow the format:   DD-MON-YY
        (Example:13-SEP-18)     Day or Year:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13
        Month:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.SEP
        Date:GET
        /ers/config/guestuser/?filter=toDate.CONTAINS.13-SEP-18
        Sorting:   [name, description].

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            sortasc(basestring): sortasc query parameter. sort asc.
            sortdsc(basestring): sortdsc query parameter. sort desc.
            filter(basestring, list, set, tuple): filter query
                parameter.               **Simple
                filtering** should be available through
                the filter query string parameter. The
                structure of a filter is a triplet of
                field operator and value separated with
                dots. More than one filter can be sent.
                The logical operator common to ALL
                filter criteria will be by default AND,
                and can be changed by using the
                "filterType=or" query string parameter.
                Each resource Data model description
                should specify if an attribute is a
                filtered field.              (Operator:
                Description),
                (EQ: Equals),               (NEQ: Not
                Equals),               (GT: Greater
                Than),               (LT: Less Then),
                (STARTSW: Starts With),
                (NSTARTSW: Not Starts With),
                (ENDSW: Ends With),
                (NENDSW: Not Ends With),
                (CONTAINS: Contains),
                (NCONTAINS: Not Contains),
                .
            filter_type(basestring): filterType query parameter. The
                logical operator common to ALL filter
                criteria will be by default AND, and can
                be changed by using the parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.

              + RestResponse: REST response with following properties:

                  - headers(MyDict): response headers.
                  - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                    or the bracket notation.
                  - content(bytes): representation of the request's response
                  - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """

        yield from get_next_page(
            self.get_self_registered_portals, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          filter=None,
                          filter_type=None,
                          page=None,
                          size=None,
                          sortasc=None,
                          sortdsc=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_self_registered_portals_generator <#ciscoisesdk.
        api.v3_1_0.self_registered_portal.
        SelfRegisteredPortal.get_self_registered_portals_generator>`_
        """
        yield from get_next_page(
            self.get_self_registered_portals, dict(
                filter=filter,
                filter_type=filter_type,
                page=page,
                size=size,
                sortasc=sortasc,
                sortdsc=sortdsc,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_self_registered_portal(self,
                                      customizations=None,
                                      description=None,
                                      name=None,
                                      portal_test_url=None,
                                      portal_type=None,
                                      settings=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **query_parameters):
        """This API creates a self registered portal.

        Args:
            customizations(object): Defines all of the Portal
                Customizations available, property of
                the request body.
            description(string): description, property of the
                request body.
            name(string): name, property of the request body.
            portal_test_url(string): URL to bring up a test page for
                this portal, property of the request
                body.
            portal_type(string): Allowed values: BYOD, HOTSPOTGUEST,
                MYDEVICE, SELFREGGUEST, SPONSOR,
                SPONSOREDGUEST, property of the request
                body.
            settings(object): Defines all of the settings groups
                available for a portal, property of the
                request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'name':
                    name,
                'description':
                    description,
                'portalType':
                    portal_type,
                'portalTestUrl':
                    portal_test_url,
                'settings':
                    settings,
                'customizations':
                    customizations,
            }
            _payload = {
                'SelfRegPortal': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d524614e122d53d68324daf1681eb753_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/selfregportal')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_d524614e122d53d68324daf1681eb753_v3_1_0', _api_response)

    def create(self,
               customizations=None,
               description=None,
               name=None,
               portal_test_url=None,
               portal_type=None,
               settings=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_self_registered_portal <#ciscoisesdk.
        api.v3_1_0.self_registered_portal.
        SelfRegisteredPortal.create_self_registered_portal>`_
        """
        return self.create_self_registered_portal(
            customizations=customizations,
            description=description,
            name=name,
            portal_test_url=portal_test_url,
            portal_type=portal_type,
            settings=settings,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the self registered portal.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/selfregportal/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d8cc0e6962558c58d263f53b857cff0_v3_1_0', _api_response)
