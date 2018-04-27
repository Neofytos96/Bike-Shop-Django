from django.contrib import admin
from bikes.models import Bike
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('bike', 'user', 'comment', 'pub_date', 'rating')
    list_filter = ['pub_date', 'user']
    search_fields = ['comment']
    
#admin.site.register(Bike)
admin.site.register(Review, ReviewAdmin)