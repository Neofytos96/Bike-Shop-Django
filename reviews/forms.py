from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Review


class ReviewCreateForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'comment', 'pub_date']
    

    def clean_user_name(self):
    	return user_name


    def clen_comment(self):
    	return comment

    def clean_pub_date():
    	return pub_date
