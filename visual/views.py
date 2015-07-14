from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time, datetime,json,os
from .models import *
from django.http import HttpResponseRedirect, Http404
from .forms import SearchForm

class HomeView(generic.TemplateView):
	template_name = "visual/index.html"

class AboutView(generic.TemplateView):
    template_name = "visual/about.html"

class ContactView(generic.TemplateView):
	template_name = "visual/contact.html"

class FaqView(generic.TemplateView):
	template_name = "visual/faq.html"

def search(request,country):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # search for data in the database then return the view that will show the list of hotels that match the search
            # process the data in form.cleaned_data as required

            ##############################################################################
            n_o_a = form.cleaned_data['no_of_adults']
            n_o_c = form.cleaned_data['no_of_children']
            n_o_r = form.cleaned_data['no_of_rooms']
            star_rate = form.cleaned_data['star_rating']
            stay_len = form.cleaned_data['length_of_stay']
            priceVal = form.cleaned_data['price_dollars']
            ##############################################################################

            searchids1 = []
            searchids2 = []
            searchids = []
            hotelids = []
            result = []

            country = country.replace('_', ' ')
            # get country
            objectCountry = VisualCountry.objects.get(name = country)
            countryid = objectCountry.id

            #sorts out no of adult, children, rooms get list of searchids
            objects1 = VisualSearch.objects.filter(no_adults = n_o_a).filter(no_children = n_o_c).filter(no_rooms = n_o_r) 
            for search in objects1:
                searchids1.append(search.id)

            #sorts out length of stay gets list of searchids
            objects2 = VisualDateInfo.objects.filter(length_of_stay = stay_len)
            for search in objects2:
                searchids2.append(search.search_id)

            #refine search ids list
            searchids = list(set(searchids1)&set(searchids2))

            #sorts out star rating and country get list of hotels
            objects2 = VisualHotel.objects.filter(star_rating = star_rate, country_id = countryid )
            for search in objects2:
                hotelids.append(search.id)

            # get the hottels with all specifications
            if not hotelids:
                objects3 = VisualSearchResult.objects.filter(search_id__in=searchids)
            elif not searchids:
                objects3 = VisualSearchResult.objects.filter(hotel_id__in=hotelids)
            else:
                objects3 = VisualSearchResult.objects.filter(search_id__in=searchids).filter(hotel_id__in=hotelids)
    
            newobj = objects3[0:5]
            for search in newobj:
                result.append(search.hotel_id)
            
            #paginate the list of hotels
            paginator = Paginator(result, 5) # Show 5 hotels per page

            page = request.GET.get('page')
            try:
                hotels = paginator.page(page)
            except PageNotAnInteger:
            # If page is not an integer, deliver first page.
                hotels = paginator.page(1)
            except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
                hotels = paginator.page(paginator.num_pages)
            
            # redirect to a new URL: Should be the list.html template
            return render_to_response('visual/list.html', {"hotels": hotels})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
    
    return render(request, 'visual/search.html', {'form': form})

def hotel(request,hotel_id):
    return render(request, 'visual/hotel.html')

def play(request):
    context = {"helo": "This is a hello message oooh yeah"}
    return render_to_response('visual/play.html', context,RequestContext(request),)
