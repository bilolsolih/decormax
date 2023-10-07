import requests
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

        if user:
            items = CartItem.objects.filter(cart__user=user)
        else:
            items = CartItem.objects.filter(device_id=device_id)

        if not items:
            raise ValueError('Your cart is empty, you cannot create an order!')

        final_price = items.aggregate(final_price=Sum('cost'))['final_price']
        order = serializer.save(user=user, final_price=final_price)
        for item in items:
            OrderItem.objects.create(order=order, collection=item.collection, artikul=item.articul,
                                     quantity=item.quantity, cost=item.cost)
            item.delete()

        photo_path = []
        order_items = OrderItem.objects.all(order=order)
        for item in order_items:
            photo_path.append(item.artikul.photo.path)
        photos = [('photo', open(path, 'rb')) for path in photo_path]
        order_message = f"Order {order.id}:\n"
        order_message += f"Full Name: {order.full_name}\n"
        order_message += f"Phone Number: {order.phone_number}\n"
        order_message += f"Email: {order.email}\n"
        order_message += f"Способ доставки: {order.delivery_type}\n"
        order_message += f"Способ оплаты: {order.payment_method}\n"
        order_message += f"Цена: {order.final_price}\n"
        order_message += f"Город: {order.city}\n"
        order_message += f"Регион: {order.region}\n"
        order_message += f"Адрес: {order.address}\n"
        order_message += f"Этаж: {order.level}\n"
        order_message += f"Дата доставки: {order.delivery_date}\n"
        telegram_bot_token = '6619661511:AAFbb2HydLQNVdIqkzh6slLUsxWvKM0xxQI'
        chat_id = '-1001920070201'

        response = requests.post(
            f"https://api.telegram.org/bot{telegram_bot_token}/sendPhoto",
            data={'chat_id': chat_id, 'caption': order_message},
            files=photos
        )
        if response.status_code != 200:
            pass


__all__ = ['OrderCreateAPIView']
