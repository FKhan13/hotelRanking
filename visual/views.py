from django.shortcuts import render
from django.views import generic
#import countryStats
from .models import VisualCountry, VisualSearchResult

from django.http import HttpResponseRedirect
from .forms import SearchForm

class HomeView(generic.TemplateView):
	template_name = "visual/index.html"

class AboutView(generic.TemplateView):
    template_name = "visual/about.html"

class ContactView(generic.TemplateView):
	template_name = "visual/contact.html"

class FaqView(generic.TemplateView):
	template_name = "visual/faq.html"

def country(request, country): 
	return render(request, 'visual/index.html')


def search(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # search for data in the database then return the view that will show the list of hotels that match the search
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'visual/search.html', {'form': form})

name = 'Ukraine'
#countries = countryStats.countryNames(name)