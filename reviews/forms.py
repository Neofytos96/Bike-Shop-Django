from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Review
import datetime


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user_name','bike_id','comment', 'rating')

    def clean_bike_id(self):
        bike_id = self.cleaned_data['bike_id']
        return bike_id

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        return user_name
    

    def clen_comment(self):
    	comment = self.cleaned_data['comment']
    	return comment

    

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        return rating
