# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine SponsorPortal API wrapper.

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


class SponsorPortal(object):
    """Identity Services Engine SponsorPortal API (version: 3.1.1).

    Wraps the Identity Services Engine SponsorPortal
    API and exposes the API as native Python
    methods that return native Python objects.

    Sponsor Portal API provides the ability to create, read, update, delete
    and search sponsor portals.

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
    | name      | String    | Yes       | Resource  |           | Sponsor   |
    |           |           |           | Name      |           | Portal    |
    |           |           |           |           |           | (default) |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | id        | String    | No        | Resource  |           | 04cd708b- |
    |           |           |           | UUID,     |           | feef-4c75 |
    |           |           |           | mandatory |           | -bf3e-2d2 |
    |           |           |           | for       |           | a9c302da2 |
    |           |           |           | update    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | de        | String    | No        |           |           | Default   |
    | scription |           |           |           |           | portal    |
    |           |           |           |           |           | used by   |
    |           |           |           |           |           | sponsors  |
    |           |           |           |           |           | to create |
    |           |           |           |           |           | and       |
    |           |           |           |           |           | manage    |
    |           |           |           |           |           | accounts  |
    |           |           |           |           |           | for       |
    |           |           |           |           |           | a         |
    |           |           |           |           |           | uthorized |
    |           |           |           |           |           | visitors  |
    |           |           |           |           |           | to        |
    |           |           |           |           |           | securely  |
    |           |           |           |           |           | access    |
    |           |           |           |           |           | the       |
    |           |           |           |           |           | network   |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | port      | String    | No        | URL to    |           | h         |
    | alTestUrl |           |           | bring up  |           | ttps://{i |
    |           |           |           | a test    |           | se-ip}:84 |
    |           |           |           | page for  |           | 45/portal |
    |           |           |           | this      |           | /PortalSe |
    |           |           |           | portal    |           | tup.actio |
    |           |           |           |           |           | n?portal= |
    |           |           |           |           |           | 04cd708b- |
    |           |           |           |           |           | feef-4c75 |
    |           |           |           |           |           | -bf3e-2d2 |
    |           |           |           |           |           | a9c302da2 |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | p         | Enum      | Yes       | Allowed   | SPONSOR   |           |
    | ortalType |           |           | values:   |           |           |
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
    |   -       | Integer   | Yes       | The port  |           | 8445      |
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
    |   - fqdn  | String    | No        | The       |           | Default   |
    |           |           |           | fully-    |           | Portal    |
    |           |           |           | qualified |           | Ce        |
    |           |           |           | domain    |           | rtificate |
    |           |           |           | name      |           | Group     |
    |           |           |           | (FQDN)    |           |           |
    |           |           |           | that      |           |           |
    |           |           |           | end-users |           |           |
    |           |           |           | will use  |           |           |
    |           |           |           | to access |           |           |
    |           |           |           | this      |           |           |
    |           |           |           | portal.   |           |           |
    |           |           |           | Used only |           |           |
    |           |           |           | in        |           |           |
    |           |           |           | Sponsor   |           |           |
    |           |           |           | portal    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Unique Id |           | 92faba60- |
    | au        |           |           | of the    |           | 8c01-11e6 |
    | thenticat |           |           | identity  |           | -996c-525 |
    | ionMethod |           |           | source    |           | 400b48521 |
    |           |           |           | sequence  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Integer   | No        |           | 10        |           |
    | id        |           |           |           |           |           |
    | leTimeout |           |           |           |           |           |
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
    |   -       | List      | No        | Names of  |           |           |
    | avail     |           |           | the SSIDs |           |           |
    | ableSsids |           |           | available |           |           |
    |           |           |           | for       |           |           |
    |           |           |           | a         |           |           |
    |           |           |           | ssignment |           |           |
    |           |           |           | to guest  |           |           |
    |           |           |           | users by  |           |           |
    |           |           |           | sponsors  |           |           |
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
    | sp        |           |           |           |           |           |
    | onsorChan |           |           |           |           |           |
    | gePasswor |           |           |           |           |           |
    | dSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | Boolean   | No        | Allow     | false     |           |
    | allow     |           |           | sponsors  |           |           |
    | SponsorTo |           |           | to change |           |           |
    | ChangePwd |           |           | their own |           |           |
    |           |           |           | passwords |           |           |
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
        """Initialize a new SponsorPortal
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SponsorPortal, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_sponsor_portal_by_id(self,
                                 id,
                                 headers=None,
                                 **query_parameters):
        """This API allows the client to get a sponsor portal by ID.

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

        e_url = ('/ers/config/sponsorportal/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cd6793a4a8e7576c8b290bdc88001f6f_v3_1_1', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_sponsor_portal_by_id <#ciscoisesdk.
        api.v3_1_1.sponsor_portal.
        SponsorPortal.get_sponsor_portal_by_id>`_
        """
        return self.get_sponsor_portal_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def update_sponsor_portal_by_id(self,
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
        """This API allows the client to update a sponsor portal by ID.

        Args:
            customizations(object): customizations, property of the
                request body.
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
                'SponsorPortal': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_bd8691c5d9435e48a3c7a08658bda585_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sponsorportal/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_bd8691c5d9435e48a3c7a08658bda585_v3_1_1', _api_response)

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
        """Alias for `update_sponsor_portal_by_id <#ciscoisesdk.
        api.v3_1_1.sponsor_portal.
        SponsorPortal.update_sponsor_portal_by_id>`_
        """
        return self.update_sponsor_portal_by_id(
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

    def delete_sponsor_portal_by_id(self,
                                    id,
                                    headers=None,
                                    **query_parameters):
        """This API deletes a sponsor portal by ID.

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

        e_url = ('/ers/config/sponsorportal/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d8d4c7451f7f5e2faae4e8ac530b5f08_v3_1_1', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_sponsor_portal_by_id <#ciscoisesdk.
        api.v3_1_1.sponsor_portal.
        SponsorPortal.delete_sponsor_portal_by_id>`_
        """
        return self.delete_sponsor_portal_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def get_sponsor_portal(self,
                           filter=None,
                           filter_type=None,
                           page=None,
                           size=None,
                           sortasc=None,
                           sortdsc=None,
                           headers=None,
                           **query_parameters):
        """This API allows the client to get all the sponsor portals.
        Filter:   [name, description]   To search resources by
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

        e_url = ('/ers/config/sponsorportal')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aa24c1260a568b93c283ecd2c3510e_v3_1_1', _api_response)

    def get_all(self,
                filter=None,
                filter_type=None,
                page=None,
                size=None,
                sortasc=None,
                sortdsc=None,
                headers=None,
                **query_parameters):
        """Alias for `get_sponsor_portal <#ciscoisesdk.
        api.v3_1_1.sponsor_portal.
        SponsorPortal.get_sponsor_portal>`_
        """
        return self.get_sponsor_portal(
            filter=filter,
            filter_type=filter_type,
            page=page,
            size=size,
            sortasc=sortasc,
            sortdsc=sortdsc,
            headers=headers,
            **query_parameters
        )

    def get_sponsor_portal_generator(self,
                                     filter=None,
                                     filter_type=None,
                                     page=None,
                                     size=None,
                                     sortasc=None,
                                     sortdsc=None,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to get all the sponsor portals.
        Filter:   [name, description]   To search resources by
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
            self.get_sponsor_portal, dict(
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
        """Alias for `get_sponsor_portal_generator <#ciscoisesdk.
        api.v3_1_1.sponsor_portal.
        SponsorPortal.get_sponsor_portal_generator>`_
        """
        yield from get_next_page(
            self.get_sponsor_portal, dict(
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

    def create_sponsor_portal(self,
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
        """This API creates a sponsor portal.

        Args:
            customizations(object): customizations, property of the
                request body.
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
                'SponsorPortal': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_f15d19b858d59218ab56b7323ca2fae_v3_1_1')\
                .validate(_payload)

        e_url = ('/ers/config/sponsorportal')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_f15d19b858d59218ab56b7323ca2fae_v3_1_1', _api_response)

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
        """Alias for `create_sponsor_portal <#ciscoisesdk.
        api.v3_1_1.sponsor_portal.
        SponsorPortal.create_sponsor_portal>`_
        """
        return self.create_sponsor_portal(
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
        the sponsor portal.

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

        e_url = ('/ers/config/sponsorportal/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fa39b9cc4834522395edcbe0d6830ae4_v3_1_1', _api_response)
