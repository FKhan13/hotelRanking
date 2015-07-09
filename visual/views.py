from django.shortcuts import render
from django.views import generic

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