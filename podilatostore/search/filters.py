from django import forms
from django.contrib.auth.models import User, Bike

import django_filters


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    bike = django_filters.CharFilter(lookup_expr='icontains')
    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brands.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'bike', 'brand']