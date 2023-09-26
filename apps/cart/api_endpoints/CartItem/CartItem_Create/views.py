from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView

from .serializers import CartItemCreateSerializer


@method_decorator(csrf_exempt, name='post')
class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemCreateSerializer


__all__ = ['CartItemCreateAPIView']
