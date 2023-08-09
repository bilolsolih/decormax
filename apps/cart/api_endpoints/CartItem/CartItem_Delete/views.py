from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import DestroyAPIView

from apps.cart.models import CartItem


class CartItemDeleteAPIView(DestroyAPIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('device_id', openapi.IN_QUERY, description='Device id', type=openapi.TYPE_STRING),
        ]
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        device_id = self.request.query_params.get('device_id', None)
        if user.is_authenticated and device_id:
            raise ValueError('device_id is needed only for guest users.')
        if user.is_authenticated:
            return CartItem.objects.filter(cart__user=user)
        else:
            return CartItem.objects.filter(device_id=device_id)


__all__ = ['CartItemDeleteAPIView']
