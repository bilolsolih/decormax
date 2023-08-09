from django.conf import settings
from rest_framework.generics import CreateAPIView

from .serializers import CartItemNoAuthCreateSerializer


class CartItemNoAuthCreateAPIView(CreateAPIView):
    serializer_class = CartItemNoAuthCreateSerializer

    def perform_create(self, serializer):
        cart = self.request.session.get(settings.CART_SESSION_ID, None)
        if not cart:
            cart = self.request.session[settings.CART_SESSION_ID] = {}
        id = serializer.validated_data['id']
        price = serializer.validated_data['price']
        quantity = serializer.validated_data['quantity']
        if id not in cart:
            cart[id] = {
                'quantity': quantity,
                'price': price
            }


__all__ = ['CartItemNoAuthCreateAPIView']
