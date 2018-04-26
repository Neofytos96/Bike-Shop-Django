from django.contrib import admin
from bikes.models import Bike
from .models import Review, ReviewItem


#class OrderItemInline(admin.TabularInline):
#    model = ReviewItem
#    raw_id_fields = ['bike']

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('bike', 'user_name', 'comment', 'pub_date', 'created')
    list_filter = ['pub_date', 'user_name ', 'created']
    search_fields = ['comment']
    
#admin.site.register(Bike)
admin.site.register(Review, ReviewAdmin)