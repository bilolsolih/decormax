from rest_framework.generics import ListAPIView

from apps.about.models import Contact
from .serializers import ContactListSerializer


class ContactListAPIView(ListAPIView):
    serializer_class = ContactListSerializer
    queryset = Contact.objects.all()


__all__ = ['ContactListAPIView']
