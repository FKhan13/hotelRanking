# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:12:40 2015

@author: User
"""

#import os
#import django
#
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
#django.setup()
#
#from visual.models import VisualCountry, VisualSearchResult, VisualHotel, VisualDateInfo
#
#from django.db.models import Q

import time
import datetime
import json

from operator import itemgetter
itemlist = []
listofhotels = [1,2,3,4,5]

start_time = time.time()
#objects1 = VisualSearchResult.objects.filter(hotel_id__in=listofhotels)
objects = VisualSearchResult.objects.filter(Q(hotel_id = listofhotels[0]) |Q(hotel_id = listofhotels[1])|Q(hotel_id = listofhotels[2])|Q(hotel_id = listofhotels[3])|Q(hotel_id = listofhotels[4]))
#objects = VisualSearchResult.objects.filter(hotel_id = listofhotels[0])
hotels = []
#objects2 = objects1[0:5]
hotellist = []
for x in objects: 
    timestampo = VisualDateInfo.objects.get(search_id = x.search_id)
    hotelobj = VisualHotel.objects.get(id = x.hotel_id) 
    times = timestampo.date_time
    year = times.strftime("%Y")# this is the timestamp
    document = {}
    hotelname = "Hotel " + str(x.hotel_id)
    if hotelname not in hotellist:
        document["name"] =  hotelname
        document["price"] = 0 
        document["bookings"] = 0 # booking boolean
        document["review_score"] = 0 # property review score
        document["year"] = 2011
        document["desirability"] = 0
        document["independant_bool"] = int(hotelobj.independent)
        itemlist.append(document)
    document = {}
    document["name"] =  hotelname
    document["price"] = float(x.price) 
    document["bookings"] = int(x.booking_bool) # booking boolean
    document["review_score"] = float(x.prop_review_score) # property review score
    document["year"] = int(year)
    document["desirability"] = float(hotelobj.desirability)
    document["independant_bool"] = int(hotelobj.independent)
    itemlist.append(document)
  
        
elapsed_time = time.time() - start_time
print("Test1: ")
print(elapsed_time)

with open('result.json', 'w') as fp:
    json.dump(itemlist, fp)


# this one was waaaaay slower
#start_time = time.time()
#checklist2 = []
#for x in listofhotels:
#    objects = VisualSearchResult.objects.filter(hotel_id = x)
#    for thing in objects:
#        checklist2.append(thing.hotel_id)
#elapsed_time = time.time() - start_time
#print("Test2: ")
#print(elapsed_time)