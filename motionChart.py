# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:12:40 2015

@author: User
"""

import os
#import django

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
#django.setup()

#from visual.models import VisualCountry, VisualSearchResult, VisualHotel, VisualDateInfo

#from django.db.models import Q

import time
import datetime
import json

from operator import itemgetter
itemlist = []
listofhotels = [1,2,3,4,5]

start_time = time.time()
#objects = objects.filter(hotel_id__in=listofhotels)
objects = VisualSearchResult.objects.filter(Q(hotel_id = listofhotels[0]) |Q(hotel_id = listofhotels[1])|Q(hotel_id = listofhotels[2])|Q(hotel_id = listofhotels[3])|Q(hotel_id = listofhotels[4]))
#objects = VisualSearchResult.objects.filter(hotel_id = listofhotels[0])
hotels = []
for x in objects:
    name = "Hotel" + str(x.hotel_id) 
    timestampo = VisualDateInfo.objects.get(search_id = x.search_id) 
    times = timestampo.date_time
    year = times.strftime("%Y")# this is the timestamp
    concat = name + year
    if concat not in hotels:
        hotels.append(concat)
        document = {}
        document["name"] = name#hotel name
        document["price"] = float(x.price) 
        document["bookings"] = int(x.booking_bool) # booking boolean
        document["review_score"] = float(x.prop_review_score) # property review score
        document["year"] = year
        #document["timestamp"] = times.strftime("%Y-%m-%d %H:%M:%S")

        hotelobj = VisualHotel.objects.get(id = x.hotel_id) 
        desirability = float(hotelobj.desirability)
        if (desirability <= 0.00000): 
            document["desirability"] = "Not desirable" 
        elif (0.00000 < desirability <= 2.00000):
            document["desirability"] = "Fairly desirable" 
        elif (6.00000 < desirability <= 4.00000):
            document["desirability"] = "Desirable" 
        elif (8.00000 < desirability):
            document["desirability"] = "Highly desirable" 
        # location desirability
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