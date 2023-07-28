from os import getenv

from rest_framework.generics import CreateAPIView
from telegram import Bot

from apps.users.models import TelegramUser
from .serializers import InquiryCreateSerializer


class InquiryCreateAPIView(CreateAPIView):
    serializer_class = InquiryCreateSerializer

    def perform_create(self, serializer):
        q = serializer.save()
        bot = Bot(token=getenv('BOT_TOKEN'))
        message = f"New Inquiry:\n\nName: {q.full_name}\nNumber: {q.phone_number}\nEmail: {q.email}"
        for user in TelegramUser.objects.filter(active=True):
            bot.send_message(chat_id=user.chat_id, text=message)

# TODO: botga xabar jo'natadigan qismi celery orqali bo'lishi kerak
