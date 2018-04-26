from django.forms import Textarea
from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from .models import Review

class ReviewCreateForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ('review')
		widgets = {
            'review': Textarea(attrs={'cols': 40, 'rows': 15})
        }

	