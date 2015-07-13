from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import VisualCountry, VisualSearchResult

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
            
            #query DB and whaever else here
            hotel_list = ['mine','mine1', 'mine2', 'mine3','mine','mine1', 'mine2', 'mine3','mine','mine1', 'mine2', 'mine3','mine','mine1', 'mine2', 'mine3','mione','sansjd','sdasd','dasnds'] #Variable that will contain the list of hotels that mathc the search criteria
            
            #paginate the list of hotels
            paginator = Paginator(hotel_list, 10) # Show 10 hotels per page

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

def country(request, country): 
	return render(request, 'visual/country.html')

def play(request):
    
    return render_to_response('visual/play.html', context,RequestContext(request),)
