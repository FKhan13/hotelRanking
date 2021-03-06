from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^contact/', views.ContactView.as_view(), name='contact'),
    url(r'^faq/', views.FaqView.as_view(), name='faq'),
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^(?P<hotel_id>[0-9]+)/$',views.hotel, name='hotel'),
    url(r'^(?P<country>\D+)/search/$',views.search, name='search'),
]

    #url(r'^[0-9]/$', views.play , name='play'),] #temporary url to test bubble view (ex: /visual/[number] : /visual/1)
