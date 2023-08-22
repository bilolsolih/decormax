from rest_framework.serializers import ModelSerializer, ValidationError

from apps.cart.models import CartItem


class CartItemCreateSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['device_id', 'collection', 'articul', 'quantity']

    def validate(self, data):
        user = self.context['request'].user
        if "device_id" in data and data['device_id'] and user.is_authenticated:
            raise ValidationError('Authenticated users don\'t have to provide device_id.')

        if "device_id" in data and data['device_id']:
            if CartItem.objects.filter(device_id=data['device_id'], collection=data['collection']).first():
                raise ValidationError('Item already in the cart.')

        if self.context['request'].user.is_authenticated:
            if CartItem.objects.filter(cart=user.cart, collection=data['collection']).first():
                raise ValidationError('Item already in the cart.')
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
                device_id=data['device_id'], collection=data['collection'], articul=data['articul'],
                quantity=data['quantity'],
                cost=(data['collection'].price * data['quantity'])
            )
        return item
