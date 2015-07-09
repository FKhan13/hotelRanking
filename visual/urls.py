from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^contact/', views.ContactView.as_view(), name='contact'),
    url(r'^faq/', views.FaqView.as_view(), name='faq'),
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^(?P<country>\D+)/$',views.country, name='country'),
]