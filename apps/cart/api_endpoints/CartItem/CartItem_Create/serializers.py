from rest_framework import serializers

from apps.store.models.product import Product


class CartItemNoAuthCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        id = attrs.get('id')
        if id not in Product.objects.all().values_list('id', flat=True):
            raise serializers.ValidationError('Such product doesn\'t exist.')
        return attrs
