from django.conf import settings
from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response


class CartItemNoAuthDeleteAPIView(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        cart = request.session.get(settings.CART_SESSION_ID, None)
        if id in cart:
            del cart[id]
            request.session.modified = True
        return Response(status=status.HTTP_204_NO_CONTENT)


__all__ = ['CartItemNoAuthDeleteAPIView']
