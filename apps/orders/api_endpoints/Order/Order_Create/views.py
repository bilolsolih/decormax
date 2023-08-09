from django.db.models.aggregates import Sum
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView

from apps.cart.models import CartItem
from apps.orders.models import OrderItem
from .serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('device_id', openapi.IN_QUERY, description='Device id', type=openapi.TYPE_STRING),
        ]
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        device_id = self.request.query_params.get('device_id', None)
        if user and device_id:
            raise ValueError('device_id is needed only for guest users.')
        if user:
            items = CartItem.objects.filter(cart__user=user)
        else:
            items = CartItem.objects.filter(device_id=device_id)

        if not items:
            raise ValueError('Your cart is empty, you cannot create an order!')

        final_price = items.aggregate(final_price=Sum('cost'))['final_price']
        order = serializer.save(user=user, final_price=final_price)
        for item in items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, cost=item.cost)
            item.delete()


__all__ = ['OrderCreateAPIView']
