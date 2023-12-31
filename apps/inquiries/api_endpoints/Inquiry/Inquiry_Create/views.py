from os import getenv

from asgiref.sync import async_to_sync
from rest_framework.generics import CreateAPIView
from telegram import Bot
from telegram.error import NetworkError

from apps.users.models import TelegramUser
from .serializers import InquiryCreateSerializer


class InquiryCreateAPIView(CreateAPIView):
    serializer_class = InquiryCreateSerializer

    @staticmethod
    def send_message_to_users(message):
        bot = Bot(token=getenv('BOT_TOKEN'))
        for user in TelegramUser.objects.filter(active=True):
            async_to_sync(bot.send_message)(chat_id=user.chat_id, text=message)

    def perform_create(self, serializer):
        q = serializer.save()
        if q.on_collection:
            product_details = f"ID: {q.on_collection.pk}, Название: {q.on_collection.title}"
            message = f"Новый запрос:\n\nПолное имя: {q.full_name}\nТелефон: {q.phone_number}\nПочта: {q.email}\n{product_details}"
        else:
            message = f"Новый запрос:\n\nПолное имя: {q.full_name}\nТелефон: {q.phone_number}\nПочта: {q.email}"
        try:
            self.send_message_to_users(message)
        except NetworkError as e:
            if 'Event loop is closed' in str(e):
                pass
            else:
                raise ValueError('Some error happened which is not that Event loop closed error!')

# TODO: botga xabar jo'natadigan qismi celery orqali bo'lishi kerak
