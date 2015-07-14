# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:11:22 2015
This script generates data for the bubble chart view for the loactions page(country)
@author: Pelonomi Moiloa
"""

#import os
#import django
#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
django.setup()

from visual.models import VisualCountry, VisualSearchResult, VisualHotel

def countryNames(country):
    #countries = [country.name for country in VisualCountry.objects.all()]
    #countries = [country.id for country in VisualCountry.objects.all()]

    entry = VisualCountry.objects.get(name = country)
    countid = entry.id
    print(countid)
    hotellist = [search.id for search in VisualHotel.objects.filter(country_id = countid)]    
    prices = []
    starratings = []
    rank = []
    bookings = 0
    dictionary = {}
    for hotel in hotellist:
        listofthings = VisualSearchResult.objects.filter(hotel_id = hotel)
        for search in listofthings:
            prices.append(search.price)
            starratings.append(search.prop_review_score)
            rank.append(search.rank_pos)
            bookings = bookings + int(search.booking_bool)
    dictionary['price'] = prices
    dictionary['starrating'] = starratings
    dictionary['rank'] = rank
    dictionary['bookings'] = bookings
    return dictionary
    
hlist = countryNames('Ukraine')