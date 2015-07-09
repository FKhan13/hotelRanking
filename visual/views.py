from django.shortcuts import render
from django.views import generic
from models import VisualCountry, VisualSearch_Result


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
 
def countryNames(country):
    #countries = [country.name for country in VisualCountry.objects.all()]
    #countries = [country.id for country in VisualCountry.objects.all()]
    entry = VisualCountry.objects.get(name = country)
    countid = entry.id
    
    pricelist = [search.price for search in VisualSearch_Result.objects.filter(search_id = countid)]    
    
    return pricelist
    
name = 'Ukraine'
countries = countryNames(name)