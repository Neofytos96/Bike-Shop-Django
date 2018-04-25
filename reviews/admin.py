from django.contrib import admin
from .models import Review, ReviewItem


class ReviewItemInline(admin.TabularInline):
    model = ReviewItem
    raw_id_fields = ['bike']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'pub_date', 'bike']
    list_filter = ['review', 'pub_date', 'bike']
    inlines = [ReviewItemInline]
    
admin.site.register(Review, ReviewAdmin)
