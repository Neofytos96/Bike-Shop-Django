#adapted from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, required=False)
    address = forms.CharField(max_length=30, required=False)
    city = forms.CharField(max_length=30, required=False)
    postCode = forms.CharField(max_length=30, required=False)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'city', 'postCode', 'password1', 'password2' )
        