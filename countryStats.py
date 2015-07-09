# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:11:22 2015
This script generates data for the bubble chart view for the loactions page(country)
@author: Pelonomi Moiloa
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
django.setup()

from visual.models import *