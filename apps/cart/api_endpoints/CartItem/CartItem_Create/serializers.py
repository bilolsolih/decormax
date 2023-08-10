from rest_framework.serializers import ModelSerializer, ValidationError

from apps.cart.models import CartItem


class CartItemCreateSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['device_id', 'collection', 'articul', 'quantity']

    def validate(self, data):
        if hasattr(data, 'device_id') and data['device_id'] and self.context['request'].user.is_authenticated:
            raise ValidationError('Authenticated users don\'t have to provide device_id.')
        return data

    def create(self, data):
        user = self.context['request'].user
        if user.is_authenticated:
            item = CartItem.objects.create(
                cart=user.cart, collection=data['collection'], articul=data['articul'], quantity=data['quantity'],
                cost=(data['collection'].price * data['quantity'])
            )
        else:
            item = CartItem.objects.create(
                device_id=data['device_id'], collection=data['collection'], articul=data['articul'], quantity=data['quantity'],
                cost=(data['collection'].price * data['quantity'])
            )
        return item
