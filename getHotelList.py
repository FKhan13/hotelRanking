# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:12:40 2015

@author: User
"""

import os
#import django

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
#django.setup()

#from visual.models import VisualCountry, VisualSearchResult, VisualHotel, VisualDateInfo, VisualSearch

#from django.db.models import Q 

import time
import datetime
import json

##############################################################################
# dummy variables
country = "Ukraine"
n_o_a = 2
n_o_c = 0
n_o_r = 1
star_rate = 5
stay_len = 1
##############################################################################
priceVal = 200

searchids1 = []
searchids2 = []
searchids = []
hotelids = []
result = []
start_time = time.time()
#objects = VisualSearchResult.objects.filter(Q(hotel_id = listofhotels[0]) |Q(hotel_id = listofhotels[1])|Q(hotel_id = listofhotels[2])|Q(hotel_id = listofhotels[3])|Q(hotel_id = listofhotels[4]))
#objects = VisualSearchResult.objects.filter(price__range = [100.00, 150.00])

country = country.replace('_', ' ')
# get country
objectCountry = VisualCountry.objects.get(name = country)
countryid = objectCountry.id

#sorts out no of adult, children, rooms get list of searchids
objects1 = VisualSearch.objects.filter(no_adults = n_o_a).filter(no_children = n_o_c).filter(no_rooms = n_o_r) 
for search in objects1:
    searchids1.append(search.id)
    
elapsed_time = time.time() - start_time
print("Time for country and search ids ")
print(elapsed_time)

#sorts out length of stay gets list of searchids
objects2 = VisualDateInfo.objects.filter(length_of_stay = stay_len)
for search in objects2:
    searchids2.append(search.search_id)
    
elapsed_time = time.time() - start_time
print("Time for searchids from length of stay: ")
print(elapsed_time)

# refine search ids list
searchids = list(set(searchids1)&set(searchids2))

#sorts out star rating and country get list of hotels
objects2 = VisualHotel.objects.filter(star_rating = star_rate, country_id = countryid )
for search in objects2:
    hotelids.append(search.id)
    
elapsed_time = time.time() - start_time
print("Time for hotelids and calculating common search ids: ")
print(elapsed_time)

# get the hottels with all specifications
if not hotelids:
    objects3 = VisualSearchResult.objects.filter(search_id__in=searchids)
elif not searchids:
    objects3 = VisualSearchResult.objects.filter(hotel_id__in=hotelids)
else:
    objects3 = VisualSearchResult.objects.filter(search_id__in=searchids).filter(hotel_id__in=hotelids)

elapsed_time = time.time() - start_time
print("Time for getting query for hotels and search items: ")
print(elapsed_time)
    
newobj = objects3[0:5]
for search in newobj:
    result.append(search.hotel_id)
  
    
elapsed_time = time.time() - start_time
print("Time for forloop: ")
print(elapsed_time)

 