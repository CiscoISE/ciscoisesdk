# -*- coding: utf-8 -*-
"""IPython Project Console.

Used to interactively work with the main package contents in IPython.
"""


__copyright__ = "Copyright (c) 2021 Cisco and/or its affiliates."
__license__ = "MIT"


import logging
from ciscoisesdk import IdentityServicesEngineAPI
import warnings

# Disable warnings caused by (verify=False)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')


api = IdentityServicesEngineAPI(verify=False, debug=True)

logging.getLogger('ciscoisesdk').addHandler(logging.StreamHandler())
# logging.getLogger('ciscoisesdk').addHandler(ch)

# api.network_device.get_all_network_device().response

# CONFIGURE logger correctly following
# https://docs.python.org/3.7/howto/logging.html#configuring-logging
# We were using basic logging
# if we remove the line debug does not log
