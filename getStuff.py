import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
django.setup()

from visual.models import VisualCountry, VisualSearchResult, VisualHotel, VisualDateInfo, VisualSearch

from django.db.models import Q 

import time
import datetime
import json

hotelid = 1
review_score = 3 

searchids =[]
reviewScores = []
dates = []
objects2 = []

objects1 = VisualSearchResult.objects.filter(hotel_id = hotelid)

for i in objects1:
	searchids.append(i.search_id)

for y in searchids:
	objects2 = VisualDateInfo.objects.filter(search = y)

#for z in objects2:
#	if z != None:
#		dates.append(z)
		
for x in searchids:
	print (x)

#	for x in objects1:
#		searchids1.append(string(x.date) x.prop_review_score)

https://github.com/FKhan13/hotelRanking.git
