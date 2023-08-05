from os import getenv
from asgiref.sync import async_to_sync

from rest_framework.generics import CreateAPIView
from telegram import Bot

from apps.users.models import TelegramUser
from .serializers import InquiryCreateSerializer


class InquiryCreateAPIView(CreateAPIView):
    serializer_class = InquiryCreateSerializer

    @staticmethod
    def send_message(message):
        bot = Bot(token=getenv('BOT_TOKEN'))
        for user in TelegramUser.objects.filter(active=True):
            async_to_sync(bot.send_message)(chat_id=user.chat_id, text=message)

    def perform_create(self, serializer):
        q = serializer.save()
        message = f"New Inquiry:\n\nName: {q.full_name}\nNumber: {q.phone_number}\nEmail: {q.email}"
        self.send_message(message)

# TODO: botga xabar jo'natadigan qismi celery orqali bo'lishi kerak
