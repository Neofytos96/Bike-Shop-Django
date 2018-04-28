from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Review
import datetime


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user_name','bike','comment', 'rating')

    def clean_bike(self):
        bike = self.cleaned_data['bike']
        return bike

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        return user_name
    

    def clen_comment(self):
    	comment = self.cleaned_data['comment']
    	return comment

    

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        return rating
