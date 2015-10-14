# -*- coding: utf-8 -*-
"""
USDA National Agricultural Statistics Service API wrapper

This Python wrapper implements the public API for the USDA National
Agricultural Statistics Service. It is a very thin layer over the Requests
package.

This product uses the NASS API but is not endorsed or certified by NASS.

:copyright: (c) 2015 by Nick Frost.
:license: MIT, see LICENSE for more details.
"""

__version__ = '0.1.1'

from .api import NassApi
