# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


#class AuthGroup(models.Model):
#    name = models.CharField(unique=True, max_length=80)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_group'
#
#
#class AuthGroupPermissions(models.Model):
#    group = models.ForeignKey(AuthGroup)
#    permission = models.ForeignKey('AuthPermission')
#
#    class Meta:
#        managed = False
#        db_table = 'auth_group_permissions'
#        unique_together = (('group_id', 'permission_id'),)
#
#
#class AuthPermission(models.Model):
#    name = models.CharField(max_length=255)
#    content_type = models.ForeignKey('DjangoContentType')
#    codename = models.CharField(max_length=100)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_permission'
#        unique_together = (('content_type_id', 'codename'),)
#
#
#class AuthUser(models.Model):
#    password = models.CharField(max_length=128)
#    last_login = models.DateTimeField(blank=True, null=True)
#    is_superuser = models.BooleanField()
#    username = models.CharField(unique=True, max_length=30)
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    email = models.CharField(max_length=254)
#    is_staff = models.BooleanField()
#    is_active = models.BooleanField()
#    date_joined = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user'
#
#
#class AuthUserGroups(models.Model):
#    user = models.ForeignKey(AuthUser)
#    group = models.ForeignKey(AuthGroup)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user_groups'
#        unique_together = (('user_id', 'group_id'),)
#
#
#class AuthUserUserPermissions(models.Model):
#    user = models.ForeignKey(AuthUser)
#    permission = models.ForeignKey(AuthPermission)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user_user_permissions'
#        unique_together = (('user_id', 'permission_id'),)
#
#
#class DjangoAdminLog(models.Model):
#    action_time = models.DateTimeField()
#    object_id = models.TextField(blank=True, null=True)
#    object_repr = models.CharField(max_length=200)
#    action_flag = models.SmallIntegerField()
#    change_message = models.TextField()
#    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
#    user = models.ForeignKey(AuthUser)
#
#    class Meta:
#        managed = False
#        db_table = 'django_admin_log'
#
#
#class DjangoContentType(models.Model):
#    app_label = models.CharField(max_length=100)
#    model = models.CharField(max_length=100)
#
#    class Meta:
#        managed = False
#        db_table = 'django_content_type'
#        unique_together = (('app_label', 'model'),)
#
#
#class DjangoMigrations(models.Model):
#    app = models.CharField(max_length=255)
#    name = models.CharField(max_length=255)
#    applied = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'django_migrations'
#
#
#class DjangoSession(models.Model):
#    session_key = models.CharField(primary_key=True, max_length=40)
#    session_data = models.TextField()
#    expire_date = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'django_session'

class VisualSite(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    a_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visual_site'
        app_label = 'visual'

        
        
class VisualBooking(models.Model):
    total_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    search_result_id = models.IntegerField()
    site = models.ForeignKey(VisualSite)

    class Meta:
        managed = True
        db_table = 'visual_booking'
        app_label = 'visual'


class VisualCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    a_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visual_country'
        app_label = 'visual'

        

class VisualCity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    a_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.ForeignKey(VisualCountry, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visual_city'
        app_label = 'visual'



class VisualCompetitiveOta(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    percent_diff = models.IntegerField(blank=True, null=True)
    availablity = models.NullBooleanField()
    high_low_same = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visual_competitive_ota'
        app_label = 'visual'


class VisualSearch(models.Model):
    id = models.IntegerField(primary_key=True)
    no_adults = models.IntegerField()
    no_children = models.IntegerField()
    no_rooms = models.IntegerField()
    dest_city = models.ForeignKey(VisualCity)

    class Meta:
        managed = True
        db_table = 'visual_search'
        app_label = 'visual'
        

class VisualDateInfo(models.Model):
    date_time = models.DateTimeField()
    length_of_stay = models.IntegerField()
    booking_window = models.IntegerField()
    arrive = models.DateField(blank=True, null=True)
    leave = models.DateField(blank=True, null=True)
    search = models.ForeignKey(VisualSearch, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visual_date_info'
        app_label = 'visual'

class VisualHotel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    a_name = models.CharField(max_length=20, blank=True, null=True)
    star_rating = models.IntegerField(blank=True, null=True)
    independent = models.NullBooleanField()
    desirability = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    country = models.ForeignKey(VisualCountry, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visual_hotel'
        app_label = 'visual'


class VisualSearchResult(models.Model):
    rank_pos = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promo_flag = models.BooleanField()
    affinity_score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    if_clicked = models.BooleanField()
    short_stay_sat = models.BooleanField()
    prop_review_score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    random_bool = models.BooleanField()
    hotel_id = models.IntegerField()
    search_id = models.IntegerField()
    site = models.ForeignKey(VisualSite, blank=True, null=True)
    booking_bool = models.NullBooleanField()
    total_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hist_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visual_search_result'
        app_label = 'visual'


class VisualVisitor(models.Model):
    dist_to_dest = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mean_star_rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mean_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    country = models.ForeignKey(VisualCountry)
    search = models.ForeignKey(VisualSearch)

    class Meta:
        managed = True
        db_table = 'visual_visitor'
        app_label = 'visual'
