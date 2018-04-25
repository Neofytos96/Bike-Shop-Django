#adapted from https://github.com/guinslym/django-by-example-book
from django.contrib import admin
from .models import Bike, Brand, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    prepopulated_fields = {'slug': ('category',)}
admin.site.register(Category, CategoryAdmin)


class BikeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'brands', 'category', 'price', 'stock', 'available', 'release_date']
    list_filter = ['available', 'release_date', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Bike, BikeAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug']
    prepopulated_fields = {'slug': ('last_name',)}
admin.site.register(Brand, BrandAdmin)
