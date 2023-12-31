from rest_framework import serializers

from apps.orders.models import Order


class OrderRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'full_name', 'phone_number', 'email', 'delivery_type', 'payment_method', 'final_price', 'created',
            'status', 'items', 'city', 'region', 'address', 'level', 'delivery_date', 'get_collection_articuls'
        ]
        depth = 1
