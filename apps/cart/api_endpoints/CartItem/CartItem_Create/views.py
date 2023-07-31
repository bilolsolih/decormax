from django.conf import settings
from rest_framework.generics import CreateAPIView
from apps.store.models.product import Product

from .serializers import CartItemNoAuthCreateSerializer


class CartItemNoAuthCreateUpdateAPIView(CreateAPIView):
    serializer_class = CartItemNoAuthCreateSerializer

    def perform_create(self, serializer):
        cart = self.request.session.get(settings.CART_SESSION_ID, None)
        if not cart:
            cart = self.request.session[settings.CART_SESSION_ID] = {}

        id = serializer.validated_data['id']
        quantity = serializer.validated_data['quantity']
        product = Product.objects.filter(pk=id).values('photo', 'price').first()

        if not product:
            raise ValueError('Such product doesn\'t exist.')
        cart[id] = {
            'quantity': quantity,
            'photo': self.request.build_absolute_uri(product['photo']),
            'cost': int(product['price']) * quantity
        }
        self.request.session.modified = True


__all__ = ['CartItemNoAuthCreateUpdateAPIView']
