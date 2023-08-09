from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class CartItemNoAuthListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if not request.session.get(settings.CART_SESSION_ID, None):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(request.session.get(settings.CART_SESSION_ID, None))


__all__ = ['CartItemNoAuthListAPIView']
