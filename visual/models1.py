from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.IntegerField(primary_key =True)
    name = models.CharField(max_length = 30)
    a_name = models.CharField(max_length = 20)
    
class Site(models.Model):
    id = models.IntegerField(primary_key =True)
    name = models.CharField(max_length=30)
    a_name = models.CharField(max_length = 20)
    
class City(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)
    a_name = models.CharField(max_length = 20)
    country_id = models.ForeignKey(Country, default = 0)
    
class Date_Info(models.Model):
    date_time = models.DateTimeField(default = '2013-04-04 08:32:15')
    length_of_stay = models.IntegerField(default = 0)
    booking_window = models.IntegerField(default = 0)
    arrival = models.DateField(null = True)
    checkOut = models.DateField(null = True)
    
class Search(models.Model):
    id = models.IntegerField(primary_key = True)
    date_info = models.ForeignKey(Date_Info, default = 0)
    no_adults = models.IntegerField(default = 1)
    no_children = models.IntegerField(default = 0)
    no_rooms = models.IntegerField(default = 1)
    dest_city = models.ForeignKey(City, default = 0)
    
class Hotel(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30, default = 'default')
    a_name = models.CharField(max_length = 20, default = 'default')
    country = models.ForeignKey(Country, default = 0)
    star_rating = models.IntegerField(default = 0)
    independent = models.BooleanField(default = 0)
    desirability = models.DecimalField(null = True, max_digits=10, decimal_places=5)
    hist_price = models.DecimalField(null = True, max_digits=10, decimal_places=2)
    
class Search_Result(models.Model):
    search = models.ForeignKey(Search, default = 0)
    hotel = models.ForeignKey(Hotel, default = 0)
    rank_pos = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promo_flag = models.BooleanField(default = 0)
    affinity_score = models.DecimalField(null = True, max_digits=10, decimal_places=5)
    if_clicked = models.BooleanField(default = 0)
    short_stay_sat = models.BooleanField(default = 0)
    prop_review_score = models.DecimalField(null = True, max_digits=2, decimal_places=2)
    random_bool = models.BooleanField(default = 0)    
    
class Visitor(models.Model):
    search_result = models.ForeignKey(Search_Result, default = 0)
    country = models.ForeignKey(Country, default = 0)
    dist_to_dest = models.IntegerField(default = 0)
    mean_star_rating = models.DecimalField(null = True, max_digits=2, decimal_places=2)
    mean_price = models.DecimalField(null = True, max_digits=10, decimal_places=2) 
    
class Booking(models.Model):
    search_result = models.ForeignKey(Search_Result, default = 0)
    total_value = models.DecimalField(null = True, max_digits=10, decimal_places=2)
    site = models.ForeignKey(Site, default = 0)
    
class Competitive_OTA(models.Model):
    search_result = models.ForeignKey(Search_Result)
    price = models.DecimalField(null = True, max_digits = 10, decimal_places=2)
    percent_diff = models.IntegerField(null = True)
    availablity = models.NullBooleanField(null = True)
    high_low_same = models.CharField(null = True, max_length = 1) 