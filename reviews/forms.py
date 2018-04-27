from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Review


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user_name', 'comment', 'pub_date')
    

    def clean_user_name(self):
    	user_name = self.cleaned_data['user_name']
    	return user_name


    def clen_comment(self):
    	comment = self.cleaned_data['comment']
    	return comment

    def clean_pub_date():

    	pub_date = self.cleaned_data['pub_date']

    	return pub_date
