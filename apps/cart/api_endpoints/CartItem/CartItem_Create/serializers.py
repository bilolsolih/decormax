from rest_framework.serializers import ModelSerializer, ValidationError

from apps.cart.models import CartItem
from apps.store.models.product import Product


class CartItemCreateSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['device_id', 'product', 'quantity']

    def validate(self, data):
        if data['device_id'] and self.context['request'].user.is_authenticated:
            raise ValidationError('Authenticated users don\'t have to provide device_id.')
        return data

    def create(self, data):
        user = self.context['request'].user
        product = Product.objects.get(pk=data['product'])
        if user.is_authenticated:
            item = CartItem.objects.create(
                cart=user.cart, product=data['product'], quantity=data['quantity'], cost=(product.price * data['quantity'])
            )
        else:
            item = CartItem.objects.create(
                device_id=data['device_id'], product=data['product'], quantity=data['quantity'], cost=(product.price * data['quantity'])
            )
        return item
