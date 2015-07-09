from django import forms

class SearchForm(forms.Form):
	star_rating = forms.IntegerField(min_value=0,max_value=5)
	review_score = forms.FloatField(min_value=0,max_value=5)
	no_of_adults = forms.IntegerField(min_value=1,max_value=9)
	no_of_children = forms.IntegerField(min_value=0,max_value=9)
	begin_date = forms.SplitDateTimeField()
	end_date = forms.SplitDateTimeField()
