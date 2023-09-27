from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInOrder(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'email', 'delivery_type', 'payment_method', 'final_price', 'status']
    list_display_links = ['id', 'full_name', 'phone_number']
    list_filter = ['payment_method', 'delivery_type']
    inlines = [OrderItemInOrder]
