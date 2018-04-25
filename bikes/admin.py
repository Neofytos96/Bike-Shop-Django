#adapted from https://github.com/guinslym/django-by-example-book
from django.contrib import admin
from .models import Bike, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand', 'slug']
    prepopulated_fields = {'slug': ('brand',)}
admin.site.register(Brand, BrandAdmin)


class BikeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'brand', 'price', 'stock', 'available', 'release_date']
    list_filter = ['available', 'release_date', 'brand']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Bike, BikeAdmin)

