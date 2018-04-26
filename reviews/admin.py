from django.contrib import admin

from .models import Bike, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('bike', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Bike)
admin.site.register(Review, ReviewAdmin)