from django import forms

class searchForm(forms.Form):
	star_rating = forms.decimalField(minvalue=0,maxvalue=5)
	