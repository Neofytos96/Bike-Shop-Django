from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Review
from django.forms import ModelForm, Textarea


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user_name', 'comment', 'pub_date')
        

    def clean_user_name(self):
		user_name = self.cleaned_data['user_name']
		
		#check the user input is only numbers
		if not user_name.replace(" ", "").isalpha():
			raise forms.ValidationError("Card holder name can contain only letters")
		
		return user_name

    

    #def clean_user_name(self):
   # 	return user_name


  #  def clen_comment(self):
  #  	return comment

#    def clean_pub_date():
#    	return pub_date
