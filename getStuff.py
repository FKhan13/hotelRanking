import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelRanking.settings")
django.setup()

from visual.models import VisualCountry, VisualSearchResult, VisualHotel, VisualDateInfo, VisualSearch

import datetime 
avg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
add = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
months = ["Jan12","Feb12","Mar12","Apr12","May12","Jun12","Jul12","Aug12","Sep12","Oct12","Nov12","Dec12","Jan13","Feb13","Mar13","Apr13","May13","Jun13",
"Jul13","Aug13","Sep13","Oct13","Nov13","Dec13"]


def getAverage(hotelId,avg_of_what):
 	searchids = []
 	dates = []
 	prices = []
 	hotelList = VisualSearchResult.objects.filter(hotel_id = hotelId)

 	for i in hotelList:
 		searchids.append(i.search_id)

 	for y in searchids:
 		visualTable = VisualDateInfo.objects.get(search = y)
 		dates.append(visualTable.date_time)

 	for r in searchids:
 		searchResult = VisualSearchResult.objects.filter(hotel_id = hotelId).values(avg_of_what).get(search_id = r)[avg_of_what]
 		prices.append(searchResult)

 	counter =0
 	for d in dates:
 		if d.year == 2012:
 			avg[d.month-1] = (avg[d.month-1] + prices[counter]) / 2
 		if d.year == 2013:
 			avg[d.month+11]= (avg[d.month+11]+ prices[counter]) / 2
 		counter += 1

def getSum(hotelId,sum_of_what, add):
 	searchids = []
 	dates = []
 	bools = []
 	hotelList = VisualSearchResult.objects.filter(hotel_id = hotelId)

 	for i in hotelList:
 		searchids.append(i.search_id)

 	for y in searchids:
 		visualTable = VisualDateInfo.objects.get(search = y)
 		dates.append(visualTable.date_time)

 	for r in searchids:
 		searchResult = VisualSearchResult.objects.filter(hotel_id = hotelId).values(sum_of_what).get(search_id = r)[sum_of_what]
 		bools.append(searchResult)

 	counter =0
 	for d in dates:
 		if d.year == 2012:
 			if bools[counter] == True: add[d.month-1] = add[d.month-1] + 1
 		if d.year == 2013:
 			if bools[counter] == True: add[d.month+11] = add[d.month+11]+ 1
 		counter += 1


#getAverage(41975,"prop_review_score")

getSum(1, "booking_bool", add)

for x in add:
	print (x)

