from rest_framework import serializers
from apps.about.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'region', 'district', 'street', 'house_no']
