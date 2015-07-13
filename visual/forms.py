from django import forms

class SearchForm(forms.Form):
    star_rating = forms.IntegerField(min_value=0, max_value=5)
    no_of_adults = forms.IntegerField(min_value=1, max_value=9)
    no_of_children = forms.IntegerField(min_value=0, max_value=9)
    no_of_rooms = forms.IntegerField(min_value = 0, max_value = 10)
    price_dollars = forms.FloatField(min_value=0, max_value=1.97e7)
    length_of_stay = forms.IntegerField(min_value=0, max_value=59)
      
      #destination/city id
