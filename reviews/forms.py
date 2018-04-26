from django.forms import ModelForm, Textarea
#from reviews.models import Review
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from .models import Review

class ReviewCreateForm(ModelForm):

	class Meta:
		model = Review
		fields = ['review']
		widgets = {
            'review': Textarea(attrs={'cols': 40, 'rows': 15})
        }


