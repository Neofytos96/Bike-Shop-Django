from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Review


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user_name', 'comment', 'pub_date', 'rating')
    

    def clean_user_name(self):
    	user_name = self.cleaned_data['user_name']
    	return user_name


    def clen_comment(self):
    	comment = self.cleaned_data['comment']
    	return comment

    def clean_pub_date():
        pub_date = self.cleaned_data['pub_date']

        if not datetime.datetime.strptime(pub_date, '%d/%m/%Y'):
            raise forms.ValidationError("Date should be in the format DD/MM/YYYY")
        
        return pub_date

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        return rating
