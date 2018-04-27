from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Review
import datetime


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user','comment', 'rating')

    def clean_user(self):
        user = self.cleaned_data['user']
        return user
    

    def clen_comment(self):
    	comment = self.cleaned_data['comment']
    	return comment

    

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        return rating
