# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:11:22 2015
This script generates data for the bubble chart view for the loactions page(country)
@author: Pelonomi Moiloa
"""

#import os
#import django
##
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
#django.setup()

from models import VisualCountry, VisualSearchResult, VisualHotel

def countryNames(country):
    #countries = [country.name for country in VisualCountry.objects.all()]
    #countries = [country.id for country in VisualCountry.objects.all()]
    entry = VisualCountry.objects.get(name = country)
    countid = entry.id
    print(countid)
    hotellist = [search.id for search in VisualHotel.objects.filter(country_id = countid)]    
    prices = []
    for hotel in hotellist:
        prices = [search.price for search in VisualSearchResult.objects.filter(hotel_id = hotel)]
    return prices
    
hlist = countryNames('Ukraine')