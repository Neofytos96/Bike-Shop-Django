from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['bike']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_number', 'cardholder_name', 'expiry_date', 'CVV_code', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    
admin.site.register(Order, OrderAdmin)
